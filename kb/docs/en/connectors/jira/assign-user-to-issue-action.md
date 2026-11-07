---
url: 'https://docs.workato.com/en/connectors/jira/assign-user-to-issue-action.md'
description: This action assigns an issue to a Jira user.
---

# Jira - Assign user to issue action

The **Assign user to issue** action assigns an issue to a Jira user. This action replaces existing assignees.

> **ACCOUNT ID REQUIRED**
> 
> Atlassian has deprecated the use of usernames and user keys in the Jira Cloud API. Use the account ID of the user instead of the username when you assign issues. Refer to the Atlassian [user privacy API migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for more details.

## Input

| Input field | Description |
| --- | --- |
| Issue ID or key | Enter the ID or key of the issue. |
| Assignee username | Use the drop-down menu to select **Enter assignee account ID**, then enter the Atlassian account ID of the user to assign the issue to. The default **Assignee username** field is deprecated. |

## Output

There is no output for this action.

---
