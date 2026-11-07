---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/new-updated-object-trigger-batch.md
description: >-
  The New or updated object batch trigger in the Microsoft Dynamics 365
  connector picks up newly created or updated records in batches each interval.
---

# Microsoft Dynamics 365 - New or updated object trigger (batch)

New or updated object trigger (batch) in Microsoft Dynamics 365 checks for newly created or updated objects every specified interval and retrieves a batch of new or updated records as a single trigger event.

## Input

| Field | Description |
| --- | --- |
| Object | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| From | Fetch new or updated object from the specified time. |
| Output fields | Select the fields of the selected objects you plan to use in your recipe. All fields are returned if left blank. |
| Filter condition | Condition to filter the records. Use OData $filter syntax. For example, `contains(name, 'sample')` and `revenue gt 1000000`. [Learn more about filters](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query-data-web-api#filter-results). |
| Batch size | Number of records in a single trigger event, default batch size is 100. Minimum size is 1, maximum size is 1000. |

## Output

| Field | Description |
| --- | --- |
| Range | The range of record IDs retrieved from the search. |
| Time | The time range of the records retrieved. |
| First ID | The ID of the first record in the batch. |
| Last ID | The ID of the last record in the batch. |
| Change details | This contains information about the changed object, including the fields specified in the output fields. |
