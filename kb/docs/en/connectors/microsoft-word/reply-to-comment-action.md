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
