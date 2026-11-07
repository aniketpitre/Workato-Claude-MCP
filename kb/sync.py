#!/usr/bin/env python3
"""Sync Workato's official documentation into a local Markdown knowledge base.

Sources (all first-party, published by Workato for LLM consumption):
  * https://docs.workato.com/llms.txt       - index of every page (title, section, description)
  * https://docs.workato.com/llms-full.txt  - most pages' Markdown in a single file
  * https://docs.workato.com/<page>.md      - per-page Markdown (for pages missing from llms-full)
  * https://docs.workato.com/sitemap.xml    - per-page last-modified dates (incremental sync)

Output:
  kb/docs/en/**.md        one Markdown file per docs page (with YAML front matter)
  kb/manifest.json        url, path, title, section, description, lastmod, sha256 per page
  kb/last_sync.json       what changed on the most recent sync
  kb/CHANGELOG.md         running log of added/changed/removed pages
  kb/INDEX.md             table of contents: sections -> kb/index/<section>.md
  kb/index/*.md           per-section page lists (title, path, one-line description)

Only the standard library is used, so this runs anywhere Python 3.9+ is available.

Usage:
  python kb/sync.py            # incremental: only re-download pages whose lastmod moved
  python kb/sync.py --full     # re-download every page
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE = "https://docs.workato.com"
KB_DIR = Path(__file__).resolve().parent
DOCS_DIR = KB_DIR / "docs"
MANIFEST = KB_DIR / "manifest.json"
LAST_SYNC = KB_DIR / "last_sync.json"
CHANGELOG = KB_DIR / "CHANGELOG.md"
USER_AGENT = "workato-claude-kb-sync/1.0 (+https://github.com/aniketpitre/Workato-Claude-MCP)"


# --------------------------------------------------------------------------- http
def fetch(url: str, retries: int = 4, timeout: int = 120) -> str:
    last: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise
            last = e
        except Exception as e:  # network hiccup
            last = e
        time.sleep(2 ** attempt)
    raise RuntimeError(f"failed to fetch {url}: {last}")


# ------------------------------------------------------------------------ parsing
LINK_RE = re.compile(r"^\s*-\s*\[(?P<title>[^\]]+)\]\((?P<url>https://docs\.workato\.com/[^)\s]+\.md)\)(?::\s*(?P<desc>.*))?$")


def parse_llms_index(text: str) -> dict[str, dict]:
    """Return {url: {title, section, subsection, description}} from llms.txt."""
    pages: dict[str, dict] = {}
    section = subsection = ""
    for line in text.splitlines():
        if line.startswith("### "):
            section, subsection = line[4:].strip(), ""
        elif line.startswith("#### "):
            subsection = line[5:].strip()
        else:
            m = LINK_RE.match(line)
            if m and "/en/" in m["url"]:
                pages.setdefault(m["url"], {
                    "title": m["title"].strip(),
                    "section": section,
                    "subsection": subsection,
                    "description": (m["desc"] or "").strip(),
                })
    return pages


PAGE_SPLIT_RE = re.compile(r"^---\nurl: '(https://docs\.workato\.com/[^']+)'\n", re.M)


def split_llms_full(text: str) -> dict[str, str]:
    """Split llms-full.txt into {url: markdown_including_front_matter}."""
    out: dict[str, str] = {}
    matches = list(PAGE_SPLIT_RE.finditer(text))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out[m.group(1)] = text[m.start():end].rstrip() + "\n"
    return out


def parse_sitemap(text: str) -> dict[str, str]:
    """Return {md_url: lastmod} for English pages."""
    out: dict[str, str] = {}
    for m in re.finditer(r"<url><loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>", text):
        loc, lastmod = m.group(1), m.group(2)
        if "/en/" not in loc:
            continue
        loc = re.sub(r"\.html$", "", loc).rstrip("/")
        out[loc + ".md"] = lastmod
    return out


def url_to_path(url: str) -> Path:
    rel = url[len(BASE):].lstrip("/")
    return DOCS_DIR / rel


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def ensure_front_matter(url: str, body: str, meta: dict) -> str:
    if body.startswith("---\n"):
        return body
    desc = meta.get("description", "").replace("'", "''")
    return f"---\nurl: '{url}'\ndescription: '{desc}'\n---\n\n{body.lstrip()}"


# --------------------------------------------------------------------------- sync
def sync(full: bool = False, workers: int = 12, verbose: bool = True) -> dict:
    log = (lambda *a: print(*a, file=sys.stderr)) if verbose else (lambda *a: None)
    started = dt.datetime.now(dt.timezone.utc)

    old: dict[str, dict] = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}

    log("fetching llms.txt index ...")
    index = parse_llms_index(fetch(f"{BASE}/llms.txt"))
    log(f"  {len(index)} English pages listed")

    log("fetching sitemap.xml ...")
    try:
        lastmods = parse_sitemap(fetch(f"{BASE}/sitemap.xml"))
    except Exception as e:  # sitemap is a nice-to-have
        log(f"  sitemap unavailable ({e}); falling back to content hashes")
        lastmods = {}

    log("fetching llms-full.txt bundle ...")
    bundle = split_llms_full(fetch(f"{BASE}/llms-full.txt", timeout=300))
    log(f"  {len(bundle)} pages in bundle")

    # Pages present in the bundle but missing from the index still get stored.
    for url in bundle:
        if url not in index and "/en/" in url:
            index[url] = {"title": url.rsplit("/", 1)[-1][:-3], "section": "Other", "subsection": "", "description": ""}

    contents: dict[str, str] = {}
    to_fetch: list[str] = []
    for url in index:
        if url in bundle:
            contents[url] = bundle[url]
            continue
        prev = old.get(url)
        path = url_to_path(url)
        unchanged = prev and lastmods.get(url) and prev.get("lastmod") == lastmods.get(url)
        if not full and unchanged and path.exists():
            contents[url] = path.read_text(encoding="utf-8")
        else:
            to_fetch.append(url)

    log(f"fetching {len(to_fetch)} individual pages ...")
    failed: list[str] = []
    missing: list[str] = []

    def _get(u: str) -> tuple[str, str | None, str | None]:
        try:
            return u, fetch(u), None
        except urllib.error.HTTPError as e:
            return u, None, f"http {e.code}"
        except Exception as e:
            return u, None, str(e)

    with cf.ThreadPoolExecutor(max_workers=workers) as pool:
        for n, (u, text, err) in enumerate(pool.map(_get, to_fetch), 1):
            if text is not None:
                contents[u] = text
            elif err == "http 404":
                missing.append(u)
            else:
                failed.append(u)
                # keep the previous copy rather than dropping knowledge on a transient error
                p = url_to_path(u)
                if p.exists():
                    contents[u] = p.read_text(encoding="utf-8")
            if n % 200 == 0:
                log(f"  {n}/{len(to_fetch)}")

    # ------------------------------------------------------------- write files
    new_manifest: dict[str, dict] = {}
    added, changed = [], []
    for url, body in sorted(contents.items()):
        meta = index.get(url, {})
        body = ensure_front_matter(url, body, meta)
        digest = sha(body)
        path = url_to_path(url)
        prev = old.get(url)
        if not prev or not path.exists():
            added.append(url)
        elif prev.get("sha256") != digest:
            changed.append(url)
        if not path.exists() or (prev or {}).get("sha256") != digest:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(body, encoding="utf-8")
        new_manifest[url] = {
            "path": str(path.relative_to(KB_DIR.parent)),
            "title": meta.get("title", ""),
            "section": meta.get("section", ""),
            "subsection": meta.get("subsection", ""),
            "description": meta.get("description", ""),
            "lastmod": lastmods.get(url, (prev or {}).get("lastmod", "")),
            "sha256": digest,
            "chars": len(body),
        }

    removed = sorted(u for u in old if u not in new_manifest and u not in failed)
    for u in removed:
        p = url_to_path(u)
        if p.exists():
            p.unlink()
    # tidy empty directories
    for d in sorted(DOCS_DIR.rglob("*"), key=lambda p: len(p.parts), reverse=True):
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()

    MANIFEST.write_text(json.dumps(new_manifest, indent=1, sort_keys=True) + "\n")
    write_indexes(new_manifest)

    report = {
        "synced_at": started.isoformat(timespec="seconds"),
        "mode": "full" if full else "incremental",
        "pages": len(new_manifest),
        "from_bundle": sum(1 for u in new_manifest if u in bundle),
        "fetched_individually": len(to_fetch) - len(failed) - len(missing),
        "added": added if old else [],
        "added_count": len(added),
        "changed": changed,
        "removed": removed,
        "failed": failed,
        "not_found": missing,
    }
    LAST_SYNC.write_text(json.dumps(report, indent=1) + "\n")
    _append_changelog(report, first_run=not old)
    log(f"done: {len(new_manifest)} pages | +{len(added)} ~{len(changed)} -{len(removed)} | "
        f"failed {len(failed)} | 404 {len(missing)}")
    return report


def _slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "other"


def write_indexes(manifest: dict[str, dict]) -> None:
    """Write kb/INDEX.md and kb/index/<section>.md so the KB is browsable as plain files."""
    idx_dir = KB_DIR / "index"
    idx_dir.mkdir(exist_ok=True)
    by_section: dict[str, list[dict]] = {}
    for url, m in manifest.items():
        by_section.setdefault(m.get("section") or "Other", []).append({**m, "url": url})
    for f in idx_dir.glob("*.md"):
        f.unlink()
    top = ["# Workato documentation knowledge base - index", "",
           "Generated by `kb/sync.py` from docs.workato.com. Do not edit by hand.", "",
           "Search: `python3 kb/search.py \"<query>\"`. Read a page: open its path below.", "",
           "| Section | Pages | Index |", "| --- | ---: | --- |"]
    for section in sorted(by_section, key=lambda k: -len(by_section[k])):
        pages = sorted(by_section[section], key=lambda m: (m.get("subsection") or "", m["path"]))
        fname = f"{_slug(section)}.md"
        top.append(f"| {section} | {len(pages)} | [index/{fname}](index/{fname}) |")
        lines = [f"# {section}", "", f"{len(pages)} pages. Paths are relative to the repository root.", ""]
        current = None
        for m in pages:
            sub = m.get("subsection") or ""
            if sub != current:
                current = sub
                lines += ["", f"## {sub or section}", ""]
            desc = (m.get("description") or "").replace("\n", " ")
            lines.append(f"- **{m['title']}** - `{m['path']}`" + (f" - {desc[:200]}" if desc else ""))
        (idx_dir / fname).write_text("\n".join(lines) + "\n")
    (KB_DIR / "INDEX.md").write_text("\n".join(top) + "\n")


def _append_changelog(r: dict, first_run: bool) -> None:
    if not first_run and not (r["added"] or r["changed"] or r["removed"]):
        return
    lines = [f"## {r['synced_at']} ({r['mode']})", "",
             f"- Pages: {r['pages']} | added {r['added_count']} | changed {len(r['changed'])} | removed {len(r['removed'])}"]
    if not first_run:
        for label, key in (("Added", "added"), ("Changed", "changed"), ("Removed", "removed")):
            items = r[key]
            if items:
                lines.append(f"- {label}:")
                lines += [f"  - {u}" for u in items[:50]]
                if len(items) > 50:
                    lines.append(f"  - ... and {len(items) - 50} more")
    else:
        lines.append("- Initial import of the Workato documentation.")
    entry = "\n".join(lines) + "\n\n"
    header = "# Workato docs knowledge base - change log\n\n"
    prev = CHANGELOG.read_text().removeprefix(header) if CHANGELOG.exists() else ""
    CHANGELOG.write_text(header + entry + prev)


if __name__ == "__main__" and "--index-only" in sys.argv:
    write_indexes(json.loads(MANIFEST.read_text()))
    sys.exit(0)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--full", action="store_true", help="re-download every page")
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()
    rep = sync(full=args.full, workers=args.workers, verbose=not args.quiet)
    sys.exit(1 if rep["failed"] and len(rep["failed"]) > 50 else 0)
