---
url: 'https://docs.workato.com/en/data-orchestration/replication-pipelines.md'
description: >-
  Learn how Workato replication pipelines continuously copy data between systems
  using CDC, schema replication, and bulk and batch processing.
---

# Replication pipelines

Replication pipelines in Workato continuously copy data from one system to another, ensuring data accuracy and consistency. These pipelines support real-time analytics, backups, disaster recovery, and cross-system synchronization, keeping your data current and reliable across platforms.

## Set up a pipeline for replication

You can set up a replication pipeline in Workato with features that ensure efficiency, scalability, and real-time data consistency:

- Change Data Capture (CDC) with triggers
  
- Workato triggers capture data changes quickly and efficiently, which minimizes system impact while keeping data replication up to date in real-time or near-real-time.
  
- Schema replication
  
- Workato replicates schemas from source systems to destinations without manual schema definitions. This maintains data structure integrity and simplifies setup.
  
- Scalability
  
- Workato scales elastically to meet demand and provides the necessary resources to handle high-volume data loads.
  
- Bulk and batch processing
  
- Workato supports bulk and batch processing to handle large data volumes efficiently. Bulk processing moves large datasets in a single job, while batch processing moves incremental updates. Both methods support ETL and ELT workflows.
  

## Schema drift

Schema drift refers to changes in the structure of a dataset over time and typically occurs after you implement a data orchestration process. These changes may include additions, deletions, or modifications of fields, data types, or other schema elements.

Schema drift creates inconsistencies between source and target systems, which can lead to data transformation errors, data loss, or inaccurate analysis if not properly addressed.

### How Workato detects and manages schema drift

Workato detects schema drift through automated schema detection and adaptation. It regularly monitors and validates data structures, sending notifications when schema changes occur. This enables you to intervene manually when necessary to maintain consistency between source and destination systems.

## Replicate schema actions for Snowflake, BigQuery, and SQL Server

Workato supports schema replication for [Google BigQuery](/en/connectors/bigquery), [SQL Server](/en/connectors/mssql/replicate), and [Snowflake](/en/connectors/snowflake/replicate-schema).

### How schema replication works in Snowflake

Schema replication in Workato ensures that the structure of your source data matches the destination table in Snowflake. This process keeps your data pipelines consistent and up to date, even when the source schema changes.

Workato manages schema replication in Snowflake through the following processes:

- Automatic table creation
  
- If the specified destination table does not exist in Snowflake, Workato creates it automatically.
  
- Schema comparison and updates
  
- Workato compares the source schema with the destination Snowflake table. If columns exist in the source but not in the destination, Workato adds the missing columns using DDL commands (`ALTER TABLE`).
  
- Data type consistency
  
- New columns follow the data type provided in the source (applies to schema-based sources).
  
- Non-destructive updates
  
- Workato adds columns but doesn't remove them. If columns exist in the Snowflake destination but not in the source, no changes occur.
  
- Column ordering
  
- Workato maintains the exact column order from the source data in the destination Snowflake table.
  

### Modify a Snowflake table to match a source schema

The [Replicate schema action](/en/connectors/snowflake/replicate-schema) inspects the source data schema and updates the Snowflake table to match.

Complete the following steps to modify a Snowflake table to match a source schema.

1. Go to Workato and configure the **Replicate schema** action for Snowflake.
   
   ![Replicate schema action](/assets/configure-replicate-schema-action.BoQZtYhZ.png)_Configure the Replicate schema action_
   
2. Select the destination table in Snowflake in the **Table name** field. You can select from a list of existing tables in Snowflake, or enter a table name manually.
   
   > **CASE-SENSITIVITY IN TABLE NAMES**
   > 
   > Table names are case-sensitive because Workato applies double-quotes around them. This allows you to use special characters in table names. Refer to the [Double-quoted identifiers](https://docs.snowflake.com/en/sql-reference/identifiers-syntax.html#double-quoted-identifiers) documentation for more information.
   
3. Optional. Select how to format replicated column names in the **Column case** field.
   
4. Choose whether the **Source type** is **CSV** or **Schema**.
   
5. Configure the following schema fields based on your selected data type:
   
   **CSV schema**
   
   - CSV data
     
   - Use a datapill of CSV data with a header row.
     
   - Column separator
     
   - Select the delimiter of the CSV data. The default is comma.
     
   - Quote character
     
   - Select the character used to quote the CSV cell values.
     
   
   **Schema**
   
   - Schema source list
     
   - Input a list datapill. [Learn more about list input](/en/features/list-management#list-batch-action).
     
   - Column name
     
   - Map the source field name to the corresponding column name in Snowflake.
     
   - Column type
     
   - Map the field type to the Snowflake data type. Leave blank to default to `VARCHAR`.
     
   
6. Optional. Enter one or more unique keys to identify duplicate rows in the **Key columns** field.
   
7. Optional. Specify one or more columns to exclude from replication in the **Exclude columns** field.

---
