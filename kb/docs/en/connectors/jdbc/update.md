---
url: 'https://docs.workato.com/en/connectors/jdbc/update.md'
description: >-
  The Update rows action in the JDBC connector lets you update one or more rows
  that match a WHERE condition with a single set of values.
---

# JDBC - Update rows action

This action updates one or more rows with a single set of values. It uses a `WHERE` condition to select the rows to perform the update.

![Update rows action](/assets/update-row-action.CLRIYd1P.png)_Update rows action_

## Table

First, select a table to update. This can be done either by selecting a table from the pick list, or toggling the input field to text mode and typing the full table name. Case sensitivity of table name depends on the database you are connected to.

## WHERE condition

Next, provide a `WHERE` condition to select rows to be updated. This condition can be as simple as filtering a single record to update based on `ID`.

```sql
id = 123
```

Alternatively, it can be used to select and update multiple rows.

```sql
status = 'closed'
```

Take note that all rows matching this criteria will be updated with the same values provided in **Columns** input.

Complex `WHERE` conditions with subqueries can also be used. Refer to the [WHERE condition](/en/connectors/jdbc#where-condition) guide for more information.

## Columns

Lastly, map the datapills from your previous triggers or actions into their respective columns. The columns in the selected table are presented as input fields here for you to insert datapills.

---
