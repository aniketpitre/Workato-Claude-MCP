---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-cloud.md
description: >-
  Set up Google Cloud Storage as a data pipeline source to extract and sync
  records from CSV and Parquet files into your destination.
---

# Configure Google Cloud Storage as your data pipeline source

Set up Google Cloud Storage as a data pipeline source to extract and sync records into your destination. This guide includes connection setup, pipeline configuration, and key behavior for working with `.csv` and `.parquet` files stored in GCS buckets.

## Google Cloud Storage features supported

The following features are supported when using Google Cloud Storage as a data pipeline source:

- Extract and sync data from `.csv` and `.parquet` files in GCS buckets
- Support for full and incremental sync through file detection
- Field‑level selection for data extraction
- Field‑level data masking

## Google Cloud Storage prerequisites

You must have the following configuration and access:

- A Google Cloud account with access to storage buckets that contain `.csv` or `.parquet` files
- A Google service account with permissions to list and read objects
- Folder paths and file patterns for the files to sync

## Connect to Google Cloud Storage

Complete the following steps to connect to Google Cloud Storage as a data pipeline source. This connection allows the pipeline to extract and sync records from your storage buckets.

Refer to [How to connect to Google Cloud Storage](/en/connectors/google_cloud_storage#how-to-connect-to-google-cloud-storage-on-workato) to learn how to create a Google service account and download the private key.

Connect to Google Cloud Storage

1. Select **Create > Connection** or press C twice.
   
2. Search for `Google Cloud Storage` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
   ![Google Cloud Storage connection setup](/assets/connect-to-google-cloud.BVL2jDgO.png)_Google Cloud Storage_
   
4. Use the **Location** drop-down to select the project where you plan to store the connection.
   
5. Select **Cloud** in the **Connection type** field, unless you need to connect through an on-prem group.
   
6. Enter your Google Cloud **Project identifier**. You can find this in the Google Cloud Console.
   
7. Enter the **GCS Project service account email**. This is the email associated with your Google service account.
   
8. Paste the **Private key** from your service account JSON file. You must include the full key, from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----`.
   
9. Optional. Use the **Restrict to bucket** field to limit access to specific buckets. Enter a comma-separated list such as `bucket-1,bucket-2`.
   
10. Optional. Expand **Advanced settings** and select **Requested permissions (OAuth scopes)**.
    
11. Click **Sign in with Google** to authenticate and complete the connection setup.
    

## Configure the pipeline

Complete the following steps to configure Google Cloud Storage as your data pipeline source:

1. Select **Create > Data pipeline** or press C+I.
   
2. Enter a name for the data pipeline in the **Data pipeline name** field.
   
   ![Data pipeline setup](/assets/set-up-pipeline.Cxx6hIk2.png)_Data pipeline setup_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the data pipeline.
   
4. Click **Start building**.
   
5. Click the **Extract new/updated records from source app** trigger. This trigger defines how the pipeline retrieves data from the source application.
   
   ![Configure the Extract new/updated records from source app trigger](/assets/choose-source-app.B2OOUpgY.png)_Configure the Extract new/updated records from source app trigger_
   
6. Use the **Your Connected Source Apps** drop-down menu to select **Google Cloud Storage**.
   
7. Choose the Google Cloud Storage connection you plan to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
   ![Choose a Google Cloud Storage connection](/assets/choose-google-cloud-connection.CjWMyhO2.png)_Choose a Google Cloud Storage connection_
   
8. Click **Add object** to configure the files the pipeline monitors and syncs.
   
   ![Add Google Cloud Storage objects](/assets/select-storage-objects.DzHcfaAJ.png)_Add Google Cloud Storage objects_
   
9. Enter the folder within the bucket to monitor in the **Source Folder path** field. The pipeline monitors this folder and fetches files that match your filename pattern.
   
   ![Configure file settings](/assets/configure-file-settings-source.CVFjze4d.png)_Configure file settings_
   
10. Use the **File type** drop-down menu to select the file format to extract. Workato supports the following file types:
    
    - **CSV**: Extract data from `.csv` files. Requires additional file type settings configuration.
    - **Parquet**: Extract data from `.parquet` files. Schema and data types are inferred directly from the file.
11. Define which files to fetch using a pattern in the **Filename pattern** field. Use wildcards, such as `orders_*`, to include multiple files. The file extension is appended automatically based on the **File type** you select.
    
12. Click **Fetch matching files** to preview files matching the defined pattern.
    
13. Select a **Reference file** to define the schema for your destination table.
    
14. Configure **File type settings**:
    
    **CSV**
    
    1. Use the **Header line** drop-down menu to indicate whether your CSV contains a header line. Select **Yes** if the CSV contents include a header line that shouldn't be parsed as data.
       
    2. Use the **Column delimiter** drop-down menu to select the character used to separate column values within each CSV line. Defaults to **Comma**.
       
    
    **Parquet**
    
    Parquet files include embedded schema information, so no additional file type settings are required. Workato reads the schema and data types directly from the reference file.
    
15. Click **Fetch schema** to load and preview columns from the reference file.
    
16. Review the schema to ensure it matches your expected table structure. The schema preview includes the columns from your source file along with the following system-generated columns:
    
    - `_file`: The name of the source file each row originated from.
    - `_line`: The line or row number of each record within the source file.
    
    ![Review schema](/assets/review-schema-s3.BXKIKDpo.png)_Review schema_
    
17. Configure how rows are merged in the destination table in the **Choose a merge strategy** field. Workato supports the following merge strategies:
    
    - **Upsert**: Inserts new rows and updates existing rows. The **Merge method** field appears when you choose **Upsert**. You can select one or more columns to use as the primary key for the destination table. The pipeline uses the system-generated `_file` and `_line` columns as a composite primary key if you leave **Merge method** blank.
    - **Append only**: Inserts all rows without attempting to match or update existing records. The pipeline doesn't match on a key and doesn't update existing rows when you choose **Append only**.
18. Click **Review object** to confirm your setup. This screen displays your file settings, file type-specific options, and merge details.
    
    ![Review object](/assets/review-object-s3.s4_ztQhU.png)_Review object_
    
19. Enter an **Object name**. This name defines the destination table name.
    
20. Click **Finish** to save the object configuration.
    
21. Review and customize the schema for each selected object. The pipeline automatically fetches an object's schema when you select it. This ensures the destination matches the source.
    
    Expand an object to view associated fields. Keep all fields selected to extract all available data, or deselect specific fields to exclude them from data extraction and schema replication.
    
22. Optional. Configure field-level data protection. After you expand an object, choose how to handle each field:
    
    - **Replicate as is** (default): Data values at the source are replicated identically to the destination.
    - **Hash**: Hash sensitive data values in the column before syncing to your destination.
    
    ![Configure field-level data protection](/assets/configure-field-data-s3.OQuIyiFP.png)_Configure field-level data protection_
    
23. Click **Add object** again to add more objects using the same flow. You can repeat this step to include multiple Google Cloud Storage objects in your pipeline.
    
24. Use the **Choose how to handle schema changes** drop-down menu to select a schema drift handling option:
    
    - **Auto-sync new fields**: Automatically detects and syncs new fields added in the source.
    - **Block new fields**: Keeps the schema fixed after the pipeline starts. You must add new fields manually. This option may cause the destination to fall out of sync if the source schema updates.
    
    Refer to [Schema replication and schema drift management](/en/data-orchestration/data-pipeline-recipe/concepts#schema-drift) for more information.
    
    Schema drift management is currently not supported for file-based pipelines. Support for automatic schema updates is planned for a future release.
    
25. Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from Google Cloud Storage to the destination.
    
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

The Google Cloud Storage connector reads `.csv` and `.parquet` files stored in buckets you specify. These files define the structure and data the pipeline extracts and syncs to your destination.

Workato infers the schema and data types from the selected reference file. Workato treats date and date-time values as strings for `.csv` files. Transform these fields to the appropriate data type in the destination after the load completes.

All files matched by the file pattern must maintain the same column structure and data format to ensure accurate schema mapping.
