---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-sharepoint.md
description: >-
  Configure Microsoft SharePoint as a data pipeline source to extract and sync
  CSV, Parquet, and Avro files from SharePoint Online document libraries to your
  destination.
---

# Configure Microsoft SharePoint as a data pipeline source

Set up Microsoft SharePoint as a data pipeline source to extract and sync `.csv`, `.parquet`, and `.avro` files from SharePoint Online document libraries into your destination.

Use this guide to set up your Microsoft Entra app, connect SharePoint to Workato, configure the pipeline, and review file handling, sync modes, and limitations.

## Microsoft SharePoint features supported

The following features are supported when you use Microsoft SharePoint as a pipeline source:

- **SharePoint Online connectivity**: Connects to SharePoint Online through the Microsoft Graph API over HTTPS.
- **CSV, Parquet, and Avro files**: Extracts data from `.csv`, `.parquet`, and `.avro` files stored directly in a document library folder.
- **Full sync and incremental sync**: Incremental sync detects new and modified files based on each file's last modified timestamp. Refer to [Sync modes](#sync-modes) for more information.
- **Site and document library selection**: Select the SharePoint site and document library to sync for each pipeline.
- **Merge strategies**: Choose **Upsert** or **Append only** to control how rows load into the destination table.
- **Schema drift detection and handling**: Detect and apply schema changes automatically with **Auto-sync new fields**, or keep the schema fixed with **Block new fields**.
- **Field-level data protection**: Hash or replicate sensitive fields as is before the data reaches your destination.
- **Configurable sync frequency**: Schedule syncs on a time-based interval or with a cron expression. The minimum supported interval is 15 minutes.

## Microsoft SharePoint prerequisites

Connecting Microsoft SharePoint as a data pipeline source requires:

- A SharePoint Online site with a document library that stores `.csv`, `.parquet`, or `.avro` files
- Access to the Azure portal to register an app in Microsoft Entra ID
- A Microsoft Entra admin who can grant admin consent for application permissions. A SharePoint or Global admin must also grant the app access to each site if you use the `Sites.Selected` permission.
- The folder path and filename pattern for the files to sync

## Supported connection types

Microsoft SharePoint data pipelines support one authentication method:

