---
url: 'https://docs.workato.com/en/connectors/redshift.md'
description: >-
  The Redshift connector lets you run SQL on your data warehouse: select,
  insert, update, upsert, and delete rows, and trigger on new rows.
---

# Redshift

[Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html) is a fast and fully managed data warehouse that makes it simple and cost-effective to analyze all your data using standard SQL and your existing Business Intelligence (BI) tools.

## How to connect to Redshift on Workato

The Redshift connector uses basic authentication to authenticate with Redshift. ![Configured Redshift connection](/assets/connection.CMiATZr8.png)

| Field | Description |
| --- | --- |
| Connection name | Give this Redshift connection a unique name that identifies which Redshift instance it is connected to. |
| URL | Full JDBC URL of your Redshift instance. Example: **jdbc:redshift://redshift-main.sample.us-east-2.redshift.amazonaws.com:5439/dev** |
| Username | Username to connect to Redshift. |
| Password | Password to connect to Redshift. |
| Schema | Name of the schema within the Redshift database you wish to connect to. Defaults to **public**. |
| Connection type | Choose an on-prem group if your database is running in a network that does not allow direct connection. Before attempting to connect, make sure you have an active on-prem agent. Refer to the [On-premise connectivity](/en/on-prem.html) guide for more information. |

### Permissions required to connect

