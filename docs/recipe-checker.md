# Recipe checker (M2): how validation works and how well it works

`tools/recipe_check.py` is the deterministic gate every recipe passes before it reaches Workato.
It's needed because Workato's own server validators are lenient: in testing, they returned
`valid: true` for a recipe with a duplicate step number, a misspelled action, a dangling datapill,
and an empty required field.

## What it checks (47 rules, `python3 tools/recipe_check.py --rules`)

| Tier | Checks |
| --- | --- |
| 0 Structure | JSON validity, no `recipe` wrapper, top-level keys, `code` is a trigger object, `config` shape |
| 1 Steps | keywords, numbers (integer, unique, sequential depth-first, trigger = 0), uuid (present, ≤ 36, unique), `as` (present, unique), provider rules per keyword, catch retry, stop reason, condition format |
| 2 Control flow | else/elsif inside if and else last; catch inside try and last; try has catch; repeat has while_condition (last); foreach has source; empty blocks; **every path returns** for API endpoints, recipe functions and Genie skills |
| 3 Data flow | `_dp` JSON validity, no integer path indexes, datapill line resolves, provider matches the step, step is before use, foreach pills used inside their loop; legacy `_('data.…')` pills too |
| Catalog (unique to us) | provider exists in **this workspace**, trigger or action name exists, **required scalar inputs mapped**; custom connectors reported as unverifiable |
| Config | every used provider configured; no `workato` provider; platform entries have `name` |

Profiles:
- **`author`** (default) for recipes we generate: style rules (numbering, uuid, stop reason, elsif, platform config name, all-paths-return) are errors.
- **`corpus`** for third-party examples: legacy operations, providers missing from this workspace, required inputs, missing returns, and foreach scope are warnings.

## Accuracy (2026-11-07)

| Measure | Result | Target |
| --- | --- | --- |
| Golden corpus: 301 real recipes (228 community, 43 Labs samples, 22 Labs templates, 8 workspace) | **5 files with errors, all verified real defects → 0 false positives** | < 2% |
| Mutation suite: 24 defect types injected into 296 clean recipes | **923 mutants, 923 caught → 0 false negatives** | 0 |
| Runtime | ~3 s for the whole test suite | < 5 s per recipe |

Verified defects in the corpus (`tools/tests/known_defects.json`). The examples index flags these, and
`kb/search.py --examples` ranks them last with a warning:

| File | Defect |
| --- | --- |
| Labs template `control-flow-examples.template.json` | an `if` with two `else` branches; duplicate uuid |
| Labs template `gmail-salesforce-integration.json` | foreach written as `input.items` with no `source`; datapill provider `null` instead of `foreach` |
| community 281543 (Infusionsoft → Xero) | uses `get_contact` at step 15, but it's defined at step 18 inside a branch |
| community 46706736, 67250918 | unfinished steps with no app or action selected |

Also removed from the KB: Workato platform-cli `docs/examples` (synthetic snippets with
non-existent structures, e.g. `actions_if_true`, and a provider absent from the catalog).

## Using it

```bash
python3 tools/recipe_check.py automations/<name>/recipes/          # author profile, exit 1 on errors
python3 tools/recipe_check.py --json file.recipe.json              # for reports
python3 tools/spec_check.py automations/<name>/spec.yaml           # Intent gate
python3 -m unittest discover -s tools/tests -v                     # unit + golden + mutation tests
python3 tools/mutate.py --verbose                                  # full mutation report
```

CI (`.github/workflows/ci.yml`) runs all of the above on every push and PR, plus a credential scan.

## Known limits
- Required inputs are enforced for **scalar** fields without visibility conditions. Composite or
  conditional fields (`visible_if`, schema-builder objects) are validated by Workato's server
  validators and by tests.
- Dynamic outputs (`extends_schema`) can't be verified offline; `DP_PATH_RESOLVES` is left to the
  Push read-back and Test stages.
- Reachability is approximated by depth-first order and loop scope; branch-exclusive references (a
  pill defined only in the if-branch, used after the if) aren't flagged yet.
