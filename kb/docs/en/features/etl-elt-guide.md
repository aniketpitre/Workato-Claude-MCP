---
url: 'https://docs.workato.com/en/features/etl-elt-guide.md'
description: >-
  Learn how to build ETL and ELT recipes in Workato to extract, transform, and
  load data from sources into a data warehouse or data lake.
---

# Data orchestration - ETL/ELT

Extract, Transform, and Load (ETL) and Extract, Load, and Transform (ELT) are processes used in data integration and data warehousing to extract, transform, and load data from various sources into a target destination, such as a data warehouse or a data lake.

This guide will take you through sample recipes with explanations, that represent practical use cases of ELT/ETL.

## Bulk vs Batch

Bulk/Batch actions/triggers are available throughout Workato. Bulk processing gives you the ability to process large amounts of data in a single job, especially suited for ETL/ELT. Batch processing is restricted by batch sizes and memory constraints, and are generally less suitable in the context of ETL/ELT.

## Extract, Transform, and Load (ETL)

ETL begins with the extraction phase, where data is sourced from multiple heterogeneous sources, including databases, files, APIs, and web services. This raw data is then subjected to a transformation phase (cleansing, filtering, etc.) and finally loaded into a target system, typically a data warehouse.

### Sample ETL Recipe

Refer to the [sample ETL recipe](https://app.workato.com/recipes/20464353?st=238620a97a2c7d4fd3598992e5c53fe77415524a10f426b2f023213fdc628628) for a working example.

![ETL Recipe](/assets/ETL.DEQA7rdr.png)_Sample ETL Recipe_

#### Recipe Breakdown

The sample ETL recipe is a setup of how you can extract data from an on-prem data source ([SQL Server](/en/connectors/mssql)), merge it together with a product catalog stored in [Workato FileStorage](/en/features/workato-filestorage#workato-filestorage) and load this transformed output into a data warehouse ([BigQuery](/en/connectors/bigquery#how-to-connect-to-bigquery-on-workato)). Additionally, Workato file streaming capabilities allows you to transfer data without having to worry about time or memory constraints. This recipe serves as a general guide when building ETL recipes, and performs basic transformations on data extracted from an on-prem data source before loading them into a data warehouse.

##### Setup

This recipe does not require any additional steps behind the scenes.

1. This recipe triggers on a schedule everyday at 0030. This trigger should be customized to your use case.
   
2. Used **[Generate on-prem file URL](/en/connectors/on-prem-files/generate-on-prem-file-url)** to prepare an on-prem location for the subsequent files to be loaded to.
   
3. Used **[Export query result (bulk)](/en/connectors/mssql/export-query-result)** to extract the required Sales data from SQL Server, into the on-prem location specified in the previous step.
   
   - Loads data into the on-prem file created earlier
4. Used **[Download an on-prem file](/en/connectors/on-prem-files/download-file-action)** to retrieve the Sales data from the on-prem location that was specified earlier.
   
   - Retrieves the CSV content from the on-prem file created earlier
5. Used **[Query data using SQL Transformations](/en/features/sql-transformations-query-setting#configure)** to merge the Sales data with Product data retrieved from [Workato FileStorage](/en/features/workato-filestorage).
   
   - Merge Sales and Product Data to produce a transformed output, appropriate for the business requirement
6. Used **[Load data into BigQuery](/en/connectors/bigquery/load_data)** to load the transformed data into a Data Warehouse.
   
   - Final loading of the transformed output into a data warehouse

* * *

## Extract, Load, and Transform (ELT)

Similar to ETL, ELT starts with the extraction phase, where data is extracted from various sources. ELT focuses on loading the extracted data into a target system such as a data lake or distributed storage. Once the data is loaded, transformations occur within the target system.

### Sample ELT Recipe

Refer to the [sample ELT recipe](https://app.workato.com/recipes/20464660?st=048710e3309391e4c3817c31d9810923835278661267275188fcad92add00269) for a working example.

![ELT Recipe](/assets/ELT.CBr1Iwcz.png)_Sample ELT Recipe_

#### Recipe Breakdown

The sample ELT recipe is a setup of how you can extract data from a cloud data source (Salesforce) into a data warehouse (Snowflake). This recipe serves as a guide when building ELT recipes, and performs the basic functionality of extracting bulk data from cloud data sources and loading them into a database.

##### Setup

- You should have set up an external stage on Snowflake with the necessary permissions. Refer to the Snowflake [CREATE STAGE](https://docs.snowflake.com/en/sql-reference/sql/create-stage) documentation for more information.

1. Create a new recipe, using **Export new/updated records (Bulk)** as the trigger.
   
   - Configure the trigger according to your use case
   - **Bulk actions** are suited for extracting large amounts of data in a single job
2. Used **[S3 Upload file (streaming)](/en/connectors/s3/action-upload-file)** action to upload the extracted CSV file contents to designated S3 bucket.
   
   - Action streams the data extracted to the designated S3 bucket
3. Used **[Snowflake Replicate Schema](/en/connectors/snowflake/replicate-schema)** action to create/update an new/existing table.
   
   - This step is optional. If you have an existing table that matches the schema of the staged data, this step is not necessary
   - Replicate schema ensures that the schema of the destination table in Snowflake exists and/or has an appropriate schema matching the source data.
4. Used **[Bulk load data to a table from an external stage](/en/connectors/snowflake/bulk-load-to-table-from-stage)** to load data from staged files to an existing table.
   
   - Loads data from staged file setup in the previous step into an existing table using the `COPY` command
5. > **Data Transformation**
   > 
   > This recipe does not show how transformation can be done in Snowflake. Data transformations can happen after loading data into a table, or even before. Refer to the Snowflake [Querying data in staged files](https://docs.snowflake.com/en/user-guide/querying-stage) documentation for more information.

---
