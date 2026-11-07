---
url: >-
  https://docs.workato.com/en/connectors/tradacoms-edi/generate-tradacoms-file-action.md
description: >-
  Generate a TRADACOMS transmission file from typed header, detail, VAT, and
  trailer fields for a selected file type.
---

# TRADACOMS EDI - Generate TRADACOMS file (typed) action

The **Generate TRADACOMS file (typed)** action generates a TRADACOMS transmission file from named fields in TRADACOMS EDI. Select a **File type** to display named fields for the header, detail, VAT, and trailer messages. The action automatically generates the envelope, assigns message numbers, and calculates all counts.

## Input

Input fields dynamically generate based on the **File type** you select. Refer to the recipe editor to view the fields available for your selected file type.

| Input field | Description |
| --- | --- |
| File type | Select the file type, for example **Order File** or **Invoice File**. The selected file type determines which typed input fields appear. Select **Other / custom** to provide custom schemas or use raw segments for message types without a schema. |
| Custom message schemas (JSON) | Optional. Enter JSON keyed by message type to add or override field mappings, for example `{"ORDERS": {"properties": {"my_field": {"path": "CLO/1", "picture": "X(40)"}}}}`. The action uses the built-in schemas for the selected file type if you leave this field blank. |
| Sender code | Enter the sender's location code (STX FROM), such as an EAN/GLN. For example, `5000000000001`. |
| Recipient code | Enter the recipient's location code (STX UNTO), such as an EAN/GLN. For example, `5000000000002`. |
| Sender reference | Enter a unique transmission reference (STX SNRF). |
| File header message | Enter the header message's fields. |
| Detail messages | Enter one entry per document, for example an order, invoice, or bill. |
| VAT trailer messages | Optional. Enter VAT trailer details. The **VAT trailer messages** field is only available for file types that include a VAT trailer message, for example **Invoice File**. The action omits the VAT trailer message from the file if you leave this field blank. |
| File trailer message | Optional. Enter the trailer message's fields. The action omits the trailer message from the file if you leave this field blank. |
| Segment separator | Optional. Select the layout between segments in the output document. Options are **Newline** or **None**. Defaults to **Newline** if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Document | The generated TRADACOMS file. |
| Segment count | The total number of segments in the file. |
| Message count | The total number of messages in the file. |
