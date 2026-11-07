---
url: 'https://docs.workato.com/en/connectors/asana/actions/list-workspaces.md'
description: The List workspaces batch action lists all workspaces in Asana.
---

# Asana - List workspaces action (batch)

The **List workspaces** batch action lists all workspaces in Asana.

## Input

| Input field | Description |
| --- | --- |
| Limit | Enter the number of objects to return per page. The value must be between 1 and 100. |
| Offset | Enter an offset to the next page returned by the API. If you don't provide an offset, the API returns the first page of results. |

## Output

| Output field | Description |
| --- | --- |
| Workspaces | Array of all workspaces. |
| ID (Workspaces) | The unique identifier of each workspace. |
| Name (Workspaces) | The name of each workspace. |
| Next page | Pagination information for the next page of results. |
| Offset (Next page) | The offset for the next page. |
| Path (Next page) | The path for the next page. |
| URI (Next page) | The URI for the next page. |

---
