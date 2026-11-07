---
url: 'https://docs.workato.com/en/connectors/netsuite/execute-saved-search.md'
description: >-
  The Execute saved search for record action in the NetSuite SOAP connector lets
  you retrieve records from a saved search, with optional filters.
---

# NetSuite SOAP - Execute saved search for record action

The **Execute saved search for record** action retrieves records from NetSuite based on a saved search, with optional filters to refine the results.

![Execute saved search for record action](/assets/execute-saved-search.EGj2A8vu.png)_Execute saved search for record action_

## Input

| Input field | Description |
| --- | --- |
| Record type | Select the type of NetSuite record to retrieve saved searches for, such as `Customer`, `Vendor`, or `Transaction`. |
| Saved search | Select a saved search from the list or enter the **Saved search ID** if it’s not listed. Ensure the saved search is set up correctly in NetSuite. |
| Record list | Select the specific records to retrieve in the output. You must select **Internal IDs** of records to retrieve their data. |
| Fields | Select the fields from the selected records to include in the output. Only the fields you select appear in the output data. The **Internal ID** of all selected records must be included in the **Record list**. |
| Results list page size | Specify the number of records to retrieve per page. The default is 25 records per page. The minimum value is 5, and the maximum is 200. If the number of records exceeds the page size, use the **Search ID** and **Page number** fields to retrieve the remaining records. |
| Search ID | Provide the **Search ID** from a previous search to retrieve subsequent pages of results. When **Search ID** is specified, other search criteria are ignored. |
| Page number | Enter the page number to retrieve if the search returns more than one page. Use this field with **Search ID** to paginate through results. |
| Search settings | Configure additional operators to refine your search. For example, you can filter string fields with a `Contains` operator or integer fields with `Equal to`. Each operator applies to all fields of that type. |

## Output

| Output field | Description |
| --- | --- |
| Search ID | The unique identifier for the search results. |
| Page number | The current page number of the results being retrieved. |
| Total pages | The total number of pages in the search result. |

---
