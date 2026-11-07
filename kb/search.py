#!/usr/bin/env python3
"""Full-text search over the local Workato docs knowledge base (SQLite FTS5, stdlib only).

Usage:
  python3 kb/search.py "recipe function call"            # ranked pages + matching headings
  python3 kb/search.py "hashed token" --section MCP -n 5   # restrict to a docs section
  python3 kb/search.py --read en/recipes/building-recipes [--heading "Triggers"]
  python3 kb/search.py --sections                          # list docs sections and page counts
  python3 kb/search.py --examples salesforce.search_sobjects [--feature try]   # real recipes using a step
  python3 kb/search.py --connector slack [--op post_message_to_channel]        # live catalog schema


The index (kb/index.sqlite) is a build artifact: it is rebuilt automatically whenever
kb/manifest.json is newer than the index, so `git pull` or `kb/sync.py` is all you need.
"""
from __future__ import annotations

import json
import re
import sqlite3
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KB_DIR = ROOT / "kb"
MANIFEST = KB_DIR / "manifest.json"
INDEX = KB_DIR / "index.sqlite"
DOCS_BASE = "https://docs.workato.com"

_lock = threading.Lock()
FRONT_MATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.S)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$", re.M)


def _strip_front_matter(text: str) -> str:
    return FRONT_MATTER_RE.sub("", text, count=1)


def _chunks(body: str, target: int = 2500) -> list[tuple[str, str]]:
    """Split a page into (heading, text) chunks along headings so search hits are precise."""
    parts: list[tuple[str, str]] = []
    positions = [(m.start(), m.group(2).strip()) for m in HEADING_RE.finditer(body)]
    if not positions or positions[0][0] != 0:
        positions.insert(0, (0, ""))
    for i, (start, heading) in enumerate(positions):
        end = positions[i + 1][0] if i + 1 < len(positions) else len(body)
        text = body[start:end].strip()
        if not text:
            continue
        # merge tiny sections into the previous chunk
        if parts and len(parts[-1][1]) + len(text) < target and len(text) < 400:
            parts[-1] = (parts[-1][0], parts[-1][1] + "\n\n" + text)
        else:
            parts.append((heading, text))
    return parts or [("", body)]


def needs_rebuild() -> bool:
    return not INDEX.exists() or (MANIFEST.exists() and MANIFEST.stat().st_mtime > INDEX.stat().st_mtime)


def build(force: bool = False) -> int:
    with _lock:
        if not force and not needs_rebuild():
            return -1
        manifest = json.loads(MANIFEST.read_text())
        tmp = INDEX.with_suffix(".tmp")
        tmp.unlink(missing_ok=True)
        con = sqlite3.connect(tmp)
        con.executescript(
            """
            CREATE VIRTUAL TABLE chunks USING fts5(
                title, section, heading, description, body,
                url UNINDEXED, path UNINDEXED, chunk UNINDEXED,
                tokenize = 'porter unicode61'
            );
            """
        )
        rows = 0
        for url, meta in manifest.items():
            p = ROOT / meta["path"]
            if not p.exists():
                continue
            body = _strip_front_matter(p.read_text(encoding="utf-8"))
            section = " / ".join(x for x in (meta.get("section"), meta.get("subsection")) if x)
            for n, (heading, text) in enumerate(_chunks(body)):
                con.execute(
                    "INSERT INTO chunks VALUES (?,?,?,?,?,?,?,?)",
                    (meta.get("title", ""), section, heading, meta.get("description", ""), text, url, meta["path"], n),
                )
                rows += 1
        con.commit()
        con.close()
        tmp.replace(INDEX)
        return rows


def _connect() -> sqlite3.Connection:
    if needs_rebuild():
        build()
    return sqlite3.connect(f"file:{INDEX}?mode=ro", uri=True)


STOPWORDS = set("a an and are as at be by can do does for from how i in is it of on or the to via what when where which with you your".split())


def _fts_query(q: str, mode: str = "AND") -> str:
    """Turn free text into a forgiving FTS5 query (quoted terms joined by AND/OR, phrases kept)."""
    phrases = re.findall(r'"([^"]+)"', q)
    rest = re.sub(r'"[^"]+"', " ", q)
    terms = [t for t in re.findall(r"[\w\-\.]+", rest) if len(t) > 1 and t.lower() not in STOPWORDS]
    parts = [f'"{p}"' for p in phrases] + ['"' + t.replace('"', "") + '"' for t in terms]
    return f" {mode} ".join(parts) if parts else '""'


