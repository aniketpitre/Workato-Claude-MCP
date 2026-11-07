---
url: >-
  https://docs.workato.com/en/connectors/microsoft-word/create-document-action.md
description: >-
  The Create document action creates a new Word document, optionally from a
  template, XML content, or a binary upload.
---

# Microsoft Word - Create document action

The **Create document** action creates a new Word document or copies an existing template. The action supports blank documents, XML content, binary uploads, or template-based creation.

## Input

| Input field | Description |
| --- | --- |
| File destination | Select where the document is saved. Options are **OneDrive** and **SharePoint**. |
| Creation mode | Choose to create an empty document, provide content, or copy an existing template. Options are **Blank or with content** and **From template**. Defaults to **Blank or with content**. |
| Template location | Select where the template document is stored. Options are **OneDrive** and **SharePoint**. The **Template location** field is only available when **Creation mode** is **From template**. Defaults to **OneDrive**. |
| File name | Enter a name for the new document. The **File name** field is only available when **Creation mode** is **Blank or with content**. |
| New document name | Optional. Enter a name for the copied document. The **New document name** field is only available when **Creation mode** is **From template**. Defaults to `Copy of <template file name>` if left blank. |
| Destination folder | Optional. Select the folder where the action creates the document. Defaults to the root folder if left blank. |
| Content type | Optional. Choose how you provide content. Options are **Document body XML** and **Raw binary (.docx)**. |
| Content | Optional. Enter the document content that matches the selected content type. |

## Output

The following are a representative set of output fields. Refer to the Microsoft Graph [driveItem](https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Document ID | The document's unique identifier. |
| ETag | The ID representing the current version of the document metadata. Use this value for revision safety when updating the document. |
| File name | The document file name, including its extension. |
| Created date | The date and time the document was created. |
| Created by | The application and user that created the document. |
| Last modified date | The date and time the document was last modified. |
| Download URL | A pre-authenticated URL you can use to download the document. |
| Web URL | The URL to view the document in the browser. |
| Parent reference | Details about the document's parent folder, including drive type, drive ID, folder name, and path. |
| Size (bytes) | The document size in bytes. |
