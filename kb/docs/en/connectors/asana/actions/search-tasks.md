---
url: 'https://docs.workato.com/en/connectors/asana/actions/search-tasks.md'
description: >-
  The Search tasks batch action searches tasks in a specified workspace in
  Asana.
---

# Asana - Search tasks action (batch)

The **Search tasks** batch action searches tasks in a specified workspace in Asana.

## Input

| Input field | Description |
| --- | --- |
| Workspace ID | Enter the workspace ID. |
| Assignee ID | Enter the assignee ID. Leave this field empty to get tasks assigned to the authorized user. |

## Output

| Output field | Description |
| --- | --- |
| Tasks | Array of tasks that belong to the assignee. |
| ID (Tasks) | The unique identifier of each task. |
| Name (Tasks) | The name of each task. |
| Created by (Tasks) | The user who created each task. |
| ID (Created by) | The unique identifier of the creator. |
| Name (Created by) | The name of the creator. |
| Resource type (Created by) | The resource type of the creator. |

---
