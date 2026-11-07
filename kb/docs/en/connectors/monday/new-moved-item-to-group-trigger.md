---
url: >-
  https://docs.workato.com/en/connectors/monday/new-moved-item-to-group-trigger.md
description: >-
  The New Moved Item to Group trigger runs the recipe when an item is moved to a
  group on Monday.
---

# Monday - New moved item to group trigger

The **New moved item to group** trigger runs the recipe when an item is moved to a group in Monday.

## Input

| Input field | Description |
| --- | --- |
| Board name | Enter the name of the board to monitor. |
| Group name | Enter the name of the group to monitor. |
| When first started, this recipe should pick up events from | Set the date and time for the trigger to start picking up items when the recipe runs for the first time. Defaults to 1 hour ago if left blank. You can't change this value after the recipe runs or tests successfully. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the event. |
| Created at | Date and time the event was created. |
| Event | Given event name. |
| Entity | Given entity name. |
| Account ID | The account’s unique identifier. |
| User ID | The user’s unique identifier. |
| Board ID | The board’s unique identifier. |
| Group ID | The group’s unique identifier. |
| ID | The source board’s unique identifier. |
| Name | The source board’s name. |
| Kind | The source board’s kind. |
| ID | The source group’s unique identifier. |
| Name | The source group’s name. |
| Color | The source group’s color. |
| Is top group | Belongs to top source group or not. |
| ID | The destination group’s unique identifier. |
| Name | The destination group’s name. |
| Color | The destination group’s color. |
| Is top group | Belongs to top destination group or not. |
| Pulse ID | The pulse’s unique identifier. |
| Pulse name | Given pulse name. |
| Action record ID | The action record’s unique identifier. |
| Is undo action | Reverses previous action or not. |
| Is batch action | Processes multiple actions together or not. |
