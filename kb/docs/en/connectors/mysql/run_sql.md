---
url: 'https://docs.workato.com/en/connectors/mysql/run_sql.md'
description: >-
  The Run custom SQL action in the MySQL connector sends a SQL string to your
  instance to run DML statements and DDL commands.
---

# MySQL - Run custom SQL action

This action lets you send a SQL string to the MySQL instance to be executed. It can be used to execute Data Manipulation Language (DML) statements like `INSERT`, `UPDATE`, `SELECT` and `DELETE`, as well as Data Definition Language (DDL) commands, like `CREATE`, `ALTER` and `DROP`.

> **1 MB QUERY SIZE QUOTA**
> 
> Starting 1 December 2025, the **Run custom SQL** action in this connector enforces a 1 MB query size quota. This change improves platform reliability, increases performance, and avoids large queries that overload database connections or impact upstream systems.

![Run custom SQL action](/assets/run_sql.XILf_YpJ.png)_Run custom SQL action_

## Input

| Input field | Description |
| --- | --- |
| SQL | Provide a valid SQL string to be executed. This SQL string is executed in your MySQL instance. You can map datapills here to execute dynamically changing SQL statements. Wrap datapills in quotes (`''`). The query size is limited to 1 MB. |
| Execute update only SQL statement without row limit | Select `Yes` to return rows, up to a 50k row limit, or for SELECT queries. Select `No` to return no rows in the response, or for INSERT or UPDATE queries. |
| Output fields | Use this input to describe the columns that you expect from your SQL statement. You can leave this input field empty if you don't expect return values. |

## Output

| Output field | Description |
| --- | --- |
| Rows | List of rows returned from the SQL execution. The fields in this list are defined by the **Output fields** input field. If left blank, this row is available in the datatree as an array datapill. |
| Rows affected | An integer value that indicates the number of rows inserted, updated, or deleted from the SQL string. When you execute `SELECT` statements, this returns `nil`. When you execute a DDL statement (for example, creating a table), this returns `0`. |

### Limitations

There is a size quota of `50000` rows when your custom SQL statement returns data.

---
