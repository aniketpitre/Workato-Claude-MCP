#!/usr/bin/env python3
"""recipe_check: deterministic validator for Workato recipe JSON (QA gate "Validate").

Implements the checklist in kb/patterns/RECIPE_JSON_SPEC.md §9: Workato Labs recipe-lint
rules (tiers 0-3, re-implemented) plus checks against the LIVE connector catalog
(kb/connectors/) that no other validator does: operation names and required inputs.

Usage:
  python3 tools/recipe_check.py automations/foo/recipes/*.recipe.json
  python3 tools/recipe_check.py --profile corpus kb/examples/labs      # directories are walked
  python3 tools/recipe_check.py --json file.json                        # machine-readable
Exit code: 1 if any finding has level "error", else 0.

Profiles:
  author (default)  for recipes we generate: strict; style rules promoted to errors
  corpus            for third-party examples: structural/semantic errors only, style as warnings

Stdlib only. No network.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG_DIR = ROOT / "kb" / "connectors" / "catalog"

KEYWORDS = {"trigger", "action", "if", "elsif", "else", "try", "catch", "foreach", "repeat",
            "while_condition", "stop", "filter"}
NO_PROVIDER = {"if", "elsif", "else", "try", "foreach", "repeat", "while_condition", "stop", "filter"}
NEEDS_AS = {"trigger", "action", "catch", "foreach", "repeat"}
PLATFORM = {"workato_api_platform", "workato_recipe_function", "workato_variable", "workato_skill",
            "workato_db_table", "logger", "clock", "workato_list", "lookup_table", "workato_files",
            "workato_webhooks", "workato_pub_sub", "workato_genie", "workato_custom_code", "workato_template",
            "workato_smart_list", "workato_transformations", "workato_idp", "workato_workflow_task"}
RETURNING_TRIGGERS = {
    ("workato_api_platform", "receive_request"): "workato_api_platform.return_response",
    ("workato_recipe_function", "execute"): "workato_recipe_function.return_result",
    ("workato_skill", "start_workflow"): "workato_skill.workflow_return_result",
}
CUSTOM_CONNECTOR_RE = re.compile(r"_connector_\d+_\d+$")
DP_RE = re.compile(r"_dp\('(\{.*?\})'\)", re.S)
LEGACY_RE = re.compile(r"_\('data\.([A-Za-z0-9_]+)\.([A-Za-z0-9_\-]+)((?:\.[^']*)?)'\)")

# rule -> (default level, description)
RULES = {
    "INVALID_JSON": ("error", "File is not valid JSON"),
    "CODE_WRAPPED_IN_RECIPE": ("error", "Top level must not be wrapped in a 'recipe' key"),
    "MISSING_TOP_LEVEL_KEYS": ("error", "Recipe file is missing required top-level keys"),
    "CODE_NOT_OBJECT": ("error", "'code' must be an object whose keyword is 'trigger'"),
    "CONFIG_INVALID": ("error", "'config' must be an array of application entries"),
    "UNKNOWN_KEYWORD": ("error", "Unknown step keyword"),
    "STEP_MISSING_NUMBER": ("error", "Step is missing 'number'"),
    "NUMBER_NOT_INTEGER": ("error", "Step 'number' must be an integer"),
    "STEP_NUMBER_DUPLICATE": ("error", "Two steps share the same number"),
    "STEP_NUMBERING": ("warn", "Step numbers should be sequential depth-first (0,1,2,...)"),
    "TRIGGER_NUMBER_ZERO": ("error", "Trigger must have number 0"),
    "STEP_MISSING_UUID": ("warn", "Step is missing 'uuid'"),
    "UUID_TOO_LONG": ("error", "uuid longer than 36 characters (import fails)"),
    "UUID_UNIQUE": ("error", "uuid values must be unique"),
    "AS_MISSING": ("error", "Step needs an 'as' alias"),
    "AS_UNIQUE": ("error", "'as' aliases must be unique (datapill ambiguity)"),
    "PROVIDER_MISSING": ("error", "trigger/action needs 'provider' and 'name'"),
    "CONTROL_HAS_PROVIDER": ("warn", "Control-flow step should not have a provider"),
    "CATCH_PROVIDER_NULL": ("warn", "catch should have \"provider\": null"),
    "CATCH_HAS_RETRY": ("info", "catch input should set max_retry_count"),
    "NO_ELSIF": ("warn", "elsif is not allowed by Workato Labs lint; use nested if/else"),
    "ELSE_LAST_IN_IF": ("error", "else must be the last child of its if"),
    "ELSE_OUTSIDE_IF": ("error", "else/elsif must be a child of an if block"),
    "CATCH_LAST_IN_TRY": ("error", "catch must be the last child of its try"),
    "TRY_HAS_CATCH": ("error", "try block must contain a catch"),
    "REPEAT_HAS_WHILE_CONDITION": ("error", "repeat must contain a while_condition"),
    "WHILE_CONDITION_LAST_IN_REPEAT": ("error", "while_condition must be the last child of repeat"),
    "FOREACH_SOURCE": ("error", "foreach needs a 'source' datapill"),
    "STOP_MISSING_REASON": ("warn", "stop should set input.stop_reason"),
    "CONDITION_FORMAT": ("error", "Condition block malformed (needs type/operand/conditions[] with operand+lhs)"),
    "CONFIG_PROVIDER_MATCH": ("error", "Provider used in a step has no config entry"),
    "CONFIG_NO_WORKATO": ("warn", "Config should not list the built-in 'workato' provider"),
    "CONFIG_PLATFORM_NAME": ("warn", "Platform provider config entry should include 'name'"),
    "OP_UNKNOWN_PROVIDER": ("error", "Provider not in the workspace connector catalog"),
    "OP_UNKNOWN_NAME": ("error", "Trigger/action name not found for this provider in the catalog"),
    "OP_UNVERIFIED": ("info", "Custom connector; operation names can't be verified against the catalog"),
    "REQUIRED_INPUT": ("error", "Required input (per catalog) is missing or empty"),
    "DP_VALID_JSON": ("error", "_dp() payload is not valid JSON or lacks provider/line/path"),
    "DP_INT_INDEX": ("error", "Datapill path uses an integer index (invalid path element)"),
    "DP_LINE_RESOLVES": ("error", "Datapill line does not match any step alias"),
    "DP_PROVIDER_MATCHES": ("error", "Datapill provider does not match the referenced step's provider"),
    "DP_STEP_REACHABLE": ("error", "Datapill references a step that is not before it / not in scope"),
    "DP_FOREACH_SCOPE": ("error", "foreach datapill used outside its foreach block"),
    "DP_LHS_NO_FORMULA": ("warn", "Condition lhs should use #{} interpolation, not formula mode"),
    "BODY_FORMULA_MODE": ("warn", "HTTP body field in formula mode may be stripped; use interpolation"),
    "RETURN_MISSING": ("error", "Returning trigger has no return step"),
    "ALL_PATHS_RETURN": ("warn", "Not every path ends with a return (callers may hang or get empty results)"),
    "EMPTY_BLOCK": ("warn", "Control-flow block has no steps"),
}
# Third-party examples may use legacy operations or providers this workspace lacks: report, don't fail.
CORPUS_DEMOTE = {"OP_UNKNOWN_NAME", "OP_UNKNOWN_PROVIDER", "REQUIRED_INPUT", "RETURN_MISSING", "DP_FOREACH_SCOPE"}
SPECIAL_LEGACY_LINES = {"job_context", "recipe", "account_property", "project_property", "user"}
STRICT_PROMOTE = {"STEP_NUMBERING", "STEP_MISSING_UUID", "NO_ELSIF", "STOP_MISSING_REASON", "CATCH_PROVIDER_NULL",
                  "CONFIG_NO_WORKATO", "CONFIG_PLATFORM_NAME", "ALL_PATHS_RETURN", "CONTROL_HAS_PROVIDER",
                  "BODY_FORMULA_MODE"}


@dataclass
class Finding:
    rule: str
    level: str
    message: str
    step: int | None = None
    alias: str | None = None
    detail: str | None = None


@dataclass
class Step:
    block: dict
    number: object
    keyword: str
    provider: str | None
    name: str | None
    alias: str | None
    order: int                      # depth-first position
    parent: "Step | None"
    foreach_scope: tuple = ()       # aliases of enclosing foreach blocks
    catch_scope: tuple = ()         # aliases of enclosing catch blocks
    children: list = field(default_factory=list)


class Catalog:
    def __init__(self, directory: Path):
        self.dir = directory
        self.cache: dict[str, dict | None] = {}
        self.available = directory.exists()

    def get(self, provider: str) -> dict | None:
        if provider not in self.cache:
            p = self.dir / f"{provider}.json"
            self.cache[provider] = json.loads(p.read_text()) if p.exists() else None
        return self.cache[provider]


# --------------------------------------------------------------------------- helpers
def _strings(obj, path=""):
    """Yield (path, string) for every string inside a JSON value."""
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from _strings(v, f"{path}.{k}" if path else k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from _strings(v, f"{path}[{i}]")


def _is_empty(v) -> bool:
    return v is None or (isinstance(v, str) and v.strip() == "") or (isinstance(v, (list, dict)) and not v)


def load_recipe(path: Path) -> tuple[dict | None, dict | None, list | None, list[Finding]]:
    """Return (document, code, config, findings). Accepts our file format, API format (code as string),
    community harvest format, or a bare code object."""
    f: list[Finding] = []
    try:
        doc = json.loads(path.read_text())
    except Exception as e:
        return None, None, None, [Finding("INVALID_JSON", "error", f"{e}")]
    if isinstance(doc, dict) and "recipe" in doc and isinstance(doc["recipe"], dict):
        f.append(Finding("CODE_WRAPPED_IN_RECIPE", "error", RULES["CODE_WRAPPED_IN_RECIPE"][1]))
        doc = doc["recipe"]
    if isinstance(doc, dict) and doc.get("keyword") == "trigger":
        return doc, doc, None, f
    code = doc.get("code") if isinstance(doc, dict) else None
    if isinstance(code, str):
        try:
            code = json.loads(code)
        except Exception as e:
            f.append(Finding("CODE_NOT_OBJECT", "error", f"code string is not JSON: {e}"))
            return doc, None, None, f
    if not isinstance(code, dict) or code.get("keyword") != "trigger":
        f.append(Finding("CODE_NOT_OBJECT", "error", RULES["CODE_NOT_OBJECT"][1]))
        return doc, None, None, f
    config = doc.get("config")
    if isinstance(config, str):
        try:
            config = json.loads(config or "[]")
        except Exception:
            config = "invalid"
    return doc, code, config, f


# --------------------------------------------------------------------------- checker
class Checker:
    def __init__(self, catalog: Catalog | None, profile: str = "author"):
        self.catalog = catalog
        self.profile = profile

    def add(self, out: list, rule: str, step: Step | None = None, detail: str | None = None, level: str | None = None):
        lvl = level or RULES[rule][0]
        if self.profile == "author" and rule in STRICT_PROMOTE:
            lvl = "error"
        if self.profile == "corpus" and rule in CORPUS_DEMOTE and lvl == "error":
            lvl = "warn"
        out.append(Finding(rule, lvl, RULES[rule][1],
                           step.number if step and isinstance(step.number, int) else None,
                           step.alias if step else None, detail))

    # ---- tree
    def build(self, code: dict) -> list[Step]:
        steps: list[Step] = []

        def visit(b: dict, parent: Step | None, fe: tuple, ca: tuple):
            kw = b.get("keyword")
            s = Step(b, b.get("number"), kw, b.get("provider"), b.get("name"), b.get("as") or None,
                     len(steps), parent, fe, ca)
            steps.append(s)
            if parent:
                parent.children.append(s)
            child_fe = fe + ((s.alias,) if kw == "foreach" and s.alias else ())
            child_ca = ca + ((s.alias,) if kw == "catch" and s.alias else ())
            for c in b.get("block") or []:
                if isinstance(c, dict):
                    visit(c, s, child_fe, child_ca)

        visit(code, None, (), ())
        return steps

    # ---- main
    def check(self, doc: dict | None, code: dict, config, require_top_level: bool,
              steps: list[Step]) -> list[Finding]:
        out: list[Finding] = []
        if require_top_level and isinstance(doc, dict) and doc is not code:
            missing = [k for k in ("name", "code", "config") if k not in doc]
            if missing:
                self.add(out, "MISSING_TOP_LEVEL_KEYS", detail=", ".join(missing))
        self.structure(steps, out)
        self.control_flow(steps, out)
        self.config_checks(steps, config, out)
        if self.catalog and self.catalog.available:
            self.catalog_checks(steps, out)
        self.datapills(steps, out)
        self.returns(steps, out)
        return out

    def structure(self, steps: list[Step], out: list):
        seen_nums, seen_uuid, seen_as = {}, {}, {}
        ints = []
        for s in steps:
            b = s.block
            if s.keyword not in KEYWORDS:
                self.add(out, "UNKNOWN_KEYWORD", s, str(s.keyword))
            if "number" not in b:
                self.add(out, "STEP_MISSING_NUMBER", s)
            elif not isinstance(b["number"], int) or isinstance(b["number"], bool):
                self.add(out, "NUMBER_NOT_INTEGER", s, repr(b["number"]))
            else:
                if b["number"] in seen_nums:
                    self.add(out, "STEP_NUMBER_DUPLICATE", s, f"number {b['number']}")
                seen_nums[b["number"]] = s
                ints.append(b["number"])
            if s.order == 0 and b.get("number") != 0:
                self.add(out, "TRIGGER_NUMBER_ZERO", s, repr(b.get("number")))
            u = b.get("uuid")
            if not u:
                self.add(out, "STEP_MISSING_UUID", s)
            else:
                if len(str(u)) > 36:
                    self.add(out, "UUID_TOO_LONG", s, str(u))
                if u in seen_uuid:
                    self.add(out, "UUID_UNIQUE", s, str(u))
                seen_uuid[u] = s
            if s.keyword in NEEDS_AS and not s.alias:
                self.add(out, "AS_MISSING", s)
            if s.alias and s.keyword in NEEDS_AS:
                if s.alias in seen_as:
                    self.add(out, "AS_UNIQUE", s, s.alias)
                seen_as[s.alias] = s
            if s.keyword in ("trigger", "action") and (not s.provider or not s.name):
                self.add(out, "PROVIDER_MISSING", s)
            if s.keyword in NO_PROVIDER and b.get("provider"):
                self.add(out, "CONTROL_HAS_PROVIDER", s, f"{s.keyword} has provider {b.get('provider')}")
            if s.keyword == "catch":
                if b.get("provider") is not None:
                    self.add(out, "CATCH_PROVIDER_NULL", s)
                if "max_retry_count" not in (b.get("input") or {}):
                    self.add(out, "CATCH_HAS_RETRY", s)
            if s.keyword == "stop" and not (b.get("input") or {}).get("stop_reason"):
                self.add(out, "STOP_MISSING_REASON", s)
            if s.keyword in ("if", "elsif", "while_condition"):
                self.condition(s, b.get("input") or {}, out)
            if s.keyword == "trigger" and isinstance(b.get("filter"), dict) and b["filter"].get("conditions"):
                self.condition(s, b["filter"], out)
        if ints and ints != list(range(len(ints))) and len(set(ints)) == len(ints):
            self.add(out, "STEP_NUMBERING", None, f"got {ints[:12]}{'...' if len(ints) > 12 else ''}")

    def condition(self, s: Step, cond: dict, out: list):
        conds = cond.get("conditions")
        if not isinstance(conds, list) or not conds or cond.get("operand") not in ("and", "or"):
            self.add(out, "CONDITION_FORMAT", s, "missing operand/conditions")
            return
        for c in conds:
            if not isinstance(c, dict):
                continue
            if c.get("type") == "compound" or "conditions" in c:   # nested group
                self.condition(s, c, out)
                continue
            if not c.get("operand") or "lhs" not in c:
                self.add(out, "CONDITION_FORMAT", s, f"condition {c.get('uuid')}")
            lhs = c.get("lhs") or ""
            if isinstance(lhs, str) and lhs.startswith("=") and "_dp(" in lhs and lhs.count("_dp(") == 1 \
                    and lhs.strip().startswith("=_dp(") and lhs.strip().endswith("')"):
                self.add(out, "DP_LHS_NO_FORMULA", s)

    def control_flow(self, steps: list[Step], out: list):
        for s in steps:
            kids = [c for c in s.children]
            kws = [c.keyword for c in kids]
            if s.keyword in ("else", "elsif") and (not s.parent or s.parent.keyword != "if"):
                self.add(out, "ELSE_OUTSIDE_IF", s)
            if s.keyword == "elsif":
                self.add(out, "NO_ELSIF", s)
            if s.keyword == "if":
                branch_idx = [i for i, k in enumerate(kws) if k in ("else", "elsif")]
                if "else" in kws and kws.index("else") != len(kws) - 1:
                    self.add(out, "ELSE_LAST_IN_IF", s)
                if branch_idx and any(k not in ("else", "elsif") for k in kws[branch_idx[0]:]):
                    if "else" not in kws or kws.index("else") == len(kws) - 1:
                        self.add(out, "ELSE_LAST_IN_IF", s, "branch followed by a regular step")
            if s.keyword == "try":
                if "catch" not in kws:
                    self.add(out, "TRY_HAS_CATCH", s)
                elif kws[-1] != "catch":
                    self.add(out, "CATCH_LAST_IN_TRY", s)
            if s.keyword == "catch" and (not s.parent or s.parent.keyword != "try"):
                self.add(out, "CATCH_LAST_IN_TRY", s, "catch outside try")
            if s.keyword == "repeat":
                if "while_condition" not in kws:
                    self.add(out, "REPEAT_HAS_WHILE_CONDITION", s)
                elif kws[-1] != "while_condition":
                    self.add(out, "WHILE_CONDITION_LAST_IN_REPEAT", s)
            if s.keyword == "foreach" and not s.block.get("source"):
                self.add(out, "FOREACH_SOURCE", s)
            if s.keyword in ("if", "try", "foreach", "repeat", "catch") and not kids:
                self.add(out, "EMPTY_BLOCK", s)

    def config_checks(self, steps: list[Step], config, out: list):
        if config is None or (self.profile == "corpus" and config == []):
            return
        if not isinstance(config, list) or any(not isinstance(c, dict) or c.get("keyword") != "application" for c in config):
            self.add(out, "CONFIG_INVALID", None)
            return
        configured = {c.get("provider") for c in config}
        if "workato" in configured:
            self.add(out, "CONFIG_NO_WORKATO", None)
        for c in config:
            if c.get("provider") in PLATFORM and c.get("account_id") is None and not c.get("name"):
                self.add(out, "CONFIG_PLATFORM_NAME", None, c.get("provider"))
        used = {s.provider for s in steps if s.keyword in ("trigger", "action") and s.provider}
        for p in sorted(used - configured - {"workato"}):
            self.add(out, "CONFIG_PROVIDER_MATCH", None, p)

    def catalog_checks(self, steps: list[Step], out: list):
        for s in steps:
            if s.keyword not in ("trigger", "action") or not s.provider or not s.name:
                continue
            c = self.catalog.get(s.provider)
            if c is None:
                if CUSTOM_CONNECTOR_RE.search(s.provider) or s.provider.endswith("_connector"):
                    self.add(out, "OP_UNVERIFIED", s, s.provider)
                else:
                    self.add(out, "OP_UNKNOWN_PROVIDER", s, s.provider)
                continue
            ops = c["triggers"] if s.keyword == "trigger" else c["actions"]
            op = next((o for o in ops if o["name"] == s.name), None)
            if op is None:
                if s.name != "__adhoc_http_action":   # custom HTTP action exists on most app connectors
                    self.add(out, "OP_UNKNOWN_NAME", s, f"{s.provider}.{s.name} ({s.keyword})")
                continue
            inp = s.block.get("input") or {}
            for f in op.get("input") or []:
                if not f.get("required") or f.get("visible_if"):
                    continue
                if f.get("type") in ("object", "array") or f.get("properties"):
                    continue        # composite fields are filled via schema builders; not reliably checkable
                if _is_empty(inp.get(f["name"])):
                    self.add(out, "REQUIRED_INPUT", s, f"{s.provider}.{s.name}: '{f['name']}'")

    def datapills(self, steps: list[Step], out: list):
        by_alias = {s.alias: s for s in steps if s.alias}
        for s in steps:
            fields = list(_strings(s.block.get("input") or {}, "input"))
            if s.keyword == "foreach" and isinstance(s.block.get("source"), str):
                fields.append(("source", s.block["source"]))
            if isinstance(s.block.get("filter"), dict):
                fields += list(_strings(s.block["filter"], "filter"))
            for fpath, text in fields:
                if s.provider and s.name == "__adhoc_http_action" and fpath.startswith("input.body") \
                        and text.startswith("="):
                    self.add(out, "BODY_FORMULA_MODE", s, fpath)
                for m in DP_RE.finditer(text):
                    try:
                        pill = json.loads(m.group(1))
                        if pill.get("pill_type", "output") != "output":
                            continue        # project_property, account_property, job_context, ...
                        line, prov, path = pill["line"], pill["provider"], pill.get("path", [])
                        if not line or not isinstance(path, list):
                            raise ValueError("line/path")
                    except Exception:
                        self.add(out, "DP_VALID_JSON", s, m.group(1)[:120])
                        continue
                    if any(isinstance(p, int) for p in path):
                        self.add(out, "DP_INT_INDEX", s, f"{line} {path}")
                    self.resolve(s, line, prov, out, fpath)
                for m in LEGACY_RE.finditer(text):
                    if m.group(1) == "workato" or m.group(2) in SPECIAL_LEGACY_LINES:
                        continue
                    self.resolve(s, m.group(2), m.group(1), out, fpath)

    def resolve(self, s: Step, line: str, prov: str, out: list, fpath: str):
        steps_alias = self._alias
        target = steps_alias.get(line)
        if target is None:
            self.add(out, "DP_LINE_RESOLVES", s, f"line '{line}' in {fpath}")
            return
        expected = {"foreach": "foreach", "catch": "catch", "repeat": "repeat"}.get(target.keyword, target.provider)
        if prov != expected and not (target.keyword == "trigger" and prov == target.provider):
            self.add(out, "DP_PROVIDER_MATCHES", s, f"pill provider '{prov}' vs step '{expected}' ({line})")
        if target.keyword == "foreach":
            if line not in s.foreach_scope and target is not s:
                self.add(out, "DP_FOREACH_SCOPE", s, line)
            return
        if target.order >= s.order and target is not s:
            self.add(out, "DP_STEP_REACHABLE", s, f"'{line}' is step {target.number}, used at step {s.number}")

    # ---- returns
    def returns(self, steps: list[Step], out: list):
        trig = steps[0]
        ret = RETURNING_TRIGGERS.get((trig.provider, trig.name))
        if not ret:
            return
        rp, rn = ret.split(".")
        is_ret = lambda st: st.keyword == "action" and st.provider == rp and st.name == rn
        if not any(is_ret(st) for st in steps):
            self.add(out, "RETURN_MISSING", trig, ret)
            return

        def terminates(seq: list[Step]) -> bool:
            for st in seq:
                if is_ret(st) or st.keyword == "stop":
                    return True
            if not seq:
                return False
            last = seq[-1]
            if last.keyword == "if":
                main = [c for c in last.children if c.keyword not in ("else", "elsif")]
                branches = [c for c in last.children if c.keyword in ("else", "elsif")]
                has_else = any(c.keyword == "else" for c in branches)
                return has_else and terminates(main) and all(terminates(b.children) for b in branches)
            if last.keyword == "try":
                body = [c for c in last.children if c.keyword != "catch"]
                catch = [c for c in last.children if c.keyword == "catch"]
                return terminates(body) and all(terminates(c.children) for c in catch)
            return False

        if not terminates(trig.children):
            self.add(out, "ALL_PATHS_RETURN", trig, f"expected {ret} at the end of every path")

    def run(self, doc, code, config, require_top_level: bool) -> list[Finding]:
        steps = self.build(code)
        self._alias = {}
        for s in steps:
            if s.alias and s.alias not in self._alias:
                self._alias[s.alias] = s
        return self.check(doc, code, config, require_top_level, steps)


# --------------------------------------------------------------------------- CLI
def _looks_like_recipe(p: Path) -> bool:
    try:
        head = p.read_text()[:200000]
    except Exception:
        return False
    return '"keyword"' in head and '"trigger"' in head


def iter_files(paths: list[str]) -> list[Path]:
    files: list[Path] = []
    for p in paths:
        pp = Path(p)
        if pp.is_dir():   # when walking directories, only pick up files that look like recipes
            files += sorted(x for x in pp.rglob("*.json")
                            if x.name not in ("index.json", "catalog.json") and _looks_like_recipe(x))
        else:
            files.append(pp)
    return files


def check_file(path: Path, checker: Checker) -> list[Finding]:
    doc, code, config, findings = load_recipe(path)
    if code is None:
        return findings
    require = checker.profile == "author"
    return findings + checker.run(doc, code, config, require)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--profile", choices=["author", "corpus"], default="author")
    ap.add_argument("--no-catalog", action="store_true", help="skip live-catalog checks")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quiet", action="store_true", help="only print files with errors")
    ap.add_argument("--rules", action="store_true", help="list rules and exit")
    a = ap.parse_args(argv)
    if a.rules:
        for k, (lvl, d) in RULES.items():
            print(f"{k:32} {lvl:5} {d}")
        return 0
    if not a.paths:
        ap.error("give at least one recipe file or directory")
    checker = Checker(None if a.no_catalog else Catalog(CATALOG_DIR), a.profile)
    results, n_err = {}, 0
    for f in iter_files(a.paths):
        fs = check_file(f, checker)
        results[str(f)] = fs
        n_err += sum(1 for x in fs if x.level == "error")
    if a.json:
        print(json.dumps({k: [asdict(x) for x in v] for k, v in results.items()}, indent=1))
    else:
        for f, fs in results.items():
            errs = [x for x in fs if x.level == "error"]
            if a.quiet and not errs:
                continue
            status = "FAIL" if errs else "ok"
            print(f"{status:4} {f}")
            for x in fs:
                if a.quiet and x.level != "error":
                    continue
                loc = f"step {x.step}" if x.step is not None else "recipe"
                print(f"     {x.level:5} {x.rule:28} {loc:9} {x.detail or ''}")
        files_err = sum(1 for v in results.values() if any(x.level == "error" for x in v))
        print(f"\n{len(results)} file(s), {files_err} with errors, {n_err} error(s)")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
