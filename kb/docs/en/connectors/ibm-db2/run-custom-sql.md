---
url: 'https://docs.workato.com/en/connectors/ibm-db2/run-custom-sql.md'
description: >-
  The Run custom SQL action in the IBM Db2 connector lets you run custom DML and
  DDL statements like INSERT, UPDATE, SELECT, DELETE, CREATE, and ALTER.
---

# IBM Db2 - Run custom SQL action

This action enables you query IBM Db2 using a custom SQL string. With it, you can run Data Manipulation Language (DML) statements like `INSERT`, `UPDATE`, `SELECT` and `DELETE`. You can also run Data Definition Language (DDL) commands, like `CREATE`, `ALTER` and `DROP`.

> **1 MB QUERY SIZE QUOTA**
> 
> Starting 1 December 2025, the **Run custom SQL** action in this connector enforces a 1 MB query size quota. This change improves platform reliability, increases performance, and avoids large queries that overload database connections or impact upstream systems.

## Input

| Input field | Description |
| --- | --- |
| SQL | The required SQL code for selecting rows from your Db2 instance. If you provide multiple SQL statements, the system runs all statements. However, it only returns the results of the last statement. You must separate statements using the semicolon character `;`. You can map datapills into this field to execute dynamically changing SQL statements. Datapills must be wrapped in single quote characters, `'`. The query size is limited to 1 MB. |
| Output fields | Define the expected fields of each retrieved row. This enables Workato to generate datapills it can use in downstream systems, or to drive recipe logic. If you do not expect or require return values, ignore this field. |

## Output

| Output field | Description |
| --- | --- |
| rows | List of rows returned from the SQL execution. |
| rows\_affected | Reports the number of rows inserted, updated, or deleted from the SQL string. When running `SELECT` statements, this will return nil. When executing a DDL (for example, creating a table), the value 0 will be returned. |

---
