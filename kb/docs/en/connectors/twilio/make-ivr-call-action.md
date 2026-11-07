---
url: 'https://docs.workato.com/en/connectors/twilio/make-ivr-call-action.md'
description: >-
  The Make IVR phone call action in the Twilio connector lets you place an
  interactive voice call with key prompts the recipient responds to.
---

# Twilio - Make IVR phone call action

This action allows you to make an interactive voice response (IVR) phone call. For example, if a trigger event occurs, the action makes a call to a phone number that you configure, and an artificial voice speaks aloud the message you provided. You can configure key prompts to allow the person receiving the call to select options or provide a general response with the dial pad.

![Make IVR call](/assets/make-ivr-call-action.QUZFBIKJ.png)_Make IVR call action_

## Input

| Input field | Description |
| --- | --- |
| From | The Twilio phone number from which the IVR call is made. |
| To | The phone number to which the IVR call is made. The phone number must include the country code. For example, `+14235550001`. |
| Welcome message | The message vocalized when the recipient answers the call. |
| Key 1 prompt | Enter a description of what happens if the recipient presses 1. For example, `list opening hours`. |
| Key 1 response | The message vocalized when the recipient presses 1. |

## Output

The output for this action is a datatree containing information on the object.

---
