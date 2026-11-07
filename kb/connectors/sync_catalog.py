#!/usr/bin/env python3
"""Sync the live Workato connector catalog: every connector's triggers and actions with schemas.

This is the ground truth for recipe generation: exact operation names, input fields (required or
optional, type, picklist, toggle alternative, nested properties), and output fields.

Source: Workato Developer API  GET /api/workato_cli/v1/connectors
        (the same data as the official Workato MCP tool `get_workato_cli_v1_connectors`)

Output:
  kb/connectors/catalog/<connector>.json   compact schema per connector
  kb/connectors/INDEX.md                   connector -> triggers / actions (required inputs)
  kb/connectors/catalog.json               {connector: {title, triggers[], actions[]}} name index

Auth: WORKATO_API_TOKEN (Bearer) and WORKATO_BASE_URL (default https://app.trial.workato.com).
In a Claude cloud session the egress proxy injects credentials, so the token can be omitted.

Usage:  python3 kb/connectors/sync_catalog.py [--names slack salesforce ...]
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

BASE = os.environ.get("WORKATO_BASE_URL", "https://app.trial.workato.com").rstrip("/")
TOKEN = os.environ.get("WORKATO_API_TOKEN")
HERE = Path(__file__).resolve().parent
CATALOG_DIR = HERE / "catalog"
TAG_RE = re.compile(r"<[^>]+>")


def api(params: list[tuple[str, str]]) -> dict:
    url = f"{BASE}/api/workato_cli/v1/connectors?" + urllib.parse.urlencode(params)
    headers = {"Accept": "application/json", "User-Agent": "workato-claude-kb/1.0"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    for attempt in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=120) as r:
                return json.loads(r.read().decode())
        except Exception as e:  # 429/5xx/network
            if attempt == 4:
                raise
            print(f"  retry {attempt + 1}: {e}", file=sys.stderr)
            time.sleep(2 ** attempt)
    raise RuntimeError("unreachable")


def text(s, limit: int = 240) -> str | None:
    if not s:
        return None
    if isinstance(s, dict):
        s = s.get("body") or ""
    s = " ".join(html.unescape(TAG_RE.sub(" ", str(s))).split())
    return (s[:limit] + "…") if len(s) > limit else s or None


def field(f: dict) -> dict:
    out = {"name": f.get("name"), "type": f.get("type")}
    for k in ("label", "control_type"):
        if f.get(k):
            out[k] = f[k]
    if not f.get("optional") and not f.get("optionalExpression"):
        out["required"] = True
    if f.get("mark_as_required"):
        out["required_when_visible"] = True
    if f.get("ngIf"):
        out["visible_if"] = f["ngIf"]
    if f.get("default") not in (None, ""):
        out["default"] = f["default"]
    pl = f.get("pick_list")
    if isinstance(pl, str):
        out["pick_list"] = pl
    elif isinstance(pl, list):
        out["options"] = [p[1] if isinstance(p, list) and len(p) > 1 else p for p in pl][:50]
    if f.get("extends_schema"):
        out["extends_schema"] = True
    if isinstance(f.get("toggle_field"), dict):
        t = f["toggle_field"]
        out["toggle_field"] = {"name": t.get("name"), "type": t.get("type")}
    if f.get("of"):
        out["of"] = f["of"]
    if f.get("properties"):
        out["properties"] = [field(p) for p in f["properties"] if isinstance(p, dict)]
    h = text(f.get("hint"), 200)
    if h:
        out["hint"] = h
    return out


def operation(op: dict) -> dict:
    out = {"name": op.get("name"), "title": text(op.get("title"), 120)}
    d = text(op.get("description"), 160)
    if d:
        out["description"] = d
    hp = text(op.get("help"), 300)
    if hp:
        out["help"] = hp
    if "input" in op:
        out["input"] = [field(f) for f in op.get("input") or [] if isinstance(f, dict)]
    if "output" in op:
        out["output"] = [field(f) for f in op.get("output") or [] if isinstance(f, dict)]
    return out


def list_names() -> list[str]:
    names, page = [], 1
    while True:
        d = api([("page[number]", str(page)), ("page[size]", "100")])
        names += [c["name"] for c in d["data"]]
        if len(names) >= d.get("total", 0) or not d["data"]:
            return names
        page += 1


def sync(only: list[str] | None = None, batch: int = 8) -> dict:
    names = only or list_names()
    print(f"{len(names)} connectors", file=sys.stderr)
    CATALOG_DIR.mkdir(parents=True, exist_ok=True)
    index: dict[str, dict] = {}
    for i in range(0, len(names), batch):
        chunk = names[i:i + batch]
        params = [("include_schemas", "true"), ("page[size]", "100")] + [("names[]", n) for n in chunk]
        for c in api(params)["data"]:
            doc = {
                "name": c["name"], "title": c.get("title"),
                "requires_connection": c.get("requires_connection"),
                "categories": c.get("categories"), "aliases": c.get("aliases"),
                "triggers": [operation(t) for t in c.get("triggers") or []],
                "actions": [operation(a) for a in c.get("actions") or []],
            }
            (CATALOG_DIR / f"{c['name']}.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
            index[c["name"]] = {
                "title": c.get("title"),
                "requires_connection": c.get("requires_connection"),
                "triggers": [t["name"] for t in doc["triggers"]],
                "actions": [a["name"] for a in doc["actions"]],
            }
        print(f"  {min(i + batch, len(names))}/{len(names)}", file=sys.stderr)
        time.sleep(0.3)
    if only:  # partial run: merge into existing index
        prev = json.loads((HERE / "catalog.json").read_text()) if (HERE / "catalog.json").exists() else {}
        prev.update(index)
        index = prev
    (HERE / "catalog.json").write_text(json.dumps(dict(sorted(index.items())), indent=1, ensure_ascii=False) + "\n")
    write_index()
    return index


def required_inputs(op: dict) -> list[str]:
    return [f["name"] for f in op.get("input", []) if f.get("required")]


def write_index() -> None:
    lines = ["# Workato connector catalog", "",
             "Generated by `kb/connectors/sync_catalog.py` from the live workspace. **Use these exact names in recipe JSON.**",
             "Full schemas: `kb/connectors/catalog/<connector>.json`. Required inputs shown in brackets.", ""]
    for p in sorted(CATALOG_DIR.glob("*.json")):
        c = json.loads(p.read_text())
        lines.append(f"## {c['title']} (`{c['name']}`)" + ("" if c.get("requires_connection") else " — no connection needed"))
        for kind in ("triggers", "actions"):
            ops = c.get(kind) or []
            if ops:
                items = []
                for o in ops:
                    req = required_inputs(o)
                    items.append(f"`{o['name']}`" + (f" [{', '.join(req)}]" if req else ""))
                lines.append(f"- **{kind}**: " + "; ".join(items))
        lines.append("")
    (HERE / "INDEX.md").write_text("\n".join(lines))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--names", nargs="*", help="only these connectors (merged into the existing catalog)")
    a = ap.parse_args()
    idx = sync(a.names)
    print(f"done: {len(idx)} connectors, "
          f"{sum(len(v['triggers']) for v in idx.values())} triggers, "
          f"{sum(len(v['actions']) for v in idx.values())} actions", file=sys.stderr)
