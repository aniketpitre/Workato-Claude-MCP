---
url: 'https://docs.workato.com/en/data-orchestration/load-data.md'
description: >-
  Load data in batch or bulk into destinations like Snowflake with Workato
  connector actions to insert, update, upsert, and replicate records.
---

# Load data

Load data in [batch](/en/data-orchestration/concepts#batch-operations) or [bulk](/en/data-orchestration/concepts#bulk-operations) into your target destination, such as a data lake or warehouse. Workato supports a variety of design patterns for loading data to different destinations, ensuring data is ready for analysis or reporting. This section guides you through leveraging Workato's data loading capabilities to optimize your data orchestration processes.

## Snowflake connector actions

Workato provides comprehensive support for loading data into Snowflake using various actions. These actions enable you to insert, update, upsert, and delete records efficiently. Explore the following actions for detailed instructions:

- [Select rows batch action](/en/connectors/snowflake/select)
- [Insert row action](/en/connectors/snowflake/insert)
- [Update rows action](/en/connectors/snowflake/update)
- [Upsert rows action](/en/connectors/snowflake/upsert)
- [Delete rows action](/en/connectors/snowflake/delete)
- [Run long query using custom SQL action](/en/connectors/snowflake/run-long-query)
- [Run custom SQL action](/en/connectors/snowflake/run_sql)
- [Export query result action](/en/connectors/snowflake/export-query-result)
- [Upload file to internal stage action](/en/connectors/snowflake/upload-file-to-internal-stage)
- [Bulk load to table from stage action](/en/connectors/snowflake/bulk-load-to-table-from-stage)
- [Replicate rows action](/en/connectors/snowflake/replicate)
- [Replicate schema action](/en/connectors/snowflake/replicate-schema)
- [Merge rows action](/en/connectors/snowflake/merge)

### Sample recipe: Batch load data from Salesforce into Snowflake

This recipe demonstrates Workato's batch-loading capabilities. It exports new leads in batches from Salesforce and loads the data into Snowflake.

![Batch loading into Snowflake](/assets/di-batch-load-into-snowflake.C9Y-046A.png)_Batch load into Snowflake_

#### Recipe walkthrough

1. Configure the **New records batch** trigger in Salesforce to export new leads in batches.
   
2. Upsert the new records by mapping the output datapill of the list of leads from Salesforce in batches to the **Rows source list** input using the **Upsert rows batch** action in Snowflake.
   

## SQL Server connector actions

Workato provides comprehensive support for loading data into SQL Server using various actions. These actions enable you to insert, update, upsert, and delete records efficiently. Explore the following actions for detailed instructions:

- [Select rows batch action](/en/connectors/mssql/select#select-rows)
- [Select rows using custom SQL batch action](/en/connectors/mssql/select#select-rows-using-custom-sql)
- [Insert row action](/en/connectors/mssql/insert#insert-row)
- [Insert rows batch action](/en/connectors/mssql/insert#insert-batch-of-rows)
- [Update rows action](/en/connectors/mssql/update#update-rows)
- [Update rows batch action](/en/connectors/mssql/update#update-batch-of-rows)
- [Upsert row action](/en/connectors/mssql/upsert#upsert-row)
- [Upsert rows batch action](/en/connectors/mssql/upsert#upsert-batch-of-rows)
- [Delete rows batch action](/en/connectors/mssql/delete)
- [Replicate rows batch action](/en/connectors/mssql/replicate)
- [Bulk load from on-prem file action](/en/connectors/mssql/bulk-load-from-on-prem-file)
- [Run custom SQL action](/en/connectors/mssql/run_sql#run-custom-sql)
- [Run long query using custom SQL action](/en/connectors/mssql/run_sql#run-custom-sql-asynchronously)
- [Execute stored procedure action](/en/connectors/mssql/stored-procedure)
- [Export query result action](/en/connectors/mssql/export-query-result)

### Sample recipe: Bulk fetch data from Salesforce and load to on-prem SQL Server

The following example uses bulk fetch to extract sales order data from Salesforce and loads it to an on-premise SQL Server.

![Bulk fetch from Salesforce cloud and load to on-prem SQL Server](/assets/bulk-fetch-from-salesforce.CoLe3CQL.png)_Bulk fetch from Salesforce cloud and load to on-prem SQL Server_

#### Recipe walkthrough

1. Configure the **Export new records in Salesforce (bulk)** trigger to fetch newly created records in bulk from Salesforce as CSV data.
   
2. Load the CSV data to the on-prem folder using the **On-prem files - Upload file** action.
   
3. Generate a URL for the CSV file created in the on-prem systems using the **On-prem files - Generate on-prem file URL** action.
   
4. Map the URL generated in the previous step to the **SQL Server - Bulk load from an on-prem file** action. This action fetches the file from the on-prem folder and loads it into the table directly.
   

### Sample recipe: Bulk load data from SQL Server to Amazon S3

The following example uses bulk load to extract data from SQL Server and loads it to Amazon S3.

![Bulk load data from SQL Server to Amazon S3](/assets/bulk-load-data-from-sql-server-to-amazon-s3.DD9j5fHP.png)_Bulk load data from SQL Server to Amazon S3_

#### Recipe walkthrough

1. Set up a **Scheduler** trigger and determine the frequency for bulk loading the data.
   
2. Use the **Export query result** action in SQL Server to run a custom SQL query on the database and export the results in bulk as a CSV file.
   
3. Map the contents of the file from the previous step to the **Upload file streaming** action in Amazon S3 to stream and upload the data into the cloud store.
   

#### Supported connectors

The following connectors support bulk uploads:

**All file connectors:**

- [On-prem files](/en/connectors/on-prem-files)
- [Workato FileStorage](/en/features/workato-filestorage)
- [SFTP](/en/connectors/sftp)
- [FTP/FTPS](/en/connectors/ftp)
- [Google Drive](/en/connectors/google-drive)
- [Microsoft OneDrive](/en/connectors/onedrive)
- [Microsoft Sharepoint](/en/connectors/sharepoint)
- [Box](/en/connectors/box)
- [Dropbox](/en/connectors/dropbox)
- [BIM 360](/en/connectors/bim360)
- [Egnyte](/en/connectors/egnyte)

**All data lake connectors:**

- [AWS S3](/en/connectors/s3)
- [Azure Blob Storage](/en/connectors/azure_blob_storage)
- [Google Cloud Storage](/en/connectors/google_cloud_storage)

## Incremental loading

Use incremental loading to maintain up-to-date data in the target destination without the overhead of full loads. It involves tracking changes in the source data, often through timestamps, version keys, or triggers, and only loading the data that has been added or modified since the last load. This strategy is essential for real-time data orchestration and minimizing the impact on system resources.

---
