---
url: 'https://docs.workato.com/en/connectors/jira/deleted-object-trigger.md'
description: This trigger monitors Jira for deleted objects in real-time.
---

# Jira - Deleted object trigger (real-time)

The **Deleted object (real-time)** trigger monitors Jira for deleted objects in real-time.

## Prerequisites

This trigger requires the `administrators` global permission in Jira and an authentication type other than OAuth 2.0.

Use the **HTTP** connector's [New event via polling](/en/developing-connectors/http/building-http-trigger) trigger or the [Webhooks connector](/en/connectors/workato-webhooks) if the connected Jira account doesn't have this permission.

Refer to [How Jira real-time triggers work in Workato](/en/connectors/jira/triggers#how-jira-real-time-triggers-work-in-workato) for more information.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to monitor. |

## Output

The output for this trigger varies based on your `Object` selection. For example, the `Issue` object returns the following:

| Output field | Description |
| --- | --- |
| ID | The numeric Jira identifier for the deleted object. For example: `16982`. |
| Self | The API URL of the deleted Jira object. |
| Key | The human-readable Jira identifier for the deleted object. For example: `SQ-16`. |
| Changelog | Contains information about previous changes to the deleted object, such as `Histories`. |
| Fields | Contains information about the object's fields, such as its `Parent` and `Last Viewed` time. Workato automatically fetches and expands all parameters. Refer to the Jira Cloud REST API documentation on [resource expansion](https://developer.atlassian.com/cloud/jira/platform/rest/#expansion) for more information. |

---
