---
url: >-
  https://docs.workato.com/en/connectors/pipedrive-custom/search-records-by-query-action.md
description: >-
  The Search records by query action searches Pipedrive and returns a list of
  records that match the criteria you specify.
---

# Pipedrive - Search records by query action

The **Search records by query** action searches Pipedrive and returns a list of records that match the criteria you specify.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the type of object to retrieve from Pipedrive. |
| Term | Enter a search term to query by. |
| Fields to search | Select in which fields to compare the search **Term** and Pipedrive records. |
| Exact match | Select whether to search for exact or partial matches. |
| Limit | Enter the maximum number of records to return. |
| Cursor | Provide the `next_cursor` value to retrieve the next page of results. Defaults to the first page if left blank. |

## Output

The **Search records by query** action's output fields vary based on your selected **Object** type. The following output table uses an **Organization** object as an example:

| Output field | Description |
| --- | --- |
| Data | Contains information about the current state of the organization. |
| Items | Contains records from Pipedrive that match the search criteria. |
| Result score | Indicates whether the search was successful. |
| Item | The organization returned by the search. |
| ID | A unique identifier for the organization. |
| Name | Name of the organization |
| Type | Type of organization |
| Address | The address of the organization. |
| Visible to | The visibility rules set for this organization. |
| Owner | Contains information about the owner of the organization. |
| Custom fields | Contains additional information about the returned records. |
| Notes | Notes from the returned organization. |
| Next cursor | Cursor to use for pagination to fetch the next page. |

> **VARIABLE OUTPUT**
> 
> The **Search records by query** action's output fields vary based on your selected **Object** type.
