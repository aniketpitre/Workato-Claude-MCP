---
url: >-
  https://docs.workato.com/en/connectors/docusign/action-list-documents-in-envelope.md
description: >-
  The List documents in envelope (batch) action in the Docusign connector lets
  you retrieve a list of all documents contained within a given envelope.
---

# Docusign - List documents in envelope (batch) action

The **List documents in envelope (batch)** action provides a list of documents contained within the envelope in Docusign.

## Input

| Input field | Description |
| --- | --- |
| Envelope ID | Enter the GUID value that identifies a Docusign [envelope](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/). Docusign automatically generates this value when the envelope is created. |

## Output

| Output field | Description |
| --- | --- |
| Envelope ID | The ID assigned to the envelope for tracking and managing the document lifecycle. |
| Envelope documents | The documents contained in the envelope. |
| Document ID (Envelope documents) | The ID of the envelope container for the document. |
| Name (Envelope documents) | The name of the document. |
| Type (Envelope documents) | The type of document. |
| URI (Envelope documents) | The URI of the document. |
| Order (Envelope documents) | The order of the document. |
| Pages (Envelope documents) | The number of pages in the document. |
| Attachment tab ID (Envelope documents) | The ID of the attachment tab. |
| Contains pdf form fields (Envelope documents) | Indicates whether the document contains PDF form fields. |
| Available document types (Envelope documents) | The type of document and whether it is the default. |
| Document fields (Envelope documents) | The document's fields, including name, value, and error details (code and message). |
