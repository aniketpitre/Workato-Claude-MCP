---
url: >-
  https://docs.workato.com/en/connectors/microsoft-word/get-document-info-action.md
description: >-
  The Get document info action retrieves metadata and properties of a Word
  document without returning its content.
---

# Microsoft Word - Get document info action

The **Get document info** action retrieves metadata and properties of a Word document, including file size, dates, and parent folder information, without returning its content.

## Input

| Input field | Description |
| --- | --- |
| File source | Select where the document is stored. Options are **OneDrive** and **SharePoint**. |
| Document | Select the Word document from a folder-tree list scoped to the file source you selected. |

## Output

The following are a representative set of output fields. Refer to the Microsoft Graph [driveItem](https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Download URL | A pre-authenticated URL you can use to download the document. |
| Created by | The application and user that created the document. |
| Created date | The date and time the document was created. |
| ETag | The ID representing the current version of the document metadata. Use this value for revision safety when updating the document. |
| Document ID | The document's unique identifier. |
| Last modified by | The application and user that last modified the document. |
| Last modified date | The date and time the document was last modified. |
| File name | The document file name, including its extension. |
| Parent reference | Details about the document's parent folder, including drive type, drive ID, folder name, and path. |
| File | File-level details, including the file extension and a hash value used to verify content integrity. |
