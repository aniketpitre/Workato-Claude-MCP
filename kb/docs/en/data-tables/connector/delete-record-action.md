---
url: 'https://docs.workato.com/en/data-tables/connector/delete-record-action.md'
description: >-
  The delete record action deletes a record you specify from a data table using
  its ID.
---

# Delete record action

The **Delete record** action deletes a record you specify from a data table using its ID.

## Input

| Input fields | Description |
| --- | --- |
| Data table | Select the data table you plan to delete a record from. Click the link in this field's description to view the selected data table in the [Data tables interface](/en/data-tables/data-table-interface). |
| Record ID | Provide the unique identifier of the record you plan to delete. You can input a Record ID datapill or enter a static value from the data table's **Record ID** column, which is hidden by default. |

## Output

| Output fields | Description |
| --- | --- |
| Success | A boolean (`true` or `false`) value indicating whether the record was deleted successfully. |

---

---
url: >-
  https://docs.workato.com/en/data-tables/connector/delete-record-batch-action.md
description: >-
  The delete records batch action deletes multiple records in a data table you
  specify.
---

# Delete records action (batch)

The **Delete records** batch action deletes multiple records in a data table you specify. This action supports the following maximum batch size:

| Description | Quota |
| --- | --- |
| Maximum batch size for all Data table connector batch actions, except **Delete records by condition**, which deletes up to 200 records per run | 1,000 |

## Input

| Input fields | Description |
| --- | --- |
| Data table | Select the data table you plan to delete records from. Click the link in this field's description to view the selected data table in the [Data tables interface](/en/data-tables/data-table-interface). |
| Records source list | Provide the IDs of the records you plan to delete in a list. You can input a list datapill for dynamic records or define individual fields for each record. |
| Record ID | Provide the unique identifier of the record you plan to delete. You can input a Record ID datapill or enter a static value from the data table's **Record ID** column, which is hidden by default. |

## Output

| Output fields | Description |
| --- | --- |
| Record ID | The record ID of the deleted record. |
| List size | Total number of records in the list. |
| List index | The position of the record in the list. |

---

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

---

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

---
