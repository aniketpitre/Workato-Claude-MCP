---
url: >-
  https://docs.workato.com/en/connectors/recipe-functions/actions/wait-for-async-calls.md
description: >-
  The Wait for async calls action in the Recipe functions connector pauses a
  recipe until the specified asynchronous calls complete or time out.
---

# Recipe function by Workato - Wait for async calls action

This action waits for specified async calls to complete before proceeding to the next step in the recipe. When invoked, Workato puts the recipe on hold and periodically checks if the defined async calls have completed.

Once all calls have been completed - whether successfully or not - the recipe will proceed to the next step.

* * *

## Example Usage

When used with the [Recipe functions - Call recipe asynchronously action](/en/connectors/recipe-functions/actions/call-recipe-function-asynchronously), you can efficiently run independent processes in parallel. This can speed up overall job time for your recipe(s).

For example: Every day, you sync data from Amazon S3 to multiple tables in Snowflake. Recipes that [bulk load to Snowflake tables](/en/connectors/snowflake/bulk-load-to-table-from-stage) are called asynchronously, allowing loads to occur for multiple tables at once.

Once all the jobs loading data to Snowflake complete, the recipe will move onto the next step. At this point, you could configure a step that sends a notification that loading is complete.

* * *

## Requirements

To use this action, you need a [Recipe function](/en/connectors/recipe-functions). This is a recipe that uses the [Recipe functions - New function call](/en/connectors/recipe-functions/triggers/new-function-call) trigger and can be called from other recipes.

* * *

## Limitations

When using this action, note that:

- **This action shouldn't be used if steps must run in sequence.** If your recipe requires steps to be executed in order, use the [**Recipe functions - Call recipe synchronously**](/en/connectors/recipe-functions/actions/call-recipe-function-synchronously) action.

* * *

## Input

| Field | Description |
| --- | --- |
| **Async calls to wait for** | Defines the async calls the action must wait to complete. To add multiple async calls, click **\+ Add an async call job reference**. |
| **Timeout limit (minutes)** | Defines the maximum amount of time, in minutes, that calls can take to complete. **The maximum is 1440 minutes**, or 24 hours. Entering `0` is equivalent to using the maximum of `1440` minutes. If one or more async calls take longer than this amount of time, the recipe will proceed to the next step without waiting. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Results** | A list datapill containing metadata about the jobs that were called asynchronously, including the list size and list index. This field has some additional sub-fields:
| Field | Description |
| --- | --- |
| **Called from line** | The line of the parent recipe that called the async action. |
| **Recipe ID** | The ID of the recipe. |
| **Job ID** | The ID of the job. |
| **Job started at** | The time the job started. |
| **Job completed at** | The time the job completed. |
| **Job completed** | If `true`, the job completed successfully. |
| **Job error** | The error the job encountered, if any. |
| **List size** | The total number of items in the `Results` list. |
| **List index** | The index of the current result in the list. | |
| **All jobs succeeded** | If `true`, all async calls completed successfully. |
| **Job succeeded count** | The total number of async calls that completed successfully. |
| **Job failed count** | The total number of async calls that failed. |
| **Job timed out count** | The total number of async calls that exceeded the defined [**Timeout limit (minutes)**](#input) parameter. |

* * *

## Resources

- [Recipe function overview](/en/connectors/recipe-functions)
- [Recipe function actions](/en/connectors/recipe-functions#actions)
- [Recipe function triggers](/en/connectors/recipe-functions#triggers)
