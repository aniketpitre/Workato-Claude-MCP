---
url: 'https://docs.workato.com/en/features/callable-recipes/call-recipe-action.md'
description: >-
  Reference for the Call recipe action in Callable recipes, covering synchronous
  and asynchronous input and output fields used to invoke a recipe.
---

# Callable recipes by Workato - Call recipe actions

There are two types of **Call recipe** actions:

- [Synchronous](#call-recipe-synchronous)
- [Asynchronous](#call-recipe-asynchronous)

> **THIS ACTION IS DEPRECATED**
> 
> These actions have been replaced by the following actions:
> 
> - [**Recipe functions - Call recipe function (asynchronous)**](/en/connectors/recipe-functions/actions/call-recipe-function-asynchronously)
> - [**Recipe functions - Call recipe function (synchronous)**](/en/connectors/recipe-functions/actions/call-recipe-function-synchronously)
> 
> While you can continue to use callable recipes in other recipes, new callable recipes can no longer be created. Check out the [migration guide](/en/features/callable-recipes/migrating-to-recipe-functions-api-recipes) and [Recipe functions FAQ](/en/features/callable-recipes/recipe-functions-faq) for more info.

* * *

## Requirements

To use the actions in this guide, you need:

- **A Callable recipe.** Callable recipes are a type of recipe that can be called from another recipe. Refer to the [Callable recipe docs](/en/features/callable-recipes) to learn more.

* * *

## Call Recipe (Synchronous)

This action calls a recipe and waits for the response before proceeding to the next step in the recipe.

### Limitations

This action is subject to a [timeout limit](/en/recipes/jobs#timeouts). If the timeout limit is exceeded, the job will fail. You can reduce the likelihood of timeout errors by [calling the recipe asynchronously](#call-recipe-asynchronous).

### Input

| Field | Description |
| --- | --- |
| **Recipe to call** | Select from a list of Callable recipes in your workspace. |
| **Recipe input** | The fields defined in the selected Callable recipe's **Input schema**. |

### Output

| Field | Description |
| --- | --- |
| **Job ID** | The ID of the created job. |
| **Job URL** | The URL of the created job. |
| **Reply** | The callable recipe's **Response schema** configuration. |

* * *

## Call Recipe (Asynchronous)

This action calls a recipe and then immediately proceeds to the next step in the recipe. Asynchronous calls are useful for use cases where the successive steps don't depend on the outcome of the callable recipe workflow.

If your workflow involves follow-up steps that occur after long asynchronous calls, use the [Wait for async calls action](/en/features/callable-recipes/wait-for-async-action) to ensure that all asynchronous calls have completed processing.

### Limitations

Asynchronous calls are not guaranteed to be executed in sequence. Use the [Call recipe (synchronous)](/en/features/callable-recipes/call-recipe-action#call-recipe-synchronous) action if your workflow requires steps to be called in sequence.

### Input

| Field | Description |
| --- | --- |
| **Recipe to call** | Select from a list of Callable recipes in your workspace. |
| **Recipe input** | The fields defined in the selected Callable recipe's **Input schema**. |

### Output

**Note**: Since this action does not wait for a response, there will not be any **Reply** output fields.

| Field | Description |
| --- | --- |
| **Job ID ref** | A job ID reference. **Note**: This is not the job ID. |
| **Job URL** | The URL of the created job. |

---
