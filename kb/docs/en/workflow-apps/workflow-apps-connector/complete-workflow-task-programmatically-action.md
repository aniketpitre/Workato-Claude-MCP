---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/complete-workflow-task-programmatically-action.md
description: >-
  Configure the Complete workflow task programmatically action to approve,
  reject, or complete a Workflow app task with an optional status label.
---

# Complete workflow task programmatically

Use this action to complete a workflow task programmatically. For example, you can use it to perform a workflow task in a different UI (including Workbot for Slack or Microsoft Teams), or to close a task that is no longer valid.

## Input

| Input field | Description |
| --- | --- |
| Workflow app | Select a Workflow app in which to complete a task. |
| Record ID | Choose a request (identified by its **Record ID**) to update. Use a datapill or enter the exact ID. Workato automatically generates a unique ID for each record in a Workflow app's corresponding data table. |
| Task status | Complete a task by approving, rejecting, or completing it. |
| Custom status label | _Optional_. Provide a custom task status label to customize what users see when a task is approved, rejected, or completed in the portal. For example, you can use a custom task status such as `sent for rework` to accompany a `rejected` status. This communicates clearly the reason the request was rejected and enables you to configure conditional logic to customize how your workflow handles requests assigned custom task status labels. When left empty, the label appears the same as the task status. |
| Email address | _Optional_. Provide the email address of the assignee you plan to complete the task. If this field is left empty, Workato defaults to the currently assigned user. |

* * *

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

### Completed task object

| Output field | Description |
| --- | --- |
| Task ID | Workato automatically generates a unique ID for each task in a `Task` object. |
| Task name | The name of the task. |
| Status | The task's status. Available values include: `Approved`, `Rejected` and `Expired`. |
| Custom status label | The custom status label applied to the task. |
| Is approved | Whether the task was completed with `Approved` status. |
| Is rejected | Whether the task was completed with `Rejected` status. |
| Is expired | Whether the task was completed with `Expired` status. |
| Created at | The date the task was created. |
| Completed at | The date the task was completed. |
| Completed by (Task) | A nested object within the `Task` object describing the user that completed the task. Empty if the task is expired. |
| User ID (Completed by) | The user's ID. |
| Task name (Completed by) | Name of the task. |
| Email (Completed by) | The user's email address. |

### Request object

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
