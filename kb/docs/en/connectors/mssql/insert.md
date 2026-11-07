---
url: 'https://docs.workato.com/en/connectors/mssql/insert.md'
description: >-
  Use the SQL Server insert actions in Workato to add a single row or a batch of
  rows to a selected table for higher-throughput data loads.
---

# SQL Server - Insert actions

Workato offers both batch and single insert row actions. This allows you the flexibility to choose the action that you require for your recipe and to fulfill your business needs. Check out our [best practices on whether to use batch or single insert actions](/en/connectors/databases/best-practices#batch-versus-single-row-triggers-and-actions) and [when to use insert, update, or update](/en/connectors/databases/best-practices#using-update-insert-and-upsert-actions).

> **USE UPSERT TO AVOID DUPLICATION**
> 
> If an error occurs in a step following an **Insert row** action during a job run, repeating the job will cause the insert to happen again. To avoid inserting duplicate rows into your database tables, consider using [upserts](/en/connectors/mssql/upsert), which deduplicates records based on a key.

## Insert row

This action inserts a single row into the selected table.

![Insert row action](/assets/insert-row-action.DYRv9pDk.png)_Insert row action_

### Table/view

First, select a table to insert a row into. This can be done either by selecting a table from the pick list, or toggling the input field to text mode and typing the full table name.

### Columns

Next, enter data manually into the input fields or map the datapills from your previous triggers or actions into their respective columns. The input fields generated here are based off columns in your table.

## Insert batch of rows

This action allows you to insert multiple rows in a single action instead of one row at a time. This provides higher throughput when you are moving a large number of records from one app to SQL Server. Depending on the structure of your recipe and volume of data, this action can reduce integration time by a factor of 100.

![Insert batch of rows action](/assets/insert-rows-batch-action.gG7Dm9p0.png)_Insert batch of rows action_

### Table

Just like with the single row insert action, you need to select the target table first.

### Rows source list

Unlike the **Insert row** action (where we deal with a single row), we are now dealing with a batch of rows. Hence, the next datapill to input is the _source_ of the batch of rows to insert to the table. This can come from any trigger or action that outputs a list datapill.

![A list datapill from the datatree](/assets/list_datapill_in_output_tree.BibnCSke.png)_A list datapill from the datatree_

If you do not map a list datapill to this field, this action will insert only 1 row and will behave like the **Insert row** action.

### Columns

Finally, you will need to map the required fields from the output datatree here to insert rows with data from preceding trigger or actions. Take note that datapills mapped to each column here should be from the source list datapill you used earlier. Datapills that are mapped outside the source list datapill will not be iterated.

Refer to the [List management](/en/features/list-management) guide for more information about working with batches.

### Additional Notes

Ensure that the data you insert into the database matches the specified data types defined in the schema. Inserting data of the correct type is crucial for data integrity and system functionality. When there is a mismatch, fallback behavior for batch insert would be the conversion of the non-numeric value to a float value of `0.0`.

---
