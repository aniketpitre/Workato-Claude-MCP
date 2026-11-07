---
url: 'https://docs.workato.com/en/connectors/onedrive/new-folder-trigger.md'
description: >-
  The New folder trigger in the OneDrive connector picks up new folders created
  in a specified Microsoft OneDrive folder on each poll interval.
---

# OneDrive - New folder trigger

Configure the OneDrive connector to detect new folders created in a specified folder in your OneDrive account. The **New folder** trigger checks for new folders once every poll interval and processes each folder as a separate job.

## Input

| Input fields | Description |
| --- | --- |
| Folder | Select the folder to monitor for new folders. Subfolders aren't monitored. |
| Trigger poll interval | Determine how frequently to check for new events. Defaults to five minutes if left blank. The minimum allowed value is five minutes. |

## Output

The output datatree contains information about the new folder. This includes the folder name, size, and web URL.

| Output fields | Description |
| --- | --- |
| ID | The unique identifier of the folder. |
| Name | The name of the folder. |
| Folder size | The size of the folder in bytes. |
| Kind | Indicates whether the item is a file or folder. |
| Download URL | The URL to download the file. |
| Web URL | The URL to view the folder in a web browser. |
| Created by | Information about the user who created the folder. |
| Created date time | The date and time when the folder was created. |
| Last modified by | Information about the user who last modified the folder. |
| Last modified date time | The date and time when the folder was last modified. |
| ETag | The ETag (entity tag) is a unique identifier assigned to a version of a file or resource in OneDrive. It serves as a way for the system to track whether the content of the file has changed. |
| CTag | The CTag (change tag) is a timestamp or identifier used to track changes in a folder in OneDrive. It is often used for synchronization of folder contents, rather than individual files. |

---
