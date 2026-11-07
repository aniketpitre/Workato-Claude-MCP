---
url: 'https://docs.workato.com/en/connectors/google-calendar/action-update-task.md'
description: >-
  The Update task action updates an existing task in a Google Calendar task list
  you specify.
---

# Google Calendar - Update task action

The **Update task** action updates an existing task in a Google Calendar task list you specify. Updated tasks are assigned to the connected account's time zone.

> **ENSURE CALENDAR ACCESS**
> 
> Ensure the calendar you plan to modify is accessible from your connected account and that you have the necessary permissions to manage tasks.

## Input

| Input field | Description |
| --- | --- |
| Tasklist | Enter the ID of the task list in which you plan to update a task. |
| Task ID | Enter the Google Calendar ID of the task you plan to update. |
| Notes | Enter any relevant notes or additional information to add to the task. |
| Status | Enter `needsAction` or `completed` to set the status of the task. |
| Due date | Enter a due date for task completion. |
| Completed date | Enter the date the task was completed. |
| Hidden | Select whether to hide the task from the default task list view. |

## Output

| Output field | Description |
| --- | --- |
| ID | The Google ID for the created task. |
| Etag | The etag for the task. |
| Parent | The Google ID of the parent task, if the created task is a subtask. |
| Title | The title of the task. |
| Description | The task's description. |
| Status | The status of the task. |
| Position | The position of the task in the task list. |
| Self link | The URL of the task in the Google Tasks interface. |
| Updated | The time the task was last updated. |
| Due date | The due date assigned to the task. |
| Completed date | The date when the task was completed, if applicable. |
| Hidden | Indicates whether the task is hidden. |
| Deleted | Indicates whether the task is marked as deleted. |
| Links | Contains associated links for the task, such as: **Type:** The type of link., **Description:** A description of the link., **Link:** The URL., **List size:** The total number of links associated with the task., **List index:** The position of this specific link in the list of links. |

---
