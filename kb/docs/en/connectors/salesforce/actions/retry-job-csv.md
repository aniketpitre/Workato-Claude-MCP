---
url: 'https://docs.workato.com/en/connectors/salesforce/actions/retry-job-csv.md'
description: This action retries failed Salesforce jobs in bulk from a CSV file.
---

# Salesforce - Retry bulk job for failed records from CSV file action

This action retries failed Salesforce jobs in bulk from a CSV file.

> **POLLING BEHAVIOR**
> 
> Recipes that contain an action with polling must be in a running state for asynchronous polling to function as expected.

This action is synchronous, meaning Workato waits for Salesforce to complete the bulk job processing before moving to the next recipe action.

Use this action after another Salesforce bulk action, such as [Upsert records in bulk from CSV file](/en/connectors/salesforce/actions/upsert-records-in-bulk-from-csv), to resubmit failed records as a new bulk job. Refer to the [Salesforce bulk operations](/en/connectors/salesforce/salesforce-bulk) guide for more information about bulk operations.

![Configured Salesforce bulk retry action](/assets/configured-bulk-retry-action.uesG83CP.png)_Configured Salesforce bulk retry action_

## Input

| Input fields | Description |
| --- | --- |
| CSV content with failed records | Enter a CSV content with failed records datapill from a previous Salesforce bulk operation action. This informs the action about the previous step's configuration. For example: what the CSV file looks like, what Salesforce object to write to, and how to map the CSV data into Salesforce fields. |

## Output

| Output fields | Description |
| --- | --- |
| All records successfully processed? | Specifies whether all CSV rows across Salesforce bulk jobs were processed successfully. |
| Number of records succeeded | The total number of CSV rows that were successfully processed in Salesforce. |
| Number of records failed | The total number of CSV rows that encountered issues and were not processed in Salesforce. |
| Number of retried records | The total number of CSV rows that retried processing in Salesforce. |
| Number of records processed | The total number of CSV rows processed in Salesforce, excluding the header row. |
| CSV contents with failed records | CSV file content containing CSV rows that encountered issues and were not processed. Two additional columns are added to this CSV file: `sf__Error` and `sf__Id`. Refer to the [Salesforce documentation](https://developer.salesforce.com/docs/atlas.en-us.api_bulk_v2.meta/api_bulk_v2/get_job_failed_results.htm) for more information. |
| CSV content with success records | CSV file content containing CSV rows that were successfully processed in Salesforce. Two additional columns are added to this CSV file: `sf__Created` and `sf__Id`. Refer to the [Salesforce documentation](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/get_job_successful_results.htm) for more information. |
| Failed records report header | Header information of failed record reports. |
| Success records report header | Header information of successful record reports. |
| Salesforce bulk jobs | An object containing information about each Salesforce bulk job. Refer to the [Salesforce bulk jobs](#salesforce-bulk-jobs) section for more information. |

### Salesforce bulk jobs

Workato splits large CSV files into chunks and processes them as separate Salesforce bulk jobs to comply with Salesforce API size limits. Bulk operations output a `Salesforce bulk jobs` datatree that contains information about each chunk processed.

![Salesforce bulk operation output datatree - list of bulk jobs](/assets/bulk-operation-datatree-array-of-jobs.CZCluW4m.png)_Salesforce bulk operation output datatree - list of bulk jobs_

Workato includes the aggregated results across all bulk jobs at the top of the output, outside of the `Salesforce bulk jobs` datatree.

![Salesforce bulk operation output datatree - aggregated results across bulk jobs](/assets/bulk-operation-datatree-aggregate-numbers.Cn8qzyPE.png)_Salesforce bulk operation output datatree - aggregated results across bulk jobs_

---
