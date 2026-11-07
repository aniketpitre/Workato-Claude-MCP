---
url: 'https://docs.workato.com/en/connectors/cornerstone-hr/new-record-trigger.md'
description: >-
  The New record trigger activates when a record, such as a user, is created in
  Cornerstone.
---

# Cornerstone HR - New record trigger

The **New record** trigger activates when a record, such as a user, is created in Cornerstone HR.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object you plan to monitor for new records. Options are **User** and **Training**. |
| When first started, this recipe should pick up events from | Select the date and time this recipe starts picking up events from when you run it for the first time. Leave blank to pick up records created one hour ago. |

## Output

Output fields dynamically generate based on the object you select. Refer to the [Cornerstone API documentation](https://apiexplorer.csod.com) for a complete list of output fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/cornerstone-hr/new-updated-record-trigger.md
description: >-
  The New/updated record trigger activates when a record, such as a user, is
  created or updated in Cornerstone.
---

# Cornerstone HR - New/updated record trigger

The **New/updated record** trigger activates when a record, such as a user, is created or updated in Cornerstone HR.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object you plan to monitor for new or updated records. Options are **User** and **Training**. |
| When first started, this recipe should pick up events from | Select the date and time this recipe starts picking up events from when you run it for the first time. Leave blank to pick up records created one hour ago. |

## Output

Output fields dynamically generate based on the object you select. Refer to the [Cornerstone API documentation](https://apiexplorer.csod.com) for a complete list of output fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/cornerstone-hr/new-record-batch-trigger.md
description: >-
  The New record batch trigger activates when records, such as users, are
  created in Cornerstone, and returns them in batches.
---

# Cornerstone HR - New record batch trigger

The **New record batch** trigger activates when records, such as users, are created in Cornerstone HR, and returns them in batches.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object you plan to monitor for new records. Options are **User** and **Training**. |
| When first started, this recipe should pick up events from | Select the date and time this recipe starts picking up events from when you run it for the first time. Leave blank to pick up records created one hour ago. |

## Output

Output fields dynamically generate based on the object you select, returned as an array of records. Refer to the [Cornerstone API documentation](https://apiexplorer.csod.com) for a complete list of output fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/cornerstone-hr/new-updated-record-batch-trigger.md
description: >-
  The New/updated record batch trigger activates when records, such as users,
  are created or updated in Cornerstone, and returns them in batches.
---

# Cornerstone HR - New/updated record batch trigger

The **New/updated record batch** trigger activates when records, such as users, are created or updated in Cornerstone HR, and returns them in batches.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object you plan to monitor for new or updated records. Options are **User** and **Training**. |
| When first started, this recipe should pick up events from | Select the date and time this recipe starts picking up events from when you run it for the first time. Leave blank to pick up records created one hour ago. |

## Output

Output fields dynamically generate based on the object you select, returned as an array of records. Refer to the [Cornerstone API documentation](https://apiexplorer.csod.com) for a complete list of output fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/cornerstone-hr/new-webhook-event-trigger.md
description: >-
  The New webhook event trigger activates when Cornerstone sends a webhook
  notification for an event type you select, such as training completed or
  employee created.
---

# Cornerstone HR - New webhook event (real-time) trigger

The **New webhook event (real-time)** trigger activates when Cornerstone HR sends a webhook notification for an event type you select, such as training completed or employee created.

## Input

| Input field | Description |
| --- | --- |
| Event types | Select one or more event types you plan to monitor. Only matching events trigger this recipe. Options are grouped into categories, including `Employee`, `Skills library`, `Training`, `User ratings`, `User skills`, `Status`, `Recruiting`, `Ecommerce`, and `Alerts`. |
| Webhook API key | Enter the `x-api-key` value configured on your Cornerstone HR webhook endpoint. Cornerstone HR sends this header with every webhook callback. Leave blank if API key authentication isn't enabled. |
| Webhook HMAC secret | The Base64-encoded secret key configured on your Cornerstone HR webhook endpoint for HMAC-SHA256 authentication. Used to verify webhook payload integrity. Leave blank if HMAC-SHA256 isn't enabled. |

## Output

| Output field | Description |
| --- | --- |
| Subscription ID | The unique identifier for the Cornerstone webhook subscription. |
| Session ID | The unique identifier for the webhook delivery session. |
| Attempt number | The delivery attempt number for this webhook notification. |
| Offset | The offset of the event record within the stream. |
| Timestamp | The date and time the event occurred. |
| Correlation ID | The unique identifier used to correlate related events. |
| Lag | The delay, in seconds, between when the event occurred and when it was delivered. |
| Event name | The name of the Cornerstone event that occurred, for example, **Training completed** or **Employee created**. |
| Data | An object containing the event-specific details. The **Data** field's contents vary based on the event type received. Refer to the [Cornerstone Webhooks Guide](https://csod.dev/guides/webhooks/) for the fields available for each event type. |

---
