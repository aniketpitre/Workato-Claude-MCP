---
url: >-
  https://docs.workato.com/en/connectors/onedrive/upload-file-file-content-action.md
description: >-
  The Upload file using file content action in the OneDrive connector uploads a
  file up to 4MB to Microsoft OneDrive from its text or binary content.
---

# OneDrive - Upload file using file content action

The **Upload file using file content** action uploads a file to Microsoft OneDrive using its content. The maximum supported file size is 4MB.

## Input

| Input fields | Description |
| --- | --- |
| Folder | Specify the folder path where the file is uploaded. For example, `folder-one/folder-two`. |
| File name | Provide the file name with its extension, such as `New-csv-file.csv`. If a file with the same name and extension exists, the action overwrites it with the new data. |
| File contents in text or binary format | Provide the file content in text or binary format to upload. |

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
