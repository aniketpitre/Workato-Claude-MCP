---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/search-objects-action.md
description: >-
  The Search objects action in the Microsoft Dynamics 365 connector lets you
  retrieve a list of objects that match your specified search criteria.
---

# Microsoft Dynamics 365 - Search objects action (batch)

This action retrieves a list of objects in Microsoft Dynamics 365 that match the specified search criteria.

## Input

| Field | Description |
| --- | --- |
| Object name | Select a standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| Result list size | Number of records retrieved. Minimum is 1, maximum is 5000. Defaults to 200. |
| Output fields | Select the fields of the selected objects you plan to use in your recipe. |
| Filter condition | Condition to filter the records. Use OData $filter syntax. For example, `contains(name, 'sample')` and `revenue gt 1000000`. [Learn more about filters](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query-data-web-api#filter-results). |
| Order by | Specify the order in which items are returned. |
| Expand | Expand navigation properties in the related entity set. |
| Next page URL | Next page URL, returned by a previous call, to request the next page of results. |

## Output

The output datatree contains a list of objects that match the search criteria. Each object contains information, such as ID and other attributes.

| Field | Description |
| --- | --- |
| Records | A list of records that match the search criteria. |
| Next page URL | URL to fetch the next page of results. |
