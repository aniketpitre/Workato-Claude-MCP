---
url: >-
  https://docs.workato.com/en/connectors/veeva-vault/download-document-rendition-action.md
description: >-
  The Download document rendition action downloads a document's viewable
  rendition as a PDF file in Veeva Vault.
---

# Veeva Vault - Download document rendition action

The **Download document rendition** action downloads a document's viewable rendition as a PDF file in Veeva Vault. This action is useful for forwarding documents to SharePoint, S3, or other downstream destinations. Refer to the [Veeva Vault](https://developer.veevavault.com/api/26.1/#download-document-version-rendition-file) documentation for more information.

## Input

| Input field | Description |
| --- | --- |
| Document ID | Enter the Vault document ID. Map from the **ID** field of a search or trigger. |
| Major version | Enter the major version of the document you plan to download. Leave blank for the latest version. |
| Minor version | Enter the minor version of the document you plan to download. Leave blank for the latest version. |
| File name | Optional. Enter a file name for the downloaded PDF. Defaults to `document_{id}.pdf`. |

## Output

| Output field | Description |
| --- | --- |
| File name | The name of the downloaded file. |
| File content | Base64-encoded PDF content. Pass to a downstream file-upload action. |
| Document ID | The ID of the document. |
| Major version | The major version number downloaded. |
| Minor version | The minor version number downloaded. |
