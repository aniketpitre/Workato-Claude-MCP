# Workato × Claude: system architecture and design

Status: **DRAFT for review** · Owner: aniketpitre · Last updated: 2026-11-07
Related: [agent-team.md](agent-team.md) (virtual Workato team), [lifecycle.md](lifecycle.md) (closed loop), [recipe-accuracy-plan.md](recipe-accuracy-plan.md) (research)

---

## 1. Purpose

Build a production-grade system in which Claude Code acts as a **Workato automation engineer**. It
takes a business requirement and delivers working, tested, governed Workato assets: recipes, recipe
functions, data tables, API endpoints, MCP servers, skills, and Genies. It then keeps them healthy.
It does this through a repeatable, auditable, closed-loop lifecycle.

### 1.1 Goals

| ID | Goal |
| --- | --- |
| G1 | Turn intent into a deployed automation with human approval only at defined gates |
| G2 | Produce recipes that are correct on the first push in ≥ 80% of cases and pass tests within 5 debug rounds in ≥ 95% |
| G3 | Every change is traceable: requirement → design → code → validation → test → deployment |
| G4 | Safe by default: least privilege, no secrets in git, no unapproved production changes |
| G5 | Knowledge stays current with Workato automatically (docs, connectors, patterns) |
| G6 | Works the same for one developer or a team, from one workspace to dev/test/prod |

### 1.2 Non-goals

- Replacing Workato's runtime, editor, or official MCP server. **Workato executes; this system engineers.**
- Building a custom MCP server or proxy for the Workato API.
- Fully unattended production changes. Humans approve go-live.

---

## 2. Requirements

### 2.1 Functional

| ID | Requirement |
| --- | --- |
| F1 | Capture intent as a structured, versioned spec with acceptance tests |
| F2 | Check feasibility: connectors exist, connections are authorized, quotas and plan features are available |
| F3 | Produce a solution design (assets, patterns, data mapping, error handling) for approval |
| F4 | Generate recipe JSON and related asset definitions from proven patterns |
| F5 | Validate deterministically (local) and against the platform (server) before any push |
| F6 | Push to a target workspace or environment idempotently; verify by read-back diff |
| F7 | Execute acceptance tests and produce a pass or fail report with evidence |
| F8 | Diagnose failed jobs, auto-fix within limits, and escalate with a clear summary otherwise |
| F9 | Deploy (start or enable) on approval; promote across environments via packages/RLCM |
| F10 | Monitor production health and route incidents back into the loop |
| F11 | Snapshot workspace assets into git; detect drift between git and workspace |
| F12 | Keep the knowledge base (docs, catalog, Labs patterns, community examples) synchronized |

### 2.2 Non-functional

| Area | Requirement |
| --- | --- |
| Security | API tokens only via environment or secret store, one per environment, least-privilege API client roles; secrets and PII never committed; human gate before any production mutation |
| Auditability | Every lifecycle transition recorded in git (artifact + commit); Workato activity audit log correlates by API client |
| Reliability | Pushes are idempotent and resumable; rollback to the previous recipe version in one step; no partial deployments left running |
| Correctness | Validation gate blocks on any error; tests run against acceptance criteria, not just "job succeeded" |
| Maintainability | Rules, patterns, and catalog are data (JSON/Markdown), not code; tooling has unit tests and CI |
| Portability | Any data center (US, EU, JP, SG, AU, trial); any number of workspaces and environments via config |
| Performance | Validation < 5 s per recipe; full KB sync < 2 min; a typical single recipe goes from intent to tested in < 30 min of agent time |
| Cost | Stdlib-only Python tooling; no hosted infrastructure beyond GitHub Actions and Workato |

---

## 3. Context and constraints (as of 2026-11-07)

| Fact | Impact on design |
| --- | --- |
| Workspace is the **Free plan**, single environment **Development**, trial data center | Design for multi-environment, but run dev-only now; promotion stages are no-ops until test and prod exist |
| **AIRO is not available** on this plan | Use the official **Developer API MCP server** (`/mcp`, 299 tools); no dependency on AIRO tools |
| Workspace has 8 recipes, 0 connections, 2 projects | Live tests need connections authorized by a human; platform-only connectors can be tested immediately |
| Server recipe validators are lenient (passed a broken recipe) | A local deterministic validator is mandatory (ADR-3) |
| Community recipe code is reachable via an undocumented public endpoint | Treat as best-effort enrichment, never a hard dependency (ADR-5) |
| Cloud sandbox blocks `www.workato.com`, the CDN, and building external code | The official `wk`/`recipe-lint` run on developer machines or CI, not in the cloud sandbox |
| MCP API-token identity = API client; actions are attributed to it | Separate API clients per environment and purpose (build vs. operate) |

