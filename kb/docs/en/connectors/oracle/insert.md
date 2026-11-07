---
url: 'https://docs.workato.com/en/connectors/oracle/insert.md'
description: >-
  The Insert actions in the Oracle connector let you add a single row or a batch
  of rows to a selected table in your Oracle database.
---

# Oracle - Insert actions

Workato offers both batch and single insert row actions. This allows you the flexibility to choose the action that you require for your recipe and to fulfill your business needs. Check out our [best practices on whether to use batch or single insert actions](/en/connectors/databases/best-practices#batch-versus-single-row-triggers-and-actions) and [when to use insert, update, or update](/en/connectors/databases/best-practices#using-update-insert-and-upsert-actions).

* * *

## Insert row

This action inserts a single row into the selected table.

![Insert row action](/assets/insert_row_action.CZr3xJQP.png)_Insert row action_

> **WARNING**
> 
> Multiple inserts are possible if the step following this action encounters an error and the job is repeated.
> 
> Consider using an [Upsert action](/en/connectors/oracle/upsert) instead, which allows you to de-dupe rows.

### Table/view

Select a table in which to insert a row. You can either select a table from the pick list or toggle the input field to text mode and type the full table name.

### Columns

Map the datapills from your previous triggers or actions into their respective columns. Workato presents the columns in the selected table as input fields here, allowing you to insert datapills.

**Note**: How `date` and `timestamp` values are inserted depends on the connector's [Improved datetime handling](/en/connectors/oracle/introduction#step-3-configure-advanced-settings) settings are configured.

* * *

## Insert batch of rows

This action allows you to insert multiple rows in a single action instead of one row at a time. This provides higher throughput when you are moving a large number of records from one app to Oracle. Depending on the structure of your recipe and volume of data, this action can reduce integration time by a factor of 100.

![Insert batch of rows action](/assets/insert_rows_batch_action.CUmxiB-I.png)_Insert batch of rows action_

### Table

Just like with the single row insert action, you need to select the target table first.

### Rows source list

Unlike the **Insert row** action (where we deal with a single row), we are now dealing with a batch of rows. Hence, the next datapill to input is the _source_ of the batch of rows to insert to the table. This can come from any trigger or action that outputs a list datapill.

![A list datapill from the datatree](/assets/list_datapill_in_output_tree.oCqTmekh.png)_A list datapill from the datatree_

If you do not map a list datapill to this field, this action inserts only one row and behaves like the **Insert row** action.

### Columns

You must map the required fields from the output datatree here to insert rows with data from preceding trigger or actions. Take note that datapills mapped to each column here should be from the source list datapill you used earlier. Datapills that are mapped outside the source list datapill are not iterated.

Refer to the [List management](/en/features/list-management) guide for more information about working with batches.

**Note**: How `date` and `timestamp` values are inserted depends on the connector's [Improved datetime handling](/en/connectors/oracle/introduction#step-3-configure-advanced-settings) settings are configured.

---
