---
url: 'https://docs.workato.com/en/connectors/redshift/custom-sql-action.md'
description: >-
  The Run custom SQL action in the Redshift connector executes a single DML or
  DDL SQL statement, returning up to 50,000 rows in Workato.
---

# Redshift - Run custom SQL action

This action enables you to execute a SQL in Redshift. The maximum number of rows returned in this action is 50,000. Redshift only supports one SQL statement per action. You can use this action to execute Data Manipulation Language (DML) statements such as `INSERT`, `UPDATE`, and `DELETE`, as well as Data Definition Language (DDL) commands, such as `CREATE`, `ALTER`, and `DROP`.

> **1 MB QUERY SIZE QUOTA**
> 
> Starting 1 December 2025, the **Run custom SQL** action in this connector enforces a 1 MB query size quota. This change improves platform reliability, increases performance, and avoids large queries that overload database connections or impact upstream systems.

Use the [Select rows using custom SQL](/en/connectors/redshift/select#select-rows-using-custom-sql) action to retrieve a CSV stream for [SELECT](/en/connectors/redshift/select) actions.

![Run custom SQL action](/assets/run-custom-sql.BgJ8yN6U.png)_Run custom SQL action_

## Input

| Input field | Description |
| --- | --- |
| SQL | Enter a valid SQL query string. For example: `SELECT * FROM PUBLIC.ACCOUNTS`. The query size is limited to 1 MB. |
| Execute update only SQL statement without row limit | Enables the action to run with no row limits on SQL statements, but also returns no rows. You can use this field to perform bulk data transformations. Defaults to no. |
| Parameters | Define the fields you plan to include in the list, and assign values to each field. You must declare the named bind variables in your `WHERE` input and assign values to these variables. Parameter values can be static or datapills. Select the closest corresponding data type that your database expects for the bind variable. |
| Output Fields | Describe the output for each row of your custom SQL string. |

## Output

| Output field | Description |
| --- | --- |
| Rows | Returns a list of rows from SQL execution. Only fields you defined in the **Output Fields** input field are returned. If you leave this field blank, the row is available in the datatree as an array datapill. |
| Rows affected | Returns the number of rows affected by the SQL string execution. This field returns `nil` for `SELECT` statements and `0` for DDL statements. |

---
