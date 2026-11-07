---
url: 'https://docs.workato.com/en/connectors/jdbc/new-row-trigger.md'
description: >-
  The JDBC new row triggers pick up rows inserted in a selected table or view,
  processing them individually or in batches each poll interval.
---

# JDBC - New row triggers

## New row trigger

This trigger picks up rows that are inserted in the selected table or view. Each row is processed as an individual job. It checks for new rows once every poll interval.

![New row trigger](/assets/new-row-trigger.CH-z84-x.png)_New row trigger_

| Input field | Description |
| --- | --- |
| [Table](#table) | Select a table/view to process rows from. |
| [Unique key](#unique-key) | Select a unique key column to uniquely identify rows. This list of columns are generated from the selected table/view. |
| [WHERE condition](#where-condition) | Provide an optional `WHERE` condition to filter rows. |

## New batch of rows trigger

This trigger picks up rows that are inserted in the selected table or view. These rows are processed in batches. Each batch of rows is processed as an individual job. This batch size can be configured in the trigger input. It checks for new rows once every poll interval.

![New batch of rows trigger](/assets/new-batch-of-rows-trigger.Dm9L8uJ0.png)_New batch of rows trigger_

| Input field | Description |
| --- | --- |
| [Table](#table) | Select a table/view to process rows from. |
| [Unique key](#unique-key) | Select a unique key column to uniquely identify rows. This list of columns are generated from the selected table/view. |
| [Batch size](#batch-size) | Configure the batch size to process in each individual job for this recipe. Maximum batch size is 50,000 and default is 100. |
| [WHERE condition](#where-condition) | Provide an optional `WHERE` condition to filter rows. |

## New batch of rows via custom SQL trigger

**This trigger is not supported for SQL Server 2008 version or earlier.**

This trigger picks up rows when any rows matching the custom SQL are inserted. These rows are processed as a batch of rows for each job. This batch size can be configured in the trigger input. It checks for new rows once every poll interval.

This trigger is especially useful if you wish to pick up data selected from multiple tables using a `JOIN` statement. In the example below, the trigger picks up new rows from a custom SQL that joins information from the `Opportunity` and `users` table.

![New batch of rows via custom SQL trigger](/assets/new-batch-of-rows-via-custom-sql-trigger.BGlmLIOE.png)_New batch of rows trigger via custom SQL_

| Input field | Description |
| --- | --- |
| [SQL](#sql) | Custom SQL query to be executed at each poll interval to pick up new rows. |
| [Unique key](#unique-key) | Select a unique key column to uniquely identify rows. This list of columns are generated from custom SQL provided. |
| [Batch size](#batch-size) | Configure the batch size to process in each individual job for this recipe. This defaults to 100. |

## Input

### Table

Select the table/view to process rows from. This can be done either by selecting a table from the pick list, or toggling the input field to text mode and typing the full table name. Case sensitivity of table name depends on the database you are connected to.

### Unique key

Values from this selected column is used to deduplicate rows in the selected table, making sure that the same row is not processed twice in the same recipe.

As such, the values in the selected column should not be repeated in your table. Typically, this column is the primary key of the table (for example, `ID`). It should be incremental and sortable. This column can also be indexed for better performance.

### Batch size

Batch size of rows to return in each job. This can be any number between **1** and the maximum batch size. Maximum batch size is 50,000 and default is 100.

In any given poll, if there are less rows than the configured batch size, this trigger will deliver all rows as a smaller batch.

### WHERE condition

This condition is used to filter rows based on one or more column values.

```sql
STATUS = 'closed' and PRIORITY > 3
```

Leave blank to process all rows from the selected table.

Complex `WHERE` conditions with subqueries can also be used. Refer to the [WHERE condition](/en/connectors/jdbc#where-condition) guide for more information.

---
