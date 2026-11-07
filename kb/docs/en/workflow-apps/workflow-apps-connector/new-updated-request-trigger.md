---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/new-updated-request-trigger.md
description: >-
  Configure the New/updated request trigger to run a recipe when a Workflow app
  request, task, or data table record is created or updated.
---

# New/updated request trigger

This real-time trigger runs when there is a New/updated request in a Workflow app.

It also runs when the following events occur:

- When a new task in a Workflow app is created.
- When a user completes a task or a task expires.
- When a task is reassigned from one app user to another app user.
- When a user creates/updates a record manually in a Workflow app's corresponding [data table](/en/data-tables).

## Input

| Input field | Description |
| --- | --- |
| Workflow app | Choose a Workflow app to check for new requests. |
| When first started this recipe should pick up events from | Get new requests since a particular date/time. Leave empty to get new requests since one hour ago. Once the recipe has been run or tested, you cannot change this value. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

You can also toggle **Set trigger condition** to only process trigger events matching conditions you specify.

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

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
| Change ID | The ID number that corresponds to the Workflow app's corresponding data table. |

### Old request object

| Output field | Description |
| --- | --- |
| Record ID | Workato automatically generates a unique ID for each record in a Workflow app's data table. |
| Assigned task (Old request) | A nested object within the `Old request` object. Empty if no active task is associated with the request. |
| Task ID (Assigned task) | Task ID of the assigned task. |
| Task name (Assigned task) | Name of the assigned task. |
| Status (Assigned task) | Status of the assigned task. |
| Due date (Assigned task) | Due date of the assigned task. |
| Task URL (Assigned task) | URL of the assigned task. |
| Assigned user (Assigned task) | A nested object within the `Assigned task` object. Empty if task is assigned to a group. |
| User ID (Assigned user) | User ID of the assigned user. |
| User name (Assigned user) | Name of the assigned user. |
| Email (Assigned user) | Email of the assigned user. |
| Status (Assigned user) | Status of the assigned user. |
