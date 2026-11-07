---
url: 'https://docs.workato.com/en/connectors/smb/list-action.md'
description: >-
  The List folder action in the SMB connector lets you list all files and
  subfolders in a specified folder of your share. Subfolder items are excluded.
---

# SMB - List folder action

This action lists all files and subfolders from a specified folder in your SMB share. Items in subfolders are not retrieved.

## Input

| Input field | Description |
| --- | --- |
| Folder path | Provide the full path of the folder to retrieve the content of, for example: `/folder1/folder2` |

## Output

The output of this action is a list of records, each record containing the following details:

| Output field | Description |
| --- | --- |
| Path | The full path of the resource, including the file name and extension, for example: `/folder1/folder2/filename.csv`. |
| Size | The size of the resource. |
| Kind | Indicates whether this item is a file or folder. |
| Attributes | Attributes of the resource. |
| Create time | The time the resource was created. |
| Change time | The time the resource was last changed. |
| Access time | The time the resource was accessed. |

---