---

## 4. Architecture overview

```
                         ┌─────────────────────────── Developer / Approver ───────────────────────────┐
                         │      requirement · approvals at gates (spec, design, go-live) · escalations │
                         └───────────────┬────────────────────────────────────────────▲───────────────┘
                                         ▼                                            │
┌──────────────────────────────────── CLAUDE CODE (agent) ───────────────────────────────────────────────┐
│  CONTROL PLANE                                                                                          │
│   lifecycle orchestrator skill ─ state machine, gates, retry budget, escalation                         │
│   stage skills: intent · design · recipe-builder · mcp-server-builder · genie-builder · debug · operate │
│                                                                                                        │
│  KNOWLEDGE PLANE (read-only, versioned in git)              TOOLING (offline, deterministic)           │
│   kb/docs        official docs (4.5k pages, daily)          tools/recipe_check   validate JSON          │
│   kb/connectors  live catalog: actions, fields (weekly)     tools/recipe_diff    source vs read-back    │
│   kb/patterns    Labs skills, JSON spec, playbooks          tools/test_report    acceptance evaluation  │
│   kb/community   curated community recipes (monthly)        tools/error_classify job error → cause/fix  │
│   kb/examples    Labs samples + own recipes                 tools/ws_snapshot    workspace → git        │
└───────────────┬─────────────────────────────────────────────────────────────┬──────────────────────────┘
                │ all workspace actions                                       │ artifacts, history
                ▼                                                             ▼
┌──────────── EXECUTION PLANE ────────────┐                    ┌────────── SOURCE OF TRUTH (git) ──────────┐
│ Workato official MCP server (per env)   │                    │ automations/<name>/ spec, design, recipes, │
│  dev  → app.trial.workato.com/mcp       │                    │   reports, state, changelog               │
│  test → <test env token>                │◀── drift check ───▶│ workspace/<env>/ snapshots                │
│  prod → <prod env token>                │                    │ kb/ …  · tools/ … · .github/workflows/ …   │
│ Workato runtime: recipes, jobs, Genies  │                    └─────────────────────┬─────────────────────┘
└─────────────────────────────────────────┘                                          │
                                                               ┌──────── CI (GitHub Actions) ─────────┐
                                                               │ PR: unit tests, recipe_check on all   │
                                                               │     automations, spec schema check    │
                                                               │ schedule: KB/catalog sync, health     │
                                                               └───────────────────────────────────────┘
```

**Principles**

1. **Git is the source of truth** for everything Claude builds. The workspace is a deployment target.
2. **Workato's official MCP is the only path to the workspace.** Local tools never hold credentials.
3. **Deterministic checks before probabilistic judgment.** The model proposes, tools verify, humans approve.
4. **Knowledge is data.** Rules, patterns, and catalogs are files that update without code changes.
5. **Fail closed.** If a gate can't be evaluated (tool error, missing connection), the loop stops and reports.

---

## 5. Components

### 5.1 Control plane

The control plane is a **virtual Workato engineering team** of 12 specialised agents (Engagement
Lead, Business Analyst, Solution Architect, Integration Developer, AI and Agentic Engineer, Connector
Engineer, QA, Support, Release Manager, Platform Admin and Security, Operations, Knowledge
Librarian), with separation of duties and per-role permissions. See **[agent-team.md](agent-team.md)**.
The skills below are the procedures those agents follow.

| Component | Responsibility |
| --- | --- |
| `workato-lifecycle` skill | Drives one automation through the state machine (§6); enforces gates, the retry budget (5 debug rounds), and escalation; writes `state.json` |
| `workato-intent` skill | Interviews the requester and writes `spec.yaml`; runs the feasibility check (catalog, connections, plan) |
| `workato-design` skill | Selects assets and patterns; writes `design.md` with the data mapping, error strategy, naming, and test plan |
| Builder skills (recipe, MCP server, Genie) | Asset-specific generation rules and templates |
| `workato-debug` skill | Error triage using `error_classify` plus the debug playbook; proposes and applies patches |
| `workato-operate` skill | Health checks, incident creation, routing back to debug or intent |
| `CLAUDE.md` | Global rules: gates, safety, citation of sources |

