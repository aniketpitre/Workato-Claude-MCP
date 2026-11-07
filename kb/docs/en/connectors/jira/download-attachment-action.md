---
url: 'https://docs.workato.com/en/connectors/jira/download-attachment-action.md'
description: This action downloads an attachment from a Jira issue.
---

# Jira - Download attachment action

The **Download attachment** action downloads an attachment from a Jira issue.

You can use this action to sync files, such as screenshots attached to tickets, between Jira and another ticket management application (for example, [ServiceNow](/en/connectors/servicenow) or [Freshdesk](/en/connectors/freshdesk)).

## Input

| Input field | Description |
| --- | --- |
| Attachment URI | Enter the URI of an attachment. You can retrieve this value from the output of other steps. For example, the Self datapill from the [Get issue](/en/connectors/jira/get-issue-action) action. |

## Output

| Output field | Description |
| --- | --- |
| Attachment content | The content of the attachment. |
| Size | The size of the attachment in bytes. |

---

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

---
