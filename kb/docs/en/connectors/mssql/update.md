---
url: 'https://docs.workato.com/en/connectors/mssql/update.md'
description: >-
  Use the SQL Server update actions in Workato to update one or more rows with a
  set of values selected by a WHERE condition, in single or batch mode.
---

# SQL Server - Update actions

Workato offers both batch and single update row actions. This allows you the flexibility to choose the action that you require for your recipe and to fulfill your business needs. Check out our [best practices on whether to use batch or single insert actions](/en/connectors/databases/best-practices#batch-versus-single-row-triggers-and-actions) and [when to use insert, update, or update](/en/connectors/databases/best-practices#using-update-insert-and-upsert-actions).

## Update rows

This action updates one or more rows with a single set of values. It uses a `WHERE` condition to select the rows to perform the update.

![Update rows action](/assets/update-row-action.CDfoCasj.png)_Update rows action_

### Table

First, select a table to update. This can be done either by selecting a table from the pick list, or toggling the input field to text mode and typing the full table name.

### WHERE condition

Next, provide a `WHERE` condition to select rows to be updated. This condition can be as simple as filtering a single record to update based on `ID`.

```sql
ID = 123
```

Alternatively, it can be used to select and update multiple rows.

```sql
status = 'closed'
```

Take note that all rows matching this criteria will be updated with the same values provided in **Columns** input.

Complex `WHERE` conditions with subqueries can also be used. Refer to the [WHERE condition](/en/connectors/mssql/introduction#using-where-conditions) guide for more information.

### Columns

Lastly, map the datapills from your previous triggers or actions into their respective columns. The columns in the selected table are presented as input fields here for you to insert datapills.

## Update batch of rows

This action allows you to update multiple rows in a single action instead of one row at a time. This provides higher throughput when you are moving a large number of records from one app to SQL Server. Depending on the structure of your recipe and volume of data, this action can reduce integration time by a factor of 100.

![Update batch of rows action](/assets/update-rows-batch-action.DSwCQP5F.png)_Update batch of rows action_

### Table

Just like with the single row update action, you need to select the target table first.

### Rows source list

Unlike the **Update row** action (where we deal with a single row), we are now dealing with a batch of rows. Hence, the next datapill to input is the _source_ of the batch of rows to update in the table. This can come from any trigger or action that outputs a list datapill.

![A list datapill from the datatree](/assets/list_datapill_in_output_tree.BibnCSke.png)_A list datapill from the datatree_

If you do not map a list datapill to this field, this action will update only 1 row and will behave like the **Update row** action.

### Columns

Finally, you will need to map the required fields from the output datatree here to update rows with data from preceding trigger or actions. Take note that datapills mapped to each column here should be from the source list datapill you used earlier. Datapills that are mapped outside the source list datapill will not be iterated.

Refer to the [List management](/en/features/list-management) guide for more information about working with batches.

---
