---
url: >-
  https://docs.workato.com/en/connectors/recipe-functions/triggers/new-function-call.md
description: >-
  The New call for function trigger in the Recipe functions connector lets you
  build a reusable recipe that other recipes can call.
---

# Recipe function by Workato - New call for function trigger

This trigger allows you to build a recipe that can be called from another recipe. When naming the recipe, keep in mind that the recipe name is what displays in the **Recipe function** menu of the [**Call recipe synchronously**](/en/connectors/recipe-functions/actions/call-recipe-function-synchronously) and [**asynchronously**](/en/connectors/recipe-functions/actions/call-recipe-function-asynchronously) actions.

**Note**: This trigger partially replaces the [Callable Recipes - New call for recipe trigger](/en/features/callable-recipes/new-call-trigger). Use the [API platform - New API request trigger](/en/api-mgmt/api-recipes/trigger-new-api-request) to trigger recipes based on API requests.

* * *

## Input

| Field | Description |
| --- | --- |
| **Parameters schema** | Defines the schema of the input the recipe expects. |
| **Result schema** | Defines the schema of the recipe's response. |

Looking to test out this trigger? Check out [manually testing triggers](/en/recipes/testing#trigger-manual-test) in the Testing recipes guide for more info.

* * *

## Output

| Field | Description |
| --- | --- |
| **Context** | Details about the job and recipe that triggered this recipe. This field has some additional sub-fields:
| Field | Description |
| --- | --- |
| **Calling job ID** | The ID of the job that triggered this recipe. |
| **Calling recipe ID** | The ID of the recipe that called this recipe. |

 |
| **Parameters** | The schema provided in the **Parameters schema** section. |

* * *

## Resources

- [Recipe function overview](/en/connectors/recipe-functions)
- [Recipe function actions](/en/connectors/recipe-functions#actions)
- [Recipe function triggers](/en/connectors/recipe-functions#triggers)
