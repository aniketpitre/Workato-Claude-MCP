#!/usr/bin/env python3
"""Build the Developer API payload for creating or updating a recipe (Push stage).

Source recipe files are environment-neutral. A config entry may name a LOGICAL connection:
    {"keyword": "application", "provider": "salesforce", "connection": "crm", "account_id": null}
This tool resolves it per environment from config/environments.yaml (connections: {crm: <id>}),
drops our helper keys, and serialises `code` and `config` as JSON strings, as the API requires.

Usage:
  python3 tools/recipe_payload.py automations/<name>/recipes/<file>.recipe.json [--env dev] [--out payload.json]
The output object is the `recipe` argument for the Workato MCP tools post_recipes / put_recipes_.
Exit 1 if the recipe fails recipe_check (author profile): nothing unvalidated gets pushed.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))


def load_env(env: str) -> dict:
    import yaml
    cfg = yaml.safe_load((ROOT / "config" / "environments.yaml").read_text())
    envs = cfg.get("environments") or {}
    if env not in envs:
        sys.exit(f"unknown environment '{env}' (have: {sorted(envs)})")
    return envs[env]


def build(path: Path, env: str) -> tuple[dict, list[str]]:
    import recipe_check as rc
    notes: list[str] = []
    doc = json.loads(path.read_text())
    findings = rc.check_file(path, rc.Checker(rc.Catalog(rc.CATALOG_DIR), "author"))
    errs = [f for f in findings if f.level == "error"]
    if errs:
        raise SystemExit(f"recipe_check failed ({len(errs)} errors), e.g. {errs[0].rule} {errs[0].detail or ''}; "
                         f"fix before pushing")
    e = load_env(env)
    mapping = e.get("connections") or {}
    config = []
    for c in doc.get("config") or []:
        c = dict(c)
        logical = c.pop("connection", None)
        if logical:
            if logical in mapping:
                c["account_id"] = mapping[logical]
            else:
                notes.append(f"connection '{logical}' ({c['provider']}) not mapped in env '{env}': "
                             f"recipe will need its connection bound before it can start")
        config.append(c)
    payload = {
        "name": doc["name"],
        "description": doc.get("description", ""),
        "folder_id": str(e["project"]["folder_id"]),
        "code": json.dumps(doc["code"], separators=(",", ":"), ensure_ascii=False),
        "config": json.dumps(config, separators=(",", ":"), ensure_ascii=False),
    }
    return payload, notes


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("recipe")
    ap.add_argument("--env", default="dev")
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    payload, notes = build(Path(a.recipe), a.env)
    text = json.dumps(payload, indent=1, ensure_ascii=False)
    if a.out:
        Path(a.out).write_text(text + "\n")
        print(f"wrote {a.out}")
    else:
        print(text)
    for n in notes:
        print("NOTE:", n, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
