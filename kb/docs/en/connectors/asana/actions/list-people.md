---
url: 'https://docs.workato.com/en/connectors/asana/actions/list-people.md'
description: The List people batch action lists people in Asana.
---

# Asana - List people action (batch)

The **List people** batch action lists people in Asana.

## Input

| Input field | Description |
| --- | --- |
| Workspace | Enter the workspace or organization ID to filter users by. |
| Limit | Enter the number of objects to return per page. The value must be between 1 and 100. You must provide a workspace for pagination. |
| Offset | Enter an offset to the next page returned by the API. If you don't provide an offset, the API returns the first page of results. |

## Output

| Output field | Description |
| --- | --- |
| People | Array of all people. |
| ID (People) | The unique identifier of each person. |
| Email (People) | The email address of each person. |
| Name (People) | The name of each person. |
| Next page | Pagination information for the next page of results. |
| Offset (Next page) | The offset for the next page. |
| Path (Next page) | The path for the next page. |
| URI (Next page) | The URI for the next page. |

---
