---
url: 'https://docs.workato.com/en/connectors/alayacare/search-records-action.md'
description: The Search records action searches and retrieves records in AlayaCare.
---

# AlayaCare - Search records action

The **Search records** action searches and retrieves records in AlayaCare.

## Input

Input fields load dynamically based on the selected object. For example, if you select the **Client** object, the following fields appear:

| Input fields | Description |
| --- | --- |
| Object | Select the AlayaCare object to search. |
| Page | Enter the page number to start the search. Default is `1`. |
| Count | Enter the number of records to list per page. |
| Branch | Enter a branch ID to filter records by. |
| Filter | Enter filters to search records by. |
| Status | Enter a client status to filter by. |
| Group | Enter a group ID to filter by. |
| AlayaCare ID | Enter an AlayaCare ID to filter by. |

## Output

| Output fields | Description |
| --- | --- |
| Count | The total number of records returned by the search. |
| Page | The page number where the search started. |
| Total pages | The total number of pages returned in the search. |
| Items | Additional details related to the search results. |

Additional output fields load dynamically based on the object you select.

---
