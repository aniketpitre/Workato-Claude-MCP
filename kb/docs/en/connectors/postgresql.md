---
url: 'https://docs.workato.com/en/connectors/postgresql.md'
description: >-
  The PostgreSQL connector lets you automate database workflows: insert, select,
  update, upsert, and delete rows, and trigger on new or updated rows.
---

# PostgreSQL

[PostgreSQL](https://www.postgresql.org/) is an open-source object-relational database management system hosted either in the cloud or on-premise.

## Supported editions

All releases of PostgreSQL are supported.

## How to connect to PostgreSQL on Workato

The PostgreSQL connector uses basic authentication to authenticate with PostgreSQL. ![Configured PostgreSQL connection](/assets/connection.rFBZ5ny2.png)

| Field | Description |
| --- | --- |
| Connection name | Give this PostgreSQL connection a unique name that identifies which PostgreSQL instance it is connected to. |
| On-prem secure agent | Choose an on-prem agent if your database is running in a network that does not allow direct connection. Before attempting to connect, make sure you have an active on-prem agent. Refer to the [On-premise connectivity](/en/on-prem.html) guide for more information. |
| Username | Username to connect to PostgreSQL. |
| Password | Password to connect to PostgreSQL. |
| Host | URL of your hosted server. |
| Port | Port number that your server is running on, typically **5432**. |
| Database name | Name of the PostgreSQL database you wish to connect to. |
| Schema | Name of the schema within the PostgreSQL database you wish to connect to. Defaults to **public**. |

### Permissions required to connect

At minimum, the database user account must be granted `SELECT` permission to the database specified in the [connection](#how-to-connect-to-postgresql-on-workato).

If we are trying to connect to a PostgreSQL instance, using a new database user `workato`, the following example queries can be used.

First, create a new user dedicated to integration use cases with Workato.

```sql
CREATE USER workato WITH PASSWORD 'password';
```

The next step is to grant access to `customer` table in the schema. In this example, we only wish to grant `SELECT` and `INSERT` permissions.

```sql
GRANT SELECT,INSERT ON customer TO workato;
```

Finally, check that this user has the necessary permissions. Run a query to see all grants.

```sql
SELECT grantee, table_name, privilege_type
FROM information_schema.role_table_grants
WHERE grantee = 'workato';
```

This should return the following minimum permission to create a PostgreSQL connection on Workato.

```
+---------+------------+----------------+
| grantee | table_name | privilege_type |
+---------+------------+----------------+
| workato | customer   | SELECT         |
+---------+------------+----------------+
| workato | customer   | INSERT         |
+---------+------------+----------------+
2 rows in set (0.26 sec)
```

## Working with the PostgreSQL connector

### Table, view, and stored procedure

The PostgreSQL connector works with all tables, views, and stored procedures. These are available in pick lists in each trigger/action or you can provide the exact name.

![Table selection from pick list](/assets/table_pick_list.C5vxAja9.png)_Select a table/view from pick list_

![Exact table name provided](/assets/table_name_text.MINqJklu.png)_Provide exact table/view name in a text field_

In PostgreSQL, unquoted identifiers are case-insensitive. Thus,

```sql
SELECT ID FROM USERS
```

is equivalent to

```sql
SELECT ID FROM users
```

However, quoted identifiers are case-sensitive. Hence,

```sql
SELECT ID FROM "USERS"
```

is **NOT** equivalent to

```sql
SELECT ID FROM "users"
```

### Single row vs batch of rows

PostgreSQL connector can read or write to your database either as a single row or in batches. When using batch triggers/actions, you have to provide the batch size you wish to work with. The batch size can be any number between 1 and 100, with 100 being the maximum batch size.

![Batch trigger inputs](/assets/batch_trigger_input.BDXsE6O1.png)_Batch trigger inputs_

Besides the difference in input fields, there is also a difference between the outputs of these 2 types of operations. A trigger that processes rows one at a time will have an output datatree that allows you to map data from that single row.

![Single row output](/assets/single_row_trigger_output.CPQaaSmr.png)_Single row output_

However, a trigger that processes rows in batches will output them as an array of rows. The Rows datapill indicates that the output is a list containing data for each row in that batch.

![Batch trigger output](/assets/batch_trigger_output.B74MZCBy.png)_Batch trigger output_

As a result, the output of batch triggers/actions needs to be handled differently. This [recipe](https://www.workato.com/recipes/667105) uses a batch trigger for new rows in the `users` table. The output of the trigger is used in a Salesforce bulk create action that requires mapping the Rows datapill into the source list.

![Using batch trigger output](/assets/using_batch_output.DhVGjyED.png)_Using batch trigger output_

### WHERE condition

This input field is used to filter and identify rows to perform an action on. It is used in multiple triggers and actions in the following ways:

- filter rows to be picked up in triggers
- filter rows in **Select rows** action
- filter rows to be deleted in **Delete rows** action

> **TIP**
> 
> Examples below showcase how to use WHERE conditions directly with user input. For added security, use WHERE conditions with parameters to prevent SQL injection. [Learn more](#using-parameters)

This clause will be used as a `WHERE` statement in each request. This should follow basic SQL syntax. Refer to this [PostgreSQL documentation](https://dev.postgresql.com/doc/refman/5.7/en/language-structure.html) for a full list of rules for writing PostgreSQL statements.

#### Operators

| Operator | Description | Example |
| --- | --- | --- |
| \= | Equal | `WHERE ID = 445` |
| != <> | Not equal | `WHERE ID <> 445` |
| \> >= | Greater than Greater than or equal to | `WHERE PRICE > 10000` |
| < <= | Less than Less than or equal to | `WHERE PRICE > 10000` |
| IN(...) | List of values | `WHERE ID IN(445, 600, 783)` |
| LIKE | Pattern matching with wildcard characters (`%` and `_`) | `WHERE EMAIL LIKE '%@workato.com'` |
| BETWEEN | Retrieve values with a range | `WHERE ID BETWEEN 445 AND 783` |
| IS NULL IS NOT NULL | NULL values check Non-NULL values check | `WHERE NAME IS NOT NULL` |

#### Simple statements

String values must be enclosed in single quotes (`''`) and columns used must exist in the table.

A simple `WHERE` condition to filter rows based on values in a single column looks like this.

```sql
role = 'admin'
```

If used in a **Select rows** action, this `WHERE` condition will return all rows that have the value 'admin' in the `role` column. Just remember to wrap datapills with single quotes in your inputs.

![Using datapills in WHERE condition](/assets/use_datapill_in_where.DLDmluXH.png)_Using datapills in `WHERE` condition_

Column names with spaces must be enclosed in double quotes (`""`). For example, **currency code** must to enclosed in brackets to be used as an identifier. Note that all quoted identifiers are case-sensitive.

```sql
"created date" = '2020-05-06'
```

In a recipe, remember to use the appropriate quotes for each value/identifier.

![WHERE condition with enclosed identifier](/assets/where-condition-with-enclosed-identifier.BQn-FbW1.png)_`WHERE` condition with enclosed identifier_

#### Complex statements

Your `WHERE` condition can also contain subqueries. The following query can be used on the `users` table.

```sql
id in (select user_id from tickets where priority = 2)
```

When used in a **Delete rows** action, this will delete all rows in the `users` table where at least one associated row in the `tickets` table has a value of 2 in the `priority` column.

![Using datapills in WHERE condition with subquery](/assets/use_datapill_in_where_complex.BfiziGsu.png)_Using datapills in `WHERE` condition with subquery_

## Using parameters

Parameters are used in conjunction with `WHERE` conditions to add an additional layer of security against SQL injection. To use parameters in your `WHERE` conditions, you will first need to declare bind variables in your input. Bind parameters must be declared in the form `:bind_variable` where the variable name is preceded with a `:`. After this is done, declare the parameter in the section directly below using the exact name you have given.

> **TIP**
> 
> Bind variables should only be used in place of column values and not column names.

![WHERE condition with bind variable](/assets/where-condition-with-bind-variable.CdW0wsTr.png)_`WHERE` condition with bind variable_

You can provide as many bind variables as you'd like and each one should have a unique name. We distinguish bind variables from column names and static values by ignoring any `:` inside single quotes (`'`), double quotes (`"`) and square brackets (`[]`).

### Unique key

In all triggers and some actions, this is a required input. Values from this selected column are used to uniquely identify rows in the selected table.

As such, the values in the selected column must be unique. Typically, this column is the **primary key** of the table (for example, `ID`).

When used in a trigger, this column must be incremental. This constraint is required because the trigger uses values from this column to look for new rows. In each poll, the trigger queries for rows with a unique key value greater than the previous greatest value.

Let's use a simple example to illustrate this behavior. We have a **New row** trigger that processed rows from a table. The **unique key** configured for this trigger is `ID`. The last row processed has `100` as it's `ID` value. In the next poll, the trigger will use `ID >= 101` as the condition to look for new rows.

Performance of a trigger can be improved if the column selected to be used as the **unique key** is indexed.

### Sort column

This is required for **New/updated row triggers**. Values in this selected column are used to identify updated rows.

When a row is updated, the Unique key value remains the same. However, it should have it's timestamp updated to reflect the last updated time. Following this logic, Workato keeps track of values in this column together with values in the selected **Unique key** column. When a change in the **Sort column** value is observed, an updated row event will be recorded and processed by the trigger.

For PostgreSQL, only **timestamp** and **timestamp with time zone** column types can be used.

### Parameter quotas

PostgreSQL supports a maximum of **65,535** bind parameters in a single SQL statement. You may encounter a query failure if you exceed this quota.

To avoid this, reduce the batch size, split the query into smaller parts, use array binding, or load data in bulk using COPY.

Workato recommends that you structure recipes and SQL operations to operate within this parameter quota to ensure stability.

---
