---
url: >-
  https://docs.workato.com/en/connectors/google-drive/trigger-new-file-hierarchy.md
description: >-
  The New file or folder in folder hierarchy trigger in the Google Drive
  connector picks up new files or folders created in a folder and its
  subfolders.
---

# Google Drive - New file or folder in folder hierarchy trigger

This trigger checks periodically for new files or folders created in a specified folder and its subfolders. Each new file and folder generates a new job. Use this to monitor a family of folders.

This trigger is compatible with [file streaming](/en/features/file-streaming), allowing it to send large amounts of data from Google Drive to other streaming-compatible connectors in Workato.

![Google Drive New file or folder in folder hierarchy trigger](/assets/google-drive-new-file-in-hirearchy.B7QEadIN.png) _Google Drive New file or folder in folder hierarchy trigger_

## Input

| Input field | Description |
| --- | --- |
| Folder | The folder to monitor for new files or folders. Subfolders are monitored as well. Select a folder from the picklist or enter the folder ID directly. If entering the folder ID for a shared drive (formerly Team Drive), this value must be in the form `folder_id/shared_drive_id` (for example, `1fm6iCMYrN7roZZ-ynpVFRTVq9mellrWp/0AB6ZFCw3XdamUk9PAA`). IDs can be found at the end of folder and drive URLs. |
| Chunk size (KB) | Configure this to optimize throughput. Larger chunk size increases throughput, but may hit API quotas. Defaults to 1024 KB. Only applicable when the downstream application is streaming compatible. Refer to [File streaming](/en/features/file-streaming) for more information. |

## Output

Note that in Google Drive API, the terms `folder` and `file` are used interchangeably. A `folder` is technically a special `file`. As a result, whenever the field name or field description mentions `file`, it also applies to `folder`.

| Output field | Description |
| --- | --- |
| Is folder | Indicates whether this is a folder. |
| Is Google file | Indicates whether this is a Google file, such as Google Sheets, Google Docs, Google Slides, and so on. |
| Is other file | Indicates whether this is a non-Google file, such as a `CSV`, `PDF`, `DOCX`, and so on. |
| File contents | Full contents of the file. This is a [streaming object](/en/features/file-streaming). |
| ID | ID of the file. |
| Name | Name of the file or folder. |
| MIME type | MIME type of this file, as stated in [Google Drive's documentation](https://developers.google.com/drive/api/v3/mime-types). |
| Description | A short description of the file. |
| Starred | Indicates whether the user has starred the file. |
| Trashed | Indicates whether the file has been trashed, either explicitly or from a trashed parent folder. Only the owner can trash a file. Other users cannot see files in the owner's trash. |
| Explicitly trashed | Indicates whether the file has been explicitly trashed, as opposed to recursively trashed from a parent folder (for example, when you trash an entire parent folder). |
| Parents | The list of the parent folders that contain the file. Each parent folder in the list contains the following output field, in addition to **List size** and **List index**: **ID**: The ID of the parent folder containing the file. |
| Version | A version number for the file. This reflects every change made to the file on the server, even those not visible to the user. |
| Web content link | A link for downloading the content of the file in a browser. This is only available for files with binary content in Google Drive. |
| Icon link | A static, unauthenticated link to the file's icon. |
| Thumbnail link | A short-lived link to the file's thumbnail, if available. Typically lasts on the order of hours. Only populated when the requesting app can access the file's content. |
| Viewed by me | Indicates whether the file has been viewed by this user. |
| Viewed by me time | The last time the file was viewed by this user (RFC 3339 date-time). |
| Created time | The time at which the file was created (RFC 3339 date-time). |
| Modified time | The last time the file was modified by anyone (RFC 3339 date-time). |
| Modified by me time | The last time the file was modified by this user (RFC 3339 date-time). |
| Sharing user | The user who shared the file with the requesting user, if applicable. Each user contains the following output fields: **Display name**: A plain text displayable name for this user.; **Email address**: The email address of the user. This may not be present in certain contexts if the user has not made their email address visible to the requester.; **Permission ID**: The user's ID as visible in Permission resources.; **Photo link**: A link to the user's profile photo, if available.; **Me**: Whether this user is the requesting user. |
| Owners | The list of owners of the file. Only certain legacy files can have more than one owner. This field is not populated for shared drive files. Each owner contains the following fields, in addition to **List size** and **List index**: **Display name**: A plain text displayable name for this user.; **Email address**: The email address of the user. This may not be present in certain contexts if the user has not made their email address visible to the requester.; **Permission ID**: The user's ID as visible in Permission resources.; **Photo link**: A link to the user's profile photo, if available.; **Me**: Whether this user is the requesting user. |
| Last modifying user | The last user to modify the file. Each user contains the following output fields: **Display name**: A plain text displayable name for this user.; **Email address**: The email address of the user. This may not be present in certain contexts if the user has not made their email address visible to the requester.; **Permission ID**: The user's ID as visible in Permission resources.; **Photo link**: A link to the user's profile photo, if available.; **Me**: Indicates whether this user is the requesting user. |
| Shared | Indicates whether the file has been shared. This field isn't populated for shared drive files. |
| Owned by me | Indicates whether the user owns the file. This field isn't populated for shared drive files. |
| Viewers can copy content | Indicates whether users with **View** access can copy the file contents. |
| Writers can share | Indicates whether users with **Edit** access can share the file. This field isn't populated for shared drive files. |
| Original filename | The original filename of the uploaded content if available, or else the original value of the name field. This is only available for files with binary content in Google Drive. |
| Full file extension | The full file extension extracted from the name field. May contain multiple concatenated extensions (for example, `tar.gz`). This is only available for files with binary content in Google Drive. The file is automatically updated when the name field changes, but it isn't cleared if the new name doesn't contain a valid extension. |
| File extension | The final component of the full file extension (for example, `gz`). This is only available for files with binary content in Google Drive. |
| MD5 checksum | The MD5 checksum for the content of the file. This is only applicable to files with binary content in Google Drive. |
| Size | The size of the file's content in bytes. This is only applicable to files with binary content in Google Drive. |
| Quota bytes used | The number of storage quota bytes used by the file. This includes the head revision as well as previous revisions with [Keep Forever](https://developers.google.com/drive/api/guides/change-overview) enabled. |
| Head revision ID | The ID of the file's most current version. This is only available for files with binary content in Google Drive. |
