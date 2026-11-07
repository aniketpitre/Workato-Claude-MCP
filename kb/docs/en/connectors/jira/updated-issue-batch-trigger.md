---
url: 'https://docs.workato.com/en/connectors/jira/updated-issue-batch-trigger.md'
description: >-
  This trigger retrieves updated issues from Jira in batches at an interval you
  specify.
---

# Jira - Updated issue trigger (batch)

The **Updated issue (batch)** trigger retrieves updated issues from Jira in batches at an interval you specify.

> **ISSUE ACCESS**
> 
> Workato only triggers jobs from issues that the connected Jira account has access to.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Optional. Select how frequently to check for new events. The default and minimum value is five minutes. |
| When first started, this recipe should pick up events from | Specify the date and time from which the recipe picks up trigger events. Defaults to one hour ago if left blank. You can't change this value after running or testing the recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Batch size | Optional. Enter the number of issues to include in each batch. The default and maximum value is `100`. |
| JQL WHERE clause | Filter the records using a JQL query, such as `project = "PRJ" AND status = "Done"`. Only `issueKey`, `project`, `issuetype`, `status`, `assignee`, `reporter`, `issue.property`, and `cf[id]` JQL queries are supported. Refer to the Jira documentation to learn more about [JQL](https://www.atlassian.com/software/jira/guides/jql/overview#what-is-jql). |

## Output

| Output field | Description |
| --- | --- |
| Range | The range of record IDs retrieved in the batch. For example: `16982..16982` |
| First issue ID | The Jira identifier of the first issue in the batch. |
| Last issue ID | The Jira identifier of the last issue in the batch. |
| Issues | Contains information about the updated issues, including `Changelog` and `Fields`. |

---
