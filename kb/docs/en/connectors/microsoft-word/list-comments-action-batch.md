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
