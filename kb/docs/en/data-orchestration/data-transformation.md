---
url: 'https://docs.workato.com/en/data-orchestration/data-transformation.md'
description: >-
  Learn how data transformation works in Workato with ETL and ELT patterns for
  normalizing, aggregating, enriching, and cleaning data.
---

# Data transformation

Data transformation converts data from one format, structure, or representation to another to meet specific requirements or objectives. This process manipulates, enriches, cleans, or restructures data, making it suitable for analysis, storage, presentation, or exchange.

Perform data transformation between the extraction and load steps of ETL or transform data after loading it to the destination in ELT.

## ELT (Extract, Load, Transform)

Use custom SQL query actions with database or data warehouse connectors to execute transformations on data already loaded into destination systems. Workato orchestrates this process by passing the SQL query to the destination system, which executes it and returns the outcome.

## ETL (Extract, Transform, Load)

Leverage Workato's [data orchestration](https://www.workato.com/platform/data-orchestration?utm_source=docs&utm_medium=referral&utm_campaign=data-orchestration) capabilities to perform transformations directly within the platform using SQL transformations or SQL collection. Workato's services execute the transformations on the data, providing the output within the recipe that you can forward to various downstream destinations.

## Example business use cases

In various business scenarios, data transformation plays a crucial role in optimizing and preparing data for effective use. The following are key examples:

### Normalization

Normalization involves ensuring data consistency and eliminating redundancy by organizing data into a standard format or structure. This step is vital for maintaining uniformity across datasets, which simplifies analysis and reporting.

### Aggregation

Aggregation combines data from multiple sources, including file systems, applications, and databases. This consolidated data can then be sent to a specific destination for analysis or reporting purposes, providing a comprehensive view of the business metrics.

### Enrichment

Enrichment enhances data by adding additional information, attributes, or derived values from external sources. This process improves the quality and value of the data, making it more informative and actionable.

### Conversion

Conversion is the process of changing data from one data type, format, or encoding to another. Examples include converting text to numeric formats or transforming CSV files to JSON format. This step ensures compatibility and usability of the data across different systems.

### Validation and cleaning

Validation and cleaning involve verifying the integrity, accuracy, and completeness of data. It includes removing or correcting errors, inconsistencies, or outliers to ensure the data meets predefined standards or criteria required to maintain a high quality of data.

### Reverse ETL

Reverse ETL refers to re-syncing data from data warehouses back to source applications after applying data standardization transformations. This approach ensures that the source applications have the most updated and standardized data for operational use.

## Further exploration

To delve deeper into data transformation, explore the following sections that cover specific techniques and tools:

### Transformation techniques

Learn how to use Workato's built-in formulas for data manipulation and transformation tasks. For more complex needs, discover how to leverage custom code for data transformations tailored to your specific requirements. [Explore more](/en/data-orchestration/how-to/data-transformation/transformation-techniques) about transformation techniques.

### Using SQL in Transformations

Explore how to perform data transformations using SQL, including an overview of SQL transformations and SQL collection methods. You can use SQL queries to execute complex transformations directly on your database or data warehouse. [Learn more](/en/data-orchestration/data-transformation/sql-transformations/sql-based) about leveraging SQL for your data transformation needs.

---

---
url: >-
  https://docs.workato.com/en/data-orchestration/how-to/data-transformation/transformation-techniques.md
description: >-
  Learn the data transformation techniques in Workato, including built-in
  formulas, custom code in Ruby, Python, or JavaScript, and SQL.
---

# Transformation techniques

Effective data transformation is crucial for preparing your data to meet specific business requirements. Workato provides various methods to transform data efficiently and accurately. This section introduces you to the different transformation techniques available, ensuring you can choose the approach for your needs.

## Built-in formulas for simple transformations

Workato offers a wide range of built-in formulas suitable for performing simple data transformations. These formulas simplify common data manipulation tasks, allowing you to quickly prepare your data for further processing or analysis.

The following data types are supported:

- [String](/en/formulas/string-formulas)
  
- [Integer or number](/en/formulas/number-formulas)
  
- [Date or datetime](/en/formulas/date-formulas)
  
- [List](/en/formulas/array-list-formulas)
  
- [Complex data types](/en/formulas/complex-data-types).
  

## Custom code transformations

For more complex transformation needs, Workato supports custom code transformations. This feature allows you to write custom scripts to handle specific data manipulation tasks that are not covered by built-in formulas. You can use the following languages:

- [Ruby](/en/connectors/ruby-snippets-by-workato)
- [Python](/en/connectors/python)
- [JavaScript](/en/connectors/javascript)

## SQL-based transformation

Workato enables you to perform SQL-based transformations on your data. This method is powerful for integrating with database connectors and leveraging the full capabilities of SQL. For more information, refer to our [SQL-based transformations](/en/data-orchestration/data-transformation/sql-transformations/sql-based) section.

---

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

---
