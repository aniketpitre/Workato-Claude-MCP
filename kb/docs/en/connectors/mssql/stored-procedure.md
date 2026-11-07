---
url: 'https://docs.workato.com/en/connectors/mssql/stored-procedure.md'
description: >-
  The Execute stored procedure action in the SQL Server connector lets you run
  stored procedures or functions and pass dynamic input parameters.
---

# SQL Server - Execute stored procedure action

## Execute stored procedure

This action lets you execute any stored procedure or functions saved in your database instance. Stored procedures are user defined processes written directly into your database. They can be written to accept input parameters and perform actions on these input parameters. Workato's `Execute stored procedure` action is able to pick up on parameter inputs and allows you to dynamically input these parameters directly from your workflow.

Using stored procedures are a great way to improve recipe efficiency and balance load between Workato and your database. [Find out more in our best practices section how to use stored procedures to make your recipes more efficient.](/en/connectors/databases/best-practices#using-custom-sql-and-stored-procedures)

## Supported versions

This action is only supported for SQL Server 2012 or newer. It uses a default stored procedure `sp_describe_first_result_set` that is only available from SQL Server 2012 onwards.

![Execute stored procedure rows action](/assets/stored-procedure.Bt-AKjbC.png)_Execute stored procedure rows action_

### Stored procedure

First, select a stored procedure to execute. This can be done either by selecting from the pick list, or toggling the input to text mode and providing the full stored procedure name.

### Input parameters

Next, provide any input parameters required for the selected stored procedure.

### Output

If the selected stored procedures outputs multiple datasets, only the first will be returned in this action. The returned dataset size is limited to 50000 rows.

---
