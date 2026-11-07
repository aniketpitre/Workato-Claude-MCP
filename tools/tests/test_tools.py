"""Unit and corpus tests for the validation tooling.  Run:  python3 -m unittest discover -s tools/tests -v"""
from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))

import mutate  # noqa: E402
import recipe_check as rc  # noqa: E402
import spec_check  # noqa: E402


def pill(provider, line, path):
    return "#{_dp('" + json.dumps({"pill_type": "output", "provider": provider, "line": line, "path": path},
                                  separators=(",", ":")) + "')}"


VALID = {
    "name": "Unit test recipe",
    "version": 1, "private": True, "concurrency": 1,
    "config": [
        {"keyword": "application", "name": "workato_recipe_function", "provider": "workato_recipe_function",
         "skip_validation": False, "account_id": None},
        {"keyword": "application", "name": "logger", "provider": "logger", "skip_validation": False, "account_id": None},
    ],
    "code": {
        "number": 0, "keyword": "trigger", "provider": "workato_recipe_function", "name": "execute", "as": "trigger",
        "input": {"parameters_schema_json": "[{\"name\":\"email\",\"type\":\"string\"}]",
                  "result_schema_json": "[{\"name\":\"ok\",\"type\":\"boolean\"}]"},
        "uuid": "trigger-001",
        "block": [
            {"number": 1, "keyword": "try", "input": {}, "uuid": "try-001", "block": [
                {"number": 2, "keyword": "action", "provider": "logger", "name": "log_message", "as": "log1",
                 "input": {"message": "Email " + pill("workato_recipe_function", "trigger", ["parameters", "email"]),
                           "user_logs_enabled": "false"}, "uuid": "log-001"},
                {"number": 3, "keyword": "action", "provider": "workato_recipe_function", "name": "return_result",
                 "as": "ret_ok", "input": {"result": {"ok": "true"}}, "uuid": "ret-ok-001"},
                {"number": 4, "keyword": "catch", "provider": None, "as": "catch1",
                 "input": {"max_retry_count": "0", "retry_interval": "2"}, "uuid": "catch-001", "block": [
                     {"number": 5, "keyword": "action", "provider": "workato_recipe_function", "name": "return_result",
                      "as": "ret_err", "input": {"result": {"ok": "false"}}, "uuid": "ret-err-001"}]},
            ]},
        ],
    },
}


def run_checker(doc, profile="author"):
    ch = rc.Checker(rc.Catalog(rc.CATALOG_DIR), profile)
    return ch.run(doc, doc["code"], doc.get("config"), True)


def errors(findings):
    return {f.rule for f in findings if f.level == "error"}


class RecipeCheckUnit(unittest.TestCase):
    def test_valid_recipe_has_no_errors(self):
        self.assertEqual(errors(run_checker(copy.deepcopy(VALID))), set())

    def test_file_roundtrip_and_cli_exit_codes(self):
        with tempfile.TemporaryDirectory() as d:
            good = Path(d, "good.recipe.json")
            good.write_text(json.dumps(VALID))
            self.assertEqual(rc.main([str(good), "--quiet"]), 0)
            bad = copy.deepcopy(VALID)
            bad["code"]["block"][0]["block"][0]["name"] = "log_mesage"
            badp = Path(d, "bad.recipe.json")
            badp.write_text(json.dumps(bad))
            self.assertEqual(rc.main([str(badp), "--quiet"]), 1)

    def test_api_format_code_as_string(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d, "api.json")
            p.write_text(json.dumps({"name": "x", "code": json.dumps(VALID["code"]), "config": json.dumps(VALID["config"])}))
            doc, code, config, f = rc.load_recipe(p)
            self.assertEqual(code["keyword"], "trigger")
            self.assertIsInstance(config, list)

    def test_missing_return_on_catch_path(self):
        doc = copy.deepcopy(VALID)
        doc["code"]["block"][0]["block"][2]["block"] = [
            {"number": 5, "keyword": "action", "provider": "logger", "name": "log_message", "as": "log2",
             "input": {"message": "failed", "user_logs_enabled": "false"}, "uuid": "log-002"}]
        self.assertIn("ALL_PATHS_RETURN", errors(run_checker(doc)))

    def test_special_pills_are_not_flagged(self):
        doc = copy.deepcopy(VALID)
        log = doc["code"]["block"][0]["block"][0]
        log["input"]["message"] = ("#{_dp('{\"pill_type\":\"project_property\",\"property_name\":\"env\"}')} "
                                   "#{_('data.workato.job_context.id')}")
        self.assertEqual(errors(run_checker(doc)), set())

    def test_catch_pill_in_scope(self):
        doc = copy.deepcopy(VALID)
        catch = doc["code"]["block"][0]["block"][2]
        catch["block"][0]["input"]["result"]["ok"] = pill("catch", "catch1", ["message"])
        self.assertNotIn("DP_PROVIDER_MATCHES", errors(run_checker(doc)))

    def test_corpus_profile_demotes_legacy_operations(self):
        doc = copy.deepcopy(VALID)
        doc["code"]["block"][0]["block"][0]["name"] = "legacy_op"
        self.assertIn("OP_UNKNOWN_NAME", errors(run_checker(doc, "author")))
        self.assertNotIn("OP_UNKNOWN_NAME", errors(run_checker(doc, "corpus")))


class GoldenCorpus(unittest.TestCase):
    """Every real recipe passes, except the verified defects recorded in known_defects.json."""

    def test_golden_corpus_matches_known_defects(self):
        known = json.loads((TOOLS / "tests" / "known_defects.json").read_text())["files"]
        checker = rc.Checker(rc.Catalog(rc.CATALOG_DIR), "corpus")
        got = {}
        for d in ("kb/examples", "kb/community/recipes", "kb/patterns/workato-labs"):
            for p in rc.iter_files([str(ROOT / d)]):
                errs = sorted({f.rule for f in rc.check_file(p, checker) if f.level == "error"})
                if errs:
                    got[str(p.relative_to(ROOT))] = errs
        self.assertEqual(got, known, "golden corpus errors changed: new false positive or fixed defect")


class Mutations(unittest.TestCase):
    """Every injected defect is detected (zero false negatives)."""

    def test_zero_false_negatives(self):
        res = mutate.run(per_mutation=15)
        missed = {k: v for k, v in res["mutations"].items() if v["caught"] != v["applied"]}
        self.assertFalse(missed, f"false negatives: {missed}")
        self.assertGreater(res["total_applied"], 300)


class SpecCheck(unittest.TestCase):
    def setUp(self):
        import yaml
        self.spec = yaml.safe_load((ROOT / "automations" / "_template" / "spec.yaml").read_text())

    def test_template_is_valid(self):
        self.assertFalse([r for r in spec_check.check(self.spec) if r["level"] == "error"])

    def test_missing_acceptance_tests(self):
        s = copy.deepcopy(self.spec)
        s["acceptance_tests"] = []
        self.assertTrue(any(r["field"] == "acceptance_tests" for r in spec_check.check(s)))

    def test_unknown_connector(self):
        s = copy.deepcopy(self.spec)
        s["systems"][0]["connector"] = "salesforcee"
        self.assertTrue(any(r["field"] == "systems[0].connector" for r in spec_check.check(s)))

    def test_confirmed_needs_approval(self):
        s = copy.deepcopy(self.spec)
        s["status"] = "confirmed"
        self.assertTrue(any(r["field"] == "approvals" for r in spec_check.check(s)))


if __name__ == "__main__":
    unittest.main()
