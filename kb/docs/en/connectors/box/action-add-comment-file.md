---
url: 'https://docs.workato.com/en/connectors/box/action-add-comment-file.md'
description: The Add comment to file action adds a comment to a file in Box.
---

# Box - Add comment to file action

The **Add comment to file** action adds a comment to a file in Box. You can add plain text comments or tagged messages that include user mentions.

## Input

| Input field | Description |
| --- | --- |
| File ID | Enter the ID of the file you plan to comment on. |
| Message | Enter the comment text. Required if `Tagged message` isn't provided. |
| Tagged message | Enter a tagged message that includes `@mention`. Use the format `@[id:username]`. Required if `Message` isn't provided. |

## Output

| Output field | Description |
| --- | --- |
| Type | Type of object, such as `comment`. |
| ID | Unique identifier of the comment. |
| Is reply comment | Indicates if the comment is a reply to another comment. |
| Message | The text of the comment. |
| Created by | User who created the comment. |
| Created at | Timestamp when the comment was created. |
| Modified at | Timestamp when the comment was last modified. |
| Item | The file that the comment is associated with. |

---
