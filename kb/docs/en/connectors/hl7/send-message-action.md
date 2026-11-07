---
url: 'https://docs.workato.com/en/connectors/hl7/send-message-action.md'
description: >-
  The Send message action in the HL7 connector lets you send an HL7 message
  using the model version and message type you specify.
---

# HL7 - Send message action

The **Send message** action sends an HL7 message using the model version and message type you specify.

## Input

![Send message action input fields](/assets/hl7-send-message-action.6-e4pJ3M.png)_Input fields to send message to HL7 server_

| Input field | Description |
| --- | --- |
| Model version | Select the HL7 message model version you plan to use. |
| Message type | Select the HL7 message type to generate message input fields for. The options available vary based on the selected **Model version**. |
| HL7 message | Enter the contents of the HL7 message. The fields in this section vary based on the selected **Model version** and **Message type**. |
| Custom message schema | Add custom segments and fields to the message schema. Provide custom segments and fields that aren't already present in the HL7 schema as the custom schema will be merged with the HL7 schema. |

## Output

This action doesn't produce any output fields.

---
