---
url: 'https://docs.workato.com/en/connectors/recipeops/actions/list-connections.md'
description: >-
  The List connections action in the RecipeOps connector retrieves connection
  details in the account, filtered by name, recipe, and application type.
---

# RecipeOps - List connections action

This action retrieves details about connections in the Workato account. Results can be filtered by name, recipe, and application type (for example, Salesforce).

This action also supports retrieving runtime user connections. To search for these connections, provide an external ID or parent-child relationship.

* * *

## Limitations

Results are limited to 1,000 connections, ordered by most recently updated.

* * *

## Input

| Field | Description |
| --- | --- |
| **Connection name** | Searches for connections using the full name of the connection. **Note**: Search is case-sensitive. |
| **Recipe** | Filters connections by recipe. If defined, results will be limited to connections used in the selected recipe. |
| **Application** | Filters connections by application type. If defined, results will be limited to connections of this application type. For example: If **Salesforce** is selected, only **Salesforce** connections will be included in the results. |
| **Parent connection name** | **Applicable when [Runtime user connections](/features/runtime-user-connections.html) are being used.** Filters connections by their parent connection. If defined, results will be limited to connections linked to the selected parent connection. **Note**: If searching for child connections, the **Search for child connections** field should also be defined. |
| **Search for child connections** | If **Yes**, the action will search for child connections using the **Parent connection name** value. |
| **External ID** | Filters connections by their external ID. If defined, results will be limited to connections with the provided external ID. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Connection ID** | The ID of the connection. |
| **User ID** | This ID indicates the Workspace where the connection is located. |
| **Name** | The name of the connection. |
| **Application** | The application type of the connection. For example: `salesforce` |
| **Authorization status** | The current authorization status of the connection. |
| **Authorization error** | If the connection's **Authorization status** is in an error state, this will describe the reason for the error state. |
| **Authorized at** | The time the connection was authorized. |
| **Created at** | The time the connection was created. |
| **Updated at** | The time the connection was last updated. |
| **List size** | The total number of connections in the result set. |
| **List index** | The index (current position) of the connection in the list of results. |

* * *

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---
