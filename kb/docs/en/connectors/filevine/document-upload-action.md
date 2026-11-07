---
url: 'https://docs.workato.com/en/connectors/filevine/document-upload-action.md'
description: >-
  The Batch document upload action generates S3 upload URLs to upload files to
  Filevine.
---

# Filevine - Batch document upload action

The **Batch document upload** action generates S3 upload URLs to upload multiple files to Filevine.

## Input

| Input field | Description |
| --- | --- |
| Files source list | Provide a list datapill containing file entries. Each entry must include file details. |
| File name | Provide the name of the file to upload. |
| Folder ID | Optional. Enter the ID of the folder to store the file. |
| Project ID | Enter the ID of the project associated with the file. |
| Size in bits | Enter the file size in bits. |
| Size in bytes | Enter the file size in bytes. |
| Uploader ID | Optional. Enter the ID of the user uploading the file. |
| Upload URL Time to Live | Optional. Enter the time-to-live value for the generated S3 upload URLs. |

## Output

| Output field | Description |
| --- | --- |
| Upload URLs | List of S3 upload URL objects containing metadata for each file. |

---

---
url: >-
  https://docs.workato.com/en/connectors/filevine/document-confirmation-action.md
description: >-
  The Batch document upload confirmation action finalizes pending uploads and
  makes them available for use in Filevine.
---

# Filevine - Batch document upload confirmation action

The **Batch document upload confirmation** action finalizes uploaded documents in Filevine. Use this action after calling the **Batch document upload** action to make the files available for use.

## Input

| Input field | Description |
| --- | --- |
| Documents source list | Provide a list datapill containing the uploaded document entries. |
| Document ID | Enter the ID of each document in the list item. |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates whether the operation completed successfully. |

---
