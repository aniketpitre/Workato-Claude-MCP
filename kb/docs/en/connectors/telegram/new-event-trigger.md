---
url: 'https://docs.workato.com/en/connectors/telegram/new-event-trigger.md'
description: >-
  Fire a recipe on a fixed set of Telegram events, such as new messages or
  channel posts. Deprecated in favor of New events.
---

# Telegram - New event trigger

The **New event** trigger monitors Telegram for new events, such as channel posts.

> **DEPRECATION NOTICE**
> 
> This trigger is deprecated. Use the [New events](/en/connectors/telegram/new-events-trigger) trigger instead, which lets you select which event types to subscribe to.

> **ONE TRIGGER PER CONNECTION**
> 
> Telegram supports only one active trigger per connection.

## Input

This trigger doesn't have any input fields.

## Output

This trigger's output fields vary based on event type. The following table contains frequently returned fields. Refer to the Telegram Bot API [Update](https://core.telegram.org/bots/api#update) documentation for more information on available event types.

| Output field | Description |
| --- | --- |
| Update ID | The update's unique identifier. |
| Message | A new incoming message of any kind, such as text, photo, or sticker. |
| Edited message | The new version of an edited message. |
| Channel post | The new incoming channel post of any kind, such as text, photo, or sticker. |
| Edited channel post | The new version of an edited channel post. |
| Inline query | The new incoming inline query. |
| Callback query | The new incoming callback query. |
| Shipping query | The new incoming shipping query. |
| Pre-checkout query | The new incoming pre-checkout query. |
| Chat member | The updated status of a chat member. Requires the bot to be a chat administrator. |

---
