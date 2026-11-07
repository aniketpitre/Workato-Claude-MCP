---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/new-updated-object-trigger.md
description: >-
  The New or updated object trigger in the Microsoft Dynamics 365 connector
  picks up newly created or updated objects each polling interval.
---

# Microsoft Dynamics 365 - New or updated object trigger

The New or updated object trigger checks for newly created or updated objects when a specified interval lapses and processes each object as a single trigger event.

## Input

| Field | Description |
| --- | --- |
| Object | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| From | Fetch new or updated object from the specified time. |
| Output fields | Select the fields of the selected objects you plan to use in your recipe. All fields are returned if left blank. |
| Filter condition | Condition to filter the records. Use OData $filter syntax. For example, `contains(name, 'sample')` and `revenue gt 1000000`. [Learn more about filters](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query-data-web-api#filter-results). |

## Output

| Field | Description |
| --- | --- |
| Change details | This contains information about the changed object, including the fields specified in the output fields. |
