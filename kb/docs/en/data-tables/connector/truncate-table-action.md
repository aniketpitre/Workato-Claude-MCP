---
url: 'https://docs.workato.com/en/data-tables/connector/truncate-table-action.md'
description: >-
  The truncate table batch action permanently deletes all of a data table's
  records.
---

# Truncate table action (batch)

The **Truncate table** batch action permanently deletes all of a data table's records.

> **DATA DELETION IS PERMANENT**
> 
> The **Truncate table** action _can't be undone_, even if the action is run during a test job.

## Input

| Input fields | Description |
| --- | --- |
| Data table | Select the data table you plan to delete all entries from. Click the link in this field's description to view the selected data table in the [Data tables interface](/en/data-tables/data-table-interface). |

## Output

| Output fields | Description |
| --- | --- |
| Success | A boolean (`true` or `false`) value indicating whether the records were deleted successfully. |

---
