---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/scheduled-object-search-trigger.md
description: >-
  The Scheduled object search trigger in the Microsoft Dynamics 365 connector
  searches for objects on a set schedule and returns matching records.
---

# Microsoft Dynamics 365 - Scheduled object search trigger

The Scheduled object search trigger allows you to search for objects on a specified schedule and return results as a list of records.

## Input

| Field | Description |
| --- | --- |
| Object | Select a standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| Output fields | Select the fields of the selected objects you plan to use in your recipe. All fields are returned if left blank. |
| Filter condition | Condition to filter the records. Use OData $filter syntax. For example, `contains(name, 'sample')` and `revenue gt 1000000`. [Learn more about filters](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query-data-web-api#filter-results). |
| Batch size | Number of records in a single trigger event, default batch size is 100. Minimum size is 1, maximum size is 1000. |
| Schedule | Define the schedule for the trigger. |
| Timezone | Define the timezone of the schedule. |

## Output

| Field | Description |
| --- | --- |
| Range | The range of record IDs retrieved from the search. |
| Time | The time range of the records retrieved. |
| First ID | The ID of the first record in the batch. |
| Last ID | The ID of the last record in the batch. |
| First batch | Whether this is the first batch of records. |
| Last batch | Whether this is the last batch of records. |
| Starting offset | The offset number for the first record of this batch. |
| Ending offset | The offset number for the last record of this batch. |
| Records | This contains a list of records. Each record contains information about the object, including the fields specified in the output fields. |
