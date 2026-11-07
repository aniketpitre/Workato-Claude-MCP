---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-salesforce.md
description: >-
  Configure Salesforce as a data pipeline source to extract standard and custom
  object records through the Bulk API and sync them to your destination.
---

# Configure Salesforce as a data pipeline source

Set up Salesforce as a data pipeline source to extract and sync records into your destination. This guide includes connection setup, pipeline configuration, and key behavior for working with Salesforce as a source.

Workato uses the [Salesforce Bulk API v2](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/intro_bulk_api.htm) to extract and sync data efficiently at scale.

## Features supported

The following features are supported when using Salesforce as a data pipeline source:

- Extract data from standard and custom Salesforce objects
- Support for full and incremental sync
- Field-level selection for object extraction
- Schema drift detection and handling
- Field-level data masking

## Prerequisites

You must have the following permissions to connect to and extract data from Salesforce:

- An active Salesforce user account with API access
- Read access to the objects and fields included in the pipeline

## How to connect

Complete the following steps to connect to **Salesforce** as a data pipeline source. This connection lets the pipeline extract data from Salesforce.

Workato supports OAuth 2.0 for data pipelines, which provides a more secure and scalable authentication method compared to alternative connection types.

Connect to Salesforce

1. Select **Create > Connection** or press C twice.
   
2. Search for `Salesforce` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Salesforce connection setup](/assets/connect-to-salesforce.B5puhQuy.png)_Salesforce connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Sandbox** drop-down menu to specify whether the connection is a sandbox account.
   
6. Select **OAuth 2.0** as the **Auth type**. This is the default and only supported authentication method for data pipelines.
   
7. Optional. Expand **Advanced settings** to configure advanced connection options.
   
8. Optional. Select a **Custom OAuth profile** to restrict the connection to specific scopes. This ensures the authentication flow uses the client app linked to the custom profile.
   
9. Select **Connect** and enter your Salesforce account credentials when prompted.
   
   ![Salesforce connection setup](/assets/login.CIu5oc0P.png)_Log in to your Salesforce account_
   
10. Select **Log In** to verify the connection.
    

## Configure the pipeline

Complete the following steps to configure Salesforce as your data pipeline source:

1. Select **Create > Data pipeline** or press C+I.
   
2. Enter a name for the data pipeline in the **Data pipeline name** field.
   
   ![Data pipeline setup](/assets/set-up-pipeline.Cxx6hIk2.png)_Data pipeline setup_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the data pipeline.
   
4. Click **Start building**.
   
5. Click the **Extract new/updated records from source app** trigger. This trigger defines how the pipeline retrieves data from the source application.
   
   ![Configure the Extract new/updated records from source app trigger](/assets/choose-source-app.B2OOUpgY.png)_Configure the Extract new/updated records from source app trigger_
   
6. Use the **Your Connected Source Apps** drop-down menu to select **Salesforce**.
   
7. Choose the Salesforce connection you plan to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
   ![Choose a Salesforce connection](/assets/choose-salesforce-connection.9ATdiWy5.png)_Choose a Salesforce connection_
   
8. Click **Add object** to open the object wizard.
   
   ![Add object](/assets/add-salesforce-object.DTQ1xLAz.png)_Add object_
   
9. Search or browse the list of available Salesforce objects. Select the objects you plan to sync and click **Add**.
   
   ![Add object](/assets/select-salesforce-object.r3AUgChm.png)_Add object_
   
10. Review and customize the schema for each selected object. When you select an object, the pipeline automatically fetches its schema to ensure the destination matches the source.
    
    ![Expand object](/assets/expand-object.EtBMmh9F.png)_Expand object_
    
    You can expand any object to view its fields. Keep all fields selected to extract all available data, or deselect specific fields to exclude them from data extraction and schema replication.
    
11. Optional. Configure field-level data protection by expanding an object and choosing how to handle each field:
    
    - **Replicate as is**: Data values at the source replicate identically to the destination.
    - **Hash**: Hash sensitive data values in the field before syncing to your destination.
    
    Workato recommends hashing personally identifiable information (PII) and other sensitive fields.
    
12. Optional. Click the gear icon next to an object to open its settings, then complete the following steps:
    
    1. Use the **Sync mode** drop-down menu to select **Full sync** or **Incremental**. Workato defaults to **Full sync** if it doesn't detect a timestamp for the object.
       
    2. Optional. Enter a SOQL condition in the **SOQL WHERE clause** field, without the `WHERE` keyword, to filter which records sync for the object. For example, enter `StageName = 'Closed Lost'` for the `Opportunity` object to sync only closed-lost opportunities.
       
    3. Click **Save**.
       
13. Click **Add object** again to add more objects using the same flow. You can repeat this step to include multiple Salesforce objects in your pipeline.
    
14. Optional. Use the **Relax Numeric Fields** drop-down menu to select **Yes** to convert Salesforce numeric fields to double-precision floating point values in the destination. This lets the destination safely handle values with higher precision and scale.
    
15. Use the **Choose how to handle schema changes** drop-down menu to select a schema drift handling option:
    
    - **Auto-sync new fields**: Automatically detects and syncs new fields added in the source.
    - **Block new fields**: Keeps the schema fixed after the pipeline starts. You must add new fields manually. This option may cause the destination to fall out of sync if the source schema updates.
    
    Refer to [Schema replication and schema drift management](/en/data-orchestration/data-pipeline-recipe/concepts#schema-drift) for more information.
    
16. Optional. Enter a value in the **Concurrency limit** field to cap the number of concurrent operations. Leave the field blank to use the default quota set by Workato. The maximum value is `100`.
    
17. Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from Salesforce to the destination.
    
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
       
    

## Supported Salesforce objects

The pipeline supports most Salesforce standard and custom objects with read permissions. Workato uses the [Salesforce Bulk API v2](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/intro_bulk_api.htm) to fetch object records.
