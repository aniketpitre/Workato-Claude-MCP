---
url: 'https://docs.workato.com/en/connectors/microsoft-word/add-comment-action.md'
description: >-
  The Add comment action adds a comment to a Word document, optionally anchored
  to a specific block.
---

# Microsoft Word - Add comment action

The **Add comment** action adds a comment to a Word document, optionally anchored to a specific block. The action creates the comment under the authenticated user's identity.

## Input

| Input field | Description |
| --- | --- |
| File source | Select where the document is stored. Options are **OneDrive** and **SharePoint**. |
| Document | Select the Word document from a folder-tree list scoped to the file source you selected. |
| Comment text | Enter the text of the comment to add. |
| Anchor text | Optional. Anchor the comment to the paragraph that contains this text, instead of an element ID. The comment anchors to the block in **Element ID** if you leave this field blank, or to the first paragraph if you leave both blank. The **Anchor text** field is required when **Occurrence** is greater than `1`. |
| Element ID | Optional. Anchor the comment to a specific content block by its element ID. The action scopes the match to this element when you also provide **Anchor text**. |
| Occurrence | Optional. If the anchor text appears more than once in the document, specify which occurrence to anchor the comment to. Defaults to `1`. |

## Output

The following are a representative set of output fields. Refer to the output datapills in the recipe editor to view additional output.

| Output field | Description |
| --- | --- |
| Comment ID | The comment's unique identifier. |
| Author | The display name of the user the comment was created under. |
| Initials | The comment author's initials. |
| Content | The comment text. |
| Date | The date and time the comment was created. |
| Resolved | A boolean response (`true` or `false`) that indicates whether the comment is resolved. |
| Referenced text | The paragraph text the comment is anchored to. |
| Replies | The comment thread's replies. Returns one entry per reply. |
| Author (Replies) | The display name of the user the reply was created under. |
| Content (Replies) | The reply text. |
| Date (Replies) | The date and time the reply was created. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-word/download-document-action.md
description: >-
  The Download document action downloads a Word document as XML, binary (.docx),
  or PDF.
---

# Microsoft Word - Download document action

The **Download document** action downloads a Word document in XML, binary (.docx), or PDF format.

## Input

| Input field | Description |
| --- | --- |
| File source | Select where the document is stored. Options are **OneDrive** and **SharePoint**. |
| Document | Select the Word document from a folder-tree list scoped to the file source you selected. |
| Output format | Choose the format the action returns. **Document body XML** returns the WordprocessingML body content. **Raw binary** returns the full `.docx` file. **PDF** converts the document to PDF. |

## Output

| Output field | Description |
| --- | --- |
| Content | The downloaded file content, in the format specified by **Output format**. |
| Content type | The returned file MIME type, which varies based on the selected output format. |
| File name | The downloaded file name. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-word/get-document-content-action.md
description: >-
  The Get document content action returns structured content blocks from a Word
  document, with optional filtering and pagination.
---

# Microsoft Word - Get document content action

The **Get document content** action returns structured content blocks, such as headings, paragraphs, lists, and tables, from a Word document. Filter results by section heading, block type, or search text, and use **Max blocks** and **Page token** to paginate through large documents.

## Input

| Input field | Description |
| --- | --- |
| File source | Select where the document is stored. Options are **OneDrive** and **SharePoint**. |
| Document | Select the Word document from a folder-tree list scoped to the file source you selected. |
| Section heading | Optional. Filter content blocks to a specific section by its heading text. |
| Search text | Optional. Filter content blocks to those containing the specified text. |
| Block type filter | Optional. Filter content blocks by type, such as heading, paragraph, list, or table. |
| Match mode | Optional. Determine how the action matches search text or filters against content blocks. |
| Max blocks | Optional. Limit the number of content blocks returned in a single response. The response includes a **Page token** when more blocks remain. |
| Page token | Optional. Provide the page token from a previous response to retrieve the next page of content blocks. |

## Output

The following are a representative set of output fields. Refer to the output datapills in the recipe editor for additional output.

| Output field | Description |
| --- | --- |
| Content blocks | The document's structured content blocks. Returns one entry per block. |
| Element ID (Content blocks) | The block's unique identifier. Pass this value to the [Update document content](/en/connectors/microsoft-word/update-document-content-action) action to target the block. |
| Block type (Content blocks) | The block's type, such as paragraph or heading. |
| Text content (Content blocks) | The block's text. |
| Total blocks | The total number of content blocks in the document. |
| Page token | A token you can use to retrieve the next page of content blocks, if more exist. |
| Has more | A boolean response (`true` or `false`) that indicates whether additional content blocks are available beyond the current page. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-word/list-comments-action-batch.md
description: >-
  The List comments action lists comment threads in a Word document with
  filtering and pagination support.
