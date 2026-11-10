---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-ellucian.md
description: >-
  Set up Ellucian Banner as a data pipeline source to extract and sync records
  through the Ethos Integration APIs into your destination.
---

# Configure Ellucian Banner as your data pipeline source

Set up Ellucian Banner as a data pipeline source to extract and sync records into your destination. This guide includes connection setup, pipeline configuration, and key behavior for working with your Banner environment.

## Ellucian Banner features supported

The following features are supported when using Ellucian Banner as a data pipeline source:

- Extract and sync data using the Ellucian Ethos Integration APIs
- Support for full syncs
- Field-level selection for data extraction
- Schema drift detection and handling
- Field-level data masking

## Ellucian Banner prerequisites

Ensure you have completed the following tasks before you begin:

- Access your Ellucian Banner Cloud environment.
- Generate an Ethos Integration API key.
- Obtain your Ellucian Cloud region and domain details.
- Configure the underlying Ethos API integration to allow the required scopes for Banner Student API endpoints.
- Grant read privileges to the API key for each Banner object you plan to sync.

Workato only syncs objects for which the API key has read access.

## Connect to Ellucian Banner

Complete the following steps to connect to Ellucian Banner as a data pipeline source. This connection enables the pipeline to extract and sync records from your Ellucian environment.

Connect to Ellucian Banner

1. Select **Create > Connection** or press C twice.
   
2. Search for `Ellucian Banner` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
   ![Ellucian Banner connection setup](/assets/connect-to-ellucian.SHS8WEc6.png)_Ellucian Banner connection setup_
   
4. Use the **Location** drop-down to select the project where you plan to store the connection.
   
5. Select **Cloud** in the **Connection type** field, unless you need to connect through an on-prem group.
   
6. Select your region from the **Domain** drop-down. Choose the domain based on the location of your Ellucian Cloud instance (for example, **U.S.**, **Canada**, or **Europe**).
   
7. Enter your **API key**. This is the API key for your Ethos Integration application in Ellucian.
   
8. Select **Connect** to verify and store the connection.
   

## Configure the pipeline

Complete the following steps to configure Ellucian Banner as your data pipeline source.

1. Select **Create > Data pipeline** or press C+I.
   
2. Enter a name for the data pipeline in the **Data pipeline name** field.
   
   ![Data pipeline setup](/assets/set-up-pipeline.Cxx6hIk2.png)_Data pipeline setup_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the data pipeline.
   
4. Click **Start building**.
   
5. Click the **Extract new/updated records from source app** trigger. This trigger defines how the pipeline retrieves data from Ellucian Banner.
   
   ![Configure the Extract new/updated records from source app trigger](/assets/choose-source-app.B2OOUpgY.png)_Configure the Extract new/updated records from source app trigger_
   
6. Use the **Your Connected Source Apps** drop-down menu to select **Ellucian Banner**.
   
7. Choose the Ellucian Banner connection you plan to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
8. Click **Add object** to open the object wizard.
   
9. Search or browse the list of available Ellucian Banner objects. Select the objects you plan to sync and click **Add**.
   
10. Review and customize the schema for each selected object. The pipeline automatically fetches an object's schema when you select it. This ensures the destination matches the source.
    
    Expand an object to view associated fields. Keep all fields selected to extract all available data, or deselect specific fields to exclude them from data extraction and schema replication.
    
11. Optional. Configure field-level data protection. After you expand an object, choose how to handle each field:
    
    - **Replicate as is (default)**: Data values at the source are replicated identically to the destination.
    - **Hash**: Hash sensitive data values in the column before syncing to your destination.
12. Click **Add object** again to add more objects using the same flow. You can repeat this step to include multiple Ellucian Banner objects in your pipeline.
    
13. Use the **Choose how to handle schema changes** drop-down menu to select a schema drift handling option:
    
    - **Auto-sync new fields**: Automatically detects and syncs new fields added in the source.
    - **Block new fields**: Keeps the schema fixed after the pipeline starts. You must add new fields manually. This option may cause the destination to fall out of sync if the source schema updates.
    
    Refer to [Schema replication and schema drift management](/en/data-orchestration/data-pipeline-recipe/concepts#schema-drift) for more information.
    
14. Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from Ellucian Banner to the destination.
    
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
       
    

## Object schema behavior

The Ellucian Banner connector extracts records from objects exposed through the Ethos Integration API. These objects define the schema used by the pipeline.

Workato infers schema and data types from the selected reference object at the time of configuration. The structure of each object must remain consistent to ensure accurate schema mapping and reliable data replication.
