---
url: 'https://docs.workato.com/en/connectors/microsoft-word/reopen-comment-action.md'
description: >-
  The Reopen comment action marks a resolved comment thread as unresolved in a
  Word document.
---

# Microsoft Word - Reopen comment action

The **Reopen comment** action marks a resolved comment thread as unresolved in a Word document.

## Input

| Input field | Description |
| --- | --- |
| File source | Select where the document is stored. Options are **OneDrive** and **SharePoint**. |
| Document | Select the Word document from a folder-tree list scoped to the file source you selected. |
| Comment ID | Enter the ID of the comment thread to reopen. |

## Output

| Output field | Description |
| --- | --- |
| Comment ID | The comment's unique identifier. |
| Author | The display name of the comment's original author. |
| Content | The comment text. |
| Date | The date and time the comment was created. |
| Resolved | A boolean response (`true` or `false`) that indicates whether the comment has been resolved. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-word/reply-to-comment-action.md
description: >-
  The Reply to comment action adds a reply to an existing comment thread in a
  Word document.
---

# Microsoft Word - Reply to comment action

The **Reply to comment** action adds a reply to an existing comment thread under the authenticated user's identity. This action fails if the thread is already resolved.

## Input

| Input field | Description |
| --- | --- |
| File source | Select where the document is stored. Options are **OneDrive** and **SharePoint**. |
| Document | Select the Word document from a folder-tree list scoped to the file source you selected. |
| Comment ID | Enter the ID of the comment thread to reply to. |
| Reply text | Enter the text of the reply. |

## Output

| Output field | Description |
| --- | --- |
| Reply ID | The reply's unique identifier. |
| Author | The display name of the user the reply was created under. |
| Initials | The reply author initials. |
| Content | The reply text. |
| Date | The date and time the reply was created. |
| Parent comment ID | The ID of the comment thread the reply belongs to. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-word/resolve-comment-action.md
description: >-
  The Resolve comment action marks an existing comment thread as resolved in a
  Word document.
---

# Microsoft Word - Resolve comment action

The **Resolve comment** action marks an existing comment thread as resolved in a Word document.

## Input

| Input field | Description |
| --- | --- |
| File source | Select where the document is stored. Options are **OneDrive** and **SharePoint**. |
| Document | Select the Word document from a folder-tree list scoped to the file source you selected. |
| Comment ID | Enter the ID of the comment thread to resolve. |

## Output

| Output field | Description |
| --- | --- |
| Comment ID | The comment's unique identifier. |
| Author | The display name of the comment's original author. |
| Content | The comment text. |
| Date | The date and time the comment was created. |
| Resolved | A boolean response (`true` or `false`) that indicates whether the comment has been resolved. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-word/update-document-content-action.md
description: >-
  The Update document content action applies block-level updates or a full
  content replacement to a Word document, with revision safety enforcement.
---

# Microsoft Word - Update document content action

The **Update document content** action applies block-level operations, such as insert, replace, or delete by element ID, or replaces the full document content.

## Input

| Input field | Description |
| --- | --- |
| File source | Select where the document is stored. Options are **OneDrive** and **SharePoint**. |
| Document | Select the Word document from a folder-tree list scoped to the file source you selected. |
| Update mode | Choose how to update. **Block operations** applies targeted changes by element ID. **Full replace (XML)** and **Full replace (binary)** accept raw content. |
| Operation type | Select the type of block operation to perform. Options are **Replace**, **Delete**, **Insert before**, **Insert after**, **Insert at start**, and **Insert at end**. The **Operation type** field is only available when **Update mode** is **Block operations**. |
| Element ID | Enter the element ID of the block to target. The **Element ID** field is only available when **Update mode** is **Block operations**. |
| Content XML | Enter the raw XML content for the block. The **Content XML** field is only available when **Update mode** is **Block operations**, and it's mutually exclusive with **Block structure**. **Delete** operations don't require this field. |
| Block structure | Build content with structured fields instead of raw XML, such as block type, text, heading level, list type, or nesting level. Provide table rows for table blocks. The **Block structure** field is only available when **Update mode** is **Block operations**, and it takes precedence over **Content XML**. |
| ETag | Optional. Provide the ETag from a previous action. The update fails if the document was modified since you provided this value. |

## Output

The following are a representative set of output fields. Refer to the Microsoft Graph [driveItem](https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Document ID | The document's unique identifier. |
| ETag | The ID representing the document version after the update. |
| Last modified date | The date and time the document was last modified. |
| Last modified by | The application and user that last modified the document. |
| File name | The document file name, including its extension. |
| Created date | The date and time the document was created. |
| Download URL | A pre-authenticated URL you can use to download the document. |
| Web URL | The URL to view the document in the browser. |
| Parent reference | Details about the document's parent folder, including drive type, drive ID, folder name, and path. |
| Size (bytes) | The document size in bytes. |

---
