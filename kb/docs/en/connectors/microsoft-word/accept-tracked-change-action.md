---
url: >-
  https://docs.workato.com/en/connectors/microsoft-word/accept-tracked-change-action.md
description: >-
  The Accept tracked change action accepts a specific tracked change in a Word
  document by its ID.
---

# Microsoft Word - Accept tracked change action

The **Accept tracked change** action accepts a specific tracked change by its ID. The action makes inserted text permanent and removes deleted text.

## Input

| Input field | Description |
| --- | --- |
| File source | Select where the document is stored. Options are **OneDrive** and **SharePoint**. |
| Document | Select the Word document from a folder-tree list scoped to the file source you selected. |
| Change ID | Enter the ID of the tracked change to accept. |

## Output

The following are a representative set of output fields. Refer to the Microsoft Graph [driveItem](https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Action taken | The operation performed, such as `accepted_insertion` or `accepted_deletion`. |
| Document ID | The document's unique identifier. |
| ETag | The ID representing the document version after the tracked change was accepted. |
| Last modified date | The date and time the document was last modified. |
| Last modified by | The application and user that last modified the document. |
| File name | The document file name, including its extension. |
| Download URL | A pre-authenticated URL you can use to download the document. |
| Web URL | The URL to view the document in the browser. |
| Parent reference | Details about the document's parent folder, including drive type, drive ID, folder name, and path. |
| Size (bytes) | The document size in bytes. |
