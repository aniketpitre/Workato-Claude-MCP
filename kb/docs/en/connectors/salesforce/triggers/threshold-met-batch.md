---
url: >-
  https://docs.workato.com/en/connectors/salesforce/triggers/threshold-met-batch.md
description: >-
  This trigger monitors Salesforce for when the number of newly created objects
  reaches a threshold you specify.
---

# Salesforce - Threshold met for new records created trigger (batch)

This trigger monitors Salesforce for when the number of newly created objects reaches a threshold you specify. When Salesforce reaches the new object threshold, Workato triggers a job, retrieves the newly created objects in batches, and waits for the number of new jobs to reach the threshold again.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the object type to monitor. |
| Threshold | Enter the number of records that must be created in Salesforce to trigger a new job. |
| Fields to retrieve | Select the fields to retrieve from the object. Workato retrieves all fields by default. Entering specific fields to retrieve improves recipe performance and mitigates [schema errors](/en/connectors/salesforce/troubleshoot-runtime#schema-errors). |
| Batch size | Enter the maximum number of records to contain in each batch. The minimum value for this field is `1` and the maximum is `10000`. Salesforce records with many custom fields require smaller batch sizes. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output fields | Description |
| --- | --- |
| Job ID | The Salesforce ID of the job. |
| Batch ID | The Salesforce ID of the batch. |
| State | The current state of the batch. For example: `Open` or `Closed` |
| Created date | The date and time the batch was created. |
| Number of records processed | The number of records processed. |
| Number of records failed | The number of records that failed to process. |
