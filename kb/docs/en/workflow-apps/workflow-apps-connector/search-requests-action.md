---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/search-requests-action.md
description: >-
  Configure the Workflow apps connector search requests action to find requests
  matching filters, sort criteria, and result quotas.
---

# Search requests action

Search requests in a Workflow app matching criteria you specify.

## Input

| Input Field | Description |
| --- | --- |
| Workflow app | Select the Workflow app from which you plan to retrieve lists. |
| Filters | Add one or more filters to the query. All filters must contain `Column name`, `Operand`, and `Value`. All filters are chained using `AND`. |
| Column name | Available column names depend on the Workflow app you select and the columns available in its corresponding data table. |
| Operand | Available operands depend on the Workflow app and column types. Operands by data type include: Short text Equals, Is not equal to, Is null, Is not null ; Long text Equals, Is not equal to, Is null, Is not null ; Integer Equals, Is not equal to, Is less than, Is greater than, Is less or equals, Is greater or equals, Is null, Is not null ; Decimal Equals, Is not equal to, Is less than, Is greater than, Is less or equals, Is greater or equals, Is null, Is not null ; Boolean Is true, Is false, Is null, Is not null ; Date Equals, Is not equal to, Is before, Is after, Is on or before, Is on or after, Is null, Is not null ; DateTime Equals, Is not equal to, Is before, Is after, Is on or before, Is on or after, Is null, Is not null |
| Value | The value you enter must match the data type of the column and the operand you select. |
| Sort by | Organize search results by `Column name`. Options depend on the Workflow app and its data table. |
| Sort direction | Order search results in `Ascending` or `Descending` order. |
| Limit | Determine how many records to fetch. The default is 100 and the maximum is 200 records. |
| Next page token | Get records starting from the specified offset. |

* * *

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

| Output field | Description |
| --- | --- |
| Request | This object represents a record in a Workflow app. It includes metadata and links to related objects. |
| Record ID | Workato automatically generates a unique ID for each record in a Workflow app's corresponding data table. |
| Active task (Request) | A nested object within the `Request` object. Empty if there is not an active task associated with the request. |
| Task ID (Active task) | The ID of the task. |
| Task name (Active task) | The name of the task. |
| Status (Active task) | The task's status. |
| Due date (Active task) | The due date of the task. |
| Task URL (Active task) | The URL for the task. |
| Assigned user (Active task) | A nested object within the `Active task` object containing information about the task assignee. Empty if the task is assigned to a group. |
| User ID (Assigned user) | The ID of the user assigned to the task. |
| User name (Assigned user) | The name of the user assigned to the task. |
| Email (Assigned user) | The email of the user assigned to the task. |
| Status (Assigned user) | The status of the user assigned to the task. |
| Assigned group (Active task) | A nested object within the `Active task` object containing information about the assigned group. Empty if the task is assigned to an individual user. |
| User ID (Assigned group) | The ID of the user assigned to the task. |
| User name (Assigned group) | The name of the user assigned to the task. |
| Email (Assigned group) | The email of the user assigned to the task. |
| Status (Assigned group) | The status of the user assigned to the task. |
| Created by (Request) | A nested object within the `Request` object containing information about the user who created the request. |
| User ID (Created by) | The ID of the user who created the request. |
| User name (Created by) | The name of the user who created the request. |
| Email (Created by) | The email of the user who created the request. |
| Status (Created by) | The status of the user. |
| Groups (Created by) | A nested object within the `Created by` object containing information on group membership. |
| Group ID (Groups) | The ID of the group this task is assigned to. |
| Group name (Groups) | The name of the group this task is assigned to. |
| List size (Groups) | The size of the list. |
| List index (Groups) | The list index. |
| Stage (Request) | A nested object within the `Request` object containing stage details. |
| Stage ID (Stage) | The ID of the group this task is assigned to. |
| Group name (Stage) | The name of the group this task is assigned to. |
| Created at | The date the record was created. |
| Updated at | The date the record was most recently updated. |
| Next page token | Get records starting from the specified offset. |
| List size | Size of the list. |
| List index | Index of the list. |
