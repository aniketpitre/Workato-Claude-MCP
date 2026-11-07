# Plan: building Workato recipes accurately

Goal: Claude generates recipe JSON that imports, validates, and runs the first time, for any
connector, and then uses the same loop for skills, MCP servers, and Genies.

## 1. Research findings (2026-11-07)

### Where the recipe patterns and JSON format come from (best first)

| # | Source | What it gives | Reliability |
| --- | --- | --- | --- |
| 1 | **Live platform: connector catalog** (`get_workato_cli_v1_connectors?include_schemas=true`, Workato MCP) | Exact trigger and action names, input fields (required or optional, picklists, toggles), output fields for every connector in the workspace | Authoritative. It's what the recipe editor uses. Tested with Slack. |
| 2 | **Live platform: extended schemas** (`post_workato_cli_v1_connectors_schemas_`, `get_recipe_validators_schemas_extended`) | Dynamic fields such as Salesforce object fields and data table columns | Authoritative, but needs a live connection for dynamic fields |
| 3 | **Workato Labs `recipe-skills`** (github.com/workato-devs/recipe-skills, MIT) | Recipe JSON structure, datapill syntax, config section, control flow (if/else, try/catch, foreach, repeat/while, stop), triggers (API endpoint, recipe function, Genie skill, scheduler, data table), patterns, templates, per-connector allowed action lists for 7 connectors | Official and curated |
| 4 | **Workato Labs `recipe-lint`** (79 rules, 4 tiers) | The precise rules a recipe must satisfy: structure, numbering, UUIDs, datapills, EIS/EOS, control-flow terminals, datapill resolution | Official |
| 5 | **Real recipes**: 104 in Workato's sample repos (dewy-resort, dewy-bank, platform-cli examples) plus the workspace's own 8 | Working examples of API endpoint, recipe function, Genie skill, Slack bot, Salesforce, Stripe, scheduler, Python, and variables | Real, exported from Workato |
| 5b | **Workato community library** (thousands of public recipes; 1,549 involve Slack alone). The listing comes from `app.workato.com/browse/recipes?q=app:<app>` (rendered page via Firecrawl); full code comes from public `app.trial.workato.com/recipes/<id>/code.json?community=us` | Real, popular, end-to-end recipes for almost every app, ranked by copy count | Real, community quality (curate by copies and "Workato Tutorial" or Featured authors) |
| 6 | `kb/docs/en/**` (official docs) | Concepts and per-connector field docs | Official, but describes the UI, not JSON |
| 7 | General web | Nothing better. Third-party pages describe the UI only. | Low |

### Facts that affect accuracy

- **Two datapill syntaxes exist.** Workato Labs writes `#{_dp('{"pill_type":"output","provider":"salesforce","line":"<as>","path":["Id"]}')}`.
  Exported recipes in this workspace use the legacy `#{_('data.<provider>.<as>.<field>')}`. The generator
  should emit `_dp` and must be able to read both.
- **The server-side validators are lenient.** `post_recipe_validators_validate` and `validate_full`
  returned `valid: true` for a recipe with a duplicate step number, a misspelled action name, a datapill
  to a step that doesn't exist, and an empty required field. They mostly check fields described by the
  `extended_input_schema` a step carries. **They can't be the only gate.**
- `post_recipe_validators_validate_pre_upload` expects a recipe shape I haven't pinned down yet: every
  shape I tried returned "Recipe must have a trigger". To revisit.
- `extended_input_schema` and `extended_output_schema` on each step matter for the UI and for
  datapill resolution (lint rules `EIS_*`, `DP_PATH_RESOLVES`).
- The create API requires `folder_id`, takes `code` and `config` as JSON **strings**, and doesn't
  accept Home assets.

## 2. Plan

### Phase A: pattern library (in repo, refreshed automatically)

- **A1. Store `recipe-skills`** under `kb/patterns/workato-labs/` with the MIT license and attribution,
  and refresh it from GitHub in the daily sync.
- **A2. Connector catalog.** Harvest every connector's triggers and actions with schemas into
  `kb/connectors/<connector>.json`, plus a compact `kb/connectors/INDEX.md` (name → actions, required
  inputs). Refresh weekly. This is the ground truth for action names and required fields.
- **A3. Example corpus.** Normalize the 104 Labs recipes and the workspace recipes into
  `kb/examples/`, indexed by trigger and action (for example `salesforce/search_sobjects`), and add
  `kb/search.py --examples <connector> [action]`.
- **A3b. Community library.** `kb/community/harvest.py` (done; 12 Slack recipes harvested as a test).
  Next: list the top recipes for each priority app through Firecrawl, harvest about 25–50 per app
  (sorted by copy count, about 1 request per second), and index them by step. Author details aren't
  stored, and email addresses in steps are redacted.
- **A4. One-page recipe JSON spec** (`kb/patterns/RECIPE_JSON_SPEC.md`) distilled from A1–A3: top-level
  shape, block keywords, numbering, UUIDs, aliases, both datapill forms, formulas, config, control
  flow, EIS/EOS, API endpoint and Genie skill return rules, and known pitfalls.

### Phase B: validation loop (several gates, because the server validator is lenient)

- **B1. Local checker** `kb/tools/recipe_check.py` (stdlib), implementing the high-value
  `recipe-lint` rules and two checks against the A2 catalog:
  - structure, numbering, UUID length and uniqueness, alias uniqueness;
  - control-flow child order (else last, catch last, `while_condition`);
  - datapill JSON validity, line and provider resolution, reachability;
  - config contains every provider used;
  - **action and trigger names exist in the catalog**;
  - **required inputs are mapped**.
- **B2. Official linter.** Install on your machine:
  `brew install workato-devs/tap/wk workato-devs/tap/recipe-lint && wk plugins install recipe-lint`,
  then `wk lint recipe.json --skills-path kb/patterns/workato-labs/skills`. Building it in the cloud
  sandbox was blocked.
- **B3. Server checks.** Run `post_recipe_validators_validate_full`, then create the recipe
  **stopped**, read it back with `get_recipes_`, and diff it to catch fields Workato dropped silently.
- **B4. Runtime check** (needs connections): recipe test cases or a test job, then inspect it with
  `get_recipes_jobs_`.

### Phase C: standard build loop (goes into the recipe-builder skill)

1. Research: docs, then catalog schema, then the closest example and template.
2. Plan the steps and get your confirmation.
3. Generate JSON from the closest template.
4. B1 local check.
5. B3 server check.
6. Create the recipe, stopped.
7. Read it back and diff.
8. Connect and test (B4).
9. Start it only with your approval.

### Phase D: proof builds in project **Test**

1. Scheduler → variables → data table write → logger. Platform connectors only, no app sign-in needed.
2. An API endpoint recipe (API platform) with a request and response schema and try/catch.
3. A recipe function → skill → new MCP server exposing it, and a Genie using that skill.
4. App recipes (Slack, Salesforce, Google Drive, …) after you authorize those connections.

## 3. Needed from you

- Approve creating test assets in project **Test**.
- Authorize the app connections you care about in Workato. Without them, recipes can only be built
  and validated, not run.
- Optional: install `wk` and `recipe-lint` locally (B2).
- Tell me your main apps, so A2 and A3 prioritize their patterns.
