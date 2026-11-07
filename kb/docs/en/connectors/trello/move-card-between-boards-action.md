---
url: >-
  https://docs.workato.com/en/connectors/trello/move-card-between-boards-action.md
description: >-
  The Move card between boards action in the Trello connector lets you move a
  card from one board to a list on another board.
---

# Trello - Move card between boards action

The **Move card between boards** action moves a card between boards.

## Input

| Field | Description |
| --- | --- |
| Card ID | Specify the card you intend to move. |
| Board name | Select the board where you plan to add the card. |
| List name | Specify the list to put the card under. |

## Output

| Field | Description |
| --- | --- |
| ID | The ID of the card that was moved. |
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