At minimum, the database user account must be granted `SELECT` permission to the database specified in the [connection](#how-to-connect-to-redshift-on-workato).

If we are trying to connect to a Redshift instance, using a new database user `workato`, the following example queries can be used.

First, create a new user dedicated to integration use cases with Workato.

```sql
CREATE USER workato PASSWORD 'password';
```

The next step is to grant access to `customer` table in the schema. In this example, we only wish to grant `SELECT` and `INSERT` permissions.

```sql
GRANT SELECT,INSERT ON TABLE customer TO workato;
```

Finally, check that this user has the necessary permissions. Run a query to see all grants.

```sql
SELECT
    u.usename,
    t.schemaname||'.'||t.tablename AS "table",
    has_table_privilege(u.usename,t.tablename,'select') AS "select",
    has_table_privilege(u.usename,t.tablename,'insert') AS "insert",
    has_table_privilege(u.usename,t.tablename,'update') AS "update",
    has_table_privilege(u.usename,t.tablename,'delete') AS "delete"
FROM
    pg_user u
CROSS JOIN
    pg_tables t
WHERE
    u.usename = 'workato'
```

This should return the following minimum permission to create a Redshift connection on Workato.

```
+---------+----------+--------+--------+--------+--------+
| usename | table    | select | insert | update | delete |
+---------+----------+--------+--------+--------+--------+
| workato | customer | true   | true   | false  | false  |
+---------+----------+--------+--------+--------+--------+
2 rows in set (0.26 sec)
```

## Working with the Redshift connector

### Table and view

The Redshift connector works with all tables and views. These are available in pick lists in each trigger/action or you can provide the exact name.

![Table selection from pick list](/assets/table_pick_list.TjqSwf3M.png)_Select a table/view from pick list_

![Exact table name provided](/assets/table_name_text.C6rxxPwv.png)_Provide exact table/view name in a text field_

In Redshift, unquoted identifiers are case-insensitive. Thus,

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

Redshift connector can read or write to your database either as a single row or in batches. When using batch triggers/actions, you have to provide the batch size you wish to work with. The batch size can be any number between 1 and 100, with 100 being the maximum batch size.

![Batch trigger inputs](/assets/batch_trigger_input.DzZzPA49.png)_Batch trigger inputs_

Besides the difference in input fields, there is also a difference between the outputs of these 2 types of operations. A trigger that processes rows one at a time will have an output datatree that allows you to map data from that single row.

![Single row output](/assets/single_row_trigger_output.DFyTsXoK.png)_Single row output_

However, a trigger that processes rows in batches will output them as an array of rows. The Rows datapill indicates that the output is a list containing data for each row in that batch.

![Batch trigger output](/assets/batch_trigger_output.C0du3bVd.png)_Batch trigger output_

As a result, the output of batch triggers/actions needs to be handled differently. This [recipe](https://www.workato.com/recipes/690471) uses a batch trigger for new rows in the `users` table. The output of the trigger is used in a Salesforce bulk update action that requires mapping the Rows datapill into the source list.

![Using batch trigger output](/assets/using_batch_output.CLtQf0VW.png)_Using batch trigger output_

### WHERE condition

This input field is used to filter and identify rows to perform an action on. It is used in multiple triggers and actions in the following ways:

- filter rows to be picked up in triggers
- filter rows in **Select rows** action
- filter rows to be deleted in **Delete rows** action

This clause will be used as a `WHERE` statement in each request. This should follow basic SQL syntax. Refer to this [Redshift documentation](https://docs.aws.amazon.com/redshift/latest/dg/c_redshift-sql.html) for a full list of rules for writing Redshift SQL statements.

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
currency = 'USD'
```

If used in a **Select rows** action, this `WHERE` condition will return all rows that have the value 'USD' in the `currency` column. Just remember to wrap datapills with single quotes in your inputs.

![Using datapills in WHERE condition](/assets/use_datapill_in_where.Dq9K7vx2.png)_Using datapills in `WHERE` condition_

Column names with spaces must be enclosed in double quotes (`""`). For example, **currency code** must to enclosed in brackets to be used as an identifier. Note that all quoted identifiers are case-sensitive.

```sql
"currency code" = 'USD'
```

In a recipe, remember to use the appropriate quotes for each value/identifier.

![WHERE condition with enclosed identifier](/assets/where-condition-with-enclosed-identifier.DjGoi9eo.png)_`WHERE` condition with enclosed identifier_

#### Complex statements

Your `WHERE` condition can also contain subqueries. The following query can be used on the `accounts` table.

```sql
id in (select user_id from tickets where priority = 2)
```

When used in a **Delete rows** action, this will delete all rows in the `invoices` table where at least one associated row in the `accounts` table has a value of 2 in the `account_name` column.

![Using datapills in WHERE condition with subquery](/assets/use_datapill_in_where_complex.D-MtK9E_.png)_Using datapills in `WHERE` condition with subquery_

#### Unique key

In all triggers and some actions, this is a required input. Values from this selected column are used to uniquely identify rows in the selected table.

As such, the values in the selected column must be unique. Typically, this column is the **primary key** of the table (for example, `ID`).

When used in a trigger, this column must be incremental. This constraint is required because the trigger uses values from this column to look for new rows. In each poll, the trigger queries for rows with a unique key value greater than the previous greatest value.

Let's use a simple example to illustrate this behavior. We have a **New row** trigger that processed rows from a table. The **unique key** configured for this trigger is `ID`. The last row processed has `100` as it's `ID` value. In the next poll, the trigger will use `ID >= 101` as the condition to look for new rows.

Performance of a trigger can be improved if the column selected to be used as the **unique key** is indexed.

#### Sort column

This is required for **New/updated row triggers**. Values in this selected column are used to identify updated rows.

When a row is updated, the **Unique key** value remains the same. However, it should have it's **Sort column** updated to reflect the last updated time. Following this logic, Workato keeps track of values in this column together with values in the selected **Unique key** column. When a change in the **Sort column** value is observed, an updated row event will be recorded and processed by the trigger.

Let's use a simple example to illustrate this behavior. We have a **New/updated row** trigger that processed rows from a table. The **Unique key** and **Sort column** configured for this trigger is `ID` and `UPDATED_AT` respectively. The last row processed by the trigger has `ID` value of `100` and `UPDATED_AT` value of `2018-05-09 16:00:00.000000`. In the next poll, the trigger will query for new rows that satisfy either of the 2 conditions:

1. `UPDATED_AT > '2018-05-09 16:00:00.000000'`
2. `ID > 100 AND UPDATED_AT = '2018-05-09 16:00:00.000000'`

For Redshift, only **timestamp** and **timestamptz** column types can be used.

---
