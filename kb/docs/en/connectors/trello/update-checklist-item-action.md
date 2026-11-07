---
url: 'https://docs.workato.com/en/connectors/trello/update-checklist-item-action.md'
description: >-
  The Update checklist item action in the Trello connector lets you update a
  checklist item on a card you specify.
---

# Trello - Update checklist item action

The **Update checklist item** action updates a checklist item on a card you specify.

## Input

| Field | Description |
| --- | --- |
| Card ID | Specify the ID of the card that contains the checklist item. Obtain the ID from a prior [List cards](/en/connectors/trello/list-cards-action) action. |
| Checklist item ID | Specify the ID of the checklist item to update. Obtain the ID from a prior [Get card details](/en/connectors/trello/get-card-details-action) action. |
| State | Specify the state of the checklist item. Valid values include: `complete` or `incomplete`. |

## Output

| Field | Description |
| --- | --- |
| ID | The ID of the checklist item. |
| Name | The name of the checklist item. |
| State | Indicates whether the checklist item is `complete` or `incomplete`. |
| Checklist ID | The ID of the checklist that contains the item. |
| Card ID | The ID of the card that contains the checklist item. |
| Board ID | The ID of the board that contains the card. |
| Position | The position of the checklist item within the checklist. |
| Due date | The due date on the checklist item, if one exists. |
| Due reminder | The number of minutes before the due date to send a reminder, if one is set. |
| Member ID | The ID of the member assigned to the checklist item, if any. |

---
