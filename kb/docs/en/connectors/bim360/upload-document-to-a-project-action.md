---
url: >-
  https://docs.workato.com/en/connectors/bim360/upload-document-to-a-project-action.md
description: >-
  The upload document to a project action uploads a file to a project you
  specify in BIM 360.
---

# BIM 360 - Upload document to a project action

The **Upload document to a project** action uploads a file to a project you specify in BIM 360.

> **UPLOAD LOCATION LIMITATIONS**
> 
> The **Upload document to a project** action can't upload documents to BIM 360's root `Docs` folder. It can only upload to project folders and their sub-folders.

## Input

| Input fields | Description |
| --- | --- |
| Hub name | Select the hub that contains the project where you plan to upload the document. |
| Project name | Select the project that contains the folder where you plan to upload the document. |
| Folder name | Select the folder where you plan to upload the document. |
| File name | Specify the file name and extension of the document you plan to upload. |
| Contents | Enter the contents of the file. |
| Upload threads | Specify the number of threads to use for processing the document. The default value is `10` and the maximum is `20`. |
| Item ID | Specify the BIM 360 item ID of the document. |
| File extension | Select the document's file extension type. |
| Type of version | Select the document's version type. |
| File size | Enter the file size in bytes. This is required for documents larger than 10 MB. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the document. |
| Project ID | The BIM 360 ID of the project that contains the document. |
| Folder ID | The BIM 360 ID of the folder that contains the document. |
| Item ID | The BIM 360 ID of the document. |
| Item type | The document's type. |
| Attributes | Contains information about the document's attributes, such as their `Name` an `Created at` date. |
| Links | Contains information about the document's link, such as its `Href`. |
| Relationships | Contains information about the document's relationships, such as their `Links` and `Parent`. |
