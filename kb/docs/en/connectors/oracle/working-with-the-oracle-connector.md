---
url: >-
  https://docs.workato.com/en/connectors/oracle/working-with-the-oracle-connector.md
description: >-
  Best practices for working with the Oracle connector in Workato, including
  tables, views, stored procedures, and WHERE conditions.
---

# Working with the Oracle connector

This guide provides best practices for working with our Oracle connector. Refer to [Oracle connector](/en/connectors/oracle) for more information.

* * *

## Table, view, and stored procedure

You can select either a table, view, or stored procedure after successfully connecting to your Oracle database and selecting an action/trigger in your recipe. This tells Workato where to pull or send data.

* * *

## Tables and Views

The Oracle connector works with all tables and views. You can select the tables or views you plan to use in the drop-down menu in each trigger or action, or you can provide the exact name.

![Table selection from pick list](/assets/table_pick_list.CUNfJ3m0.png)_Select a table/view from pick list_

  

![Exact table name provided](/assets/table_name_text.SeYmjcQS.png)_Provide exact table/view name in a text field_

* * *

## Stored Procedures

Stored procedures are custom written workflows that must be written and saved within your Oracle database. Stored procedures enable you to create, update, and delete rows. You can also provide parameters in your stored procedures. Refer to [Oracle - Execute stored procedure action](/en/connectors/oracle/stored-procedure) for more information on how to use stored procedures.

* * *

## Using `WHERE` conditions

Use this input field to filter and identify rows in multiple triggers and actions. The following filters are available:

- Filter rows to be picked up in triggers
- Filter rows in **Select rows** action
- Filter rows to be deleted in **Delete rows** action

