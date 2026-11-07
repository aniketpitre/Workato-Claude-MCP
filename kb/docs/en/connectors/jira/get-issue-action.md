---
url: 'https://docs.workato.com/en/connectors/jira/get-issue-action.md'
description: This action retrieves an issue from Jira.
---

# Jira - Get issue action

The **Get issue** action retrieves an issue from Jira.

## Input

| Input field | Description |
| --- | --- |
| Issue ID or key | Enter the ID or key of the issue to retrieve. |

## Output

| Output field | Description |
| --- | --- |
| ID | The numeric Jira identifier for the issue. |
| Self | The API URL of the issue. |
| Key | The human-readable Jira identifier for the issue. |
| Changelog | Contains information about previous changes to the issue, such as `Histories`. |
| Fields | Contains information about the object's fields, such as its `Parent` and `Last Viewed` time. Workato automatically fetches and expands all parameters. Refer to the Jira Cloud REST API documentation on [resource expansion](https://developer.atlassian.com/cloud/jira/platform/rest/#expansion) for more information. |

---
