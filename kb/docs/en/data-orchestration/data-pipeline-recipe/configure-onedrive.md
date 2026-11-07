---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-onedrive.md
description: >-
  Set up OneDrive as a data pipeline source to extract and sync records from CSV
  and Parquet files into your destination.
---

# Configure OneDrive as your data pipeline source

Set up OneDrive as a data pipeline source to extract and sync records into your destination.

Use this guide to review connection setup, pipeline configuration, and key behavior for working with `.csv` and `.parquet` files stored in OneDrive folders.

## Features supported

The following features are supported when you use OneDrive as a data pipeline source:

- **File format support**: Extract and sync data from `.csv` and `.parquet` files in OneDrive folders.
- **Full and incremental sync**: Runs a full sync when the pipeline starts, then incremental syncs on every later run to pick up files created or modified since the last run.
- **Drive selection**: Select a specific OneDrive drive to sync from, including a shared drive or a SharePoint site document library.
- **Field-level selection**: Choose which fields to extract and replicate to your destination.
- **Field-level data protection**: Hash or replicate sensitive fields as is before the data reaches your destination.

## Prerequisites

Connecting OneDrive as a data pipeline source requires:

- A Microsoft OneDrive account: personal, business, or tied to a specific tenant
- Credentials for your chosen authentication method:
  - **Authorization code grant**: Register an app in the Azure portal and assign it the required permissions. Refer to [Connect to OneDrive](#connect-to-onedrive) for setup steps.
  - **Client credentials grant**: Register a tenant-specific app in the Azure portal, generate a client secret, and obtain the tenant, client, and user IDs. This method is only available for tenant-specific accounts. Refer to [Connect to OneDrive](#connect-to-onedrive) for setup steps.

> **REQUIRED PERMISSIONS**
> 
> OneDrive data pipelines are read-only. They extract and sync file contents but don't create, update, move, or delete files in OneDrive. Grant only the scopes needed for your chosen authentication method.

## Supported connection types

OneDrive data pipelines support the following authentication methods:

- **Authorization code grant (OAuth 2.0)**: Sign in with a Microsoft personal, business, or tenant-specific account. Refer to [Connect to OneDrive](#connect-to-onedrive) for setup steps.
- **Client credentials grant (OAuth 2.0)**: Authenticate using a tenant-specific app's client ID and client secret, without an interactive user sign-in. This method is only supported for tenant-specific accounts.

## Connect to OneDrive

The OneDrive connector supports the following authentication types:

- [Authorization code grant authentication (OAuth 2.0)](#authentication-auth-code)
- [Client credentials-based authentication (OAuth 2.0)](#authentication-client-credentials)

> **MICROSOFT MFA ENFORCEMENT**
> 
> Microsoft is rolling out mandatory multifactor authentication (MFA) gradually to different applications and accounts in phases. This enforcement continues throughout 2025 and beyond. Refer to the Microsoft [Mandatory multifactor authentication for Azure and admin portals](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication?tabs=dotnet) documentation for more information.
> 
> We strongly recommend enabling MFA now for all Microsoft accounts used with Workato to avoid service disruptions from short-notice enforcement changes.
> 
> Complete the following steps to maintain uninterrupted service:
> 
> 1. Enable MFA for your Microsoft organization following the Microsoft MFA setup guide. Refer to [Set up multifactor authentication for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/set-up-multi-factor-authentication?view=o365-worldwide) for more information.
>    
> 2. Reconnect your Microsoft connection in Workato.
>    
> 3. Complete the OAuth flow with MFA when prompted.
>    
> 4. Test your recipes to ensure they work with the updated connection.
>    

### Authorization code grant authentication (OAuth 2.0)

Use the Tenant ID/Domain value with tenant-specific account types.

#### Minimum and default scopes

The OneDrive connector requests the following scopes by default. These scopes support all triggers and actions. You must assign these as **Delegated** permissions in the Azure portal:

- `Files.ReadWrite`
- `Group.Read.All`
- `Files.Read`
- `offline_access`

You must add the following minimum scopes to establish a connection to OneDrive with authorization code grant authentication:

- `Files.Read`
- `offline_access`

#### OneDrive setup for authorization code grant authentication

Complete the following steps to set up OneDrive for authorization code grant authentication:

- [Register the Workato app in Azure portal](#auth-register)
- [Assign permissions to your app](#assign-permissions)
- [Obtain the Directory (tenant) ID from the Azure portal](#obtain-directory-id)

##### Register the Workato App in Azure portal

View register the Workato app in the Azure portal steps

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
   

  

##### Assign permissions to your app

View assign permissions to your app steps

Complete the following steps to assign permissions to your app:

1. Go to your newly registered app and select **Manage > API permissions** in the navigation sidebar.
   
2. Click **\+ Add a permission** and select **Microsoft Graph APIs**.
   
3. Add the required permissions. Depending on your connection type, you must assign **Application** or **Delegated** permissions.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**. If specific permissions require admin consent, refer to [Connect Microsoft Entra ID to the Outlook connector](/en/connectors/onedrive#admin-consent) to learn more.
   

  

##### Obtain the Directory (tenant) ID from the Azure portal

View obtain the Directory (tenant) ID from the Azure portal steps

Complete the following steps to obtain the Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the `Directory (tenant) ID` for use in Workato.
   

  

#### Connect to OneDrive with authorization code grant authentication

View connect to OneDrive with authorization code grant authentication steps

Complete the following steps to set up a authorization code grant connection to OneDrive in Workato:

1. Click **Create > Connection**.
   
2. Search for `OneDrive` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection account type** drop-down menu to select the type of account you plan to use. The available choices are **Personal**, **Business**, and **Tenant-specific**.
   
   **Personal**
   
   - **Personal**: This option allows you to sign in using a personal account that isn't restricted to a specific organization (tenant).
   
   ![Personal connection](/assets/connect-personal.kBRKqbGY.png)_Personal connections_
   
   **Business**
   
   - **Business**: This option allows you to sign in using a user account that belongs to a company or organization.
   
   ![Business connection](/assets/connect-business.BTxzvVgS.png)_Business connections_
   
   **Tenant specific**
   
   - **Tenant specific**: This option is specifically designed for users who belong to a particular organization (tenant).
   
   ![Provide the tenant ID/domain](/assets/connect-tenant-specific.CTOJkWIZ.png)_Tenant specific connections_
   
   Enter the **Tenant ID/Domain**. Use either the `Directory (tenant) ID` or the tenant domain for your Microsoft Entra ID tenant. This ensures that you are accessing resources that are specifically configured for that tenant. Refer to [Obtain the Directory (tenant) ID from the Azure portal](#obtain-directory-id) for more information.
   
6. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
7. Optional. Use the **Requested permissions (OAuth scopes)** field to select specific permissions. The minimum permissions required to establish a connection are `Files.Read` and `offline_access`. Workato requests these permissions regardless of the permissions you select. Refer to [Minimum and default scopes](#authorization-code-grant-scopes) for more information.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
9. Click **Sign in with Microsoft**.
   

### Client credentials-based authentication (OAuth 2.0)

This authentication type requires the following values:

- Tenant ID/Domain
- User ID
- Client ID
- Client secret

#### Minimum and default scopes

We recommend the following scopes for client credentials-based connections. These scopes support all triggers and actions. You must assign these as **Application** permissions in the Azure portal:

- `Files.Read.All`
- `Files.ReadWrite.All`
- `Group.Read.All`
- `Sites.ReadWrite.All`

You must add the following minimum scopes to establish a connection to OneDrive with client credentials-based authentication:

- `Files.Read.All`

#### OneDrive setup for client credentials-based authentication

Complete the following steps to set up OneDrive for client credentials-based authentication:

- [Register the Workato app in the Azure portal](#client-credentials-register)
- [Assign permissions to your app](#assign-permissions-client-credentials)
- [Generate a client secret](#generate-client-secret)
- [Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal](#obtain-ids)
- [Obtain the User ID from the Azure portal](#obtain-user-id)

> **COMPATIBLE AUTHENTICATION**
> 
> Client credentials-based authentication is only compatible with tenant-specific connections.

##### Register the Workato App in the Azure portal

View register the Workato app in the Azure portal steps

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
   

##### Assign permissions to your app

View assign permissions to your app steps

Complete the following steps to assign permissions to your app:

1. Go to your newly registered app and select **Manage > API permissions** in the navigation sidebar.
   
2. Click **\+ Add a permission** and select **Microsoft Graph APIs**.
   
3. Add the required permissions. Depending on your connection type, you must assign **Application** or **Delegated** permissions.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**. If specific permissions require admin consent, refer to [Connect Microsoft Entra ID to the Outlook connector](/en/connectors/onedrive#admin-consent) to learn more.
   

##### Generate a client secret

View generate a client secret steps

Complete the following steps to generate a client secret:

1. Go to **Manage > Certificates & Secrets > Client secrets**.
   
2. Click **\+ New client secret**.
   
3. Provide a **Description** for the client secret and specify an **Expires** date.
   
4. Click **Add**.
   
5. Copy and save the client secret **Value**—not the **Secret ID**—for use in Workato.
   
   ![Copy and save the client secret value](/assets/sharepoint-troubleshoot.DPBGyl4B.png)_Copy and save the client secret value_
   

##### Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal

View obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal steps

Complete the following steps to obtain the Application ID, Object ID, and Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the **Application (client) ID**, **Object ID**, and **Directory (tenant) ID** for use in Workato.
   

##### Obtain the User ID from the Azure portal

View obtain the User ID from the Azure portal steps

Complete the following steps to obtain the User ID from the Azure portal:

1. Go to **Home > Users** to obtain the `User ID`.
   
   ![Users](/assets/users.CuDgSGeL.png)_Select users_
   
2. Search for and select the default user you plan to use to perform operations. This user doesn't establish the connection but is required for performing certain operations that an app can't perform. It's also required in picklists to pull user data. For example, the folder picklist populates folders belonging to the default user.
   
3. Copy and save the **User principal name**. Use this value as the **User ID** in Workato.
   

#### Connect to OneDrive with client credentials-based authentication

View connect to OneDrive with client credentials-based authentication steps

Complete the following steps to set up a client credentials-based connection to OneDrive in Workato:

1. Click **Create > Connection**.
   
2. Search for `OneDrive` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select **Tenant specific** as the **Connection account type**. This option supports accounts tied to a specific organization (tenant).
   
   ![Tenant specific connection type](/assets/connect-tenant-specific-2.Bc0pu37N.png)_Tenant specific account connection type_
   
6. Provide your **Tenant ID/Domain**. This is the `Directory (tenant) ID` for your app. Refer to [Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal](#obtain-ids) for more information.
   
7. Use the **Authentication type** drop-down menu to select **Client credentials**.
   
8. Provide the **User ID**, **Client ID**, and **Client secret** for your app. Refer to [Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal](#obtain-ids) and [Generate a client secret](#generate-client-secret) for more information.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Sign in with Microsoft**.
    

## Connect Microsoft Entra ID to the OneDrive connector

View connect Microsoft Entra ID to the OneDrive connector steps

To connect to the OneDrive connector using a Microsoft Entra ID account, ensure that all the consent requests are granted by admins.

Complete the following steps to grant admin consent using an admin account:

1. Sign in to your Azure portal and navigate to **Enterprise Applications > Activity > Admin consent requests**.
   
2. Approve the necessary consent requests.
   

## Configure the pipeline

Complete the following steps to configure OneDrive as your data pipeline source:

1. Select **Create > Data pipeline** or press C+I.
   
2. Enter a name for the data pipeline in the **Data pipeline name** field.
   
   ![Data pipeline setup](/assets/set-up-pipeline.Cxx6hIk2.png)_Data pipeline setup_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the data pipeline.
   
4. Click **Start building**.
   
5. Click the **Extract new/updated records from source app** trigger. This trigger defines how the pipeline retrieves data from OneDrive.
   
   ![Configure the Extract new/updated records from source app trigger](/assets/choose-source-app.B2OOUpgY.png)_Configure the Extract new/updated records from source app trigger_
   
6. Use the **Your Connected Source Apps** drop-down menu to select **OneDrive**.
   
7. Choose the OneDrive connection you plan to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
8. Optional. Enter a **Drive ID**. Leave this field blank to use the authorized user's personal OneDrive drive. To list files and folders from a shared OneDrive drive or a SharePoint site document library, provide the drive ID that the authorized user can access. You can find the drive ID in the OneDrive URL as the `cid` parameter. For example, in `https://onedrive.live.com/?id=244DDFC44A57%21103&cid=24C9A8FC44A57`, `24C9A8FC44A57` is the drive ID.
   
9. Click **Add object** to open the **New object** panel.
   
   ![Add object](/assets/add-object-onedrive.BmgctVmw.png)_Add object_
   
10. Enter the folder path to monitor in the **Source Folder path** field. The pipeline lists direct child files in this folder and fetches files that match your filename pattern.
    
    ![Configure file settings](/assets/configure-file-settings-onedrive.i8wSy4Vi.png)_Configure file settings_
    
    > **NESTED FOLDER LIMITATION**
    > 
    > OneDrive data pipelines only fetch files located directly within the folder specified in the **Source Folder path** field. Files in nested subfolders aren't fetched. If your pipeline expects files in subfolders, move those files to the top-level folder.
    
11. Use the **File type** drop-down menu to select the file format to extract. Workato supports the following file types:
    
    - **CSV**: Extract data from `.csv` files. Requires additional file type settings configuration.
    - **Parquet**: Extract data from `.parquet` files. Schema and data types are inferred directly from the file.
12. Define which files to fetch using a pattern in the **Filename pattern** field. Use wildcards, such as `orders_*`, to include multiple files. The file extension is appended automatically based on the **File type** you select.
    
13. Click **Fetch matching files** to preview files matching the defined pattern.
    
14. Select a **Reference file** to define the schema for your destination table.
    
15. Configure **File type settings**:
    
    **CSV**
    
    1. Use the **Header line** drop-down menu to indicate whether your CSV contains a header line. Select **Yes** if the CSV contents include a header line that shouldn't be parsed as data.
       
    2. Use the **Column delimiter** drop-down menu to select the character used to separate column values within each CSV line. Defaults to **Comma**.
       
    
    **Parquet**
    
    Parquet files include embedded schema information, so no additional file type settings are required. Workato reads the schema and data types directly from the reference file.
    
    Click **Fetch schema** to retrieve the schema from the reference file.
    
16. Review the schema to ensure it matches your expected table structure. The schema preview includes the columns from your source file along with the following system-generated columns:
    
    - `_file`: The name of the source file each row originated from.
    - `_line`: The line or row number of each record within the source file.
17. Configure how rows are merged in the destination table in the **Choose a merge strategy** field:
    
    - **Upsert** (default): Inserts new rows and updates existing rows. When you choose **Upsert**, the **Merge method** field appears. You can select one or more columns to use as the primary key for the destination table. If you leave **Merge method** blank, the pipeline uses the system-generated `_file` and `_line` columns as a composite primary key.
    - **Append only**: Inserts all rows without attempting to match or update existing records. Append-only tables also include a system-generated `_modified` column so you can track each row's source file modification time.
18. Click **Review object** to confirm your setup. This screen displays your file settings, file type-specific options, and merge details.
    
19. Enter an **Object name**. This name defines the destination table name.
    
20. Click **Finish** to save the object configuration.
    
21. Review and customize the schema for each selected object. The pipeline automatically fetches an object's schema when you select it. This ensures the destination matches the source.
    
    Expand an object to view associated fields. Keep all fields selected to extract all available data, or deselect specific fields to exclude them from data extraction and schema replication.
    
22. Optional. Configure field-level data protection by expanding an object and choosing how to handle each field:
    
    - **Replicate as is**: Data values at the source replicate identically to the destination.
    - **Hash**: Hash sensitive data values in the field before syncing to your destination.
    
    Workato recommends hashing personally identifiable information (PII) and other sensitive fields. Refer to [Sensitive data handling](#sensitive-data-handling) for a list of fields that commonly contain PII.
    
23. Click **Add object** again to add more objects. Repeat this step to include additional OneDrive objects in your pipeline.
    
24. Use the **Choose how to handle schema changes** drop-down menu to select a schema drift handling option:
    
    - **Auto-sync new fields**: Automatically detects and syncs new fields added in the source.
    - **Block new fields**: Keeps the schema fixed after the pipeline starts. You must add new fields manually. This option may cause the destination to fall out of sync if the source schema updates.
    
    Refer to [Schema replication and schema drift management](/en/data-orchestration/data-pipeline-recipe/concepts#schema-drift) for more information.
    
25. Optional. Enter a value in the **Concurrency limit** field to cap the number of concurrent operations. Leave the field blank to use the default quota set by Workato. The maximum value is `100`.
    
26. Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from OneDrive to the destination.
    
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
       
    

## Supported objects

OneDrive doesn't have a fixed object catalog. Instead, each folder and filename pattern configuration you add becomes an object that syncs as a separate table in your destination:

| Object | Sync modes | Delete tracking |
| --- | --- | --- |
| `CSV files` | Full sync, then incremental | No |
| `Parquet files` | Full sync, then incremental | No |

Refer to [Sync modes](#sync-modes) and [Delete tracking](#delete-tracking) for more information.

## Sync modes

OneDrive data pipelines run a full sync followed by incremental syncs on every later run. This sequence isn't configurable.

### Full sync

A full sync lists all files matching the configured folder path, file type, and filename pattern, and extracts all rows from each matching file. This full sync runs only once, when the pipeline starts. Every later run is an incremental sync.

### Incremental sync

Incremental sync is file-level, not row-level. Each run lists matching files and processes only files created or modified after the last recorded modification time. OneDrive doesn't provide row-level change tracking inside a CSV or Parquet file, so a modified file is reprocessed in full rather than diffed row by row.

### Delete tracking

OneDrive doesn't support delete tracking. Workato doesn't remove or mark rows as deleted in your destination when a source file is removed, regardless of the merge strategy you choose. Include a column to track deletions in your source files if you require this behavior.

## Schema and data type handling

OneDrive data pipelines infer the schema from the selected CSV or Parquet file:

- **CSV files**: Workato samples the file to infer column names and types. Ambiguous or unsupported values remain strings.
- **Parquet files**: Workato reads the embedded Parquet schema directly from the file. Nested structures and repeated fields are preserved according to the shared Parquet reader, with nested structures serialized as JSON strings where required.

All files matched by the same object configuration must maintain the same column structure and data format to ensure accurate schema mapping.

### Synthetic columns

Workato adds the following synthetic columns to each destination table:

| Column | Purpose |
| --- | --- |
| `_file` | The name of the source file each row originated from. |
| `_line` | The line or row number of each record within the source file. |
| `_modified` | The source file's last-modified timestamp. Only added when you choose the **Append only** merge strategy. |

Refer to the [Configure the pipeline](#configure-the-pipeline) steps for how to choose a merge strategy and primary key.

## Sensitive data handling

OneDrive files can contain arbitrary customer data, including personally identifiable information (PII) and other sensitive or confidential content. Because file columns are customer-defined rather than fixed source API fields, OneDrive data pipelines don't expose a fixed list of sensitive fields.

Use the **Hash** option in field-level data protection during pipeline configuration to protect PII before it reaches your destination. Refer to the [Configure the pipeline](#configure-the-pipeline) steps for more information.

## Limitations

The following limitations apply when you use OneDrive as a data pipeline source:

### Supported file formats

OneDrive data pipelines only support `.csv` and `.parquet` files. Other formats, including Excel, JSON, XML, PDF, images, and other binary files, aren't supported.

### Folder traversal

OneDrive data pipelines only fetch files from the direct children of the configured folder. Files in nested subfolders aren't fetched or synced.

### Maximum file size

Each file must be `10` GB or smaller.

### Minimum sync frequency

The minimum supported sync interval is 15 minutes.
