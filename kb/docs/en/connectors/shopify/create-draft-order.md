---
url: 'https://docs.workato.com/en/connectors/shopify/create-draft-order.md'
description: >-
  The Create draft order action in the Shopify connector lets you create a draft
  order for a list of items that can later become an order.
---

# Shopify - Create draft order action

This action creates a draft order for a list of items on Shopify. A draft order represents the intent of ordering by a customer. It can be transitioned into an order.

Refer to the [Shopify documentation](https://shopify.dev/api/admin-rest/2022-01/resources/draftorder) for more information on the draft order resource.

## Input

| Field | Description |
| --- | --- |
| Customer ID | The ID of the customer for whom the draft order is created. |
| Use customer default address | If set to `yes/1`, attach the customer’s default address as the shipping address. Defaults to `false/0`. |
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

The output of this action is a datatree that contains information about the draft order object created.

Learn more about the [draft order object](https://shopify.dev/api/admin-rest/2024-04/resources/draftorder#resource-object).

---
