---
url: 'https://docs.workato.com/en/connectors/shopify/delete-draft-order.md'
description: >-
  The Delete draft order action in the Shopify connector lets you delete an
  existing draft order that has not yet been converted to an order.
---

# Shopify - Delete draft order action

This action deletes a draft order on Shopify. A draft order represents the intent of ordering by a customer. It can be transitioned into an order.

Refer to the [Shopify documentation](https://shopify.dev/api/admin-rest/2022-01/resources/draftorder) for more information on the draft order resource.

## Input

| Field | Description |
| --- | --- |
| Draft order ID | The ID of the draft order to be deleted. |

## Output

There is no return payload upon successful deletion. Successful deletion is indicated by a `200` response code.

---
