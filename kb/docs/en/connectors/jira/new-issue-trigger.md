---
url: 'https://docs.workato.com/en/connectors/jira/new-issue-trigger.md'
description: This trigger checks Jira for new issues at an interval you specify.
---

# Jira - New issue trigger

The **New issue** trigger checks Jira for new issues at an interval you specify.

> **ISSUE ACCESS**
> 
> Workato only triggers jobs from issues that the connected Jira account has access to.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Optional. Select how frequently to check for new events. The default and minimum value is five minutes. |
| When first started, this recipe should pick up events from | Specify the date and time from which the recipe picks up trigger events. Defaults to one hour ago if left blank. You can't change this value after running or testing the recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output field | Description |
| --- | --- |
| ID | The numeric Jira identifier for the issue. For example: `16982` |
| Self | The API URL of the issue. |
| Key | The human-readable Jira identifier for the new issue. For example: `SQ-16` |
| Changelog | Contains information about previous changes to the issue, including `Histories`. |
| Fields | Contains information about the issue's fields, including `Parent` and `Last Viewed` time. |

---
