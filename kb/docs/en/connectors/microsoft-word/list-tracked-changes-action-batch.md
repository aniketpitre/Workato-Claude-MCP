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
