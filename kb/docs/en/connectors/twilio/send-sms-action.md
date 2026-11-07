---
url: 'https://docs.workato.com/en/connectors/twilio/send-sms-action.md'
description: >-
  The Send SMS action in the Twilio connector lets you send a text message from
  a Twilio phone number or alphanumeric sender ID.
---

# Twilio - Send SMS action

This action sends an SMS (text) message.

![Send SMS action](/assets/send-sms-action.BhoXBG-c.png)_Send SMS action_

## Input

| Input field | Description |
| --- | --- |
| From | The Twilio phone number from which the SMS is sent. You can use an [alphanumeric value](https://help.twilio.com/articles/223181348#h_01FGPN6Y5Z7NK4HB7BP1X13A5F) rather than a phone number to improve deliverability, for example `Acme-Corporation`. |
| To | The phone number to which the SMS is sent. The phone number must include the country code. For example, `+14235550001`. |
| Message | The message you plan to send. This field is limited to 160 characters. |

## Output

| Output field | Description |
| --- | --- |
| Body | The content of the SMS. |
| num\_segments | The number of segments within the SMS. |
| Direction | The direction (inbound or outbound) of the SMS. Sent messages are outbound. |
| From | The phone number or alphanumeric value from which the SMS was sent. For example, `+14325550001` or `Acme-Corporation`. |
| Date\_updated | The date the message was updated. For example, `Tue, 05 Dec 2023 18:57:20 +0000`. |
| Price | The amount it cost to send the SMS. This value is null if there is no cost per message for the phone plan. |
| Error message | This value is null if the message is sent successfully. |
| URI | The unique identifier for the SMS. |
| Account\_SID | This is the string identifier. This provides unique key that is used to identify specific resources. Each SID has 34 digits. |
| Num media | The multimedia (for example, images or emojis) within the SMS. This value is null if the SMS contains no media. |
| To | The phone number to which the SMS was sent. |
| Date\_created | The date the SMS was created. |
| Status | The status of the SMS. For example, failed, success, or queued. |
| SID | This is the string identifier. This provides a unique key that is used to identify specific resources. Each SID has 34 digits. |
| Date sent | The date the SMS was sent. |
| Messaging service SID | The SID of the messaging service. This value is null if a messaging service wasn't used. |
| Error\_code | The error code if the message failed. |
| Price\_unit | The unit used to identify the price to send the message, for example, USD. |
| API\_version | The Twilio API version used by the sender. For example, `2010-04-01`. |
| Subresource URIs | If subresources, such as recordings or notifications, are present, the URIs display in the subresource URIs property. This value is blank if no subresource URIs are present. |

---
