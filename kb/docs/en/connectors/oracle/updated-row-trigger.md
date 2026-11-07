---
url: 'https://docs.workato.com/en/connectors/oracle/updated-row-trigger.md'
description: >-
  The New/updated row trigger in the Oracle connector picks up rows inserted or
  updated in a selected table or view, processing each as a separate job.
---

# Oracle - New/updated row triggers

## New/updated row

This trigger picks up rows that are inserted/updated in the selected table or view. Each row is processed as a separate job. It checks for new/updated rows once every poll interval.

> **TRIGGER USAGE**
> 
> This trigger fetches all matching rows from the table or view you select, including historical records. We recommend that you add a **WHERE condition** to limit the number of rows the trigger processes and reduce load on large tables.

![New/updated row trigger](/assets/new-updated-row-trigger.CgbxayGj.png)_New/updated row trigger_

| Input field | Description |
| --- | --- |
| [Table](#table) | First, select a table/view to process rows from. |
| [Unique key](#unique-key) | Next, select a unique key column to uniquely identify rows. This list of columns are generated from the selected table/view. |
| [Sort column](#sort-column) | Now, select a column to identify updated rows. |
| [WHERE condition](#where-condition) | Finally, provide an optional `WHERE` condition to filter rows. |

## New/updated batch of rows

This trigger picks up rows that are inserted/updated in the selected table or view. These rows are processed as a batch of rows for each job. This batch size can be configured in the trigger input. It checks for new/updated rows once every poll interval.

> **TRIGGER USAGE**
> 
> This trigger fetches all matching rows from the table or view you select, including historical records. We recommend that you add a **WHERE condition** to limit the number of rows the trigger processes and reduce load on large tables.

![New/updated batch of rows trigger](/assets/new-updated-batch-of-rows-trigger.DKog2RUh.png)_New/updated batch of rows trigger_

| Input field | Description |
| --- | --- |
| [Table](#table) | Select the table/view from which you plan to process rows. |
| [Unique key](#unique-key) | Select a unique key column to uniquely identify rows. This list of columns is generated from the selected table/view. |
| [Sort column](#sort-column) | Select a column from which you plan to identify updated rows. |
| [Batch size](#batch-size) | Configure the batch size to process in each individual job for this recipe. |
| [WHERE condition](#where-condition) | Provide an optional `WHERE` condition to filter rows. |

## Input

### Table

The Table field is where you select the table/view from which you plan to process rows. You can either select a table from the pick list or toggle the input field to text mode and type the full table name.

### Unique key

Values from this selected column is used to deduplicate rows in the selected table.

The values in the selected column should not be repeated in your table. Typically, this column is the primary key of the table (for example, `ID`). It should be incremental and sortable. This column can also be indexed for better performance.

Only columns that have **primary key ('P')** or **unique ('U')** constraints can be used. Run the following SQL query to find out which columns fulfill this requirement.

```sql
SELECT c.column_name
FROM all_indexes i, all_ind_columns c
WHERE
  i.table_owner = 'TABLE_OWNER' AND
  i.table_name = 'TABLE_NAME' AND
  i.uniqueness = 'UNIQUE' AND
  i.table_name = c.table_name AND
  i.index_name = c.index_name
UNION
SELECT cc.column_name
FROM all_constraints con, all_cons_columns cc
WHERE
  con.table_owner = 'TABLE_OWNER' AND
  con.table_name = 'TABLE_NAME' AND
  con.constraint_type in ('U', 'P') AND
  con.table_name = cc.table_name AND
  con.constraint_name = cc.constraint_name
```

If no column can be found, check out our [best practices](/en/connectors/databases/best-practices#designing-tables-for-workato-use) to find out how to make one.

### Sort column

Sort column is a column that is updated whenever a row in the table is updated. Typically, this is a timestamp column.

When a row is updated, the Unique key value remains the same. However, it should have it's timestamp updated to reflect the last updated time. Following this logic, Workato keeps track of values in this column together with values in the selected [**Unique key**](#unique-key) column. When a change in the **Sort column** value is observed, an updated row event will be recorded and processed by the trigger.

Only **date**, **timestamp**, **timestamp with time zone** and **timestamp with local time zone** column types can be used. Run this SQL query to find out which columns fulfill this requirement.

```sql
SELECT column_name
FROM all_tab_columns
WHERE
  owner = 'WORKATO' AND
  table_name = 'ORACLE_STRING' AND
  (data_type LIKE 'TIMESTAMP%' OR data_type LIKE 'DATE%')
```

If no column can be found, check out our [best practices](/en/connectors/databases/best-practices#designing-tables-for-workato-use) to find out how to make one.

### Batch size

This field determines the Batch size of rows to return in each job. This can be any number between **1** and the maximum batch size. Maximum batch size is **1000** and the default is **100**.

For any poll, if there are less rows than the configured batch size, this trigger delivers all rows as a smaller batch.

### WHERE condition

The `WHERE` condition is used to filter rows based on one or more column values. For example:

```sql
status = 'closed' and priority > 3
```

Leave the `WHERE` field blank to process all rows from the selected table.

Complex `WHERE` conditions with subqueries can also be used. Refer to the [WHERE condition](/en/connectors/oracle/working-with-the-oracle-connector#using-where-conditions) guide for more information.

---
