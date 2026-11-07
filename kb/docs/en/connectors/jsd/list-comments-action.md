---
url: 'https://docs.workato.com/en/connectors/jsd/list-comments-action.md'
description: >-
  The List comments action in the Jira Service Desk connector lets you list the
  comments on an issue in your service desk instance.
---

# Jira Service Desk - List comments action

This action lists comments in an issue within your Jira Service Desk instance.

![List comments action](/assets/list-comments-action.CWH_2eJO.png)_List comments action_

## Input

| Input field | Description |
| --- | --- |
| Issue | Accepts the issue ID or key |
| \[Optional\] Public | Whether the comment is public or not. Input 1 for true, 0 for false. Defaults to true |
| \[Optional\] Internal | Whether the comment is internal or not. Input 1 for true, 0 for false. Defaults to true |

## Output

The output of this action will be a list of datatree that contains information about the created Jira Service Desk comments.

Find out more about [Jira Service Desk comment object](https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-request/#api-rest-servicedeskapi-request-issueidorkey-comment-get).

---
