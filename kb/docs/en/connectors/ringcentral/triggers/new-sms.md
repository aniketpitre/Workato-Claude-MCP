---
url: 'https://docs.workato.com/en/connectors/ringcentral/triggers/new-sms.md'
description: >-
  Use the New SMS trigger to monitor when your connected RingCentral extension
  receives new SMS messages.
---

# RingCentral - New SMS trigger

The **New SMS** trigger activates when a new SMS message is received by the connected RingCentral extension. The trigger checks for new SMS messages every five minutes.

Ensure the connected RingCentral extension has **SMS** and **Read Messages** permissions. These permissions are typically enabled for predefined or default RingCentral roles.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. The minimum allowed value is five minutes. |
| When first started, this recipe should pick up events from | Specify the start time to retrieve new SMS messages received since this time. Defaults to one hour before the recipe is first started if left blank. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Field | Description |
| --- | --- |
| URI | The URI of the SMS message. |
| ID | The unique identifier of the SMS message. |
| To | A list containing the recipients of the SMS message. |
| Phone number (to) | The phone number of the recipient. |
| Extension ID (to) | The unique identifier of the recipient's extension. |
| Extension number (to) | The extension number of the recipient. |
| Name (to) | The name associated with the recipient. |
| From | An object containing information about the sender of the SMS message. |
| Phone number (from) | The phone number of the sender. |
| Extension ID (from) | The unique identifier of the sender's extension. |
| Extension number (from) | The extension number of the sender. |
| Name (from) | The name associated with the sender. |
| Type | The type of message. |
| Creation time | The time the message was created in ISO 8601 format. |
| Read status | Indicates whether the message has been read. |
| Priority | The priority of the message. |
| Attachments | An object containing details about the attachments. |
| ID (attachments) | The unique identifier of the attachment. |
| URI (attachments) | The URI of the attachment. |
| Type (attachments) | The type of attachment. |
| Content type (attachments) | The content type of the attachment. |
| Direction | The direction of the message (for example, inbound or outbound). |
| Availability | Indicates the availability status of the message. |
| Subject | The subject of the message, if specified. |
| Message status | The current status of the message. |
| Conversation ID | The unique identifier of the conversation the message belongs to. |
| Conversation | An object containing details about the conversation. |
| ID (conversation) | The unique identifier of the conversation. |
| URI (conversation) | The URI of the conversation. |
| Last modified time | The last modified time of the message in ISO 8601 format. |
| Pg to department | Indicates whether the message was sent to an entire department. |

---
