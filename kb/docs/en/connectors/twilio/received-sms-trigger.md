---
url: 'https://docs.workato.com/en/connectors/twilio/received-sms-trigger.md'
description: >-
  The Received SMS trigger in the Twilio connector picks up text messages
  received on a Twilio phone number you monitor, checking every five minutes.
---

# Twilio - Received SMS trigger

The Received SMS trigger checks for received SMS (text) messages every five minutes.

![Received SMS trigger](/assets/twilio-received-sms-trigger.C3nIi4x4.png)_Received SMS trigger_

## Input

| Input field | Description |
| --- | --- |
| Phone number | The Twilio phone number you plan to monitor for received SMSes. |

## Output

| Output field | Description |
| --- | --- |
| Body | The body (text) of the SMS received. |
| Direction | The direction (inbound or outbound) of the SMS. Received messages are inbound. |
| From | The phone number from which the SMS was sent. |
| Price | The amount it cost to send the SMS. This value is null if there is no cost per message for the phone plan. |
| Error message | This value is null if the message is sent successfully. |
| To | The phone number to which the SMS was sent. |
| Date created | The date the SMS was created. |
| Status | The status of the SMS (failed, success, or queued). |
| SID | This is the string identifier. This provides a unique key that is used to identify specific resources. Each SID has 34 digits. |
| Date sent | The date the SMS was sent. |
| Messaging service SID | The SID of the messaging service. This value is null if a messaging service wasn't used. |
| Error code | The error code if the message failed. |
| Price unit | The unit used to identify the price to send the message, for example, USD. |
| API version | The Twilio API version used by the sender. For example, `2010-04-01`. |
| Subresource URIs | If subresources, such as recordings or notifications, are present, the URIs display in the subresource URIs property. This value is blank if no subresource URIs are present. |

---
