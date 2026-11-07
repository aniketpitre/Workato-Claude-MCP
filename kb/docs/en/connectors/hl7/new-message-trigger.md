---
url: 'https://docs.workato.com/en/connectors/hl7/new-message-trigger.md'
description: >-
  The New message trigger in the HL7 connector fires when a message of the
  specified model version and type is received from an HL7 server.
---

# HL7 - New message trigger (real-time)

The **New message** real-time trigger immediately creates a job when a message is received from an HL7 server. This trigger supports various model versions and message types.

Note that jobs are only created for HL7 messages with the message type and model version that you specify. You must create separate recipes if you plan to receive messages with different types or model versions.

## Input

![New message trigger input fields](/assets/hl7-new-message-trigger-input.D-n8hUNW.png)_Input fields to trigger **New message (real-time)**_

| Input field | Description |
| --- | --- |
| Model version | Select the HL7 model version. |
| Message type | Select the HL7 message type. |
| Custom message schema | Add custom segments and fields to the message schema. Only add custom segments and fields that are absent in the HL7 schema to avoid duplication when the custom schema is merged with the HL7 schema. |

## Output

The output fields are determined by the model version and message type you selected in the input. You can map relevant datapills from the datatree to use output fields in downstream steps.

![New message trigger output fields](/assets/hl7-new-message-trigger-output.7YSSzIYh.png)_Output fields_

---
