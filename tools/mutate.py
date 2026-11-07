#!/usr/bin/env python3
"""Mutation testing for tools/recipe_check.py.

Takes known-good recipes (the golden corpus files with no errors in profile "corpus"), injects one
defect at a time, and checks that recipe_check reports the expected rule at level "error" (profile
"author"). A mutant that isn't caught is a FALSE NEGATIVE; the target is zero.

Usage:  python3 tools/mutate.py [--per-mutation 25] [--verbose]
"""
from __future__ import annotations

import argparse
import copy
import json
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import recipe_check as rc  # noqa: E402

ROOT = rc.ROOT
CATALOG = rc.Catalog(rc.CATALOG_DIR)


# --------------------------------------------------------------------------- helpers
def steps_of(code: dict) -> list[dict]:
    out = []

    def walk(b):
        out.append(b)
        for c in b.get("block") or []:
            if isinstance(c, dict):
                walk(c)
    walk(code)
    return out


def actions(code):
    return [s for s in steps_of(code) if s.get("keyword") == "action" and s.get("provider") and s.get("name")]


def catalog_actions(code):
    res = []
    for s in actions(code):
        c = CATALOG.get(s["provider"])
        if c and any(o["name"] == s["name"] for o in c["actions"]):
            res.append(s)
    return res


def pills_in(step) -> list[str]:
    return rc.DP_RE.findall(json.dumps(step.get("input") or {}, ensure_ascii=False).replace('\\"', '"'))


def replace_in_input(step, old: str, new: str) -> bool:
    """Replace text inside any string of step['input'] (first occurrence)."""
    done = [False]

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if done[0]:
                    return
                if isinstance(v, str) and old in v:
                    o[k] = v.replace(old, new, 1)
                    done[0] = True
                else:
                    walk(v)
        elif isinstance(o, list):
            for i, v in enumerate(o):
                if done[0]:
                    return
                if isinstance(v, str) and old in v:
                    o[i] = v.replace(old, new, 1)
                    done[0] = True
                else:
                    walk(v)
    walk(step.get("input") or {})
    return done[0]


def step_with_pill(code):
    """First non-trigger step holding an output datapill (with provider and line)."""
    for s in steps_of(code)[1:]:
        for p in pills_in(s):
            try:
                pill = json.loads(p)
            except Exception:
                continue
            if pill.get("pill_type", "output") == "output" and pill.get("line") and pill.get("provider"):
                return s, p
    return None, None


# --------------------------------------------------------------------------- mutations
# each returns the mutated document (dict) or None if not applicable; rule = expected finding
def m_dup_number(doc):
    a = actions(doc["code"])
    if len(a) < 2:
        return None
    a[1]["number"] = a[0]["number"]
    return doc


def m_trigger_number(doc):
    doc["code"]["number"] = 1
    return doc


def m_bad_action_name(doc):
    a = [s for s in catalog_actions(doc["code"]) if s["name"] != "__adhoc_http_action"]
    if not a:
        return None
    a[0]["name"] = a[0]["name"] + "_typo"
    return doc


def m_bad_provider(doc):
    a = actions(doc["code"])
    if not a:
        return None
    a[0]["provider"] = "nonexistent_app_xyz"
    return doc


def _replace_line(step, line, new):
    return replace_in_input(step, f'"line":"{line}"', f'"line":"{new}"')


def m_dangling_pill2(doc):
    s, p = step_with_pill(doc["code"])
    if not s:
        return None
    line = json.loads(p)["line"]
    return doc if _replace_line(s, line, "nope_alias_404") else None


def m_invalid_pill_json(doc):
    s, p = step_with_pill(doc["code"])
    if not s:
        return None
    return doc if replace_in_input(s, '"pill_type":"output"', '"pill_type":"output",broken') else None


def m_wrong_pill_provider(doc):
    s, p = step_with_pill(doc["code"])
    if not s:
        return None
    prov = json.loads(p)["provider"]
    return doc if replace_in_input(s, f'"provider":"{prov}"', '"provider":"wrong_provider"') else None


def m_int_index(doc):
    s, p = step_with_pill(doc["code"])
    if not s:
        return None
    return doc if replace_in_input(s, '"path":[', '"path":[0,') else None


def m_forward_ref(doc):
    a = actions(doc["code"])
    if len(a) < 2 or not a[-1].get("as"):
        return None
    last = a[-1]
    pill = json.dumps({"pill_type": "output", "provider": last["provider"], "line": last["as"], "path": ["id"]},
                      separators=(",", ":"))
    a[0].setdefault("input", {})["mutant_field"] = f"#{{_dp('{pill}')}}"
    return doc


