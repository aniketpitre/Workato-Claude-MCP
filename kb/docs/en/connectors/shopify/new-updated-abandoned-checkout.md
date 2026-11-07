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
