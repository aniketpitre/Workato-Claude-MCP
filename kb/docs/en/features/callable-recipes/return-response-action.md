---
url: >-
  https://docs.workato.com/en/features/callable-recipes/return-response-action.md
description: >-
  Reference for the Return response from recipe action in Callable recipes,
  which replies to a recipe call with a status and any returned data.
---

# Callable recipes by Workato - Return response from recipe action

This action responds to the recipe call with a status confirmation together with any data. This action will respond with a data format defined in the [New call for recipe](/en/features/callable-recipes/new-call-trigger) trigger.

> **THIS ACTION IS DEPRECATED**
> 
> This action is deprecated and applies only to legacy callable recipes with the [New call for recipe trigger](/en/features/callable-recipes/new-call-trigger). If you use this action with any other trigger, an error occurs.
> 
> Existing recipes that use this action continue to work. For new recipes, use the [Recipe functions - Return data from a recipe function](/en/connectors/recipe-functions/actions/return-data-from-a-recipe-function) action. Refer to the [Recipe functions FAQ](/en/features/callable-recipes/recipe-functions-faq) for more information.

![Return response from recipe action](/assets/return-response-action.DbN6DvhV.png)_Return response from recipe action_

* * *

## Input

| Input field | Description |
| --- | --- |
| Response type | Select a response (**Success** or **Error**) according to the recipe logic. |
| Reply/Response | Depending on the response type, a relevant input field will be displayed for mapping. |
| Content type | If you select **Raw response** in the trigger, define the response data type here. |
| Error message | If you chose an **Error** response type, provide an appropriate error message here. |

If you are using a REST-enabled recipe, these input fields will also be relevant.

| Input field | Description |
| --- | --- |
| Error code | If you chose an **Error** response type, choose a HTTP error code to respond with. |
| Custom error response? | Select **Yes** to send content of **Error message** input as the response body. |