def m_drop_required(doc):
    for s in catalog_actions(doc["code"]):
        op = next(o for o in CATALOG.get(s["provider"])["actions"] if o["name"] == s["name"])
        for f in op.get("input") or []:
            if f.get("required") and not f.get("visible_if") and f.get("type") not in ("object", "array") \
                    and not f.get("properties") and not rc._is_empty((s.get("input") or {}).get(f["name"])):
                del s["input"][f["name"]]
                return doc
    return None


def _find(code, kw):
    return [s for s in steps_of(code) if s.get("keyword") == kw]


def m_else_not_last(doc):
    for s in _find(doc["code"], "if"):
        kids = s.get("block") or []
        if len(kids) >= 2 and kids[-1].get("keyword") == "else":
            s["block"] = [kids[-1]] + kids[:-1]
            return doc
    return None


def m_catch_not_last(doc):
    for s in _find(doc["code"], "try"):
        kids = s.get("block") or []
        if len(kids) >= 2 and kids[-1].get("keyword") == "catch":
            s["block"] = [kids[-1]] + kids[:-1]
            return doc
    return None


def m_try_no_catch(doc):
    for s in _find(doc["code"], "try"):
        if any(k.get("keyword") == "catch" for k in s.get("block") or []):
            s["block"] = [k for k in s["block"] if k.get("keyword") != "catch"]
            return doc
    return None


def m_add_elsif(doc):
    for s in _find(doc["code"], "if"):
        kids = s.get("block") or []
        if kids and kids[-1].get("keyword") == "else":
            kids.insert(len(kids) - 1, {"number": 9999, "keyword": "elsif", "input": copy.deepcopy(s.get("input")),
                                        "block": [], "uuid": "mutant-elsif"})
            return doc
    return None


def m_uuid_long(doc):
    a = actions(doc["code"])
    if not a:
        return None
    a[0]["uuid"] = "x" * 40
    return doc


def m_dup_uuid(doc):
    a = actions(doc["code"])
    if not a or not doc["code"].get("uuid"):
        return None
    a[0]["uuid"] = doc["code"]["uuid"]
    return doc


def m_dup_as(doc):
    a = [s for s in actions(doc["code"]) if s.get("as")]
    if len(a) < 2:
        return None
    a[1]["as"] = a[0]["as"]
    return doc


def m_remove_config(doc):
    cfg = doc.get("config")
    if not isinstance(cfg, list) or not cfg:
        return None
    used = {s.get("provider") for s in actions(doc["code"])}
    for i, c in enumerate(cfg):
        if c.get("provider") in used:
            del cfg[i]
            return doc
    return None


def m_stop_no_reason(doc):
    for s in _find(doc["code"], "stop"):
        (s.setdefault("input", {})).pop("stop_reason", None)
        return doc
    return None


def m_remove_returns(doc):
    trig = doc["code"]
    ret = rc.RETURNING_TRIGGERS.get((trig.get("provider"), trig.get("name")))
    if not ret:
        return None
    rp, rn = ret.split(".")

    def strip(b):
        b["block"] = [c for c in (b.get("block") or []) if not (c.get("provider") == rp and c.get("name") == rn)]
        for c in b["block"]:
            strip(c)
    strip(trig)
    return doc


def m_repeat_no_while(doc):
    for s in _find(doc["code"], "repeat"):
        s["block"] = [k for k in s.get("block") or [] if k.get("keyword") != "while_condition"]
        return doc
    return None


def m_foreach_no_source(doc):
    for s in _find(doc["code"], "foreach"):
        s.pop("source", None)
        return doc
    return None


def m_condition_malformed(doc):
    for s in _find(doc["code"], "if"):
        s["input"] = {"type": "compound", "operand": "and"}
        return doc
    return None


def m_wrap_recipe(doc):
    return {"recipe": doc}


