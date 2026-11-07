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
