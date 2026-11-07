---
url: 'https://docs.workato.com/en/features/callable-recipes/new-call-trigger.md'
description: >-
  Reference for the New call for recipe trigger in Callable recipes, which
  creates a job in real time when called from another recipe or REST endpoint.
---

# Callable recipes by Workato - New call for recipe trigger

This trigger creates a job whenever it is called, in real-time. It can be called from [another recipe](/en/features/callable-recipes/call-recipe-action) or from another system as a [API Platform REST endpoint](/en/api-management).

> **THIS TRIGGER IS DEPRECATED**
> 
> This trigger has been replaced by the following triggers:
> 
> - [Recipe functions - New function call trigger](/en/connectors/recipe-functions/triggers/new-function-call) - Creates a recipe that can be called from another recipe
> - [API platform - New API request trigger](/en/api-mgmt/api-recipes/trigger-new-api-request) - Creates a job based on API requests
> 
> Recipes using this trigger will continue to function. Use the new **Recipe functions** and **API platform** triggers instead to take advantage of new features - check out the [Recipe functions FAQ](/en/features/callable-recipes/recipe-functions-faq) and [API platform FAQ](/en/api-mgmt/api-recipes/api-recipes-faq) for more info.

  

> **INFO**
> 
> API Platform must be enabled for your workspace before you can expose a callable recipe as a REST endpoint.

![New call for recipe trigger](/assets/callable-recipe-trigger.CSbX2T9D.png)_New call for recipe trigger_

* * *

## Input

| Input field | Description |
| --- | --- |
| Name | Give this callable recipe trigger a name that describes its function. |
| Input schema | If this recipe expects JSON, use this to describe the expected JSON structure. |
| Response schema | If this recipe responds with JSON data, use this to describe the JSON structure. |
| Request type | Select the request data format. Defaults to **JSON request body** if left blank. |
| Response type | Select the response data format. Defaults to **JSON response** if left blank. |

* * *

## Output

Certain output fields are only available if the recipe is called as an API platform REST endpoint. More information can be found on the [API platform](/en/api-management) documentation.

| Output field | Description |
| --- | --- |
| Calling job ID | ID of the job in the parent recipe that made the call. |
| Calling recipe ID | ID of the parent recipe that made the call. |
| _Only available if called as an API Platform **REST endpoint**_ | Calling IP address | IP address of the client calling this recipe as a REST endpoint. |
| Access profile | Contains **ID**, **name** and **authentication method** of the access profile used to perform the request. |
| API client | Contains **API client ID** and **API client name** values to perform the request. |
| JWT claims | _Only available a JWT token is used._ Contains **Audience**, **JWT ID**, **Issuer**, and **Expiration Time**, **Not before** and **Issued At** values of the JWT used to authenticate the request. |
| _Only if request type is **Raw request body**_ | Content type | `Content-Type` header value from the incoming request. |
| Request body (raw) | Full raw request body. |
| Recipe input | This output object will contain all the fields defined in **Input schema**. |

---

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

---