- **Client credentials**: Authenticate with an app registered in Microsoft Entra ID that has application permissions for Microsoft Graph. Refer to [Set up your Microsoft Entra app](#set-up-your-microsoft-entra-app) for setup steps.

Authorization code grant isn't supported for data pipelines, even though the SharePoint connector for recipes supports it.

> **USE SEPARATE CONNECTIONS FOR PIPELINES AND RECIPES**
> 
> Data pipelines require a SharePoint connection with the **Graph API (Data-Pipelines only)** API scope. This scope doesn't work with recipe triggers and actions, and recipe connections that use the **SharePoint API** or **SharePoint & Graph API** scope don't work with data pipelines. Create a separate SharePoint connection for your pipelines instead of reusing a connection from your recipes.

## Required permissions

Assign one of the following Microsoft Graph permissions to your Workato app as an **Application** permission:

| Permission | Access | Additional setup |
| --- | --- | --- |
| `Sites.Selected` (recommended) | Only the sites you explicitly grant to the app. | A SharePoint or Global admin must grant the app access to each site. Refer to [Grant site access for Sites.Selected](#grant-site-access-for-sites-selected). |
| `Sites.Read.All` | All site collections in your tenant. | Admin consent only. |

The pipeline only reads files, so it doesn't require write permissions.

## Set up your Microsoft Entra app

Complete the following steps to register a Workato app in the Azure portal and collect the values you need to create the connection:

1. Register the Workato app in the Azure portal
   
   Complete the following steps to register the Workato app in the Azure portal:
   
   1. Sign in to the [Azure portal](https://portal.azure.com/).
      
   2. Select **App registrations > + New registration**.
      
   3. Enter a unique name for the application.
      
   4. Use the **Supported account types** drop-down menu to select an account type.
      
   5. Select **Web** from the **Select a platform** drop-down menu.
      
   6. Use the following URI for the **Redirect URI**:
      
      ```html
      https://www.workato.com/oauth/callback
      ```
      
   7. Select **Register**.
      
   
2. Assign permissions to your app
   
   Complete the following steps to assign Microsoft Graph application permissions to your app:
   
   1. Go to your newly registered app and select **Manage > API permissions**.
      
   2. Click **\+ Add a permission** and select **Microsoft Graph**.
      
   3. Select **Application permissions** as the permission type, because your pipeline runs without a signed-in user.
      
   4. Search for and select the `Sites.Selected` or `Sites.Read.All` permission. Refer to [Required permissions](#required-permissions) to choose between them.
      
   5. Click **Add permissions**.
      
   
3. Generate a certificate and private key
   
   You need a certificate and private key to authenticate using client credentials. You can generate these locally using OpenSSL or PowerShell. Refer to the [Microsoft documentation](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-self-signed-certificate) to generate a certificate with PowerShell.
   
   Complete the following steps to generate a self-signed certificate with OpenSSL:
   
   1. Open terminal, or another CLI (command-line interface) tool.
      
   2. Create a password-protected, 2048-bit RSA private key named `domain.key`:
      
      ```bash
      openssl genrsa -out domain.key 2048
      ```
      
   3. Create a Certificate Signing Request (CSR) `domain.csr` from the private key. Provide values for the required fields when prompted:
      
      ```bash
      openssl req -key domain.key -new -out domain.csr
      ```
      
   4. Create a self-signed certificate named `domain.crt` with your private key and CSR:
      
      ```bash
      openssl x509 -signkey domain.key -in domain.csr -req -days 365 -out domain.crt
      ```
      
   5. Open `domain.crt` and copy the entire certificate string, including the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines. Use this as your **Certificate** value in Workato.
      
   6. Open `domain.key` and copy the entire private key string, including the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` lines. Use this as your **Private key** value in Workato.
      
   7. Go to **Manage > Certificates & secrets > Certificates** in the Azure Portal.
      
   8. Click **Upload certificate** and select the `domain.crt` file.
      
   9. Provide a description for the certificate.
      
   10. Click **Add**.
       
   
4. Obtain the Application (client) ID and Directory (tenant) ID from the Azure portal
   
   1. Go to the **Overview > Essentials** section.
      
      ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
      
   2. Copy the `Application (client) ID` and `Directory (tenant) ID` for use in Workato.
      
   
5. Grant admin consent
   
   To connect to the Microsoft SharePoint connector using a Microsoft Entra ID account, ensure that all the consent requests are granted by admins.
   
   Complete the following steps to grant admin consent using an admin account:
   
   1. Sign in to your Azure portal and navigate to **Enterprise Applications > Activity > Admin consent requests**.
      
   2. Approve the necessary consent requests.
      
   
6. Required if you selected the `Sites.Selected` permission. Grant your app access to your SharePoint sites. Syncs fail without the grant. Refer to [Grant site access for Sites.Selected](#grant-site-access-for-sites-selected) for more information.
   

## Grant site access for Sites.Selected

The `Sites.Selected` permission doesn't give your app access to any site until a SharePoint or Global admin grants it. You can't start this grant inside Workato. Use PowerShell or the Microsoft Graph `POST /sites/{site-id}/permissions` call to grant your app access to each site you plan to sync.

Refer to the [Microsoft documentation](https://learn.microsoft.com/en-us/graph/permissions-selected-overview) on `Sites.Selected` for the steps.

> **THE CONNECTION'S SITE REQUIRES A GRANT**
> 
> If you use `Sites.Selected`, Workato checks the site in your connection's **Site name** field at the start of every sync, even if you enter a different **Site name** in the pipeline. Workato checks the root site of your tenant if you leave the connection's **Site name** field blank. The root site needs its own site grant, like any other site. Without it, the sync fails with a permission error.
> 
> Enter a site your app can access in the connection's **Site name** field to avoid granting access to the root site.

## Connect to Microsoft SharePoint

Complete the following steps to connect Microsoft SharePoint as a data pipeline source:

Connect to Microsoft SharePoint

1. Select **Create > Connection** or press C twice.
   
2. Search for `SharePoint` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select **Cloud** in the **Connection type** field.
   
6. Select the **Client credentials** option from the **Authentication type** drop-down menu.
   
7. Enter your SharePoint **Subdomain**. You can find it in your SharePoint URL. For example, if your SharePoint URL is `https://abc.sharepoint.com`, the subdomain is `abc`.
   
8. Use the **API Scope** drop-down menu to select **Graph API (Data-Pipelines only)**. Data pipelines return an error for connections that use the **SharePoint API** or **SharePoint & Graph API** scope.
   
   ![Select the Graph API (Data-Pipelines only) API scope](/assets/select-graph-scope.BL1yF66B.png)_Select the Graph API (Data-Pipelines only) API scope_
   
9. Provide the **Directory (tenant) ID** from the Azure portal in the **Tenant ID** field.
   
10. Provide the **Application (client) ID** from the Azure portal in the **Client ID** field.
    
11. Provide the certificate string you generated in the **Certificate** field.
    
12. Provide the private key string you generated in the **Private key** field.
    
13. Optional. Provide the name of your SharePoint site in the **Site name** field. Enter the name as it appears in the site URL. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If left blank, Workato connects to the root site of your tenant.
    
    You can override this value for each pipeline when you configure the pipeline.
    
14. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
    
15. Click **Sign in with Microsoft**.
    

## Configure the pipeline

Complete the following steps to configure Microsoft SharePoint as your data pipeline source:

1. Select **Create > Data pipeline** or press C+I.
   
2. Enter a name for the data pipeline in the **Data pipeline name** field.
   
   ![Data pipeline setup](/assets/set-up-pipeline.Cxx6hIk2.png)_Data pipeline setup_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the data pipeline.
   
4. Click **Start building**.
   
5. Click the **Extract new/updated records from source app** trigger. This trigger defines how the pipeline retrieves data from Microsoft SharePoint.
   
   ![Configure the Extract new/updated records from source app trigger](/assets/choose-source-app.B2OOUpgY.png)_Configure the Extract new/updated records from source app trigger_
   
6. Use the **Your Connected Source Apps** drop-down menu to select **Microsoft SharePoint**.
   
7. Choose the Microsoft SharePoint connection you plan to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
8. Optional. Enter the name of the SharePoint site that contains your document library in the **Site name** field. Leave the field blank to use the **Site name** from your connection.
   
   ![Enter site name](/assets/enter-site-name.BS5W7zWT.png)_Enter site name_
   
9. Use the **Document library** drop-down menu to select the document library you plan to monitor. Each pipeline reads from one document library.
   
10. Click **Add object** to configure the files the pipeline monitors and syncs. Each object configuration creates a dedicated table in your destination.
    
11. Enter the folder path to monitor in the **Source Folder path** field. The pipeline monitors this folder and fetches files that match your filename pattern. Enter `/` to monitor the root of the document library.
    
    ![Configure file settings](/assets/configure-file-settings-source.CVFjze4d.png)_Configure file settings_
    
    > **NESTED FOLDER LIMITATION**
    > 
    > The pipeline fetches only files located directly within the folder specified in the **Source Folder path** field. It doesn't fetch files from nested subfolders.
    > 
    > If your pipeline expects to include files in subfolders, move those files to the top-level folder or create a separate object for each folder.
    
12. Use the **File type** drop-down menu to select the file format to extract. Workato supports the following file types for Microsoft SharePoint:
    
    - **CSV**: Extract data from `.csv` files. Requires additional file type settings configuration. To sync tab-separated files, select this option and set the column delimiter to **Tab**.
    - **Parquet**: Extract data from `.parquet` files. Schema and data types are inferred directly from the file.
    - **Avro**: Extract data from `.avro` files. Schema and data types are inferred directly from the file.
13. Define which files to fetch using a pattern in the **Filename pattern** field. Use wildcards, such as `orders_*`, to include multiple files. The file extension is appended automatically based on the **File type** you select.
    
14. Click **Fetch matching files** to preview files matching the defined pattern.
    
15. Select a **Reference file** to define the schema for your destination table.
    
16. Configure **File type settings**:
    
    **CSV**
    
    1. Use the **Header line** drop-down menu to indicate whether your CSV contains a header line. Select **Yes** if the CSV contents include a header line that shouldn't be parsed as data.
       
    2. Use the **Column delimiter** drop-down menu to select the character used to separate column values within each CSV line. Defaults to **Comma**.
       
    
    **Parquet**
    
    Parquet files include embedded schema information, so no additional file type settings are required. Workato reads the schema and data types directly from the reference file.
    
    **Avro**
    
    Avro files include embedded schema information, so no additional file type settings are required. Workato reads the schema and data types directly from the reference file. The top-level Avro schema must be a record.
    
    Click **Fetch schema** to retrieve the schema from the reference file.
    
17. Review the schema to ensure it matches your expected table structure. The schema preview includes the columns from your source file along with the system-generated columns described in [Synthetic columns](#synthetic-columns).
    
    ![Review schema](/assets/review-schema-s3.BXKIKDpo.png)_Review schema_
    
18. Configure how rows are merged in the destination table in the **Choose a merge strategy** field. Workato supports the following merge strategies:
    
    - **Upsert**: Inserts new rows and updates existing rows. The **Merge method** field appears when you choose **Upsert**. You can select one or more columns to use as the primary key for the destination table. The pipeline uses the system-generated `_file` and `_line` columns as a composite primary key if you leave **Merge method** blank.
    - **Append only**: Inserts all rows without attempting to match or update existing records. The pipeline doesn't match on a key and doesn't update existing rows when you choose **Append only**.
19. Click **Review object** to confirm your setup. This screen displays your file settings, file type-specific options, and merge details.
    
    ![Review object](/assets/review-object-s3.s4_ztQhU.png)_Review object_
    
20. Enter an **Object name**. This value becomes the destination table name.
    
21. Click **Finish** to save the object configuration.
    
22. Review and customize the schema for each selected object. The pipeline automatically fetches an object's schema when you select it. This ensures the destination matches the source.
    
    Expand an object to view associated fields. Keep all fields selected to extract all available data, or deselect specific fields to exclude them from data extraction and schema replication.
    
23. Optional. Configure field-level data protection by expanding an object and choosing how to handle each field:
    
    - **Replicate as is**: Data values at the source replicate identically to the destination.
    - **Hash**: Hash sensitive data values in the field before syncing to your destination.
    
    Workato recommends hashing personally identifiable information (PII) and other sensitive fields. Refer to [Sensitive data handling](#sensitive-data-handling) for a list of fields that commonly contain PII.
    
24. Click **Add object** again to add more objects. Repeat this step to include additional Microsoft SharePoint objects in your pipeline.
    
25. Use the **Choose how to handle schema changes** drop-down menu to select a schema drift handling option:
    
    - **Auto-sync new fields**: Automatically detects and syncs new fields added in the source.
    - **Block new fields**: Keeps the schema fixed after the pipeline starts. You must add new fields manually. This option may cause the destination to fall out of sync if the source schema updates.
    
    Refer to [Schema replication and schema drift management](/en/data-orchestration/data-pipeline-recipe/concepts#schema-drift) for more information.
    
26. Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from Microsoft SharePoint to the destination.
    
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

The Microsoft SharePoint connector reads `.csv`, `.parquet`, and `.avro` files stored in the folder you specify. These files define the structure and data that the pipeline extracts and syncs to your destination.

Workato infers the schema and data types from the selected reference file:

- **CSV**: Workato infers boolean and numeric types and treats all other values, including date and date-time values, as strings. Transform these fields to the appropriate data type in the destination after the load completes.
- **Parquet and Avro**: Workato reads the schema and data types embedded in the file, including date and timestamp types.

All matched files must maintain the same column structure and data format to ensure accurate schema mapping.

## Sync modes

Microsoft SharePoint data pipelines support full sync and incremental sync. Workato skips empty files in both modes.

### Full sync

A full sync lists the files that match your folder path and filename pattern and extracts all rows from each file.

### Incremental sync

An incremental sync is file-level, not row-level. Workato uses each file's last modified timestamp in SharePoint as the incremental cursor. The pipeline lists the files in your folder on every run and processes files that are new or modified since the previous successful sync started. Unmodified files are skipped.

Workato reprocesses a modified file in full, because SharePoint doesn't provide row-level change tracking for CSV, Parquet, or Avro content. Use the **Upsert** merge strategy if you want reprocessed rows to update existing rows instead of inserting again.

If you set a start date in the **When first started, this pipeline should pick up records from** field, the first run includes only files modified on or after that date.

### Delete tracking

Microsoft SharePoint data pipelines don't support delete tracking. Workato doesn't remove or mark rows that came from a file you delete from SharePoint.

## Schema and data type handling

The following considerations apply to schema and data types when you sync data from Microsoft SharePoint:

### Nested data

Parquet and Avro files can contain nested objects and repeated fields (arrays). Workato serializes these as JSON in a single column rather than flattening them into individual columns. For Avro files, this also applies to maps and to union fields that can hold more than one non-null type.

Workato extracts Avro `bytes` and `fixed` values as Base64-encoded strings. Values that use the `decimal` logical type are extracted as decimals.

### Synthetic columns

Workato adds the following synthetic columns to destination tables created from a Microsoft SharePoint object:

| Column | Type | Purpose |
| --- | --- | --- |
| `_file` | String | Path of the source file the row was read from, including the folder path and file name |
| `_line` | Long | Row number of the record within the source file |
| `_modified` | Timestamp | Last modified timestamp of the source file at the time of sync. Workato adds this column only when you use the **Append only** merge strategy. |

The names `_file`, `_line`, and `_modified` are reserved. A file that contains a column with one of these names fails schema processing.

## Sensitive data handling

SharePoint files can contain any customer data, including PII and business-confidential information. Workato can't predict which columns contain sensitive data ahead of time, because the schema of every file is customer-defined.

Review the fields in each object before you sync it, and use the **Hash** option in field-level data protection to hash any column that contains PII or other sensitive data. Refer to the [Configure the pipeline](#configure-the-pipeline) steps for more information.

## Microsoft SharePoint limitations

The following limitations apply when you use Microsoft SharePoint as a data pipeline source:

### Recipe connections can't be reused

Data pipelines require a SharePoint connection with the **Graph API (Data-Pipelines only)** API scope, which doesn't work with recipes. Create a separate connection for your pipelines. Refer to [Supported connection types](#supported-connection-types) for more information.

### Nested folders aren't supported

The pipeline fetches only files located directly within the folder in the **Source Folder path** field. Files in subfolders aren't synced.

### Only CSV, Parquet, and Avro files are supported

The pipeline doesn't extract data from other file formats, such as Excel, JSON, XML, PDF, or images.

### SharePoint Lists and SharePoint Server aren't supported

Data pipelines read files from SharePoint Online document libraries only. Structured SharePoint Lists and SharePoint Server (on-premises) deployments aren't supported.

### One site and document library for each pipeline

Each pipeline reads from the single site and document library you select. The pipeline doesn't aggregate files across multiple sites or enumerate every file in your tenant.

### Minimum sync frequency

The minimum supported sync interval is 15 minutes.
