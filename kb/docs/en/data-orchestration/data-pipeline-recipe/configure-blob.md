---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-blob.md
description: >-
  Set up Azure Blob Storage as a data pipeline source to extract and sync
  records from CSV and Parquet files into your destination.
---

# Configure Azure Blob Storage as your data pipeline source

Set up Azure Blob Storage as a data pipeline source to extract and sync records into your destination. This guide includes connection setup, pipeline configuration, and key behavior for working with `.csv` and `.parquet` files stored in Azure Blob containers.

## Azure Blob Storage features supported

The following features are supported when using Azure Blob Storage as a data pipeline source:

- Extract and sync data from `.csv` and `.parquet` files in Blob containers
- Support for full and incremental sync through file detection
- Field-level selection for data extraction
- Field-level data masking

## Azure Blob Storage prerequisites

You must have the following configuration and access:

- An Azure account with Blob Storage containers storing `.csv` or `.parquet` files
- Access to the storage account and container
- Required permissions to read from containers and blobs
- Folder paths and file patterns for the files to sync

## How to connect

Complete the following steps to connect to Azure Blob Storage as a data pipeline source. This connection allows the pipeline to extract and sync records from blob containers.

Connect to Azure Blob Storage

1. Select **Create > Connection** or press C twice.
   
2. Search for `Azure Blob Storage` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
   ![Azure Blob Storage connection setup](/assets/connect-to-blob.q_rP3nXN.png)_Azure Blob Storage_
   
4. Use the **Location** drop-down to select the project where you plan to store the connection.
   
5. Select **Cloud** in the **Connection type** field, unless you need to connect through an on-prem group.
   
6. Enter your Azure **Storage account** name. You can find this value in the **Azure Portal > Storage accounts** section.
   
7. Select the **Connection account type**:
   
   - **Common**: Supports personal, enterprise, and multi-tenant accounts that are not tenant-specific.
     
   - **Organization**: Supports multi-tenant enterprise accounts.
     
   - **Tenant-specific**: Requires you to provide the **Tenant ID** or **Domain**.
     
   
   The default is the **Common** type.
   
8. Go to **Advanced settings** to manage additional configurations based on your connection:.
   
   **Authorization code grant**
   
   Set **OAuth 2.0 authorization code scopes**. Include `Management` to support dynamic webhook triggers through EventGrid. If left blank, the default scopes are `Offline_access`, `Storage`, and `Management`.
   
   **Client credentials grant**
   
   Set **OAuth 2.0 client credentials scopes**. Include `Management` to support dynamic webhook triggers through EventGrid. If left blank, the default scopes are `Storage` and `Management`.
   
9. Enter the **Client ID** from your Azure app registration. Refer to the **Azure Portal > App registrations** section to retrieve it.
   
10. Enter the **Client secret** from **Certificates & secrets** in the Azure Portal.
    
11. Optional. Enter an **Access key** to support the **Generate presigned URL** action. You can find this in the Azure Portal under the **Storage account > Access keys**.
    
12. Click **Sign in with Microsoft**. Authorize the necessary permissions to complete the connection setup.
    

## Configure the pipeline

Complete the following steps to configure Azure Blob Storage as your data pipeline source:

1. Select **Create > Data pipeline** or press C+I.
   
2. Enter a name for the data pipeline in the **Data pipeline name** field.
   
   ![Data pipeline setup](/assets/set-up-pipeline.Cxx6hIk2.png)_Data pipeline setup_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the data pipeline.
   
4. Click **Start building**.
   
5. Click the **Extract new/updated records from source app** trigger. This trigger defines how the pipeline retrieves data from the source application.
   
   ![Configure the Extract new/updated records from source app trigger](/assets/choose-source-app.B2OOUpgY.png)_Configure the Extract new/updated records from source app trigger_
   
6. Use the **Your Connected Source Apps** drop-down menu to select **Azure Blob Storage**.
   
7. Choose the Azure Blob Storage connection you plan to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
   ![Choose an Azure Blob Storage connection](/assets/choose-azure-blob-connection.B7UIENdk.png)_Choose an Azure Blob Storage connection_
   
8. Select the Azure Blob Storage container you plan to monitor in the **Container name** field.
   
   ![Select Azure Blob Storage container](/assets/select-azure-container.DFIl0RHm.png)_Select Azure Blob Storage container_
   
9. Click **Add object** to configure files you plan the pipeline to monitor and sync.
   
10. Enter the folder path within the container in the **Source Folder path** field. The pipeline monitors this folder and fetches files that match your filename pattern.
    
    ![Configure file settings](/assets/configure-file-settings-source.CVFjze4d.png)_Configure file settings_
    
11. Use the **File type** drop-down menu to select the file format to extract. Workato supports the following file types:
    
    - **CSV**: Extract data from `.csv` files. Requires additional file type settings configuration.
    - **Parquet**: Extract data from `.parquet` files. Schema and data types are inferred directly from the file.
12. Define which files to fetch using a pattern in the **Filename pattern** field. Use wildcards, such as `orders_*`, to include multiple files. The file extension is appended automatically based on the **File type** you select.
    
13. Click **Fetch matching files** to preview files matching the defined pattern.
    
14. Select a **Reference file** to define the schema for the destination table.
    
