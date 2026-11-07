---
url: 'https://docs.workato.com/en/connectors/shopify/list-draft-orders.md'
description: >-
  The List draft orders action in the Shopify connector lets you retrieve a list
  of draft orders from your store.
---

# Shopify - List draft orders action

This action retrieves a list of draft orders on Shopify. A draft order represents the intent of ordering by a customer. It can be transitioned into an order.

Refer to the [Shopify documentation](https://shopify.dev/api/admin-rest/2022-01/resources/draftorder) for more information on the draft order resource.

## Input

| Field | Description |
| --- | --- |
| Draft order ID | Optional. Filters the response to the specified draft orders. |
| Result limit | Optional. Supports any integer up to 250. If unspecified, defaults to 50. |
| Status | Optional. Allows filtering by draft order status. |
| Fetch results before last updated date | Optional. Only returns draft orders last updated before the specified date. |
| Fetch results after last updated date | Optional. Only returns draft orders last updated after the specified date. |
| Fetch results after ID | Optional. When provided, only orders with IDs following this ID are retrieved. |
| Return full data | Optional. If set to `yes/1`, the entire product image source is returned. Defaults to `false/0`. |

## Output

The output is a list of draft order IDs if **Return full data** is set to `false`. Else, we should return a list of datatree that contains information about the draft order object.

Learn more about the [draft order object](https://shopify.dev/api/admin-rest/2024-04/resources/draftorder#resource-object).

---
