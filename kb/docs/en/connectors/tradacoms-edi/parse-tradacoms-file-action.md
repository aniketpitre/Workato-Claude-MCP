---
url: >-
  https://docs.workato.com/en/connectors/tradacoms-edi/parse-tradacoms-file-action.md
description: >-
  Parse a TRADACOMS transmission file into typed documents with named fields for
  the selected file type.
---

# TRADACOMS EDI - Parse TRADACOMS file (typed) action

The **Parse TRADACOMS file (typed)** action parses a TRADACOMS transmission file into typed documents in TRADACOMS EDI. Select a **File type** to map message data to named fields for the header, detail, VAT, and trailer messages. The action also includes raw segments in the output.

## Input

| Input field | Description |
| --- | --- |
| File type | Select the file type, for example **Order File** or **Invoice File**. The selected file type determines which typed output fields appear. Select **Other / custom** to provide custom schemas. |
| Custom message schemas (JSON) | Optional. Enter JSON keyed by message type to add or override field mappings, for example `{"ORDERS": {"properties": {"my_field": {"path": "CLO/1", "picture": "X(40)"}}}}`. The action uses the built-in schemas for the selected file type if you leave this field blank. |
| TRADACOMS document | Enter the raw TRADACOMS EDI content, from `STX` through `END`. |

## Output

The following output fields are common to all file types. The mapped fields nested within these output fields dynamically generate based on the **File type** you select. For example, an **Order File** generates **Customer order number** and **Date order placed by customer**. Refer to the output datapills in the recipe editor to view the fields available for your selected file type.

| Output field | Description |
| --- | --- |
| Sender code | The sender's location code from the STX header. |
| Recipient code | The recipient's location code from the STX header. |
| Document count | The number of detail documents in the file. |
| Integrity | The file's integrity report. |
| Valid (Integrity) | A boolean value (`true` or `false`) that indicates whether the file passed every integrity check. |
| Head | The file header message's mapped fields and raw segments. |
| Documents | The detail messages' mapped fields and raw segments, with one entry per document. |
| Vat trailers | The VAT trailer messages' mapped fields and raw segments. |
| Summary | The file trailer message's mapped fields and raw segments. |
| Reconciliation message | The reconciliation message's raw segments, if the file includes one. |
