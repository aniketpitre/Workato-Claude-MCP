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
