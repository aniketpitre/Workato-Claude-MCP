---
url: 'https://docs.workato.com/en/connectors/smb/upload-file-action.md'
description: >-
  The Upload file action in the SMB connector lets you upload a file to a
  specific path in your network share, overwriting any file with the same name.
---

# SMB - Upload file action

This action uploads a file to a specific path in your SMB network share. If a file with the same name already exists in the folder, the action overwrites it.

The default chunk size is set to 5 MB. You can change the chunk size to increase the upload speed if your connection is stable. The maximum chunk size is 100 MB.

You can use this action with the [Create folder](/en/connectors/smb/create-folder) action to upload files into a new folder.

## Input

| Input field | Description |
| --- | --- |
| File path | Provide the full path of the file, including the file name and extension, for example: `/folder1/folder2/filename.csv`. The folders provided in the path must exist before you can add a file in them. |
| File name | Enter a name for the uploaded file. |
| File contents | Input a File contents datapill from another step or enter the file contents directly. Leave this field blank to create an empty file at the target location. |

## Output

| Output field | Description |
| --- | --- |
| Path | The path of the uploaded file, including the file name and extension, for example: `/folder1/folder2/filename.csv`. |
| File name | The name of the uploaded file. |
| Directory name | The complete path of the uploaded file, for example: `/folder1/folder2/`. |
| Written length | The size of the uploaded file. |

> **ADDITIONAL FILE DATA**
> 
> You can use the [Get metadata](/en/connectors/smb/metadata-action) action to retrieve more details about a file.

---
