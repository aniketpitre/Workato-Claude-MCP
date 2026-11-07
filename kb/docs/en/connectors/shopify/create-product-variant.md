---
url: 'https://docs.workato.com/en/connectors/shopify/create-product-variant.md'
description: >-
  The Create product variant action in the Shopify connector lets you create a
  new variant for an existing product.
---

# Shopify - Create product variant action

This action creates a product variant in Shopify.

> **PRODUCT VARIANT RESOURCE DEPRECATION NOTICE**
> 
> Listing, creating, updating, and deleting product variants is deprecated as of Shopify REST API version `2024-04`. For more information, refer to the [guide to the new product model](https://shopify.dev/docs/api/admin/migrate/new-product-model).

## Input

| Field | Description |
| --- | --- |
| Product ID | The unique numeric identifier for the product. |
| Option 1 | The custom properties that a shop owner uses to define product variants. You can define up to three options for a product variant. |
| Option 2 | The custom properties that a shop owner uses to define product variants. You can define up to three options for a product variant. |
| Option 3 | The custom properties that a shop owner uses to define product variants. You can define up to three options for a product variant. |
| Image ID | The unique numeric identifier for a product's image. The image must be associated to the same product as the variant. |
| Price | The price of the product variant. |
| Barcode | The barcode, UPC, or ISBN number for the product. |
| Compare at price | The original price of the item before an adjustment or a sale. |
| Taxable | Select from the picklist or input your own value. Select yes to charge tax when the product variant is sold. |
| Requires shipping | Select from the picklist or input your own value. |
| Weight | The weight of the product variant. |
| Weight unit | Unit can be either 'g', 'kg', 'oz', or 'lb' |
| Inventory management | Select whether to track number of items in stock for this product variant |

## Output

| Field | Description |
| --- | --- |
| ID | The unique numeric identifier for the product variant. |
| Product ID | The unique numeric identifier for the product. |
| Barcode | The barcode, UPC, or ISBN number for the product. |
| Compare at price | The original price of the item before an adjustment or a sale. |
| Fulfillment service | The fulfillment service associated with the product variant. Valid values: manual or the handle of a fulfillment service. |
| Grams | The weight of the product variant in grams. |
| Inventory management | The fulfillment service that tracks the number of items in stock for the product variant. |
| Inventory policy | Whether customers are allowed to place an order for the product variant when it's out of stock. |
| Position | The order of the product variant in the list of product variants. The first position in the list is 1. |
| Price | The price of the product variant. |
| Requires shipping | Note: Shopify API states that this property is deprecated. Use the `requires_shipping` property on the InventoryItem resource instead. |
| Taxable | Whether a tax is charged when the product variant is sold. |
| Title | The title of the product variant. The title field is a concatenation of the option1, option2, and option3 fields. You can only update title indirectly using the option fields. |
| Old inventory quantity (deprecated) | Note: Shopify API states that this property is deprecated. Use the InventoryLevel resource instead. |
| Image ID | The unique numeric identifier for a product's image. The image must be associated to the same product as the variant. |
| Weight | The weight of the product variant. |
| Weight unit | Unit can be either 'g', 'kg', 'oz', or 'lb' |
| Option 1 | Custom variants of the product defined in options. |
| Option 2 | Custom variants of the product defined in options. |
| Option 3 | Custom variants of the product defined in options. |
| Sku | A unique identifier for the product variant in the shop. Required to connect to a FulfillmentService. |
| Inventory quantity (deprecated) | An aggregate of inventory across all locations. |
| Inventory item ID | The unique identifier for the inventory item, which is used in the Inventory API to query for inventory information. |
| Created at | The date and time when the product variant was created. |
| Updated at | The date and time when the product variant was last updated. |

---
