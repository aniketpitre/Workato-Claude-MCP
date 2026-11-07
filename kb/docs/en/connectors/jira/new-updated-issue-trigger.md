---
url: 'https://docs.workato.com/en/connectors/jira/new-updated-issue-trigger.md'
description: This trigger monitors Jira for new or updated issues in real-time.
---

# Jira - New/updated issue trigger (real-time)

The **New/updated issue (real-time)** trigger monitors Jira for new or updated issues in real-time.

> **ISSUE ACCESS**
> 
> Workato only triggers jobs from issues that the connected Jira account has access to.

## Prerequisites

This trigger requires the `administrators` global permission in Jira and an authentication type other than OAuth 2.0.

Use the **HTTP** connector's [New event via polling](/en/developing-connectors/http/building-http-trigger) trigger or the [Webhooks connector](/en/connectors/workato-webhooks) if the connected Jira account doesn't have this permission.

Refer to [How Jira real-time triggers work in Workato](/en/connectors/jira/triggers#how-jira-real-time-triggers-work-in-workato) for more information.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Specify the date and time from which the recipe picks up trigger events. Defaults to one hour ago if left blank. You can't change this value after running or testing the recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| JQL WHERE clause | Filter the records using a JQL query, such as `project = "PRJ" AND status = "Done"`. Only `issueKey`, `project`, `issuetype`, `status`, `assignee`, `reporter`, `issue.property`, and `cf[id]` JQL queries are supported. Refer to the Jira documentation to learn more about [JQL](https://www.atlassian.com/software/jira/guides/jql/overview#what-is-jql). |

## Output

| Output field | Description |
| --- | --- |
| ID | The numeric Jira identifier of the new or updated issue. |
| Self | The API URL of the new or updated issue. |
| Key | The human-readable Jira identifier for the issue, for example: `SQ-16` |
| Changelog | Contains information about previous changes to the issue, including `Histories`. |
| Fields | Contains information about the issue's fields, including its `Parent` and `Last Viewed` time. |
| Webhook data | Contains information about the webhook event, including the `Timestamp` and `Webhook event` name. |

This output doesn't include all issue-related fields due to Jira API limitations. Use the **Get issue** action to obtain all issue-related fields.

---
