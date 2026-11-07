---
url: 'https://docs.workato.com/en/connectors/databricks/run-custom-sql.md'
description: >-
  The Run custom SQL action in the Databricks connector lets you run DML and DDL
  statements such as INSERT, UPDATE, SELECT, DELETE, CREATE, and DROP.
---

# Databricks - Run custom SQL action

This action lets you send a SQL string to you Databricks instance for execution. It can be used to run Data Manipulation Language (DML) statements like `INSERT`, `UPDATE`, `SELECT` and `DELETE`, as well as Data Definition Language (DDL) commands, like `CREATE`, `ALTER` and `DROP`.

![Run custom SQL action](/assets/databricks-run-custom-sql.BOQnu6Jx.png)_Run custom sql action_

This action is not optimized for easy configuration. For SELECT statements with a large number of columns, use the [Select rows using custom SQL](/en/connectors/databricks/select-rows-custom-sql-action) action instead.

* * *

## Input

To use this action, configure the following input fields.

- SQL
  
- Provide the SQL query, including meaningful column aliases. The query is used to generate the output datatree. To do this, the SQL is executed when you provide it. Use bind variables (for example,`id = :id`) and the parameter field to parameterize inputs. You must manually define the schema when you use bind variables.
  
  > **CLAUSES TO AVOID**
  > 
  > Avoid using restrictive clauses like `LIMIT` or `TOP(N)` in your SQL.
  

- Parameters
  
- This field is used in conjunction with your `WHERE` condition. First, declare the named bind variables in your `WHERE` input. Next, assign values to these variables using this input field. Parameter values can be static or datapills. Select the closest corresponding data type that your database is expecting for the bind variable.
  
- Output fields
  
- Use this field to define the columns returned in your query. Workato does this dynamically, but you can use this field to override any columns in case of errors. The name of the fields defined here must match the column names in your query exactly.
  

* * *

## Output

This action generates the following output.

- rows
  
- A JSON array of objects. Each object describes one row of the selected data.
  
- rows\_affected
  
- The number of rows added/updated.
  
- rows\_count
  
- The number of rows returned.
  

## Numeric precision behavior in Databricks

Databricks stores `FLOAT` values using 4-byte IEEE 754 single-precision floating-point format. This format represents approximate numeric values and supports approximately seven significant digits of precision.

Databricks stores the closest representable floating-point value if you insert a value with more than seven significant digits. This can cause the stored value to differ slightly from the inserted value.

For example:

```sql
INSERT INTO table_name (float_col)
VALUES (11.123456789);
```

Databricks stores an approximated value because `FLOAT` can't represent the full decimal precision of the input.

Use a fixed-precision type such as the following to store exact decimal values:

```sql
DECIMAL(18,9)
```

Use `DOUBLE` only when approximate precision is acceptable.

---
