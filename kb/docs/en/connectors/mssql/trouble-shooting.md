---
url: 'https://docs.workato.com/en/connectors/mssql/trouble-shooting.md'
description: >-
  Troubleshoot common SQL Server recipe errors in Workato, including timeouts,
  connection failures, and other database design-time issues.
---

# SQL Server - Troubleshooting

During the design stage of recipes, errors are bound to happen. Here are some more common ones relating to databases that we've seen so we decided to compile them into a list! [Check out our troubleshooting section as well for more help.](/en/recipes/recipe-job-errors) If it still doesn't work or you cant find your particular error over here, contact our customer support and they would be more than happy to help!

## Recipe design-time errors

### Timeouts

Workato employs [timeouts on jobs and actions](/en/recipes/recipe-job-errors#timeouts) when they take too long to execute. When working with databases, this could be a common occurrence since queries and stored procedures may too long to respond. When this happens, consider doing the following:

##### Action timeouts (One specific step times out)

- Limiting the number of rows returned further
- Introducing indexes in your database
- Optimizing custom SQL queries (i.e. eliminating unnecessary joins)

##### Job timeouts (One entire run of a recipe times out)

- Separating recipes and using [Recipe functions](/en/connectors/recipe-functions) to trigger workflows
- Use asynchronous calls when calling recipe functions
- Eliminating unnecessary actions

### Unable to connect to existing database

When your database connection returns an error when you try to connect, here are some possible reasons:

- On-prem agent is inactive (when using an on-prem agent) and needs to be [restarted](/en/on-prem/agents/run).
- Credentials to your database have changed. Contact your database administrator for help.
- Your database server does not accept network requests from Workato or the server that has our OPA installed. Configure your network access control to allow access to Workato or our OPAs.

## Logic errors

### Infinite loops

Infinite loops can occur in Workato when actions inside a recipe trigger the recipe yet again. This is not exclusive to databases. [Here are some ways you can detect and solve them](/en/recipes/infinite-loops). When building recipes that are triggered on new rows in a table as well as inserting rows into that same table i.e. performing some data enrichment or data transformation on existing data, here are some ways to prevent infinite loops from occurring:

- Creating a column in your table that denotes whether that same column as been processed by Workato (detailed further in our infinite loop documentation)
- Creating separate tables for raw unprocessed data and transformed data

### Multiple copies of the same record

When using insert actions, job runs that raise errors but have completed the insert row action step will reinsert rows when the job is repeated. This could result in multiple copies of the same record being inserted. Consider using upsert actions that can first search for an existing record before updating one if found or inserting a new record. Find out different use cases and when to use either in our [best practices](/en/connectors/databases/best-practices#using-update-insert-and-upsert-actions).

### Missing values

SQL server allows you to validate new data before inserting them into tables to ensure data integrity using `CONSTRAINTS`. Constraints on data can be defined in SQL server itself when tables are created or altered and are used to make sure data integrity is maintained. You may not be aware of these constraints when designing a recipe. For example, a column that has a UNIQUE constraint cannot be guaranteed until an actual job is run. During recipe run-time, errors will be raised when these constraints are violated. The following screenshot shows a job error when no input is given for a field that has a `PRIMARY KEY` constraint:

![Common-error-missing-values](/assets/Common-error-missing-values.CZ1Jzu97.png)

Here are some possible reasons and fixes for missing values:

- Your primary key column is not auto-incrementing. Alter the column to be an identity column which auto-increments after every insert
- The column has an `unique` constraint and results duplicate values being rejected. Consider using the upsert action to update record instead of inserting a new one.
- The datapill entered during recipe run-time returned a `NULL` value. When this was inserted in a column with `NOT NULL` constraint, an error was thrown. [More info here.](/en/recipes/recipe-job-errors#missing-required-fields-at-run-time) Consider adding logical checks for `NULL` values and passing default values in when need. This can be accomplished with [Workato's formula mode.](/en/formulas/formula-mode)

---
