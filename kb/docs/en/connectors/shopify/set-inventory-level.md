---
url: 'https://docs.workato.com/en/connectors/shopify/set-inventory-level.md'
description: >-
  The Set inventory level action in the Shopify connector lets you set the
  available quantity of an inventory item at a given location.
---

# Shopify - Set inventory level action

This action will set the inventory level for an inventory item at the given location. The inventory item will be connected to the location if they are not previously connected.

You must set up [Inventory tracking](https://help.shopify.com/en/manual/products/inventory/track_inventory) on Shopify to use this action.

## Input

| Field | Description |
| --- | --- |
| Inventory item ID | Shopify ID of the inventory item to set inventory level for. |
| Location ID | Shopify ID of the location to set inventory level. To find the ID of the location, use List locations action. |
| Quantity available | Sets the available inventory quantity. |
| Disconnect if necessary? | Select from the picklist or input your own value. Relevant if inventory item has been or will be connected to a fulfillment service. If yes, inventory levels for any previously connected locations are set to 0 and disconnected. If no but a fulfillment service location is involved, the action fails and inventory level is not set. |

## Output

| Field | Description |
| --- | --- |
| Inventory item ID | The inventory item ID. |
| Location ID | The location ID. |
| Available | The quantity of inventory items available for sale. Returns null if the inventory item is not tracked. |
| Updated at | When this inventory level was last available. |
| Admin GraphQL API ID | A unique admin Graphql API ID. |

---
