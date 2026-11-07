---
url: >-
  https://docs.workato.com/en/connectors/salesforce/actions/search-records-soql.md
description: >-
  This action retrieves a CSV stream of Salesforce records that match the SOQL
  query you provide.
---

# Salesforce - Search records in bulk using SOQL query action

This action retrieves a CSV stream of Salesforce records that match the SOQL query you provide. This action uses the Salesforce bulk API.

> **POLLING BEHAVIOR**
> 
> Recipes that contain an action with polling must be in a running state for asynchronous polling to function as expected.

Refer to the [SOQL](/en/connectors/salesforce/salesforce-soql) guide for more information about SOQL or the [Salesforce bulk operations](/en/connectors/salesforce/salesforce-bulk) guide for more information about bulk operations.

> **API VERSIONS**
> 
> This action exists in both API v1.0 and API v2.0 versions. Workato recommends using the bulk API v2.0 for optimal performance. This version reduces the impact on Salesforce API quotas by batching records more efficiently.

> **SELECT CLAUSE IN SOQL**
> 
> SOQL queries don't support the `SELECT *` operation often used in SQL queries. You must specify specific fields to retrieve in the SELECT clause.

## Input

| Input fields | Description |
| --- | --- |
| SOQL query | Provide a valid SOQL query excluding the LIMIT param. Enclose clauses with parentheses for logical operators. |
| Include deleted records? | Select whether to include deleted records in the results. Defaults to `No`. |
| Include header line? | Select whether to include the header line in the CSV results. |
| Retain failed job logs on Salesforce interface? | Select whether to persist failed job logs in Salesforce. Defaults to `No`. |
| Wait for Salesforce to process all CSV rows? (Advanced configuration) | Select whether to run the action synchronously. Select `Yes` to wait until Salesforce processes all rows in the CSV file before starting the next action. Select `No` to start the next action after the CSV file is uploaded to Salesforce. Bulk operations are asynchronous by default. |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

## Output

| Output fields | Description |
| --- | --- |
| Job ID | The Salesforce ID of the job. |
| All records successfully processed? | Specifies whether all CSV rows across Salesforce bulk jobs were processed successfully. |
| CSV results | The retrieved records as a CSV stream. You can write the CSV stream to a file using a file connector, such as [Box](/en/connectors/box) or [SFTP](/en/connectors/sftp). You can also parse it as a list of data in Workato using the [Parse CSV](/en/connectors/csv-by-workato/parse-csv-action) action in the CSV tools by Workato utility connector. |
| Number of records processed | The total number of CSV rows processed in Salesforce, excluding the header row. |
| Number of records failed | The total number of CSV rows that encountered issues and were not processed in Salesforce. |
| Number of retried records | The total number of CSV rows that retried processing in Salesforce. This field is relevant for the [Retry objects bulk job in Salesforce from CSV file](/en/connectors/salesforce/actions/retry-job-csv) action. |
| Processing time | The amount of time spent processing records. |
