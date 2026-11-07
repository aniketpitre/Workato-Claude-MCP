---
url: 'https://docs.workato.com/en/connectors/trello/create-card-action.md'
description: >-
  The Create card action in the Trello connector lets you create a new card in a
  list you specify, with a name, description, and due date.
---

# Trello - Create card action

The **Create card** action creates a new card in a list that you specify.

## Input

| Field | Description |
| --- | --- |
| List name | Specify the name of the list where you plan to add the card. |
| Display name | Provide a display name for the card. |
| Description | Provide a description for the card. |
| Due date | Provide a due date for the card. |
| Closed | Specify whether to set the card to closed. |
| Email | Provide an email to associate with the card. |
| Position | Specify the position the card should take in the list. Valid values include: `top`, `bottom`, or a positive integer such as `1`. |

## Output

| Field | Description |
| --- | --- |
| ID | The ID of the card. |
| Badges | An object that contains the information displayed on the front of the card, such as the `Votes`, `Comments`, and `Attachments`. |
| Closed | Indicates whether the card is closed (archived). Setting a board to archived does not set the cards within the board to archived. A card on an archived board may display as `closed: false`. |
| Updated at | A timestamp indicating when the card was last updated. |
| ID list | The ID of the list that contains the card. |
| ID attachment cover | The ID of the card's cover image, if it has one. |
| ID board | The ID of the board that contains the card. |
| ID short | A short ID for the card, unique only within the current board, and subject to change as cards move. |
| ID members | An array of member IDs that are associated with the card. |
| Labels | A datatree that contains information regarding the labels on the card, such as their `Color`, number of `Uses`, and `Name`. |
| Manual cover attachment | Indicates whether the cover image was set automatically by Trello. |
| Short link | An eight character ID for the card. |
| Short URL | The URL of the card, shortened by removing the name slug. |
| Subscribed | Indicates whether the connected account is subscribed to the card. |
| ID labels | An array containing the IDs of the labels on the card. |
| URL | The full URL for the card. |
| Display name | The name of the card. |
| Description | The description on the card, up to 16384 characters. |
| Due date | The due date on the card, if one exists. |
| Position | The position of the card within the list. |

---
