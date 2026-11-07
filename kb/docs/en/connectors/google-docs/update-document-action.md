---
url: 'https://docs.workato.com/en/connectors/google-docs/update-document-action.md'
description: This action enables you to update the selected Google document.
---

# Google Docs - Update document action

The **Update document** action updates the specified Google document.

## Input

| Input field | Description |
| --- | --- |
| Document ID | Specify the ID of the document you plan to update. |
| Requests source list | Input a list datapill. |
| Replace with | Specify the text to be replaced with. |
| Find text | Specify the text to search in the document. |
| Match case | Select the appropriate value from the drop-down menu. |

## Output

| Output field | Description |
| --- | --- |
| Document ID | A unique identifier for the Google Docs document. |
| Replies | Responses to comments or suggested edits within the document. |
| Replace all text | A function that allows replacing all occurrences of a specific text string within the document. |
| Occurrences changed | The number of times a specific text replacement occurred, such as 3 replacements made. |
| Write control | Mechanism to prevent conflicts when multiple users are editing; ensures only authorized changes are made. |
| Required revision ID | A specific document version identifier is needed to make changes, ensuring edits apply to the correct version. |
| Doc URL | The direct link to the Google Docs document, allowing access for viewing or editing. |

---