def search(query: str, limit: int = 8, section: str | None = None) -> list[dict]:
    """Rank pages by BM25 (title and headings weighted highest). Tries all-terms match first,
    then tops up with any-term matches so vague queries still return something useful."""
    con = _connect()
    try:
        seen: dict[str, dict] = {}
        for mode in ("AND", "OR"):
            if len(seen) >= limit:
                break
            sql = (
                "SELECT title, section, heading, url, path, "
                "snippet(chunks, 4, '**', '**', ' ... ', 40) AS snip, "
                "bm25(chunks, 12.0, 2.0, 6.0, 4.0, 1.0) AS score "
                "FROM chunks WHERE chunks MATCH ?"
            )
            args: list = [_fts_query(query, mode)]
            if section:
                sql += " AND section LIKE ?"
                args.append(f"%{section}%")
            sql += " ORDER BY score LIMIT ?"
            args.append(max(limit * 5, 25))
            for title, sec, heading, url, path, snip, _score in con.execute(sql, args):
                if url in seen:  # one result per page; remember extra matched headings
                    hs = seen[url]["matched_headings"]
                    if heading and heading not in hs and len(hs) < 5:
                        hs.append(heading)
                    continue
                if len(seen) >= limit:
                    continue
                seen[url] = {
                    "title": title, "section": sec, "url": url.removesuffix(".md"), "path": path,
                    "matched_headings": [heading] if heading else [], "snippet": snip,
                }
        return list(seen.values())
    finally:
        con.close()


def resolve_path(ref: str) -> Path | None:
    """Accept a repo path, a docs URL (with or without .md/.html), or a docs-relative path."""
    ref = ref.strip()
    if ref.startswith("http"):
        ref = ref.split("#", 1)[0].split("?", 1)[0]
        ref = re.sub(r"\.html$", "", ref).removesuffix(".md").removeprefix(DOCS_BASE)
        ref = "kb/docs" + ref + ".md"
    candidates = [ref, f"kb/docs/{ref.lstrip('/')}", f"kb/docs/en/{ref.lstrip('/')}"]
    for c in list(candidates):
        if not c.endswith(".md"):
            candidates.append(c + ".md")
    for c in candidates:
        p = (ROOT / c).resolve()
        if p.is_file() and KB_DIR in p.parents:
            return p
    return None


def read(ref: str, heading: str | None = None, offset: int = 0, max_chars: int = 20000) -> dict:
    p = resolve_path(ref)
    if not p:
        return {"error": f"page not found: {ref}. Use kb_search to find the right path."}
    text = p.read_text(encoding="utf-8")
    headings = [m.group(0) for m in HEADING_RE.finditer(_strip_front_matter(text))]
    if heading:
        body = _strip_front_matter(text)
        ms = list(HEADING_RE.finditer(body))
        hit = next((m for m in ms if heading.lower() in m.group(2).lower()), None)
        if not hit:
            return {"error": f"heading '{heading}' not found", "headings": headings}
        level = len(hit.group(1))
        nxt = next((m for m in ms if m.start() > hit.start() and len(m.group(1)) <= level), None)
        text = body[hit.start(): nxt.start() if nxt else len(body)]
    chunk = text[offset: offset + max_chars]
    return {
        "path": str(p.relative_to(ROOT)),
        "total_chars": len(text),
        "offset": offset,
        "truncated": offset + max_chars < len(text),
        "next_offset": offset + max_chars if offset + max_chars < len(text) else None,
        "headings": headings if len(text) > max_chars and not heading else None,
        "content": chunk,
    }


def sections() -> dict[str, int]:
    manifest = json.loads(MANIFEST.read_text())
    out: dict[str, int] = {}
    for meta in manifest.values():
        out[meta.get("section") or "Other"] = out.get(meta.get("section") or "Other", 0) + 1
    return dict(sorted(out.items(), key=lambda kv: -kv[1]))


def list_pages(section: str, subsection: str | None = None, limit: int = 200) -> list[dict]:
    manifest = json.loads(MANIFEST.read_text())
    out = []
    for url, m in sorted(manifest.items()):
        if section.lower() not in (m.get("section") or "").lower():
            continue
        if subsection and subsection.lower() not in (m.get("subsection") or "").lower():
            continue
        out.append({"title": m["title"], "subsection": m.get("subsection"), "path": m["path"], "description": m["description"]})
    return out[:limit]


