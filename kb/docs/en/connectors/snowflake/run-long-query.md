---
url: 'https://docs.workato.com/en/connectors/snowflake/run-long-query.md'
description: >-
  The Run long query using custom SQL action in the Snowflake connector runs DML
  and DDL statements asynchronously within a set timeout.
---

# Snowflake - Run long query using custom SQL action

This action allows you to run custom SQL queries asynchronously, within the timeout configured. It can be used to execute Data Manipulation Language (DML) statements like `INSERT`, `UPDATE`, and `DELETE`, as well as Data Definition Language (DDL) commands, like `CREATE`, `ALTER`, and `DROP`.

After the custom SQL query begins processing, Workato checks periodically to see if the query results are ready to be retrieved. When the results have been successfully retrieved, Workato proceeds to the next steps in the recipe.

## Why you should use long queries

When a large dataset is being uploaded (`INSERT`) or updated (`UPDATE`), the action may take a long time to respond. If it exceeds the timeout limit, it will cause the recipe to fail due to a timeout error.

Running the SQL query asynchronously allows you to execute queries on large datasets. The maximum time the action can take is 60 minutes. If the action takes longer than this upper quota, the job will time out.

![Long Query Action](/assets/long-query.CyM5ZXxY.png)_Run long query with custom SQL action_

## Input

| Input field | Description |
| --- | --- |
| SQL | **This field is required**. Provide a valid SQL string to be executed. This SQL string will be executed in your Snowflake instance. If multiple SQL statements are provided, all of them will be executed. However, only results from the last statement will be returned. Make sure each statement is separated by a `;` character. You can map datapills here to execute dynamically changing SQL statements. Remember to wrap datapills in single quotes (`' '`). |
| Parameters | This field is used in conjunction with your SQL statement. First, declare the named bind variables in your WHERE input. Next, assign values to these variables using this input field. Parameter values can be static or datapills. Select the closest corresponding data type that your database is expecting for the bind variable. |
| Timeout limit (minutes) | Set an upper quota for this wait action. The job will return an error if this action takes longer than the specified timeout. The maximum timeout is 60 minutes. |
| Output Fields | Use this input to describe the columns that you are expecting from your SQL statement. If you do not expect any return values or do not need any, you may ignore this input field. |

## Output

| Output field | Description |
| --- | --- |
| Rows | List of rows returned from the SQL execution. The fields in this list are defined by the **Output fields** input field. If left blank, this row will be available in the datatree as an array datapill. |
| Rows affected | Refers to the number of rows that are impacted or modified by the execution of a Data Manipulation Language (DML) statement. When executing a DDL(CREATE), the value `0` will be returned. |
| Row count | Refers to the number of rows returned. |

---
