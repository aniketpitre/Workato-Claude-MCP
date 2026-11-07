---
url: 'https://docs.workato.com/en/connectors/shopify/list-fulfillments.md'
description: >-
  The List fulfillments by fulfillment order action in the Shopify connector
  returns all fulfillments associated with a fulfillment order.
---

# Shopify - List fulfillments by fulfillment order action

This action returns all the fulfillments associated with a fulfillment order in your Shopify instance. Check out this [Shopify Documentation](https://shopify.dev/docs/api/admin-rest/2022-04/resources/fulfillment) to learn more about the relationship between Order, Fulfillment Order, and Fulfillments.

## Input

| Field | Description |
| --- | --- |
| Fulfillment order ID | The ID of the fulfillment order that is associated with the fulfillments. |

## Output

The output of the action above is a list of the `Fulfillment` resource. Read the [Shopify documentation](https://shopify.dev/docs/api/admin-rest/2024-04/resources/fulfillment#resource-object) for more information.

---
