---
url: 'https://docs.workato.com/en/connectors/jira/new-event-trigger.md'
description: This trigger monitors Jira for new events in real-time.
---

# Jira - New event trigger (real-time)

The **New event (real-time)** trigger monitors Jira for new events in real-time.

## Prerequisites

This trigger requires the `administrators` global permission in Jira and an authentication type other than OAuth 2.0.

Use the **HTTP** connector's [New event via polling](/en/developing-connectors/http/building-http-trigger) trigger or the [Webhooks connector](/en/connectors/workato-webhooks) if the connected Jira account doesn't have this permission.

Refer to [How Jira real-time triggers work in Workato](/en/connectors/jira/triggers#how-jira-real-time-triggers-work-in-workato) for more information.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type to monitor. |
| Event name | Enter the name of the event configured in Jira. |

> **CONFIGURATION IN JIRA**
> 
> Refer to the [Registering a webhook trigger as a Jira Administrator](/en/connectors/jira#using-jira-real-time-triggers) guide after you configure the input fields to complete the trigger setup.

## Output

The output for this trigger varies based on your **Object** selection. For example, the `Project` object returns the following:

| Output field | Description |
| --- | --- |
| Timestamp | A timestamp indicating when the project was created. |
| Webhook event | The type of Jira webhook event that triggered the job. |
| Project | Contains information about the new project, including the `Self` URL and `Description`. |

---
