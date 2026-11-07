---
url: 'https://docs.workato.com/en/connectors/freshbooks/update-record-action.md'
description: >-
  The Update record action enables you to update the details of a specific
  record in FreshBooks.
---

# FreshBooks - Update record action

The **Update record** action enables you to update the details of a specific record in FreshBooks.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the object to update from the drop-down menu. Fields load dynamically based on the object you select. |
| Account ID | Select the FreshBooks account ID from the drop-down menu to update the record. |

For example, if you select **Item** object, the input schema is as follows:

| Input field | Description |
| --- | --- |
| ID | Provide the ID of the item to update. |
| Name | Provide the name of the item/service. |
| Description | Provide a detailed description of the item/service. |
| Quantity | Specify the quantity of the item. |
| Inventory | Specify the inventory quantity. |
| Unit cost | Provide the cost per unit of the item. |
| Tax 1 ID | Provide the ID of the default tax for the item. |
| Tax 2 ID | Provide the ID of the second default tax for the item. |
| Domain | Specify the domain associated with the item. |
| Product code | Provide the product code identifier. |
| SKU | Provide the Stock Keeping Unit identifier. |
| Tax rule code | Specify the tax rule code for the item. |
| Unit code | Provide the unit of measurement code. |
| Visibility state | Select the visibility state (Active or Deleted). |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps.

For example, if you select the **Item** object, the output schema is as follows:

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
