---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-drive.md
description: >-
  Set up Google Drive as a data pipeline source to extract and sync records from
  CSV and Parquet files into your destination.
---

# Configure Google Drive as your data pipeline source

Set up Google Drive as a data pipeline source to extract and sync records into your destination. This guide includes connection setup, pipeline configuration, and key behavior for working with `.csv` and `.parquet` files stored in Google Drive folders.

## Google Drive features supported

The following features are supported when using Google Drive as a data pipeline source:

- Extract and sync data from `.csv` and `.parquet` files in Drive folders
- Support for full and incremental sync through file detection
- Field-level selection for data extraction
- Field-level data masking

## Google Drive prerequisites

You must have the following configuration and access:

- A Google account with access to the required Drive folders
- OAuth or service account credentials for authentication
- Folder paths and file patterns for the files to sync

## Connect to Google Drive

Complete the following steps to connect to Google Drive as a data pipeline source. This connection enables the pipeline to extract and sync records from files in your Drive.

Connect to Google Drive

1. Select **Create > Connection** or press C twice.
   
2. Search for `Google Drive` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
   ![Google Drive connection setup](/assets/connect-to-drive.DZvES6xE.png)_Google Drive_
   
4. Use the **Location** drop-down to select the project where you plan to store the connection.
   
5. Select an **Authentication type**:
   
   - **OAuth 2.0**: Use this method to authenticate with a Google user account.
   - **Service account**: Use this method to authenticate using a service account JSON key from your Google Cloud Project.
6. Configure the following additional fields based on your **Authentication type**:
   
   **OAuth 2.0**
   
   No additional fields are required. Workato authenticates the connection when you sign in with Google.
   
   **Service account**
   
   - Enter the **GCP project service account email**.
   - Paste the **Private key** associated with the service account.
   - Optional. Enter a **User email** to impersonate a specific user. If left blank, Workato accesses the service account's Drive.
   
7. Optional. Expand **Advanced settings** and select **Requested permissions**.
   
8. Optional. Use a **Custom OAuth profile** if you manage OAuth settings externally.
   
9. Click **Sign in with Google** and complete the OAuth consent flow.
   

## Configure the pipeline

Complete the following steps to configure Google Drive as your data pipeline source:

1. Select **Create > Data pipeline** or press C+I.
   
2. Enter a name for the data pipeline in the **Data pipeline name** field.
   
   ![Data pipeline setup](/assets/set-up-pipeline.Cxx6hIk2.png)_Data pipeline setup_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the data pipeline.
   
4. Click **Start building**.
   
5. Click the **Extract new/updated records from source app** trigger. This trigger defines how the pipeline retrieves data from the source application.
   
   ![Configure the Extract new/updated records from source app trigger](/assets/choose-source-app.B2OOUpgY.png)_Configure the Extract new/updated records from source app trigger_
   
6. Use the **Your Connected Source Apps** drop-down menu to select **Google Drive**.
   
7. Choose the Google Drive connection you plan to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
   ![Choose a Google Drive connection](/assets/choose-google-drive-connection.hKyEAU86.png)_Choose a Google Drive connection_
   
8. Click **Add object** to configure files you plan the pipeline to monitor and sync.
   
   ![Add Google Drive objects](/assets/select-drive-objects.CiwmqgJ1.png)_Add Google Drive objects_
   
9. Enter the folder path to monitor in the **Source Folder path** field. The pipeline monitors this folder and fetches files that match your filename pattern.
   
   ![Configure file settings](/assets/configure-file-settings-source.CVFjze4d.png)_Configure file settings_
   
   > **NESTED FOLDER LIMITATION**
   > 
   > The Google Drive connector doesn't fetch files from nested subfolders. It only monitors and fetches files located directly within the folder specified in the **Source Folder path** field.
   > 
   > If your pipeline expects to include files in subfolders, move those files to the top-level folder. Support for nested folders in Google Drive is planned for a future update.
   
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
    
    Click **Fetch schema** to retrieve the schema from the reference file.
    
15. Review the schema to ensure it matches your expected table structure. The schema preview includes the columns from your source file along with the following system-generated columns:
    
    - `_file`: The name of the source file each row originated from.
    - `_line`: The line or row number of each record within the source file.
    
    ![Review schema](/assets/review-schema-s3.BXKIKDpo.png)_Review schema_
    
16. Configure how rows are merged in the destination table in the **Choose a merge strategy** field. Workato supports the following merge strategies:
    
    - **Upsert**: Inserts new rows and updates existing rows. The **Merge method** field appears when you choose **Upsert**. You can select one or more columns to use as the primary key for the destination table. The pipeline uses the system-generated `_file` and `_line` columns as a composite primary key if you leave **Merge method** blank.
    - **Append only**: Inserts all rows without attempting to match or update existing records. The pipeline doesn't match on a key and doesn't update existing rows when you choose **Append only**.
17. Click **Review object** to confirm your setup. This screen displays your file settings, file type-specific options, and merge details.
    
    ![Review object](/assets/review-object-s3.s4_ztQhU.png)_Review object_
    
18. Enter an **Object name**. This name defines the destination table name.
    
19. Click **Finish** to save the object configuration.
    
20. Review and customize the schema for each selected object. The pipeline automatically fetches an object's schema when you select it. This ensures the destination matches the source.
    
    Expand an object to view associated fields. Keep all fields selected to extract all available data, or deselect specific fields to exclude them from data extraction and schema replication.
    
21. Optional. Configure field-level data protection. After you expand an object, choose how to handle each field:
    
    - **Replicate as is** (default): Data values at the source are replicated identically to the destination.
    - **Hash**: Hash sensitive data values in the column before syncing to your destination.
    
    ![Configure field-level data protection](/assets/configure-field-data-s3.OQuIyiFP.png)_Configure field-level data protection_
    
22. Click **Add object** again to add more objects using the same flow. You can repeat this step to include multiple Google Drive objects in your pipeline.
    
23. Use the **Choose how to handle schema changes** drop-down menu to select a schema drift handling option:
    
    - **Auto-sync new fields**: Automatically detects and syncs new fields added in the source.
    - **Block new fields**: Keeps the schema fixed after the pipeline starts. You must add new fields manually. This option may cause the destination to fall out of sync if the source schema updates.
    
    Refer to [Schema replication and schema drift management](/en/data-orchestration/data-pipeline-recipe/concepts#schema-drift) for more information.
    
24. Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from Google Drive to the destination.
    
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

The Google Drive connector reads `.csv` and `.parquet` files stored in specified folders. These files define the structure and data that the pipeline extracts and syncs to your destination.

Workato infers the schema and data types from the selected reference file. Workato treats date and date-time values as strings for `.csv` files. Transform these fields to the appropriate data type in the destination after the load completes.

All matched files must maintain the same column structure and data format to ensure accurate schema mapping.
