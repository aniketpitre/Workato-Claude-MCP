---
url: >-
  https://docs.workato.com/en/data-tables/connector/delete-records-condition-action.md
description: >-
  The delete records by condition batch action deletes records that match the
  filter conditions you specify, up to 200 records per run.
---

# Delete records by condition action (batch)

The **Delete records by condition** batch action deletes records that match the filter conditions you specify in a data table. Each run deletes up to 200 records.

The action deletes the first 200 records when more than 200 records match your filters. The remaining matching records stay in the table, and the job still completes successfully. Run the action again with the same filters to delete them. Repeat until **Deleted records count** is less than `200`.

## Input

| Input fields | Description |
| --- | --- |
| Data table | Select the data table to delete records from. Click the link in this field's description to view the selected data table in the [Data tables interface](/en/data-tables/data-table-interface). |
| Filters | Define the conditions a record must meet before this action deletes it. Each filter contains a **Column name**, **Operand**, and **Value** field. Click **Add filter** to add filters for additional columns. The available operands vary based on the selected column's type. Refer to [Available operands by column type](#available-operands-by-column-type) for supported options. |

## Output

| Output fields | Description |
| --- | --- |
| Deleted records count | Total number of records this action deleted. |

## Available operands by column type

The following table lists the operands available for each data table column type.

| Column type | Available operands |
| --- | --- |
| ID | `equals`, `not equals` |
| String, File | `equals`, `not equals`, `is null`, `is not null`, `starts with` |
| Integer, Number | `equals`, `not equals`, `greater than`, `less than`, `greater than or equals`, `less than or equals`, `is null`, `is not null` |
| Date, Date-time | `equals`, `not equals`, `is after`, `is before`, `is on or after`, `is on or before`, `is null`, `is not null` |
| Boolean | `is true`, `is false`, `is null`, `is not null` |
| Relation | `equals`, `not equals`, `in`, `is null`, `is not null` |
| Set types (string set, number set, integer set, date set, date-time set, relation set) | `contains`, `is null`, `is not null` |
