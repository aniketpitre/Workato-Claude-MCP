---
url: 'https://docs.workato.com/en/connectors/sftp/list-directory-action.md'
description: >-
  The List folder action in the SFTP connector lists all files and subfolders in
  a specified folder on your SFTP server, excluding subfolder contents.
---

# SFTP - List folder action

This action lists all items from a specified folder in your SFTP server. All files and subfolders in the specified path will be retrieved. However, items in the subfolders will not be retrieved.

![List folder action](/assets/list-directory-action.CnOaXHy5.png)_List folder action_

## Input

| Input field | Description |
| --- | --- |
| Folder path | Provide the full path of the folder to list its contents. Example: `/folder1/folder2` |

## Output

The output of this action is a **list of records** with each record containing the following details:

| Output field | Description |
| --- | --- |
| Name | The name of the file. |
| Symlink | Whether this file contain links to other files. |
| Size | The size of the file. |
| Owner | The designated owner of the file. |
| Group | The group that this file belongs to. |
| Permissions | The permissions enabled on this file. |
| Last accessed time | The last time this file was accessed. |
| Last modified time | The last time this file was modified. |
| Directory | Whether this item is a folder. |
| List size | Total number of items in the list. |
| List index | Position of each item in the list, starting at `0`. |

---
