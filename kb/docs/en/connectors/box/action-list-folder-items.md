---
url: 'https://docs.workato.com/en/connectors/box/action-list-folder-items.md'
description: >-
  The List folder items batch action retrieves the files and folders contained
  within a specific folder in Box.
---

# Box - List folder items (batch) action

The **List folder items** batch action retrieves all files and folders within a specified folder in Box.

## Input

| Input field | Description |
| --- | --- |
| Folder | Select the folder from which to list files and folders. |

## Output

| Output field | Description |
| --- | --- |
| Entries | A list of files and folders retrieved from the specified folder. |
| ID | Unique identifier for the file or folder. |
| Name | Name of the file or folder. |
| Type | Type of the object, such as `file` or `folder`. |
| Sequence ID | Position of this object in the folder hierarchy. |
| Etag | Entity tag identifying the version of the file or folder. |
| List size | Total number of items in the retrieved list. |
| List index | Index of the current item within the list. |

---
