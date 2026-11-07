---
url: 'https://docs.workato.com/en/connectors/mysql/update.md'
description: >-
  The Update rows action in the MySQL connector lets you update one or more rows
  with a single set of values, using a WHERE condition to select the rows.
---

# MySQL - Update actions

## Update rows

This action updates one or more rows with a single set of values. It uses a `WHERE` condition to select the rows to perform the update.

![Update rows action](/assets/update-row-action.BRzoehS1.png)_Update rows action_

### Table

First, select a table to update. This can be done either by selecting a table from the pick list, or toggling the input field to text mode and typing the full table name.

### WHERE condition

Next, provide a `WHERE` condition to select rows to be updated. This condition can be as simple as filtering a single record to update based on `ID`.

```sql
id = 123
```

Alternatively, it can be used to select and update multiple rows.

```sql
role = 'admin'
```

Take note that all rows matching this criteria will be updated with the same values provided in **Columns** input.

Complex `WHERE` conditions with subqueries can also be used. Refer to the [WHERE condition](/en/connectors/mysql#where-condition) guide for more information.

### Columns

Lastly, map the datapills from your previous triggers or actions into their respective columns. The columns in the selected table are presented as input fields here for you to insert datapills.

---
