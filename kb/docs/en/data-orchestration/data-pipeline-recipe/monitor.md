---
url: 'https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/monitor.md'
description: >-
  Monitor and manage Workato data pipelines to track sync status, review object
  runs, analyze performance, and manage connections.
---

# Monitor and manage data pipelines

Data pipelines provide the following options to monitor sync activity, track performance, and manage configurations:

- **[Monitor pipeline status](#pipeline-statuses)**: View real-time sync activity and historical trends.
  
- **[View synced objects and statuses](#view-synced-objects-and-statuses)**: Check the current sync status of each object and trigger re-syncs as needed.
  
- **[Monitor object runs](#object-runs)**: Track sync progress, review errors, and analyze performance metrics.
  
- **[Manage connections](#view-and-manage-connections)**: Verify existing connections, switch sources or destinations, and update credentials.
  

## Pipeline statuses

After you start the pipeline, it syncs selected objects in parallel and continuously updates the destination. The first run loads historical data into the destination.

The pipeline status sidebar provides real-time updates on sync progress and pipeline activity. It displays different details based on the pipeline's status:

**Sync in progress**

The sidebar displays **Syncing now (%)**, which indicates the overall sync progress as a percentage. It also tracks the number of synced objects out of the total selected.

![Data pipeline activity status during sync](/assets/pipeline-syncing-now.DYpPkfke.png)_Data pipeline activity status during sync_

If the current sync runs longer than expected and overlaps with the next scheduled sync, the pipeline skips the next sync. The sidebar shows the time when the skip occurred.

**Sync completed**

After a sync finishes, the sidebar updates with the last sync time and the number of successfully synced objects. It also displays the time until the next scheduled sync.

The sync activity section summarizes successful and failed runs over the last 30 days.

![Data pipeline activity status during completed sync](/assets/pipeline-syncing-completed.nidKWwmm.png)_Data pipeline activity status during completed sync_

**Paused pipeline**

The sidebar updates to **Stopping pipeline** when you select **Stop pipeline**. It continues to display the last sync time and retains the activity summary for the last 30 days.

![Stop pipeline](/assets/pause-pipeline.CyT1yqSw.png)_Stop pipeline_

**Inactive pipeline**

The sidebar displays **Inactive pipeline** when the pipeline isn't active. No sync activity occurs in this state.

Select **Start pipeline** to activate it. After activation, the pipeline enters a syncing state or prepares for the first sync.

![Inactive pipeline](/assets/stopped-inactive-pipeline.N3N44qz_.png)_Inactive pipeline_

## Monitor orchestration activity

The data orchestration dashboard allows you to monitor pipeline run status, sync duration, and data volumes across all pipelines in your workspace. The dashboard displays 30 days of activity, including trends in run outcomes, row counts, and duration averages. You can filter by pipeline status, explore daily run timelines, and open specific syncs to investigate issues.

Go to **Platform > Data Orchestration** in Workato to open the dashboard.

![Data orchestration dashboard](/assets/orchestration-dashboard.CXjpYmea.gif)_Data orchestration dashboard_

Refer to the [Monitor orchestration activity](/en/data-orchestration#monitor-orchestration-activity) section for more information.

## View synced objects and statuses

The **Objects** tab displays all objects selected in the pipeline and their current sync statuses. Use this tab to monitor sync status and re-sync specific objects when needed.

![Objects tab](/assets/object-tab.PRS0RX77.png)_Objects tab_

Each row displays the following details:

- Object name
  
- The name of the source object.
  
- Last status
  
- The result of the most recent sync for this object. Workato marks it as **Synced**, **Failed**, **Syncing...**, **Re-syncing...**, or **Queued**.
  
- Re-sync
  
- Hover over the object row or open the object detail panel to access the **Re-sync** option. This triggers a one-time sync for that object. It extracts and loads the object data immediately, without waiting for the next scheduled sync.
  
  ![Re-sync object](/assets/resync-object.CIxOmFt1.png)_Re-sync object_
  

The sidebar summarizes the following pipeline activity:

- Time until the next sync
  
- Time and result of the last sync
  
- Total successful and failed runs in the last 30 days
  
- Number of object re-syncs in progress or queued
  
  ![Object sidebar](/assets/object-sidebar.C-sZkpIO.png)_Object sidebar_
  

## Object runs

The **Runs** tab provides real-time insights into execution progress, errors, and performance. Use this tab to track object run status, review the execution history, analyze pipeline activity, and troubleshoot failures.

Complete the following steps to access and utilize the **Runs** tab:

1. Go to the **Runs** tab to view execution logs, pipeline status, and performance statistics.
   
   ![Runs tab](/assets/pipeline-objectsync-connections-settings.DFXH_i3R.png)_Runs tab_
   
2. Review the execution history table, which lists all object runs and their statuses.
   
   ![Object syncs tab for a running pipeline](/assets/objectsyncs-table-and-pipeline-status.3BT0m3Tq.png)_Object syncs page for a running pipeline_
   
   Each row in the execution history table provides the following details:
   
   - Start time
     
   - Displays when the run for that object began.
     
   - Object
     
   - The name of the object extracted from the source application.
     
   - Sync type
     
   - Indicates whether the run was an incremental sync or full sync. Refer to the [Sync types and execution](/en/data-orchestration/sync-types) guide to learn more about sync types.
     
   - Rows extracted
     
   - Lists the number of records retrieved from the source during the run.
     
   - Rows loaded
     
   - Displays how many records were successfully written to the destination.
     
   - Duration
     
   - Total time taken to complete the run.
     
3. Use the following filters to refine the table and locate specific object runs:
   
   ![Filter the runs table](/assets/filter-sort-sync-table.FpRS-3XF.png)_Filter the runs table_
   
   - Search objects
     
   - Enter the name of an object to find matching runs.
     
   - Status
     
   - Filter by execution status, such as **Successful**, **Syncing**, **Failed**, or **Canceled**.
     
   - Sync type
     
   - Filter by **Incremental** or **Full** syncs.
     
   - Period
     
   - Define a time period to display syncs from a specific timeframe.
     

### Sync types

The pipeline automatically applies different sync types based on the current state and configuration:

**Full sync:** Runs once when the pipeline starts. It loads either all historical records from the source or only from a specific date, based on the configuration settings. This is a full sync that occurs during the first pipeline execution.

**Incremental sync**: Runs at scheduled intervals to track and apply changes from the source.

**Re-sync**: A one-time manual sync for a specific object. It reloads current data for that object immediately, outside the regular schedule.

Refer to the [Sync types and execution](/en/data-orchestration/sync-types) guide for more details.

## View and manage connections

The **Connections** tab displays the source and destination connections used in the data pipeline.

![Connections tab](/assets/connections-tab.DFCnZ7Th.png)_Connections tab_

Each connection displays its name, authentication type, and configuration details.

You can switch a connection only when the pipeline isn't running. Stop the pipeline before you change the connection if it's active.

To switch a connection:

1. Select the source or destination to update.
   
2. Click **Switch**.
   
3. Choose a different connection from the list.
   

The pipeline applies the new connection immediately for all future syncs.

## Concurrency

The pipeline processes selected objects in parallel during each scheduled sync. Workato automatically manages concurrency and optimizes it based on system availability.

The pipeline processes up to 100 objects in parallel per batch. Pipelines with more than 100 objects are processed in successive batches. You can't manually configure concurrency settings.

## Edit pipeline

Click **Edit pipeline** to modify sync frequency, source objects, and field settings. Changes apply to future syncs and don't affect previously synced data.

![Edit data pipeline](/assets/edit-data-pipeline.bNcHtQyJ.png)_Edit data pipeline_

## Pause and resume pipelines

Select **Stop pipeline** to stop all syncs while the pipeline remains intact. If the pipeline is mid-sync, it stops immediately. Objects that complete extraction and loading count as successful runs. The pipeline cancels any remaining runs and marks them as **Canceled**. These runs don't sync data to the destination.

The pipeline doesn't extract data while stopped. Logs and historical run data remain available for reference.

![Stop data pipeline](/assets/stop-pipeline.DnRRb5rb.png)_Stop data pipeline_

Select **Start pipeline** to resume syncs. The pipeline immediately resumes with the next incremental sync regardless of the schedule. After this run completes, it follows the configured sync frequency. The system doesn’t retry any syncs missed while the pipeline was paused, but it catches up on the missed data from those canceled runs during the next successful sync. If you update the sync frequency while the pipeline is paused, the pipeline applies the updated configuration when it resumes.

If the pipeline uses **Block new fields**, schema changes made while it's paused don't apply automatically. These changes take effect after the pipeline resumes.

### Deployment considerations

You can export and deploy data pipelines using RLCM manifests or deployment packages.

![Data pipeline manifest](/assets/pipeline-manifest.CEMOKqT7.png)_Data pipeline manifest_

Workato blocks deployment if the pipeline doesn't include valid source and destination connections. This ensures the system can load schemas correctly and avoids errors during configuration. You must include all required connections before you can export or deploy a pipeline.

If you plan to use different connections in production, deploy the pipeline with test connections first, then switch to the appropriate production connections in the target environment.

Workato also blocks deployment if the same pipeline is already active in the target environment. You must stop the running pipeline before deploying an updated version to the same environment.

## Data pipeline triggers in recipes

You can use the [PipelineOps by Workato](/en/connectors/pipelineops) connector to trigger recipes when a data pipeline sync completes. This allows recipes to run immediately after data loads into the destination.

Use these triggers to run post-load transformations, monitor pipeline activity, and send customized error alerts or status reports.

Refer to the [Monitor data pipelines using recipes](/en/data-orchestration/data-pipeline-recipe/pipeline-triggers) guide for a step-by-step example.

## Troubleshoot failed runs

The **Runs** tab displays detailed error information for each failed object run. Failed runs appear in the run history with a **Failed** status.

![Failed runs](/assets/failed-runs.fUc2sMg8.png)_Failed runs_

Click a failed run to open its details. The right-hand panel displays the `Error` type, `Error ID`, and `Run ID`. You can also select the source trigger or destination action to view specific error messages for that run.

![Failed run details](/assets/failed-run-details.B3xdWqf-.png)_Failed run details_

Refer to the [Troubleshoot your data pipelines](/en/data-orchestration/data-pipeline-recipe/troubleshoot) for more information about how to identify and troubleshoot errors.

## Review pipeline logs

Workato's logging service captures detailed information for every pipeline sync. Use these logs to trace pipeline activity, confirm successful executions, and troubleshoot errors across syncs and individual object runs.

![Data pipeline logs](/assets/pipeline-logs.BGe6AcxQ.png)_Data pipeline logs_

Complete the following steps to locate specific logs:

1. Go to **Tools > Logs**
   
2. Use the following filters to locate specific logs:
   
   - Period
     
   - Choose a preset like **Last 30 days** or define a custom date range.
     
   - Log type
     
   - Select **Data pipelines** to view logs related to pipeline activity.
     
   - Log level
     
   - Select **INFO** to view successful events or **ERROR** to investigate failures.
     
   - Pipeline ID
     
   - Filter logs by the unique identifier of a specific pipeline.
     
   - Run ID
     
   - Filter logs by the unique identifier of a specific run.
     

### Common log types

Workato generates structured log events for each stage of the pipeline sync process. These events help you track sync activity and identify issues at the object level:

- `PIPELINE_SYNC_START`: The pipeline started a new sync across all selected objects.
- `OBJECT_RUN_START`: The pipeline started processing an object run.
- `OBJECT_SCHEMA_SYNCHRONISATION_COMPLETED`: The pipeline completed schema updates for one object run.
- `OBJECT_EXTRACTION_COMPLETED`: The pipeline finished extracting data from the source for one object run.
- `OBJECT_LOADING_COMPLETED`: The pipeline finished loading data into the destination for one object run.
- `OBJECT_MERGE_COMPLETED`: The pipeline merged incremental changes into the destination for one object run.
- `OBJECT_RUN_COMPLETED`: The pipeline completed all operations for one object run.
- `PIPELINE_SYNC_COMPLETED`: The pipeline completed a sync across all selected objects.
- `PIPELINE_SYNC_CANCEL`: The pipeline stopped before completing the sync.

### View log entry details

Click any log row to view its full context. Each log entry includes values such as `pipeline_id`, `pipeline_sync_id`, and `workato_pipeline_id` to identify the pipeline and corresponding sync.

![View log details](/assets/view-log-details.RDkhiPVS.png)_View log details_

Log entries also capture the source and destination systems, object names, record counts, and any error messages for failed object runs.

#### Example log entry

The following example displays a `PIPELINE_SYNC_COMPLETED` log entry. It includes the sync durations, pipeline identifiers, systems involved, and object and record metrics:

```json
{
  "context": {
    "event": "PIPELINE_SYNC_COMPLETED",
    "start_time": "2025-04-15T14:00:17.088Z",
    "end_time": "2025-04-15T14:03:45.562Z",
    "pipeline_id": "dpr-ARQRRwxR-w4xLrt",
    "workato_pipeline_id": "1275",
    "pipeline_sync_id": "019639c0-1ae3-77fd-8eb9-14b20e4fed38",
    "source": "SALESFORCE-70612",
    "destination": "SNOWFLAKE-72522",
    "duration": "208 seconds"
  },
  "number_of_objects": 8,
  "number_of_objects_successful": 8,
  "number_of_objects_failed": 0,
  "number_of_records_extracted": 900,
  "number_of_records_loaded": 900
}
```

---

---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/pipeline-triggers.md
description: >-
  Build Workato recipes that monitor data pipelines, automate error handling,
  and send alerts when object syncs fail.
---

# Monitor data pipelines using recipes

You can use recipes to orchestrate monitoring workflows for your data pipelines. These recipes help you respond to pipeline sync results, automate error handling, and send alerts when syncs fail.

## Use case: Monitor pipeline failures

A common use case is error monitoring. You can configure a recipe to notify teams when any object in a pipeline fails to sync.

Workato recommends triggering recipes on every sync completion, rather than failed syncs. This ensures object-level failures are captured. Failed syncs only detect sync-level issues, which may exclude failures within individual objects.

### Configure pipeline triggers in recipes

Complete the following steps to build a pipeline monitoring recipe:

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create connections for PipelineOps by Workato:
   
   Set up your PipelineOps connection
   
   ### Set up your PipelineOps connection
   
   1. Select **Create > Connection** or press C twice.
      
   2. Search for `PipelineOps by Workato` and select it as your app.
      
   3. Provide a name for your connection in the **Connection name** field.
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Click **Connect**.
      
   
4. Set up your Gmail connection
   
   ### Set up your Gmail connection
   
   Workato supports two types of connections to Gmail:
   
   - [OAuth 2.0 authentication](#authentication-oauth)
   - [Service account authentication](#connect-to-a-service-account-in-workato)
   
   #### OAuth 2.0 authentication
   
   Complete the following steps to set up an OAuth 2.0 connection:
   
   1. Sign in to your Workato account and go to the project where you plan to add your Gmail connection.
      
   2. Click **Create > Connection** (or press C twice), then select **Gmail** as your connection.
      
   3. Provide a **Connection name** that uniquely identifies the Gmail connection instance.
      
   4. Click the **Authentication type** menu and select **OAuth 2.0**.
      
   5. Optional. Click **Advanced settings** and select additional **OAuth 2.0 scopes**. If left blank, the following scopes are requested:
      
      - **See your primary Google Account email address**
      - **See and edit your email labels**
      - **Send email on your behalf**
      - **View your email messages and settings**
      - **Read, compose, and send emails from your Gmail account**
   6. Click **Sign in with Google** and sign in to your Google account to complete the setup.
      
   
   #### Connect to a service account in Workato
   
   Complete the following steps to set up a service account connection:
   
   1. Sign in to your Workato account and navigate to the project where you plan to add your Gmail connection.
      
   2. Click **Create > Connection** (or press C twice), then select **Gmail** as your connection.
      
   3. Select the **Authentication type** drop-down menu.
      
   4. Click **Sign in with Google** and sign in to your Google account to complete the setup.
      
   
5. Go back to your project and click **Create > Recipe** or press C+R.
   
   ![Create a new recipe](/assets/create-recipe-standard.CiyoivKN.png)_Create a new recipe_
   
6. Click **Pick a starting point**, then select **Select an app and trigger event**.
   
7. Set up your data pipeline sync trigger
   
   ### Set up the data pipeline trigger
   
   This trigger monitors the sync status of a pipeline. It fires every time a sync completes.
   
   1. Search for `PipelineOps by Workato` and select it as your app.
      
   2. Select the **Sync completed** real-time trigger.
      
      ![Set up the data pipeline trigger](/assets/set-up-pipeline-trigger.NR6OUdAC.png)_Set up the data pipeline trigger_
      
   3. Choose the **Data pipeline** you plan to monitor.
      
   4. Select **Every sync completion** in the **Trigger on** field .
      
      Workato recommends selecting **Every sync completion** instead of **Failed syncs**. This ensures you capture object-level failures, which may not be tracked under sync-level failures.
      
   
8. Set up your trigger condition
   
   ### Set up a trigger condition
   
   You can set a trigger condition directly in the trigger setup.
   
   1. Enable the **Set trigger condition** toggle.
      
   2. Map the Sync state (Step 1) datapill to the **Trigger data** field.
      
      ![Set up your trigger condition](/assets/set-up-trigger-condition.CaClIN8a.png)_Set up your trigger condition_
      
   3. Set **Condition** to `contains`.
      
   4. Set **Value** to `ERROR`.
      
   
9. Click **\+ Add step**, then select **Action in an app**.
   
   ![Select Gmail](/assets/set-up-pipeline-gmail.CKxyki1v.png)_Select Gmail_
   
10. Search for `Gmail` and select it as your app.
    
11. Set up a Gmail alert
    
    ### Send an email when a pipeline sync fails
    
    This step sends an email from your connected Gmail account when a pipeline sync fails.
    
    1. Select the **Send email** action.
       
    2. Enter one or more recipients in the **To** field. Separate multiple email addresses with commas.
       
       ![Configure your Gmail action](/assets/configure-gmail-pipeline.QER_-8b8.png)_Configure your Gmail action_
       
    3. Enter a subject in the **Subject** field, such as `Pipeline Sync Failure Alert`.
       
    4. Select **Text** or **HTML** in the **Email type** field.
       
    5. Enter the message body in the **Message** field.

---
