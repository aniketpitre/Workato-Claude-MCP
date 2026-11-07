---
url: 'https://docs.workato.com/en/connectors/telegram/send-chat-action.md'
description: >-
  Show a status indicator, such as typing or uploading a photo, in a Telegram
  chat so users know your bot is active.
---

# Telegram - Send chat action

The **Send chat** action shows a status, such as **typing...**, in a chat so users know the bot is working in Telegram. The indicator clears after 5 seconds or when the bot's next message is sent.

## Input

| Input field | Description |
| --- | --- |
| Business connection ID | Optional. Enter the unique identifier of the business connection on behalf of which the action is sent. |
| Chat ID | Enter the unique identifier for the target chat or the username of the target channel. |
| Message thread ID | Optional. Enter the unique identifier of the target message thread or forum topic. Only for supergroups and private chats with forum topic mode enabled. |
| Action | Select the status to broadcast, such as **Typing**, **Upload photo**, **Record voice**, or **Upload document**. |

## Output

| Output field | Description |
| --- | --- |
| Is sent? | A boolean response (`true` or `false`) that indicates if the status was broadcast successfully. |

---
