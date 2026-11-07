---
url: 'https://docs.workato.com/en/connectors/mysql.md'
description: >-
  The MySQL connector automates relational database workflows: insert, update,
  upsert, select, and delete rows, run custom SQL, and trigger on new rows.
---

# MySQL

[MySQL](http://www.MySQL.com/) is an open-source relational database management system hosted either in the cloud or on-premise.

## Supported editions

All editions of MySQL are supported.

## How to connect to MySQL on Workato

The MySQL connector uses basic authentication to authenticate with MySQL. ![Configured MySQL connection](/assets/connection.Dl1cma9d.png)

Complete the following steps to connect to MySQL:

1. Select **Create > Connection** or press C twice.
   
2. Search for `MySQL` on the **New connection** page and select it.
   
3. Enter a name in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select **Cloud**, or select an on-prem group if your database isn't directly reachable from Workato.
   
6. Enter the hostname of your MySQL instance in the **Host** field.
   
7. Enter the port number in the **Port** field. The default MySQL port is `3306`.
   
8. Enter your MySQL username in the **Username** field.
   
9. Enter your MySQL password in the **Password** field.
   
10. Enter the name of the database to sync in the **Database** field.
    
11. Optional. Expand **Advanced settings** to configure the following:
    
    1. Toggle **Use improved datetime handling** to enable enhanced handling of `date`, `datetime`, and `timestamp` data types. Defaults to true.
       
    2. Set the **Database timezone** field to the local timezone of your database. Default is UTC.
       
12. Select **Connect** to verify and save the connection.
    

### Improved datetime handling

The MySQL connector now has the option to utilize improved handling of datetime, datetime2, and datetimeoffset datatype. This can be enabled in the connection settings of each MySQL connection. This defaults to `Yes` for all new connections and defaults to UTC timezones. Change this to the local timezone of your database if needed. This affects all actions that **insert rows** into MySQL.

> **WARNING**
> 
> There are various timezone settings in MySQL. If no changes are made, your MySQL **system** timezone should be the same as your **global** timezone and set to UTC.

![Advanced connection setting](/assets/advanced_date_time_handling.DYigUUKa.png)_Configure this in the setting of your MySQL connection_

**Summary of behavior**

| Datatype | Workato input | Improved datetime handling set to false/unselected | Improved datetime handling set to true |
| --- | --- | --- | --- |
| date | Time with no TZ | Workato workspace timezone assumed. Converted to UTC before insertion | No TZ assumed. Inserted as is |
| date | Time with TZ | Converted to UTC before insertion | Converted to database timezone in connection setting timezone before insertion |
| datetime | Time with no TZ | Workato workspace timezone assumed. Converted to UTC before insertion. | No TZ assumed. Inserted as is |
| datetime | Time with TZ | Converted to UTC before insertion. | Converted to database timezone in connection setting timezone before insertion |
| timestamp | Time with no TZ | Workato workspace timezone assumed. Converted to UTC before insertion with +00:00 tz | No TZ assumed. Inserted as is |
| timestamp | Time with TZ | Converted to UTC before insertion | Converted to database timezone in connection setting timezone before insertion |

> **Note**
> 
> When using the calendar datepicker for date/datetime/timestamp fields, times are defined using your Workato workspace timezone.

### Permissions required to connect

At minimum, the database user account must be granted `SELECT` permission to the database specified in the [connection](#how-to-connect-to-mysql-on-workato).

If we are trying to connect to a named database (`HR_PROD`) in a MySQL instance, using a new database user `workato`, the following example queries can be used.

First, create a new user dedicated to integration use cases with Workato.

```sql
CREATE USER 'workato' IDENTIFIED BY 'password';
```

This allows the user to have login access to the MySQL instance. However, this user will not have access to any tables.

The next step is to grant access to all tables in `HR_PROD`. In this example, we only wish to grant `SELECT` permissions.

```sql
GRANT SELECT ON `HR_PROD`.* TO 'workato';
```

Finally, check that this user has the necessary permissions. Run a query to see all grants.

```sql
SHOW GRANTS FOR 'workato';
```

This should return the following minimum permission to create a MySQL connection on Workato.

```
+---------------------------------------------------------------------+
| Grants for workato@%                                                |
+---------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'workato'@'%' IDENTIFIED BY PASSWORD <secret> |
| GRANT SELECT ON `HR_PROD`.* TO 'workato'@'%'                        |
+---------------------------------------------------------------------+
2 rows in set (0.24 sec)
```

## Working with the MySQL connector

### Table, view, and stored procedure

The MySQL connector works with all tables, views, and stored procedures. These are available in pick lists in each trigger/action or you can provide the exact name.

![Table selection from pick list](/assets/table_pick_list.CeuXIQqR.png)_Select a table/view from pick list_

![Exact table name provided](/assets/table_name_text.CjI8_wcW.png)_Provide exact table/view name in a text field_

Case sensitivity of the name of a table/view depends on your database implementation. The underlying OS that your database is hosted determines if you need to provide exact table/view names. Typically, database, and table names are case insensitive in Windows.

### Single row vs batch of rows

The MySQL connector supports reading from and writing to your database, either one row at a time or in batches. For batch triggers and actions, you must specify the batch size. The default is 100 rows per batch, and the maximum is 1000.

![Batch trigger inputs](/assets/batch_trigger_input.zdbc83aj.png)_Batch trigger inputs_

Besides the difference in input fields, there is also a difference between the outputs of these 2 types of operations. A trigger that processes rows one at a time will have an output datatree that allows you to map data from that single row.

![Single row output](/assets/single_row_trigger_output.Yp530LFt.png)_Single row output_

However, a trigger that processes rows in batches will output them as an array of rows. The Rows datapill indicates that the output is a list containing data for each row in that batch.

![Batch trigger output](/assets/batch_trigger_output.D6ii6bQb.png)_Batch trigger output_

As a result, the output of batch triggers/actions needs to be handled differently. This [recipe](https://www.workato.com/recipes/660208) uses a batch trigger for new rows in the `users` table. The output of the trigger is used in a Salesforce bulk update action that requires mapping the Rows datapill into the source list.

![Using batch trigger output](/assets/using_batch_output.BldQ3GCi.png)_Using batch trigger output_

### WHERE condition

This input field is used to filter and identify rows to perform an action on. It is used in multiple triggers and actions in the following ways:

- filter rows to be picked up in triggers
- filter rows in **Select rows** action
- filter rows to be deleted in **Delete rows** action

> **TIP**
> 
> Examples below showcase how to use WHERE conditions directly with user input. For added security, use WHERE conditions with parameters to prevent SQL injection. [Learn more](#using-parameters)

This clause will be used as a `WHERE` statement in each request. This should follow basic SQL syntax. Refer to this [MySQL documentation](https://dev.mysql.com/doc/refman/5.7/en/language-structure.html) for a full list of rules for writing MySQL statements.

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
username = 'someone'
```

If used in a **Select rows** action, this `WHERE` condition will return all rows that have the value 'someone' in the `username` column. Just remember to wrap datapills with single quotes in your inputs.

![Using datapills in WHERE condition](/assets/use_datapill_in_where.O9B8bDOj.png)_Using datapills in `WHERE` condition_

Backticks (` `` `) in `WHERE` statements are for tables and columns identifiers. This is required when the identifier is a MySQL reserved keyword or contains special characters.

```sql
`username` = 'someone'
```

In a recipe, remember to add backticks to the column identifiers.

![Using datapills in WHERE condition with backticks](/assets/use_datapill_in_where_backticks.v1JoGpxX.png)_Using datapills in `WHERE` condition backticks_

Double quotes (`""`) can also be used for string values but is less commonly accepted in other databases. For this reason, single quotes are used more widely than double quotes.

MySQL also expects `DATE` and `DATETIME` values to be single quoted.

```sql
created_date > '2018-03-01' and country = 'USA'
```

In a recipe, remember to use the appropriate quotes for each value.

![Using datapills in WHERE condition with mixed column types](/assets/use_datapill_in_where_mixed.DOW73V1y.png)_Using datapills in `WHERE` condition with mixed column types_

#### Complex statements

Your `WHERE` condition can also contain subqueries. The following query can be used on the `users` table.

```sql
id in (select id from user where created_time < '2020-05-06')
```

When used in a **Delete rows** action, this will delete all rows in the `users` table where at least one associated row in the `tickets` table has a value of 2 in the `priority` column.

![Using datapills in WHERE condition with subquery](/assets/use_datapill_in_where_complex.CIx5OEZx.png)_Using datapills in `WHERE` condition with subquery_

## Using Parameters

Parameters are used in conjunction with `WHERE` conditions to add an additional layer of security against SQL injection. To use parameters in your `WHERE` conditions, you will first need to declare bind variables in your input. Bind parameters must be declared in the form `:bind_variable` where the variable name is preceded with a `:`. After this is done, declare the parameter in the section directly below using the exact name you have given.

> **TIP**
> 
> Bind variables should only be used in place of column values and not column names.

![WHERE condition with bind variable](/assets/where-condition-with-bind-variable.CdW0wsTr.png)_`WHERE` condition with bind variable_

You can provide as many bind variables as you'd like and each one should have a unique name. We distinguish bind variables from column names and static values by ignoring any `:` inside single quotes (`'`), double quotes (`"`) and square brackets (`[]`).

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

For MySQL, only **datetime** and **timestamp** column types can be used.

---
