---
url: 'https://docs.workato.com/en/connectors/box/action-upload-file-url.md'
description: >-
  The Upload file using file URL action uploads a file to Box from a public URL.
  You can upload a new file to a folder or a new version of an existing file.
---

# Box - Upload file using file URL action

The **Upload file using file URL** action uploads a file to Box from a public URL. You can use this action to upload a new file into a folder or replace an existing file with a new version. This action only supports files **less than 50 MB**. Use the **Upload file using file contents** action for files larger than 50 MB.

## Input

| Input field | Description |
| --- | --- |
| Source URL | Enter the public URL where the file is located. |
| File ID | Enter the file ID if you plan to upload a new version of an existing file. |
| Destination folder | Select the folder where you plan to upload the file. Required only for new files. |
| File name | Enter a name for the uploaded file. Must include extension. If left blank, the name is taken from the source URL. |

## Output

| Output field | Description |
| --- | --- |
| File version | Details of the file version uploaded. |
| ID | Unique identifier of the file. |
| Name | Name of the uploaded file. |
| Type | Type of the object. |
| Description | Description of the file. |
| Size | Size of the uploaded file. |
| Shared link | Shared link details, if available. |
| Created at | Timestamp when the file was created. |
| Modified at | Timestamp when the file was last modified. |
| Trashed at | Timestamp when the file was moved to trash. |
| Purged at | Timestamp when the file was permanently deleted. |
| Content created at | Timestamp when the file content was created. |
| Content modified at | Timestamp when the file content was modified. |
| Sequence ID | Position of the file in the folder hierarchy. |
| Etag | Entity tag identifying the file version. |
| Sha 1 | SHA-1 hash of the file. |
| Parent | Parent folder details. |
| Path | Path to the file. |
| Path collection | Collection of all folder paths that contain the file. |
| Created by | User who created the file. |
| Modified by | User who last modified the file. |
| Owned by | User who owns the file. |
| Item status | Current status of the file. |

---
