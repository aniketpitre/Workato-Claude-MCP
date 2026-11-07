---
url: 'https://docs.workato.com/en/connectors/mssql/bulk-load-from-on-prem-file.md'
description: >-
  The Bulk load from on-prem file action in the SQL Server connector loads data
  from a CSV file on the on-prem agent into a target table.
---

# SQL Server - Bulk load from on-prem file action

This action loads an on-prem CSV data file into a table in SQL Server. The source CSV data file should be accessible by the [On-prem files](/en/connectors/on-prem-files) connector.

> **OPA required**
> 
> This action requires a connection that uses the Workato on-prem agent. Refer to [On-prem connectivity](/en/on-prem) for more information.
> 
> The **Match columns by**, **If a row fails**, and **Columns to identify failed rows** fields require **On-prem agent (OPA) version 34.0 or later**.

## Input

| Input field | Description |
| --- | --- |
| Table name | **Required**. The name of the target table to load the data into. |
| File URL | **Required**. The [on-prem file URL](/en/connectors/on-prem-files/generate-on-prem-file-url) that references a CSV file located in the on-prem agent. The CSV columns must be in the same order as the columns in the target table when **Match columns by** is set to **Column order**. |
| Advanced configuration | Configure advanced settings for the action. Refer to the [Advanced configuration](#advanced-configuration) section for more information. |

> **CHARACTER LIMIT**
> 
> The source CSV file supports up to 100,000,000 characters.

### Advanced configuration

Use the following fields to control how the action matches columns, handles failed rows, and reads and loads the source file:

| Input field | Description |
| --- | --- |
| Match columns by | Select how CSV columns map to table columns. **Column order** fills table columns by position. **Column name (from CSV header)** matches each CSV header to a table column by exact name, and requires **First row number** to be `2` or greater. Defaults to **Column order**. Refer to [Match columns by](#match-columns-by) for more information. |
| If a row fails | Select how the action handles rows that fail to load. Defaults to **Stop and load nothing, fail job**. Refer to [If a row fails](#if-a-row-fails) for more information. |
| Columns to identify failed rows | Select table columns, such as a customer ID, to include in the **Failed rows file** output. Use this to trace each failed row back to its source record. Line numbers are always included. This field appears only when **If a row fails** is set to **Load valid rows, skip the failed rows**. |
| First row number | **Required**. The index of the first row in the file to process. Set this to `2` to skip the header row if your data contains one. Defaults to `1`. |
| Field quote | **Required**. The quote character for fields in the source CSV. Defaults to a double quote. |
| Field terminator | **Required**. The symbol that separates fields in the source CSV. Defaults to a comma. |
| Batch size | Sets the number of rows in each transaction. Rows are gradually inserted across multiple transactions, batch by batch. Advanced users can customize this to control memory usage and optimize loads. Defaults to `10,000`. |
| Last row number | The index of the last row in the file to process, counted from the start of the file. Use this to stop loading before the end of the file. Defaults to `0`, which processes every row through the final row. |
| Fire triggers | Indicate if triggers on the table should be fired upon data insertion. Defaults to **No**. |
| Keep null values | Indicate how to treat empty values in the file. Select **Yes** to insert `NULL` values, or **No** to insert default column values. Defaults to **Yes**. |
| Data file type | Defines the character encoding for the data file. Defaults to **Char**. |
| Allow partial inserts on error? | Select **No** to insert no data when an error occurs, or **Yes** to insert all data up to the errored row. Defaults to **No**. This field appears only on OPA versions earlier than 34.0. |
| Insert in a single batch? | Select **Yes** to insert all rows in a single batch and ignore **Batch size**. Defaults to **No**. This field appears only on OPA versions earlier than 34.0. |

#### Match columns by

**Column order** requires the source CSV file to contain the same columns, in the same order, as the target table. This is the default.

**Column name (from CSV header)** matches each CSV header to a table column by exact, case-sensitive name. Column order in the CSV file doesn't matter. This option requires **First row number** to be `2` or greater. Alias the columns in any query that generates the CSV file so they match the table column names.

- A table column missing from the CSV file is set to `NULL` and listed in the **Unmapped destination columns** output. Columns with a default value receive that default instead when **Keep null values** is set to **No**.
- The batch fails with an error naming the missing column if the column isn't nullable and has no default value.
- A CSV column that doesn't match any table column is ignored and listed in the **Unmapped source columns** output.
- Adding a column to the target table doesn't break recipes that use **Column name (from CSV header)**. The new column is treated as missing from the CSV file.

#### If a row fails

The **If a row fails** field determines which rows are inserted when a row fails to load, and whether the job fails:

| Option | Behavior |
| --- | --- |
| Stop and load nothing, fail job | Cancels the batch if any row fails. The job fails. This is the default. |
| Stop and load nothing, continue job | Cancels the batch if any row fails. The job continues. Use the **Status** output to check the result. |
| Stop at the first bad row, continue job | Inserts every row up to the first failure, then stops. The job continues. |
| Load valid rows, skip the failed rows | Inserts every valid row, then returns every failed row in the **Failed rows file** output. The job continues, and the **Status** output returns **Partially Loaded** when some rows fail. The **Rows failed** output contains the total count of failed rows. |

The **Failed rows file** output has no size limit and includes every failed row, even if every row in the batch fails. Each failed row includes its line number, its error details, and the values of any columns you select in **Columns to identify failed rows**.

The **If a row fails** field doesn't change how the action handles CSV parsing errors, such as a malformed source file.

## Output

| Output field | Description |
| --- | --- |
| Destination table | Name of the table where the rows were inserted. |
| Rows parsed | Number of rows read from the source file. |
| Rows loaded | Number of rows loaded. |
| Status | **Loaded**: all rows loaded successfully. **Load failed**: unsuccessful load, and nothing was loaded. **Partially Loaded**: unsuccessful load, and some rows were loaded. **Timeout**: execution timed out (24-hour timeout). |
| First error line | First row where the error occurred, if any. |
| First error details | Description of the first error, if any. |
| First error character | The index of the character where the error occurred, if any. |
| First error column name | The name of the column for the field where the error occurred, if any. |
| Rows failed | Number of rows that failed to load. Populated when **If a row fails** is set to **Load valid rows, skip the failed rows**. |
| Failed rows file | A CSV file listing every row that failed to load. Populated when **If a row fails** is set to **Load valid rows, skip the failed rows**. Refer to [If a row fails](#if-a-row-fails) for the file contents. |
| Unmapped source columns | CSV columns that don't match a column in the target table. These columns aren't loaded. Populated when **Match columns by** is set to **Column name (from CSV header)**. |
| Unmapped destination columns | Table columns missing from the CSV file. Refer to [Match columns by](#match-columns-by) for the values these columns receive. Populated when **Match columns by** is set to **Column name (from CSV header)**. |

---
