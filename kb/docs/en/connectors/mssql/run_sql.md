---
url: 'https://docs.workato.com/en/connectors/mssql/run_sql.md'
description: >-
  The Run custom SQL action in the SQL Server connector lets you execute DML and
  DDL statements such as INSERT, UPDATE, CREATE, and DROP.
---

# SQL Server - Run custom SQL action

## Run custom SQL

This action lets you send a SQL string to the SQL Server instance to be executed. It can be used to execute Data Manipulation Language (DML) statements like `INSERT`, `UPDATE`, `SELECT` and `DELETE`, as well as Data Definition Language (DDL) commands, like `CREATE`, `ALTER` and `DROP`.

> **1 MB QUERY SIZE QUOTA**
> 
> Starting 1 December 2025, the **Run custom SQL** action in this connector enforces a 1 MB query size quota. This change improves platform reliability, increases performance, and avoids large queries that overload database connections or impact upstream systems.

Unlike [Select rows using custom SQL](/en/connectors/mssql/select#select-rows-using-custom-sql), this action is not optimized for easy configuration. For `SELECT` statements with many columns, use that action instead. Using custom SQL is a great way to improve recipe efficiency and balance load between Workato and your database. [Find out more in our best practices section how to use custom SQL to make your recipes more efficient.](/en/connectors/databases/best-practices#using-custom-sql-and-stored-procedures)

> **OPA required**
> 
> This action requires a connection using Workato on-prem agent. Refer to [On-prem connectivity](/en/on-prem) for more information.

> **Getting timeout error**
> 
> During bulk load of large datasets, creating, and updating tables in a database may take a long time. It may cause the job to fail with a [timeout](/en/recipes/jobs#timeouts).
> 
> Prevent timeout errors by running your custom SQL asynchronously. Refer to [Run custom SQL asynchronously](#run-custom-sql-asynchronously) for more information.

![Run custom SQL action](/assets/run_sql.BWzooMDN.png)_Run custom SQL action_

### Input

| Input field | Description |
| --- | --- |
| SQL | **Required**. Enter a valid SQL string to run on your SQL Server instance. Workato can execute multiple SQL statements, but only returns results from the last statement. Separate each statement with a `;`. You can map datapills to execute dynamic SQL. Wrap datapills in single quotes (`''`). The query size is limited to 1 MB. |
| Output fields | Define the columns returned by your SQL statement. You can configure the output schema manually or click **Use SQL** to generate it from a sample query. The **Use SQL** option only supports queries that begin with a `SELECT` statement. Queries that begin with `WITH` aren't supported and trigger a syntax error. Leave this field blank if you don't expect return values. |

### Output

| Output field | Description |
| --- | --- |
| Rows | A list of rows returned from the SQL execution. The structure is defined by the **Output fields** input. This field appears as an array datapill in the datatree if the **Output fields** input is blank. |
| Rows affected | The number of rows inserted, updated, or deleted. Returns `nil` for `SELECT` statements. Returns `0` for DDL statements like `CREATE TABLE`. |

> **Size quota**
> 
> There is a size quota of `50,000` rows when your custom SQL statement returns data.

## Run custom SQL asynchronously

This action lets you send a SQL string to the SQL Server instance to be executed. It can be used to execute Data Manipulation Language (DML) statements like `INSERT`, `UPDATE`, `SELECT` and `DELETE`, as well as Data Definition Language (DDL) commands, like `CREATE`, `ALTER` and `DROP`.

After the custom SQL query begins processing, Workato will check in periodically to see if the query results are ready to be retrieved. When the results have been successfully retrieved, Workato will proceed to the next steps in the recipe.

### Why run asynchronously

When a large dataset is being uploaded (`INSERT`) or updated (`UPDATE`), the action may take a long time to respond. If it exceeds the timeout limit, it will cause the recipe to fail due to a timeout error.

Running the SQL query asynchronously allows you to execute queries on large datasets without worrying about the time out. Even if the action takes hours to process, the job will not time out.

> **ACTION REQUIRES AN ON-PREM AGENT**
> 
> This action requires a connection using Workato on-prem agent. Refer to the [On-premise connectivity](/en/on-prem) guide for more information.

![Run custom SQL (async) action](/assets/run_sql_async.BJEwqe1G.png)_Run custom SQL (async) action_

### Output

| Input field | Description |
| --- | --- |
| Rows | List of rows returned from the SQL execution. The fields in this list are defined by the **Output fields** input field. If left blank, this row will be available in the datatree as an array datapill. |
| Rows affected | This is an integer value indicating the number of rows inserted/updated/deleted from the SQL string. When executing `SELECT` statements, this will return `nil`. When executing a DDL (for example, creating a table), the value `0` will be returned. |

> **Size quota**
> 
> There is a size quota of `50,000` rows when your custom SQL statement returns data.

---
