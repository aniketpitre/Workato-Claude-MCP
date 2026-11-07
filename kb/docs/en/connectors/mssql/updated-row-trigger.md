---
url: 'https://docs.workato.com/en/connectors/mssql/updated-row-trigger.md'
description: >-
  The New/updated row trigger in the SQL Server connector processes rows
  inserted or updated in a table or view, with optional WHERE condition
  filtering.
---

# SQL Server - New/updated row triggers

## New/updated row

This trigger processes rows that are inserted or updated in the selected table or view. It processes each row as a separate job. When you start the trigger, it processes existing rows in the table or view. You can use a [WHERE condition](#where-condition) to filter the rows. Subsequently, it checks for new or updated rows once every poll interval. For example, `WHERE date > '2024-12-31'` filters only rows where the `date` column contains a value after December 31, 2024.

![New/updated row trigger](/assets/new-updated-row-trigger.DPU96fv2.png)_New/updated row trigger_

| Input field | Description |
| --- | --- |
| [Table](#table) | Select a table/view to process rows from. |
| [Unique key](#unique-key) | Select a unique key column to uniquely identify rows. This list of columns are generated from the selected table/view. |
| [Sort column](#sort-column) | Select a column to identify updated rows. |
| [WHERE condition](#where-condition) | Provide an optional `WHERE` condition to filter rows. |

## New/updated batch of rows

This trigger processes rows that are inserted or updated in the selected table or view and processes them in batches. When you start the trigger, it processes all existing rows in the table or view. Subsequently, it checks for new or updated rows once every poll interval. You can use a [WHERE condition](#where-condition) to filter which rows to process. For example, `WHERE date > '2024-12-31'` filters for rows where the `date` column contains a value after December 31, 2024.

![New/updated batch of rows trigger](/assets/new-updated-batch-of-rows-trigger.B5z0Fot7.png)_New/updated batch of rows trigger_

| Input field | Description |
| --- | --- |
| [Table](#table) | First, select a table/view to process rows from. |
| [Unique key](#unique-key) | Select a unique key column to uniquely identify rows. This list of columns are generated from the selected table/view. |
| [Sort column](#sort-column) | Select a column to identify updated rows. |
| [Batch size](#batch-size) | Configure the batch size to process in each individual job for this recipe. |
| [WHERE condition](#where-condition) | Provide an optional `WHERE` condition to filter rows. |

## New/updated batch of rows via custom SQL

This trigger processes rows that match your custom SQL when inserted or updated in the selected table or view. It processes rows in batches. When you start the trigger, it processes all existing rows in the table or view. Subsequently, it checks for new or updated rows once every poll interval. You can use a [WHERE condition](#where-condition) to filter which rows to process. For example, `WHERE date > '2024-12-31'` filters for rows where the `date` column contains a value after December 31, 2024.

## Supported versions

This trigger is only supported for SQL Server 2012 or newer. It uses a default stored procedure `sp_describe_first_result_set` that is only available from SQL Server 2012 onwards.

![New/updated batch of rows via custom SQL trigger](/assets/new-updated-batch-of-rows-via-custom-sql-trigger.XZwHTpJQ.png)_New/updated batch of rows trigger via custom SQL_

**This trigger is not supported for SQL Server 2008 version or earlier.**

| Input field | Description |
| --- | --- |
| [SQL](#sql) | Custom SQL query to be executed at each poll interval to pick up new rows. |
| [Unique key](#unique-key) | Select a unique key column to uniquely identify rows. This list of columns are generated from custom SQL provided. |
| [Sort column](#sort-column) | Select a column to identify updated rows. |
| [Batch size](#batch-size) | Configure the batch size to process in each individual job for this recipe. This defaults to 100. |

## Input

### Table

Select the table/view to process rows from. This can be done either by selecting a table from the pick list, or toggling the input field to text mode and typing the full table name.

### Unique key

Values from this selected column is used to deduplicate rows in the selected table.

As such, the values in the selected column should not be repeated in your table. Typically, this column is the primary key of the table (for example, `ID`). It should be incremental and sortable. This column can also be indexed for better performance.

Only columns that have **PRIMARY KEY** or **UNIQUE** constraints can be used. Run this SQL query to find out which columns fulfill this requirement.

```sql
SELECT col.column_name
FROM INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE col
JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS c ON c.constraint_name = col.constraint_name
WHERE
  c.constraint_type IN ('PRIMARY KEY','UNIQUE') AND
  c.table_schema='schema_name' AND
  c.table_name='table_name'
```

If no column can be found, check out our [best practices](/en/connectors/databases/best-practices#designing-tables-for-workato-use) to find out how to make one.

### Sort column

Sort column is a column that is updated whenever a row in the table is updated. Typically, this is a timestamp column.

When a row is updated, the Unique key value remains the same. However, it should have it's timestamp updated to reflect the last updated time. Following this logic, Workato keeps track of values in this column together with values in the selected [**Unique key**](#unique-key) column. When a change in the **Sort column** value is observed, an updated row event will be recorded and processed by the trigger.

Only **datetime2** and **datetime** column types can be used. Run this SQL query to find out which columns fulfill this requirement.

```sql
SELECT column_name
FROM INFORMATION_SCHEMA.COLUMNS
WHERE
  table_schema='table_schema' AND
  table_name='table_name' AND
  data_type in('datetime', 'datetime2')
```

If no column can be found, check out our [best practices](/en/connectors/databases/best-practices#designing-tables-for-workato-use) to find out how to make one.

### Batch size

Batch size of rows to return in each job. This can be any number between **1** and the maximum batch size. Maximum batch size is **100** and default is **100**.

In any given poll, if there are less rows than the configured batch size, this trigger will deliver all rows as a smaller batch.

### WHERE condition

This condition is used to filter rows based on one or more column values.

```sql
status = 'closed' and priority > 3
```

Leave blank to process all rows from the selected table.

Complex `WHERE` conditions with subqueries can also be used. Refer to the [WHERE condition](/en/connectors/mssql/introduction#using-where-conditions) guide for more information.

### SQL

Provide the SQL to be executed to select rows. The SQL here will be used to generate the output datatree. To do this, the SQL will be executed once when you provide it. You can map datapills here to execute dynamically changing SQL statements. Remember to wrap datapills in quotes (`''`).

Avoid using limit clauses like `TOP` in your SQL. This is because the limit to the number of rows returned in the query is based on the value defined in the **Batch size** input field. Adding your own limit clause will cause the action to fail.

---
