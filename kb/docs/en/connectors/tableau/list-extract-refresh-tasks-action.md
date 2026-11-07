---
url: >-
  https://docs.workato.com/en/connectors/tableau/list-extract-refresh-tasks-action.md
description: >-
  The List extract refresh tasks action returns a list of extract refresh tasks
  from the Tableau site.
---

# Tableau - List extract refresh tasks action

The **List extract refresh tasks** action returns a list of extract refresh tasks from the Tableau site.

## Input

This action doesn’t require any input fields.

## Output

| Output field | Description |
| --- | --- |
| Schedule ID | The unique identifier for the schedule associated with the extract refresh task. |
| Name | The name of the extract refresh task or the associated schedule. |
| State | Indicates the current status of the extract refresh task. |
| Priority | The priority of the task execution in relation to other tasks. |
| Created at | A timestamp indicating when the extract refresh task was created. |
| Updated at | A timestamp of the most recent update to the extract refresh task. |
| Type | The type of task. |
| Frequency | How often the extract refresh task runs. |
| Next run at | A timestamp indicating the next scheduled execution of the extract refresh task. |
| Workbook ID | Unique identifier for the workbook associated with the extract refresh task. |
| Extract refresh task ID | Unique identifier for the extract refresh task itself. |
| Consecutive failed count | The number of times the extract refresh task has failed consecutively. |
