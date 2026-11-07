---
url: 'https://docs.workato.com/en/connectors/authhub/search-records-action.md'
description: >-
  The Search records action retrieves a list of records from AuthHub matching
  your search criteria.
---

# AuthHub - Search records action

The **Search records** action retrieves a list of records from AuthHub matching your search criteria. The current version of the AuthHub connector only supports the **User** object for this action.

## Input

| Input field | Description |
| --- | --- |
| Filter | Enter the search criteria to filter results. |
| Sort by | Specify the field by which to sort results. |
| Sort order | Specify the order in which to sort records. Possible values are `ascending` and `descending`. |

## Output

| Output field | Description |
| --- | --- |
| Total results | The total number of users returned in the results. |
| Start index | The index number of the first result. |
| Items per page | The total number of records returned per page. |
| Schemas | A list of object schemas returned in the response. |
| Resources | An array of user records. |

---
