---
url: 'https://docs.workato.com/en/connectors/tradacoms-edi.md'
description: >-
  Parse and generate TRADACOMS EDI documents for UK retail electronic data
  interchange, with no authentication required.
---

# TRADACOMS EDI

[TRADACOMS EDI](https://en.wikipedia.org/wiki/TRADACOMS) is an electronic data interchange (EDI) standard used in UK retail for orders, invoices, credit notes, deliveries, and related transmission files. The TRADACOMS EDI connector parses and generates TRADACOMS documents.

Use the TRADACOMS EDI connector to:

- Parse a TRADACOMS document into segments, messages, and an integrity report.
- Parse a typed transmission file, such as an order or invoice, into named fields.
- Generate a TRADACOMS document from raw segments.
- Generate a typed transmission file from structured fields.
- Look up TRADACOMS code list values.

## How to connect to TRADACOMS EDI

This connector doesn't require authentication or a connection setup. It parses and generates TRADACOMS files locally. You must install this connector from the [community library](https://app.workato.com/browse/connectors) before you can use it in your workspace.

### Download the TRADACOMS EDI connector from the community library

Complete the following steps to install the TRADACOMS EDI connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_

---

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

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/tradacoms-edi/look-up-tradacoms-code-value-action.md
description: >-
  Translate a standard TRADACOMS ANA code, such as a transaction code or VAT
  category, into its meaning.
---

# TRADACOMS EDI - Look up TRADACOMS code value action

The **Look up TRADACOMS code value** action translates a standard Article Numbering Association (ANA) code, for example a transaction code, VAT category, or priority, into its meaning in TRADACOMS EDI.

## Input

| Input field | Description |
| --- | --- |
| Code list | Select the ANA code list to use, or enter an element code, for example `TCDE` or `VATC`. |
| Code | Enter the code value to look up, for example `0430` or `S`. The action keeps leading zeros on numeric codes, so enter `0430` instead of `430`. |

## Output

| Output field | Description |
| --- | --- |
| Code | The matched code. Returns the code you entered if the action finds no match. |
| Found | A boolean value (`true` or `false`) that indicates whether the action found the code in the selected code list. |
| Meaning | The code's meaning, for example `New orders`. Empty if the action finds no match. |
| List name | The selected code list's full name, for example `VAT rate category code (ANA List 12)`. |
| Entries | Every code in the selected code list. |
| Code (Entries) | The entry's code. |
| Meaning (Entries) | The entry's meaning. |

---

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

---

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

---