15. Configure file type-specific settings:
    
    **CSV**
    
    1. Use the **Header line** drop-down menu to indicate whether your CSV contains a header line. Select **Yes** if the CSV contents include a header line that shouldn't be parsed as data.
       
    2. Use the **Column delimiter** drop-down menu to select the character used to separate column values within each CSV line. Defaults to **Comma**.
       
    
    **Parquet**
    
    Parquet files include embedded schema information, so no additional file type settings are required. Workato reads the schema and data types directly from the reference file.
    
16. Click **Fetch schema** to load and preview columns from the reference file.
    
17. Review the schema to ensure it matches your expected table structure. The schema preview includes the columns from your source file along with the following system-generated columns:
    
    - `_file`: The name of the source file each row originated from.
    - `_line`: The line or row number of each record within the source file.
18. Configure how rows are merged in the destination table in the **Choose a merge strategy** field. Workato supports the following merge strategies:
    
    - **Upsert**: Inserts new rows and updates existing rows. The **Merge method** field appears when you choose **Upsert**. You can select one or more columns to use as the primary key for the destination table. The pipeline uses the system-generated `_file` and `_line` columns as a composite primary key if you leave **Merge method** blank.
    - **Append only**: Inserts all rows without attempting to match or update existing records. The pipeline doesn't match on a key and doesn't update existing rows when you choose **Append only**.
19. Click **Review object** to confirm your setup. This screen displays your file settings, file type-specific options, and merge details.
    
20. Enter an **Object name**. This name defines the destination table name.
    
21. Click **Finish** to save the object configuration.
    
22. Review and customize the schema for each selected object. The pipeline automatically fetches an object's schema when you select it. This ensures the destination matches the source.
    
    Expand an object to view associated fields. Keep all fields selected to extract all available data, or deselect specific fields to exclude them from data extraction and schema replication.
    
23. Optional. Configure field-level data protection. After you expand an object, choose how to handle each field:
    
    - **Replicate as is** (default): Data values at the source are replicated identically to the destination.
    - **Hash**: Hash sensitive data values in the column before syncing to your destination.
    
    ![Configure field-level data protection](/assets/configure-field-data-s3.OQuIyiFP.png)_Configure field-level data protection_
    
24. Click **Add object** again to add more objects using the same flow. You can repeat this step to include multiple Azure Blob Storage objects in your pipeline.
    
25. Use the **Choose how to handle schema changes** drop-down menu to select a schema drift handling option:
    
    - **Auto-sync new fields**: Automatically detects and syncs new fields added in the source.
    - **Block new fields**: Keeps the schema fixed after the pipeline starts. You must add new fields manually. This option may cause the destination to fall out of sync if the source schema updates.
    
    Refer to [Schema replication and schema drift management](/en/data-orchestration/data-pipeline-recipe/concepts#schema-drift) for more information.
    
26. Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from Azure Blob Storage to the destination.
    
    **Time-based schedule**
    
    1. Select the **Time unit**, such as **Minutes**, **Hours**, or **Days**.
       
    2. Specify the sync interval in the **Trigger every** field.
       
       For example, the pipeline syncs every 6 hours if you select **Hours** as the **Time unit** and enter `6` in the **Trigger every** field.
       
       The minimum interval you can set is 15 minutes.
       
    3. Select a start date for the historical data sync in the **When first started, this pipeline should pick up records from** field. This defines the earliest date from which the pipeline extracts records. The pipeline picks up all available records from the source if you leave this field blank.
       
       You can't change this value after you run the pipeline.
       
    4. Click **Save** to save your progress before you [configure your data pipeline destination](/en/data-orchestration/data-pipeline-recipe/configure-pipeline-destinations#configure‒how‒data‒is‒loaded‒in‒the‒workato‒data‒pipeline).
       
    
    **Cron-based scheduling**
    
    1. Use the **Time unit** drop-down menu to select **Custom schedule**.
       
    2. Enter an expression in the **Cron expression** field using the format:
       
       ```text
       [minute] [hour] [day of month] [month] [day of week]
       ```
       
       The minimum interval for cron schedules is 15 minutes.
       
       For example, enter the following expression to sync every day at 8:00 AM UTC:
       
       ```text
       0 8 * * *
       ```
       
    3. Optional. Select a **Timezone** for the cron expression. Leave blank to use `Etc/UTC`.
       
    4. Select a start date for the historical data sync in the **When first started, this pipeline should pick up records from** field. This defines the earliest date from which the pipeline extracts records. The pipeline picks up all available records from the source if you leave this field blank.
       
       You can't change this value after you run the pipeline.
       
    5. Click **Save** to save your progress before you [configure your data pipeline destination](/en/data-orchestration/data-pipeline-recipe/configure-pipeline-destinations#configure‒how‒data‒is‒loaded‒in‒the‒workato‒data‒pipeline).
       
    

## File schema and processing

The Azure Blob Storage connector reads `.csv` and `.parquet` files stored in containers. These files define the structure and data that the pipeline extracts and syncs to your destination.

Workato infers the schema and data types from the selected reference file and maps them to the destination table. Workato treats date and date-time values as strings for `.csv` files. Transform these fields to the appropriate date or date-time type in the destination after the load completes.

All files processed by the pipeline must maintain the same column structure and data format as the reference file to ensure accurate schema mapping.
