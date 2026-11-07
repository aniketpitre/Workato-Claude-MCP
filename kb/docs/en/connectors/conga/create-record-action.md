---
url: 'https://docs.workato.com/en/connectors/conga/create-record-action.md'
description: 'The Create record action creates a new record in Conga, such as a new contact.'
---

# Conga - Create record action

The **Create record** action creates a new record in Conga, such as a new contact.

## Input

Input fields generate dynamically based on the object you select. The following are common input fields for all object types.

| Input field | Description |
| --- | --- |
| Object | Select the type of object to create. |
| Include record payload in response | Select **Yes** or **No** to specify whether to include full record details in the response. |
| Name | Enter the name of the new record to create. |

## Output

Output fields generate dynamically based on the object you select. The following are common output fields for all object types.

| Output field | Description |
| --- | --- |
| Success | A boolean response that indicates if the action was successful. |
| Status code | A code indicating the status of the action, such as `OK`, `BadRequest`, `Unauthorized`, and more. |
| Record ID | The unique ID of the created record. |
| Data | ID: The unique ID of the created record., Name: The name of the new record., Created by: The name of the user that created the new record., Created date: The date that the new record was created., Modified by: The name of the user that modified the record., Modified date: The date that the new record was modified., E tag: The E tag with a unique identifier included in the Conga response header., External ID: The external ID of the created record. |

---

---
url: >-
  https://docs.workato.com/en/connectors/conga/download-document-based-on-document-id-action.md
description: >-
  The Download document based on ID action downloads a document based on the
  Conga ID.
---

# Conga - Download document based on ID action

The **Download document based on ID** action downloads a document based on the Conga ID.

## Input

| Input field | Description |
| --- | --- |
| Document ID | The ID of the document to download. |

## Output

| Output field | Description |
| --- | --- |
| Document | The path of the downloaded document. |

---

---
url: >-
  https://docs.workato.com/en/connectors/conga/generate-a-document-record-action.md
description: Generate a document record
---

# Conga - Generate a document record action

The **Generate a document record** action generates a document record in Conga.

## Input

| Input field | Description |
| --- | --- |
| Contract ID | Enter the ID of the contract to generate a document for. |
| Template ID | Enter the ID of the template to use to generate the document. |

## Output

| Output field | Description |
| --- | --- |
| Document version ID | The ID of the document version. |
| Status | A boolean response indicating if the request was successful. |
| Message | An error message. |
| Document ID | The ID of the generated document. |
| Document parent ID | The ID of the parent document associated with the newly generated document. |
| Document | The newly generated document as a Blob (byte array). |
| Document extension | The extension of the document, such as `PDF` or `DOCX`. |

---
