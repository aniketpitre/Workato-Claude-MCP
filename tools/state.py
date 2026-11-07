#!/usr/bin/env python3
"""Lifecycle state machine for automations (docs/lifecycle.md, docs/architecture.md §6).

Every automation lives in automations/<name>/ with spec.yaml, design.md, recipes/, reports/, and
state.json. This tool is the only writer of state.json: it enforces the allowed transitions, the
gate criteria, human approvals, and the debug budget, and keeps an append-only history.

Commands:
  new <name> --title "..." [--requester who]        scaffold from automations/_template
  show <name> | list                                status
  approve <name> spec|design|go-live --by <human>   record a HUMAN approval (only when the user said so)
  advance <name> <state> --by <role> [--note ...]   move to a state; gate checks run first
  record-push <name> --env dev --recipe <file> --id <workato id> --diff-ok|--diff-failed
  record-test <name> --result pass|fail --report <path>
States: draft specified designed built validated pushed tested deployed operating debugging escalated incident
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUTOMATIONS = ROOT / "automations"
TEMPLATE = AUTOMATIONS / "_template"
sys.path.insert(0, str(ROOT / "tools"))

DEBUG_BUDGET = 5
TRANSITIONS = {
    "draft": {"specified"},
    "specified": {"designed", "draft"},
    "designed": {"built", "specified"},
    "built": {"validated", "debugging"},
    "validated": {"pushed", "debugging"},
    "pushed": {"tested", "debugging"},
    "tested": {"deployed", "debugging"},
    "debugging": {"built", "designed", "specified", "escalated"},
    "escalated": {"debugging", "designed", "specified"},
    "deployed": {"operating", "pushed"},          # pushed = rollback/stop
    "operating": {"incident", "specified"},
    "incident": {"debugging", "specified", "operating"},
}


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def git_head() -> str | None:
    try:
        return subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return None


def adir(name: str) -> Path:
    return AUTOMATIONS / name


def load(name: str) -> dict:
    p = adir(name) / "state.json"
    if not p.exists():
        sys.exit(f"no automation '{name}' (missing {p.relative_to(ROOT)})")
    return json.loads(p.read_text())


def save(name: str, st: dict) -> None:
    (adir(name) / "state.json").write_text(json.dumps(st, indent=1) + "\n")


def recipes(name: str) -> list[Path]:
    return sorted((adir(name) / "recipes").glob("*.json"))


# --------------------------------------------------------------------------- gates
def gate(name: str, st: dict, to: str) -> list[str]:
    """Return the list of unmet criteria for entering state `to` (empty = OK)."""
    import recipe_check as rc
    import spec_check
    import yaml
    d, problems = adir(name), []
    spec = yaml.safe_load((d / "spec.yaml").read_text()) if (d / "spec.yaml").exists() else None

    if to == "specified":
        errs = [r for r in spec_check.check(spec, d / "spec.yaml") if r["level"] == "error"]
        problems += [f"spec_check: {r['field']}: {r['message']}" for r in errs]
        if not st["approvals"].get("spec"):
            problems.append("human approval missing: approve <name> spec --by <requester>")
    elif to == "designed":
        text = (d / "design.md").read_text() if (d / "design.md").exists() else ""
        if not text or "<title>" in text or "Status: draft | approved" in text:
            problems.append("design.md not filled in (template placeholders remain)")
        if not st["approvals"].get("design"):
            problems.append("human approval missing: approve <name> design --by <requester>")
    elif to == "built":
        if not recipes(name):
            problems.append("no recipe files in recipes/")
    elif to == "validated":
        checker = rc.Checker(rc.Catalog(rc.CATALOG_DIR), "author")
        for p in recipes(name):
            errs = [f for f in rc.check_file(p, checker) if f.level == "error"]
            if errs:
                problems.append(f"recipe_check {p.name}: {len(errs)} error(s), e.g. {errs[0].rule}")
        v = d / "reports" / "validate.json"
        if not v.exists() or json.loads(v.read_text()).get("verdict", {}).get("result") != "pass":
            problems.append("QA verdict missing: reports/validate.json with verdict.result == pass")
    elif to == "pushed":
        env = st.get("env", "dev")
        pushed = st["assets"].get(env, {})
        for p in recipes(name):
            rec = pushed.get(p.name)
            if not rec:
                problems.append(f"{p.name} not pushed to {env}")
            elif not rec.get("diff_ok"):
                problems.append(f"{p.name}: read-back diff not clean")
    elif to == "tested":
        t = st.get("tests") or {}
        if t.get("result") != "pass":
            problems.append("acceptance tests not recorded as pass (record-test)")
    elif to == "deployed":
        if not st["approvals"].get("go-live"):
            problems.append("human approval missing: approve <name> go-live --by <requester>")
        if (st.get("tests") or {}).get("result") != "pass":
            problems.append("tests must pass before deploy")
    if to == "debugging" and st["debug_rounds"] >= DEBUG_BUDGET:
        problems.append(f"debug budget ({DEBUG_BUDGET}) exhausted: advance to 'escalated'")
    return problems


# --------------------------------------------------------------------------- commands
def cmd_new(a):
    name = a.name
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        sys.exit("name must be kebab-case")
    d = adir(name)
    if d.exists():
        sys.exit(f"{d.relative_to(ROOT)} already exists")
    d.mkdir(parents=True)
    (d / "recipes").mkdir()
    (d / "reports").mkdir()
    spec = (TEMPLATE / "spec.yaml").read_text()
    spec = re.sub(r"(?m)^name: .*$", f"name: {name}", spec, count=1)
    spec = re.sub(r"(?m)^title: .*$", f"title: {a.title}", spec, count=1)
    spec = re.sub(r"(?m)^requester: .*$", f"requester: {a.requester}", spec, count=1)
    (d / "spec.yaml").write_text(spec)
    (d / "design.md").write_text((TEMPLATE / "design.md").read_text())
    (d / "CHANGELOG.md").write_text(f"# {a.title}\n\n## Unreleased\n- Created {now()[:10]}\n")
    st = {"name": name, "title": a.title, "state": "draft", "env": "dev", "approvals": {},
          "assets": {}, "tests": None, "debug_rounds": 0,
          "history": [{"at": now(), "from": None, "to": "draft", "by": a.by, "note": "created", "commit": git_head()}]}
    save(name, st)
    print(f"created {d.relative_to(ROOT)} (state: draft). Next: fill spec.yaml, then spec_check.")


def cmd_show(a):
    st = load(a.name)
    print(json.dumps({k: v for k, v in st.items() if k != "history"}, indent=1))
    print("history:")
    for h in st["history"][-10:]:
        print(f"  {h['at']}  {h['from'] or '-':>10} -> {h['to']:<10} by {h['by']}  {h.get('note') or ''}")
    nxt = sorted(TRANSITIONS.get(st["state"], []))
    print("next:", ", ".join(nxt))
    for to in nxt:
        p = gate(a.name, st, to)
        print(f"  {to}: {'ready' if not p else 'blocked: ' + '; '.join(p)}")


def cmd_list(a):
    for d in sorted(AUTOMATIONS.iterdir()):
        if (d / "state.json").exists():
            st = json.loads((d / "state.json").read_text())
            print(f"{st['name']:40} {st['state']:11} {st['history'][-1]['at']}")


def cmd_approve(a):
    st = load(a.name)
    st["approvals"][a.gate] = {"by": a.by, "at": now(), "commit": git_head(), "note": a.note}
    if a.gate == "spec":   # mirror into spec.yaml (text edit keeps comments)
        p = adir(a.name) / "spec.yaml"
        t = p.read_text()
        t = re.sub(r"(?m)^status: \w+", "status: confirmed", t, count=1)
        t = re.sub(r"(?m)^(\s*spec_confirmed_by:).*$", rf"\1 {a.by}", t, count=1)
        t = re.sub(r"(?m)^(\s*spec_confirmed_at:).*$", rf"\1 '{now()}'", t, count=1)
        p.write_text(t)
    st["history"].append({"at": now(), "from": st["state"], "to": st["state"], "by": a.by,
                          "note": f"APPROVED {a.gate}" + (f": {a.note}" if a.note else ""), "commit": git_head()})
    save(a.name, st)
    print(f"recorded approval of {a.gate} by {a.by}")


def cmd_advance(a):
    st = load(a.name)
    cur, to = st["state"], a.to
    if to not in TRANSITIONS.get(cur, set()):
        sys.exit(f"transition {cur} -> {to} not allowed (allowed: {sorted(TRANSITIONS.get(cur, []))})")
    problems = [] if a.force_note else gate(a.name, st, to)
    if problems:
        print(f"BLOCKED {cur} -> {to}:")
        for p in problems:
            print("  -", p)
        sys.exit(1)
    if to == "debugging":
        st["debug_rounds"] += 1
    if to in ("specified", "designed"):
        st["debug_rounds"] = 0
    st["history"].append({"at": now(), "from": cur, "to": to, "by": a.by, "note": a.note or a.force_note,
                          "commit": git_head()})
    st["state"] = to
    save(a.name, st)
    print(f"{a.name}: {cur} -> {to}")
    print(f'commit with: git add automations/{a.name} && git commit -m "{a.name}: {cur} -> {to}"')


def cmd_record_push(a):
    st = load(a.name)
    rec = st["assets"].setdefault(a.env, {})
    name = Path(a.recipe).name
    rec[name] = {"type": "recipe", "id": a.id, "pushed_at": now(), "diff_ok": bool(a.diff_ok), "commit": git_head()}
    save(a.name, st)
    print(f"recorded {name} -> {a.env} recipe {a.id} (diff_ok={bool(a.diff_ok)})")


def cmd_record_test(a):
    st = load(a.name)
    st["tests"] = {"result": a.result, "report": a.report, "at": now(), "commit": git_head()}
    save(a.name, st)
    print(f"recorded tests: {a.result}")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("new"); p.add_argument("name"); p.add_argument("--title", required=True)
    p.add_argument("--requester", default="aniketpitre"); p.add_argument("--by", default="workato-lead")
    p.set_defaults(fn=cmd_new)
    p = sub.add_parser("show"); p.add_argument("name"); p.set_defaults(fn=cmd_show)
    p = sub.add_parser("list"); p.set_defaults(fn=cmd_list)
    p = sub.add_parser("approve"); p.add_argument("name"); p.add_argument("gate", choices=["spec", "design", "go-live"])
    p.add_argument("--by", required=True); p.add_argument("--note"); p.set_defaults(fn=cmd_approve)
    p = sub.add_parser("advance"); p.add_argument("name"); p.add_argument("to")
    p.add_argument("--by", required=True); p.add_argument("--note")
    p.add_argument("--force-note", help=argparse.SUPPRESS)  # emergency override; recorded in history
    p.set_defaults(fn=cmd_advance)
    p = sub.add_parser("record-push"); p.add_argument("name"); p.add_argument("--env", default="dev")
    p.add_argument("--recipe", required=True); p.add_argument("--id", required=True, type=int)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--diff-ok", action="store_true"); g.add_argument("--diff-failed", action="store_true")
    p.set_defaults(fn=cmd_record_push)
    p = sub.add_parser("record-test"); p.add_argument("name"); p.add_argument("--result", choices=["pass", "fail"], required=True)
    p.add_argument("--report", required=True); p.set_defaults(fn=cmd_record_test)
    a = ap.parse_args(argv)
    a.fn(a)


if __name__ == "__main__":
    main()
