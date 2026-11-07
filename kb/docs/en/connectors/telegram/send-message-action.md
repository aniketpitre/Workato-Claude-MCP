---
url: 'https://docs.workato.com/en/connectors/telegram/send-message-action.md'
description: >-
  Post a plain-text or formatted message from your Telegram bot to a chat or
  channel.
---

# Telegram - Send message action

The **Send message** action sends a text message to a chat in Telegram.

## Input

| Input field | Description |
| --- | --- |
| Chat ID | Enter the unique identifier for the target chat or the username of the target channel, for example `@channelusername`. |
| Message to send | Enter the text of the message. Maximum 4096 characters. |
| Parse mode | Optional. Select the mode to format the message text with bold, italic, or other styling. Options are **Markdown**, **MarkdownV2**, or **HTML**. Leave blank for plain text. |
| Disable web page preview | Optional. Select whether to disable link previews for links in this message. |
| Disable notification | Optional. Select whether to send the message silently. |
| Protect content | Optional. Select whether to protect the message content from forwarding and saving. |
| Allow sending without reply | Optional. Select whether to send the message even if the message being replied to is deleted or doesn't exist. |
| Reply to message ID | Optional. Enter the ID of the message this message is replying to. |
| Reply markup | Optional. Enter a JSON-serialized inline keyboard, custom reply keyboard, or other reply markup object. |

## Output

This action returns the sent message. Refer to the Telegram Bot API [Message](https://core.telegram.org/bots/api#message) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Message ID | The message's unique identifier inside the chat. |
| From | The bot that sent the message. |
| Chat | The chat the message was sent to. |
| Date | The Unix timestamp the message was sent. |
| Text | The text of the message that was sent. |

---

---
url: >-
  https://docs.workato.com/en/connectors/telegram/send-message-with-buttons-or-voice-action.md
description: >-
  Send an interactive message with tappable inline buttons, or a voice note,
  from your Telegram bot to a chat.
---

# Telegram - Send message with buttons or voice action

The **Send message with buttons or voice** action sends either a text message with an inline keyboard or a voice note to a chat in Telegram. Voice audio must be OGG/OPUS, MP3, or M4A format.

## Input

Input fields vary based on your **Message type** selection. The following input fields are common to both options. Refer to the Telegram Bot API [sendMessage](https://core.telegram.org/bots/api#sendmessage) and [sendVoice](https://core.telegram.org/bots/api#sendvoice) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Message type | Select the type of message to send. Options are **Text with buttons** or **Voice message**. Defaults to **Text with buttons**. |
| Chat ID | Enter the unique identifier for the target chat or the username of the target bot, supergroup, or channel. |
| Parse mode | Optional. Select the mode to format the message text with bold, italic, or other styling. Options are **Markdown**, **MarkdownV2**, or **HTML**. Leave blank for plain text. |
| Disable notification | Optional. Select whether to send the message silently. If **Yes**, users receive a notification with no sound. |
| Protect content | Optional. Select whether to protect the message content from forwarding and saving. |
| Reply parameters | Optional. Enter a description of the message this message is replying to. |

> **VOICE CONTENT REQUIRED**
> 
> Provide either a voice file (URL or file ID) or base64-encoded voice content for voice messages. The action fails if both are left blank.

## Output

Output fields vary based on your **Message type** selection. The following output fields are common to both options. Refer to the Telegram Bot API [Message](https://core.telegram.org/bots/api#message) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Message ID | The message's unique identifier inside the chat. |
| Chat | The chat the message was sent to. |
| Date | The Unix timestamp the message was sent. |

---
