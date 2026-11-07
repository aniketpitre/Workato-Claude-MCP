---
url: 'https://docs.workato.com/en/connectors/mysql/select.md'
description: >-
  The Select rows action in the MySQL connector lets you return rows from a
  table that match a WHERE condition, including complex conditions with
  subqueries.
---

# MySQL - Select actions

## Select rows

This action lets you select rows based on certain criteria defined by a `WHERE` condition. Rows from the selected table that match the `WHERE` condition will be returned as the output of this action.

![Select rows action](/assets/select-rows-action.CjJZhk_M.png)_Select rows action_

### Table

First, select a table to work with. This can be done either by selecting a table from the pick list, or toggle the input to text mode and type the full table name.

### WHERE condition

Next, provide a `WHERE` condition to filter rows. This condition can be as simple as filtering a single record by it's `ID`.

```sql
id = 123
```

Alternatively, it can be used to select multiple rows based on values in one or more columns.

```sql
role = 'admin' and title = 'Procurement Analyst'
```

Complex `WHERE` conditions with subqueries can also be used. Refer to the [WHERE condition](/en/connectors/mysql#where-condition) guide for more information.

### Parameters

Used in conjunction with your `WHERE` condition to prevent SQL injection. After declaring named bind variables in your `WHERE` input, assign values to these variables using this input field. [Learn more](/en/connectors/mysql#using-parameters)

### Order by

Rows returned from this action can be ordered based on the **Order by** input field. This field is used to change the default ordering of rows from your MySQL database.

You can also define the direction of order for each column you wish to order by. The following order by statement will order rows by `priority` in ascending order followed by `created_date` in descending order (latest first).

```sql
id asc, created_date desc
```

### Limit

This input field determines the maximum number of rows to return. The default quota is 100 and capped at a maximum of 50000 rows for a single **Select rows** action.

### Offset

This input field gives you the option to fetch only a page of results from the entire results set. For example, to skip the first 100 rows of the selected results set, input `100` to this field. The default is `0`.

---
