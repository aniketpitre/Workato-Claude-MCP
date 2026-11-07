---
url: 'https://docs.workato.com/en/connectors/tiktok-shop/new-record-trigger.md'
description: >-
  The New record trigger monitors TikTok Shop for newly created records, for
  example, newly created orders.
---

# TikTok Shop - New record trigger

The **New record** trigger monitors TikTok Shop for newly created records, for example, newly created orders. This trigger currently only supports the **Order** object.

## Input

| Input Field | Description |
| --- | --- |
| Trigger poll interval | Select how frequently to check for newly created records. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up trigger events from this date and time. Defaults to one hour before the recipe starts. You cannot change this value after the recipe runs or is tested. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output Field | Description |
| --- | --- |
| ID | The unique ID of the order. |
| Shipping provider | The name of the current shipping provider. |
| Status | The status of the order, for example: `UNPAID` or `ON_HOLD`. |
| Delivery type | Indicates whether the delivery is to a Pick-Up Drop-Off (PUDO) location. The buyer can select a PUDO location when they place an order. |
| Shipping type | The delivery method, such as `TIKTOK` or `SELLER`. |
| User ID | The buyer's user ID. |
| Tracking number | The shipment's tracking number. |
| Warehouse ID | The seller's warehouse ID. |
| Order type | The type of order placed, for example: `PRE_ORDER` or `MADE_TO_ORDER`. |
| Paid time | A Unix timestamp of the date and time the order was paid. |

---

---
url: >-
  https://docs.workato.com/en/connectors/tiktok-shop/new-updated-record-trigger.md
description: >-
  The New/Updated Record trigger monitors TikTok Shop for newly created or
  updated records, for example, newly created orders.
---

# TikTok Shop - New/updated record trigger

The **New/updated record** trigger monitors TikTok Shop for newly created or updated records, for example, newly created orders. This trigger currently only supports the **Order** object.

## Input

| Input Field | Description |
| --- | --- |
| Trigger poll interval | Select how frequently to check for newly created or updated records. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up trigger events from this date and time. Defaults to one hour before the recipe starts. You cannot change this value after the recipe runs or is tested. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output Field | Description |
| --- | --- |
| ID | The unique ID of the order. |
| Shipping provider | The name of the current shipping provider. |
| Status | The status of the order, for example: `UNPAID` or `ON_HOLD`. |
| Delivery type | Indicates whether the delivery is to a Pick-Up Drop-Off (PUDO) location. The buyer can select a PUDO location when they place an order. |
| Shipping type | The delivery method, such as `TIKTOK` or `SELLER`. |
| User ID | The buyer's user ID. |
| Tracking number | The shipment's tracking number. |
| Warehouse ID | The seller's warehouse ID. |
| Order type | The type of order placed, for example: `PRE_ORDER` or `MADE_TO_ORDER`. |
| Paid time | A Unix timestamp of the date and time the order was paid. |

---

---
url: >-
  https://docs.workato.com/en/connectors/tiktok-shop/get-record-details-by-id-action.md
description: >-
  The Get record details by ID action retrieves details about a specific record
  in TikTok Shop.
---

# TikTok Shop - Get record details by ID action

The **Get record details by ID** action retrieves details about a specific record in TikTok Shop. This action currently only supports the **Order** object.

## Input

| Input Field | Description |
| --- | --- |
| IDs | Enter a list of record IDs to retrieve details from. |

## Output

| Output Field | Description |
| --- | --- |
| Code | The success or failure message returned in the API response. |
| Message | An object detailing the product prices. |
| Request ID | A unique customer ID. |
| Company | A log of requests. |
| Orders | An object containing details about retrieved records, such as their `ID`, `Shipping type` , `Status`, and the `User ID` of the buyer. Refer to TikTok Shop's [Get Order Detail documentation](https://partner.tiktokshop.com/docv2/page/get-order-detail-202309) for more information. |

---
