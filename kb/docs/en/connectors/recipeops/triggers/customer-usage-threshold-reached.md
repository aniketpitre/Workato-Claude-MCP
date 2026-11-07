---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/customer-usage-threshold-reached.md
description: >-
  Use the Usage threshold reached trigger in Embedded partner workspaces to send
  alerts when a workspace reaches a task usage threshold according to its plan.
---

# RecipeOps - Usage threshold reached trigger

The **Usage threshold reached** trigger monitors task usage across all Embedded customer workspaces and runs when a customer reaches a usage threshold based on their plan. The trigger generates an event each time a customer reaches a 10% increment of their plan's task usage limit.

> **EMBEDDED PARTNER WORKSPACE REQUIRED**
> 
> The **Usage threshold reached** trigger only works in Embedded partner workspaces and you must enable this trigger before you can use it. Although the trigger appears in other workspace types, jobs fail with an error if you add it to a recipe.
> 
> The RecipeOps connection used with this trigger must use an API token from the parent Embedded partner workspace. API tokens from Embedded customer workspaces result in an insufficient permissions error.
> 
> Contact your Workato Success Representative to learn more.

## Input

The **Usage threshold reached** trigger doesn't require any input.

## Output

| Output field | Description |
| --- | --- |
| ID | The Workato ID of the customer. |
| External ID | The external ID of the customer, if defined. |
| Customer Name | The name of the customer. |
| Plan | Object containing details about the customer's plan. |
| Plan name (Plan) | The name of the plan. |
| Plan accounting period (Plan) | The accounting period of the plan. |
| Billing cycle reset date | The reset date of the current billing cycle. |
| Current limit | Object containing details about the limits applied to the account. |
| Task limit (Current limit) | The task limit for the account. |
| Threshold reached at | The time the threshold was reached. |
| % Threshold reached | The percentage of the threshold that was reached. |

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)
