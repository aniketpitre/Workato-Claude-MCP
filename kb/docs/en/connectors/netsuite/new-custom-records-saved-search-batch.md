---
url: >-
  https://docs.workato.com/en/connectors/netsuite/new-custom-records-saved-search-batch.md
description: >-
  The New custom records in a saved search trigger (batch) retrieves batches of
  new custom records from a saved search in NetSuite.
---

# NetSuite SOAP - New custom records in a saved search trigger (batch)

The **New custom records in a saved search** trigger (batch) retrieves batches of new custom records from a saved search in NetSuite. Ensure the saved search results include the following fields:

- The **Internal ID** and **Date Created** fields of the base object.
- The **Internal ID** field for all joined objects.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | Specify the date and time from which this recipe retrieves trigger events. You can't change this value after you test or run this recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Custom Record | Select the NetSuite custom record to retrieve. |
| Saved search | Select an option from the drop-down menu, or enter the saved search ID from the URL of the saved search page. |
| Batch size | Enter the number of NetSuite records to retrieve at a time. The minimum value is `1`, and the maximum is `100`. |
| Output field configuration | Select the NetSuite fields to include in the trigger output. |
| Object list | Select the records to include in the trigger output. |
| Fields | Select the fields to include in the trigger output. You must select the **Internal ID** checkbox for each record in the **Record list** field. |
| Custom record custom fields | Select custom fields to include in the trigger output. |

## Output

| Output field | Description |
| --- | --- |
| Range | The range of records retrieved in the current batch. |
| First batch ID | The unique identifier of the first batch retrieved during the trigger's execution. |
| Last batch ID | The unique identifier of the last batch retrieved during the trigger's execution. |
| Records | A list datapill containing the records that match the saved search criteria. |
| Basic (records) | An object containing fields specific to your selected **Custom Record**. The fields included are determined by your selections in the **Object list** and **Fields** input fields. |
| Total number of records | The total count of records retrieved from the saved search across all batches. |
| First batch | Indicates whether this batch is the first batch of records retrieved. |
| Last batch | Indicates whether this batch is the last batch of records retrieved. |
| Starting offset | The position of the first record in the current batch within the overall dataset. |
| Ending offset | The position of the last record in the current batch within the overall dataset. |
