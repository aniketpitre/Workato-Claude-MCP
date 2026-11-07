---
url: >-
  https://docs.workato.com/en/connectors/salesforce/triggers/export-new-updated-records.md
description: >-
  This trigger retrieves Salesforce records created or updated since the last
  job as a CSV stream.
---

# Salesforce - Export new/updated records trigger

This trigger monitors Salesforce for newly created or updated records that match the SOQL WHERE clause you provide and retrieves them as a CSV stream.

There is an expected delay when this trigger creates a job. The job processes after a query is completed in Salesforce. You can't test recipes using this trigger due to the processing delay.

This trigger uses [V2.0 of the Salesforce Bulk API](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/queries.html). Refer to the [Salesforce bulk operations](/en/connectors/salesforce/salesforce-bulk) guide for more information about bulk operations.

> **REPLICATE DATA TO A DATA WAREHOUSE**
> 
> You can use this trigger with the [Get object schema action](/en/connectors/salesforce/database-syncs#get-object-schema-action) to fetch schema information from a Salesforce object and replicate it to a data warehouse.

Refer to the [ETL/ELT](/en/features/etl-elt-guide#bulk-vs-batch) documentation for more information about bulk triggers and ELT/ETL processes.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the standard or custom object type to monitor. |
| Fields to retrieve | Select the fields to retrieve from the object. Workato retrieves all fields by default. Entering specific fields to retrieve improves recipe performance and mitigates [schema errors](/en/connectors/salesforce/troubleshoot-runtime#schema-errors). |
| SOQL WHERE clause | Enter a SOQL query to filter records by. For example: `StageName = 'Closed Lost' AND IsClosed = false`. Refer to the [SOQL](/en/connectors/salesforce/salesforce-soql) guide for more information. |
| Schedule settings | Configure the trigger schedule. Refer to the [scheduler trigger](/en/features/scheduler) to configure this section. |
| When exporting records to form the CSV, fetch them in batches of | Enter the maximum number of records to process in each batch. Defaults to `10000`. |
| Include deleted records? | Select whether to include deleted records in the results. Defaults to `No`. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output fields | Description |
| --- | --- |
| All records successfully processed? | Whether all records were processed successfully. |
| Number of records processed | The number of records processed. |
| Number of records failed | The number of records that failed to process. |
| Number of retried records | The number of records Workato retried processing. |
| CSV content | Datapill that contains the output of the trigger. Take note to utilize it primarily alongside streaming compatible actions like S3 upload file streaming action. |
| Object name | Name of the object being retrieved. |
| Object schema | The schema of the object being retrieved, based on the fields the user has selected. Each field has with it the associated name, label, original datatype, and mapped datatype. This allows for easy processing with database uploads and any additional transformations required. |
| Created or updated from | The time and date the record was created or updated. |