def find_examples(step: str | None, feature: str | None, limit: int) -> list[dict]:
    rows = json.loads((ROOT / "kb" / "examples" / "index.json").read_text())
    out = []
    for r in rows:
        if step and not any(s == step or s.startswith(step + ".") or step in s for s in r["steps"]):
            continue
        if feature and feature not in r["features"]:
            continue
        out.append(r)
    rank = {"labs-template": 0, "labs-sample": 1, "workspace": 2, "community": 3}
    out.sort(key=lambda r: (rank.get(r["source"], 9), -r.get("copies", 0), len(r["steps"])))
    return out[:limit]


def connector(name: str, op: str | None) -> dict:
    p = ROOT / "kb" / "connectors" / "catalog" / f"{name}.json"
    if not p.exists():
        idx = json.loads((ROOT / "kb" / "connectors" / "catalog.json").read_text())
        near = [k for k, v in idx.items() if name.lower() in k or name.lower() in (v.get("title") or "").lower()]
        return {"error": f"connector '{name}' not in catalog", "did_you_mean": near[:15]}
    c = json.loads(p.read_text())
    if not op:
        return {"name": c["name"], "title": c["title"], "requires_connection": c.get("requires_connection"),
                "triggers": [(t["name"], t.get("title")) for t in c["triggers"]],
                "actions": [(a["name"], a.get("title")) for a in c["actions"]]}
    for kind in ("triggers", "actions"):
        for o in c[kind]:
            if o["name"] == op:
                return {"connector": name, "kind": kind[:-1], **o}
    return {"error": f"operation '{op}' not found", "available": [o["name"] for k in ("triggers", "actions") for o in c[k]]}


def main() -> None:
    import argparse
    ap = argparse.ArgumentParser(description="Search the local Workato docs knowledge base")
    ap.add_argument("query", nargs="*", help="free-text query; use quotes for exact phrases")
    ap.add_argument("-n", "--limit", type=int, default=8)
    ap.add_argument("-s", "--section", help="restrict to a docs section, e.g. 'Connectors', 'MCP'")
    ap.add_argument("--read", metavar="PAGE", help="print a page (path, docs URL or en/... slug)")
    ap.add_argument("--heading", help="with --read: print only this section of the page")
    ap.add_argument("--sections", action="store_true", help="list sections with page counts")
    ap.add_argument("--list", metavar="SECTION", help="list pages in a section")
    ap.add_argument("--rebuild", action="store_true", help="force rebuild of the search index")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--examples", metavar="STEP", nargs="?", const="", help="example recipes using provider[.action]")
    ap.add_argument("--feature", help="with --examples: require a feature (try, foreach, if, custom_http, ...)")
    ap.add_argument("--connector", metavar="NAME", help="show a connector from the live catalog")
    ap.add_argument("--op", help="with --connector: full schema of one trigger/action")
    a = ap.parse_args()

    if a.examples is not None:
        for r in find_examples(a.examples or None, a.feature, a.limit):
            print(f"[{r['source']}] {r['name']}  (copies {r.get('copies', 0)})\n   {r['path']}\n   "
                  f"steps: {' > '.join(r['steps'][:8])}{' ...' if len(r['steps']) > 8 else ''}\n   features: {', '.join(r['features'])}")
        return
    if a.connector:
        print(json.dumps(connector(a.connector, a.op), indent=1, ensure_ascii=False))
        return

    if a.rebuild:
        print(f"indexed {build(force=True)} chunks")
    if a.sections:
        for k, v in sections().items():
            print(f"{v:5d}  {k}")
    elif a.list:
        for pg in list_pages(a.list, limit=1000):
            print(f"{pg['path']}  -  {pg['title']}")
    elif a.read:
        r = read(a.read, heading=a.heading, max_chars=10**9)
        print(json.dumps(r, indent=1) if a.json or "error" in r else r["content"])
    elif a.query:
        res = search(" ".join(a.query), limit=a.limit, section=a.section)
        if a.json:
            print(json.dumps(res, indent=1))
        for i, r in enumerate([] if a.json else res, 1):
            print(f"{i}. {r['title']}  [{r['section']}]")
            print(f"   {r['path']}")
            if r["matched_headings"]:
                print("   headings: " + " | ".join(h[:70] for h in r["matched_headings"][:4]))
            print("   " + " ".join(r["snippet"].split())[:240])
    elif not a.rebuild:
        ap.print_help()


if __name__ == "__main__":
    main()
