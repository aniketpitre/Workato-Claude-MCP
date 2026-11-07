---
url: 'https://docs.workato.com/en/connectors/shopify/adjust-inventory-level.md'
description: >-
  The Adjust inventory level action in the Shopify connector lets you adjust the
  inventory level of an inventory item at a given location.
---

# Shopify - Adjust inventory level action

This action will adjust inventory level of an inventory item at the given location.

You must set up [Inventory tracking](https://help.shopify.com/en/manual/products/inventory/track_inventory) on Shopify to use this action.

## Input

| Field | Description |
| --- | --- |
| Inventory item ID | Shopify ID of the target inventory item. |
| Location ID | Shopify ID of the location to adjust inventory level. To find the ID of the location, use the [List locations action](/en/connectors/shopify/list-locations). |
| Quantity to adjust | How much to adjust. This field accepts positive and negative numbers. For example, 2 increases the current available quantity by 2, -3 decreases the current available quantity by 3. |

## Output

| Field | Description |
| --- | --- |
| Inventory item ID | The inventory item ID. |
| Location ID | The location ID. |
| Available | The quantity of inventory items available for sale. Returns null if the inventory item is not tracked. |
| Updated at | When this inventory level was last available. |
| Admin GraphQL API ID | A unique admin GraphQL API ID. |

---
