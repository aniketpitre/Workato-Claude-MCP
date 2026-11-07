---
url: >-
  https://docs.workato.com/en/connectors/ringcentral/actions/send-pager-message.md
description: >-
  Use the Send pager message action to send a pager message to specified
  extension numbers within RingCentral.
---

# RingCentral - Send pager message action

The **Send pager message** action sends a pager message to specified extension numbers within RingCentral.

## Input

| Field | Description |
| --- | --- |
| To source list | Provide a list datapill that contains the recipients’ extension numbers. Learn more about [list input](/en/features/list-management#list-batch-action). |
| Extension number (to) | Enter the recipient's extension number. For example, `102`. |
| Extension number (from) | Enter the sender's extension number. For example, `101`. |
| Text | Enter the content of the pager message. |

## Output

| Field | Description |
| --- | --- |
| URI | The URI of the message. |
| ID | The unique identifier of the message. |
| To | An array containing information about the recipients. |
| Extension ID (to) | The recipient's extension ID. |
| Extension number (to) | The recipient's extension number. |
| Name (to) | The recipient's name. |
| From | An object containing information about the sender. |
| Extension ID (from) | The sender's extension ID. |
| Extension number (from) | The sender's extension number. |
| Name (from) | The sender's name. |
| Type | The type of message. |
| Creation time | The timestamp when the message was created. |
| Read status | The read status of the message. |
| Priority | The priority of the message. |
| Attachments | An array containing information about message attachments. |
| ID (attachments) | The unique identifier of the attachment. |
| URI (attachments) | The URI of the attachment. |
| Type (attachments) | The type of attachment. |
| Content type (attachments) | The content type of the attachment. |
| Direction | The direction of the message (for example, inbound or outbound). |
| Availability | The availability status of the message. |
| Subject | The subject of the message. |
| Message status | The status of the message. |
| Conversation ID | The unique identifier of the conversation. |
| Conversation | An object containing details about the conversation. |
| ID (conversation) | The unique identifier of the conversation. |
| URI (conversation) | The URI of the conversation. |
| Last modified time | The timestamp when the message was last modified. |
| Pg to department | Indicates whether the pager message was sent to an entire department. |
