---
url: 'https://docs.workato.com/en/connectors/jira/get-issue-comments-batch-action.md'
description: This action retrieves the comments belonging to an existing issue in batches.
---

# Jira - Get issue comments action (batch)

The **Get issue comments (batch)** action retrieves the comments belonging to an existing issue in batches.

## Input

| Input field | Description |
| --- | --- |
| Issue ID or key | Enter the ID or key of the issue to retrieve comments from. |

## Output

| Output field | Description |
| --- | --- |
| Self | The API URL of the issue. |
| ID | The numeric Jira identifier for the comment. |
| Author | Contains information about the original author, including `Name` and `Account ID`. |
| Body | The content of the comment. |
| Update author | Contains information about the author of the latest update, including `Name` and `Account ID`. |
| Created | The date and time the comment was created. |
| Updated | The date and time the comment was last updated. |
| Visibility | Contains visibility settings for the comment, including `Type` and `Value`. |
| List size | The total number of comments retrieved from the issue. |
| List index | The position of the current comment in the results list. |

---
