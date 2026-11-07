---
url: 'https://docs.workato.com/en/connectors/box/action-upload-file-contents.md'
description: >-
  The Upload file action uploads a new file to Box or updates an existing file
  using file contents.
---

# Box - Upload file using file contents action

The **Upload file using file contents** action uploads a file to Box by providing the contents of the file. You must input the file ID to update an existing file, or input the filename to upload a new file.

## Input

| Input field | Description |
| --- | --- |
| File contents | Provide the file contents. You can use file contents from Box's **Download file** action or from another app. |
| File size | Enter the file size if it's larger than 20 MB. Use the output of another action/trigger or specify the size in bytes. |
| Destination folder | Enter the folder where you plan to upload the new file. Leave blank if you plan to upload a new version of an existing file. |
| File name | Enter the name of the file if uploading a new file. File name must include the extension, such as `my_report.csv`. Leave blank if you plan to upload a new version of an existing file. |
| File ID | Enter the ID of the file if uploading a new version of an existing file. Leave blank if you plan to upload a new file. The file ID appears in the output of other Box actions or at the end of the file's Box URL. |

## Output

| Output field | Description |
| --- | --- |
| File version | Details of the current version of the file. |
| ID | ID of the file. |
| Name | Name of the file. |
| Type | Type of object, such as `file`. |
| Description | Description of the file. |
| Size | Size of the file. |
| Shared link | Shared link details for the file. |
| Created at | Timestamp when the file was created. |
| Modified at | Timestamp when the file was last modified. |
| Trashed at | Timestamp when the file was moved to trash. |
| Purged at | Timestamp when the file was permanently deleted. |
| Content created at | Timestamp when the file content was created. |
| Content modified at | Timestamp when the file content was last modified. |
| Sequence ID | Position of the file in the folder hierarchy. |
| Etag | Entity tag identifying the version of the file. |
| Sha 1 | SHA-1 hash value of the file. |
| Parent | Parent folder details. |
| Path | File path. |
| Path collection | Collection of all folder paths containing the file. |
| Created by | User who created the file. |
| Modified by | User who last modified the file. |
| Owned by | User who owns the file. |
| Item status | Status of the file, such as `active`. |

---