---

# Microsoft Word - List comments action (batch)

The **List comments (batch)** action lists comment threads in a Word document. Filter results by resolution status and paginate through large result sets.

## Input

| Input field | Description |
| --- | --- |
| File source | Select where the document is stored. Options are **OneDrive** and **SharePoint**. |
| Document | Select the Word document from a folder-tree list scoped to the file source you selected. |
| Resolution filter | Optional. Filter comments by resolution status. Defaults to unresolved comments only. |
| Page size | Optional. Set the number of comments to return per page. Defaults to `20`. |
| Page | Optional. Specify the page number to retrieve. Defaults to `1`. |

## Output

The following are a representative set of output fields. Refer to the output datapills in the recipe editor to view additional output.

| Output field | Description |
| --- | --- |
| Comments | The document's comment threads. Returns one entry per thread. |
| Comment ID (Comments) | The comment's unique identifier. |
| Author (Comments) | The comment author's display name. |
| Date (Comments) | The date and time the comment was created. |
| Content (Comments) | The comment's text content. |
| Resolved (Comments) | A boolean response (`true` or `false`) that indicates whether the comment is resolved. |
| Total count | The total number of comments matching the filter. |
| Page | The current page number. |
| Next page | The next page number, if more comments exist. |
| Has more | A boolean response (`true` or `false`) that indicates whether additional comments are available beyond the current page. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-word/list-tracked-changes-action-batch.md
description: >-
  The List tracked changes action lists pending tracked changes in a Word
  document with authorship and location information.
---

# Microsoft Word - List tracked changes action (batch)

The **List tracked changes (batch)** action lists pending tracked changes in a Word document. Filter results by author and paginate through large result sets.

## Input

| Input field | Description |
| --- | --- |
| File source | Select where the document is stored. Options are **OneDrive** and **SharePoint**. |
| Document | Select the Word document from a folder-tree list scoped to the file source you selected. |
| Author filter | Optional. Filter tracked changes by the display name of the author who made them. |
| Page size | Optional. Set the number of tracked changes to return per page. Defaults to `20`. |
| Page | Optional. Specify the page number to retrieve. Defaults to `1`. |

## Output

The following are a representative set of output fields. Refer to the output datapills in the recipe editor to view additional output.

| Output field | Description |
| --- | --- |
| Tracked changes | The document's pending tracked changes. Returns one entry per change. |
| Change ID (Tracked changes) | The change's unique identifier. |
| Change type (Tracked changes) | The change's type, such as insertion or deletion. |
| Changed content (Tracked changes) | The changed text. |
| Author (Tracked changes) | The display name of the person who made the change. |
| Date (Tracked changes) | The date and time the change was made. |
| Total count | The total number of tracked changes matching the filter. |
| Page | The current page number. |
| Next page | The next page number, if more tracked changes exist. |
| Has more | A boolean response (`true` or `false`) that indicates whether additional tracked changes are available beyond the current page. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-word/reject-tracked-change-action.md
description: >-
  The Reject tracked change action rejects a specific tracked change in a Word
  document by its ID.
---

# Microsoft Word - Reject tracked change action

The **Reject tracked change** action rejects a specific tracked change by its ID. The action removes inserted text and restores deleted text.

## Input

| Input field | Description |
| --- | --- |
| File source | Select where the document is stored. Options are **OneDrive** and **SharePoint**. |
| Document | Select the Word document from a folder-tree list scoped to the file source you selected. |
| Change ID | Enter the ID of the tracked change to reject. |

## Output

The following are a representative set of output fields. Refer to the Microsoft Graph [driveItem](https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0) documentation for additional output.

| Output field | Description |
| --- | --- |
| Action taken | The operation performed, such as `rejected_insertion` or `rejected_deletion`. |
| Document ID | The document's unique identifier. |
| ETag | The ID representing the document version after the tracked change was rejected. |
| Last modified date | The date and time the document was last modified. |
| Last modified by | The application and user that last modified the document. |
| File name | The document file name, including its extension. |
| Download URL | A pre-authenticated URL you can use to download the document. |
| Web URL | The URL to view the document in the browser. |
| Parent reference | Details about the document's parent folder, including drive type, drive ID, folder name, and path. |
| Size (bytes) | The document size in bytes. |

---