> **HOW TO USE WHERE CONDITIONS EXAMPLES**
> 
> Refer to the following examples on how to use `WHERE` conditions directly with user input. Use WHERE conditions with parameters to prevent SQL injection for added security. Refer to [Using parameters](#using-parameters) for more information.

This clause is used as a `WHERE` statement in each request. This should follow basic SQL syntax. Refer to this [Oracle documentation](http://www.oracle.com/technetwork/issue-archive/2012/12-mar/o22sql-1494267.html) for a full list of rules for writing Oracle statements.

### Operators

`WHERE` statements allow you to select operators to filter and identify the rows you plan to return in Workato. You can chain operators the same as in SQL, you can use them to create robust and complex filters on your data directly from Workato.

Click here for a list of operators

> | Operator | Description | Example |
> | --- | --- | --- |
> | \= | Equal | `WHERE ID = 445` |
> | != <> | Not equal | `WHERE ID <> 445` |
> | \> >= | Greater than Greater than or equal to | `WHERE PRICE > 10000` |
> | < <= | Less than Less than or equal to | `WHERE PRICE > 10000` |
> | IN(...) | List of values | `WHERE ID IN(445, 600, 783)` |
> | LIKE | Pattern matching with wildcard characters (`%` and `_`) | `WHERE EMAIL LIKE '%@workato.com'` |
> | BETWEEN | Retrieve values with a range | `WHERE ID BETWEEN 445 AND 783` |
> | IS NULL IS NOT NULL | NULL values check Non-NULL values check | `WHERE NAME IS NOT NULL` |

## Data types

The other component of a `WHERE` condition is to use these operators in conjunction with the proper datatypes. Ensure you compare a variable of `data type = integer` in the table with the same variable of `data type = integer`(instead of `data type = string`) when writing `WHERE` statements.

Workato displays the expected data types for each input field when you select one of the following actions:

- **Update rows** actions
- **Upsert rows** actions

Data types appear directly below the output field, so you know the expected data type to be sent while building the recipe. You can avoid unexpected behavior or failed jobs if you use this information to send the proper data types to your Oracle database.

![input field hints](data:image/png;base64,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)_Information below each input field gives you the expected data type_

Click here for a list of common data types

> | Data type | Description | Example |
> | --- | --- | --- |
> | number | The NUMBER data type stores zero, positive, and negative fixed numbers. | `-100`,`1`,`30,000` |
> | FLOAT | The FLOAT data type is a subtype of NUMBER. You can specify it with or without precision. Scale cannot be specified, but is interpreted from the data. Each FLOAT value requires from 1 to 22 bytes. | `1.11`,`2.0761`,`1.61803398875` |
> | YEAR | valid values are -4712 to 9999 excluding year 0 | `1`,`245`,`100` |
> | MONTH | 01-12 | `1` |
> | DAY | 01-31 | `1`,`0`,`15` |
> | VARCHAR2(n) | **Variable** width character string of length `n` | `Foo_bar` |
> | nchar(n) | **Fixed** width character string of length `n` | `Foo` where n = 3 |
> | TIMESTAMP | From January 1, 1753 to December 31, 9999 with an accuracy of 3.33 milliseconds | `2011-09-16 13:23:18.767` |

Refer to [SQL Data Types](https://www.w3schools.com/sql/sql_datatypes.asp) for a more comprehensive list.

## Writing `WHERE` conditions

String values must be enclosed in single quotes (`''`) and columns used must exist in the table or view.

The following example shows a simple `WHERE` condition to filter rows based on values in a single column.

```sql
currency = 'USD'
```

This `WHERE` condition returns all rows that have the value 'USD' in the `currency` column if used in a **Select rows** action. Wrap datapills with single quotes in your inputs.

![Using datapills in WHERE condition](/assets/use_datapill_in_where.EhQL_lTn.png)_Using datapills in `WHERE` condition_

Column names that don't conform to standard rules, such as spaces, lower-case letters, or special characters, and must be enclosed in double quotes (`""`). For example, **PUBLISHER NAME** must be enclosed in backquotes to be used as a valid identifier.

```sql
"PUBLISHER NAME" = 'USD'
```

![WHERE condition with enclosed identifier](/assets/where_condition_with_enclosed_identifier.CUVepL2A.png)_`WHERE` condition with enclosed identifier_

Click the tabs below for more details on how to use `WHERE` conditions.

Using AND and OR in your WHERE conditions

`WHERE` conditions can also be used in conjunction with basic SQL logical operators like `AND` and `OR` to add more filters on the rows you return.

```sql
("currency code" = 'USD' AND totalAmt >1000) OR totalAmt>2000
```

When used together, this `WHERE` condition returns all rows that either have the value 'USD' in the `currency code` column `AND` more than 1000 in the `totalAmt` column `OR` more than 2000 in the `totalAmt` column.

Using sub-queries in your WHERE conditions

The `WHERE` condition can also contain subqueries. The following query can be used on the `users` table.

```sql
ID IN (SELECT "USER ID" FROM TICKETS WHERE PRIORITY >= 2)
```

This deletes all rows in the `users` table where at least one associated row in the `tickets` table has a value of 2 in the `priority` column when used in a **Delete rows** action.

![Using datapills in WHERE condition with subquery](/assets/use_datapill_in_where_complex.BhDsqAKf.png)_Using datapills in `WHERE` condition with subquery_

## Using Parameters

Parameters are used in conjunction with `WHERE` conditions to add an additional layer of security against SQL injection. You must declare bind variables in your input to use parameters in `WHERE` conditions. Bind parameters must be declared in the form `:bind_variable` where the variable name is preceded with a `:`. Then declare the parameter in the following section using the exact name you previously entered.

> **BIND VARIABLES**
> 
> Bind variables should only be used in place of column values and not column names.

![WHERE condition with bind variable](/assets/where-condition-with-bind-variable.CdW0wsTr.png)_`WHERE` condition with bind variable_

You can provide unlimited bind variables. Each bind variable should have a unique name. Workato distinguishes bind variables from column names and static values by ignoring any `:` inside single quotes (`'`), double quotes (`"`), and square brackets (`[]`).

* * *

## Configuring triggers

The Oracle connector has triggers for both new and updated rows. Both **Unique keys** must be configured for the triggers to work. **Sort columns** must be configured for triggers that find recently updated rows.

A table must satisfy some constraints to be used in a trigger. The following sections contain more information about specific constraints. Refer to [Designing tables for Workato use](/en/connectors/databases/best-practices#designing-tables-for-workato-use) for more information on how to prepare tables for Workato use.

### Unique keys

A unique key is a required input in all triggers and some actions. Values from this selected column are used to uniquely identify rows in the selected table. The values in the selected column must also be unique. This column is typically the **primary key** of the table, for example, `ID`.

When used in a trigger, this column must be incremental. This constraint is required because the trigger uses values from this column to look for new rows. In each poll, the trigger queries for rows with a unique key value greater than the previous greatest value.

Click here for a detailed example

A **New row trigger** processed rows from a table. The **unique key** configured for this trigger is `ID`. The last row processed has `100` as it's `ID` value. The trigger uses `>= 101` as the condition to look for new rows in the next poll.

> The trigger performance can be improved if the column selected to be used as the **unique key** is indexed.

### Sort column

Sort column is required for **New/updated row triggers**. Values in this selected column are used to identify updated rows.

When a row is updated, the **Unique key** value remains the same. However, it should have it's **Sort column** updated to reflect the last updated time. Following this logic, Workato keeps track of values in this column together with values in the selected **Unique key** column. When a change in the **Sort column** value is observed, an updated row event is recorded and processed by the trigger.

For Oracle database, only **date**, **timestamp**, **timestamp with time zone**, and **timestamp with local time zone** column types can be used.

Click here for a detailed example

A **new/updated row trigger** processed rows from a table. The **Unique key** and **Sort column** configured for this trigger is `ID` and `UPDATED_AT`, respectively. The last row processed by the trigger has `ID` value of `100` and `UPDATED_AT` value of `2018-05-09 16:00:00.000000`. In the next poll, the trigger queries for new rows that satisfy either of the following two conditions:  

- `UPDATED_AT'2018-05-09 16:00:00.000000'`  
  
- `ID` > 100 AND `UPDATED_AT = '2018-05-09 16:00:00.000000'`

## Using single row actions and triggers or using batch of rows actions and triggers

The Oracle connector can read or write to your database either as a single row or in batches. You must provide your preferred batch size when using batch triggers and actions. The batch size can be any number from 1-100. Use batch triggers and actions for jobs when you expect to read, create, or update a large number of rows. Batch jobs save the operations band, reduce recipe runtimes, and decrease load on your servers by splitting jobs into separate job runs. Refer to [Batch processing](/en/features/batch-processing) for more information.

![Batch trigger inputs](/assets/batch_trigger_input.DTcfszRv.png)_Batch trigger inputs_

There's also a difference between the outputs of these two types of operations. A trigger that processes rows one at a time has an output datatree that allows you to map data from that single row.

![Single row output](/assets/single_row_trigger_output.1D7V6ba_.png)_Single row output_

However, a trigger that processes rows in batches outputs them as an array of rows. The Rows datapill indicates that the output is a list containing data for each row in that batch.

![Batch trigger output](/assets/batch_trigger_output.HMnvK15R.png)_Batch trigger output_

The output of batch triggers and actions must be handled differently as a result. The **Sync customers from Oracle to Salesforce in batches** recipe uses a batch trigger for new rows in the `users` table. The output of the trigger is used in a Salesforce bulk upsert action that requires mapping the Rows datapill into the source list. Refer to [your Workato instance](https://www.workato.com/recipes/666497) for more information.

![Using batch trigger output](/assets/using_batch_output.Co5pT0Hd.png)_Using batch trigger output_

Outputs from batch triggers and actions can also be used outside of actions that work specifically with lists. You can use Workato's repeat step to control batch outputs and use them with any action build for single rows. Refer to [Lists](/en/features/list-management) for more information.

BEST PRACTICES FOR RECIPE DESIGN

Unsure when to use batch actions and single row actions? Refer to [Batch versus single row triggers and actions](/en/connectors/databases/best-practices#batch-versus-single-row-triggers-and-actions) for more information.

## Smart boolean conversion

Oracle doesn't have a built-in boolean column type. A popular workaround is to use a `NUMBER(1,0)` column with a `CHECK (COLUMN_NAME IN(1,0))` constraint. As a result, standard values from other applications don't map well to this column and may cause unexpected values or errors.

This checkbox allows you to enable automatic smart conversion. The conversion is applied to all columns with `NUMBER` type and precision of `1` if it's set to **Yes**. This reduces the amount of configuration needed to transform datapills in a recipe. The following table describes the logic for the boolean conversion.

| Input value | Converted value |
| --- | --- |
| `true` | `1` |
| `false` | `0` |
| `"true"` | `1` |
| `"false"` | `0` |
