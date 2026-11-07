---
url: >-
  https://docs.workato.com/en/connectors/salesforce/triggers/export-new-records.md
description: >-
  This trigger monitors Salesforce for new records that match the SOQL WHERE
  clause you provide and retrieves them as a CSV stream.
---

# Salesforce - Export new records trigger

This trigger monitors Salesforce for new records that match the SOQL WHERE clause you provide and retrieves them as a CSV stream.

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
| When exporting records to form the CSV, fetch them in batches of | Enter the maximum number of records to process in each batch. Defaults to `10000`. |
| Include deleted records? | Select whether to include deleted records in the results. Defaults to `No`. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output fields | Description |
| --- | --- |
| All records successfully processed | Indicates whether all CSV rows across Salesforce bulk jobs processed successfully. |
| Number of records processed | The total number of CSV rows processed in Salesforce, excluding the header row. |
| Number of records failed | The total number of CSV rows that encountered issues and were not processed in Salesforce. |
| Number of retried records | The total number of CSV rows that retried processing in Salesforce. This field is relevant for the [Retry objects bulk job in Salesforce from CSV file](/en/connectors/salesforce/actions/retry-job-csv) action. |
| CSV content | The contents of the retrieved record as a CSV stream. You can write the CSV stream to a file using a file connector, such as Box or SFTP. You can also parse it to use as a list in Workato using the [Parse CSV](/en/connectors/csv-by-workato/parse-csv-action) action in the CSV tools by Workato utility connector. |
| Object name | The name of the retrieved object. |
| Object schema | An object containing information about the object's fields, such as `Field name`, `Custom field?`, and `Length`. |
| Created from | The date and time the object was created. |
