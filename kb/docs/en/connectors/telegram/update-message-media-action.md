---
url: 'https://docs.workato.com/en/connectors/telegram/update-message-media-action.md'
description: >-
  Swap the photo, video, or file attached to a message your Telegram bot already
  sent for a new one.
---

# Telegram - Update message media action

The **Update message media** action replaces the media of an existing message in Telegram.

> **BOTS CAN ONLY EDIT THEIR OWN MESSAGES**
> 
> This action can only edit a message the bot itself sent. Editing a message from another user or bot fails. Messages can only be edited within 48 hours of being sent.

## Input

| Input field | Description |
| --- | --- |
| Chat ID | Enter the unique identifier for the target chat or the username of the target channel. Required if **Inline message ID** isn't specified. |
| Message ID | Enter the identifier of the message to edit. Required if **Inline message ID** isn't specified. |
| Inline message ID | Enter the identifier of the inline message to edit. Required if **Chat ID** and **Message ID** aren't specified. |
| Media type | Select the new media type. Options are **Audio**, **Photo**, **Animation**, **Video**, or **Document**. |
| Media | Enter the new file. Pass a file ID to send a file that already exists on Telegram's servers, or an HTTP URL for Telegram to fetch the file from the internet. |
| Caption | Optional. Enter a new caption for the file. |
| Parse mode | Optional. Select the mode to format the caption with bold, italic, or other styling. Options are **Markdown**, **MarkdownV2**, or **HTML**. Leave blank for plain text. |
| Reply markup | Optional. Enter a JSON-serialized inline keyboard, custom reply keyboard, or other reply markup object. |

## Output

This action returns the updated message. Refer to the Telegram Bot API [Message](https://core.telegram.org/bots/api#message) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Message ID | The message's unique identifier inside the chat. |
| From | The bot that sent the message. |
| Chat | The chat the message belongs to. |
| Date | The Unix timestamp the message was originally sent. |
| Edit date | The Unix timestamp the message was last edited. |
| Caption | The caption of the updated media, if any. |

---
