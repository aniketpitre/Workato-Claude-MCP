---
url: 'https://docs.workato.com/en/connectors/jdbc/insert.md'
description: Insert multiple rows into a table using the JDBC connector.
---

# JDBC - Insert rows (batch) action

The **Insert rows** batch action inserts multiple rows into a table in JDBC.

You can use this action to add batches of records to a database table in a single request. Batch inserts improve performance when you process large datasets.

> **VERSION REQUIREMENT**
> 
> This action requires **On-prem agent (OPA) version 31.0 or later**.

## Input

| Input field | Description |
| --- | --- |
| Table name | Select the table to insert rows into. Choose a table from the pick list or enter the full table name. Some databases enforce case-sensitive table names. |
| Return primary keys | Select **Yes** to return primary keys for the inserted rows in the action output. Select **No** to improve performance when you don't need primary keys. |
| Rows | Provide a list of rows to insert into the selected table. Map a list datapill to the **Rows source list**, then map datapills to the corresponding **Rows fields**. |

## Output

| Output field | Description |
| --- | --- |
| Keys | Primary keys generated for the inserted rows. Returned when **Return primary keys** is set to **Yes**. |

---
