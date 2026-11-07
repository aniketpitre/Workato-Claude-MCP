---
url: 'https://docs.workato.com/en/connectors/clickup/new-record-trigger.md'
description: The **New record** trigger runs when a new task is created in ClickUp.
---

# ClickUp - New record trigger

The **New record** trigger runs immediately as soon as trigger events, such as a task creation, occur in ClickUp.

## Input

| Input field | Description |
| --- | --- |
| Workspace/Team | Select the name of the team or workspace from the drop-down menu. |
| Subtasks | Select the boolean value from the drop-down menu to include the subtasks. |
| Trigger poll interval | Select how frequently to check for new events. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up trigger events from this specified date and time. Leave empty to get events created one hour ago. |

## Output

| Output field | Description |
| --- | --- |
| Task ID | Unique identifier of the task automatically assigned by ClickUp. |
| Custom ID | An optional user-defined ID for the task, useful for external reference or integration. |
| Name | Title or name of the task. |
| Text content | Additional textual content associated with the task, if any. |
| Description | Detailed information or explanation about the task. |
| Status | Object containing the information about task status, such as Status ID, Status, Color, Type, Order index, and more. |
| Archived | Field indicating whether the task is archived. |
| Order index | Internal value used to determine the task’s position in a list. |
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
| Due date | The date and time by which the task must be completed. |
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
