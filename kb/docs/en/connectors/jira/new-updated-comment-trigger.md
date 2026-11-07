---
url: 'https://docs.workato.com/en/connectors/jira/new-updated-comment-trigger.md'
description: This trigger monitors Jira for new or updated comments in real-time.
---

# Jira - New/updated comment trigger (real-time)

The **New/updated comment (real-time)** trigger monitors Jira for new or updated comments in real-time.

> **COMMENT ACCESS**
> 
> Workato only triggers jobs from comments that the connected Jira account has access to.

## Prerequisites

This trigger requires the `administrators` global permission in Jira and an authentication type other than OAuth 2.0.

Use the **HTTP** connector's [New event via polling](/en/developing-connectors/http/building-http-trigger) trigger or the [Webhooks connector](/en/connectors/workato-webhooks) if the connected Jira account doesn't have this permission.

Refer to [How Jira real-time triggers work in Workato](/en/connectors/jira/triggers#how-jira-real-time-triggers-work-in-workato) for more information.

## Input

| Input field | Description |
| --- | --- |
| JQL where clause | Enter a JQL query to filter records by. For example: `project = "PRJ" AND status = "Done"`. This field only supports the following queries: `issueKey`, `project`, `issuetype`, `status`, `assignee`, `reporter`, `issue`, `property`, and `cf[id]`. The `ORDER BY` clause isn't supported. Refer to the Jira documentation to learn more about [JQL](https://www.atlassian.com/software/jira/guides/jql/overview#what-is-jql). |

## Output

| Output field | Description |
| --- | --- |
| Self | The API URL of the new or updated comment. |
| ID | The Jira identifier of the new or updated comment. |
| Author | Contains information about the user who originally made the comment, including `Name` and `Account ID`. |
| Body | The string content of the comment. |
| Update author | Contains information about the user who updated the comment, including `Name` and `Account ID`. |
| Created | The date and time when the comment was created. |
| Updated | The date and time when the comment was updated. |
| Visibility | Contains information about the comment's visibility settings, including `Type` and `Value`. |

---
