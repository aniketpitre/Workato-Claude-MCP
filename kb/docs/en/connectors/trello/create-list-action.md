---
url: 'https://docs.workato.com/en/connectors/trello/create-list-action.md'
description: >-
  The Create list action in the Trello connector lets you create a new list at a
  position you set on a board you specify.
---

# Trello - Create list action

The **Create list** action creates a new list on a board that you specify.

## Input

| Field | Description |
| --- | --- |
| Board name | Specify the name of the board to which you plan to add the list. |
| List name | Provide a name for the list. |
| Position | Provide a position for the list within the board. Valid values include: `top`, `bottom`, or a positive integer such as `1`. |

## Output

| Field | Description |
| --- | --- |
| ID | The ID of the list. |
| Name | The name of the list. |
| Closed | Indicates whether the list is closed (archived). |
| ID board | The ID of the board that contains the list. |
| Pos | The position of the list within the board. |

---
