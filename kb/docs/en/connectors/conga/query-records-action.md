---
url: 'https://docs.workato.com/en/connectors/conga/query-records-action.md'
description: The Query records action searches for records in Conga.
---

# Conga - Query records action

The **Query records** action searches for records in Conga.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to query for. |
| Include total count | Select `True` or `False` to determine if the response will include a total count of records. |

## Output

| Output field | Description |
| --- | --- |
| Success | A boolean response that indicates if the action was successful. |
| Data | ID: The ID of the query result in the search results., Name: The name of the record in the query results., Created by: The ID and name of the user that created the record., Created date: The date the record was created., Modified by: The ID and name of the user that modified the record., Modified date: The date the record was modified., E tag: The E tag associated with the queried record., External ID: The external ID of the queried record. |
| Has more records | Indicates if the query includes additional records. |
| Record count | A count of the total number of records in the query. |
| Status code | A code indicating the status of the action, such as `OK`, `BadRequest`, `Unauthorized`, and more. |
| Next cursor | An identifier for the next page of query results. |

---
