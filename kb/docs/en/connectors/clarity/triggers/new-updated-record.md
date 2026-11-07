---
url: 'https://docs.workato.com/en/connectors/clarity/triggers/new-updated-record.md'
description: >-
  The New/updated record trigger in the Clarity connector monitors a selected
  object type and fires when records are created or updated.
---

# Clarity - New/updated record trigger

The **New/updated record** trigger monitors a specified Clarity object type for new or updated records.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. |
| Object | Select the object to monitor for new or updated records. Options include:. |
| Filter condition | Configure this field to filter the returned records. Use Clarity query syntax, for example `(isActive = true)`. |
| Limit | Specify the maximum number of records to return. The maximum is 100 records per poll for optimal performance. |
| Offset | Specify the starting offset for pagination. Used internally for polling. |
| Sort | Define the sort order using field names. The default is `lastUpdatedDate asc` for incremental polling. |
| Fields to retrieve | Select specific fields to retrieve. ID and lastUpdatedDate fields are included for proper tracking. |

Additional fields may load based on the object you select.

## Output

The trigger returns individual records as they are created or updated. The output fields vary based on the selected object type and fields to retrieve.

---
