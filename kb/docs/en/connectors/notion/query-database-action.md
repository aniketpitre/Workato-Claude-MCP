---
url: 'https://docs.workato.com/en/connectors/notion/query-database-action.md'
description: >-
  The Query database action in the Notion connector searches a database and
  returns the records that match the filter and sort criteria you specify.
---

# Notion - Query database action

The **Query database** action searches a Notion database and returns a list of records that match the criteria you specify.

## Input

| Field | Description |
| --- | --- |
| Database | Select the database to search. |
| Filter source list | Input a list datapill to create the filter from. |
| Column | Select the column to filter by. |
| Value | Provide the value to compare against the selected **Column** values. |
| Filter condition | Specify how to compare the returned **Column** values against the **Value** you set. |
| Condition | Specify whether to use `AND` or `OR` logic for the filter's conditions. |
| Sort by | Select a property to sort the results by. |
| Sort order | Specify whether to sort the records in ascending or descending order. |
| Sort by Timestamp column | Select a timestamp column to sort the results by. |
| Cursor | Provide the `next_cursor` value to retrieve the next page of results. Defaults to the first page if left blank. |
| Page size | Enter the number of records to return per page. The maximum and default value is `100`. |

## Output

| Field | Description |
| --- | --- |
| Object | The type of object retrieved. |
| Page ID | The identifier for the associated page. |
| Created time | The timestamp when the object was created. |
| Last edited time | The timestamp when the object was last updated. |
| Archived | Indicates whether the database is archived. |
| URL | The queried object's URL. |
| Parent | Contains information about the queried object's parent, such as its `Type` and `ID`. |
| Properties | Contains information about the queried object's properties, such as its `Title`, `Type`, and `ID`. |
| List size | The total number of matching results. |
| List index | The position of the returned entries within the results list. |
| Next cursor | The identifier for the next page of results. |
| Has more | Indicates if there are additional results. |

---