MUTATIONS = {
    "dup_number": (m_dup_number, "STEP_NUMBER_DUPLICATE"),
    "trigger_number": (m_trigger_number, "TRIGGER_NUMBER_ZERO"),
    "bad_action_name": (m_bad_action_name, "OP_UNKNOWN_NAME"),
    "bad_provider": (m_bad_provider, "OP_UNKNOWN_PROVIDER"),
    "dangling_pill": (m_dangling_pill2, "DP_LINE_RESOLVES"),
    "invalid_pill_json": (m_invalid_pill_json, "DP_VALID_JSON"),
    "wrong_pill_provider": (m_wrong_pill_provider, "DP_PROVIDER_MATCHES"),
    "int_index": (m_int_index, "DP_INT_INDEX"),
    "forward_ref": (m_forward_ref, "DP_STEP_REACHABLE"),
    "drop_required": (m_drop_required, "REQUIRED_INPUT"),
    "else_not_last": (m_else_not_last, "ELSE_LAST_IN_IF"),
    "catch_not_last": (m_catch_not_last, "CATCH_LAST_IN_TRY"),
    "try_no_catch": (m_try_no_catch, "TRY_HAS_CATCH"),
    "add_elsif": (m_add_elsif, "NO_ELSIF"),
    "uuid_long": (m_uuid_long, "UUID_TOO_LONG"),
    "dup_uuid": (m_dup_uuid, "UUID_UNIQUE"),
    "dup_as": (m_dup_as, "AS_UNIQUE"),
    "remove_config": (m_remove_config, "CONFIG_PROVIDER_MATCH"),
    "stop_no_reason": (m_stop_no_reason, "STOP_MISSING_REASON"),
    "remove_returns": (m_remove_returns, "RETURN_MISSING"),
    "repeat_no_while": (m_repeat_no_while, "REPEAT_HAS_WHILE_CONDITION"),
    "foreach_no_source": (m_foreach_no_source, "FOREACH_SOURCE"),
    "condition_malformed": (m_condition_malformed, "CONDITION_FORMAT"),
    "wrap_recipe": (m_wrap_recipe, "CODE_WRAPPED_IN_RECIPE"),
}


# --------------------------------------------------------------------------- runner
def golden_files() -> list[Path]:
    rows = json.loads((ROOT / "kb" / "examples" / "index.json").read_text())
    checker = rc.Checker(CATALOG, "corpus")
    good = []
    for r in rows:
        p = ROOT / r["path"]
        if not any(f.level == "error" for f in rc.check_file(p, checker)):
            good.append(p)
    return good


def normalized(p: Path) -> dict:
    doc, code, config, _ = rc.load_recipe(p)
    d = {"name": (doc or {}).get("name", p.stem), "code": copy.deepcopy(code)}
    if isinstance(config, list) and config:
        d["config"] = copy.deepcopy(config)
    else:
        d["config"] = None   # unknown: config rules skipped unless a mutation needs it
    return d


def check_doc(doc: dict) -> list[rc.Finding]:
    checker = rc.Checker(CATALOG, "author")
    if "recipe" in doc and "code" not in doc:
        f = [rc.Finding("CODE_WRAPPED_IN_RECIPE", "error", "")]
        doc = doc["recipe"]
        return f + checker.run(doc, doc["code"], doc.get("config"), False)
    return checker.run(doc, doc["code"], doc.get("config"), False)


def run(per_mutation: int = 25, seed: int = 7, verbose: bool = False) -> dict:
    rnd = random.Random(seed)
    files = golden_files()
    rnd.shuffle(files)
    stats = {}
    for name, (fn, rule) in MUTATIONS.items():
        applied = caught = 0
        misses = []
        for p in files:
            if applied >= per_mutation:
                break
            mutant = fn(normalized(p))
            if mutant is None:
                continue
            applied += 1
            findings = check_doc(mutant)
            if any(f.rule == rule and f.level == "error" for f in findings):
                caught += 1
            else:
                misses.append(str(p.relative_to(ROOT)))
        stats[name] = {"rule": rule, "applied": applied, "caught": caught, "missed": misses[:5]}
        if verbose:
            print(f"{name:22} {rule:28} {caught}/{applied}" + (f"  MISSED e.g. {misses[:2]}" if misses else ""))
    return {"golden_files": len(files), "mutations": stats,
            "total_applied": sum(s["applied"] for s in stats.values()),
            "false_negatives": sum(s["applied"] - s["caught"] for s in stats.values())}


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--per-mutation", type=int, default=25)
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    res = run(a.per_mutation, verbose=not a.json)
    if a.json:
        print(json.dumps(res, indent=1))
    else:
        print(f"\ngolden files: {res['golden_files']} | mutants: {res['total_applied']} | "
              f"false negatives: {res['false_negatives']}")
    sys.exit(1 if res["false_negatives"] else 0)
