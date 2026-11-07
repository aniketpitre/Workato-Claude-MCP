---
url: >-
  https://docs.workato.com/en/data-tables/connector/remove-values-from-record-action.md
description: >-
  The remove values from record action removes column values from a record you
  specify.
---

# Remove values from record action

The **Remove values from record** action removes column values from a record you specify.

## Input

| Input fields | Description |
| --- | --- |
| Data table | Select the data table that contains the record you plan to remove values from. Click the link in this field's description to view the selected data table in the [Data tables interface](/en/data-tables/data-table-interface). |
| Record ID | Provide the ID of the record you plan to remove values from. You can input a Record ID datapill or enter a static value from the data table's **Record ID** column, which is hidden by default. |
| Values to be removed | Select the field values you plan to remove. Required fields cannot be selected as their values cannot be removed. |

## Output

| Output fields | Description |
| --- | --- |
| Record | Contains information about the modified record, such as its `Record ID`, `Created at` date, `Updated at` timestamp, and data from any of the data table's custom columns. |
