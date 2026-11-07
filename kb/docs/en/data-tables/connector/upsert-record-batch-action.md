---
url: >-
  https://docs.workato.com/en/data-tables/connector/upsert-record-batch-action.md
description: >-
  The upsert records batch action updates or creates multiple records in a data
  table in a single batch operation.
---

# Upsert records action (batch)

The **Upsert records** batch action searches a data table for entries matching the primary key you specify. If a matching record is found, the action updates it with the values you specify. If a matching record isn't found, the action creates a new record with the values you specify. This action supports a maximum of 1000 records per batch.

## Input

| Input field | Description |
| --- | --- |
| Data table | Select the data table in which you plan to upsert records. Click the link in this field's description to view the selected data table in the [Data tables interface](/en/data-tables/data-table-interface). |
| Primary key | Select the column to use as a primary key. The action uses this column to detect whether a record already exists for a given set of fields. If no record matches, the action creates a new record with the values you specify in the **Records** input. |
| Choose the desired output format | Optional. Specify how to map the upserted records data to the table fields. Refer to the [Output formats](/en/data-tables/data-table-connector#output-formats) section for more information. |
| Records | Provide the list of records to upsert. Each record must include values that correspond to the columns of the selected data table. |

> **ADDITIONAL INPUT FIELDS**
> 
> The **Records** section contains an input field for each column of the selected data table. Use these input fields to specify the values to upsert each record with. If you leave a field empty, Workato doesn't update the corresponding column.
> 
> These input fields are subject to the same restrictions as their corresponding columns, for example:
> 
> - If a column is required, its corresponding field is also required.
> - The value you provide must match the corresponding column's data type. For instance, text columns only accept alphanumeric characters. Refer to [Column types](/en/data-tables/user-interface/column-types) for detailed information on the accepted values for each data type.

## Output

| Output field | Description |
| --- | --- |
| Records | Contains information about each modified record, such as its `Record ID`, `Created at` date, `Updated at` timestamp, and data from any of the data table's custom columns. |
