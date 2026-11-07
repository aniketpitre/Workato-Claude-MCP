---
url: 'https://docs.workato.com/en/connectors/gitlab/new-event-trigger-real-time.md'
description: The New event trigger immediately detects new events in GitLab.
---

# GitLab - New event trigger (real-time)

The **New event** trigger activates immediately when a new event occurs in GitLab.

## Input

Input fields are dynamically generated based on the object you select. The following fields are common to all object types.

| Input field | Description |
| --- | --- |
| Project or Project ID | Select a project from the drop-down menu or enter the ID. |
| Event Type | Select an event type from the drop-down menu. |

## Output

| Output field | Description |
| --- | --- |
| Object Kind | The specific category for the event. |
| Event Type | The specific action or event. |
| User ID | The ID of the user who initiated the event. |
| User Name | The full display name of the user who initiated the event. For example, `Jade Green`. |
| User Email | The email address of the user who triggered the event. |
| Project ID | The ID for the event project. |
| Project Name | The name of the project that triggered the event. |
| Project Description | The short summary or text written for the project. |
| Author ID | The ID for the user who initiated the event. |
| Repository Name | The base name of the project repository. |

---
