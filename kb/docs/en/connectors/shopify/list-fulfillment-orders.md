---
url: 'https://docs.workato.com/en/connectors/shopify/list-fulfillment-orders.md'
description: >-
  The List fulfillment orders for an order action in the Shopify connector lets
  you retrieve all fulfillment orders for a specific order.
---

# Shopify - List fulfillment orders for an order action

This action retrieves a list of fulfillment orders for a specific order in Shopify.

## Input

| Field | Description |
| --- | --- |
| Order ID | The ID of the order that is associated with the fulfillment orders. |
| Include financial summaries? | Specify whether to include the financial summary data for each line item, if available. |
| Include order reference fields? | Indicate whether the order reference fields should be returned in the result. |

## Output

The output of the action above is a list of the `FulfillmentOrder` resource. Read the [Shopify documentation](https://shopify.dev/docs/api/admin-rest/2024-04/resources/fulfillmentorder#resource-object) for more information.

---
