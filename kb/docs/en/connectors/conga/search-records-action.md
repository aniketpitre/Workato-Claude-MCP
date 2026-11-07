---
url: 'https://docs.workato.com/en/connectors/conga/search-records-action.md'
description: The Search records action searches for records in Conga.
---

# Conga - Search records action

The **Search records** action searches for records in Conga.

## Input

Input fields generate dynamically based on the object you select. The following are common input fields for all object types.

| Input field | Description |
| --- | --- |
| Objects | Select the type of object to search for. |
| Page size | Enter the number of records to return on each page. |
| Page number | Enter the number of pages to fetch. |
| Sort field | Enter a field name to sort results by. |
| Sort direction | Specify the sort direction. |

## Output

Output fields generate dynamically based on the object you select. The following are common output fields for all object types.

| Output field | Description |
| --- | --- |
| Success | A boolean response that indicates if the action was successful. |
| Record count | A count of all the records returned. |
| Data | ID: The ID of the record in the search results., Name: The name of the record in the search results., Created by: The ID and name of the user that created the record., Created date: The date the record was created., Modified by: The ID and name of the user that modified the record., Modified date: The date the record was modified., E tag: The E tag associated with the record., External ID: The external ID of the record. |
| Status code | A code indicating the status of the action, such as `OK`, `BadRequest`, `Unauthorized`, and more. |

---
