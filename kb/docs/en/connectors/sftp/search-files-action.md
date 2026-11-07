---
url: 'https://docs.workato.com/en/connectors/sftp/search-files-action.md'
description: >-
  The Search files/folders action in the SFTP connector searches for files,
  folders, or both within a given folder path on your SFTP server.
---

# SFTP - Search files/folders action

This action allows you to search for files, folders, or both within a given folder path in your SFTP server. The action will fail if the path is not found.

![Search files/folders action](/assets/search-files-action.C9YvIIsi.png)_Search files/folders action_

## Input

| Input field | Description |
| --- | --- |
| Parent folder path | Provide the path of the parent folder. All of its files and subfolders will be searched. Search does not include contents of the subfolders. Example: `/folder1/folder2` |
| Entity | Select whether to search for files, folders, or both. Default is **Files**. |
| Search term | Enter the search term. Regular expression matches are supported. For example, to search for all CSV files in the folder, use `*.csv`. |

## Output

The output of this action is a **list of records** with each record containing the following details:

| Output field | Description |
| --- | --- |
| Name | The name of the file or folder. |
| Symlink | Whether this file or folder contain links to other files. |
| Size | The size of the file or folder. |
| Owner | The designated owner of the file or folder. |
| Group | The group that this file or folder belongs to. |
| Permissions | The permissions enabled on this file or folder. |
| Last accessed time | The last time this file or folder was accessed. |
| Last modified time | The last time this file or folder was modified. |
| Folder? | Whether this item is a folder. |
| List size | Total number of items in the list. |
| List index | Position of each item in the list, starting at `0`. |

---
