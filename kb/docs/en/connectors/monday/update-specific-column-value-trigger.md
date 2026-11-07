---
url: >-
  https://docs.workato.com/en/connectors/monday/update-specific-column-value-trigger.md
description: >-
  The Updated Specific Column Value trigger runs the recipe when the specific
  column value is updated on Monday.
---

# Monday - Updated specific column value trigger

The **Updated specific column value** trigger runs the recipe when a specific column value is updated in Monday.

## Input

| Input field | Description |
| --- | --- |
| Board name | Enter the name of the board to monitor. |
| Column name | Enter the name of the column to monitor. |
| When first started, this recipe should pick up events from | Set the date and time for the trigger to start picking up items when the recipe runs for the first time. Defaults to 1 hour ago if left blank. You can't change this value after the recipe runs or tests successfully. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the event. |
| Created at | The date and time the event was created. |
| Event | Given event name. |
| Entity | Given entity name. |
| Account ID | The account’s unique identifier. |
| User ID | The user’s unique identifier. |
| Board ID | The board’s unique identifier. |
| Group ID | The group’s unique identifier. |
| Is top group | Belongs to top group or not. |
| Item ID | The item’s unique identifier. |
| Pulse name | Given pulse name. |
| Column ID | The type of column. |
| Column type | The action record’s unique identifier. |
| Column title | The title of column. |
| Is column with hide permission | Indicates whether the column has hide permissions. |
