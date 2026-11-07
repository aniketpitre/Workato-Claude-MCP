---
url: 'https://docs.workato.com/en/connectors/jira/updated-issue-trigger.md'
description: This trigger checks Jira for updated issues at an interval you specify.
---

# Jira - Updated issue trigger

The **Updated issue** trigger checks Jira for updated issues at an interval you specify.

> **ISSUE ACCESS**
> 
> Workato only triggers jobs from issues that the connected Jira account has access to.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Optional. Select how frequently to check for new events. The default and minimum value is five minutes. |
| When first started, this recipe should pick up events from | Specify the date and time from which the recipe picks up trigger events. Defaults to one hour ago if left blank. You can't change this value after running or testing the recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| JQL WHERE clause | Filter the records using a JQL query, such as `project = "PRJ" AND status = "Done"`. Only `issueKey`, `project`, `issuetype`, `status`, `assignee`, `reporter`, `issue.property`, and `cf[id]` JQL queries are supported. Refer to the Jira documentation to learn more about [JQL](https://www.atlassian.com/software/jira/guides/jql/overview#what-is-jql). |

## Output

| Output field | Description |
| --- | --- |
| ID | The numeric Jira identifier of the updated issue. For example: `16982`. |
| Self | The API URL of the updated issue. |
| Key | The human-readable Jira identifier for the updated issue. For example: `SQ-16`. |
| Changelog | Contains information about previous changes to the issue, including `Histories`. |
| Fields | Contains information about the issue's fields, including its `Parent` and `Last Viewed` time. |

---
