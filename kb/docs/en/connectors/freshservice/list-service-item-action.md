---
url: >-
  https://docs.workato.com/en/connectors/freshservice/list-service-item-action.md
description: Returns a list of service items based on specified filters.
---

# Freshservice - List service items action

The **List service items** action returns a list of service items based on specified filters.

## Input

| Input field | Description |
| --- | --- |
| Category ID | Provide the category ID of service item. |
| Result per page | Provide a value between 1 to 100. |
| Page number | Provide the number of pages. |

## Output

| Output field | Description |
| --- | --- |
| Service item ID | Unique ID of the item. |
| Workspace ID | ID of the workspace to which the service item belongs (applicable for Employee Support Mode). |
| Created at | The timestamp when the item was created. |
| Updated at | The timestamp when the item was last updated. |
| Name | Name of the service item. |
| Delivery time | Estimated delivery time of the item (in hours). |
| Display ID | Unique ID of the service item specific to the account. |
| Category ID | Unique ID of the category to which the service item belongs. |
| Product ID | The ID of the product mapped to the item (returns null if no product is mapped). |
| Quantity | The number of items requested. |
| Deleted | True indicates the item was deleted successfully. |
| Group visibility | 1 denotes visibility to all requesters, 2 for restricted visibility. |
| Item type | 1 indicates a normal item, 2 indicates a loaner item. |
| CI type ID | Unique ID of the asset type associated with the product. |
| Cost visibility | Set to true if the cost should be visible to the requester. |
| Delivery time visibility | Set to true if the delivery time of the item should be visible to the requester. |
| Configs | Configuration template for the service request subject. |
| Botified | Set to true if the item is "bot ready." |
| Visibility | 1 denotes draft, 2 denotes published. |
| Allow attachments | Set to true if the requester is allowed to attach files. |
| Allow quantity | Set to true to allow the requester to request more than one quantity. |
| Is bundle | Indicating whether the item contains child items. |
| Create child | Indicating whether child items will be created as separate service requests. |
