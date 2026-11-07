---
url: 'https://docs.workato.com/en/connectors/shopify/update-sku.md'
description: >-
  The Update SKU action in the Shopify connector lets you update the stock
  keeping unit (SKU) associated with a product variant.
---

# Shopify - Update SKU action

This action updates the SKU (stock keeping unit) associated with a product variant.

## Input

| Field | Description |
| --- | --- |
| Inventory item ID | The product variant. |
| Sku | The stock keeping unit for this product variant. |
| Tracked | Select from the picklist or input your own value. If true, then inventory quantity changes are tracked. |

## Output

| Field | Description |
| --- | --- |
| ID | The unique ID of the product variant. |
| Sku | The stock keeping unit. |
| Tracked | Whether this item is being tracked. |
| Created at | The data and time when this SKU was created. |
| Updated at | The date and time when this SKU was last updated. |
| Admin GraphQL API ID | The Admin GraphQL API ID. |

---
