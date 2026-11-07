---
url: 'https://docs.workato.com/en/connectors/mssql/delete.md'
description: >-
  The Delete rows action in the SQL Server connector lets you delete one or more
  rows from a table that match a WHERE condition.
---

# SQL Server - Delete actions

## Delete rows

This action lets you delete rows based on certain criteria defined by a `WHERE` condition.

> **DATA DELETION IS PERMANENT**
> 
> Data deletion _can't be undone_, even if the action is run during a test job.

![Delete action](/assets/delete-rows-action.DydxwtRj.png)_Delete rows action_

### Table

First, select a table to delete rows from. This can be done either by selecting a table from the pick list, or toggle the input to text mode and type the full table name.

### WHERE condition

Next, provide a `WHERE` condition to select rows to be deleted. This condition can be as simple as filtering a single record to delete based on `ID`.

```sql
id = 5
```

Alternatively, it can be used to delete multiple rows.

```sql
status = 'closed'
```

Complex `WHERE` conditions with subqueries can also be used. Refer to the [WHERE condition](/en/connectors/mssql/introduction#using-where-conditions) guide for more information.

---
