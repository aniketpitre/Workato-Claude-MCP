---
url: 'https://docs.workato.com/en/connectors/jira/new-issue-batch-trigger.md'
description: >-
  This trigger retrieves new issues from Jira in batches at an interval you
  specify.
---

# Jira - New issue trigger (batch)

The **New issue (batch)** trigger retrieves new issues from Jira in batches at an interval you specify.

> **ISSUE ACCESS**
> 
> Workato only triggers jobs from issues that the connected Jira account has access to.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Optional. Select how frequently to check for new events. The default and minimum value is five minutes. |
| When first started, this recipe should pick up events from | Specify the date and time from which the recipe picks up trigger events. Defaults to one hour ago if left blank. You can't change this value after running or testing the recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Batch size | Optional. Enter the number of issues to include in each batch. The default and maximum value is `100`. |

## Output

| Output field | Description |
| --- | --- |
| Range | The range of record IDs retrieved in the batch. For example: `16982..16982` |
| First issue ID | The Jira identifier of the first issue in the batch. |
| Last issue ID | The Jira identifier of the last issue in the batch. |
| Issues | Contains information about the new issues, including `Changelog` and `Fields`. |

---
