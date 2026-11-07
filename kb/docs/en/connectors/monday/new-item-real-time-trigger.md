---
url: 'https://docs.workato.com/en/connectors/monday/new-item-real-time-trigger.md'
description: >-
  The New item (real-time) trigger runs the recipe instantly when a new item is
  created in Monday.
---

# Monday - New item trigger (real-time)

The **New item (real-time)** trigger runs the recipe instantly when a new item is created in Monday.

## Input

| Input field | Description |
| --- | --- |
| Board name | Enter the name of the board to monitor. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the item. |
| Created at | The time the item was created. |
| Event | The name of the event. |
| Entity | The name of the entity. |
| Account ID | The account’s unique identifier. |
| User ID | The user’s unique identifier. |
| Board ID | The board’s unique identifier. |
| Group ID | The group’s unique identifier. |
| Group name | The name of the group. |
| Group color | The color associated with group. |
| Is top group | Indicates whether the item belongs to the top group. |
| Item ID | The item’s unique identifier. |
| Pulse name | The name of the pulse (item). |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/monday/new-moved-item-to-group-real-time-trigger.md
description: >-
  The New moved item to group (real-time) trigger runs the recipe instantly when
  an item is moved to a group in Monday.
---

# Monday - New moved item to group trigger (real-time)

The **New moved item to group (real-time)** trigger runs the recipe instantly when an item is moved to a group in Monday.

## Input

| Input field | Description |
| --- | --- |
| Board | Select the board to monitor for any moved items. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the event. |
| Created at | Date and time the event was created. |
| Event | The name of the event. |
| Entity | The name of the entity. |
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
| Pulse name | The name of the pulse (item). |
| Action record ID | The action record’s unique identifier. |
| Is undo action | Reverses previous action or not. |
| Is batch action | Processes multiple actions together or not. |

---

---
url: >-
  https://docs.workato.com/en/connectors/monday/update-any-column-value-trigger.md
description: >-
  The Update Any Column Value trigger runs the recipe when any column value is
  updated on Monday.
---

# Monday - Update any column value trigger

The **Update any column value** trigger runs the recipe when any column value is updated in Monday.

## Input

| Input field | Description |
| --- | --- |
| Board name | Enter the name of the board to monitor. |
| When first started, this recipe should pick up events from | Set the date and time for the trigger to start picking up items when the recipe runs for the first time. Defaults to 1 hour ago if left blank. You can't change this value after the recipe runs or tests successfully. |

## Output

| Output field | Description |
| --- | --- |
| Item ID | The item’s unique identifier. |

---

---
url: >-
  https://docs.workato.com/en/connectors/monday/update-any-column-value-real-time-trigger.md
description: >-
  The Updated any column value (real-time) trigger runs the recipe instantly
  when an item is moved to any group in Monday.
---

# Monday - Update any column value trigger (real-time)

The **Updated any column value (real-time)** trigger runs the recipe instantly when an item is moved to any group in Monday.

## Input

| Input field | Description |
| --- | --- |
| Board | Select the board to monitor for any column value changes. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the event. |
| Created at | Date and time the event was created. |
| Event | The name of the event. |
| Entity | The name of the entity. |
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
| Pulse name | The name of the pulse (item). |
| Action record ID | The action record’s unique identifier. |
| Is undo action | Reverses previous action or not. |
| Is batch action | Processes multiple actions together or not. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/monday/update-specific-column-value-real-time-trigger.md
description: >-
  The Updated specific column value (real-time) trigger runs the recipe
  instantly when a specific column value is updated in Monday.
---

# Monday - Updated specific column value trigger (real-time)

The **Updated specific column value (real-time)** trigger runs the recipe instantly when a specific column value is updated in Monday.

## Input

| Input field | Description |
| --- | --- |
| Board | Select the board to monitor for column value updates. |
| Column | Select the column to monitor for column value updates. |

## Output

Output fields depend on the object you select in the input. Refer to the [Monday](https://developer.monday.com/api-reference/reference/about-the-api-reference) documentation for a complete list of output fields.

---
