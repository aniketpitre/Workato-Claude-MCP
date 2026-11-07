---
url: 'https://docs.workato.com/en/connectors/recipeops/triggers/opa-disconnected.md'
description: >-
  The On-prem agent disconnected trigger in the RecipeOps connector fires when
  an agent in the selected group disconnects from Workato and fails to
  reconnect.
---

# RecipeOps - On-prem agent disconnected trigger

This trigger monitors all your on-prem agents in the selected on-prem group. A trigger event is created if an agent has been disconnected from Workato due to an error (for example, a network outage or agent process has been killed) and fails to reconnect. This trigger aggregates disconnect events for a specific time frame to reduce noise.

This trigger is available starting from on-prem agent 2.19.0.

* * *

## Output

| Field | Description |
| --- | --- |
| **Agent name** | Name of disconnected on-prem agent. |
| **Agent address** | IP address of disconnected on-prem agent. |

* * *

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---
