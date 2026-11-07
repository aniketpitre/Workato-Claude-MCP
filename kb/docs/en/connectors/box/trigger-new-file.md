---
url: 'https://docs.workato.com/en/connectors/box/trigger-new-file.md'
description: >-
  “The New/updated file trigger starts a recipe when a file is added or updated
  in a specified Box folder.”
---

# Box - New/updated file in folder trigger

The **New/updated file in folder** trigger starts a recipe when a new file is added or when an existing file is updated, deleted, restored, moved, or copied in a specified Box folder. The trigger detects file changes from the time the recipe starts.

## Input

| Input field | Description |
| --- | --- |
| Folder | Select the folder to monitor. You can select from the drop-down menu or enter a folder ID. |
| File changes to look for | Select which types of file events to detect, such as created, uploaded, updated, deleted, restored, moved, or copied. By default, the trigger detects File created and File uploaded. |
| Include sub-folders | Select **Yes** to detect file events in sub-folders within the chosen folder. |

## Output

| Output field | Description |
| --- | --- |
| Event type | Type of file event. For example, `File updated`. |
| ID | Unique ID of the file. |
| Name | File name. |
| Type | Object type, which in this case is `file`. |
| Description | File description. |
| Size | File size in bytes. |
| Shared link | Shared link details for the file. |
| Created at | Date and time the file was created. |
| Modified at | Date and time the file was last modified. |
| Trashed at | Date and time the file was moved to trash. |
| Purged at | Date and time the file was permanently deleted. |
| Content created at | Date and time the file content was created. |
| Content modified at | Date and time the file content was modified. |
| Sequence ID | Position of this file in the folder hierarchy. |
| Etag | Entity tag of the file. |
| Sha 1 | SHA-1 hash of the file. |
| Parent | Details about the file’s parent folder. |
| Path | File path. |
| Path collection | Collection of paths the file belongs to. |
| Created by | User who created the file. |
| Modified by | User who last modified the file. |
| Owned by | User who owns the file. |
| Item status | Current status of the file. For example, `active`. |
| File version | Version details of the file. |

---
