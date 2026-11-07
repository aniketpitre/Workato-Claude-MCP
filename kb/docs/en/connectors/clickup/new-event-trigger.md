---
url: 'https://docs.workato.com/en/connectors/clickup/new-event-trigger.md'
description: >-
  The **New event** trigger runs immediately as soon as trigger events, such as
  a task created, occur.
---

# ClickUp - New event trigger

The **New event** trigger runs immediately as soon as trigger events, such as a task creation, occur in ClickUp.

## Input

Input fields load dynamically based on the object selected. For example, if you select the **Space** object, the following input fields are available:

| Input field | Description |
| --- | --- |
| Events | Select the type of event associated with the webhook from the drop-down menu. |
| Workspace/Team | Select the name of the team or workspace from the drop-down menu. |
| Space | Select the name of the space from the drop-down menu. |

## Output

The output loads dynamically based on the object selected when configuring the action. For example, if you select the **Space** object, the following output schema is generated.

| Output field | Description |
| --- | --- |
| Space ID | Unique identifier of the ClickUp Space where the event occurred. |
| Webhook ID | Unique identifier of the webhook that triggered this event. |
| Event | Type of event that occurred, such as `spaceUpdated`. Indicates what action in ClickUp triggered the webhook. |

---
