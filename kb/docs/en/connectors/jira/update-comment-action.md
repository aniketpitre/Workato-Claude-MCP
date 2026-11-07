---
url: 'https://docs.workato.com/en/connectors/jira/update-comment-action.md'
description: This action updates a comment on an existing issue.
---

# Jira - Update comment action

The **Update comment** action updates a comment on an existing issue.

## Input

| Input field | Description |
| --- | --- |
| Issue ID or key | Enter the ID or key of the issue with the comment to update. |
| Comment ID | Enter the ID of the comment to update. |
| Comment | Enter the contents to update the comment with. Use the format `[~username]` to mention a user. |
| Role (Visibility) | Optional. Enter Jira role names to restrict the visibility of the comment to specific roles. Enter `All Users` to make the comment visible to all users. |

## Output

| Output field | Description |
| --- | --- |
| Self | The API URL of the comment. |
| ID | The numeric Jira identifier of the comment. |
| Author | Contains information about the original author, including `Name` and `Account ID`. |
| Body | The content of the comment. |
| Update author | Contains information about the author of the latest update, including `Name` and `Account ID`. |
| Created | The date and time the comment was created. |
| Updated | The date and time the comment was last updated. |
| Visibility | Contains visibility settings for the comment, including `Type` and `Value`. |

---
