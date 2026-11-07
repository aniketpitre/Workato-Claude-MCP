---
url: 'https://docs.workato.com/en/connectors/smb/create-folder.md'
description: >-
  The Create folder action in the SMB connector lets you create a new folder in
  your network location, with an option to overwrite existing ones.
---

# SMB - Create folder action

This action creates a new folder in your SMB network location. You can select whether to overwrite an existing folder.

You can use this action with the [Upload file](/en/connectors/smb/upload-file-action) action to upload files into a new folder.

## Input

| Input field | Description |
| --- | --- |
| Folder path | Provide the complete path of the folder you plan to create, for example: `/folder1/folder2/new_folder_name`. If any folders on the path do not exist, they will be created automatically. |
| Folder name | Provide a name for the new folder. |
| Require folder to not exist? | Select whether to fail the action if the folder already exists. |

## Output

| Output field | Description |
| --- | --- |
| Path | The full path of the folder, including the folder name, for example: `/folder1/folder2/newFolder`. |
| Kind | Indicates whether this item is a folder. |
| Size | The size of the created folder. |
| Attributes | Attributes attached to the created folder. |
| Name | The name of the created folder. |
| Directory | The complete path of the created folder, for example: `/folder1/folder2/`. |
| Creation time | The time the folder was created. |
| Change time | The time the folder was last changed. |
| Access time | The time the folder was accessed. |

---
