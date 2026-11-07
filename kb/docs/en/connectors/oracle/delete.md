---
url: 'https://docs.workato.com/en/connectors/oracle/delete.md'
description: >-
  The Delete rows action in the Oracle connector lets you delete rows from a
  table based on a WHERE condition you define.
---

# Oracle - Delete actions

## Delete rows

This action lets you delete rows based on certain criteria defined by a `WHERE` condition.

> **DATA DELETION IS PERMANENT**
> 
> Data deletion _can't be undone_, even if the action is run during a test job.

![Delete action](/assets/delete-rows-action.DEjSJHt0.png)_Delete rows action_

### Table

Select a table from which to delete rows. You can either select a table from the pick list or toggle the input field to text mode and type the full table name.

### WHERE condition

Provide a `WHERE` condition to select rows you plan to delete. This condition can be as simple as filtering a single record to delete based on the record's `ID`.

```sql
CUSTOMER_ID = 123
```

Alternatively, it can be used to delete multiple rows.

```sql
STATUS = 'closed'
```

Complex `WHERE` conditions with subqueries can also be used. Refer to the Oracle [WHERE condition](/en/connectors/oracle/working-with-the-oracle-connector#using-where-conditions) guide for more information.

---
