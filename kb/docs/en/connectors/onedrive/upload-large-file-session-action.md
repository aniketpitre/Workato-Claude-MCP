---
url: >-
  https://docs.workato.com/en/connectors/onedrive/upload-large-file-session-action.md
description: >-
  The Upload large file using session action in the OneDrive connector uploads
  large files to Microsoft OneDrive in chunks using a file session.
---

# OneDrive - Upload large file using session action (file)

The **Upload large file using session** action uploads a large file to Microsoft OneDrive using a file session. There is no fixed file size limit. The maximum size depends on whether the upload completes within the job timeout limit.

## Input

| Input fields | Description |
| --- | --- |
| Folder | Select the folder where you plan to upload files. Enter the file path where you plan to add the new file. For example, `folder-one/folder-two`. |
| File name | Provide the file name with its extension, such as `New-csv-file.csv`. If a file with the same name exists, the action overwrites it. |
| File size | Enter the size of the file in bytes. |
| File contents in text or binary format | Provide the content of the file in text or binary format. |
| Chunk size | Configure the chunk size to optimize throughput. A larger chunk size increases throughput but risks hitting API quotas. The value entered is multiplied by `320` KB. The default is `5` (`1600` KB). |

## Output

| Output fields | Description |
| --- | --- |
| ID | The unique identifier of the uploaded file. |
| Name | The name of the uploaded file. |
| File size | The size of the uploaded file in bytes. |
| Web URL | The URL to view the file or folder in a web browser. |
| Download URL | The URL to download the file. |
| Kind | Indicates whether the item is a file or folder. |
| Created by | Information about the user who created the file or folder. |
| Created date time | The date and time when the file or folder was created. |
| Last modified by | Information about the user who last modified the file or folder. |
| Last modified date time | The date and time when the file or folder was last modified. |
| ETag | The ETag (entity tag) is a unique identifier assigned to a version of a file or resource in OneDrive. It serves as a way for the system to track whether the content of the file has changed. |
| CTag | The CTag (change tag) is a timestamp or identifier used to track changes in a folder in OneDrive. It is often used for synchronization of folder contents, rather than individual files. |
