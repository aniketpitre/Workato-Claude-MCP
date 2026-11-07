---
url: >-
  https://docs.workato.com/en/connectors/tradacoms-edi/parse-tradacoms-document-action.md
description: >-
  Parse any TRADACOMS document into its interchange structure of segments,
  messages, and an integrity report.
---

# TRADACOMS EDI - Parse TRADACOMS document (generic) action

The **Parse TRADACOMS document (generic)** action parses any TRADACOMS document in TRADACOMS EDI into an interchange structure that contains an STX header, MHD/MTR messages, and an END trailer. This action doesn't apply a schema. Use the **Parse TRADACOMS file (typed)** action to map named fields instead.

## Input

| Input field | Description |
| --- | --- |
| TRADACOMS document | Enter the raw TRADACOMS EDI content, from `STX` through `END`. |

## Output

The following are a representative set of output fields. Refer to the output datapills in the recipe editor to view the remaining fields.

| Output field | Description |
| --- | --- |
| Sender code | The sender's location code from the STX header. |
| Recipient code | The recipient's location code from the STX header. |
| Segment count | The total number of segments in the document. |
| Message count | The total number of messages in the document. |
| Messages | The document's parsed messages. |
| Number (Messages) | The message's position in the document, starting at `1`. |
| Type (Messages) | The message type, for example `ORDHDR` or `ORDERS`. |
| Version (Messages) | The message version, for example `9`. |
| Role (Messages) | The message's role in the document. Values are `header`, `detail`, `vat`, `trailer`, or `reconciliation`. |
| Segments (Messages) | The message's raw segments. |
| Integrity | The document's integrity report. |
| Valid (Integrity) | A boolean value (`true` or `false`) that indicates whether the document passed every integrity check. |
