---
url: 'https://docs.workato.com/en/connectors/onedrive/new-updated-file-trigger.md'
description: >-
  The New/updated file trigger in the OneDrive connector picks up new or updated
  files in a specified Microsoft OneDrive folder on each poll interval.
---

# OneDrive - New/updated file trigger

Configure the OneDrive connector to detect new or updated files in a specified folder in your OneDrive account. The trigger checks for changes once every poll interval and processes each file as a separate job. Subfolders aren't included in this trigger.

## Input

| Input field | Description |
| --- | --- |
| Folder | Select the folder to monitor for new or updated files. Subfolders aren't monitored. |

## Output

The output datatree contains information about the new or updated file. This includes the file name, size, and download URL.

| Output fields | Description |
| --- | --- |
| File ID | The unique identifier of the file. |
| File name | The name of the file. |
| File size | The size of the file in bytes. |
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
