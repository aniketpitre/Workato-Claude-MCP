---
url: 'https://docs.workato.com/en/connectors/twilio/make-phone-call-action.md'
description: >-
  The Make phone call action in the Twilio connector lets you place an automated
  voice call that speaks a message you provide to the recipient.
---

# Twilio - Make phone call action

This action allows you to make an automated voice phone call. For example, if a trigger event occurs, the action makes a call to a phone number that you configure, and an artificial voice speaks aloud the message you provided. This option does not allow the call recipient to press a key on the dial pad to interact with the call.

![Make phone call](/assets/make-phone-call-action.BFY1GHei.png)_Make phone call action_

## Input

| Input field | Description |
| --- | --- |
| From | The Twilio phone number from which the phone call is made. |
| To | The phone number to which the phone call is made. The phone number must include the country code. For example, `+14235550001`. |
| Message | The message vocalized when the recipient answers the call. |

## Output

The output for this action is a datatree containing information on the object.

---
