# Design: <title>

Spec: `spec.yaml` · Architect: workato-architect · Status: draft | approved

## 1. Solution overview
One paragraph, plus a step diagram.

## 2. Assets
| Asset | Type (recipe / function / data table / API endpoint / MCP server / skill / Genie) | Folder or project | Purpose |
| --- | --- | --- | --- |

## 3. Recipe flows
Draft recipes live in `recipes/*.recipe.json` and are drawn editor-style on the review page
(`python3 tools/review_page.py automation <name>`). Paste the text view here
(`python3 tools/recipe_view.py md recipes/<file>`), and name the closest example used as the
template (`kb/...` path).

## 3b. End-user experience
What each end user sees or receives (messages, fields, errors, timing), and why it meets the spec's
success measures.

## 4. Data mapping
| Source field | Target field | Transform / formula |
| --- | --- | --- |

## 5. Error handling and idempotency
try/catch placement, retries, notifications, duplicate prevention (search-then-create or upsert key).

## 6. Connections and environment
Logical connections → per-environment bindings; environment properties used.

## 7. Security
PII handled, access, exposure (API/MCP), and whether a security review is needed.

## 8. Test plan
How each acceptance test (AT-n) is executed (test case, force run, API call) and verified.

## 9. Monitoring
What the Operate stage watches; alert routing.

## 10. Decisions and alternatives
