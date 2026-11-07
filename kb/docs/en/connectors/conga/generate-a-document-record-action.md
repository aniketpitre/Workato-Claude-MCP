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
