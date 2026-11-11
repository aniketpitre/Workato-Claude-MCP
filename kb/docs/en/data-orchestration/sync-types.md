---
url: 'https://docs.workato.com/en/data-orchestration/sync-types.md'
description: >-
  Learn the data pipeline sync types in Workato: full sync, incremental sync
  with CDC, and object re-sync to keep destinations up to date.
---

# Sync types

Data pipeline recipes use the following sync types:

- **[Full sync](#full-sync)**: Loads historical data when the pipeline starts. Objects that use full sync run it on every scheduled run.
- **[Incremental sync (CDC)](#incremental-sync-cdc)**: Captures records created or updated since the last successful sync, on a schedule.
- **[Object re-sync](#object-re-sync)**: Manually triggers a sync for a specific object outside the regular pipeline schedule.

Each sync type ensures the destination remains accurate, up to date, and aligned with the source application.

## Full sync

The full sync runs when the pipeline starts. It loads historical data from the selected source objects into the destination. Objects that use full sync run a full sync on every scheduled run. An object uses full sync if you set its sync mode to **Full sync**, or if it doesn't support incremental sync, for example because the source doesn't expose a usable cursor or primary key.

The pipeline fetches all records by default when the **When first started, this pipeline should pick up records from** field is blank. You can also set a specific start date to limit the sync window. Sources such as Outreach and Sage Intacct apply this date only to objects that support incremental sync. Refer to your source application's configuration guide for its behavior.

The pipeline replicates the source schema, creates new tables in the destination, and processes each object as a separate run in parallel. Data warehouse destinations also use a stage and temporary tables to load data. For example, the pipeline creates a permanent stage in Snowflake to upload data before it loads the data into destination tables.

The initial full sync assumes the destination is empty.

The pipeline labels each run as a full sync during the initial run because it processes all records. This sync runs automatically when the pipeline starts and doesn't require any manual setup or selection.

### How a full sync works

The full sync extracts all data from the **When first started, this pipeline should pick up records from** timestamp onwards, where the source applies it. The pipeline retrieves all available records from the source if you leave this field blank.

The pipeline creates one run per object and loads data into newly created tables at the destination.

The **Runs** tab displays each object's status as **In Progress** until the pipeline loads all records. Workato doesn't provide an estimated completion time because sync duration depends on data volume. Objects that use incremental sync transition to incremental syncs after the initial load completes.

Full syncs after the initial load merge source records into the existing destination tables on the object's primary key. The pipeline inserts new records and updates existing records. It also sets `_workato_is_deleted` to `true` on records that no longer exist in the source, if the object supports delete tracking. It doesn't remove these rows, so the row count in the destination table can stay the same after a full sync even when records were deleted in the source. Exclude rows where `_workato_is_deleted` is `true` in queries, reports, and downstream transformations. Refer to [Delete tracking](/en/data-orchestration/data-pipeline-recipe/concepts#delete-tracking) for more information.

Objects without a primary key don't merge. The pipeline overwrites the entire destination table on every full sync for these objects, so rows deleted in the source are removed from the destination with no deleted-row history.

> **FULL SYNC COMPLETION**
> 
> The pipeline doesn't run incremental syncs until the full sync completes.

## Incremental sync (CDC)

The pipeline runs incremental syncs at scheduled intervals after the full sync completes, to track and apply changes from the source system for objects that use incremental sync.

### How an incremental sync works

The pipeline extracts records created or updated since the last successful sync, based on each object's incremental cursor, such as a last-modified timestamp. Sources such as Braintree and Apollo.io also re-read a recent time window on each run to capture changes the cursor doesn't reflect. Deleted records sync only for objects that support [delete tracking](/en/data-orchestration/data-pipeline-recipe/concepts#delete-tracking). The pipeline detects schema changes, such as new fields or updated field sizes, and updates the destination tables before it adds records to the destination. The pipeline processes each object as a separate run and syncs all selected objects in parallel.

The pipeline doesn't reprocess historical data for newly added fields. It captures values only from the time it detects the field. It doesn't start a new incremental sync until the previous one finishes. The pipeline skips the next scheduled run if a sync runs longer than expected.

The **Runs** tab tracks each execution's progress and duration. Refer to [Object runs](/en/data-orchestration/data-pipeline-recipe/monitor#object-runs) for more information on how to monitor syncs in real time.

> **INCREMENTAL SYNC EXECUTION**
> 
> The pipeline skips the next scheduled sync if the current one is still in progress.

## Object re-sync

An object re-sync extracts and loads data for a specific object independently of the regular pipeline schedule. You can trigger this manually from the **Objects** tab.

Use object re-syncs to retry failed runs, reload individual objects, or ensure the destination contains the most recent data for a specific object. You don't need to restart the pipeline.

### How an object re-sync works

The pipeline extracts data for an object from the source and loads it into the destination when you select **Re-sync** for that object. This sync overwrites existing records for that object only. It doesn't affect other objects or change the pipeline schema.

The pipeline doesn't delete or reset any destination tables before an object re-sync. The operation runs immediately and doesn't wait for the next scheduled sync.

> **OBJECT RE-SYNC SCOPE**
> 
> Object re-syncs apply only to the selected object. They don't affect scheduled syncs or change the pipeline's sync configuration.

---

---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/troubleshoot.md
description: >-
  Troubleshoot Workato data pipelines by reviewing failed object runs and
  investigating error details on the Runs tab.
---

# Troubleshoot data pipelines

## Identify a data pipeline issue

Use the **Runs** tab to review failed object runs and access detailed error information.

Complete the following steps to locate and investigate a failed run:

1. Click the **Runs** tab to view a list of object runs and their statuses.
   
   ![Runs tab](/assets/pipeline-objectsync-connections-settings.DFXH_i3R.png)_Runs tab_
   
2. Filter the table by **Failed** status to find unsuccessful runs.
   
   ![Runs tab](/assets/failed-runs.fUc2sMg8.png)_Filter runs_
   
3. Click a failed run to open its details in the right-hand panel. The panel displays information such as the `Error` type, `Source`, `Error ID`, and `Run ID`.
   
   ![View sync error](/assets/view-sync-error.NCY_-bPm.png)_View sync error details_
   

## Resolve object sync errors

Issues in the source or destination system often cause object run errors. The pipeline retries failed object runs in subsequent syncs.

Fix source-side errors to allow the pipeline to recover data in the next scheduled sync.

For example, a `503 Service Unavailable` error indicates an issue with the target API. [Test the endpoint](/en/api-mgmt/testing-endpoints#test-recipe-endpoint) with tools such as Postman or curl to send raw content to the endpoint and verify the response.

Refer to the [API endpoints management FAQs](/en/api-mgmt/api-endpoints-management-faqs) for more information.

## Deleted fields in the source

Data pipelines retain fields in the destination for historical reference when they are deleted in the source application.

To remove a deleted field and its data entirely, manually delete the column from the destination table. This action doesn't affect the pipeline's operation.

## Salesforce integration considerations

Consider the following behaviors and limitations when you use Salesforce as a source in a Workato data pipeline:

### Object support

Workato pipelines can synchronize only queryable Salesforce objects. The pipeline can't access or extract data from an object that isn't queryable.

Many supported objects work with Salesforce's `getUpdated()` and `getDeleted()` APIs, which let the pipeline detect changes for incremental syncs. Some queryable objects don't support these APIs, so the pipeline can't track updates or deletions for them.

Some Salesforce objects don't include fields like `SystemModstamp` or `IsDeleted`, which are required for incremental syncs and deletion tracking. Workato excludes these objects from the pipeline configuration because the pipeline can't support them without these fields.

### Unsupported fields

Workato doesn't support fields with complex types such as base64 or embedded JSON. These fields don't appear in the object field selection menu when you configure your pipeline.

### Schema handling

Workato pipelines don't update the destination schema when field data types change in Salesforce. If you change a field's type, you must update the schema manually in Snowflake.

Field size changes behave differently. If you increase a field's size in Salesforce, the pipeline reflects the new size in the destination. If you decrease the field's size, the destination column size remains unchanged.

### Deleted records

Salesforce moves deleted records to the recycle bin and retains them for 15 to 30 days, depending on the organization's settings. During this period, the pipeline captures and syncs deletions to the destination.

After Salesforce purges these records, the pipeline can't detect or sync the deletions. Deleted records remain in the destination if the pipeline runs after the purge. Schedule the pipeline to sync frequently enough to capture deletions before the purge to avoid this issue.

## Snowflake integration considerations

Consider the following behaviors and limitations when you use Snowflake as a destination in a Workato data pipeline:

### Trace records in the destination

Workato adds tracking columns to each destination table in Snowflake to support run identification and deletion logic:

- `_workato_run_id`: Identifies the run that inserted each record. Use this column to trace unexpected data, isolate specific runs, and correlate data with logs to identify the pipeline that processed it.
- `_workato_is_deleted`: Tracks deletions for supported objects.

If multiple pipelines write to the same schema, `_workato_run_id` helps expose overlaps or conflicts across runs.

### Permissions

A Snowflake connection must have permission to create and modify tables, create a stage, and perform staging operations to run a pipeline successfully.

### Table and staging behavior

Workato creates a permanent stage in Snowflake to upload data. It also creates temporary tables to stage updates before it merges them into destination tables.

### Connection setup

Create a new [Snowflake connection](/en/connectors/snowflake#how-to-connect-to-snowflake-on-workato) for your data pipeline. You must specify the schema you plan to use during connection setup. This field defaults to the public schema if left blank.

### Key-value authentication

Workato doesn't support or recommend using key-value pair authentication with Snowflake connections. Use standard authentication methods instead.

---
