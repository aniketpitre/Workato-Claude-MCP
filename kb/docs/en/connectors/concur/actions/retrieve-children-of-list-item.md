---
url: >-
  https://docs.workato.com/en/connectors/concur/actions/retrieve-children-of-list-item.md
description: >-
  The Retrieve children of list item action retrieves child items of a specific
  list item in SAP Concur.
---

# SAP Concur - Retrieve children of list item action

The **Retrieve children of list item** action retrieves child items of a specific list item in SAP Concur.

## Input

| Input field | Description |
| --- | --- |
| List / List ID | Select the list to retrieve child items from, or enter the unique identifier of the list. |
| Item / Item ID | Select the parent list item, or enter the unique identifier of the parent list item. Only the first 100 items are displayed in the selection list. |
| Has children? | Select whether to display only items with children. By default, returns items with their children attributes if present. |
| Is deleted? | Select whether to display deleted items. By default, deleted items are not returned. |
| Short code or value | Enter a value to filter list items by their value or short code. |
| Page number | Specify the page number to retrieve. Defaults to 1. |
| Sort by | Select the field to sort results by. Options include: Value, Short code |

## Output

| Output field | Description |
| --- | --- |
| Links | Hypermedia links related to the list items. |
| Rel (Links) | The relationship of the link to the current resource. |
| Href (Links) | The URL of the linked resource. |
| Content | List of child list items retrieved from the specified parent list item. |
| ID (Content) | The unique identifier of the list item. |
| Code (Content) | The long code value of the list item. |
| Short code (Content) | The short code value of the list item. |
| Value (Content) | The name or text value of the list item. |
| Parent ID (Content) | The unique identifier of the parent list item. |
| Level (Content) | The level of the list item within the hierarchy. |
| Is deleted (Content) | Indicates whether the list item has been deleted from all lists. |
| List ID (Content) | The unique identifier of the list containing this item. |
| Lists (Content) | Information about the lists containing this item. |
| ID (Lists) | The unique identifier of the list that contains the list item. |
| Has children (Lists) | Indicates whether the list item has children in this particular list. |
| Page | Pagination information for the results. |
| Size (Page) | The number of list items returned per page. |
| Total elements (Page) | The total number of list items available across all pages. |
| Total pages (Page) | The total number of pages available. |
| Number (Page) | The current page number. |
