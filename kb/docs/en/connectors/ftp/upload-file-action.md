---
url: 'https://docs.workato.com/en/connectors/ftp/upload-file-action.md'
description: This action uploads a file to a folder you specify in the connected server.
---

# FTP/FTPS - Upload file action

The **Upload file** action uploads a file to a folder you specify in the connected server. This action appends or overwrites existing files with the same name and location.

## Input

| Input field | Description |
| --- | --- |
| File name | Enter the full destination path including the file extension. For example, `/directory1/file1.txt`. This field is case-sensitive. |
| Append | Select whether to append content to existing files with the same name and location. Leave this field blank to overwrite existing files. |
| File contents | Provide the content of the file to upload. You can input text directly to create a plain text file, or map file contents from an upstream action or trigger. |

## Output

| Output field | Description |
| --- | --- |
| Uploaded bytes | The size of the uploaded file in bytes. |

---
