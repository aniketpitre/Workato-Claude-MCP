---
url: 'https://docs.workato.com/en/connectors/gumroad/new-event-trigger.md'
description: >-
  Invoke a recipe in real time when a Gumroad sale, refund, dispute,
  cancellation, or subscription event occurs.
---

# Gumroad - New event trigger

The **New event** trigger invokes in real time when a resource event, such as a sale, refund, or subscription change, occurs in Gumroad.

## Input

| Input field | Description |
| --- | --- |
| Resource | Select the event type to monitor. Options are **Sale**, **Refund**, **Dispute**, **Dispute won**, **Cancellation**, **Subscription updated**, **Subscription ended**, or **Subscription restarted**. |
| Payload schema | Optional. Define additional output fields from the webhook payload that aren't in the standard output. Leave blank to return only the standard output fields. |

## Output

Output fields dynamically generate based on the **Resource** you select. Refer to the Gumroad [API](https://app.gumroad.com/api) documentation for more information on available output fields. The following fields are common to all resources:

| Output field | Description |
| --- | --- |
| Product ID | The unique ID of the product. |
| Product name | The name of the product. |
| Subscription ID | The unique ID of the subscription. |
| Recurrence | How often the subscription renews. |
| License key | The license key issued for the purchase or subscription. |
| Custom fields | The custom fields the buyer completed at checkout. |
| Resource name | The event type that invoked the trigger. |

---

---
url: >-
  https://docs.workato.com/en/connectors/gumroad/enable-or-disable-license-action.md
description: >-
  Enable or disable a license key for a product in Gumroad. A disabled license
  key fails verification.
---

# Gumroad - Enable or disable license action

The **Enable or disable license** action enables or disables a license key for a product in Gumroad. A disabled license key fails verification.

## Input

| Input field | Description |
| --- | --- |
| Mode | Select **Enable** to activate the license key, or **Disable** to deactivate it. |
| Product ID | Select the product the license key belongs to. Alternatively, enter the product ID. |
| License key | Enter the license key to enable or disable. |

## Output

The following are a representative set of output fields. Refer to the Gumroad [API](https://app.gumroad.com/api) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Success | A boolean value (`true` or `false`) that indicates whether the action updated the license key. |
| Message | A message from Gumroad about the result. This field is blank when Gumroad doesn't return a message. |
| Uses | The number of times the license key has been used. |
| Purchase | The purchase the license key belongs to. |
| Sale ID (Purchase) | The unique ID of the sale. |
| Product ID (Purchase) | The unique ID of the product. |
| Product name (Purchase) | The name of the product. |
| Email (Purchase) | The buyer's email address. |
| License key (Purchase) | The license key for the purchase. |
| Refunded (Purchase) | A boolean value (`true` or `false`) that indicates whether the sale was refunded. |

---

---
url: >-
  https://docs.workato.com/en/connectors/gumroad/get-record-details-by-id-action.md
description: >-
  Retrieve the details of a Gumroad record, such as a sale or subscriber, by its
  unique ID.
---

# Gumroad - Get record details by ID action

The **Get record details by ID** action retrieves a record, such as a sale or subscriber, by its unique ID in Gumroad.

## Input

Input fields dynamically generate based on the **Object** you select.

| Input field | Description |
| --- | --- |
| Object | Select the object type. Options are **Sale** or **Subscriber**. |
| Sale ID | Select the sale to retrieve. Alternatively, enter the sale ID. The **Sale ID** field is only available when **Object** is **Sale**. |
| Subscriber ID | Enter the unique ID of the subscriber to retrieve. The **Subscriber ID** field is only available when **Object** is **Subscriber**. |

## Output

Output fields dynamically generate based on the **Object** you select. Refer to the Gumroad [API](https://app.gumroad.com/api) documentation for more information on available output fields. The following fields are common to all objects:

| Output field | Description |
| --- | --- |
| ID | The unique ID of the record. |
| Email | The email address of the buyer or subscriber. |
| Product ID | The unique ID of the product. |
| Product name | The name of the product. |
| Created at | The date and time the record was created. |
| License key | The license key issued for the record. |

---