### 5.2 Knowledge plane

| Store | Source | Refresh | Notes |
| --- | --- | --- | --- |
| `kb/docs` | docs.workato.com `llms.txt` / `llms-full.txt` / sitemap | daily (CI) | Done: 4,513 pages, FTS search |
| `kb/connectors` | `get_workato_cli_v1_connectors?include_schemas` | weekly | Ground truth for action and field names; diff drives re-validation |
| `kb/patterns` | Workato Labs `recipe-skills` (MIT) + our JSON spec and playbooks | weekly | Attributed; local playbooks evolve from debug learnings |
| `kb/community` | Community library (public) | monthly, curated | Redacted, ranked by copies; best-effort (ADR-5) |
| `kb/examples` | Labs sample repos + our own successful recipes | on change | Our own passing recipes become first-class examples (learning loop) |

### 5.3 Tooling (stdlib Python, unit-tested)

| Tool | Input → output | Gate |
| --- | --- | --- |
| `recipe_check.py` | recipe JSON + catalog → errors and warnings (lint tiers 0–3 plus catalog checks) | Validate |
| `recipe_diff.py` | source JSON + read-back JSON → semantic diff (ignores server-generated fields) | Push |
| `test_report.py` | spec acceptance tests + job details → pass or fail report | Test |
| `error_classify.py` | job error payload → category, likely cause, playbook entry | Debug |
| `ws_snapshot.py` | API listings → `workspace/<env>/` normalized files; drift report | Operate |
| `spec_check.py` | `spec.yaml` → schema validation | Intent |

The tools read data that Claude fetched through the MCP (saved to files) and write reports. They hold
no tokens and make no network calls (except the KB sync jobs).

### 5.4 Execution plane

The official Workato MCP server, one registration per environment (`workato-dev`, `workato-test`,
`workato-prod`), each with its own API client and token in environment variables. **Production
tokens are never loaded in a build session by default**; the deploy stage loads them explicitly.

---

## 6. Lifecycle state machine

```
draft ─▶ specified ─(gate: you)─▶ designed ─(gate: you)─▶ built ─▶ validated ─▶ pushed ─▶ tested
  ▲            ▲                       ▲                     ▲          │ fail     │ diff     │ fail
  │            │                       │                     └── debugging (≤5) ◀──┴──────────┘
  │            └──── requirement change ┴─── design flaw ◀───────────┘  │ budget exhausted
  │                                                                     ▼
  │                                                                 escalated ─▶ (you decide)
tested ─(gate: you)─▶ deployed ─▶ operating ─▶ incident ─▶ debugging | specified
                         └─ rollback ─▶ previous version
```

`automations/<name>/state.json` records the current state, history (timestamp, actor, commit),
workspace asset IDs per environment, debug round count, and last report paths. Each transition is
one commit, so `git log automations/<name>` is the audit trail.

**Gate criteria**

| Gate | Pass condition |
| --- | --- |
| Spec | Schema-valid; ≥ 1 acceptance test; feasibility OK or gaps listed; **human confirm** |
| Design | Every spec requirement mapped to an asset or step; error strategy and naming set; **human approve** |
| Validate | `recipe_check` 0 errors; server validators 0 errors; warnings justified in report |
| Push | Read-back diff empty (ignoring allowed server fields); connections bound |
| Test | 100% acceptance tests pass with evidence (job IDs) |
| Deploy | Tests passed on the same commit; **human approve**; rollback point recorded |

---

## 7. Repository layout (target)

```
.mcp.json                      MCP registrations (dev; test/prod added when they exist)
CLAUDE.md                      global agent rules
.claude/skills/                lifecycle + stage skills
automations/
  _template/                   spec.yaml, design.md
  <name>/                      spec.yaml, design.md, recipes/*.recipe.json, assets/*.json,
                               reports/, state.json, CHANGELOG.md
kb/                            docs/, connectors/, patterns/, community/, examples/, search.py, sync.py
tools/                         recipe_check.py, recipe_diff.py, test_report.py, error_classify.py,
                               ws_snapshot.py, spec_check.py, tests/
workspace/<env>/               normalized snapshots of live assets (drift detection)
ops/                           health reports, incidents
docs/                          architecture.md (this), lifecycle.md, ADRs, runbooks
.github/workflows/             ci.yml (tests + checks), sync-*.yml, health.yml
```

