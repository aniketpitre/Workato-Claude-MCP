---
url: 'https://docs.workato.com/en/connectors/redshift/long-query-custom-sql.md'
description: >-
  The Run long query custom SQL action in the Redshift connector runs DML and
  DDL queries asynchronously within a timeout you configure.
---

# Redshift - Run long query custom SQL action

This action enables you to run custom SQL queries asynchronously within a timeout you configure. You can use this action to execute Data Manipulation Language (DML) statements like `INSERT`, `UPDATE`, and `DELETE`, as well as Data Definition Language (DDL) commands, like `CREATE`, `ALTER`, and `DROP`.

After the custom SQL query begins processing, the action periodically checks if the results are ready for retrieval. The recipe moves to the next step after it retrieves the results successfully.

![Run long query custom SQL action](/assets/run-long-query-sql.zSLahPKN.png)_Run long query custom SQL action_

Use the [Export query results](/en/connectors/redshift/export-query-result) action to retrieve a CSV stream of the results for [SELECT](/en/connectors/redshift/select) actions.

## Input

| Input field | Description |
| --- | --- |
| SQL | Enter a valid SQL query. For example: `SELECT * FROM PUBLIC.ACCOUNTS`. |
| Parameters | Define the fields you plan to include in the list, and assign values to each field. You must declare the named bind variables in your `WHERE` input and assign values to these variables. Parameter values can be static or datapills. Select the closest corresponding data type that your database expects for the bind variable. |
| Timeout limit (minutes) | Set an upper limit for this wait action. The job returns an error if this action takes longer than the timeout you specified. The maximum timeout is `60` minutes. |

## Output

| Output field | Description |
| --- | --- |
| Rows | Returns a list of rows from SQL execution. The fields in this list are defined in the **Output Fields** input field. If you leave this field blank, this row appears in the datatree as an array datapill. |
| Rows affected | Returns the number of rows affected by a DML statement.`0` is returned when executing a DDL action. |
| Row count | Returns the number of rows retrieved. |

---
