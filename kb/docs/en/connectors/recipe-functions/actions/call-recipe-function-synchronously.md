---
url: >-
  https://docs.workato.com/en/connectors/recipe-functions/actions/call-recipe-function-synchronously.md
description: >-
  The Call recipe synchronously action in the Recipe functions connector calls a
  recipe function and waits for its response before continuing.
---

# Recipe function by Workato - Call recipe synchronously action

This action calls a Recipe function and waits for the response before proceeding to the next step in the recipe.

* * *

## Requirements

To use this action, you need a [Recipe function](/en/connectors/recipe-functions). This is a recipe that uses the [**Recipe functions - New function call**](/en/connectors/recipe-functions/triggers/new-function-call) trigger and can be called from other recipes.

* * *

## Limitations

When using this action, note that:

- **This action is subject to a timeout limit.** If the [timeout limit](/en/recipes/jobs#timeouts) is exceeded, the job will fail. You can reduce the likelihood of timeout errors by [calling the recipe function asynchronously](/en/connectors/recipe-functions/actions/call-recipe-function-asynchronously).
- This action can cause "job out of order" behavior. Although it is not a long action, it can cause jobs to process out of order. This occurs when multiple recipe functions are invoked within a parent recipe. For more information on this behavior when using concurrency, refer to the [concurrency](/en/recipes/settings#concurrency) documentation.

* * *

## Input

| Field | Description |
| --- | --- |
| **Recipe function** | Select from a list of Recipe functions in your workspace. |
| **Recipe input** | The fields defined in the selected Recipe function's **Input schema**. |
| **Connection overrides** | **Applicable only if the Runtime user connections setting is enabled in the selected Recipe function**. Specify the name or ID of the connection to use when the recipe is run. [Learn more](/features/runtime-user-connections.html). |

* * *

## Output

| Field | Description |
| --- | --- |
| **Job ID** | The ID of the created job. |
| **Job URL** | The URL of the created job. |
| **Result** | The Recipe function's **Response schema** configuration. |

* * *

## Resources

- [Recipe function overview](/en/connectors/recipe-functions)
- [Recipe function actions](/en/connectors/recipe-functions#actions)
- [Recipe function triggers](/en/connectors/recipe-functions#triggers)
