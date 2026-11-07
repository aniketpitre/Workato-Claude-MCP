---
url: 'https://docs.workato.com/en/connectors/onedrive/list-files-folder-action.md'
description: >-
  The List files and folders batch action in the OneDrive connector lists files
  and folders in a selected parent folder in Microsoft OneDrive.
---

# OneDrive - List files and folders action (batch)

The **List files and folders** batch action lists files and folders in the selected parent folder in Microsoft OneDrive. Items in subfolders aren't listed. To list files and folders from a shared folder, enter the folder's ID in the **Drive ID** field.

## Input

| Input fields | Description |
| --- | --- |
| Drive ID | Provide the drive ID from which you plan to download the file. The **Drive ID** appears in the CID parameter of the OneDrive URL. For example, in `https://onedrive.live.com/?id=244DDFC44A57%21103&cid=24C9A8FC44A57` `24C9A8FC44A57` is the drive ID. |
| Folder path | Provide the path of the folder to list files and folders from. For example, `folder-one/folder-two`. If empty, OneDrive lists items in the root folder. |
| List files or folders? | Select whether to list files, folders or both. |

## Output

| Output fields | Description |
| --- | --- |
| ID | The unique identifier of the created folder. |
| Name | The name of the created folder. |
| Size | The size of the file or folder in bytes. |
| Web URL | The URL to view the file or folder in a web browser. |
| Created by | Information about the user who created the file or folder. |
| Created at | The date and time when the file or folder was created. |
| Last modified by | Information about the user who last modified the file or folder. |
| Last modified at | The date and time when the file or folder was last modified. |
| ETag | The ETag (entity tag) is a unique identifier that tracks changes to a specific version of a file or folder in OneDrive. |
| CTag | The CTag (change tag) is a timestamp or identifier that tracks changes in a folder for synchronization purposes in OneDrive. |
| Parent reference | Refers to the location or container of the file or folder within the OneDrive hierarchy. |
| File system info | Provides metadata about the file or folder, including its creation and last modified timestamps. |
| Folder | Information about the folder, including the child file count. |
| Reactions | Lists user interactions with shared documents or files, including comment count, like count, and reaction types. |
| File | Represents file details, including MIME type, Quick XOR hash, SHA-1 hash, and SHA-256 hash. |
| Shared | Indicates whether the file or folder is shared. Includes permission scope and the owner’s ID and display name. |

---
