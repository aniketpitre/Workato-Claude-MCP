---
url: 'https://docs.workato.com/en/connectors/telegram/send-sticker-action.md'
description: 'Send a static, animated, or video sticker from your Telegram bot to a chat.'
---

# Telegram - Send sticker action

The **Send sticker** action sends a static `.WEBP`, animated `.TGS`, or video `.WEBM` sticker to a chat in Telegram.

## Input

Input fields vary based on your **Send by** selection. The following input fields are common to all options. Refer to the Telegram Bot API [sendSticker](https://core.telegram.org/bots/api#sendsticker) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Send by | Select how to provide the sticker. Options are **File content**, **File ID**, or **File URL**. |
| Chat ID | Enter the unique identifier for the target chat or the username of the target channel. |
| Disable notification | Optional. Select whether to send the message silently. |
| Protect content | Optional. Select whether to protect the message content from forwarding and saving. |
| Reply markup | Optional. Enter a JSON-serialized inline keyboard, custom reply keyboard, or other reply markup object. |

## Output

This action returns the sent message. Refer to the Telegram Bot API [Message](https://core.telegram.org/bots/api#message) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Message ID | The message's unique identifier inside the chat. |
| From | The bot that sent the message. |
| Chat | The chat the message was sent to. |
| Date | The Unix timestamp the message was sent. |
| Sticker | The sent sticker's file details. |

---
