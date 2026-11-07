---
url: 'https://docs.workato.com/en/connectors/trello/search-cards-action.md'
description: >-
  The Search cards action in the Trello connector lets you retrieve information
  about a card you specify by name.
---

# Trello - Search cards action (batch)

The **Search cards** action is used to retrieve information about a card you specify.

## Input

| Field | Description |
| --- | --- |
| Card name | Specify the name of the card to search. |

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
| List size | The total number of cards in the same list as this card. |
| List index | The position the card within the list. |

---
