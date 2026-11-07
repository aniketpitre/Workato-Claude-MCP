---
url: 'https://docs.workato.com/en/connectors/box/action-rename-file.md'
description: >-
  The Rename/move file or folder action renames a file, moves a file or folder
  to another folder, or both in Box.
---

# Box - Rename/move file or folder action

The **Rename/move file or folder** action lets you rename a file, move a file or folder to another folder, or perform both operations in Box.

## Input

| Input field | Description |
| --- | --- |
| Type | Specify whether the target is a **File** or **Folder**. Default is **File**. |
| File or folder ID | Enter the ID of the file or folder you plan to rename or move. You can find the ID in the output of other Box actions or in the Box file/folder URL. |
| New file/folder name | Provide a new name for the file or folder, including its extension for files. If not provided, the original name is retained. |
| Destination folder | Choose the folder where you want to move the file or folder. If not specified, the item remains in its current folder. |

## Output

| Output field | Description |
| --- | --- |
| Description | Description of the file or folder. |
| Size | Size of the file. |
| Shared link | Shared link details. |
| Created at | Timestamp when the file or folder was created. |
| Modified at | Timestamp when the file or folder was last modified. |
| Trashed at | Timestamp when the file or folder was moved to trash. |
| Purged at | Timestamp when the file or folder was permanently deleted. |
| Content created at | Timestamp when the file content was created. |
| Content modified at | Timestamp when the file content was last modified. |
| Sequence ID | Position of the file or folder in the hierarchy. |
| Etag | Entity tag identifying the file or folder version. |
| Sha 1 | SHA-1 hash of the file. |
| Parent | Details of the parent folder. |
| Path | Path to the file or folder. |
| Path collection | Details of all folder paths containing the file or folder. |
| Created by | User who created the file or folder. |
| Modified by | User who last modified the file or folder. |
| Owned by | User who owns the file or folder. |
| Item status | Status of the file or folder. |

---
