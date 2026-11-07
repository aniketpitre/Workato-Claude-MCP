---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/new-object-trigger.md
description: >-
  The New object trigger in the Microsoft Dynamics 365 connector picks up newly
  created objects each polling interval as single trigger events.
---

# Microsoft Dynamics 365 - New object trigger

The New Object trigger in Microsoft Dynamics 365 checks for newly created objects every specified interval and processes each new object as a single trigger event.

## Input

| Field | Description |
| --- | --- |
| Object | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| From | Fetch new object from the specified time. |
| Output fields | Select the fields of the selected objects you plan to use in your recipe. All fields are returned if left blank. |
| Filter condition | Condition to filter the records. Use OData $filter syntax. For example, `contains(name, 'sample')` and `revenue gt 1000000`. [Learn more about filters](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query-data-web-api#filter-results). |

## Output

| Field | Description |
| --- | --- |
| Change details | This contains information about the new object, including the fields specified in the output fields. |
