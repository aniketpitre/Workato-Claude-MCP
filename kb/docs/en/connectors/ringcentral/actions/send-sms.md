---
url: 'https://docs.workato.com/en/connectors/ringcentral/actions/send-sms.md'
description: >-
  Use the Send SMS action to send an SMS message to a specified phone number
  using RingCentral.
---

# RingCentral - Send SMS action

The **Send SMS** action sends an SMS message to a phone number you specify using RingCentral.

## Input

| Field | Description |
| --- | --- |
| Phone number (to) | Enter the recipient's phone number in E.164 format. For example, `+18001237788`. |
| Phone number (from) | Enter the sender's phone number in E.164 format. For example, `+18001237788`. |
| Text | Enter the content of the SMS message. |

## Output

| Field | Description |
| --- | --- |
| URI | The URI of the message. |
| ID | The unique identifier of the message. |
| To | An array containing information about the recipient. |
| Phone number (to) | The phone number of the recipient. |
| Name (to) | The name associated with the recipient. |
| From | An object containing the sender's phone number and name. |
| Phone number (from) | The phone number of the sender. |
| Name (from) | The name associated with the sender. |
| Type | The type of message. |
| Creation time | The timestamp when the message was created. |
| Read status | The read status of the message. |
| Priority | The priority of the message. |
| Attachments | An array containing details about the attachments. |
| ID (attachments) | The unique identifier of the attachment. |
| URI (attachments) | The URI of the attachment. |
| Type (attachments) | The type of attachment. |
| Content type (attachments) | The content type of the attachment. |
| Direction | Indicates whether the message is inbound or outbound. |
| Availability | The availability status of the message. |
| Subject | The subject of the message. |
| Message status | The status of the message. |
| Conversation ID | The unique identifier of the conversation. |
| Conversation | An object containing details about the conversation. |
| ID (conversation) | The unique identifier of the conversation. |
| URI (conversation) | The URI of the conversation. |
| Last modified time | The timestamp when the message was last modified. |

---