---

## 8. Environments and promotion

| Topology | When | Promotion mechanism |
| --- | --- | --- |
| **Single workspace, single env** (today) | Free plan | Build → test → start in Development; git tag = release |
| Workspace environments (Dev/Test/Prod) | Plans with environments | Build in Dev → `projects/:id/build` → `project_builds/:id/deploy` to Test or Prod (RLCM), with environment-specific properties and connections |
| Separate workspaces per stage | Some enterprises | Export package (manifest) from dev → import into test or prod via packages API |

Environment config lives in `config/environments.yaml` (data center URL, MCP registration name,
project or folder IDs, connection mapping by logical name, e.g. `crm` → connection ID per env).
Recipes reference logical connections; push resolves them per environment. **No environment IDs
are hardcoded in recipe source.**

---

## 9. Security and governance

| Control | Implementation |
| --- | --- |
| Credentials | Tokens only in env vars or a secret store; `.mcp.json` uses `${WORKATO_API_TOKEN_<ENV>}`; secret scanning in CI; Workato's GitHub secret scanning is on for `wrk*` tokens |
| Least privilege | API client roles: **builder** (dev: recipes, folders, connections read, validators, test cases); **deployer** (RLCM/packages, start/stop); **operator** (read jobs and health, read-only). No role has member or role management. |
| Human gates | Spec, design, go-live; plus any delete, stop of a running prod asset, or connection change |
| Destructive operations | Never automatic; `delete_*` tools need an explicit instruction naming the asset |
| Data protection | Test data synthetic by default; reports redact emails, tokens, and long IDs; job payloads aren't committed unless redacted |
| Untrusted content | Docs, community recipes, and job outputs are data, never instructions; community code is sanitized and reviewed before reuse |
| Audit | Git history per automation, plus the Workato activity audit log (actions attributed to the API client); release tags |
| Compliance | Respect Workato community policy (attribution, examples only); MIT attribution for Labs content |

---

## 10. Reliability

- **Idempotent push:** the asset identity is (environment, folder, logical name) → workspace ID in `state.json`. A rerun updates the asset instead of duplicating it. A crash mid-push resumes from state.
- **Atomic deploy of multi-asset solutions:** push everything stopped → test → start in dependency order (functions → callers → triggers). On failure, stop everything started in this deploy.
- **Rollback:** Workato recipe versions plus git tags. Rollback means pushing the previous tagged source, or restoring the previous version, then restarting.
- **Retry policy:** API calls back off on 429/5xx; the debug loop has a hard budget of 5 rounds per stage entry.
- **Concurrency:** one active lifecycle per automation (lock in `state.json`); recipe concurrency is set explicitly in the design.

---

## 11. Quality strategy

### 11.1 Testing the system itself

| Layer | Tests |
| --- | --- |
| Tools | Unit tests (`tools/tests/`), run in CI on every PR |
| Validator accuracy | **Golden corpus:** 104 Labs, 12+ community, and our own recipes must pass. **Mutation corpus:** auto-generated broken variants (bad numbering, wrong action, dangling datapill, missing required field, misordered else/catch) must fail with the right rule. Target: 0 false negatives on the mutation set, < 2% false positives on the golden set. |
| End to end | Three reference automations (§13, M5) re-run monthly in dev as a regression |

### 11.2 Standards for generated assets

Naming per `kb/docs/en/recipes/naming-conventions.md`; every external call wrapped in monitor/try
with a logged and re-raised or handled error; idempotent writes (search before create, or upsert);
explicit concurrency and job retention settings; descriptions on every recipe and skill; API
endpoints with defined response codes; Genie skills with clear descriptions and safe failure returns.

---

## 12. Observability and metrics

| Metric | Source | Target |
| --- | --- | --- |
| First-push validity | validate reports | ≥ 80% |
| Debug rounds to green | state history | median ≤ 2 |
| Acceptance pass rate at deploy | test reports | 100% |
| Production job failure rate | health checks | < 1% per recipe per week |
| Mean time to repair | incidents | < 1 day |
| KB freshness | sync logs | docs < 24 h, catalog < 7 d |

