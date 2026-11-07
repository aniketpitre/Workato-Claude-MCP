---
url: 'https://docs.workato.com/en/connectors/telegram/send-photo-action.md'
description: 'Post a photo, optionally with a spoiler cover or caption, to a Telegram chat.'
---

# Telegram - Send photo action

The **Send photo** action sends a photo to a chat in Telegram.

## Input

Input fields vary based on your **Send by** selection. The following input fields are common to all options. Refer to the Telegram Bot API [sendPhoto](https://core.telegram.org/bots/api#sendphoto) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Send by | Select how to provide the photo. Options are **File content**, **File ID**, or **File URL**. |
| Chat ID | Enter the unique identifier for the target chat or the username of the target channel. |
| Caption | Optional. Enter a caption for the photo. |
| Parse mode | Optional. Select the mode to format the caption with bold, italic, or other styling. Options are **Markdown**, **MarkdownV2**, or **HTML**. Leave blank for plain text. |
| Has spoiler | Optional. Select whether to cover the photo with a spoiler animation. |
| Disable notification | Optional. Select whether to send the message silently. |
| Protect content | Optional. Select whether to protect the message content from forwarding and saving. |

## Output

This action returns the sent message. Refer to the Telegram Bot API [Message](https://core.telegram.org/bots/api#message) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Message ID | The message's unique identifier inside the chat. |
| From | The bot that sent the message. |
| Chat | The chat the message was sent to. |
| Date | The Unix timestamp the message was sent. |
| Photo | The available sizes of the sent photo. |
| Caption | The caption of the sent photo, if any. |

---
