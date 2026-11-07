---
url: 'https://docs.workato.com/en/connectors/files-dot-com/upload-file-action.md'
description: >-
  The Upload file action uploads a file to Files.com using multipart streaming
  upload.
---

# Files.com - Upload file action

The **Upload file** action uploads a file to Files.com using multipart streaming upload.

## Input

| Input field | Description |
| --- | --- |
| Path | Enter the path to the file to upload. For example: `folder/file.txt`. |
| File content | Enter the file content to upload. You can upload files up to 5TB in an automatically chunked upload. |
| Provided modified time | Select a time for when the file was modified. Leave this field empty to use the current time. |

## Output

| Output field | Description |
| --- | --- |
| Path | The path of the uploaded file. |
| Display name | The name of the uploaded file that is displayed. |
| Size | The size of the uploaded file. |
| MIME type | The MIME type of the uploaded file. For example, `application/octet-stream`. |
| MD5 | The MD5 checksum for the uploaded file. |
| SHA256 | The SHA256 checksum for the uploaded file. |
| Upload reference | The reference ID for the upload. |

---
