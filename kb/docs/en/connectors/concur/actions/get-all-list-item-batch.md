---
url: >-
  https://docs.workato.com/en/connectors/concur/actions/get-all-list-item-batch.md
description: >-
  The Get all list item batch action retrieves the first level list items from a
  specified list in SAP Concur.
---

# SAP Concur - Get all list item action (batch)

The **Get all list item** batch action retrieves the first level list items from a specified list in SAP Concur.

## Input

| Input field | Description |
| --- | --- |
| List ID | Enter the unique identifier of the list containing the list items to retrieve. |
| Has children | Select whether to display only items with children. |
| Is deleted | Select whether to display deleted items. |
| Page number | Specify the page number to retrieve. Defaults to 1. |
| Short code or value | Enter a value to filter list items by their value or short code. |
| Sort by | Specify the field to sort results by. Options include: value, shortCode |

## Output

| Output field | Description |
| --- | --- |
| Links | Hypermedia links related to the list items. |
| Rel (Links) | The relationship of the link to the current resource. |
| Href (Links) | The URL of the linked resource. |
| Content | List of list items retrieved from the specified list. |
| ID (Content) | The unique identifier of the list item. |
| Code (Content) | The long code value of the list item. |
| Short code (Content) | The short code value of the list item. |
| Value (Content) | The name or text value of the list item. |
| Parent ID (Content) | The unique identifier of the parent list item if this is a child item. |
| Level (Content) | The level of the list item within the hierarchy. |
| Is deleted (Content) | Indicates whether the list item has been deleted. |
| List ID (Content) | The unique identifier of the list containing this item. |
| Lists | Information about the lists. |
| ID (Lists) | The unique identifier of the list. |
| Has children (Lists) | Indicates whether the list item has child items. |
| Page | Pagination information for the results. |
| Size (Page) | The number of list items returned per page. |
| Total elements (Page) | The total number of list items available across all pages. |
| Total pages (Page) | The total number of pages available. |
| Number (Page) | The current page number. |
