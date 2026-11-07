---
url: 'https://docs.workato.com/en/connectors/mysql/delete.md'
description: >-
  The Delete rows action in the MySQL connector lets you delete one or more rows
  from a selected table based on a WHERE condition.
---

# MySQL - Delete actions

## Delete rows

This action lets you delete rows based on certain criteria defined by a `WHERE` condition.

> **DATA DELETION IS PERMANENT**
> 
> Data deletion _can't be undone_, even if the action is run during a test job.

![Delete action](/assets/delete-rows-action.C-U1gpIY.png)_Delete rows action_

### Table

First, select a table to delete rows from. This can be done either by selecting a table from the pick list, or toggle the input to text mode and type the full table name.

### WHERE condition

Next, provide a `WHERE` condition to select rows to be deleted. This condition can be as simple as filtering a single record to delete based on `ID`.

```sql
id = 123
```

Alternatively, it can be used to delete multiple rows.

```sql
role = 'admin'
```

Complex `WHERE` conditions with subqueries can also be used. Refer to the [WHERE condition](/en/connectors/mysql#where-condition) guide for more information.

---
