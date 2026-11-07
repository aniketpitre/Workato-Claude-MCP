---
url: 'https://docs.workato.com/en/connectors/telegram/send-document-action.md'
description: >-
  Send a file, such as a PDF, to a Telegram chat, provided as a file upload,
  file ID, or URL.
---

# Telegram - Send document action

The **Send document** action sends a file to a chat in Telegram.

## Input

Input fields vary based on your **Send by** selection. The following input fields are common to all options. Refer to the Telegram Bot API [sendDocument](https://core.telegram.org/bots/api#senddocument) documentation for the more information on available input fields.

| Input field | Description |
| --- | --- |
| Send by | Select how to provide the document. Options are **File content**, **File ID**, or **File URL**. |
| Chat ID | Enter the unique identifier for the target chat or the username of the target channel. |
| Caption | Optional. Enter a caption for the document. |
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
| Document | The sent document's file details. |
| Caption | The caption of the sent document, if any. |

---
