---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/concurrency-exceeded.md
description: >-
  The API concurrency threshold exceeded trigger in the RecipeOps connector
  fires when workspace API requests exceed 80% of the concurrency quota.
---

# RecipeOps - API concurrency threshold exceeded

Monitors API requests across your workspace and triggers when requests exceed 80% of your concurrency quota. Additional trigger events are created for each 5% increment, up to the workspace quota. This trigger is limited to one event per threshold every five minutes to reduce noise. Subsequent requests for the same threshold within a five-minute window will not result in a job.

* * *

## Output

| Field | Description |
| --- | --- |
| **Concurrency limit** | API concurrency quota for this workspace. |
| **Concurrency** | Number of concurrency requests reached. |

* * *

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)
