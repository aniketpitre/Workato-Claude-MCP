---
url: 'https://docs.workato.com/en/connectors/recipeops/triggers/recipe-started.md'
description: >-
  The Recipe started trigger in the RecipeOps connector fires when a user starts
  a monitored recipe, in real time.
---

# RecipeOps - Recipe started trigger

The **Recipe started** trigger monitors recipes started by users in real-time.

## Input

| Input field | Description |
| --- | --- |
| Recipes to monitor | Select the recipes to monitor. Choose **All** to monitor all recipes in the workspace, **Selected** to monitor selected recipes, or **Tags** to monitor recipes associated with one or more tags. |
| Recipe IDs | Provide a comma-separated list of recipe IDs if monitoring **Selected** recipes. You can find recipe IDs in the recipe’s URL. For example, in `https://app.workato.com/recipes/362905-timekeeper`, the recipe ID is `362905`. |
| Tags | Provide one or more tags if monitoring recipes by **Tags**. |

## Output

| Output field | Description |
| --- | --- |
| Started at | The time the recipe was started. |
| Recipe ID | The ID of the recipe that was started. |
| Name | The name of the recipe that was started. |
| Last run at | The time the recipe last ran. |
| Created at | The time the recipe was created. |
| Updated at | The time the recipe was last updated. |
| Started by user | Details about the user who started the recipe, including the `User ID`, `User name`, and `User email`. |

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---

---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/recipe-stopped-by-user.md
description: >-
  The Recipe stopped by user trigger in the RecipeOps connector fires when a
  user manually stops a monitored recipe, in real time.
---

# RecipeOps - Recipe stopped by user trigger

The **Recipe stopped by user** trigger monitors recipes manually stopped by users in real-time.

## Input

| Input field | Description |
| --- | --- |
| Recipes to monitor | Select the recipes to monitor. Choose **All** to monitor all recipes in the workspace, **Selected** to monitor selected recipes, or **Tags** to monitor recipes associated with one or more tags. |
| Recipe IDs | Provide a comma-separated list of recipe IDs if monitoring **Selected** recipes. You can find recipe IDs in the recipe’s URL. For example, in `https://app.workato.com/recipes/362905-timekeeper`, the recipe ID is `362905`. |
| Tags | Provide one or more tags if monitoring recipes by **Tags**. |

## Output

| Output field | Description |
| --- | --- |
| Stopped at | The time the recipe was stopped. |
| Recipe ID | The ID of the recipe that was stopped. |
| Name | The name of the recipe that was stopped. |
| Last run at | The time the recipe last ran. |
| Created at | The time the recipe was created. |
| Updated at | The time the recipe was last updated. |
| Stopped by user | Details about the user who stopped the recipe, including the `User ID`, `User name`, and `User email`. |

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---

---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/recipe-stopped-by-workato.md
description: >-
  The Recipe stopped by Workato trigger in the RecipeOps connector fires when
  Workato stops a monitored recipe due to non-recoverable errors, in real time.
---

# RecipeOps - Recipe stopped by Workato trigger

The **Recipe stopped by Workato** trigger monitors selected recipes for stops due to non-recoverable errors in real-time. Workato typically stops a recipe when it encounters errors that cannot be resolved automatically. For example, Workato stops a recipe if 60 consecutive authentication errors occur in a recipe trigger. This trigger allows you to build logic to restart the recipe and set escalation policies to notify teammates when stops occur.

## Input

| Input field | Description |
| --- | --- |
| Recipes to monitor | Select the recipes to monitor. Choose **All** to monitor all recipes in the workspace, **Selected** to monitor selected recipes, or **Tags** to monitor recipes associated with one or more tags. |
| Recipe IDs | Provide a comma-separated list of recipe IDs if monitoring **Selected** recipes. You can find recipe IDs in the recipe’s URL. For example, in `https://app.workato.com/recipes/362905-timekeeper`, the recipe ID is `362905`. |
| Tags | Provide one or more tags if monitoring recipes by **Tags**. |

## Output

| Output field | Description |
| --- | --- |
| Recipe ID | The ID of the recipe where the error occurred. |
| Error | Details about the error. This object contains the `Error ID`, `Message`, `Error count`, `Error connector`, `Error source`, `Error source name`, `Is authorization error`, `Is rate limit error`, and `Is poll error (deprecated)` output datapills. |

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/recipeops/actions/get-account-details.md
description: >-
  The Get account details action in the RecipeOps connector retrieves Workato
  account info such as plan type and remaining transaction and recipe counts.
---

# RecipeOps - Get account details action

This action retrieves information about the Workato account, such as subscription plan type, and remaining transaction, recipe, and connection counts.

* * *

## Input

This action doesn't require any input.

* * *

## Output

| Field | Description |
| --- | --- |
| **Plan ID** | The ID of the plan used by the account. |
| **Allotted transaction count** | The allotted transaction count of the account. |
| **Available transaction count** | The number of available transactions for the account. |
| **Active recipe count** | The total number of active recipes in the account. |
| **Inactive recipe count** | The total number of inactive recipes in the account. |
| **Connection count** | The total number of connections in the account. |
| **Current billing period start** | The start date of the account's current billing period. |
| **Current billing period end** | The end date of the account's current billing period. |
| **Allotted task count** | The allotted task count for the account. |
| **Available task count** | The number of available tasks for the account. |
| **Allotted task count adjustment** |  |

* * *

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---
