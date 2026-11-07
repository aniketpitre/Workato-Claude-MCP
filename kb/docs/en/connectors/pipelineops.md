---
url: 'https://docs.workato.com/en/connectors/pipelineops.md'
description: >-
  The PipelineOps by Workato connector lets you monitor and respond to data
  pipeline sync events, enabling alerting and custom workflows for pipeline
  health.
---

# PipelineOps by Workato

The **PipelineOps by Workato** connector allows you to monitor the execution status of data pipelines. You can use this connector to respond to sync completions, capture object-level errors, and trigger alert workflows.

## How to connect to PipelineOps by Workato

You don't need to provide credentials to connect to this connector. Workato uses your current workspace authorization. Complete the following steps to create the connection:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select the `PipelineOps by Workato` connector.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to PipelineOps by Workato](/assets/connect-pipeline-ops.DvF0P1bn.png)_Connect to PipelineOps by Workato_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Click **Connect**.
   

## Supported triggers

The following trigger is supported for this connector:

- [Sync completed trigger](/en/connectors/pipelineops/sync-completed): Runs after each sync completes in the selected data pipeline. You can configure it to trigger on every sync completion or failed syncs.

Workato recommends using **Every sync completion** to ensure your workflows detect all failure scenarios.

## Example use cases

You can use this connector to respond to pipeline sync results in real time. For example, you might send email or chat alerts when any object fails during a sync, log sync statuses to a monitoring dashboard, or trigger corrective automations when issues occur.

Refer to the [Monitor data pipelines using recipes](/en/data-orchestration/data-pipeline-recipe/pipeline-triggers) guide for a step-by-step example.

---
