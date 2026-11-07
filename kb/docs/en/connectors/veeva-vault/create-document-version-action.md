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
