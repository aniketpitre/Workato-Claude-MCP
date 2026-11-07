---
url: >-
  https://docs.workato.com/en/data-orchestration/data-transformation/sql-transformations/sql-based.md
description: >-
  Learn how to perform SQL-based transformations in Workato using SQL
  Transformations and SQL Collection with database connectors.
---

# SQL-based transformations

Workato enables you to perform SQL-based transformations on your data and integrate with database connectors using our in-house applications [SQL Transformations](#sql-transformations) and [SQL Collection](#sql-collection-by-workato).

## SQL Transformations

[SQL Transformations](/en/features/sql-transformations) is a powerful tool you can use to apply transformations on bulk data using SQL (structured query language) queries.

SQL Transformations provides you with tools to perform large-volume and complex transformations on data extracted from multiple different sources. SQL Transformations uses a streaming mechanism to fetch data from various sources. This enables you to manipulate data using simple SQL queries. SQL Transformation is natively integrated with FileStorage, allowing you to store your output data as files and use them across jobs or different recipes.

### Example recipe: Extract Salesforce accounts, transform data, and load to Snowflake using SQL Transformations

This recipe extracts new or updated accounts from Salesforce, filters out all accounts below a specific monetary value, and loads the filtered records to a Snowflake table.

![Extract, transform, and load recipe](/assets/di-salesforce-snowflake-transformation.DH8hZT78.png)_Extract data from Salesforce, transform, and load to Snowflake_

#### Recipe walkthrough

1. Use the **Export new/updated accounts** trigger to export New/updated accounts in bulk from Salesforce.
   
2. Query the bulk CSV data using the SQL Transformations **Query data** action. Provide a custom SQL query to perform transformations on the data.
   
3. Use the **Upload file to internal stage** action to pass the transformed data directly to an internal stage in Snowflake.
   
   > **STREAMING**
   > 
   > All the preceding recipe steps use streaming to pass the large volume data through the workflow.
   

### Features

SQL Transformations supports the following operations:

- Query data from multiple sources within the same action.
- Fetch and transform millions of records by connecting to various bulk sources.
- High performance in running queries and producing output datasets that can complete transformation in seconds.
- Use complex select queries that involve joins and other SQL functions.

Learn more about [SQL Transformations](/en/features/sql-transformations).

## SQL Collection by Workato

[SQL Collection by Workato](/en/data-orchestration/data-transformation/sql-transformations/sql-collection) provides you with tools to manipulate data in batches. You can use SQL Collection to aggregate and query related data across multiple systems, such as databases, applications, and web services.

SQL Collection is an effective tool for incoming data that uses batch increments and has a low volume. You can use SQL collections to create lists (similar to tables) for data coming from each source. You can then run queries in a separate action to manipulate the data across these sources.

> **LIMITATIONS**
> 
> The lists you create using SQL Collection by Workato and the associated query output exist only within the time period of the job and cannot be used across jobs or recipes.

### Example recipe: Extract Salesforce accounts, transform, and load to Snowflake using SQL Collection

This recipe demonstrates how to extract new or updated accounts from Salesforce, filter out all accounts below a specific monetary value, and load the filtered records into a Snowflake table.

![Extract, transform, and load recipe](/assets/di-salesforce-snowflake-transformation-sql-collection.BuFaj7lB.png)_Extract Salesforce accounts, transform the data, and load to Snowflake_

#### Recipe walkthrough

1. Use the **New/updated accounts** in Salesforce batch trigger to fetch new/updated accounts from Salesforce in batch.
   
2. Use the **Create accounts list** action to create a list of account records in SQL Collections.
   
3. Define SQL queries using the **Query lists** SQL Collections action to manipulate the accounts list.
   
4. Use the **Upsert batch of rows** action to load the output array into a table in Snowflake.
   

Learn more about [SQL Collection by Workato](/en/data-orchestration/data-transformation/sql-transformations/sql-collection).
