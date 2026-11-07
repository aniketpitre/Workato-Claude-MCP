---
url: 'https://docs.workato.com/en/connectors/clickup/get-record-details-action.md'
description: >-
  The **Get record details** action retrieves the details of any record, such as
  a task, via its ID from ClickUp.
---

# ClickUp - Get record details action

The **Get record details** action retrieves the details of any record, such as a task, using its ClickUp ID.

## Input

Input fields load dynamically based on the object selection. For example, if you select the **Task** object, then the following fields are available.

| Input field | Description |
| --- | --- |
| Task ID | Provide the unique ID associated with the task to be retrieved. |

## Output

The output schema loads dynamically based on the object selection. For example, if you select the **Task** object, the following output is generated.

| Output fields | Description |
| --- | --- |
| Task ID | Unique identifier of the task automatically assigned by ClickUp. |
| Custom ID | An optional user-defined ID for the task, useful for external reference or integration. |
| Name | Title or name of the task. |
| Text content | Additional textual content associated with the task, if any. |
| Description | Detailed information or explanation about the task. |
| Status | Object containing the information about task status, such as Status ID, Status, Color, Type, Order index, and more. |
| Archived | Field indicating whether the task is archived. |
| Order index | Internal value used to determine the task’s position/order in a list. |
| Date created | Timestamp of when the task was created. |
| Date updated | Timestamp of the most recent update made to the task. |
| Date closed | Timestamp of when the task was marked as completed or closed. |
| Creator | The object containing information about the user who created the task. Contains fields such as Username, Creator ID, Email, Color, and more. |
| Assignees | List of users assigned to the task. Contains fields such as Username, Assignee ID, Email, Color, and more. |
| Watchers | List of users watch the task to receive notifications of updates. Contains fields such as Username, Watcher ID, Email, Color, and more. |
| Checklists | List of checklists associated with the task, containing checklist items and their details. |
| Tags | List of labels or keywords added to categorize or identify the task. |
| Parent | Parent task ID if this task is a subtask. |
| Priority | Object containing information about the priority level assigned to the task. |
| Due date | The due date/time by which the task is expected to be completed. |
| Start date | The start date and time for the task. |
| Points | Numeric value used for effort estimation. |
| Time estimate | Estimated time to complete the task. |
| Time spent | Total time logged or tracked as spent on the task. |
| Custom fields | List of custom fields configured for the task, including field names, types, and values. |
| Dependencies | List of tasks that this task is dependent on or blocking. |
| Linked tasks | List of other tasks linked to this one, often used for cross-referencing. |
| Team ID | Unique identifier of the ClickUp team to which the task belongs. |
| URL | Direct link to view the task in the ClickUp web interface. |
| Permission level | The level of access the webhook or API user has for the task. |
| List | The object containing details of the list within ClickUp that the task belongs to. |
| Project | The object containing details of the project in ClickUp. |
| Folder | The object containing details of the folder in which the list containing the task resides. |
| Space | Space ID under which the task resides. |

---
