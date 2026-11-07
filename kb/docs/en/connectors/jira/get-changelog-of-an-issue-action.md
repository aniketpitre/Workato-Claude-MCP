---
url: >-
  https://docs.workato.com/en/connectors/jira/get-changelog-of-an-issue-action.md
description: This action retrieves an issue's changelog from Jira.
---

# Jira - Get changelog of an issue action

The **Get changelog of an issue** action retrieves an issue's changelog from Jira.

## Input

| Input field | Description |
| --- | --- |
| Issue ID or key | Enter the ID or key of the issue to retrieve a changelog for. |

## Output

| Output field | Description |
| --- | --- |
| Self | The API URL of the issue. |
| Max results | The maximum number of results returned in each page. |
| Start at | The index of the current results page in the results list. |
| Total | The total number of results retrieved. |
| Is last | Indicates whether the current page of the results list is the last page. |
| Values | Contains information about the changelog, including `Author` and `Items`. |