`ops/health-<date>.md` is written by the scheduled health job; incidents in `ops/incidents/`.

---

## 13. Roadmap (milestones with exit criteria)

| M | Deliverable | Exit criteria |
| --- | --- | --- |
| **M0** | This design approved; open questions (§15) answered | Your sign-off |
| **M1** ✅ 2026-11-07 | Knowledge plane complete: connector catalog, Labs patterns, recipe JSON spec, community corpus for core apps, examples index | Catalog covers all connectors in workspace; JSON spec reviewed; ≥ 300 example recipes indexed. **Met:** 324 connectors / 913 triggers / 3,161 actions; spec written; 309 examples |
| **M2** | Validation: `recipe_check`, `spec_check`, golden and mutation corpora, CI workflow | 0 false negatives on mutations, < 2% false positives on golden; CI green |
| **M3** | Loop skeleton: lifecycle skill, templates, `state.json`, push + read-back diff, environment config | One recipe goes intent → pushed with all artifacts committed |
| **M4** | Test and debug: test runner and report, error classifier, debug playbook | Seeded failures are auto-fixed within budget in ≥ 4 of 5 cases |
| **M5** | Proof in **Test** project: (1) scheduler → data table; (2) API endpoint with try/catch; (3) recipe function → skill → MCP server → Genie | All three reach `deployed` via the loop with full audit trail |
| **M6** | Operate: workspace snapshot and drift, health job, incident flow, rollback runbook | Weekly health report; drift detected in a seeded test; rollback rehearsed |
| **M7** | Enterprise extensions: multi-env promotion (RLCM/packages), role-separated tokens, team workflow (PR review of specs and designs) | Dry-run promotion documented; ready to activate when environments exist |

---

## 14. Key decisions (ADRs)

| ADR | Decision | Rationale |
| --- | --- | --- |
| 1 | Use Workato's official Developer API MCP server; build no custom server | Your requirement; officially supported; respects API client roles |
| 2 | Git is the source of truth; the workspace is a target | Audit, review, rollback, drift detection |
| 3 | Local deterministic validator is mandatory; server validators are advisory | Server validators passed a broken recipe in testing |
| 4 | Recipes are generated from proven examples, not from scratch | Highest first-push accuracy; real field and UI conventions |
| 5 | Community corpus is best-effort enrichment | Undocumented endpoint; content quality varies |
| 6 | Human gates at spec, design, and go-live; everything else automated | Balance speed with enterprise control |
| 7 | Stdlib-only Python tooling; no hosted services | Zero ops cost; runs in cloud sandbox, laptops, and CI |
| 8 | Logical connection names resolved per environment | Portability across environments and workspaces |

---

## 15. Risks and mitigations

| Risk | Likelihood | Mitigation |
| --- | --- | --- |
| Workato changes recipe JSON or connector schemas | Medium | Weekly catalog diff → re-validate affected automations; Labs patterns sync |
| Generated recipe imports but behaves wrongly | Medium | Acceptance tests with expected outcomes, not just job success |
| Token leak | Low | Env-only tokens, secret scanning, least-privilege roles, rotation runbook |
| Agent makes an unapproved production change | Low | Prod token not loaded by default; gates; destructive-op policy |
| Community endpoint disappears | Medium | Corpus cached in git; system works without it |
| Free plan limits (single env, no AIRO, quotas) | Certain | Design is plan-agnostic; promotion features activate when available |
| Missing connections block testing | High (today) | Platform-only reference automations first; connection checklist in spec feasibility |

---

## 16. Open questions for sign-off

1. **Scope of users:** just you, or a team (PR-based reviews of specs and designs)?
2. **Environments:** stay on the Free single environment for now, or is a paid or sandbox workspace with Dev/Test/Prod expected?
3. **Priority apps** for the catalog focus and community corpus (default: Salesforce, Slack, Google Sheets/Drive, Jira, ServiceNow, NetSuite, Workday, HubSpot, Zendesk + Workato platform tools).
4. **First real use case** to run through the loop after M5.
5. **Approval channel:** approvals in the Claude conversation (default), or also via PR review in GitHub?
6. **Data policy:** may test runs use real records in connected apps, or synthetic data only (default)?
