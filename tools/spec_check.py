#!/usr/bin/env python3
"""spec_check: validate an automation spec (automations/<name>/spec.yaml), the Intent gate.

Checks required fields and types, at least one acceptance test with given/when/expect, a valid
trigger type, systems mapped to connectors in the live catalog, and that the confirmation
fields are filled when status is "confirmed".

Usage:  python3 tools/spec_check.py automations/*/spec.yaml [--json]
Requires PyYAML (pip install pyyaml), the only non-stdlib dependency, used for human-friendly specs.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("spec_check needs PyYAML: pip install pyyaml")

ROOT = Path(__file__).resolve().parents[1]
CATALOG_INDEX = ROOT / "kb" / "connectors" / "catalog.json"
TRIGGER_TYPES = {"app_event", "schedule", "api_endpoint", "recipe_function", "genie_skill", "webhook", "manual"}
STATUSES = {"draft", "confirmed", "changed"}
ACCESS = {"read", "write", "read_write"}
REQUIRED = {"spec_version": int, "name": str, "title": str, "summary": str, "requester": str, "status": str,
            "trigger": dict, "systems": list, "acceptance_tests": list, "error_policy": dict, "security": dict}


def check(spec: dict, path: Path | None = None) -> list[dict]:
    out: list[dict] = []

    def err(field, msg, level="error"):
        out.append({"level": level, "field": field, "message": msg})

    if not isinstance(spec, dict):
        return [{"level": "error", "field": "", "message": "spec must be a YAML mapping"}]
    for k, t in REQUIRED.items():
        if k not in spec or spec[k] in (None, ""):
            err(k, "required")
        elif not isinstance(spec[k], t):
            err(k, f"must be {t.__name__}")
    name = spec.get("name") or ""
    if name and not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", str(name)):
        err("name", "must be kebab-case")
    if path is not None and name and path.parent.name not in (name, "_template"):
        err("name", f"folder '{path.parent.name}' should equal name '{name}'", "warn")
    if spec.get("status") and spec["status"] not in STATUSES:
        err("status", f"one of {sorted(STATUSES)}")

    trig = spec.get("trigger") or {}
    if isinstance(trig, dict):
        if trig.get("type") not in TRIGGER_TYPES:
            err("trigger.type", f"one of {sorted(TRIGGER_TYPES)}")
        if trig.get("type") == "app_event" and not (trig.get("app") and trig.get("event")):
            err("trigger", "app_event needs app and event")
        if trig.get("type") == "schedule" and not trig.get("schedule"):
            err("trigger.schedule", "schedule trigger needs a schedule")

    catalog = json.loads(CATALOG_INDEX.read_text()) if CATALOG_INDEX.exists() else {}
    for i, s in enumerate(spec.get("systems") or []):
        f = f"systems[{i}]"
        if not isinstance(s, dict):
            err(f, "must be a mapping")
            continue
        for k in ("app", "connector", "access"):
            if not s.get(k):
                err(f"{f}.{k}", "required")
        if s.get("access") and s["access"] not in ACCESS:
            err(f"{f}.access", f"one of {sorted(ACCESS)}")
        if catalog and s.get("connector") and s["connector"] not in catalog:
            near = [c for c in catalog if str(s["connector"]).lower().replace(" ", "_") in c][:5]
            err(f"{f}.connector", f"'{s['connector']}' not in connector catalog" + (f"; did you mean {near}" if near else ""))
        if catalog and s.get("connector") in catalog and catalog[s["connector"]].get("requires_connection") \
                and not s.get("connection"):
            err(f"{f}.connection", "connector needs a connection: give a logical connection name")

    tests = spec.get("acceptance_tests") or []
    if isinstance(tests, list):
        if not tests:
            err("acceptance_tests", "at least one acceptance test is required")
        ids = set()
        for i, t in enumerate(tests):
            f = f"acceptance_tests[{i}]"
            if not isinstance(t, dict):
                err(f, "must be a mapping")
                continue
            for k in ("id", "given", "when", "expect"):
                if not t.get(k):
                    err(f"{f}.{k}", "required")
            if t.get("id") in ids:
                err(f"{f}.id", "duplicate id")
            ids.add(t.get("id"))

    ep = spec.get("error_policy") or {}
    if isinstance(ep, dict):
        if "retries" in ep and not isinstance(ep["retries"], int):
            err("error_policy.retries", "must be an integer")
        if not ep.get("on_failure"):
            err("error_policy.on_failure", "describe what happens on failure")
    sec = spec.get("security") or {}
    if isinstance(sec, dict) and "pii" not in sec:
        err("security.pii", "state whether personal data is processed (true/false)")

    if spec.get("status") == "confirmed":
        ap = spec.get("approvals") or {}
        if not ap.get("spec_confirmed_by") or not ap.get("spec_confirmed_at"):
            err("approvals", "confirmed spec needs spec_confirmed_by and spec_confirmed_at")
        if spec.get("open_questions"):
            err("open_questions", "confirmed spec still has open questions", "warn")
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    results, n_err = {}, 0
    for p in map(Path, a.paths):
        try:
            spec = yaml.safe_load(p.read_text())
            res = check(spec, p)
        except yaml.YAMLError as e:
            res = [{"level": "error", "field": "", "message": f"invalid YAML: {e}"}]
        results[str(p)] = res
        n_err += sum(r["level"] == "error" for r in res)
    if a.json:
        print(json.dumps(results, indent=1))
    else:
        for p, res in results.items():
            print(("FAIL " if any(r["level"] == "error" for r in res) else "ok   ") + p)
            for r in res:
                print(f"     {r['level']:5} {r['field']}: {r['message']}")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
