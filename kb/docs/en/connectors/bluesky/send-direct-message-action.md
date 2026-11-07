---
url: 'https://docs.workato.com/en/connectors/bluesky/send-direct-message-action.md'
description: The Send direct message action enables you to send a Bluesky direct message.
---

# Bluesky - Send direct message action

The **Send direct message** action sends a direct message in Bluesky. This action requires a connection using an app password with DM (direct message) access enabled.

## Input

| Input field | Description |
| --- | --- |
| Recipient DID | Enter the decentralized identifier of the recipient. For example, `did:plc:...`. |
| Text | Enter the message text to send. |
| Facets | Enter any rich-text facets you plan to include in the direct message. |

## Output

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the sent message. |
| Revision | Revision of the message record. |
| Text | Text content of the sent message. |
| Sender | DID of the account that sent the message. |
| Sent at | Date and time when the message was sent. |
| Embed | Embedded record details, if the message includes one. |
| Reactions | List of reactions on the message, if applicable. |

---
