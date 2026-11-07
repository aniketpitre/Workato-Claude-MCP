---
url: 'https://docs.workato.com/en/connectors/hl7/parse-message-action.md'
description: >-
  The Parse message action parses a raw HL7 message string into structured data
  based on the specified model version and message type.
---

# HL7 - Parse message action

The **Parse message** action parses a raw HL7 message string into structured data based on the specified model version and message type.

## Input

| Input field | Description |
| --- | --- |
| Model version | Select the HL7 model version or enter a custom value. For example, `2.3` or `2.5.1`. An **Expected message type** field appears when you use a custom value or datapill in this field. |
| Message type | Select the HL7 message type or enter a custom value. For example, `ADT` or`ADT_A01`. An **Expected message type** field appears when you use a custom value or datapill in this field. |
| Expected message type | Select the expected message type to generate the appropriate output schema. Choose `NONE` if you're unsure or plan to use a custom schema. This field appears only when using custom values or datapills for **Model version** or **Message type**. |
| HL7 message | Enter or provide a raw HL7 message or HL7 file contents. Messages are typically separated by carriage return (`\r`) characters which delineate each segment. The action automatically converts newline (`\n`) characters to carriage returns. |
| Custom message schema | Add custom segments and fields to the message schema. Only provide custom segments and fields that aren't already present in the HL7 schema, as the custom schema will be merged with the HL7 schema. |

## Output

The output fields are dynamically generated based on the model version and message type you specify.

| Output field | Description |
| --- | --- |
| Profile name | The OPA profile name used for parsing. |
| Model version | The HL7 model version of the parsed message. |
| Message type | The HL7 message type of the parsed message. |
| Raw message | The original raw HL7 message. |
| HL7 message | The parsed HL7 message structure with all segments and fields based on the selected message type. The schema varies depending on the message type selected. |

---
