---
url: 'https://docs.workato.com/en/connectors/trello/update-card-action.md'
description: >-
  The Update card action in the Trello connector lets you update the fields of a
  card you specify, including its name, description, due date, and location.
---

# Trello - Update card action

The **Update card** action updates the fields of a card you specify.

## Input

| Field | Description |
| --- | --- |
| Card ID | Specify the ID of the card to update. Obtain the ID from a prior [List cards](/en/connectors/trello/list-cards-action) action. |
| Title | Provide a new name for the card. |
| Description | Provide a new description for the card. |
| Due date | Provide a new due date for the card. |
| List ID | Specify the ID of the list to move the card to. Obtain the ID from a prior [List lists](/en/connectors/trello/list-lists-action) action. |

## Output

| Field | Description |
| --- | --- |
| ID | The ID of the card. |
| Badges | An object that contains the information displayed on the front of the card, such as the `Votes`, `Comments`, and `Attachments`. |
| Closed | Indicates whether the card is closed (archived). Setting a board to archived doesn't set the cards within the board to archived. A card on an archived board may display as `closed: false`. |
| Desc | The description on the card, up to 16384 characters. |
| Email | The email address used to add cards to the list by email. |
| Updated at | A timestamp indicating when the card was last updated. |
| ID list | The ID of the list that contains the card. |
| ID attachment cover | The ID of the card's cover image, if it has one. |
| ID board | The ID of the board that contains the card. |
| ID short | A short ID for the card, unique only within the current board, and subject to change as cards move. |
| ID members | An array of member IDs that are associated with the card. |
| Labels | A list of the labels on the card. Each contains fields such as `Color`, `Uses`, and `Name`. |
| Manual cover attachment | Indicates whether the card cover image was selected automatically by Trello, or manually by the user. |
| Short link | An eight character ID for the card. |
| Short URL | The URL of the card, shortened by removing the name slug. |
| Subscribed | Indicates whether the connected account is subscribed to the card. |
| ID labels | An array containing the IDs of the labels on the card. |
| URL | The full URL for the card. |
| Display name | The name of the card. |
| Description | The description on the card, up to 16384 characters. |
| Due date | The due date on the card, if one exists. |
| Position | The position of the card within the list. |
| Due complete | Indicates whether the card's due date has been marked as complete. |

---
