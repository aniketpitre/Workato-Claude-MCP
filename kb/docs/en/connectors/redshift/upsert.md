---
url: 'https://docs.workato.com/en/connectors/redshift/upsert.md'
description: >-
  Use the Redshift upsert actions in Workato to insert or update a single row or
  a batch of rows in a table based on a unique key.
---

# Redshift - Upsert actions

## Upsert row

This action upserts a single row into the selected table.

![Upsert row action](/assets/upsert-row-action.C3lZgkl9.png)_Upsert row action_

### Table

First, select a table to upsert rows in. This can be done either by selecting a table from the pick list, or toggling the input field to text mode and typing the full table name.

### Columns

Columns in the selected table are then presented as input fields here. Map the required fields from the output datatree here to upsert a row with data from preceding trigger or actions.

#### Unique key

Unique key values will be used to determine whether an update or an insert is executed in your Redshift database. If the unique key value of the given set of values exists in your table, that row will be updated with the values provided. In the absence of a row with the unique key value, a new row will be inserted with the values provided.

## Upsert batch of rows

This action allows you to upsert multiple rows in a single action instead of one row at a time. This provides higher throughput when you are moving a large number of records from one app to Redshift. Depending on the structure of your recipe and volume of data, this action can reduce integration time by a factor of 100.

![Upsert batch of rows action](/assets/upsert-rows-batch-action.Dp_hTAF0.png)_Upsert batch of rows action_

### Table

Just like with the single row upsert action, you need to select the target table first.

### Rows source list

Unlike the **Upsert row** action (where we deal with a single row), we are now dealing with a batch of rows. Hence, the next datapill to input is the _source_ of the batch of rows to upsert to the table. This can come from any trigger or action that outputs a list datapill.

![A list datapill from the datatree](/assets/list_datapill_in_output_tree.Dxf02PMk.png)_A list datapill from the datatree_

If you do not map a list datapill to this field, this action will upsert only 1 row and will behave like the **Upsert row** action.

### Columns

Finally, you will need to map the required fields from the output datatree here to upsert rows with data from preceding trigger or actions. Take note that datapills mapped to each column here should be from the source list datapill you used earlier. Datapills that are mapped outside the source list datapill will not be iterated (mappings like this will become a constant value for all rows).

Similar to the **Upsert row** action, primary key values provided will be used to determine an update or create for each row.

#### Unique key

Unique key values will be used to determine whether an update or an insert is executed in your Redshift database. If the unique key value of the given set of values exists in your table, that row will be updated with the values provided. In the absence of a row with the unique key value, a new row will be inserted with the values provided.

Refer to the [List management](/en/features/list-management) guide for more information about working with batches.

---
