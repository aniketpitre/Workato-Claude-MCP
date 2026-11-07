---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-marketo.md
description: >-
  Configure Marketo as a data pipeline source to extract object records through
  the REST API and sync them to your destination.
---

# Configure Marketo as your data pipeline source

Set up Marketo as a data pipeline source to extract and sync records into your destination. This guide includes connection setup, pipeline configuration, and key behavior for working with Marketo as a source.

Workato uses the Marketo REST API to extract object data for pipeline syncs.

## Features supported

The following features are supported when using Marketo as a data pipeline source:

- Extract data using the Marketo REST API
- Support for full and incremental sync
- Field-level selection for object extraction
- Schema drift detection and handling
- Field-level data masking

## Prerequisites

You must have the following configuration and access:

- A custom service registered in your Marketo Admin console
- The REST API endpoint for your Marketo instance
- Client ID and client secret from the custom service
- Read access to the objects used in the pipeline

## How to connect

Complete the following steps to connect to **Marketo** as a data pipeline source. This connection allows the pipeline to extract and sync data from your Marketo instance.

Connect to Marketo

1. Select **Create > Connection** or press C twice.
   
2. Search for `Marketo` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
   ![Marketo connection setup](/assets/connect-to-marketo.xSKtJ_gH.png)_Marketo connection setup_
   
4. Use the **Location** drop-down to select the project where you plan to store the connection.
   
5. Enter the **REST Endpoint**. This URL must match your Marketo instance’s Admin/Web Services REST API endpoint.
   
6. Enter the **Custom Service client ID** associated with your Marketo custom service. Refer to the [Marketo Engage Developer Documentation](https://developers.marketo.com/rest-api/authentication/#creating_a_custom_service) to create a custom service in Marketo.
   
7. Enter the **Custom Service client secret** for the Marketo client ID.
   
8. Click **Connect** to verify and establish the connection.
   

## Configure the pipeline

Complete the following steps to configure Marketo as your data pipeline source:

1. Select **Create > Data pipeline** or press C+I.
   
2. Enter a name for the data pipeline in the **Data pipeline name** field.
   
   ![Data pipeline setup](/assets/set-up-pipeline.Cxx6hIk2.png)_Data pipeline setup_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the data pipeline.
   
4. Click **Start building**.
   
5. Click the **Extract new/updated records from source app** trigger. This trigger defines how the pipeline retrieves data from the source application.
   
   ![Configure the Extract new/updated records from source app trigger](/assets/choose-source-app.B2OOUpgY.png)_Configure the Extract new/updated records from source app trigger_
   
6. Use the **Your Connected Source Apps** drop-down menu to select **Marketo**.
   
7. Choose the Marketo connection you plan to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
   ![Choose a Marketo connection](/assets/choose-marketo-connection.BTS0WjXx.png)_Choose a Marketo connection_
   
8. Click **Add object** to open the object wizard.
   
   ![Add object](/assets/add-marketo-object.Do0JS55t.png)_Add object_
   
9. Search or browse the list of available Marketo objects. Select the objects you plan to sync and click **Add**.
   
   ![Select objects](/assets/select-marketo-object.BSLfL0dT.png)_Select objects_
   
10. Review and customize the schema for each selected object. When you select an object, the pipeline automatically fetches its schema to ensure the destination matches the source.
    
    ![Expand object](/assets/expand-object-marketo.UGROjLpm.png)_Expand object_
    
    You can expand any object to view its fields. Keep all fields selected to extract all available data, or deselect specific fields to exclude them from data extraction and schema replication.
    
11. Click **Add object** again to add more objects using the same flow. You can repeat this step to include multiple Marketo objects in your pipeline.
    
12. Use the **Choose how to handle schema changes** drop-down menu to select a schema drift handling option:
    
    - **Auto-sync new fields**: Automatically detects and syncs new fields added in the source.
    - **Block new fields**: Keeps the schema fixed after the pipeline starts. You must add new fields manually. This option may cause the destination to fall out of sync if the source schema updates.
    
    Refer to [Schema replication and schema drift management](/en/data-orchestration/data-pipeline-recipe/concepts#schema-drift) for more information.
    
13. Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from Marketo to the destination.
    
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
       
    

## Supported Marketo objects

The connector supports common Marketo objects, including **Leads**, **Activities**, and **Programs**. Workato uses the Marketo REST API to query and extract records.
