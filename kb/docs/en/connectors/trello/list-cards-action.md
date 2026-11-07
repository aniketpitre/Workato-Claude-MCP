---
url: 'https://docs.workato.com/en/connectors/trello/list-cards-action.md'
description: >-
  The List cards action in the Trello connector lets you retrieve the cards in a
  list you specify.
---

# Trello - List cards action (batch)

The **List cards** action retrieves the cards in a list you specify.

The action scans a maximum of 5,000 cards per call when you filter by assignee, label, or due date. If the `More cards to scan` output field is `true`, this means that the scan stopped before reaching older cards. Use the Cursor output datapill to continue the scan from where it stopped.

## Input

| Field | Description |
| --- | --- |
| Board name | Specify the board to retrieve cards from. Provide a board or a list. At least one is required. |
| List name | Specify the list to retrieve cards from. Provide a board or a list. At least one is required. |
| Assignee | Filter cards by member ID. |
| Due date before | Return cards with a due date on or before this date, inclusive. Cards without a due date are excluded. |
| Due date after | Return cards with a due date on or after this date, inclusive. Cards without a due date are excluded. |
| Label | Filter by label ID (a 24-character hex value) or label name. A name collision returns an error. |
| Limit | Specify the maximum number of cards to return, from `1` to `100`. Default is `50`. |
| Cursor | Provide the pagination cursor from a prior response to fetch the next page. |
| Filter | Specify which cards to return. Default is `Open`. |

## Output

| Field | Description |
| --- | --- |
| Cards | A list of card objects. Each contains fields such as `ID`, `Badges`, `Closed`, `ID list`, `ID board`, `Labels`, `Due date`, `Position`, and `Due complete`. |
| Has more | Indicates whether more cards are available beyond the current page. |
| Cursor | The pagination cursor to provide in a subsequent request to retrieve the next page of cards. |
| More cards to scan | Indicates whether the scan stopped before reaching older cards. If `true`, use the returned `Cursor` to continue scanning. |

---
