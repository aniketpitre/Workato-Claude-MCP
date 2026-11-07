---
url: 'https://docs.workato.com/en/connectors/odata/new-record-trigger.md'
description: >-
  The New record trigger in the OData connector fires when a new record is
  created for the object you select.
---

# OData - New record trigger

The **New record** trigger activates when a record is created for the object you select in OData. The list of objects is dynamically generated based on the API endpoints found in the OData document.

You must select the appropriate timestamp cursor to provide the required information for handling time-ranges.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the object to monitor for new records. |
| Timestamp cursor | Select the timestamp cursor for the date-time field to filter results by. For example, LastChangedTime or Createdtime. |
| When first started, this recipe should pick up events from | Enter a data and time from which the recipe picks up trigger events from. Leave empty to get records created or updated one hour ago. |
| Expand | Select or enter related entities to expand. |

## Output

Output fields load dynamically based on the object you select.

---
