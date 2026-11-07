---
url: >-
  https://docs.workato.com/en/connectors/nocodb/new-updated-deleted-record-trigger.md
description: >-
  Start a recipe in real time when rows in a NocoDB table are inserted, updated,
  or deleted, using a webhook.
---

# NocoDB - New/updated/deleted record (real-time) trigger

The **New/updated/deleted record (real-time)** trigger registers a webhook on a NocoDB table and starts a recipe when rows are inserted, updated, or deleted.

NocoDB sends webhook events to a public Workato webhook URL. This trigger supports NocoDB Cloud and self-hosted NocoDB instances with outbound internet access.

The on-prem agent only proxies requests from Workato to NocoDB. It doesn't proxy webhook events from NocoDB to Workato.

Use the [New/updated record trigger](/en/connectors/nocodb/new-updated-record-trigger)⁠ instead if your NocoDB instance can't access the internet.

## Input

| Input field | Description |
| --- | --- |
| Base | Select the base ID, which starts with `p`. |
| Table | Select the table ID, which starts with `m`. |
| Event | Select the event you plan to subscribe to: `After insert`, `After update`, `After delete`, or `Send me everything`. The `Send me everything` option registers webhooks for insert, update, and delete events. |
| Output schema | Enter the output schema you plan to use. |

## Output

| Output field | Description |
| --- | --- |
| Id | Webhook event ID. |
| Type | Event type. For example, `records.after.insert`. |
| Data | Payload object that contains `table_id`, `table_name`, and `rows`. |
