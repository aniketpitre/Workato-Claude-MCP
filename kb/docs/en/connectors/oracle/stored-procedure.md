---
url: 'https://docs.workato.com/en/connectors/oracle/stored-procedure.md'
description: >-
  The Execute stored procedure action in the Oracle connector lets you run a
  stored procedure or function in your database with dynamic input parameters.
---

# Oracle - Execute stored procedure action

## Execute stored procedure

This action lets you execute any stored procedure or functions saved in your database instance. Stored procedures from packages are not supported in this action. They can be written to accept input parameters and perform actions on these input parameters. Workato's `Execute stored procedure` action is able to pick up on parameter inputs and allows you to dynamically input these parameters directly from your workflow.

Using stored procedures are a great way to improve recipe efficiency and balance load between Workato and your database. [Find out more in our best practices section how to use stored procedures to make your recipes more efficient.](/en/connectors/databases/best-practices#using-custom-sql-and-stored-procedures)

![Execute stored procedure rows action](/assets/stored-procedure.cv8TpHOt.png)_Execute stored procedure rows action_

### Stored procedure

Select a stored procedure to execute. This can be done either by selecting from the pick list, or toggling the input to text mode and providing the full stored procedure name. When working with overloaded stored procedures, you are given multiple stored procedures with its `sub_program_id` in brackets next to each.

> **RETURNING TABLE TYPE**
> 
> This action does not support stored procedures that return table types.

![Execute stored procedure rows action](/assets/overloaded-stored-procedure.CNhXm5lo.png)_Each overloaded stored procedure displays with its sub\_program\_id in brackets next to the name_

> **TIP**
> 
> To find out the different sub\_program\_ids for an overloaded stored procedure, use the following query in your DBMS.
> 
> ```sql
> SELECT position, argument_name, in_out, data_type,
>          data_length, data_precision, data_scale, char_length, object_name, subprogram_id
>          FROM SYS.ALL_ARGUMENTS where object_name = [stored_procedure_name]
> ```
> 
> where `[stored_procedure_name]` is the name of the overloaded stored procedure.

### Input parameters

Provide any input parameters required for the selected stored procedure.

### Output

Datasets returned from stored procedures in Oracle are not returned in this action.

---
