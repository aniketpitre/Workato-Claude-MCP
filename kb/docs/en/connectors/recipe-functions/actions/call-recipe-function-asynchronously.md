---
url: >-
  https://docs.workato.com/en/connectors/recipe-functions/actions/call-recipe-function-asynchronously.md
description: >-
  The Call recipe function asynchronously action in the Recipe functions
  connector calls a recipe function and proceeds to the next step right away.
---

# Recipe function by Workato - Call recipe function asynchronously action

This action calls a recipe function and then immediately proceeds to the next step in the recipe. Asynchronous calls are useful for use cases where the successive steps don't depend on the outcome of the recipe function's workflow.

If your workflow involves follow-up steps that occur after long asynchronous calls, use the [Wait for async calls action](/en/connectors/recipe-functions/actions/wait-for-async-calls) to ensure that all asynchronous calls have completed processing.

* * *

## Requirements

To use this action, you need a [Recipe function](/en/connectors/recipe-functions). This is a recipe that uses the [Recipe functions - New function call](/en/connectors/recipe-functions/triggers/new-function-call) trigger and can be called from other recipes.

* * *

## Limitations

When using this action, note that:

- **Calls aren't guaranteed to be executed in order.** Use the [Recipe functions - Call recipe function (synchronous)](/en/connectors/recipe-functions/actions/call-recipe-function-synchronously) action if your workflow requires steps to be called in sequence.
  
- **This action doesn't produce `result` output.** As async calls don't wait for a response, this action won't output any `result` data.
  
  If your workflow requires data from an asynchronously called recipe function, you can use [Lookup table](/en/features/lookup-tables) actions as a workaround.
  
  Check out the workaround!
  
  1. Create a new [lookup table](/en/features/lookup-tables) in your account with columns to store:
     
     - Recipe IDs
     - Job IDs
     - Data to pass back to the parent recipe
  2. In the **recipe function**:
     
     1. Add a [Add a lookup table entry action](/en/features/lookup-tables#add-entry-action) step.
        
     2. Select the lookup table you created in step 1.
        
     3. Configure the action to store the recipe ID, job ID, and the data to pass back to the parent recipe in the lookup table.
        
     
     The recipe function should look similar to this:
     
     ![Recipe function using a lookup table step](/assets/async-lookup-table-workaround.BOqJnEVA.png)
     
  3. In the **parent recipe**:
     
     1. Add a **Call recipe function (asynchronous)** action step and configure it to call the recipe function.
        
     2. Add a [Wait for async calls action](/en/connectors/recipe-functions/actions/wait-for-async-calls) step and configure it to wait for the recipe function to finish.
        
     3. Add a [Search for lookup table entries action](/en/features/lookup-tables#search-entries-action-batch) step and configure it to retrieve the entry added by the recipe function.
        
     
     The parent recipe should look similar to this:
     
     ![Parent recipe](/assets/async-parent-lookup-table-search.DB2mAg-F.png)
     
  

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
| **Job reference** | A job reference ID. **Note**: This is not the job ID. |
| **Job URL** | The URL of the created job. |
