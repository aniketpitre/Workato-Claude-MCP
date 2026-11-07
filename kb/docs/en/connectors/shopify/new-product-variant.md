---
url: 'https://docs.workato.com/en/connectors/shopify/new-product-variant.md'
description: >-
  The New product variant trigger in the Shopify connector picks up new product
  variants on every poll interval, one job per variant.
---

# Shopify - New product variant trigger

This trigger checks for new product variants in Shopify on every poll interval.

Each new product variant is processed as a separate job.

> **PRODUCT VARIANT RESOURCE DEPRECATION NOTICE**
> 
> Listing, creating, updating, and deleting product variants is deprecated as of Shopify REST API version `2024-04`. For more information, refer to the [guide to the new product model](https://shopify.dev/docs/api/admin/migrate/new-product-model).

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Set the frequency at which Workato checks for new product variants. |
| When first started, this recipe should pick up events from | Get new products since the given date/time. Leave empty to get all orders created from time when recipe is first started. After a recipe has been run or tested, this value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Product ID | The product ID. |

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

---
url: >-
  https://docs.workato.com/en/connectors/shopify/new-updated-abandoned-checkout.md
description: >-
  The New/updated abandoned checkout trigger in the Shopify connector picks up
  new or updated abandoned checkouts on every poll interval.
---

# Shopify - New/updated abandoned checkout trigger

This trigger checks for new or updated abandoned checkouts in Shopify on every poll interval.

Each checkout is processed as a separate job.

> **CHECKOUT RESOURCE DEPRECATION NOTICE**
> 
> As of Shopify API version `2024-04`, the Checkout resource is deprecated and will be sunset on April 1, 2025. Refer to the [Shopify developer changelog](https://shopify.dev/changelog/deprecation-of-checkout-apis) for more information.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Set the frequency at which Workato checks for new or updated abandoned checkouts. |
| When first started, this recipe should pick up events from | Get abandoned checkouts since the given date/time. Leave empty to get all orders created from time when recipe is first started. After a recipe has been run or tested, this value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Checkout status | Choose from `Open`, `Archived`. Defaults to `Open` |

## Output

| Field | Description |
| --- | --- |
| Abandoned checkout URL | The recovery URL that's sent to a customer so they can recover their checkout. |
| Total duties | The total duties of the checkout in presentment currency. |
| Checkout ID | The ID for the checkout. |
| Billing address | The mailing address associated with the payment method. |
| Note | The text of an optional note that a shop owner can attach to the order. |
| Note attributes | Additional information on order. |
| Buyer accepts marketing | Whether the customer consented to receive email updates from the shop. |
| Cancel reason | The reason for the abandoned checkout. |
| Cart token | The ID for the cart that's attached to the checkout. |
| Closed at | The date and time when the checkout was closed. If the checkout was not closed, then this value is null. |
| Created at | The date and time when the checkout was created. |
| Completed at | The date and time when the checkout was completed. For abandoned checkouts, this value is null. |
| Currency | The three-letter code of the shop's default currency at the time of checkout. |
| Line items | A list of line items, each containing information about an item in the checkout. |
| Customer | Information about the customer. |
| Discount codes | Discount codes applied to the checkout. Returns an empty array when no codes are applied. |
| Gateway | The payment gateway used by the checkout. For abandoned checkouts, this value is null. |
| Source identifier | The ID for the source. |
| Email | The customer's email address. |
| Landing site | The URL for the page where the customer entered the shop. |
| ID | The ID for the checkout. |
| Referring site | For example, `http://www.example.com` |
| Shipping lines | Information about the chosen shipping method. |
| Source URL | The URL of the source. |
| Source name | Where the checkout originated. Valid values: web, pos, iphone, android |
| Total price | The sum of line item prices, all discounts, shipping costs, and taxes for the checkout in presentment currency. |
| Subtotal price | The price of the checkout in presentment currency before shipping and taxes. |
| Price | The price of the item in presentment currency. |
| Total weight | The sum of all the weights in grams of the line items in the checkout. |
| Token | A unique ID for a checkout. |
| Total discounts | The total amount of discounts to be applied in presentment currency. |
| Total line items price | The sum of the prices of all line items in the checkout in presentment currency. |
| Total tax | The sum of all the taxes applied to the checkout in presentment currency. |
| Taxes included | Whether taxes are included in the price. |
| Tax lines | A list of tax line objects, each of which details a tax applied to the item. Each tax line includes: - Title - Price - Price set - Rate |
| Shipping address | The mailing address where the order will be shipped to. |
| Source | The channel where the checkout originated. |
| Date updated | The date and time when this checkout was last updated. |

---
