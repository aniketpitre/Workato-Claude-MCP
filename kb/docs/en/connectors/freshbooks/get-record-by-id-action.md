---
url: 'https://docs.workato.com/en/connectors/freshbooks/get-record-by-id-action.md'
description: >-
  The Get record by ID action enables you to retrieve details of a specific
  record in FreshBooks.
---

# FreshBooks - Get record by ID action

The **Get record by ID** action enables you to retrieve details about a specific record in FreshBooks.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the object to get the record of. Fields load dynamically based on the object you select. |
| Account ID | Select the FreshBooks account ID to retrieve the record. |
| ID | Provide the ID of the object to be retrieved. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. For example, if you select the **Item** object, the output schema is as follows:

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the item. |
| Item ID | Duplicate of the ID field. |
| Account UUID | Account UUID identifier. |
| Accounting System ID | Accounting system identifier. |
| Name | Name of the item/service. |
| Description | Detailed description of the item/service. |
| Quantity | Quantity of the item. |
| Inventory | Inventory quantity. |
| Unit cost | Cost per unit with amount and currency code. |
| Tax 1 ID | ID of the default tax for the item. |
| Tax 2 ID | ID of the second default tax for the item. |
| Domain | Domain associated with the item. |
| Product code | Product code identifier. |
| SKU | Stock Keeping Unit identifier. |
| Tax rule code | Tax rule code for the item. |
| Unit code | Unit of measurement code. |
| Updated | Last update timestamp. |
| Visibility state | Visibility state of the item (0 for active, 1 for deleted). |

---
