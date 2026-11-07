---
url: 'https://docs.workato.com/en/connectors/mysql/insert.md'
description: >-
  Use the MySQL Insert row and Insert batch of rows actions to add single or
  multiple rows to a selected table for higher throughput.
---

# MySQL - Insert actions

## Insert row

This action inserts a single row into the selected table.

![Insert row action](/assets/insert-row-action.B7CUk0Cb.png)_Insert row action_

### Table

First, select a table to insert a row into. This can be done either by selecting a table from the pick list, or toggling the input field to text mode and typing the full table name.

### Columns

Next, map the datapills from your previous triggers or actions into their respective columns. The columns in the selected table are presented as input fields here for you to insert datapills.

## Insert batch of rows

This action allows you to insert multiple rows in a single action instead of one row at a time. This provides higher throughput when you are moving a large number of records from one app to MySQL. Depending on the structure of your recipe and volume of data, this action can reduce integration time by a factor of 100.

![Insert batch of rows action](/assets/insert-rows-batch-action.Ffw5qMRc.png)_Insert batch of rows action_

### Table

Just like with the single row insert action, you need to select the target table first.

### Rows source list

Unlike the **Insert row** action (where we deal with a single row), we are now dealing with a batch of rows. Hence, the next datapill to input is the _source_ of the batch of rows to insert to the table. This can come from any trigger or action that outputs a list datapill.

![A list datapill from the datatree](/assets/list_datapill_in_output_tree.Ba6W_F74.png)_A list datapill from the datatree_

If you do not map a list datapill to this field, this action will insert only 1 row and will behave like the **Insert row** action.

### Columns

Finally, you will need to map the required fields from the output datatree here to insert rows with data from preceding trigger or actions. Take note that datapills mapped to each column here should be from the source list datapill you used earlier. Datapills that are mapped outside the source list datapill will not be iterated.

Refer to the [List management](/en/features/list-management) guide for more information about working with batches.

---
