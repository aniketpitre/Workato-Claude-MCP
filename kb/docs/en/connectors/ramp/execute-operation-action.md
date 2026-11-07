---
url: 'https://docs.workato.com/en/connectors/ramp/execute-operation-action.md'
description: >-
  Call a Ramp API endpoint that doesn't fit the other actions, with fields
  generated live from Ramp's own API schema for the operation you select.
---

# Ramp - Execute operation action

The **Execute operation** action calls a Ramp API endpoint that the other actions don't cover.

> **FALLBACK FOR UNMATCHED ENDPOINTS**
> 
> This connector automatically sorts Ramp's API endpoints into the Get record details by ID, Create record, Update record, Delete record, and Search records actions where possible. An endpoint only appears in this action's **Operation** list if it can't be matched to one of those. Refer to [API operation grouping](/en/connectors/openapi/guides/customizing-openapi-interfaces#api-operation-grouping) for more information.

## Input

Input fields dynamically generate based on the object you select and the execute operation. The following fields are common to all objects. Refer to the Ramp [REST API](https://docs.ramp.com/developer-api/v1/api/) documentation for a list of input fields.

| Input field | Description |
| --- | --- |
| Filter operations | Optional. Select a category to narrow down the **Operation** list. |
| Operation name | Optional. Enter a more descriptive name for this step in the recipe editor. The **Operation name** doesn't affect the request. |
| Operation | Select the Ramp API operation to call. |

## Output

Output fields match the selected operation's response schema in Ramp's API. Refer to the Ramp [REST API](https://docs.ramp.com/developer-api/v1/api/) documentation for field details by operation.

---
