---
url: 'https://docs.workato.com/en/connectors/shopify/update-store-metafield.md'
description: >-
  The Update store metafield action in the Shopify connector lets you update the
  metafields associated with a store.
---

# Shopify - Update store metafield action

This action updates metafields of a store in Shopify.

## Input

| Field | Description |
| --- | --- |
| Metafield ID | Identifier for the metafield |
| Value | Provide the value to the metafield. |
| Value type | For example, `integer`, `string` |

## Output

| Field | Description |
| --- | --- |
| ID | The ID for the metafield. |
| Key | Identifier for the metafield |
| Metafield name | Provide a name for the metafield. |
| Value | The value for the metafield |
| Value type | For example, `integer`, `string` |
| Description | The description for the metafield. |
| Owner ID | The parent object ID of the owner of the metafield. |
| Owner resource | The parent object type. |
| Created at | When this metafield was created. |
| Updated at | When this metafield was last updated. |

---

---
url: >-
  https://docs.workato.com/en/connectors/shopify/update-tracking-information-of-fulfillment.md
description: >-
  The Update tracking information of a fulfillment action in the Shopify
  connector lets you update the tracking details of a fulfillment.
---

# Shopify - Update tracking information of a fulfillment action

This action updates the tracking information of a fulfillment in Shopify.

## Input

| Field | Description |
| --- | --- |
| Fulfillment ID | The ID of the fulfillment. |
| Tracking information | Optional. The tracking information for the fulfillment. See below for the structure of each tracking information. |
| Notify customer? | Optional. Whether a notification should be sent to the customer when the fulfillment is created. Defaults to `false`. |

### Tracking information

| Field | Description |
| --- | --- |
| Tracking company | Optional. The name of the tracking company. |
| Tracking number | Optional. The tracking number for the fulfillment. |
| Tracking URL | Optional. The URL to track the fulfillment. |

## Output

The output of the action above is the selected fields from the `Fulfillment` resource. Read the [Shopify documentation](https://shopify.dev/docs/api/admin-rest/2024-04/resources/fulfillment#resource-object) for more information.

---
