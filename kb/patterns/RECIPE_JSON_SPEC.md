# Workato recipe JSON: working specification

The single reference Claude uses to write recipe JSON. Distilled from Workato Labs `recipe-skills`
and `recipe-lint` (MIT, `kb/patterns/workato-labs/`), the live connector catalog
(`kb/connectors/`), and 309 real recipes (`kb/examples/index.json`). Where sources disagree,
**precedence is: live catalog > real exported recipes > Labs docs > general docs.**

---

## 1. Source of truth for names

| Question | Answer from |
| --- | --- |
| Does provider X have trigger or action Y? | `kb/connectors/catalog.json` (exact `name`s) |
| What inputs does it take, and which are required? | `kb/connectors/catalog/<provider>.json` → `input[]` (`required`, `toggle_field`, `pick_list`, `visible_if`) |
| What does it output (datapill paths)? | same file → `output[]` (dynamic objects need `extends_schema` lookups via MCP `post_workato_cli_v1_connectors_schemas_` or a live connection) |
| How do real recipes use it? | `python3 kb/search.py --examples <provider.action>` |

Verified examples of catalog-over-docs:

- Genie skill trigger is **`workato_skill.start_workflow`**, returned with **`workato_skill.workflow_return_result`**. Labs docs mention `workato_genie`, but in this workspace `workato_genie` only has actions (`create_task`, `assign_task_to_genie`, …).
- Data tables: search is **`workato_db_table.get_records`** (there's no `search_records`).
- `workato_utility.*` appears in older examples but **isn't in this workspace's catalog**. Don't use it.

---

## 2. Recipe file (what we store in git)

```json
{
  "name": "Sync new Salesforce leads to Slack",
  "description": "What it does, trigger, outputs, owner.",
  "version": 1,
  "private": true,
  "concurrency": 1,
  "config": [ { "keyword": "application", "provider": "salesforce", "skip_validation": false, "account_id": null } ],
  "code": { "number": 0, "keyword": "trigger", "...": "..." }
}
```

- **Developer API create/update** (`post_recipes` / `put_recipes_`) takes
  `{"recipe": {"name", "description", "folder_id", "code": "<JSON STRING>", "config": "<JSON STRING>"}}`.
  `code` and `config` are **strings**. `folder_id` is required, and Home assets is rejected.
- Don't wrap the file in a `"recipe"` key (lint `CODE_WRAPPED_IN_RECIPE`).

### 2.1 `config`

One entry per provider used in any step, except the built-in `workato` provider (never use it).

| Provider kind | Entry |
| --- | --- |
| Platform (no connection): `workato_api_platform`, `workato_recipe_function`, `workato_variable`, `workato_skill`, `workato_db_table`, `logger`, `clock`, `workato_list`, … | `{"keyword":"application","name":"<provider>","provider":"<provider>","skip_validation":false,"account_id":null}`. **`name` is required.** |
| App connector (needs connection) | `{"keyword":"application","provider":"salesforce","skip_validation":false,"account_id":null}` in source; bind the real connection after push with `put_recipes_connect`, or set `account_id` to the connection reference |

Connection IDs are environment-specific. Keep them out of source; resolve them per environment (architecture §8).

---

## 3. Step blocks (`code` and every nested `block[]`)

| Field | Rule |
| --- | --- |
| `number` | Integer. Trigger = 0, then **sequential depth-first** (0, 1, 2, …), including control-flow blocks and their children |
| `keyword` | `trigger`, `action`, `if`, `elsif`, `else`, `try`, `catch`, `foreach`, `repeat`, `while_condition`, `stop` |
| `provider`, `name` | Required on `trigger` and `action`. **Absent** on `if`/`elsif`/`else`/`try`/`foreach`/`repeat`/`while_condition`/`stop`. `catch` has `"provider": null` |
| `as` | Step alias used by datapills; **unique** in the recipe. Required on trigger, action, catch, foreach, repeat; empty or absent on `try` and `while_condition` |
| `uuid` | Unique, **≤ 36 characters**; prefer descriptive (`"post-slack-001"`) |
| `input` | Object of field → value (strings; see §5) |
| `block` | Children (for trigger and control flow) |
| `extended_input_schema` / `extended_output_schema` | Copied schema for dynamic fields. Needed for the UI and for datapill resolution on custom or dynamic schemas (API request/response, variables, recipe function params, HTTP actions). Mirror `input` exactly (lint `EIS_*`) |
| `skip` | `true` disables the step |
| `comment`, `title`, `description` | Optional and informational; set `comment` to explain intent |

---

## 4. Datapills (references to earlier step outputs)

**Write the modern form** (`_dp`). **Read both** (legacy appears in about 63% of examples).

```text
modern:  #{_dp('{"pill_type":"output","provider":"salesforce","line":"<as>","path":["Owner","Email"]}')}
legacy:  #{_('data.salesforce.<as>.Owner.Email')}
```

| Source step | `provider` in pill | `path` starts with |
| --- | --- | --- |
| Action or trigger of an app | that app's provider | output field names |
| API endpoint trigger | `workato_api_platform` | `["request", …]` (not `body`) |
| Recipe function trigger | `workato_recipe_function` | `["parameters", …]` |
| Genie skill trigger | `workato_skill` | `["parameters", …]` |
| Variables | `workato_variable` | variable name |
| Foreach current item | `foreach` | `line` = the foreach `as`; then field names |
| Catch | `catch` | `["message"]`, `["error_type"]`, … |
| List element (explicit) | — | `{"path_element_type":"current_item"}` as a path element; **no integer indices** |

Rules (lint `DP_*`):

1. A single pill in a text field uses `#{…}` interpolation. Text and pills mix freely: `"Lead: #{_dp(...)}"`.
2. **Formula mode** starts with `=` and is Ruby-like, with no `#{}`: `"=_dp('…').present? ? _dp('…') : 'n/a'"`. Use it for concatenation with `+`, methods, and ternaries.
3. `line` must equal an `as` of a step **before** this one on every path (reachability).
4. The `_dp` payload must be valid JSON, with `\"` escaping inside the JSON string.
5. Don't put formula mode in HTTP `body` fields (silently stripped); use interpolation.

---

## 5. Input values

- All scalar inputs are **strings**: `"true"`, `"5"`, `"hours"`.
- Pick-list fields take the **value** (from catalog `options`, or a pick list resolved via MCP `post_connections_pick_list`).
- Toggle fields: when a field has `toggle_field`, a datapill or custom value goes in under the **same name**. Record the toggle in `toggleCfg: {"<field>": true}` when using the text alternative.
- Object fields with schema builders (variables, recipe function params, API request/response) store the schema as a **stringified JSON array** (`"schema"`, `parameters_schema_json`, `result_schema_json`, `body_schema`).
- Required fields: every catalog input with `required: true`, plus `required_when_visible` where its `visible_if` holds, must be mapped. Empty string `""` counts as missing. Use `"=null"` if a value can be absent.

---

## 6. Control flow (verified against real recipes)

### 6.1 Conditions (`if`, `elsif`, `while_condition`, trigger `filter`)

```json
{"number": 3, "keyword": "if", "input": {"type": "compound", "operand": "and", "conditions": [
  {"operand": "equals_to", "lhs": "#{_dp('{…}')}", "rhs": "High", "uuid": "cond-001"}
]}, "block": [ … ], "uuid": "if-high-001"}
```

Operands seen in practice: `equals_to`, `not_equals_to`, `contains`, `not_contains`, `starts_with`,
`ends_with`, `greater_than`, `less_than`, `present`, `blank`, `is_true`, `is_not_true`. Group
operand: `and` or `or`. `lhs` uses **interpolation**, not formula (lint `DP_LHS_NO_FORMULA`). Unary
operands have `"rhs": ""`.

- **else**: last child of the `if` block; `{"keyword":"else","input":{},"block":[…]}`.
- **elsif** exists in real exports, but the Labs linter rejects it (`NO_ELSIF`) because of import issues. **Generate nested if/else instead.**

### 6.2 Error handling

```json
{"number": 5, "keyword": "try", "input": {}, "block": [
   { …actions… },
   {"number": 8, "keyword": "catch", "provider": null, "as": "catch_err",
    "input": {"max_retry_count": "0", "retry_interval": "2"}, "block": [ …log, notify, return error… ], "uuid": "catch-001"}
], "uuid": "try-001"}
```

`catch` must be the **last** child of `try`. Set `max_retry_count` explicitly (0–3) for transient errors.

### 6.3 Loops

- **foreach**: `{"keyword":"foreach","as":"each_row","source":"#{_dp(<list pill>)}","repeat_mode":"simple","clear_scope":"false","input":{},"block":[…]}`.
  Use batch actions instead of foreach for large volumes (`optimizing-task-usage.md`).
- **repeat/while**: `{"keyword":"repeat","as":"loop1","input":{},"block":[ …, {"keyword":"while_condition","input":{<condition>}} ]}`. `while_condition` must be the **last** child.

### 6.4 Stop

`{"keyword":"stop","input":{"stop_with_error":"false","stop_reason":"No new rows"}}`. Always set `stop_reason`.
In Genie skill recipes, never stop with an error; return `success:false` through `workflow_return_result`.

---

## 7. Platform building blocks (exact shapes)

| Purpose | Step | Key inputs |
| --- | --- | --- |
| Schedule | `clock.scheduled_event` (trigger) | `time_unit` (`minutes`, `hours`, `days`, …), `trigger_every` (≥ 5 minutes) |
| API endpoint | `workato_api_platform.receive_request` → `return_response` | `request: {content_type, schema}`, `response: {content_type, responses:[{name, http_status_code, body_schema}]}`; return `{http_status_code, response:{…}}` for **every** declared status, on **every** path |
| Recipe function | `workato_recipe_function.execute` → `return_result` | `parameters_schema_json`, `result_schema_json`; return `{result:{…}}` with all result fields on all paths |
| Call a function | `workato_recipe_function.call_recipe` (`call_recipe_async`) | `flow_id: {folder, name, zip_name}` (lint `RECIPE_CALL_ZIP_NAME`), `parameters:{…}` |
| Genie skill | `workato_skill.start_workflow` → `workflow_return_result` | `description` (what the LLM sees), `parameters_schema_json`, `result_schema_json`, `requires_user_confirmation` |
| Variables | `workato_variable.declare_variable` / `update_variables` / `declare_list` / `insert_to_list` | `variables:{schema:"[…]", data:{…}}`; `update_variables` uses `name` + field keys (**not** the structured `variables:[…]` form, which is dropped silently) |
| Data tables | `workato_db_table.add_record` / `upsert_record` / `get_records` / `update_record` | `table_id`, `parameters:{<column uuid with _>:value}` (look up column IDs via `get_data_tables_`) |
| Logging | `logger.log_message` | `message`, `user_logs_enabled` |
| Custom HTTP on any connector | `<provider>.__adhoc_http_action` | `mnemonic`, `verb`, `path`, `response_type`, `request_type`, `input`/`output` schemas (see Labs `adhoc-http-actions.md`) |

---

## 8. Quality standards for generated recipes

1. Search for the closest example first (`--examples`) and adapt it; don't invent shapes.
2. Every external write is idempotent (search then create, or upsert with an external ID).
3. Wrap external calls in `try/catch`; the catch logs the error and either returns an error response or stops with error and a reason.
4. API endpoints, recipe functions and Genie skills return **all declared fields on all paths** (use `"=null"` for unknown values).
5. Recipe `description` and step `comment`s explain intent; naming follows `kb/docs/en/recipes/naming-conventions.md`.
6. No secrets, emails or connection IDs hard-coded; use environment properties (`account_property`) or logical connections.
7. Prefer batch, bulk and real-time triggers over tight polling; set explicit concurrency.

---

## 9. Pre-push checklist (enforced by `tools/recipe_check.py`, M2)

- [ ] Every `provider.name` exists in the catalog; every required input is mapped
- [ ] `config` has every provider used (platform entries include `name`); no `workato` provider
- [ ] Numbers sequential depth-first; UUIDs unique and ≤ 36 characters; `as` unique
- [ ] Control-flow children ordered (else last, catch last, while_condition last); no `elsif`
- [ ] Every datapill parses, its `line` exists and is reachable, and its provider matches
- [ ] Return-type recipes return on every path with all schema fields
- [ ] Stop steps have `stop_reason`; catch has `max_retry_count`
