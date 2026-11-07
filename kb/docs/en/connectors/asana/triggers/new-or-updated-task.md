---
url: 'https://docs.workato.com/en/connectors/asana/triggers/new-or-updated-task.md'
description: >-
  The New/updated task trigger checks for new or updated tasks in Asana once
  every polling interval.
---

# Asana - New/updated task trigger

The **New/updated task** trigger checks for new or updated tasks in Asana once every polling interval. This trigger requires a premium Asana account.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. |
| When first started, this recipe should pick up events from | Specify the date and time from which the recipe picks up trigger events. If you leave this field blank, the trigger begins picking up tasks created or updated 1 hour ago. You can't change this value after running or testing the recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Workspace | Select the workspace to retrieve tasks from. |
| Projects | Select specific projects to monitor for tasks. By default, tasks from all projects in the workspace are selected. You can select up to a maximum of 5 projects. |
| Assignee ID | Enter either an email address or the ID of the person assigned to the tasks. By default, tasks assigned to everyone are retrieved. |

## Output

The trigger returns task details including standard task fields and any custom fields associated with the projects being monitored.

| Output field | Description |
| --- | --- |
| Task ID | The unique identifier of the task. |
| Task name | The name of the task. |
| Description | The description or notes for the task. |
| Assignee | The user assigned to the task, including ID and name. |
| Projects | Array of projects the task belongs to. |
| Tags | Array of tags associated with the task. |
| Created at | Timestamp when the task was created. |
| Modified at | Timestamp when the task was last modified. |
| Completed | Indicates whether the task has been completed. |
| Due on / Due at | The due date or due date-time for the task. |
| Custom fields | Any custom fields configured for the projects being monitored. |

---
