---
url: >-
  https://docs.workato.com/en/connectors/gmail-custom/get-message-content-action.md
description: >-
  The Get message content action gets the full content of a Gmail message,
  identified by a Pub/Sub notification payload or a message ID.
---

# Gmail (Custom) - Get message content action

The **Get message content** action gets the full content of a Gmail message. You can identify the message using the Pub/Sub payload from a Gmail push notification or directly from a Gmail message ID. This action requires the `https://mail.google.com/` OAuth scope.

Decoded message body content is included alongside the raw base64-encoded data returned by Gmail.

## Input

| Input field | Description |
| --- | --- |
| Identify message by | Select to identify the message using Pub/Sub message data or a message ID. Defaults to **Pub/Sub message data**. |
| User id | Enter the user's email address. |
| Pub/Sub message data | Enter the base64 encoded data from the Pub/Sub trigger. Shown when **Identify message by** is set to **Pub/Sub message data**. |

## Output

| Output field | Description |
| --- | --- |
| Message ID | The unique ID of the message. |
| Thread ID | The ID of the thread the message belongs to. |
| Label IDs | The IDs of labels applied to the message. |
| Snippet | A short excerpt from the message body. |
| Payload | The parsed email structure, including MIME headers and body parts. Each body part includes the raw base64-encoded content in **Data** and the decoded, human-readable text in **Decoded content**. |
| Size estimate | The estimated size of the message in bytes. |
| History ID | The ID of the last history record that modified the message. |
| Internal date | The internal Gmail timestamp for the message, in epoch milliseconds. |
