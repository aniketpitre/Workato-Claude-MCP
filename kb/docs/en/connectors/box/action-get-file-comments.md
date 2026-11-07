---
url: 'https://docs.workato.com/en/connectors/box/action-get-file-comments.md'
description: >-
  The Get file comments (batch) action retrieves all comments from a file in
  Box.
---

# Box - Get file comments (batch) action

The **Get file comments** batch action retrieves all comments associated with a file in Box.

## Input

| Input field | Description |
| --- | --- |
| File ID | Enter the ID of the file to retrieve comments from. |

## Output

| Output field | Description |
| --- | --- |
| Entries | A list of all comments returned for the file. |
| Type | Type of the object, such as `comment`. |
| ID | Unique identifier of the comment. |
| Is reply comment | Indicates if the comment is a reply to another comment. |
| Message | Text of the comment. |
| Created by | User who created the comment. |
| Created at | Timestamp when the comment was created. |
| Modified at | Timestamp when the comment was last modified. |
| Item | File that the comment belongs to. |
| List size | Number of comments retrieved. |
| List index | Index of the current comment in the list. |

---
