---
url: 'https://docs.workato.com/en/connectors/recipe-functions/guides/walkthrough.md'
description: >-
  Walk through building a recipe function with Quickbooks and Salesforce in
  Workato so reusable logic can be called from other recipes.
---

# Recipe functions walkthrough

If your interest around **Recipe functions** is piqued but you're still a bit confused, this walkthrough can help.

In this guide, we'll walk you through creating a recipe function using Quickbooks and Salesforce.

- **What's our goal?** To automate invoice creation in Quickbooks when opportunities are **closed-won** in Salesforce.
  
- **What do we need to know?** Invoices in Quickbooks must be associated with a customer. To create an invoice, we'll also need to create a customer if one doesn't already exist.
  
  Customers can be created form multiple places such as a point-of-sale (POS) system, invoices from vendors, etc. This means that the logic for creating customers could be used in multiple places.
  

With Recipe functions, we can build a recipe that contains the steps required to create a Quickbooks customer and then call it from other recipes. This approach means logic doesn't have to be duplicated in multiple recipes.

* * *

## Step 1: Create A Recipe Function

1. Create a new recipe, using **Build a recipe function** as the **Starting point**.
   
2. Define the fields for the trigger. These fields determine:
   
   - The fields that are shown when a recipe action is used in a calling recipe, and
   - The data returned by the recipe for use as datapills in the calling recipe
   
   Refer to the [Recipe functions - New function call guide](/en/connectors/recipe-functions/triggers/new-function-call) for assistance.
   

* * *

## Step 2: Add Steps To The Recipe

Next, create the steps required to complete the action your recipe fulfills. In this case, our recipe needs to contain the steps necessary to:

- Check if a customer already exists in Quickbooks
- Based on the check, create a customer if one doesn't exist

* * *

## Step 3: Call The Recipe Function

Lastly, you'll create a recipe that calls the recipe function you created in [Step 1](#step-1-create-a-recipe-function).

1. Create a new recipe, setting the trigger to what you require.
   
2. When you're ready to call the recipe function:
   
   1. Add a new **Action in app** action.
      
   2. Search for the **Recipe functions** connector.
      
   3. From the **Actions** list, select the [Call recipe function (synchronous)](/en/connectors/recipe-functions/actions/call-recipe-function-synchronously) or [Call recipe function (asynchronous)](/en/connectors/recipe-functions/actions/call-recipe-function-asynchronously) action.
      
   4. In the action's **Recipe function** field, select the recipe you created in [Step 1](#step-1-create-a-recipe-function). The fields from the recipe function's **Input schema** will display as datapills.
      
3. Add additional steps to the recipe as needed.
   
4. When finished, click **Save**.

---

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

---

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

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/recipe-functions/actions/return-data-from-a-recipe-function.md
description: >-
  The Return data from a recipe function action in the Recipe functions
  connector responds to the calling recipe with a status and data, ending the
  job.
---

# Recipe function by Workato - Return data from a recipe function action

This action responds to the [**Recipe functions - New function call**](/en/connectors/recipe-functions/triggers/new-function-call) trigger with a status and data defined in the trigger's input parameters.

**This action ends recipe jobs**. When a job successfully executes this action, the current job will end. Any steps after this action will be ignored.

* * *

## Requirements

To use this action, you need a recipe that uses the [**Recipe functions - New function call**](/en/connectors/recipe-functions/triggers/new-function-call) trigger.

* * *

## Input

| Field | Description |
| --- | --- |
| **Result** | The fields defined in the trigger's **Result schema**. |

* * *

## Output

This action's output will take the form of the data defined in the [New function call trigger](/en/connectors/recipe-functions/triggers/new-function-call).

* * *

## Resources

- [Recipe function overview](/en/connectors/recipe-functions)
- [Recipe function actions](/en/connectors/recipe-functions#actions)
- [Recipe function triggers](/en/connectors/recipe-functions#triggers)

---

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

---
