---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-coupa.md
description: >-
  Set up Coupa as a data pipeline source to extract and sync records through the
  Coupa REST API into your destination.
---

# Configure Coupa as your data pipeline source

Set up Coupa as a data pipeline source to extract and sync records into your destination. This guide includes connection setup, pipeline configuration, and key behavior for working with Coupa as a source.

## Coupa features supported

The following features are supported when using Coupa as a data pipeline source:

- Extract data using the Coupa REST API
- Support for full and incremental sync
- Field-level selection for object extraction
- Schema drift detection and handling
- Field-level data masking

## Coupa prerequisites

You must have the following configuration and access:

- A Coupa instance with API access enabled
- Coupa instance URL
- Required scopes for the API
- Read access to the objects you plan to sync

## How to connect

Complete the following steps to connect to **Coupa** as a data pipeline source. This connection allows the pipeline to extract and sync data from your Coupa instance:

Connect to Coupa

1. Select **Create > Connection** or press C twice.
   
2. Search for `Coupa` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
   ![Coupa connection setup](/assets/connect-to-coupa.BPGbPbav.png)_Coupa connection setup_
   
4. Use the **Location** drop-down to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select one of the following authentication types:
   
   - API key
   - Client credentials
   - Authorization code grant
   
   The required fields vary depending on the authentication type.
   
6. Fill in the following fields based on the selected authentication method:
   
   **API key**
   
   1. Enter your Coupa instance URL in the **Host** field. For example:`your-instance-name.coupacloud.com`.
      
   2. Enter the **API key**. You can generate it in Coupa from **Setup > Integrations > API Keys**.
      
   
   **Client credentials**
   
   1. Enter the **Client ID** of your Open Connect client.
      
   2. Enter the **Client secret** of your Open Connect client.
      
   3. Enter your Coupa instance URL in the **Host** field.
      
   4. Select the required **Scopes**. The `core.common.read` scope is selected by default.
      
   
   **Authorization code grant**
   
   1. Enter the **Client ID** of your Open Connect client.
      
   2. Enter the **Client secret** of your Open Connect client.
      
   3. Enter your Coupa instance URL in the **Host** field.
      
   4. Select the required **Scopes**. The `core.common.read` and `offline_access` scopes are selected by default.
      
   
7. Click **Connect** to verify and establish the connection.
   

## Configure the pipeline

Complete the following steps to configure Coupa as your data pipeline source:

1. Select **Create > Data pipeline** or press C+I.
   
2. Enter a name for the data pipeline in the **Data pipeline name** field.
   
   ![Data pipeline setup](/assets/set-up-pipeline.Cxx6hIk2.png)_Data pipeline setup_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the data pipeline.
   
4. Click **Start building**.
   
5. Click the **Extract new/updated records from source app** trigger. This trigger defines how the pipeline retrieves data from the source application.
   
   ![Configure the Extract new/updated records from source app trigger](/assets/choose-source-app.B2OOUpgY.png)_Configure the Extract new/updated records from source app trigger_
   
6. Use the **Your Connected Source Apps** drop-down menu to select **Coupa**.
   
7. Choose the Coupa connection you plan to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
   ![Choose a Coupa connection](/assets/choose-coupa-connection.BYzV_jAb.png)_Choose a Coupa connection_
   
8. Click **Add object** to open the object wizard.
   
   ![Add objects](/assets/add-object-coupa.JXnuLiMn.png)_Add objects_
   
9. Search or browse the list of available Coupa objects. Select the objects you plan to sync and click **Add**.
   
   ![Select objects](/assets/select-object-coupa.Cen2140t.png)_Select objects_
   
10. Review and customize the schema for each selected object. When you select an object, the pipeline automatically fetches its schema to ensure the destination matches the source.
    
    ![Expand object](/assets/expand-object-coupa.DvPpwWqC.png)_Expand object_
    
    Expand any object to view its fields. Keep all fields selected to extract all available data, or deselect specific fields to exclude them from data extraction and schema replication.
    
11. Optional. Configure field-level data protection. After you expand an object, choose how to handle each field:
    
    - **Replicate as is** (default): Data values at the source are replicated identically to the destination.
    - **Hash**: Hash sensitive data values in the column before syncing to your destination.
    
    ![Configure field-level data protection](/assets/configure-field-data-coupa.CBYoTQ_s.png)_Configure field-level data protection_
    
12. Click **Add object** again to add more objects using the same flow. You can repeat this step to include multiple Coupa objects in your pipeline.
    
13. Use the **Choose how to handle schema changes** drop-down menu to select a schema drift handling option:
    
    - **Auto-sync new fields**: Automatically detects and syncs new fields added in the source.
    - **Block new fields**: Keeps the schema fixed after the pipeline starts. You must add new fields manually. This option may cause the destination to fall out of sync if the source schema updates.
    
    Refer to [Schema replication and schema drift management](/en/data-orchestration/data-pipeline-recipe/concepts#schema-drift) for more information.
    
14. Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from Coupa to the destination.
    
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
       
    

## Supported Coupa objects

The Coupa connector uses the Coupa REST API to retrieve records for pipeline sync. It supports standard objects commonly used in Coupa environments, including accounts, approvals, and contracts.
