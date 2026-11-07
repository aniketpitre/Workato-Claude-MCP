---
url: 'https://docs.workato.com/en/features/callable-recipes/wait-for-async-action.md'
description: >-
  Reference for the Wait for async calls action in Callable recipes, which holds
  a recipe until all asynchronous calls finish processing.
---

# Callable recipes by Workato - Wait for async calls action

This action waits for async calls to complete. At the wait action, Workato puts the recipe on hold and checks periodically if the asynchronous calls have completed processing. Once all the async calls have been completed (successfully or unsuccessfully), Workato will proceed with the next steps in the recipe.

> **THIS ACTION IS DEPRECATED**
> 
> This action has been replaced by the [Recipe functions - Wait for async calls action](/en/connectors/recipe-functions/actions/wait-for-async-calls)
> 
> **Recipes using this action will continue to function**. Use the new **Recipe functions** action to take advantage of new features - check out the [Recipe functions FAQ](/en/features/callable-recipes/recipe-functions-faq) for more info.

  

> **Run independent process in parallel**
> 
> Use async calls with the wait action to efficiently run independent processes in parallel. This speeds up the overall processing time.
> 
> For example, Acme company syncs data from S3 to Snowflake daily. Each table in Snowflake is unique and the [bulk load to Snowflake](/en/connectors/snowflake/bulk-load-to-table-from-stage) action can be called asynchronously for each table. Thus, multiple asynchronous recipes can run in parallel.
> 
> To receive a slack notification after all the asynchronous recipes have finished processing, using the use the Wait action. It checks that all async calls have completed processing before moving to the next recipe step.

![Wait for async action](/assets/wait-for-async-action.gawSRsWw.png)_Wait for async action_

## Input

| Field | Description |
| --- | --- |
| Async calls to wait for | Select the async call to wait for. Only async calls can be selected by this action. |
| Timeout limit (minutes) | Set an upper limit for this wait action. Workato allows waiting up to 24 hours (1440 minutes). |

## Output

| Field | Description |
| --- | --- |
| Results | A list datapill containing metadata about the callable recipes that were called asynchronously, including the list size and list index. |
| All jobs succeeded | Whether all async calls completed successfully. |
| Job succeeded count | The number of async calls that completed successfully. |
| Job failed count | The number of async calls that failed. |
| Job timeout count | The number of async calls that exceeded the timeout limit defined in the input configuration. |

> **Not applicable for dependent steps**
> 
> Using [call recipe (asynchronous)](/en/features/callable-recipes/call-recipe-action#call-recipe-asynchronous) does not guarantee that the callable recipes will run in sequence. If your workflow requires steps to be called in sequence, use the [Call recipe (synchronous)](/en/features/callable-recipes/call-recipe-action#call-recipe-asynchronous) instead.

## FAQ - Wait for Async calls issued within a loop

This action will not pick up Async calls that start inside of a loop. If the Wait action itself is not in the loop, all Async calls inside of the loop will not be picked up.

This will cause the recipe to continue without waiting. This may cause downstream actions to fail.

> **This action will not wait for Async calls from a loop**
> 
> The Wait action does not work if the Async calls are started from inside of a loop.
> 
> ![Bad example: Starting Async call from a loop](/assets/wait-for-async-loop-bad-example.BwObKVWm.png)_Bad example: Starting Async call from a loop_

Instead, each Async call in the [action input](#input) must be explicitly configured as a recipe step. In the example below, the recipe is making Async calls to update the `sales` and `leads` tables.

![Only wait for the last call](/assets/wait-for-async-explicit-steps.Co2dvd4D.png)_Each Async call is explicitly configured as a recipe step_

## FAQ - Output of async recipes not available

Asynchronous calls to recipes do not wait for a response, thus there will not be any `reply` output. If your use case requires information from a called recipe (asynchronous), you can use [Lookup table](/en/features/lookup-tables) actions to pass the information.

### Workaround using lookup table

1. Call recipe (asynchronous) with a unique ID. You can use the job ID of the main recipe or a unique timestamp.

![Make async call with unique lookup id](/assets/call-with-lookup-id.DMPD8GbE.png)

2. After the called recipe has finished processing, [Add an entry](/en/features/lookup-tables#add-entry-action) to the lookup table with the unique ID.

![Add lookup entry after async call](/assets/add-lookup-entry.58afS55o.png)

3. Next, retrieve the lookup table entry with the [Search entries](/en/features/lookup-tables#search-entries-action-batch) action using the same unique ID.

![Retrieve lookup value](/assets/search-with-lookup-id.DVquSYqb.png)

---
