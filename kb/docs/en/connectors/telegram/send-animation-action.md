---
url: 'https://docs.workato.com/en/connectors/telegram/send-animation-action.md'
description: >-
  Post a GIF or muted video animation to a Telegram chat, provided as a file
  upload, file ID, or URL.
---

# Telegram - Send animation action

The **Send animation** action sends a GIF or a soundless H.264/MPEG-4 AVC video to a chat in Telegram.

## Input

Input fields vary based on your **Send by** selection. The following input fields are common to all options. Refer to the Telegram Bot API [sendAnimation](https://core.telegram.org/bots/api#sendanimation) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Send by | Select how to provide the animation. Options are **File content**, **File ID**, or **File URL**. |
| Chat ID | Enter the unique identifier for the target chat or the username of the target channel. |
| Caption | Optional. Enter a caption for the animation. |
| Disable notification | Optional. Select **Yes** or **No** to send the message silently. |
| Protect content | Optional. Select **Yes** or **No** to protect the message content from forwarding and saving. |

## Output

This action returns the sent message. Refer to the Telegram Bot API [Message](https://core.telegram.org/bots/api#message) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Message ID | The message's unique identifier inside the chat. |
| From | The bot that sent the message. |
| Chat | The chat the message was sent to. |
| Date | The Unix timestamp the message was sent. |
| Animation | The sent animation's file details. |
| Caption | The caption of the sent animation, if any. |

---
