---
url: >-
  https://docs.workato.com/en/connectors/tradacoms-edi/generate-tradacoms-document-action.md
description: >-
  Build a TRADACOMS document from structured messages, segments, and components,
  with message numbers and counts calculated automatically.
---

# TRADACOMS EDI - Generate TRADACOMS document (generic) action

The **Generate TRADACOMS document (generic)** action generates a TRADACOMS document from structured messages in TRADACOMS EDI. The action automatically calculates message numbers, MTR segment counts, and the END count.

> **THE ACTION ESCAPES SPECIAL CHARACTERS FOR YOU**
> 
> The action automatically escapes the TRADACOMS special characters `=`, `+`, `:`, `'`, and `?` in component values with `?` as the release character. Enter each value exactly as it appears in your data. To split a value across components, put each part in its own component instead of entering a colon in a single component value.

## Input

| Input field | Description |
| --- | --- |
| Sender code | Enter the sender's location code (STX FROM), such as an EAN/GLN. For example, `5000000000001`. |
| Recipient code | Enter the recipient's location code (STX UNTO), such as an EAN/GLN. For example, `5000000000002`. |
| Sender reference | Enter a unique transmission reference (STX SNRF). |
| Messages | Enter one or more messages. Don't include MHD or MTR segments. |
| Type (Messages) | Enter the message type, for example `ORDERS` or `INVOIC`. |
| Version (Messages) | Optional. Enter the message version. Defaults to `9` if left blank. |
| Segments (Messages) | Enter the segments that make up the message. |
| Name (Segments) | Enter the segment tag, for example `OLD`. |
| Elements (Segments) | Optional. Enter the segment's fields. The output document separates fields with `+`. |
| Components (Elements) | Optional. Enter the parts of one field. The output document separates parts with a colon. |
| Value (Components) | Enter the component's value. |
| Segment separator | Optional. Select the layout between segments in the output document. Options are **Newline** or **None**. Defaults to **Newline** if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Document | The generated TRADACOMS document. |
| Segment count | The total number of segments in the document. |
| Message count | The total number of messages in the document. |
