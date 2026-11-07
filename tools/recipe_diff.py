#!/usr/bin/env python3
"""Compare a source recipe with what Workato actually stored (Push stage read-back).

Workato can silently drop or rewrite fields on import (unknown keys, malformed inputs, wrong
structured forms). This tool compares step by step (depth-first) and reports:
  MISSING_STEP / EXTRA_STEP     the step trees differ
  CHANGED  keyword, provider, name, as, number
  DROPPED_INPUT                 an input field we sent isn't in the stored recipe
  CHANGED_INPUT                 a value differs (after normalising types)
  ADDED_INPUT (info)            server-added defaults
Server-managed keys (titles, descriptions, extended schemas, picklist caches, toggles) are ignored.

Usage:
  python3 tools/recipe_diff.py SOURCE.recipe.json READBACK.json [--json]
READBACK may be the raw get_recipes_ response (code as a string) or a recipe file.
Exit 0 when there are no MISSING/EXTRA/CHANGED/DROPPED differences (diff_ok), else 1.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

IGNORED_STEP_KEYS = {"title", "description", "dynamicPickListSelection", "toggleCfg", "visible_config_fields",
                     "hidden_config_fields", "extended_input_schema", "extended_output_schema", "comment",
                     "wizardFinished", "job_report_schema", "job_report_config", "format_version", "param",
                     "parameters_schema", "unfinished", "block", "skip", "filter"}
BLOCKING = {"MISSING_STEP", "EXTRA_STEP", "CHANGED", "DROPPED_INPUT", "CHANGED_INPUT"}


def code_of(path: Path) -> dict:
    d = json.loads(path.read_text())
    if isinstance(d, dict) and "result" in d and isinstance(d["result"], dict):
        d = d["result"]
    if isinstance(d, dict) and d.get("keyword") == "trigger":
        return d
    c = d.get("code") if isinstance(d, dict) else None
    if isinstance(c, str):
        c = json.loads(c)
    if not isinstance(c, dict):
        raise SystemExit(f"{path}: no recipe code found")
    return c


def flatten(code: dict) -> list[dict]:
    out = []

    def walk(b, parent):
        out.append({"block": b, "parent": parent})
        for c in b.get("block") or []:
            if isinstance(c, dict):
                walk(c, b.get("as") or b.get("keyword"))
    walk(code, None)
    return out


def norm(v):
    """Normalise representation differences the server introduces (bool/int -> str, key order)."""
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, dict):
        return {k: norm(x) for k, x in v.items()}
    if isinstance(v, list):
        return [norm(x) for x in v]
    if isinstance(v, str):
        s = v.strip()
        if s[:1] in "[{":           # stringified JSON schemas: compare parsed
            try:
                return norm(json.loads(s))
            except Exception:
                pass
        return s
    return v


def diff_inputs(src: dict, got: dict, where: str, out: list):
    for k, v in (src or {}).items():
        if k not in (got or {}):
            if v in (None, "", [], {}):
                continue
            out.append({"type": "DROPPED_INPUT", "where": where, "field": k, "sent": v})
        elif isinstance(v, dict) and isinstance(got[k], dict):
            diff_inputs(v, got[k], f"{where}.{k}", out)
        elif norm(v) != norm(got[k]):
            out.append({"type": "CHANGED_INPUT", "where": where, "field": k, "sent": v, "stored": got[k]})
    for k in (got or {}):
        if k not in (src or {}):
            out.append({"type": "ADDED_INPUT", "where": where, "field": k, "stored": got[k]})


def compare(src: dict, got: dict) -> list[dict]:
    a, b = flatten(src), flatten(got)
    out: list[dict] = []
    for i in range(max(len(a), len(b))):
        if i >= len(b):
            s = a[i]["block"]
            out.append({"type": "MISSING_STEP", "where": f"#{i}", "step": f"{s.get('keyword')} {s.get('provider')}.{s.get('name')} as={s.get('as')}"})
            continue
        if i >= len(a):
            g = b[i]["block"]
            out.append({"type": "EXTRA_STEP", "where": f"#{i}", "step": f"{g.get('keyword')} {g.get('provider')}.{g.get('name')}"})
            continue
        s, g = a[i]["block"], b[i]["block"]
        where = f"step {s.get('number')} ({s.get('as') or s.get('keyword')})"
        for k in ("keyword", "provider", "name", "as", "number"):
            if norm(s.get(k)) != norm(g.get(k)) and not (k == "as" and not s.get(k)):
                out.append({"type": "CHANGED", "where": where, "field": k, "sent": s.get(k), "stored": g.get(k)})
        diff_inputs(s.get("input") or {}, g.get("input") or {}, where, out)
        if s.get("keyword") == "foreach" and norm(s.get("source")) != norm(g.get("source")):
            out.append({"type": "CHANGED", "where": where, "field": "source", "sent": s.get("source"), "stored": g.get("source")})
        for k in set(s) - IGNORED_STEP_KEYS - {"keyword", "provider", "name", "as", "number", "input", "uuid", "source"}:
            if k not in g:
                out.append({"type": "DROPPED_INPUT", "where": where, "field": f"<step>.{k}", "sent": s[k]})
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source")
    ap.add_argument("readback")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    diffs = compare(code_of(Path(a.source)), code_of(Path(a.readback)))
    ok = not any(d["type"] in BLOCKING for d in diffs)
    if a.json:
        print(json.dumps({"diff_ok": ok, "differences": diffs}, indent=1, default=str))
    else:
        for d in diffs:
            print(f"{d['type']:14} {d['where']:28} {d.get('field', d.get('step', ''))}"
                  + (f"  sent={str(d.get('sent'))[:60]!r} stored={str(d.get('stored'))[:60]!r}" if 'sent' in d or 'stored' in d else ""))
        print("diff_ok" if ok else "DIFF FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
