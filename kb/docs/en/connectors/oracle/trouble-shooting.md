---
url: 'https://docs.workato.com/en/connectors/oracle/trouble-shooting.md'
description: >-
  Troubleshoot common Oracle connector errors in Workato, including recipe
  design-time timeouts and database connection failures.
---

# Oracle - Troubleshooting

Errors can occur when designing recipes. This page provides common errors relating to databases. [Check out our troubleshooting section for more help.](/en/recipes/recipe-job-errors) Contact customer support if you can't resolve your errors with the following troubleshooting steps.

## Recipe design-time errors

### Timeouts

Workato employs [timeouts on jobs and actions](/en/recipes/recipe-job-errors#timeouts) when they take too long to execute. When working with databases, this could be a common occurrence since queries and stored procedures may too long to respond. When this happens, consider doing the following:

##### Action timeouts (One specific step times out)

- Limiting the number of rows returned further
- Introducing indexes in your database
- Optimizing custom SQL queries (for example, eliminating unnecessary joins)

##### Job timeouts (One entire run of a recipe times out)

- Separating recipes and using [Recipe functions](/en/connectors/recipe-functions) to join workflows up
- Use asynchronous calls when calling recipes
- Eliminating unnecessary actions

### Unable to connect to existing database

When your database connection returns an error when you try to connect, here are some possible reasons:

- On-prem agent is inactive (when using an on-prem agent) and needs to be [restarted](/en/on-prem/agents/run).
- Credentials to your database have changed. Contact your database administrator for help.
- Your database server does not accept network requests from Workato or the server that has our OPA installed. Configure your network access control to allow access to Workato or our OPAs.

### Error: `Something went wrong` when loading Oracle metadata

Workato may display a `Something went wrong` error when you open or configure Oracle actions like [Select rows](/en/connectors/oracle/select). This happens when Workato attempts to load metadata from Oracle, such as available tables or columns, but can't connect because the Oracle database isn't accepting new connections.

You may see the following message in the OPA logs:

```text
oracle.net.ns.NetException: Listener refused the connection with the following error:
ORA-12516, TNS:listener could not find available handler with matching protocol stack
```

Complete the following steps to resolve the issue:

1. Ask your database administrator to increase the processes and sessions quotas in the Oracle configuration.
   
2. Review the `listener.ora` file to confirm that handlers are properly configured.
   
3. Restart the Oracle listener service to reinitialize available handlers.
   
4. Reduce the number of simultaneous connections to the Oracle database, or optimize connection reuse.
   

## Logic errors

### Infinite loops

Infinite loops can occur in Workato when actions inside a recipe trigger the recipe yet again. This is not exclusive to databases. [Here are some ways you can detect and solve them](/en/recipes/infinite-loops). When building recipes that are triggered on new rows in a table as well as inserting rows into that same table i.e. performing some data enrichment or data transformation on existing data, here are some ways to prevent infinite loops from occurring:

- Creating a column in your table that denotes whether that same column as been processed by Workato (detailed further in our infinite loop documentation)
- Creating separate tables for raw unprocessed data and transformed data

### Multiple copies of the same record

When using insert actions, job runs that raise errors but have completed the insert row action step, reinsert rows when the job is repeated. This could result in multiple copies of the same record being inserted. Consider using upsert actions that can first search for an existing record before updating one if found or inserting a new record. Find out different use cases and when to use either in our [best practices](/en/connectors/databases/best-practices#using-update-insert-and-upsert-actions).

### Missing or invalid values

Oracle allows you to validate new data before inserting it into tables to ensure data integrity using `CONSTRAINTS`. Constraints on data can be defined in Oracle itself when tables are created or altered and are used to make sure data integrity is maintained. You may not be aware of these constraints when designing a recipe. For example, a column that has a UNIQUE constraint cannot be guaranteed until an actual job is run. During recipe run-time, errors are raised when these constraints are violated. The following screenshot shows a job error when no input is given for a field that has a `CHECK` constraint. The error message highlights the check constraint as well as the constraint name (`ROOT.SYS_C008445` in this case) which can be searched for inside the database.

![Common-error-invalid-values](/assets/Common-error-invalid-values.BS0xruHM.png)

Here are some possible reasons and fixes for missing values:

- Your primary key column is not auto-incrementing. Alter the column to be an identity column which auto-increments after every insert
- The column has an `unique` constraint and results duplicate values being rejected. Consider using the upsert action to update record instead of inserting a new one.
- The datapill entered during recipe run-time returned a `NULL` value. When this was inserted in a column with `NOT NULL` constraint, an error was thrown. [More info here.](/en/recipes/recipe-job-errors#missing-required-fields-at-run-time) Consider adding logical checks for `NULL` values and passing default values in when need. This can be accomplished with [Workato's formula mode.](/en/formulas/formula-mode)

---
