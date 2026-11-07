---
url: 'https://docs.workato.com/en/connectors/veeva-vault/upload-document-action.md'
description: >-
  The Upload document action creates a single document record in Veeva Vault by
  uploading its source file.
---

# Veeva Vault - Upload document action

The **Upload document** action creates a single document record by uploading its source file in Veeva Vault. Refer to the [Veeva Vault](https://developer.veevavault.com/api/26.1/#create-documents) documentation for more information.

## Input

| Input field | Description |
| --- | --- |
| Document name | Enter the display name of the document. |
| Document type | Enter the API name of the document type. For example `promotional_piece__c`. |
| Document subtype | Enter the API name of the subtype, if required by the type. |
| Document classification | Enter the API name of the classification, if required. |
| Lifecycle | Enter the API name of the document lifecycle. For example `promotional_piece__c`. |
| Major version | Enter the major version number. |
| Minor version | Enter the minor version number. |
| External ID | Enter a unique external identifier for the document. |
| Description | Optional. Enter a free-text description shown on the Vault document record. |
| File content | Enter the binary content of the file, base64-encoded. |
| File name | Enter the name of the file, including extension. For example `brochure.pdf`. |
| Content type | Enter the MIME type of the file. Defaults to `application/octet-stream`. |

## Output

| Output field | Description |
| --- | --- |
| Response status | The status of the upload operation. |
| Response message | A message describing the result of the upload operation. |
| Document ID | The ID of the created document. |
| Major version | The major version number of the created document. |
| Minor version | The minor version number of the created document. |
| External ID | The external ID of the created document. |

---
