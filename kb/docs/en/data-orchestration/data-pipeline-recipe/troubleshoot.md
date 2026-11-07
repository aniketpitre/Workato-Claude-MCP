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
