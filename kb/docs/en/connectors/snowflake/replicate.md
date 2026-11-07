---
url: 'https://docs.workato.com/en/connectors/snowflake/replicate.md'
description: >-
  The Replicate rows action in the Snowflake connector lets you insert or update
  rows from a list datapill, auto-syncing schema changes.
---

# Snowflake - Replicate rows action

This action updates a selected table in your Snowflake instance. It takes a list datapill as input and inserts or updates them as rows.

Workato will first [detect and compare the schema](#workato-schema-mapper) of the input data and Snowflake table. If they do not match, this action will create new columns in the Snowflake table. This ensures that all the data from your input will be automatically synced in Snowflake, even if there are updates to the input schema.

- Schema detection works by introspecting each of the field values in the Batch input data, and mapping it to a suitable column type. If there are multiple types found, the widest column type will be inferred so as to avoid any loss of precision. If you wish to specify column types created, consider using the [Replicate Schema action](/en/connectors/snowflake/replicate-schema).
  
- If the destination table does not exist, it will be created.
  
- This action doesn't delete existing columns in the destination table, even if the source data no longer contains data for a specific column.
  
- This action will not alter the datatype of existing columns.
  

## Inputs

| Input | Type | Description |
| --- | --- | --- |
| Table name | required | Select the table to insert your rows, or type the full table name. Schema prefix is not required. Table names are case sensitive. We recommend using UPPERCASE for the table name. [Why?](#best-practice-for-table-names). |
| Unique keys | required | Specify the columns that identify a row as unique. If the row exists in the destination, it will be updated. Otherwise, it will be inserted as a new row. |
| Rows | required | Use a list datapill as input. |
| Flatten columns | optional | If your input data is formatted as an object, use this toggle to flatten the object into individual key-value pairs. See the example [below](#when-to-use-flatten). |
| Column case | optional | Decide whether to retain column name casing during replication. We recommend the default option (`Upcase`) as it enables case-insensitive SQL queries. [Why?](#column-case-option) |
| Exclude columns | optional | Specify which columns to exclude from the replication. Leave blank to replicate all columns. |

### Best practice for Table names

If entering the table name in text, note that they are case sensitive and we recommend writing names in **UPPERCASE**.

Table names are case-sensitive as we apply double-quotes around them (see [double-quoted identifiers](https://docs.snowflake.com/en/sql-reference/identifiers-syntax.html#double-quoted-identifiers)). This gives you flexibility to use special characters in your table names if needed.

We recommend applying uppercase to the table names for ease of querying, as your Snowflake users can write queries using case-insensitive unquoted identifiers. This works because Snowflake stores and [resolves identifiers](https://docs.snowflake.com/en/sql-reference/identifiers-syntax.html#label-identifier-casing) in uppercase.

| Table name | SQL queries on Snowflake |
| --- | --- |
| MyTable | `select * from MyTable; // will not work` `select * from "MyTable"; // OK` |
| MYTABLE | `select * from MyTable; // OK` `select * from "MYTABLE"; // OK` |

### When to use flatten

If you have data formatted as an object, you may not be able to access nested data directly (for example, nested within a JSON object).

Use this toggle to flatten the object and treat individual key-value pairs as unique columns.

By default, this action will only flatten 1 level of nested data. You can configure the number of levels to flatten, up to 50.

Here is an example from a data source.

```json
{
  "id": 1,
  "name": "John Doe",
  "handles": {
    "github": "johndoe",
    "slack": "john"
  }
}
```

An unflattened row would look like this:

| ID | NAME | HANDLES |
| --- | --- | --- |
| 1 | John Doe | `{"github": "johndoe", "slack": "john"}` |

A flattened row will look like this:

| ID | NAME | HANDLES\_GITHUB | HANDLES\_SLACK |
| --- | --- | --- | --- |
| 1 | John Doe | johndoe | john |

### Column case option

#### Upcase (recommended)

Upcasing column names is recommended as it allows your Snowflake users to write queries without worrying about column casing and improves the experience when querying for data. This works because Snowflake stores and [resolves identifiers](https://docs.snowflake.com/en/sql-reference/identifiers-syntax.html#label-identifier-casing) in uppercase.

This action creates columns with [double-quoted identifiers](https://docs.snowflake.com/en/sql-reference/identifiers-syntax.html#double-quoted-identifiers) so that field names containing non-standard characters (e.g. special characters, blank spaces, ASCII, etc) are faithfully replicated.

#### Preserve original

If set to Preserve original, SQL queries will need to reference columns using exact casing (see examples below).

#### Examples

```sql
# Given that source data has a key "AccountId"

# When Column_Case is "Upcase" or blank
SELECT AccountId FROM mytable;   // OK
SELECT accountid FROM mytable;   // OK
SELECT "ACCOUNTID" FROM mytable; // OK

# When Column_Case is "Preserve original"
SELECT AccountId FROM mytable;   // will fail
SELECT accountid FROM mytable;   // will fail
SELECT "AccountId" FROM mytable; // OK
```

## Output

The output of this action is a count of the number of rows upserted.

## Workato schema mapper

Each data source (API, Database, and File) has its own schema. To maintain consistency, this action maps each data type from the source to the Snowflake table schema. This mapping is done before creating/updating the Snowflake table.

Input data will be converted to Snowflake data types, based on the mappings defined below.

| Workato type | Snowflake type |
| --- | --- |
| string | [varchar](https://docs.snowflake.net/manuals/sql-reference/data-types-text.html#data-types-for-text-strings) Defaults to maximum length. |
| string(binary) | [binary](https://docs.snowflake.net/manuals/sql-reference/data-types-text.html#data-types-for-binary-strings) |
| date | [date](https://docs.snowflake.net/manuals/sql-reference/data-types-datetime.html#date) |
| date\_time timestamp | [timestamp](https://docs.snowflake.net/manuals/sql-reference/data-types-datetime.html#timestamp) Workato will use the timezone defined in the [connection setup](/en/connectors/snowflake#database-timezone), or use the default Snowflake user account timezone. |
| integer | [number](https://docs.snowflake.net/manuals/sql-reference/data-types-numeric.html#data-types-for-fixed-point-numbers) Precision and scale defaults to (38, 0). |
| number | [double](https://docs.snowflake.net/manuals/sql-reference/data-types-numeric.html#data-types-for-floating-point-numbers) |
| boolean | [boolean](https://docs.snowflake.net/manuals/sql-reference/data-types-logical.html#boolean) |
| object | [variant](https://docs.snowflake.net/manuals/sql-reference/data-types-semistructured.html#variant) |

---
