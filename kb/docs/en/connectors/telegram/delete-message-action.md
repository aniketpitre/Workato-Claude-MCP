---
url: 'https://docs.workato.com/en/connectors/telegram/delete-message-action.md'
description: >-
  Remove a message your Telegram bot sent from a chat, for example to retract an
  outdated notification.
---

# Telegram - Delete message action

The **Delete message** action deletes an existing message from a chat in Telegram.

> **WHAT THE BOT CAN DELETE**
> 
> The bot can delete its own messages in private chats, groups, and supergroups, and incoming messages in private chats. To delete other users' messages, the bot needs administrator rights in the chat, including the **Can delete messages** right in supergroups and channels. Messages can only be deleted within 48 hours of being sent.

## Input

| Input field | Description |
| --- | --- |
| Chat ID | Enter the unique identifier for the target chat or the username of the target channel, for example `@channelusername`. |
| Message ID | Enter the identifier of the message to delete. |

## Output

| Output field | Description |
| --- | --- |
| Is deleted? | A boolean response (`true` or `false`) that indicates if the message was deleted successfully. |

---
