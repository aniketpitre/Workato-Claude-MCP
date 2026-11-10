---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-netsuite2.md
description: >-
  Configure NetSuite2 as a data pipeline source to extract records through
  SuiteAnalytics Connect and sync them to your destination.
---

# Configure NetSuite2 as your data pipeline source

Set up NetSuite2 as a data pipeline source to extract and sync records into your destination using the SuiteAnalytics Connect service. This guide includes connection setup, pipeline configuration, and key behavior for working with NetSuite2 as a source.

## NetSuite2 features supported

The following features are supported when using NetSuite2 as a data pipeline source:

- Extract data using the SuiteAnalytics Connect service
- Support for full and incremental sync
- Field-level selection for object extraction
- Schema drift detection and handling
- Field-level data masking

## NetSuite2 prerequisites

You must have the following configuration and access:

- SuiteAnalytics Connect feature enabled in your NetSuite account
- Valid NetSuite Connect user with access to SuiteAnalytics
- Read access to the tables used in the pipeline

## How to connect

Workato uses the SuiteAnalytics Connect service for NetSuite2 integrations. Complete the following steps to create a NetSuite2 connection.

Connect to NetSuite2

NetSuite2 connections use the **SuiteAnalytics Connect** service. Ensure this feature is enabled in your NetSuite account before creating the connection.

Refer to [NetSuite documentation](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_3996274388.html) for steps to enable the Connect Service feature.

Complete the following steps to connect to **NetSuite2** as a data pipeline source. This connection allows the pipeline to extract and sync data from NetSuite2.

1. Select **Create > Connection** or press C twice.
   
2. Search for `NetSuite2` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
   ![NetSuite2 connection setup](/assets/connect-to-netsuite2.DnZ0ZcZW.png)_NetSuite2 connection setup_
   
4. Use the **Location** drop-down to select the project where you plan to store the connection.
   
5. Enter the **Server Datasource**. This is the NetSuite server datasource assigned to your account.
   
6. Enter the **Server Name**. This is the specific server that hosts your NetSuite instance.
   
7. Enter any required **Custom Properties**. These are additional properties defined in your NetSuite connector setup.
   
8. Enter your **User** credentials. This field accepts the NetSuite user ID used for integration access.
   
9. Enter your **Password** for the NetSuite account.
   
10. Click **Connect** to verify and establish the connection.
    

## Configure the pipeline

Ensure that the **SuiteAnalytics Connect** feature is enabled in your NetSuite account before you use NetSuite2 as a source. This feature allows the pipeline to access NetSuite data through the SuiteAnalytics framework.

Refer to [NetSuite documentation](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_3996274388.html) for details on enabling this feature.

Complete the following steps to configure NetSuite2 as your data pipeline source:

1. Select **Create > Data pipeline** or press C+I.
   
2. Enter a name for the data pipeline in the **Data pipeline name** field.
   
   ![Data pipeline setup](/assets/set-up-pipeline.Cxx6hIk2.png)_Data pipeline setup_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the data pipeline.
   
4. Click **Start building**.
   
5. Click the **Extract new/updated records from source app** trigger. This trigger defines how the pipeline retrieves data from the source application.
   
   ![Configure the Extract new/updated records from source app trigger](/assets/choose-source-app.B2OOUpgY.png)_Configure the Extract new/updated records from source app trigger_
   
6. Use the **Your Connected Source Apps** drop-down menu to select **NetSuite2**.
   
7. Choose the NetSuite2 connection you plan to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
   ![Choose a NetSuite2 connection](/assets/choose-netsuite-connection.BHjlXv3_.png)_Choose a NetSuite2 connection_
   
8. Click **Add object** to open the object wizard.
   
   ![Add object](/assets/add-netsuite-object.kTyM_YTe.png)_Add object_
   
9. Search or browse the list of available NetSuite2 objects. Select the objects you plan to sync and click **Add**.
   
10. Review and customize the schema for each selected object. When you select an object, the pipeline automatically fetches its schema to ensure the destination matches the source.
    
    ![Expand object](/assets/expand-object-netsuite.IWzJY0ND.png)_Expand object_
    
    You can expand any object to view its fields. Keep all fields selected to extract all available data, or deselect specific fields to exclude them from data extraction and schema replication.
    
11. Click **Add object** again to add more objects using the same flow. You can repeat this step to include multiple NetSuite2 objects in your pipeline.
    
12. Use the **Choose how to handle schema changes** drop-down menu to select a schema drift handling option:
    
    - **Auto-sync new fields**: Automatically detects and syncs new fields added in the source.
    - **Block new fields**: Keeps the schema fixed after the pipeline starts. You must add new fields manually. This option may cause the destination to fall out of sync if the source schema updates.
    
    Refer to [Schema replication and schema drift management](/en/data-orchestration/data-pipeline-recipe/concepts#schema-drift) for more information.
    
13. Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from NetSuite2 to the destination.
    
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
       
    

## Deleted records behavior

NetSuite2 pipelines handle deleted records differently depending on the sync type:

- **Full sync**: The pipeline includes recently deleted records that occurred shortly before the sync begins. The pipeline excludes historical deletions that occurred outside of this period. This prevents the destination from loading deleted records that weren't present in the destination table.
- **Incremental sync**: The pipeline tracks all deletions that occurred after the previous successful sync.

## Supported NetSuite2 records

The NetSuite2 connector supports most NetSuite records and tables exposed through the SuiteAnalytics Connect service. These typically include common entities such as transactions, customers, vendors, items, accounts, and other standard record types available in your NetSuite account.

Workato uses SuiteAnalytics Connect to retrieve metadata and record data for these tables, so the set of available records depends on your NetSuite instance configuration and role permissions.
