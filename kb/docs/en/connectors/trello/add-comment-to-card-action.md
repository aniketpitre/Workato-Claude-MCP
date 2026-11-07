---
url: 'https://docs.workato.com/en/connectors/trello/add-comment-to-card-action.md'
description: >-
  The Add comment to card action in the Trello connector lets you add a comment
  to a card you specify.
---

# Trello - Add comment to card action

The **Add comment to card** action adds a comment to a card you specify.

## Input

| Field | Description |
| --- | --- |
| Card name | Specify the name of the card to which to add the comment. |
| Comment | Provide the comment to add. |

## Output

| Field | Description |
| --- | --- |
| ID | The ID of the card. |
| ID member creator | The ID of account that added the comment. |
| Data | An object that contains information about the board, list, and card where this action took place, such as their `ID` and `Name`. |
| Type | The type of action that was taken. |
| Date | A timestamp of when the comment was added. |
| Member creator | An object that contains information about the account that added the comment, such as its `ID`, `Username`, and `Full name`. |
| Entities | An object that contains information about the comment, list, card, and user associated with this action, such as the associated `Username`, `ID`, and `Translation key`. |
| Display | An object that contains information used within the Trello display, such as the `Translation key`, `Comment` object, and `Card` object. |

---
