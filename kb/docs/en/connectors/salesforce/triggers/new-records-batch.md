---
url: >-
  https://docs.workato.com/en/connectors/salesforce/triggers/new-records-batch.md
description: >-
  This trigger monitors Salesforce for newly created records and retrieves them
  in batches.
---

# Salesforce - New records trigger (batch)

This trigger monitors Salesforce for newly created records and retrieves them in batches.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the object type to monitor. |
| Fields to retrieve | Select the fields to retrieve from the object. Workato retrieves all fields by default. Entering specific fields to retrieve improves recipe performance and mitigates [schema errors](/en/connectors/salesforce/troubleshoot-runtime#schema-errors). |
| SOQL WHERE clause | Enter a SOQL query to filter events by. For example: `StageName = 'Closed Lost' AND IsClosed = false`. Refer to the [SOQL](/en/connectors/salesforce/salesforce-soql) guide for more information. |
| Batch size | Enter the maximum number of records to contain in each batch. The default value is `100` and the maximum is `2000`. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output fields | Description |
| --- | --- |
| Range | The range of records retrieved in the current batch. |

Additional outputs load dynamically based on your selected **Object** and **Fields to retrieve**. Refer to Salesforce's [Overview of Salesforce Objects and Fields](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_concepts.htm) guide for more information on available objects and fields.
