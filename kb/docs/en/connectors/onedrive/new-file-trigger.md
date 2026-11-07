---
url: 'https://docs.workato.com/en/connectors/onedrive/new-file-trigger.md'
description: >-
  The New file trigger in the OneDrive connector picks up new files created in a
  specified Microsoft OneDrive folder on each poll interval.
---

# OneDrive - New file trigger

Configure the OneDrive connector to detect new files created in a specified folder in your OneDrive account. The **New file** trigger checks for new files once every poll interval and processes each file as a separate job.

## Input

| Input fields | Description |
| --- | --- |
| Folder | Select the folder to monitor for new files. Subfolders aren't monitored. |
| Trigger poll interval | Determine how frequently to check for new events. Defaults to five minutes if left blank. The minimum allowed value is five minutes. |

## Output

The output datatree contains information about the new file. This includes the file name, size, and download URL.

| Output fields | Description |
| --- | --- |
| ID | The unique identifier of the file. |
| Name | The name of the file. |
| Size | The size of the file in bytes. |
| File kind | Indicates whether the item is a file or folder. |
| Download URL | The URL to download the file. |
| Web URL | The URL to view the file in a web browser. |
| Created by | Information about the user who created the file. |
| Created at | The date and time when the file was created. |
| Last modified by | Information about the user who last modified the file. |
| Last modified at | The date and time when the file was last modified. |
| ETag | The ETag (entity tag) is a unique identifier assigned to a version of a file or resource in OneDrive. It serves as a way for the system to track whether the content of the file has changed. |
| CTag | The CTag (change tag) is a timestamp or identifier used to track changes in a folder in OneDrive. It is often used for synchronization of folder contents, rather than individual files. |

---
