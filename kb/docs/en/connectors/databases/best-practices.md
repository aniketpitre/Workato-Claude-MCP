---
url: 'https://docs.workato.com/en/connectors/databases/best-practices.md'
description: >-
  Best practices for building Workato recipes with database connectors, covering
  recipe design patterns, table design, unique keys, and data validation.
---

# Database Connector Best Practices

We compiled a few of our best practices that make your life easier when developing workflows with Workato by causing less bugs and time wasted.

We've split up these into two overarching patterns:

- [Recipe design patterns](#recipe-design-patterns)
- [Database design patterns](#database-design-patterns)

* * *

## Applicable Databases

This guide is generally applicable to all database connectors, including [SQL Server](/en/connectors/mssql) and [Oracle](/en/connectors/oracle).

* * *

## Recipe Design Patterns

When building recipes that use database connectors, we recommend keeping the following in mind:

- [Reduce database actions](#reduce-database-actions)
- [Implement error handling](#implement-error-handling)
- [Split workflows into separate recipes](#split-complex-workflows-into-separate-recipes)

Following these guidelines will help reduce load on your database and make your Workato assets easier to manage.

### Reduce Database Actions

Keep in mind that every Workato action can create additional load on your database. To minimize strain and make your recipes more sustainable, we recommend:

- Using **Upsert** actions instead of **Select** or **Update/Insert**
- Using **Batch** actions to aggregate data and send it to the database
- Using stored procedures or custom SQL functions to transform data before sending it to Workato

### Implement Error Handling

Error handling is an important part in the recipe design process. Check out [this guide](/en/recipes/best-practices-error-handling) for more detailed info.

### Split Complex Workflows Into Separate Recipes

It may be tempting to create a single recipe that accomplishes everything, but these recipes quickly become hard to maintain. We recommend splitting workflows into multiple recipes to ensure this doesn't happen.

Splitting workflows into multiple recipes can:

- **Improve recipe maintenance**
- **Make troubleshooting issues easier**, allowing you to quickly trace errors to specific recipes or steps.
- **Reduce redundancy in recipe steps**. By using [Recipe functions](/en/connectors/recipe-functions) and [API recipes](/en/api-mgmt/api-recipes/), you can re-use a recipe in another recipe.

#### Batch Versus Single Row Triggers And Actions

With the ability to break down complex workflows through recipe functions, the decision to use batch or single row actions are often a matter of business requirements and design considerations. While batch triggers/actions reduce the load on your servers and can decrease job duration, there exists a trade-off as batch actions that do fail, fail on a batch level.

When examined, most workflows with applicable batch triggers/actions can be accomplished in three ways:

| Method | Benefits/Drawbacks | Business use case example |
| --- | --- | --- |
| The use of a batch trigger, followed by a batch action and using Workato's repeat step for any single row actions. | Using this method is the most efficient across all metrics. Since Workato employs a step-by-step (synchronous) process within each job run so any error that causes the run to stop also prevents the following steps from being executed for the entire batch. In cases where it only makes sense for the following actions to be executed contingent on the success of the initial steps, this could be useful behavior. Since even a single record causes the whole batch to stop, some thought should go into striking a balance between efficiency and stopping too many records from being processed during a failed job run. One solution would be to toggle batch size. | If we were to pull batches of new leads from a database for batch inserts into Salesforce, we could follow this up with emails to individuals on the sales team with links to the leads newly created on Salesforce directly. In cases where our information flowing in from Salesforce raised an error during the batch insert action, no email would be sent out to our sales team with links that didn’t work or were empty! We can now safely make adjustments to our recipe to accommodate this error before repeating the job. |
| The use of a single row trigger, followed by a single row actions | Using this method is the least efficient across all metrics, especially for triggers/actions that work with large numbers of records. Workato employs a step-by-step (synchronous) process within job runs so any error that causes the run to stop also prevents the following steps from being executed. Some cases call for this behavior where we would want to fix our recipe before letting the recipe run on to further steps. This is different from the batch trigger version as it only stops the job runs for those that raise errors compared to an entire batch. In time sensitive business use cases where all new rows should be processed as soon as possible, this might be the correct design choice. | Time sensitive job runs such as new orders populating a database table as new rows, the following actions may be crucial in ensuring the timely delivery of your product to your customer. Having entire batches of orders being stopped due to a single failed record may result in lost revenue for you. In this scenario, single row triggers/actions may be the way to minimize disruptions to your company's operations. **Another alternative to consider would be to reduce the batch size of your batch actions.** |
| The use of a batch trigger, followed by all required batch actions. A separate recipes can be used with a single row action and single row actions. | Using this method is allows records to be processed concurrently. This allows errors to be contained at a recipe level and only affect the steps that follow after it. In cases where steps are independent of each other and one need not be completed before the other can begin, this might be the correct solution. This fits in with more complex workflows where separating recipes based on their data types and business needs makes recipes easier to maintain and efficient as mentioned earlier. | New records in a table could signify new customer sign-ups for a free trial for your product. You hope to add them in batches to a drip campaign as well as send their details individually over to your sales team for follow-ups. Given both cases are not dependent on each other and both can be accomplished without diminishing the other's effectiveness, this workflow could and should be accomplished as separate recipes to minimize the impact if failed job runs on business. |

### Using Update, Insert, and Upsert Actions

Choosing between **Update**, **Insert**, and **Upsert** actions can have numerous implications for your recipes and database tables. While upserts can be used to accomplish most actions where update or insert are used, here are some key considerations to keep in mind when choosing one over the other.

When building, keep in mind that:

- **Upsert performs better in certain cases where records should be unique based on a single column**. This reduces the number of steps required in a recipe where a search would have had to been performed to decide whether to update a record or insert a new record.
- **Upserts are useful in situations where duplicate rows wouldn't be created.** If a job fails and is re-run, a previously inserted row might result in duplicate rows. Using an **Upsert** action would prevent this.
- **Updates allow you to update rows that might not all be identified using a unique key.** Rows to update identified using a range of parameters, i.e. updating all records `WHERE revenue >= 1000000`
- **Upserts may hide potential bugs or issues**. For example, a recipe triggering when an order is changed in Salesforce to update the record of the order in your database might not be suitable for the upsert action. Since a record of the order should have already been in the system, the lack of one to update should be noted and the job stopped with a report error instead.

#### Using Custom SQL And Stored Procedures

Workato allows you to write your own custom SQL queries in two ways:

1. Using the **Select rows using custom SQL** action, if supported by your database connector
2. Using the **Run custom SQL** action, if supported by your database connector

You can perform a wide range of actions on your database using these actions. Since writing your own queries might get messy in terms of the columns returned, remember to manage your step output by giving your returned columns **meaningful aliases** and **only returning the columns that you need**. This makes maintaining your recipe easier and more readable for others as well.

Custom SQL allows you to reduce the number of actions calling your database within a recipe. Having less actions means less load on your servers and greater time efficiency as data can be join and transformed directly on your servers before sending Workato the final result. If you're comfortable with SQL, consider using custom SQL to perform basic data transformations rather than doing so on Workato. Custom SQL also allows you to do Data Definition Language (DDL) - a far larger range of operations such as creating, dropping, and altering tables (if your connection has the correct permissions).

Besides custom SQL, Workato also supports the execution of stored procedures that are defined in your database. More than just queries, stored procedures are more commonly used to execute complex transactions or loads. In cases like these, Workato acts as the orchestration tool to execute the stored procedure at the right time. Another great feature of stored procedures is the versatility available through input parameters while still retaining control over the scope of what your recipes can do in your database.

#### Using Collections For Data Processing

In cases where custom SQL and stored procedures might not be suitable such as the transformation and aggregating of data from different sources, Workato offers the use of collections for basic transformations. Collections can be used for data cleaning, data enrichment and aggregation through easy to use commands in SQL. Collections are versatile tools that can be used as last steps before placing data inside data warehouses, data lakes or exporting to other applications.

* * *

## Database Design Patterns

- [Designing tables for Workato use](#designing-tables-for-workato-use)
- [Data validation](#data-validation)

### Designing Tables For Workato Use

When looking to make triggers using the **New row** and **New/updated row triggers**, trigger configurations require either:

- A unique key (primary key), OR
- A unique key and sorted column

This is required to ensure your trigger doesn't miss any records.

Use the following guidelines when selecting a trigger table:

- [Unique keys](#unique-keys)
- [Sort columns](#sort-columns)

#### Unique keys

1. An auto incrementing unique integer key should be present in the table that can act as your unique key. In most cases where your table's `primary` key is set to be auto incrementing, this is usable.
2. When this is not the case, one of two solutions can be implemented
   - Finding an existing key that can act as a proxy which is an integer, unique, and auto incrementing
   - Creating a new auto incrementing unique integer key

**How to create a new auto incrementing key**

1. Make sure no other column has been declared as an `IDENTITY` column in your table. (if this has been done so, you may use that directly as your unique integer key
   
2. Enter the following commands to create an new `IDENTITY` column, where \[your\_table\_name\] and \[column\_name\] are placeholders for your table name and new column name respectively
   

```
ALTER TABLE [your_table_name]
  ADD [column_name] INT UNIQUE NOT NULL IDENTITY ;
  
```

3. After this, you should be able to use your new key as a unique column!
   
4. Creating a new `IDENTITY` column in your database backfills all your previous records. Take note of the initial recipe run!
   

#### Sort columns

1. `updated_at` columns within a table should be suitable as the sort column.
2. Failing that, any column that can be sorted based on the time the record was updated can be used.
3. If no column is suitable, an `updated_at` column can be created to fulfill this purpose.
4. This new `updated_at` column in the database table can now be used as a sort column

**How to create an `updated_at` column to sort by**

1. Enter the following commands to create an `updated_at` column, where \[your\_table\_name\] and \[column\_name\] are placeholders for your table name and new column name respectively

```
ALTER TABLE [your_table_name]
add updated_at datetime2
CONSTRAINT DF_myTable_updated_at DEFAULT GETDATE()
```

2. After this, now we need to add this column to trigger and update whenever a record is changed

```
CREATE TRIGGER trg_[your_table_name]_update
 ON [your_table_name]
 AFTER UPDATE
 AS
   UPDATE [your_table_name]
   SET updatedAt = CURRENT_TIMESTAMP
   FROM INSERTED i
   WHERE [your_table_name].ID = i.ID;
```

### Data Validation

Data validation is an important step in database design that makes your data cleaner and also reduces the chances of job errors on Workato. Most databases allow you to create and alter tables to include constraints on data flowing into them. Refer to the following guides to ensure data cleanliness in your database:

- [Oracle](https://docs.oracle.com/cd/B19306_01/server.102/b14200/clauses002.htm)
- [SQL Server](https://docs.microsoft.com/en-us/sql/relational-databases/tables/create-check-constraints?view=sql-server-2017)

Data validation can also be done in a recipe if you aren’t familiar or don't have `ALTER` permissions in your database. Use Workato's formula recipes to catch values that might throw errors in your recipe. Refer to [Formulas](/en/formulas) for more information.

---
