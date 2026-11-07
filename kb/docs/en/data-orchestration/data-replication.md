---
url: 'https://docs.workato.com/en/data-orchestration/data-replication.md'
description: >-
  Learn how Workato handles data replication with change data capture, schema
  replication, scalability, and bulk and batch processing.
---

# Data replication

Workato provides data flow from source to destination with strategic loading and high-volume data handling capabilities.

## Data replication key features

- Change Data Capture (CDC) with triggers
  
- Workato's triggers are configured to capture data changes swiftly, ensuring minimal impact and maximum efficiency in the evolution of your data. This feature is crucial for maintaining up-to-date data replication in real-time or near-real-time scenarios.
  
- Schema replication
  
- Workato can replicate schemas from source systems to destinations without defining destination schemas manually. This simplifies the setup process and ensures that the data structure is maintained during replication.
  
- Scalability
  
- The platform can scale elastically based on demand, providing the necessary backend resources to handle high-volume data loads.
  
- Bulk/Batch processing
  
- Workato supports both bulk and batch processing, which is essential for handling large volumes of data efficiently. Bulk processing allows for large amounts of data to be processed in a single job, which is particularly suited for ETL/ELT processes.

---

---
url: >-
  https://docs.workato.com/en/data-orchestration/data-transformation-capabilities.md
description: >-
  Learn how Workato transforms data with ETL and ELT patterns using formulas,
  custom code, and SQL-based transformations.
---

# Data transformation

Data transformation is the process of converting data from one format, structure, or representation into another to meet specific requirements or objectives. It involves manipulating, enriching, cleaning, or restructuring data to make it suitable for analysis, storage, presentation, or exchange.

You can perform data transformation between the extraction and load steps of (ETL) or transform data after the data is loaded to the destination (ELT).

Workato supports both ELT and ETL patterns:

- ELT
  
- Use custom SQL query actions with database or data warehouse connectors to execute transformations on data already loaded into destination systems. Workato orchestrates this process by passing the SQL query to the destination system, which executes it and returns the outcome.
  
- ETL
  
- Leverage Workato's data orchestration capabilities to perform transformations directly within the platform using SQL transformations or SQL collection. Workato's services execute the transformations on the data, providing the output within the recipe that can be forwarded to various downstream destinations.
  

Example business use cases:

- **Normalization**: Ensure data consistency and eliminate redundancy by organizing data into a standard format or structure.
  
- **Aggregation**: Combine data from multiple sources, including file systems, applications, and databases before sending it to a specific destination for analysis or reporting purposes.
  
- **Enrichment**: Enhance data by adding additional information, attributes, or derived values from external sources.
  
- **Conversion**: Convert data from one data type, format, or encoding to another, such as from text to numeric or from CSV to JSON.
  
- **Validation and cleansing**: Verify the integrity, accuracy, and completeness of data and remove or correct errors, inconsistencies, or outliers to ensure your data meets predefined standards or criteria.
  
- **Reverse ETL**: Re-sync data from data warehouses to source applications after applying data standardization transformations.
  

Workato provides the following data transformation options:

- [Built-in formulas for simple transformations](#formulas)
- [Custom code transformations](#custom-code)
- [SQL-based transformations](#sql)

## Built-in formulas for simple transformations

Workato offers a wide range of built-in formulas suitable for performing simple data transformations.

The following data types are supported:

- [String](/en/formulas/string-formulas)
- [Integer or number](/en/formulas/number-formulas)
- [Date or datetime](/en/formulas/date-formulas)
- [List](/en/formulas/array-list-formulas)
- [Complex data types](/en/formulas/complex-data-types).

## Custom code transformations

Workato offers support for custom code transformations, including Ruby, [Python](/en/connectors/python), and [JavaScript](/en/connectors/javascript).

## SQL-based transformation

Workato enables you to perform SQL-based transformations on your data and integrate with database connectors using our in-house applications [SQL Transformations](#sql-transformations) and [SQL Collection](#sql-collection-by-workato).

### SQL Transformations

[SQL Transformations](/en/features/sql-transformations) is a powerful tool you can use to apply transformations on bulk data using SQL (structured query language) queries.

SQL Transformations provides you with tools to perform large-volume and complex transformations on data extracted from multiple different sources. SQL Transformations uses a streaming mechanism to fetch data from various sources. This enables you to manipulate data using simple SQL queries. SQL Transformation is natively integrated with FileStorage, allowing you to store your output data as files and use them across jobs or different recipes.

#### Example recipe: Extract Salesforce accounts, transform data, and load to Snowflake using SQL Transformations

This recipe extracts new or updated accounts from Salesforce, filters out all accounts below a specific monetary value, and loads the filtered records to a Snowflake table.

![Extract, transform, and load recipe](/assets/di-salesforce-snowflake-transformation.DH8hZT78.png)_Extract data from Salesforce, transform, and load to Snowflake_

##### Recipe walkthrough

1. Use the **Export new/updated accounts** trigger to export New/updated accounts in bulk from Salesforce.
   
2. Query the bulk CSV data using the SQL Transformations **Query data** action. Provide a custom SQL query to perform transformations on the data.
   
3. Use the **Upload file to internal stage** action to pass the transformed data directly to an internal stage in Snowflake.
   
   > **STREAMING**
   > 
   > All the preceding recipe steps use streaming to pass the large volume data through the workflow.
   

#### Features

SQL Transformations supports the following operations:

- Query data from multiple sources within the same action.
- Fetch and transform millions of records by connecting to various bulk sources.
- High performance in running queries and producing output datasets that can complete transformation in seconds.
- Use complex select queries that involve joins and other SQL functions.

Learn more about [SQL Transformations](/en/features/sql-transformations).

### SQL Collection by Workato

[SQL Collection by Workato](/en/features/collection) provides you with tools to manipulate data in batches. You can use SQL Collection to aggregate and query related data across multiple systems, such as databases, applications, and web services.

SQL Collection is an effective tool for incoming data that uses batch increments and has a low volume. You can use SQL collections to create lists (similar to tables) for data coming from each source. You can then run queries in a separate action to manipulate the data across these sources.

> **LIMITATIONS**
> 
> The lists you create using SQL Collection by Workato and the associated query output exist only within the time period of the job and cannot be used across jobs or recipes.

#### Example recipe: Extract Salesforce accounts, transform, and load to Snowflake using SQL Collection

This recipe demonstrates how to extract new or updated accounts from Salesforce, filter out all accounts below a specific monetary value, and load the filtered records into a Snowflake table.

![Extract, transform, and load recipe](/assets/di-salesforce-snowflake-transformation-sql-collection.BuFaj7lB.png)_Extract Salesforce accounts, transform the data, and load to Snowflake_

##### Recipe walkthrough

1. Use the **New/updated accounts** in Salesforce batch trigger to fetch new/updated accounts from Salesforce in batch.
   
2. Use the **Create accounts list** action to create a list of account records in SQL Collections.
   
3. Define SQL queries using the **Query lists** SQL Collections action to manipulate the accounts list.
   
4. Use the **Upsert batch of rows** action to load the output array into a table in Snowflake.
   

Learn more about [SQL Collection by Workato](/en/features/collection).

---
