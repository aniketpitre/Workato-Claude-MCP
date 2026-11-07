---
url: 'https://docs.workato.com/en/connectors/monday/new-activity-log-trigger.md'
description: The New activity log trigger monitors Monday for new activity logs.
---

# Monday - New activity log trigger

The **New activity log** trigger monitors Monday for new activity logs.

## Input

| Input field | Description |
| --- | --- |
| Board name | The name of the Monday board to monitor for activity logs. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up activity logs. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Output schema | Use JSON or add fields manually to define the output schema for the new activity log. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the newly created activity log. |
| Created at | The date/time that the new activity log was created. |
| Event | Specific events returned in the newly created activity log. |
| Entity | The entity of the event changed in the newly created activity log. |
| Account ID | The ID of the account that initiated the new activity log. |
| User ID | The ID of the user who initiated the newly created activity log. |
| Data | The column values of the newly created activity log trigger. |

---
