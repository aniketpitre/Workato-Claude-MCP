---
url: 'https://docs.workato.com/en/connectors/shopify/update-draft-order.md'
description: >-
  The Update draft order action in the Shopify connector lets you modify an
  existing draft order, including its line items, notes, and applied discounts.
---

# Shopify - Update draft order action

This action updates a draft order on Shopify. A draft order represents the intent of ordering by a customer. It can be transitioned into an order.

Refer to the [Shopify documentation](https://shopify.dev/api/admin-rest/2022-01/resources/draftorder) for more information on the draft order resource.

## Input

| Field | Description |
| --- | --- |
| Draft order ID | The ID of the draft order to be updated. |
| Note | Optional. Note to be attached onto the draft order. |
| Line items | These are the items purchased under this order. At least one item should be added into the draft order. Currently, Workato does not support the creation of custom items. See below for the structure of each line item. |
| Applied order discount | Optional. The amount discount applied to the draft order. See below for the structure of the applied discount. |

### Line item

| Field | Description |
| --- | --- |
| Product ID | Optional. The ID of the product to be added into the draft order. Either this or variant ID needs to be present. If variant ID is also input, variant ID is used instead. |
| Variant ID | Optional. The ID of the product variant to be added into the draft order. Either this or variant ID needs to be present. Note that variant ID takes precedence over product ID. |
| Quantity | The purchase quantity of the item. |
| Applied item discount | Optional. The amount discount applied to the item. See below for the structure of the applied discount. |

### Applied discount

| Field | Description |
| --- | --- |
| Description | Text describing the discount applied. |
| Value type | The type of discount applied. If set to string, accepts `percentage` or `fixed` as possible inputs. |
| Value | The applicable discount. If the value type is `percentage`, then the value is the percentage amount. If the value type is `fixed` then the value is the amount deductible from the original price. |

## Output

The output of this action is a datatree that contains information about the draft order object modified.

Learn more about the [draft order object](https://shopify.dev/api/admin-rest/2024-04/resources/draftorder#resource-object).

---
