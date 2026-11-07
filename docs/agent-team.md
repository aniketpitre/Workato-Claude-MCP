# The virtual Workato engineering team

Status: **DRAFT for review** · Part of [architecture.md](architecture.md) (control plane)

The system is organised like an enterprise Workato Center of Excellence (CoE). Each role is a
specialised Claude agent (a Claude Code subagent in `.claude/agents/`) with:

- **a mandate**: what it owns and decides
- **inputs and outputs**: the artifacts it reads and writes in `automations/<name>/`
- **permissions**: the tools it may use (least privilege, enforced by the agent's tool allowlist plus
  project permission rules)
- **a definition of done**: the gate its work must pass

Agents hand work to each other **through artifacts in git, not chat**, so every handoff is reviewable
and auditable. Only the Engagement Lead talks to you.

---

## 1. Team roster

| # | Role (agent) | Real-world equivalent | Mandate | Main outputs |
| --- | --- | --- | --- | --- |
| 1 | **Engagement Lead** (`workato-lead`, main session) | Delivery manager / CoE lead | Single point of contact; intake, routing, approval gates, status, escalation | `state.json`, status updates to you |
| 2 | **Business Analyst** (`workato-analyst`) | Business/integration analyst | Turn intent into a precise spec with acceptance tests; feasibility (connectors, connections, plan) | `spec.yaml` |
| 3 | **Solution Architect** (`workato-architect`) | Workato solution architect | Solution design: asset breakdown, patterns, data mapping, error and idempotency strategy, standards; **reviews all builds** | `design.md`, review notes |
| 4 | **Integration Developer** (`workato-recipe-dev`) | Recipe developer | Build recipes, recipe functions, data or lookup tables, API endpoints from the design | `recipes/*.recipe.json`, `assets/*.json` |
| 5 | **AI and Agentic Engineer** (`workato-ai-engineer`) | Agent Studio / MCP engineer | Genies, skills, knowledge bases, guardrails, MCP servers and tool design | `assets/genie-*.json`, `assets/mcp-*.json` |
| 6 | **Connector Engineer** (`workato-connector-dev`) | Connector SDK developer | Custom connectors (Ruby SDK) when no connector or action exists; HTTP-action fallbacks | `connectors/<name>/connector.rb` + tests |
| 7 | **QA Engineer** (`workato-qa`) | Test engineer | Independent validation and acceptance testing; never fixes code itself | `reports/validate.json`, `reports/test-*.md` |
| 8 | **Support Engineer** (`workato-support`) | L2/L3 support | Diagnose failed tests or jobs, classify the root cause, propose or apply fixes within the debug budget | `reports/debug-*.md`, patches |
| 9 | **Release Manager** (`workato-release`) | Release / DevOps engineer | Deploy, start, promote (RLCM/packages), rollback, release notes, tags | `CHANGELOG.md`, release records |
| 10 | **Platform Admin and Security** (`workato-admin`) | Workspace admin / security | API clients and roles, connection readiness, secrets hygiene, governance and security review before go-live | `reviews/security.md`, access checklist |
| 11 | **Operations (SRE)** (`workato-ops`) | Run / monitoring team | Health checks, job failure trends, quotas, drift detection, incidents | `ops/health-*.md`, `ops/incidents/*` |
| 12 | **Knowledge Librarian** (`workato-librarian`) | CoE enablement | Keep docs, connector catalog, patterns and examples current; turn debug learnings into playbooks | `kb/**`, `kb/patterns/playbooks/*` |

Roles are spawned only when needed. A simple recipe uses Analyst → Architect → Developer → QA →
Release. A Genie project adds the AI Engineer. A missing connector adds the Connector Engineer.

---

## 2. Separation of duties (enterprise controls)

| Rule | Why |
| --- | --- |
| **Builder ≠ Tester:** Developers and AI or Connector Engineers can't mark their own work as passed; only QA writes test verdicts | Independent verification |
| **Builder ≠ Deployer:** only the Release Manager can start, stop or promote assets, and only after your go-live approval | No unapproved changes reach production |
| **Architect review is mandatory** on every build before QA (design conformance, standards, patterns) | Code-review equivalent |
| **Security review is mandatory** before go-live for anything that touches PII, exposes an API or MCP server, or adds a connection | Governance |
| **Nobody deletes** workspace assets; deletes need your explicit instruction naming the asset, executed by the Release Manager | Destructive-action safety |
| **Only Platform Admin** may touch API clients, roles or access, and only with your approval | Privilege management |

---

## 3. Permissions matrix

Legend: **R** read · **W** create/update (stopped, dev only) · **X** execute/test · **D** deploy/start/stop · — none

| Capability (Workato MCP tools) | Lead | Analyst | Architect | Recipe Dev | AI Eng | Connector Eng | QA | Support | Release | Admin | Ops | Librarian |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KB search and read | R | R | R | R | R | R | R | R | R | R | R | R/W |
| Workspace read (recipes, jobs, connections, projects) | R | R | R | R | R | R | R | R | R | R | R | R |
| Recipes, functions, tables, API endpoints | — | — | — | **W** | — | — | — | **W** (fix) | **D** | — | — | — |
| Genies, skills, KBs, MCP servers | — | — | — | — | **W** | — | — | **W** (fix) | **D** | — | — | — |
| Custom connectors (SDK) | — | — | — | — | — | **W** | — | **W** (fix) | **D** (release) | — | — | — |
| Validators, test cases, force-run in dev | — | — | — | X (self-check) | X (self-check) | X | **X** | X | — | — | — | — |
| Start/stop, packages, RLCM deploy | — | — | — | — | — | — | — | — | **D** | — | — | — |
| API clients, roles, members | — | — | — | — | — | — | — | — | — | **W** (approved) | — | — |
| Any `delete_*` | — | — | — | — | — | — | — | — | on your explicit order | — | — | — |
| Connector catalog / KB sync | — | — | — | — | — | — | — | — | — | — | — | **W** |

