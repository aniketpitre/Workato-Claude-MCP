---
url: 'https://docs.workato.com/en/connectors/resend/new-email-event-trigger.md'
description: >-
  Invoke a recipe in real time when a Resend email bounces, receives a
  complaint, is delayed, or fails.
---

# Resend - New email event trigger

The **New email event** trigger invokes in real time when a selected email event, such as a bounce or complaint, occurs in Resend. Workato creates a webhook in Resend when you start the recipe and removes it when you stop the recipe.

## Input

| Input field | Description |
| --- | --- |
| Event types | Select one or more event types to monitor. Options are **Bounced**, **Complained**, **Delivery delayed**, or **Failed**. |

## Output

The following are a representative set of output fields. Refer to the Resend [Webhook Event Types](https://resend.com/docs/dashboard/webhooks/event-types) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| SVIX ID | The unique ID of the webhook delivery. Workato uses this ID to deduplicate events. |
| Type | The event type. For example, `email.bounced`. |
| Created at | The date and time the event occurred. |
| Data | The details of the email that invoked the trigger. |
| Email ID (Data) | The unique ID of the email. |
| From (Data) | The sender's email address. |
| To (Data) | The recipients' email addresses. |
| Subject (Data) | The subject of the email. |
| Tags (Data) | The tags attached to the email, as name and value pairs. |
| Bounce (Data) | The details of the bounce. This field is blank except for `email.bounced` events. |

---
