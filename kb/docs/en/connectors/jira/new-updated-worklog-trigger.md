---
url: 'https://docs.workato.com/en/connectors/jira/new-updated-worklog-trigger.md'
description: This trigger monitors Jira for new or updated worklogs in real-time.
---

# Jira - New/updated worklog trigger (real-time)

The **New/updated worklog (real-time)** trigger monitors Jira for new or updated worklogs in real-time.

> **WORKLOG ACCESS**
> 
> Workato only triggers jobs from worklogs that the connected Jira account has access to.

## Prerequisites

This trigger requires the `administrators` global permission in Jira and an authentication type other than OAuth 2.0.

Use the **HTTP** connector's [New event via polling](/en/developing-connectors/http/building-http-trigger) trigger or the [Webhooks connector](/en/connectors/workato-webhooks) if the connected Jira account doesn't have this permission.

Refer to [How Jira real-time triggers work in Workato](/en/connectors/jira/triggers#how-jira-real-time-triggers-work-in-workato) for more information.

## Input

No input fields are required.

## Output

| Output field | Description |
| --- | --- |
| Self | The API URL of the new or updated worklog. |
| ID | The numeric Jira identifier of the new or updated worklog. For example: `16982`. |
| Comment | The comments added to the worklog. |
| Author | Contains information about the original author, including `Name` and `Account ID`. |
| Body | The content of the worklog. |
| Update author | Contains information about the author of the latest update, including `Name` and `Account ID`. |
| Created | The date and time the worklog was originally created. |
| Updated | The date and time the worklog was last updated. |
| Started | The date and time the worklog started. |
| Time spent | The total amount of time logged in human-readable format. |
| Time spent seconds | The total amount of time logged in seconds. |
| Issue ID | The Jira identifier for the issue. |

---
