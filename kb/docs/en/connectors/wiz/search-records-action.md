---
url: 'https://docs.workato.com/en/connectors/wiz/search-records-action.md'
description: >-
  The Search records action retrieves a list of records from Wiz based on the
  specified object and search criteria.
---

# Wiz - Search records action

The **Search records** action retrieves a list of records from Wiz based on the object type and search criteria you specify. Use this action to fetch all matching records for supported objects.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the Wiz object to query. |
| Sub queries | Optional. Select related records to include in the response. |
| Order by | Optional. Define sorting options for the results. |

Additional fields may appear depending on the selected object.

## Output

The output includes a list of records that match the search criteria. The structure of each record varies based on the selected object. Common output fields may include the following:

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the record. |
| Name | Name of the record. |
| Type | Type or category of the record. |
| Status | Current status of the record. |

The full set of output fields depends on the selected object and its schema.

---
