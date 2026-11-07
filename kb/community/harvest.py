#!/usr/bin/env python3
"""Harvest public Workato community-library recipes as JSON examples.

Community recipes are published by their authors as reusable templates
(docs: kb/docs/en/community-library.md). This script stores only what's needed to
learn recipe patterns: name, description, apps, popularity, source URL, and the recipe
`code` and `config`. Author contact details are never stored,
and e-mail addresses and credentials inside steps are redacted.

Sources (public; reached through the Workato app host):
  https://app.trial.workato.com/recipes/<id>.json?community=us       metadata
  https://app.trial.workato.com/recipes/<id>/code.json?community=us  recipe code

Recipe IDs come from the community library listing
(https://app.workato.com/browse/recipes?q=app:<app>), collected with a browser or Firecrawl.

Usage:
  python3 kb/community/harvest.py 671384 803804 ...            # by id
  python3 kb/community/harvest.py --urls urls.txt               # file of recipe URLs or ids
  python3 kb/community/harvest.py --reindex                     # rebuild kb/community/INDEX.md
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

HOST = "https://app.trial.workato.com"
OUT = Path(__file__).resolve().parent / "recipes"
INDEX = Path(__file__).resolve().parent / "INDEX.md"
KEEP = ["id", "name", "description", "applications", "action_applications", "trigger_application",
        "business_objects", "categories", "copy_count", "curated", "recipe_type", "trigger_type",
        "published_at", "updated_at"]


def get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "workato-claude-kb/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
# Credentials that authors sometimes leave in steps. Matched values are replaced, never stored.
SECRET_RES = [
    re.compile(r"\b(?:sk|rk|pk)_(?:live|test)_[A-Za-z0-9]{10,}"),          # Stripe
    re.compile(r"\bxox[abposr]-[A-Za-z0-9-]{10,}"),                       # Slack
    re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),                         # AWS access key id
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}"),                          # GitHub
    re.compile(r"\bwrk[a-z]*-[A-Za-z0-9-]{20,}"),                         # Workato API token
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"),                               # OpenAI-style
    re.compile(r"\bAIza[0-9A-Za-z_-]{30,}"),                              # Google API key
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?-----END [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"(?i)\b(Bearer|Basic)\s+[A-Za-z0-9._~+/=-]{16,}"),
]
SENSITIVE_KEY = re.compile(r"(?i)(password|passwd|secret|api[_-]?key|access[_-]?key|token|authorization|private[_-]?key)")


def redact_str(s: str) -> str:
    s = EMAIL_RE.sub("user@example.com", s)
    for rx in SECRET_RES:
        s = rx.sub(lambda m: (m.group(1) + " " if m.re.pattern.startswith("(?i)") else "") + "REDACTED", s)
    return s


def redact(obj, key: str = ""):
    """Remove e-mail addresses and credentials that authors typed into steps."""
    if isinstance(obj, str):
        literal = obj and not obj.startswith("=") and "#{" not in obj and "_dp(" not in obj
        if key and SENSITIVE_KEY.search(key) and literal and len(obj) >= 6:
            return "REDACTED"
        return redact_str(obj)
    if isinstance(obj, list):
        return [redact(x, key) for x in obj]
    if isinstance(obj, dict):
        return {k: redact(v, k) for k, v in obj.items()}
    return obj


def walk_steps(block: dict, out: list) -> None:
    if not isinstance(block, dict):
        return
    if block.get("provider") and block.get("keyword") in ("trigger", "action"):
        out.append(f"{block['provider']}.{block.get('name')}")
    for child in block.get("block") or []:
        walk_steps(child, out)


def harvest(recipe_id: int) -> Path | None:
    meta = get(f"{HOST}/recipes/{recipe_id}.json?community=us")["result"]["recipe_data"]["flow"]
    code_raw = get(f"{HOST}/recipes/{recipe_id}/code.json?community=us")["result"]
    code = json.loads(code_raw) if isinstance(code_raw, str) else code_raw
    config = meta.get("config") or []
    if isinstance(config, str):
        config = json.loads(config or "[]")
    steps: list[str] = []
    walk_steps(code, steps)
    doc = {k: meta.get(k) for k in KEEP}
    doc["source_url"] = f"https://app.workato.com/recipes/{recipe_id}?community=us"
    doc["steps"] = steps
    doc["config"] = [{k: c.get(k) for k in ("keyword", "provider", "name")} for c in config if isinstance(c, dict)]
    doc["code"] = redact(code)
    doc["description"] = redact(doc.get("description"))
    trig = (meta.get("trigger_application") or "misc").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", (meta.get("name") or str(recipe_id)).lower()).strip("-")[:70]
    path = OUT / trig / f"{recipe_id}-{slug}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    return path


def reindex() -> int:
    rows = []
    for p in sorted(OUT.rglob("*.json")):
        d = json.loads(p.read_text())
        rows.append((d.get("copy_count") or 0, d, p))
    rows.sort(key=lambda r: -r[0])
    lines = ["# Community recipe examples", "",
             "Public Workato community-library recipes harvested as JSON pattern examples by",
             "`kb/community/harvest.py`. Search steps: `grep -rl '\"slack.post_message' kb/community/recipes`.", "",
             "| Recipe | Trigger | Steps | Copies | File |", "| --- | --- | --- | ---: | --- |"]
    for copies, d, p in rows:
        steps = ", ".join(dict.fromkeys(d.get("steps", [])))[:160]
        lines.append(f"| {d.get('name','').replace('|','/')} | {d.get('trigger_application')} | {steps} | {copies} | "
                     f"`{p.relative_to(OUT.parent.parent.parent)}` |")
    INDEX.write_text("\n".join(lines) + "\n")
    return len(rows)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--urls", help="file with recipe URLs or ids, one per line")
    ap.add_argument("--delay", type=float, default=1.0, help="seconds between recipes (be polite)")
    ap.add_argument("--reindex", action="store_true")
    a = ap.parse_args()
    refs = list(a.ids)
    if a.urls:
        refs += Path(a.urls).read_text().split()
    ids = sorted({int(m.group(1)) for r in refs for m in [re.search(r"(?:recipes/)?(\d{3,})", r)] if m})
    ok = 0
    for i, rid in enumerate(ids):
        if any(OUT.rglob(f"{rid}-*.json")):
            continue
        try:
            print("saved", harvest(rid).relative_to(OUT))
            ok += 1
        except (urllib.error.HTTPError, KeyError, json.JSONDecodeError) as e:
            print(f"skip {rid}: {e}", file=sys.stderr)
        if i + 1 < len(ids):
            time.sleep(a.delay)
    print(f"harvested {ok} new | index rows: {reindex()}")


if __name__ == "__main__":
    main()
