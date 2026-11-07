---
url: 'https://docs.workato.com/en/connectors/postgresql/run_sql.md'
description: >-
  The Run custom SQL action in the PostgreSQL connector executes a SQL string,
  supporting DML statements like INSERT and DDL commands like CREATE.
---

# PostgreSQL - Run custom SQL action

## Run custom SQL

This action lets you send a SQL string to the PostgreSQL instance to be executed. It can be used to execute Data Manipulation Language (DML) statements like `INSERT`, `UPDATE`, `SELECT` and `DELETE`, as well as Data Definition Language (DDL) commands, like `CREATE`, `ALTER` and `DROP`.

> **1 MB QUERY SIZE QUOTA**
> 
> Starting 1 December 2025, the **Run custom SQL** action in this connector enforces a 1 MB query size quota. This change improves platform reliability, increases performance, and avoids large queries that overload database connections or impact upstream systems.

Unlike [Select rows using custom SQL](/en/connectors/postgresql/select#select-rows-using-custom-sql), this action is not optimized for easy configuration. For `SELECT` statements with large number of columns, use that action instead.

![Run custom SQL action](/assets/run_sql.btMJ4KXN.png)_Run custom SQL action_

### Input

| Input field | Description |
| --- | --- |
| SQL | **This field is required**. Provide a valid SQL string to be executed. This SQL string will be executed in your PostgreSQL instance. If multiple SQL statements are provided, all of them will be executed. However, only results from the last statement will be returned. Make sure each statement is separated by a `;` character. You can map datapills here to execute dynamically changing SQL statements. Remember to wrap datapills in quotes (`''`). The query size is limited to 1 MB. |
| Output fields | Use this input to describe the columns that you are expecting from your SQL statement. If you do not expect any return values or do not need any, you may ignore this input field. |

### Output

| Input field | Description |
| --- | --- |
| Rows | List of rows returned from the SQL execution. The fields in this list are defined by the **Output fields** input field. If left blank, this row will be available in the datatree as an array datapill. |
| Rows affected | This is an integer value indicating the number of rows inserted/updated/deleted from the SQL string. When executing `SELECT` statements, this will return `nil`. When executing a DDL (for example, creating a table), the value `0` will be returned. |

### Limitations

There is a size quota of `50000` rows when your custom SQL statement returns data.

---
