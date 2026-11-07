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
