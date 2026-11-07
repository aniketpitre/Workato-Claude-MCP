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
