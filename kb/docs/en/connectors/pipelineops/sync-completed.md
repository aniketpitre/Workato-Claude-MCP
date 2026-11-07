---
url: 'https://docs.workato.com/en/connectors/pipelineops/sync-completed.md'
description: >-
  The Sync completed trigger initiates a recipe in real-time after a pipeline
  sync completes.
---

# PipelineOps by Workato - Sync completed trigger (real-time)

The **Sync completed** trigger initiates a recipe in real-time after a data pipeline completes its sync. You can use this trigger to orchestrate actions based on the results of your pipeline runs, such as sending alerts, logging sync statuses, or triggering downstream processes.

This trigger only monitors scheduled syncs (full or incremental). Re-syncs are excluded.

## Input

| Input field | Description |
| --- | --- |
| Data pipeline | Choose the pipeline to monitor. Only pipelines configured in your project appear. |
| Trigger on | Select **Every sync completion** to capture all syncs, or **Failed syncs** to monitor only failed ones. |

Workato recommends using **Every sync completion** to ensure you capture all failure scenarios, including object-level issues.

## Output

| Output field | Description |
| --- | --- |
| Pipeline ID | ID of the data pipeline. |
| Sync ID | ID of the specific sync run. |
| Source | Source system of the data pipeline. |
| Destination | Destination system of the data pipeline. |
| Started at | Timestamp when the sync began. |
| Completed at | Timestamp when the sync finished. |
| Total duration (ms) | Total duration of the sync in milliseconds. |
| Total rows extracted | Number of rows extracted during the sync. |
| Total rows loaded | Number of rows loaded into the destination. |
| Total rows inserted | Number of rows inserted in the destination. |
| Total rows updated | Number of rows updated in the destination. |
| Sync state | Final status of the sync. |
| Objects | List of pipeline objects and their individual sync statuses. |

---
