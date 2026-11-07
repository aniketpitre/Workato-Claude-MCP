# Design: <title>

Spec: `spec.yaml` · Architect: workato-architect · Status: draft | approved

## 1. Solution overview
One paragraph, plus a step diagram.

## 2. Assets
| Asset | Type (recipe / function / data table / API endpoint / MCP server / skill / Genie) | Folder or project | Purpose |
| --- | --- | --- | --- |

## 3. Recipe flows
For each recipe: trigger → numbered steps (exact `provider.action` from the catalog) → returns.
Name the closest example used as the template (`kb/...` path).

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
