---
url: 'https://docs.workato.com/en/connectors/asana/actions/list-project-tasks.md'
description: >-
  The List project tasks batch action lists tasks in a specified project in
  Asana.
---

# Asana - List project tasks action (batch)

The **List project tasks** batch action lists tasks in a specified project in Asana.

## Input

| Input field | Description |
| --- | --- |
| Project ID | Enter the project ID. You can find this value in the URL of the project page. |
| Limit | Enter the number of objects to return per page. The value must be between 1 and 100. |
| Offset | Enter an offset to the next page returned by the API. If you don't provide an offset, the API returns the first page of results. |

## Output

| Output field | Description |
| --- | --- |
| Tasks | Array of tasks that belong to the specified project. |
| ID (Tasks) | The unique identifier of each task. |
| Name (Tasks) | The name of each task. |
| Created by (Tasks) | The user who created each task. |
| ID (Created by) | The unique identifier of the creator. |
| Name (Created by) | The name of the creator. |
| Resource type (Created by) | The resource type of the creator. |
| Next page | Pagination information for the next page of results. |
| Offset (Next page) | The offset for the next page. |
| Path (Next page) | The path for the next page. |
| URI (Next page) | The URI for the next page. |

---
