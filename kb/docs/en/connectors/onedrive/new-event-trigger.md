---
url: 'https://docs.workato.com/en/connectors/onedrive/new-event-trigger.md'
description: >-
  The New event real-time trigger in the OneDrive connector monitors created,
  updated, or deleted files and folders in a specified Microsoft OneDrive
  folder.
---

# OneDrive - New event trigger (real-time)

The **New event** real-time trigger monitors all events in the specified folder. You can choose to monitor files, folders, or both, and specify the types of activities to track. This trigger processes all events in the selected file or folder.

## Input

| Input fields | Description |
| --- | --- |
| Folder | Select the folder to monitor for new files. Subfolders aren't monitored by default. |
| Monitor subfolders | Specify whether to monitor subfolders. Select **No** to monitor only the parent folder. Select **Yes** to include subfolders for new activities. Note that deleted events are limited to the parent folder due to API constraints. |
| Monitor for files or folders | Select whether to monitor files, folders, or both. |
| Activity to monitor | Select one or more activities to monitor, such as created, updated, or deleted files and folders. |

## Output

The output fields provide detailed information about each detected event, including event type, item details, and changes made.

| Output fields | Description |
| --- | --- |
| ID | The unique identifier of the file or folder involved in the event. |
| Name | The name of the file or folder involved in the event. |
| Size | The size of the file or folder in bytes. |
| Download URL | The URL to download the file. |
| Web URL | The URL to view the file or folder in a web browser. |
| Created by | Information about the user who created the file or folder. |
| Created at | The date and time when the file or folder was created. |
| Last modified by | Information about the user who last modified the file or folder. |
| Last modified at | The date and time when the file or folder was last modified. |
| Deleted state | Indicates if the item was deleted. |
| ETag | The ETag (entity tag) is a unique identifier assigned to a version of a file or resource in OneDrive. It serves as a way for the system to track whether the content of the file has changed. |
| CTag | The CTag (change tag) is a timestamp or identifier used to track changes in a folder in OneDrive. It is often used for synchronization of folder contents, rather than individual files. |
| Parent reference | Refers to the parent folder or container holding the file or folder in the OneDrive hierarchy. |
| File system info | Provides metadata about the file or folder, including creation and modification timestamps. |
| Folder | Information about the folder, including the child file count. |
| Reactions | User interactions to shared documents or files. Includes the comment count, like count, and reaction types. |
| File | Represents the file, including MIME type, Quick XOR hash, SHA-1 hash, and SHA-256 hash details. |
| Shared | Indicates whether the file or folder is shared. Includes permission scope, owner ID, and display name. |
| Deleted | Specifies whether the resource has been deleted. |

---
