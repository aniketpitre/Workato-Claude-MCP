# Workato automation lifecycle: the closed loop

Every automation that Claude builds in Workato moves through the same stages. Each stage produces
an artifact in git and passes a gate before the next one starts. A failure loops back automatically
until the gate passes, or until Claude needs a human decision.

```
 ┌─────────┐   ┌────────┐   ┌───────┐   ┌──────────┐   ┌────────┐   ┌──────┐   ┌────────┐   ┌─────────┐
 │0 INTENT │──▶│1 DESIGN│──▶│2 BUILD│──▶│3 VALIDATE│──▶│4 PUSH  │──▶│5 TEST│──▶│7 DEPLOY│──▶│8 OPERATE│
 └─────────┘   └────────┘   └───────┘   └──────────┘   └────────┘   └──────┘   └────────┘   └─────────┘
      ▲  you       ▲  you        ▲            │ fail          │ diff       │ fail       ▲  you        │
      │ confirm    │ approve     └────────────┴───────────────┴────────────┘            │ approve     │
      │            │                      6 DEBUG (auto-fix loop, max 5 rounds)           │             │
      └────────────┴──────────────── design or requirement problem ◀─────────────────────┴─ incident ──┘
```

## Stages

| # | Stage | What happens | Artifact (in git) | Gate |
| --- | --- | --- | --- | --- |
| 0 | **Intent** | Turn the request into a structured spec: goal, trigger, systems, objects and fields, volumes, SLAs, error policy, and **acceptance tests** (sample input → expected outcome). Check feasibility: connectors exist (catalog), connections are authorized, plan limits. | `automations/<name>/spec.yaml` | **You confirm** the spec |
| 1 | **Design** | Choose assets (recipes, recipe functions, data or lookup tables, API endpoints, MCP servers, skills, Genies) and the pattern for each (from docs, Labs, and community examples). Step-by-step flow, data mapping, error handling, idempotency, naming. | `automations/<name>/design.md` | **You approve** the design |
| 2 | **Build** | Generate recipe JSON from the closest proven template, using catalog field names exactly. | `automations/<name>/recipes/*.recipe.json` | Files exist and parse |
| 3 | **Validate** | (a) local checker: structure, numbering, aliases, datapills, control flow, action names and required fields against the live catalog; (b) Workato server validators; (c) optional `wk lint`. | `automations/<name>/reports/validate.json` | 0 errors |
| 4 | **Push** | Create or update in the Workato project folder, **stopped**. Read back and diff against the source to catch fields Workato dropped. Bind connections. | recipe IDs in `automations/<name>/state.json` | Read-back matches source |
| 5 | **Test** | Run the acceptance tests: recipe test cases (Test Automation API), force-run or poll-now with sample data, or call API endpoints. Inspect each job step and assert the expected outcome. | `automations/<name>/reports/test-<ts>.md` | All acceptance tests pass |
| 6 | **Debug** | For each failure: fetch job details and step errors, classify the cause (mapping, schema, auth or connection, data, logic, rate limit), search docs and examples for the fix, patch the JSON, and go back to step 3. Escalate to you after 5 rounds, or for anything needing a decision or credentials. | `automations/<name>/reports/debug-<ts>.md` | Returns to 3 |
| 7 | **Deploy** | Start the recipes on your approval (and enable API endpoints, MCP servers, Genies). When there are more environments: export a package manifest, promote via Recipe Lifecycle Management, and tag the git release. | `automations/<name>/CHANGELOG.md`, git tag | **You approve** go-live |
| 8 | **Operate** | Scheduled health checks (job failures, stopped recipes, broken connections, quota usage), with incidents fed back into 6 (fix) or 0 (requirement change). Daily docs and catalog sync. | `ops/health-<date>.md` | Healthy, or an incident opened |

Human gates are deliberate: Claude never starts, stops, or deletes production assets, and never
changes a requirement, without your OK. Everything between the gates runs automatically.

## Components to build

| Component | Purpose | Stage |
| --- | --- | --- |
| `automations/_template/` (`spec.yaml`, `design.md`) | Structured intent and acceptance tests | 0, 1 |
| `kb/patterns/` (Labs guides, recipe JSON spec), `kb/connectors/` (live catalog), `kb/community/` + `kb/examples/` | Knowledge for correct design and JSON | 1, 2, 6 |
| `tools/recipe_check.py` | Local deterministic validator (lint rules plus catalog checks) | 3 |
| `tools/recipe_diff.py` | Source vs. read-back comparison | 4 |
| `tools/test_report.py` | Turn job details into pass or fail against the spec's acceptance tests | 5 |
| `tools/error_classifier.py` + `kb/patterns/debug-playbook.md` | Map Workato job errors to causes and fixes | 6 |
| `tools/workspace_export.py` | Snapshot workspace assets into git (history and drift detection) | 7, 8 |
| `.claude/skills/workato-lifecycle` | Orchestrator that runs the loop end to end and enforces gates | all |
| Stage skills (recipe, MCP server, Genie builders, upgraded) | Asset-specific know-how | 1, 2 |
| Scheduled health check | Operate stage | 8 |

Workspace actions (create, update, start, test, jobs) always go through Workato's official MCP
server. The `tools/` scripts are offline helpers: they check, diff, and report on files and on data
Claude fetched through the MCP. They never replace it.

## Build order

1. **Knowledge**: Labs patterns, connector catalog, community examples for the core apps, the recipe JSON spec.
2. **Validate**: `recipe_check.py`, tested against the 104 Labs and 12 community recipes (known-good)
   and against deliberately broken copies.
3. **Loop skeleton**: lifecycle skill, spec and design templates, push with read-back diff.
4. **Test and debug**: test runner and report, error classifier, debug playbook.
5. **Proof**: run three automations through the full loop in project **Test**: scheduler → data
   table; API endpoint with try/catch; recipe function → skill → MCP server → Genie.
6. **Deploy and operate**: workspace export to git, health check, release playbook.
