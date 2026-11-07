---
url: 'https://docs.workato.com/en/connectors/shopify/cancel-fulfillment.md'
description: >-
  The Cancel a fulfillment action in the Shopify connector lets you cancel an
  existing fulfillment by its fulfillment ID.
---

# Shopify - Cancel a fulfillment action

This action cancels a fulfillment on Shopify.

## Input

| Field | Description |
| --- | --- |
| Fulfillment ID | The ID of the fulfillment to be canceled. |

## Output

The return payload includes the selected fields from the `Fulfillment` resource. Read the [Shopify documentation](https://shopify.dev/docs/api/admin-rest/2024-04/resources/fulfillment#resource-object) for more information.

---

---
url: >-
  https://docs.workato.com/en/connectors/shopify/connect-inventory-item-to-location.md
description: >-
  The Connect inventory item to location action in the Shopify connector lets
  you connect an inventory item to a location by creating an inventory level.
---

# Shopify - Connect inventory item to location action

This action connects an inventory item to a location in Shopify by creating an inventory level at the given location.

You must set up [Inventory tracking](https://help.shopify.com/en/manual/products/inventory/track_inventory) on Shopify to use this action.

## Input

| Field | Description |
| --- | --- |
| Inventory item ID | Shopify ID of the inventory item to connect to a location |
| Location ID | Shopify ID of the location that the inventory level should connect to. To find Shopify location IDs, use List locations action. |
| Relocate if necessary? | Relevant if inventory item has been or will be connected to a fulfillment service. If **yes**, inventory levels for previously connected locations will be relocated to this newly connected location and disconnected from other locations If **no** but a fulfillment service location is involved, the action fails and item is not connected. |

## Output

| Field | Description |
| --- | --- |
| Inventory item ID | The inventory item ID. |
| Location ID | The location ID. |
| Available | The quantity of inventory items available for sale. Returns null if the inventory item is not tracked. |
| Updated at | When this inventory level was last available. |
| Admin GraphQl API ID | A unique admin GraphQL API ID. |

---
