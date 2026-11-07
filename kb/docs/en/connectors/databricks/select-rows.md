---
url: 'https://docs.workato.com/en/connectors/databricks/select-rows.md'
description: >-
  The Select rows action in the Databricks connector lets you return rows from a
  table that match a WHERE condition, with ordering and quotas.
---

# Databricks - Select rows action

This action enables you to select rows based on certain criteria defined by a `WHERE` condition. Rows from the selected table that match the `WHERE` condition are returned as the output of this action.

![Select rows action](/assets/databricks-select-rows-action.CWUwhE8R.png)_Select rows action_

* * *

## Input

To use this action, configure the following input fields.

- Table name
  
- Select a table from which to select rows. Workato only displays the first 1,000 table names. Enter in the table name if the table you plan to use is not displayed.
  
- WHERE condition
  
- Provide a `WHERE` condition to filter rows. This condition can be as simple as filtering a single record by its `ID`.
  
  ```sql
  ID = 123
  ```
  
  Alternatively, it can be used to select multiple rows based on values in one or more columns.
  
  ```sql
  STATUS = 'closed' and PRIORITY = 1
  ```
  
  Complex `WHERE` conditions with subqueries can also be used. Refer to the [WHERE condition](/en/connectors/snowflake#where-condition) guide for more information.
  
- Parameters
  
- Used in conjunction with your `WHERE` condition to prevent SQL injection. After declaring named bind variables in your `WHERE` input, assign values to these variables using this input field. [Learn more](/en/connectors/snowflake#using-parameters)
  
- Order By
  
- Rows returned from this action can be ordered based on the **Order by** input field. This field is used to change the default ordering of rows from your Databricks database. You can also define the direction of order for each column you wish to order by. The following **Order by** statement orders rows by `priority` in ascending order followed by `created_date` in descending order (latest first).
  
  ```sql
  PRIORITY ASC, CREATED_DATE DESC
  ```
  
- Quota
  
- This input field determines the maximum number of rows to return. The default quota is 100 and capped at a maximum of 50000 rows for a single **Select rows** action.
  
- Offset
  
- This input field gives you the option to fetch only a page of results from the entire results set. For example, to skip the first 100 rows of the selected results set, input `100` to this field. The default is `0`.
  

* * *

## Output

This action generates the following output.

- rows
  
- JSON Array of objects, each object describes one row of the selected data. Workato displays only the first 10 objects.
  
- rows\_count
  
- The number of rows returned.

---

---
url: >-
  https://docs.workato.com/en/connectors/databricks/select-rows-custom-sql-action.md
description: >-
  The Select rows via custom SQL action in the Databricks connector lets you
  return rows from a custom SQL query, with ordering and row quotas.
---

# Databricks - Select rows via custom SQL action

This action lets you select rows based on a custom SQL query. Rows that are returned from the query will be returned as the output of this action.

![Select rows using custom SQL action](/assets/databricks-select-rows-custom-sql.CV-ouydt.png)_Select rows via custom SQL action_

* * *

## Input

To use this action, configure the following input fields.

- SQL
  
- Provide the SQL query you plan to use to select rows. The query is used to generate the output datatree. To do this, the SQL is executed when you provide it. Use bind variables. For example,`ID = :id` and the parameter field to parameterize inputs. You must manually define the schema when you use bind variables.
  
  > **CLAUSES TO AVOID**
  > 
  > Avoid using limit clauses like `LIMIT` or `TOP(N)` in your SQL. This is because the limit to the number of rows returned in the query is based on the value defined in the [Limit input field](#limit). Adding your own limit clause causes the action to fail. Additionally, remove `ORDER BY` clauses from the query and place them in the **Order by** input field.
  
- Parameters
  
- This field is used in conjunction with your `WHERE` condition. First, declare the named bind variables in your `WHERE` input. Next, assign values to these variables using this input field.  
  Parameter values can be static or datapills. Select the closest corresponding data type that your database is expecting for the bind variable.
  
- Order By
  
- Rows returned from this action can be ordered based on the **Order by** input field. This field is used to change the default ordering of rows from your Databricks database.  
  You can also define the direction of order for each column you plan to order by. The following **Order by** statement orders rows by `priority` in ascending order followed by `updated_at` in descending order (latest first).
  
  ```sql
  PRIORITY ASC, UPDATED_AT DESC
  ```
  
- Quota
  
- This input field determines the maximum number of rows to return. The default quota is 100 and capped at a maximum of 50000 rows for a single **Select rows using custom SQL** action.
  
- Offset
  
- This input field gives you the option to skip rows before returning rows from the query expression. For example, to skip the first 100 rows of the selected results set, input `100` to this field. The default is `0`.
  
- Output fields
  
- Use this field to define the columns returned in your query. Workato does this dynamically, but you can use this field to override any columns in case of errors. The name of the fields defined here must match the column names in your query exactly.
  

* * *

## Output

This action creates the following output.

- rows
  
- A JSON array of objects. Each object describes one row of the selected data.
  
- rows\_count
  
- The number of rows returned.

---
