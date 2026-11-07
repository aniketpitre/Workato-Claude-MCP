---
url: 'https://docs.workato.com/en/connectors/jsd/create-comment-action.md'
description: >-
  The Create comment action in the Jira Service Desk connector lets you add a
  public or private comment to an issue in your service desk instance.
---

# Jira Service Desk - Create comment action

This action creates a comment for an issue in your Jira Service Desk instance.

![Create comment action](/assets/create-comment-action.6raMjcCC.png)_Create comment action_

## Input

| Input field | Description |
| --- | --- |
| Issue | Accepts the issue ID or key. |
| Body | Content of the comment. Use the Jira format **\[~username\]** to mention a user. |
| Public | Specify the comment visibility. Type `true` to create a public comment or `false` to create a private comment. |

## Output

The output for this action is a datatree that contains information about the created Jira Service Desk comment.

Refer to the Jira Service Desk documentation for more information on the [comment object](https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-request/#api-rest-servicedeskapi-request-issueidorkey-comment-post).

---
