---
url: >-
  https://docs.workato.com/en/connectors/cisco-webex-teams/actions/post-message.md
description: >-
  The Post message action in the Cisco Webex Teams connector lets you post a
  message to a specified room or to a specific person.
---

# Cisco Webex Teams - Post message action

This action posts a message in a specified room or to a specific person in Cisco Webex Teams.

## Input

| Field | Description |
| --- | --- |
| Room name | Select the room where you plan to post the message. You can choose from a list of rooms or use a specific room ID. |
| Alternate text | Enter alternate text for the message. Required if **Message** is left blank. |
| Message | Enter the text content of the message. Required if **Alternate text** is left blank. |

Refer to the Webex [buttons and cards](https://developer.webex.com/docs/buttons-and-cards) documentation to learn how to design a message using blocks.

## Output

| Field | Description |
| --- | --- |
| Room type | The type of the room where the message was posted. |
| HTML | The HTML content of the message. |
| Message ID | The unique ID of the message. |
| Person ID | The ID of the person who sent the message. |
| Person email | The email address of the person who sent the message. |
| Room ID | The ID of the room where the message was posted. |
| Message | The text content of the message. |
| Markdown | The Markdown content of the message. |
| Attachments | An array of attachments included in the message. |
| Recipient ID | The ID of the recipient for private messages. |
| Recipient email | The email address of the recipient for private messages. |
| Created | The timestamp when the message was created. |
