---
url: 'https://docs.workato.com/en/connectors/onedrive/create-folder-action.md'
description: >-
  The Create folder action in the OneDrive connector creates a new folder under
  a specified parent path in Microsoft OneDrive.
---

# OneDrive - Create folder action

The **Create folder** action creates a new folder in Microsoft OneDrive with a specified parent path. If a folder with the same name exists, OneDrive creates a new folder with a unique name.

## Input

| Input fields | Description |
| --- | --- |
| Folder name | Specify the name of the folder to create. |
| Folder path | Provide the folder path in which the new folder has to be created. For example, `folder-one/folder-two`. If left empty, the folder is created in the root folder. |

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
| ETag | The ETag (entity tag) is a unique identifier that tracks changes to a specific version of the file or folder in OneDrive. |
| CTag | The CTag (change tag) is a timestamp or identifier that tracks changes in the folder, used for synchronization of folder contents in OneDrive. |
| Parent reference | Refers to the parent container or folder holding the file or folder in the hierarchy in OneDrive. |
| File system info | Provides metadata about the file or folder’s system properties, including creation and last modified timestamps. |
| Folder | Information about the folder, including the child file count. |

---
