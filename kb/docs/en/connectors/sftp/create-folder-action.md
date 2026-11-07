---
url: 'https://docs.workato.com/en/connectors/sftp/create-folder-action.md'
description: >-
  The Create folder action in the SFTP connector creates a new folder on your
  SFTP server, failing if a folder already exists at the given path.
---

# SFTP - Create folder action

This action creates a new folder in your SFTP server. The action will fail if a folder already exists in the given path.

You can use this action with the [Upload file](/en/connectors/sftp/upload-file-action) action to upload files into a new folder.

![Create folder action](/assets/create-folder-action.CKM4rZ9A.png)_Create folder action_

## Input

| Input field | Description |
| --- | --- |
| Folder path | Provide the complete path of the folder you plan to create. Example: `/folder1/folder2/new_folder_name` |

## Output

| Output field | Description |
| --- | --- |
| Folder name | Name of the created folder. |
| Folder path | Complete path of the created folder. |

To retrieve more details about the folder you've just created, use the [List directory](/en/connectors/sftp/list-directory-action) action.

---
