---
url: 'https://docs.workato.com/en/connectors/mssql/replicate.md'
description: >-
  The Replicate action in the SQL Server connector inserts or updates rows from
  a list datapill, creating new columns when the input schema changes.
---

# SQL Server - Replicate action

This action updates a selected table in your SQL Server instance. It takes a list datapill as input and inserts or updates them as rows.

Workato will first [detect and compare the schema](#workato-schema-mapper) of the input data and SQL Server table. If they do not match, this action will create new columns in the SQL Server table. This ensures that all the data from your input will be automatically synced in SQL Server, even if there are updates to the input schema.

## Input

| Input | Description |
| --- | --- |
| Table name | Select the table to insert your rows by typing the full table name. SQL Server is case insensitive. |
| Unique keys | Match rows using values from these unique keys. If an existing row is found in the table, it will be updated. Otherwise, a row will be inserted. |
| Rows | Use a list datapill as input. |
| Flatten columns | If your input data is formatted as an object, use this to flatten the object into individual key-value pairs. [Learn more](#when-to-use-flatten). |
| Exclude columns | Select columns from the list datapill to exclude in this replication. Excluded columns will not be added to the table. |

## Output

| Output | Description |
| --- | --- |
| A new table was created | `true` when the provided table name does not exist and is created in the job. `false` otherwise. |
| An existing table was altered | `true` when the new columns were detected and added/altered in the table. `false` otherwise. |
| Number of rows upserted | Number of rows inserted/updated in the table. |

### When to use flatten

If you have data formatted as an object, you may not be able to access nested data directly (for example, nested within a JSON object).

Use this toggle to flatten the object and treat individual key-value pairs as unique columns. This action will only flatten 1 layer of nested data.

Here is an example from a data source.

```json
{
  "ID": 1,
  "NAME": "John Doe",
  "HANDLES": {
    "GITHUB": "johndoe",
    "SLACK": "john"
  }
}
```

An unflattened row would look like this:

| ID | NAME | HANDLES |
| --- | --- | --- |
| 1 | John Doe | `{"github": "johndoe", "slack": "john"}` |

A flattened row will look like this:

| ID | NAME | HANDLES.GITHUB | HANDLES.SLACK |
| --- | --- | --- | --- |
| 1 | John Doe | johndoe | john |

## Workato schema mapper

Each data source (API, Database, and File) has its own schema. To maintain consistency, this action maps each data type from the source to the SQL Server table schema. This mapping is done before creating/updating the SQL Server table.

Input data will be converted to SQL Server data types, based on the mappings defined below.

| Workato type | SQL Server type |
| --- | --- |
| string | nvarchar(max) |
| integer | bigint |
| number | float(53) |
| boolean | bit |
| object | nvarchar(max) |
| date date\_time timestamp | datetime2 Workato will use the timezone defined in the [connection setup](/en/connectors/mssql/introduction#improved-datetime-handling), or use the default SQL Server user account timezone. |

---
