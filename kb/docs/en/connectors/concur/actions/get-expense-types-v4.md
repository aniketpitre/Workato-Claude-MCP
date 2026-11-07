---
url: 'https://docs.workato.com/en/connectors/concur/actions/get-expense-types-v4.md'
description: >-
  The Get expense types action retrieves expense types for a specific user from
  SAP Concur using the v4 API.
---

# SAP Concur - Get expense types action

The **Get expense types** action retrieves all expense types applicable to the specified user based on their assigned policies from SAP Concur using the v4 API.

This action replaces the deprecated [Get all expense types](/en/connectors/concur/actions/get-all-expense-types-batch) action.

> **PREREQUISITES**
> 
> Your SAP Concur OAuth 2.0 connection must include the following scopes to use this action:
> 
> - `expense.config.policies.restricted.read`
> - `expense.config.expensetypes.restricted.read`

## Input

| Input field | Description |
| --- | --- |
| User ID | The unique identifier of the SAP Concur user. Use the [Get user](/en/connectors/concur/actions/get-user) action to retrieve the user ID. |

## Output

| Output field | Description |
| --- | --- |
| Expense types | List of expense types available to the specified user. |
| Expense type (Expense types) | The code for the expense type. |
| Expense type name (Expense types) | The name of the expense type. |
| Spend category code (Expense types) | The code for the spend category associated with the expense type. |
| Spend category name (Expense types) | The name of the spend category associated with the expense type. |
| Is category (Expense types) | Indicates whether the expense type is a category. |
| Parent expense type (Expense types) | The code of the parent expense type, if applicable. |
| Parent name (Expense types) | The name of the parent expense type, if applicable. |
| List size | The total number of expense types returned. |
| List index | The index of the current item in the list. |

---

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

---
