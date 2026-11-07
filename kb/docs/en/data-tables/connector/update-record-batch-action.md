---
url: >-
  https://docs.workato.com/en/data-tables/connector/update-record-batch-action.md
description: >-
  The update records batch action updates multiple records in a data table you
  specify.
---

# Update records action (batch)

The **Update records** batch action updates multiple records in a data table you specify. This action supports the following maximum batch size:

| Description | Quota |
| --- | --- |
| Maximum batch size for all Data table connector batch actions, except **Delete records by condition**, which deletes up to 200 records per run | 1,000 |

## Input

| Input fields | Description |
| --- | --- |
| Data table | Select the data table in which you plan to update records. Click the link in this field's description to view the selected data table in the [Data tables interface](/en/data-tables/data-table-interface). |
| Choose the desired output format | Optional. Specify how to map the updated record data to the table fields. Refer to the [Output formats](/en/data-tables/data-table-connector#output-formats) section for more information. |
| Records source list | Provide the IDs of the records you plan to update in a list. You can input a list datapill for dynamic records or define individual fields for each record. |

> **ADDITIONAL INPUT FIELDS**
> 
> The **Record fields** section contains an input field for each column of the selected data table. Use these input fields to specify the values to update the records with. If you leave a field empty, Workato does not update the corresponding column.
> 
> These input fields are subject the same restrictions as their corresponding columns, for example:
> 
> - If a column is required, its corresponding field is also required.
> - The value you provide must match the corresponding column's data type. For instance, text columns only accept alphanumeric characters. Refer to [Column types](/en/data-tables/user-interface/column-types) for detailed information on the accepted values for each data type.

## Output

| Output fields | Description |
| --- | --- |
| Record | Contains information about each individual updated record, such as their `Record ID`, `Created at` date, `Updated at` timestamp, and data from any of the data table's custom columns. |
| List size | Total number of records in the list. |
| List index | The position of each record in the list. |
