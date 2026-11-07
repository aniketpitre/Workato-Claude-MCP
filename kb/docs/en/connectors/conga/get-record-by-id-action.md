---
url: 'https://docs.workato.com/en/connectors/conga/get-record-by-id-action.md'
description: The Get record by ID action retrieves a record by using the ID in Conga.
---

# Conga - Get record by ID action

The **Get record by ID** action retrieves a record by using the ID in Conga.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to retrieve. |
| Record ID | Enter the ID of the record to retrieve. |

## Output

| Output field | Description |
| --- | --- |
| Success | A boolean response that indicates if the action was successful. |
| Record count | A count of the total number of records in the query. |
| Data | ID: The ID of the record returned in the search results., Name: The name of the returned record., Created by: The ID and name of the user that created the record., Created date: The date the record was created., Modified by: The ID and name of the user that modified the record., Modified date: The date the record was modified., E tag: The E tag associated with the returned record., External ID: The external ID of the returned record. |
| Status code | A code indicating the status of the action, such as `OK`, `BadRequest`, `Unauthorized`, and more. |

---
