---
url: 'https://docs.workato.com/en/connectors/oracle/select.md'
description: >-
  The Select actions in the Oracle connector let you retrieve rows from a table
  or view that match a WHERE condition you define.
---

# Oracle - Select actions

## Select rows

This action lets you select rows based on certain criteria defined by a `WHERE` condition. Rows from the selected table that match the `WHERE` condition are returned as the output of this action.

![Select rows action](/assets/select-rows-action.BHZgyo0T.png)_Select rows action_

### Table/Views

Select the table/view you plan to use. This can be done either by selecting a table or view from the pick list, or toggling the input to text mode and typing the full table name.

### WHERE condition

Provide a `WHERE` condition to filter rows. This condition can be as simple as filtering a single record by its `ID`.

```sql
CUSTOMER_ID = 123
```

Alternatively, it can be used to select multiple rows based on values in one or more columns.

```sql
CUSTOMER_EMAIL = 'eeshan@workato.com' AND PRIORITY = 1
```

Complex `WHERE` conditions with subqueries can also be used. Refer to the [WHERE condition](/en/connectors/oracle/working-with-the-oracle-connector#using-where-conditions) guide for more information.

### Parameters

Used in conjunction with your `WHERE` condition to prevent SQL injection. After declaring named bind variables in your `WHERE` input, assign values to these variables using this input field. [Learn more](/en/connectors/oracle/working-with-the-oracle-connector#using-parameters)

### Order by

Rows returned from this action can be ordered based on the **Order by** input field. This field is used to change the default ordering of rows from your Oracle database.

You can also define the direction of order for each column you wish to order by. The following order by statement orders rows by `priority` in ascending order followed by `created_date` in descending order (latest first).

```sql
CUSTOMER_ID DESC
```

### Limit

This input field determines the maximum number of rows to return. The default quota is 100 and the maximum is 50,000 rows for a single **Select rows** action.

### Offset

This input field gives you the option to fetch only a page of results from the entire results set. For example, to skip the first 100 rows of the selected results set, input `100` to this field. The default is `0`.

## Select rows using custom SQL

This action lets you select rows based on a custom SQL query. Rows that are returned from the query are returned as the output of this action.

![Select rows using custom SQL action](/assets/custom-sql-action.DQgo-rJO.png)_Select rows using custom SQL action_

> **50,000 RECORD QUOTA**
> 
> Starting February 8, 2026, the **Select rows using custom SQL** action returns a maximum of 50,000 records for all **new recipes and existing recipes that don't currently exceed this quota**. Starting March 15, 2026, this quota extends to **all recipes** using this action, including existing recipes that currently exceed the quota.
> 
> Recipes configured to retrieve more than 50,000 records will be truncated to this quota.
> 
> This change improves platform reliability and performance while preventing large queries from overloading database connections or impacting upstream systems.

### SQL

Provide the SQL query to be executed to select rows. This query is used to generate the output datatree. To do this, the SQL executes once when you provide it. You can map datapills here to execute dynamically changing SQL statements. Remember to wrap datapills in quotes (`''`). **Do not add a `;` at the end of your SQL query as this causes the action to fail.**

Avoid using limit clauses like `ROWNUM` in your SQL. This is because the limit to the number of rows returned in the query is based on the value defined in the [**Limit** input field](#limit). Adding your own limit clause causes the action to fail.

### Limit

This input field determines the maximum number of rows to return. The default quota is 100 and the maximum is 50,000 rows for a single **Select rows using custom SQL** action.

If this field is left blank, `ROWNUM <= 100` is used.

---
