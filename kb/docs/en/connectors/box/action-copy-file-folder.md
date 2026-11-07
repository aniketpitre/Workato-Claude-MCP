---
url: 'https://docs.workato.com/en/connectors/box/action-copy-file-folder.md'
description: >-
  The Copy file or folder action copies a file or folder in Box to a target
  folder.
---

# Box - Copy file or folder action

The **Copy file or folder** action copies a file or folder to a target folder in Box.

## Input

| Input field | Description |
| --- | --- |
| Type | Choose whether to copy a `file` or `folder`. Defaults to `file`. |
| File or folder | Select the file or folder you plan to copy. |
| Destination folder | Select the target folder where the copied item is placed. |
| File name | Enter a new name for the copied file or folder. If blank, the copy keeps the original name. Include the extension, such `new_file_copy.txt`. |
| File version ID | Provide the version ID of the file to copy. Defaults to the latest version. |

## Output

| Output field | Description |
| --- | --- |
| ID | ID of the copied file or folder. |
| Name | Name of the copied file or folder. |
| Type | Object type, such as `file` or `folder`. |
| Description | Description of the copied file or folder. |
| Size | Size of the copied file. |
| Shared link | Shared link details for the copied file or folder. |
| Created at | Timestamp when the copied item was created. |
| Modified at | Timestamp when the copied item was last modified. |
| Trashed at | Timestamp when the copied item was moved to trash. |
| Purged at | Timestamp when the copied item was permanently deleted. |
| Content created at | Timestamp when the file content was created. |
| Content modified at | Timestamp when the file content was last modified. |
| Sequence ID | Position of this object in the folder hierarchy. |
| Etag | Entity tag identifying the version of the object. |
| Sha 1 | SHA-1 hash value of the file. |
| Parent | Parent folder details of the copied item. |
| Path | Path of the copied file or folder. |
| Path collection | Collection of all folder paths containing the copied item. |
| Created by | User who created the copied item. |
| Modified by | User who last modified the copied item. |
| Owned by | User who owns the copied item. |
| Item status | Status of the copied item, such as `active`. |
| File version | Version details of the copied file. |

---
