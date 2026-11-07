---
url: 'https://docs.workato.com/en/connectors/filevine/list-records-action.md'
description: >-
  The List records action retrieves a specific record from Filevine based on the
  selected object and identifier.
---

# Filevine - List records action

The **List records** action retrieves a list of records from Filevine based on the selected object type.

## Input

| Input field | Description |
| --- | --- |
| Object type | Select the Filevine object to query. |

## Output

| Output field | Description |
| --- | --- |
| Links | Navigation links for paginated results. |
| Count | Number of records returned in the current response. |
| Offset | Offset used for paginating the results. |
| Last ID | ID of the last record in the current result set. |
| Limit | Maximum number of records returned per request. |
| Has more | Indicates whether more records are available. |
| Requested fields | Fields requested for each record. |
| Items | List of record objects matching the query. |

---
