---
url: 'https://docs.workato.com/en/data-tables/connector/create-record-action.md'
description: The create record action creates a new record in a data table you specify.
---

# Create record action

The **Create record** action creates a new record in a data table you specify.

## Input

| Input fields | Description |
| --- | --- |
| Data table | Select the data table you plan to add a record to. Click the link in this field's description to view the selected data table in the [Data tables interface](/en/data-tables/data-table-interface). |
| Choose the desired output format | Optional. Specify how to map the new record data to the table fields. Refer to the [Output formats](/en/data-tables/data-table-connector#output-formats) section for more information. |

> **ADDITIONAL INPUT FIELDS**
> 
> The **New record fields** section contains an input field for each column of the selected data table. Use these input fields to specify the content of the new record.
> 
> These input fields are subject the same restrictions as their corresponding columns, for example:
> 
> - If a column is required, its corresponding field is also required.
> - The value you provide must match the corresponding column's data type. For instance, text columns only accept alphanumeric characters. Refer to [Column types](/en/data-tables/user-interface/column-types) for detailed information on the accepted values for each data type.

## Output

| Output fields | Description |
| --- | --- |
| Record | Contains information about the new record, such as its `Record ID`, `Created at` date, `Updated at` timestamp, and data from any of your data table's custom columns. |

---

---
url: >-
  https://docs.workato.com/en/data-tables/connector/create-record-batch-action.md
description: >-
  The create records batch action creates new records in a data table you
  specify.
---

# Create records action (batch)

The **Create records** batch action creates new records in a data table you specify. This action supports the following maximum batch size:

| Description | Quota |
| --- | --- |
| Maximum batch size for all Data table connector batch actions, except **Delete records by condition**, which deletes up to 200 records per run | 1,000 |

## Input

| Input fields | Description |
| --- | --- |
| Data table | Select the data table you plan to add records to. Click the link in this field's description to view the selected data table in the [Data tables interface](/en/data-tables/data-table-interface). |
| Choose the desired output format | Optional. Specify how to map the new record data to the table fields. Refer to the [Output formats](/en/data-tables/data-table-connector#output-formats) section for more information. |
| New records source list | Provide a list of records to create in the specified data table. You can input a list datapill for dynamic records or define individual fields for each record. |

> **ADDITIONAL INPUT FIELDS**
> 
> The **New record fields** section contains an input field for each column of the selected data table. Use these input fields to specify the content of the new records.
> 
> These input fields are subject the same restrictions as their corresponding columns, for example:
> 
> - If a column is required, its corresponding field is also required.
> - The value you provide must match the corresponding column's data type. For instance, text columns only accept alphanumeric characters. Refer to [Column types](/en/data-tables/user-interface/column-types) for detailed information on the accepted values for each data type.

## Output

| Output fields | Description |
| --- | --- |
| Record | Contains information about each individual record created, such as its `Record ID`, `Created at` date, `Updated at` timestamp, and data from any of your data table's custom columns. |
| List size | Total number of records in the list. |
| List index | The position of the record in the list. |

---
