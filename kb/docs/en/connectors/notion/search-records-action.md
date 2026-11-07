---
url: 'https://docs.workato.com/en/connectors/notion/search-records-action.md'
description: >-
  The Search records action in the Notion connector retrieves a list of Notion
  objects matching the object type you specify.
---

# Notion - Search records action

The **Search records** action retrieves a list of Notion objects matching the type you specify.

## Input

| Field | Description |
| --- | --- |
| Object | Select the object type to search for. |
| Block ID | Provide the internal ID of the block to search for its child objects. |
| Cursor | Provide the `next_cursor` value to retrieve the next page of results. Defaults to the first page if left blank. |
| Page size | Enter the number of objects to return per page. The maximum and default value is `100`. |

## Output

| Field | Description |
| --- | --- |
| Block children | Contains information about the block's children objects, such as their `Created time`, `Archived` status, and `Type`. |
| Users | Contains information about the users retrieved, such as their `ID`, `Name`, and `Type`. |
| Next cursor | The identifier for the next page of results. |
| Has more | Indicates if there are additional results. |

---
