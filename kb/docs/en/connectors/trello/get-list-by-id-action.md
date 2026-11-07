---
url: 'https://docs.workato.com/en/connectors/trello/get-list-by-id-action.md'
description: >-
  The Get list by ID action in the Trello connector lets you retrieve
  information about a list you specify by ID.
---

# Trello - Get list by ID action

The **Get list by ID** action retrieves information about a list you specify by ID.

## Input

| Field | Description |
| --- | --- |
| List ID | Specify the ID of the list to retrieve. |

## Output

| Field | Description |
| --- | --- |
| List ID | The ID of the list. |
| List name | The name of the list. |
| Closed | Indicates whether the list is closed (archived). |
| Board ID | The ID of the board that contains the list. |
| Position | The position of the list within the board. |
| Board | An object that contains information about the board that contains the list, such as its `Board ID`, `Board name`, and `URL`. |

---
