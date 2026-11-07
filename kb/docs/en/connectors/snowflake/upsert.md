---
url: 'https://docs.workato.com/en/connectors/snowflake/upsert.md'
description: >-
  The Upsert action in the Snowflake connector lets you insert or update single
  rows or batches of rows in a table using primary key values.
---

# Snowflake - Upsert action

Workato offers both batch and single upsert row actions. This allows you the flexibility to choose the action that you require for your recipe and to fulfill your business needs.

## Upsert batch of rows

This action allows you to upsert multiple rows in a single action instead of one row at a time. This provides higher throughput when you are moving a large number of records from one app to Snowflake. Depending on the structure of your recipe and volume of data, this action can reduce integration time by a factor of 100.

> **TIMEOUT ERROR**
> 
> The **Upsert rows** batch action may time out with a `Timed out reading data from server` or `Bad Gateway: context canceled` error.
> 
> This occurs when the connected Snowflake warehouse is overloaded. Increase the warehouse size to prevent timeouts.

![Upsert batch of rows action](/assets/upsert-rows-batch-action.DkSf7iTk.png)_Upsert batch of rows action_

### Table

Just like with the single row upsert action, you need to select the target table first.

### Rows source list

Unlike the **Upsert row** action (where we deal with a single row), we are now dealing with a batch of rows. Hence, the next datapill to input is the _source_ of the batch of rows to upsert to the table. This can come from any trigger or action that outputs a list datapill.

If you do not map a list datapill to this field, this action will upsert only 1 row and will behave like the **Upsert row** action.

### Columns

Finally, you will need to map the required fields from the output datatree here to upsert rows with data from preceding trigger or actions. Take note that datapills mapped to each column here should be from the source list datapill you used earlier. Datapills that are mapped outside the source list datapill will not be iterated (mappings like this will become a constant value for all rows).

Similar to the **Upsert row** action, primary key values provided will be used to determine an update or create for each row.

Refer to the [List management](/en/features/list-management) guide for more information about working with batches.

## Next steps

Learn more about the other triggers and actions Workato has to offer for Snowflake

- [New row trigger](/en/connectors/snowflake/new-row-trigger)
- [New/updated row trigger](/en/connectors/snowflake/updated-row-trigger)
- [Select actions](/en/connectors/snowflake/select)
- [Insert actions](/en/connectors/snowflake/insert)
- [Update actions](/en/connectors/snowflake/update)
- [Delete actions](/en/connectors/snowflake/delete)
- [Run custom SQL action](/en/connectors/snowflake/run_sql)

Or get busy building your recipes now! Check out our

- [Use cases](/en/connectors/database-common-use-cases)

---
