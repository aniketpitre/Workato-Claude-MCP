---
url: 'https://docs.workato.com/en/connectors/snowflake/replicate-schema.md'
description: >-
  The Replicate schema action in the Snowflake connector lets you alter a
  destination table so its columns and data types match a source schema.
---

# Snowflake - Replicate schema action

This action inspects the schema of data source against a table in Snowflake, and alters the table as required to match the source schema and column data types.

It is typically used to prepare the destination table before:

- [Replicating Rows](/en/connectors/snowflake/replicate) into Snowflake
  
- [Bulk loading from an external stage](/en/connectors/snowflake/bulk-load-to-table-from-stage) into Snowflake
  

## How it works

- If the specified destination table does not exist, it will be created in Snowflake automatically.
- Workato will compare the source data's schema against the destination Snowflake table.
- Any columns that exist in the source data but not in the destination table will be added to the destination table with DDL Commands (`ALTER TABLE`).
- New columns will follow the data type that was provided (applies only to [Schema](#schema) source type)
- Columns are added, not removed. If a column exists in the destination table but not in the source data, no action will be taken.
- The ordering of columns will follow the source data exactly.

## Inputs

### Table name

Select the destination table in Snowflake. You can select from a list of existing tables in Snowflake, or enter a table name in text.

> **Best Practice for Table Names**
> 
> If entering the table name in text, note that they are case sensitive and we recommend using UPPERCASED names.
> 
> Table names are case-sensitive as we apply double-quotes around them (see [double-quoted identifiers](https://docs.snowflake.com/en/sql-reference/identifiers-syntax.html#double-quoted-identifiers)). This gives you flexibility to use special characters in your table names if needed.
> 
> We recommend applying uppercase to the table names for ease of querying, as your Snowflake users can write queries using case-insensitive unquoted identifiers. This works because Snowflake stores and [resolves identifiers](https://docs.snowflake.com/en/sql-reference/identifiers-syntax.html#label-identifier-casing) in uppercase.
> 
> #### Examples
> 
> | Table name | SQL queries on Snowflake |
> | --- | --- |
> | MyTable | `select * from MyTable; // will not work` `select * from "MyTable"; // OK` |
> | MYTABLE | `select * from MyTable; // OK` `select * from "MYTABLE"; // OK` |

### Source type

Select the source data type (CSV or Schema).

### CSV schema

This field set will be shown if [Source type](#source-type) is **CSV**.

The data type of replicated columns using CSV schema is `VARCHAR`.

| Fields | Description |
| --- | --- |
| CSV data | Use a datapill of CSV data that **must have a header row**. |
| Column separator | Select the delimiter of the CSV data (default: comma) |
| Quote character | Select the character used to quote the CSV cell values (default: Double quote) |

### Schema

This field set will be shown if [Source type](#source-type) is **Schema**.

Schemas definitions can be obtained using Workato's inbuilt connectors, such as [Salesforce - Get object schema action](/en/connectors/salesforce/database-syncs#get-object-schema-action). You can also use [Custom Actions](/en/developing-connectors/custom-actions#custom-actions) to retrieve schema definitions from compatible API sources.

| Fields | Description |
| --- | --- |
| Schema source list | Input a list datapill. [Learn more about list input](/en/features/list-management#list-batch-action) |
| Column name | Map the field name to be used as the column name in your table. |
| Column type | Map the field type to be used as data type for the columns in the table. Leave blank to use `VARCHAR` for all the columns in the table. |

## Optional Inputs

### Column case

#### Upcase (recommended)

Upcasing column names is recommended as it allows your Snowflake users to write queries without worrying about column casing and improves the experience when querying for data. This works because Snowflake stores and [resolves identifiers](https://docs.snowflake.com/en/sql-reference/identifiers-syntax.html#label-identifier-casing) in uppercase.

This action creates columns with [double-quoted identifiers](https://docs.snowflake.com/en/sql-reference/identifiers-syntax.html#double-quoted-identifiers) so that field names containing non-standard characters (e.g. special characters, blank spaces, ASCII, etc) are faithfully replicated.

#### Preserve original

If set to **Preserve original**, SQL queries will need to reference columns using exact casing.

> **PRESERVE ORIGINAL APPLIES TO ALL COLUMNS**
> 
> The **Preserve original** setting also requires column names specified in the [Exclude columns](#exclude-columns) and [Key column](#key-columns) fields to be case-sensitive.

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

### Exclude columns

Specify which columns to exclude from the replication, each on a new line.

> **LIMITATIONS**
> 
> **Exclude columns** is subject to the following limitations:
> 
> - If you set **Retain column casing** to **Yes**, then you must specify the exact column name casing in this field.
>   
> - If you previously replicated the table, and now want to exclude certain columns, you will need to drop the table first and re-run this action. This is because this action will not drop columns from existing tables.
>   

### Key columns

Specify which keys to apply the primary key constraint.

> **LIMITATIONS**
> 
> **Key columns** is subject to the following limitations:
> 
> - If you set **Retain column casing** to **Yes**, then you must specify the exact column name casing in this field.
>   
> - If you previously replicated the table, and now want to set certain columns as primary key, you will need to drop the table first and re-run this action. This is because this action will not alter existing columns in tables.
>   

## Output

| Output | Description |
| --- | --- |
| Number of columns altered | Specifies the number of columns altered in the Snowflake table |

---
