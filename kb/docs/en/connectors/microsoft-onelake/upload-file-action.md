---
url: 'https://docs.workato.com/en/connectors/microsoft-onelake/upload-file-action.md'
description: The Upload file action uploads a new file to Microsoft OneLake storage.
---

# Microsoft OneLake - Upload file action

The **Upload file** action enables you to upload a new file to Microsoft OneLake storage.

There is no fixed limit on file size. The maximum file size depends on whether the upload can finish within the [job timeout limit](/en/recipes/jobs#timeouts).

## Input

| Input field | Description |
| --- | --- |
| Workspace ID | Enter the ID of the workspace where the lakehouse is located. |
| Lakehouse ID | Enter the ID of the lakehouse where the file is located. |
| Directory path | Specify the path of the directory where the file should be created. |
| File name | Enter the name of the file. |
| Contents | Enter the binary contents of the file to be uploaded. |

## Output

| Output field | Description |
| --- | --- |
| Success | Status of the upload file operation. |
| Name | Name of the file with its extension. |
| Parts uploaded | Number of parts uploaded to complete the multipart file upload. |
| Total bytes uploaded | Size of the uploaded files in bytes. |

---
