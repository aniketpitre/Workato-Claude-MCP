---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/create-request-action.md
description: >-
  Configure the Create request action to create a new request in a Workflow app,
  with input fields based on the app and its data table.
---

# Create request action

Use this action to create a request in a Workflow app.

## Input

| Input Field | Description |
| --- | --- |
| Workflow app | Select a Workflow app in which to create a new request. |
| New request fields | Fill in the fields for the new request. The available fields are determined by the Workflow app you select. |

### Additional input fields

Additional input fields are variable. They are determined by the Workflow app you select and the columns present in its corresponding data table.

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
