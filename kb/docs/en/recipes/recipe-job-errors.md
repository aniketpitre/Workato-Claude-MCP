---
url: 'https://docs.workato.com/en/recipes/recipe-job-errors.md'
description: >-
  Learn how to troubleshoot recipe job errors in Workato, including trigger
  errors, run-time formula errors, missing fields, and timeouts.
---

# Job errors (recipe execution errors)

Job errors, also known as recipe execution errors, usually occur when a trigger event has been found, and a job is being processed, therefore typically showing up as recipe job errors. An exception to this is trigger errors, which occur when the recipe fails to retrieve any trigger events, and therefore does not create any jobs.

## Trigger errors

Trigger errors occur when the recipe tries to retrieve trigger events by polling the trigger app, but fails to fetch trigger events successfully. As no trigger event data was retrieved, the recipe does not create a job in the first place.

The following table details the various reasons for trigger errors, and how we can resolve them.

| Trigger error reason | What happens? | How to resolve |
| --- | --- | --- |
| App connection becomes invalid and recipe is unable to connect successfully to the trigger app to fetch trigger events | Usually results in an 401 unauthorized error message | Reconnect successfully to trigger app |
| Connected user does not have the right permissions to fetch trigger events | Usually results in an 403 forbidden message | Update the connected user's permissions to provide required read/write permission scopes |
| Recipe makes an invalid API call, for example, due to schema changes such as field deletion in the app that wasn't reflected in the recipe | Usually results in schema errors | Carry out a [schema refresh](/en/recipes/editor#refresh-schema) for the recipes with schema errors |
| Recipe makes an API call that times out while waiting for trigger events to be fetched. This is usually transient, i.e. the API server might be experiencing temporary downtime | Usually results in a timeout error | If transient, you should stop getting the error after a while. If error keeps occurring, check the API uptime status of the app that the recipe keeps failing at, or reach out to us. |
| Trigger filters are logically incorrect, for example, a null value is checked against an integer, a string is checked against a number. | Usually results in a formula error | Trigger filters will need to be fixed before the recipe can run properly. Refer to [Conditions](/en/features/if-conditions) for more information on valid trigger filters. |

## Run-time formula errors

Every input field (except for list input fields) can be toggled between text and formula mode. Formulas that didn't throw any design-time errors when the recipe was started can still throw run-time errors during a job, when actual data is being processed by the recipe. some reasons for run-time errors are:

- datapill had no value and was `nil`, and the formula acting on it doesn't work on null values
- formula tries to execute invalid operation that was not caught at design time, for example, dividing a number by a string (text)
- formula was used on a datapill of the wrong data type, for example, using `true?` formula on an array datapill

## Missing required fields at run-time

Triggers and actions typically need configuration to be useful in a recipe. For example, to update a Zendesk organization, we need, at a minimum, the ID of the organization to update. Therefore, that's a required field in the recipe. Required input fields that didn't throw any design-time errors when the recipe was started, because the field had a datapill as input, can still throw run-time errors if the datapill had no value during the job, when actual data is being processed by the recipe.

## Timeouts

When a recipe checks for trigger events or executes an action, Workato sends a request to the appropriate app and waits for a response.

This request can time out in the following situations:

- The app takes too long to respond to Workato, and the trigger or action raises a timeout error.
- The job takes too long to carry out and raises a timeout error.

If the recipe that sends the request is an [API recipe](/en/api-mgmt/api-recipes/), and the request times out, the job will be terminated, and it will not raise a timeout error. To manage API request response times, you can customize the timeout value by [editing](/en/api-mgmt/api-collections#edit-collection) the API endpoint associated with the recipe.

> **ERROR MONITORING**
> 
> If an API recipe includes a [Handle errors](/en/recipes/steps#handle-errors-step) step, the **Monitoring** block will not trigger when the API request times out, given that the recipe job will be terminated. As a result, actions in the **Error** block will not be executed.

## Passing wrong data types into input fields

Sometimes, the datapill used for an input field have a data type which is not expected by the input field, for example, we pass in a string (`"12.50"`) into a input field expecting a number (`12.50`). This might not be caught at design-time, but the app we provide this string to might throw an error when it receives unexpected data types.

To resolve this, you can use formulas for data type conversions by referring to the documentation for [strings](/en/formulas/string-formulas#conversion-of-strings-to-other-data-types), [numbers](/en/formulas/number-formulas#conversions), [dates](/en/formulas/date-formulas), or [lists](/en/formulas/array-list-formulas#conversion).

---
