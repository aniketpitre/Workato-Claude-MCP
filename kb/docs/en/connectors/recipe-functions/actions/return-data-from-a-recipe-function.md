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
