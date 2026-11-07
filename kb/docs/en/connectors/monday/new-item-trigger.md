---
url: 'https://docs.workato.com/en/connectors/monday/new-item-trigger.md'
description: The New item trigger runs the recipe when a new item is created on Monday.
---

# Monday - New item trigger

The **New item** trigger runs the recipe when a new item is created in Monday.

## Input

| Input field | Description |
| --- | --- |
| Board name | Enter the name of the board to monitor. |
| When first started, this recipe should pick up events from | Set the date and time for the trigger to start picking up items when the recipe runs for the first time. Defaults to 1 hour ago if left blank. You can't change this value after the recipe runs or tests successfully. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the item. |
| Created at | The time the item was created. |
| Event | Given event name. |
| Entity | Given entity name. |
| Account ID | The account’s unique identifier. |
| User ID | The user’s unique identifier. |
| Board ID | The board’s unique identifier. |
| Group ID | The group’s unique identifier. |
| Group name | Given group name. |
| Group color | The color associated with group. |
| Is top group | Indicates whether the item belongs to the top group. |
| Item ID | The item’s unique identifier. |
| Pulse name | Given pulse name. |

---
