---
url: 'https://docs.workato.com/en/connectors/telegram/new-events-trigger.md'
description: >-
  Fire a recipe on the Telegram event types you choose, such as new messages,
  channel posts, or chat membership changes.
---

# Telegram - New events trigger

The **New events** trigger monitors Telegram for an event type you specify, such as a channel post.

> **ONE TRIGGER PER CONNECTION**
> 
> Telegram supports only one active trigger per connection.

## Input

| Input field | Description |
| --- | --- |
| Events | Select the event types to subscribe to. Leave blank to subscribe to all event types. Some events, such as **Chat member**, require the bot to be a chat administrator. |

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
| Chat member | The updated status of a chat member. |

---
