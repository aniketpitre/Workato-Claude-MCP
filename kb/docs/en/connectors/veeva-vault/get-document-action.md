---
url: 'https://docs.workato.com/en/connectors/veeva-vault/get-document-action.md'
description: >-
  The Get document action retrieves full metadata for a single document,
  including its renditions and version history, in Veeva Vault.
---

# Veeva Vault - Get document action

The **Get document** action retrieves full metadata for a single document, including its renditions and version history, in Veeva Vault. Refer to the [Veeva Vault](https://developer.veevavault.com/api/26.1/#retrieve-document) documentation for more information.

## Input

| Input field | Description |
| --- | --- |
| Document ID | Enter the internal Vault document ID, for example `776`. |

## Output

| Output field | Description |
| --- | --- |
| Response status | The status of the request. |
| Document | An object containing the document's metadata fields. |
| Renditions | An object with **Viewable rendition** and **Imported rendition**. |
| Versions | An array of the document's versions, each with a **Version number** and **Version URL**. |
| Attachments | An array of the document's attachments. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/veeva-vault/create-document-relationship-action.md
description: >-
  The Create document relationship action links a source document version to a
  target document in Veeva Vault.
---

# Veeva Vault - Create document relationship action

The **Create document relationship** action creates a relationship on a source document version, linking it to a target document, in Veeva Vault.

## Input

| Input field | Description |
| --- | --- |
| Source document type | Select the source document type. This list is populated dynamically from your Vault. Select this first, since it determines the available **Relationship type** options. |
| Relationship type | Select the relationship type. Options depend on the **Source document type** you select. This list is populated dynamically from your Vault. Standard system types, such as **Based On**, might not be creatable through the API. |
| Source document ID | Enter the internal Vault document ID of the source document, for example `776`. |
| Source major version | Enter the major version of the source document, for example `0`. |
| Source minor version | Enter the minor version of the source document, for example `1`. |
| Target document ID | Enter the internal Vault document ID of the target document. |
| Target major version | Optional. Enter the major version of the target document. Required for target version-specific relationship types. |
| Target minor version | Optional. Enter the minor version of the target document. Required for target version-specific relationship types. |

## Output

| Output field | Description |
| --- | --- |
| Response status | The status of the relationship creation operation. |
| Response message | A message describing the result of the operation. |
| Relationship ID | The ID of the created relationship. If the relationship already exists, Vault returns `0`, which is expected and not a failure. |

---

---
url: >-
  https://docs.workato.com/en/connectors/veeva-vault/create-document-version-action.md
description: >-
  The Create document version action adds a new draft version of an existing
  document in Veeva Vault.
---

# Veeva Vault - Create document version action

The **Create document version** action adds a new draft version of an existing document in Veeva Vault. You can either copy the current source file or upload a new one as the draft.

## Input

| Input field | Description |
| --- | --- |
| Document ID | Enter the internal Vault document ID, for example `776`. |
| Create draft | Select how to create the new draft. **Copy from current version** copies the current source file without uploading. **Upload new file** uploads a new source file as the draft. |
| Version description | Optional. Enter a version description shown in Version History. Maximum 1,500 characters. |
| Suppress rendition | Optional. Select to skip automatic viewable rendition generation for the uploaded file. Only available when **Create draft** is **Upload new file**. |
| File content | Enter the binary content of the new document source file. Accepts a file or stream reference. For example, mapped from another action's output or a base64-encoded string. Required when **Create draft** is **Upload new file**. |
| Content type | Optional. Enter the MIME type of the file, for example `application/pdf`. Defaults to `application/octet-stream` if left blank. Only available when **Create draft** is **Upload new file**. |
| File name | Enter the file name, including the extension, for example `brochure.pdf`. Required when **Create draft** is **Upload new file**. |

## Output

| Output field | Description |
| --- | --- |
| Response status | The status of the version creation operation. |
| Response message | A message describing the result of the operation. |
| Major version | The major version number of the new draft. |
| Minor version | The minor version number of the new draft. |

---