Enforcement:
1. Each agent's `tools:` allowlist in `.claude/agents/<role>.md` lists only its permitted `mcp__workato__*` tools.
2. Project permission rules deny `mcp__workato__delete_*` and the member and role tools by default.
3. Separate MCP registrations per environment. Only the Release Manager's session loads test or prod tokens.
4. Separate Workato API clients per role family (builder, deployer, operator, admin), so the Workato
   activity audit log shows which role acted.

---

## 4. How the team works through the lifecycle (RACI)

R = responsible, A = accountable, C = consulted, I = informed. **You** are accountable at the gates.

| Stage | Lead | Analyst | Architect | Builders (Recipe/AI/Connector) | QA | Support | Release | Admin | Ops | Librarian | You |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 Intent | A | **R** | C | — | C (testability) | — | — | C (connections) | — | C | **Approve** |
| 1 Design | A | C | **R** | C | C (test plan) | — | C | C (security) | C (monitoring) | C | **Approve** |
| 2 Build | A | — | C | **R** | — | — | — | — | — | C | I |
| 2b Review | A | — | **R** | I | — | — | — | — | — | — | — |
| 3 Validate | A | — | — | I | **R** | — | — | — | — | — | — |
| 4 Push (stopped) | A | — | — | **R** | C (read-back) | — | — | — | — | — | — |
| 5 Test | A | C (acceptance) | — | I | **R** | — | — | — | — | — | I |
| 6 Debug | A | — | C (design flaws) | C | C (re-test) | **R** | — | — | — | I (learnings) | escalation |
| 6b Security review | A | — | C | — | — | — | — | **R** | — | — | I |
| 7 Deploy | A | — | — | — | C (evidence) | — | **R** | C | I | — | **Approve** |
| 8 Operate | A | — | — | — | — | C | C (rollback) | — | **R** | I | I (reports) |

---

## 5. Collaboration model

```
              You ◀──────▶ Engagement Lead (orchestrator, owns state.json and gates)
                               │ assigns work packages (one per stage or asset)
     ┌──────────┬──────────────┼──────────────┬───────────────┬─────────────┐
     ▼          ▼              ▼              ▼               ▼             ▼
  Analyst   Architect   Builders (in parallel, one per asset)   QA      Release / Admin / Ops
     │          │        Recipe Dev · AI Eng · Connector Eng      │            │
     └─ spec ───┴─ design ──▶ recipes/assets ─▶ Architect review ─▶ QA ─▶ Support (if fail) ─┐
                                                                       ▲                    │
                                                                       └──── fixed build ◀──┘
                          Librarian runs in the background: syncs knowledge, captures learnings
```

- **Work packages:** the Lead splits a design into packages (for example, three recipes and one
  Genie) and runs builders **in parallel**. Each package lists its inputs, the expected output file
  and its done criteria.
- **Handoff contract:** every agent ends by writing its artifact and a short handoff note
  (`reports/handoff-<stage>.md`: what was done, open issues, next owner). The Lead advances `state.json`.
- **Escalation path:** builder → Architect (design questions) → Lead → you. Support escalates after
  5 debug rounds. Admin escalates every access request to you.
- **Learning loop:** after every resolved defect, the Librarian adds the root cause and fix to
  `kb/patterns/playbooks/`, and successful recipes become examples. The team improves with each delivery.

---

## 6. Role definition template (`.claude/agents/<role>.md`)

```markdown
---
name: workato-qa
description: Independent QA for Workato automations. Use to validate recipe JSON and run
  acceptance tests; never modifies recipes.
tools: Read, Grep, Glob, Bash(python3 tools/*), mcp__workato__post_recipe_validators_validate_full,
  mcp__workato__get_recipes_, mcp__workato__post_test_cases_run_requests,
  mcp__workato__get_test_cases_run_requests_, mcp__workato__post_recipes_force_run,
  mcp__workato__get_recipes_jobs, mcp__workato__get_recipes_jobs_
---
Mandate, inputs, outputs, procedure, definition of done, escalation rules ...
```

Every role file follows the same sections: **Mandate · Inputs · Outputs · Procedure · Standards ·
Definition of done · Escalation · Forbidden actions.**

---

## 7. Impact on the roadmap

| Milestone | Team work |
| --- | --- |
| M1 Knowledge | Librarian role defined first (it owns sync and curation) |
| M2 Validation | QA role plus its tools (`recipe_check`, `spec_check`) |
| M3 Loop skeleton | Lead, Analyst, Architect, Recipe Developer roles; work package and handoff contracts; permission rules |
| M4 Test and debug | Support role, error classifier, playbooks |
| M5 Proof | AI Engineer (Genie/MCP), Release Manager; all three reference automations delivered by the team |
| M6 Operate | Ops role, health schedule, incidents |
| M7 Enterprise | Admin and Security role, per-role API clients, multi-environment Release Manager, Connector Engineer |
