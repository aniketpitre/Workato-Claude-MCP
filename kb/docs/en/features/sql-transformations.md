---
url: 'https://docs.workato.com/en/features/sql-transformations.md'
description: >-
  SQL Transformations lets you transform large volumes of data from multiple
  sources using SQL SELECT statements with joins and other functions.
---

# SQL Transformations

SQL Transformations is a powerful and efficient tool you can use to apply transformations to large volumes of data using structured query language (SQL) queries.

It is an in-house utility that provides you with the necessary tools to perform large-volume and complex transformations on data extracted from multiple different sources. This utility enables you to use simple SQL SELECT statements to bind the various large-volume data sets and transform them to get the data you need.

See it in action

[Video](https://www.youtube.com/embed/rv-RQmTLc9A)

  

> **FEATURE AVAILABILITY**
> 
> SQL Transformations is available on specific pricing plans. Refer to your pricing plan and contract to learn more.

## Key features

- Query data coming in from any number of data sources.
- No limitation on the volume of data you can fetch and transform, or on the data output produced. This means you can handle millions of records with ease.
- High performance in running queries and producing output data sets. SQL Transformations can perform complete transformation in seconds.
- Supports the use of complex select queries that involve joins and other SQL functions.

* * *

## Usage inspiration

Additionally, SQL Transformations enables users to run complex queries to handle the following situations:

- Periodically fetch new accounts information from Microsoft Dynamics 365 and merge it with additional lookup data stored as a file in Workato FileStorage and load the output directly to a BigQuery data warehouse table.
  
- Export large volume sales details from Salesforce, enrich this data by joining it with product details available as a file within Workato FileStorage, filter and fetch only opportunities that are above a specific value as output data set, and load it to an on-prem system.
  
- Fetch complete employee data extract from the on-prem system, filter and get details of employees with a specific job title and store the output data set in Workato FileStorage as a file for future report generation purposes.
  

* * *

> **Sample use cases**
> 
> Refer to our guides for step-by-step instructions on how to use SQL Transformations for the following use cases:
> 
> - [Change data capture](/en/features/sql-transformations-cdc)
> - [Data enrichment](/en/features/sql-transformations-data-enrichment)
> - [Data validation and cleansing](/en/features/sql-transformations-data-validation-cleansing)

## How does it work?

SQL Transformations utilizes the Workato FileStorage system under the hood for temporary data storage of incoming large volume content stream before running transformations on it. Since it is deeply integrated with Workato FileStorage, it can scale to store and process any volume of data in a fast and efficient manner.

* * *

## Who can use this feature?

Once the connector is provisioned, it is available to all roles within the same workspace. Do note that at present, all files that are queried from, or created from the query output and stored within Workato FileStorage at a workspace level, can be accessed by all roles within the specific workspace/tenant as well.

> **Feature availability**
> 
> SQL Transformations is generally available. Contact your Customer Success Manager to enable it in your workspace.
> 
> ![SQL Transformations utility connector](/assets/connector.CK8hICQ-.png)_SQL Transformations utility connector_

* * *

## Encryption

SQL Transformations is built as a service to Workato FileStorage system, hence it follows same encryption principles as FileStorage. Refer to [FileStorage encryption](/en/features/workato-filestorage#encryption) for more information.

* * *

## Limitations

SQL Transformations has the following quotas:

- Each data source used in a query has a maximum size of 10 GB.
- Workato FileStorage [storage quotas](/en/features/workato-filestorage#limitations) apply when you store the output data in Workato FileStorage.

* * *

## Data retention

The following data are temporarily retained in SQL Transformations:

- The incoming data from different data sources other than FileStorage
- The transformed query output data

These data are all automatically purged from primary and backup drives within 4 days. You can store your data in FileStorage to enable longer data retention and still use the data in SQL Transformations.

## Read next

To use this connector, read the following guides:

1. [Connector overview](/en/features/sql-transformations-actions)
2. [Set up your data source](/en/features/sql-transformations-data-source-setting)
3. [Set up your query](/en/features/sql-transformations-query-setting)
4. [Configure your output](/en/features/sql-transformations-output-setting)
5. [Output fields](/en/features/sql-transformations-output-fields)

See the following guides for usage inspiration and instructions related to your specific use case.

- [Transform Avro and Parquet files](/en/features/sql-transformations-avro-parquet)
- [Change data capture](/en/features/sql-transformations-cdc)
- [Data validation and cleansing](/en/features/sql-transformations-data-validation-cleansing)
- [Data enrichment](/en/features/sql-transformations-data-enrichment)

---
