---
url: 'https://docs.workato.com/en/connectors/trello/list-boards-action.md'
description: >-
  The List boards action in the Trello connector lets you retrieve the boards
  that the connected account can access.
---

# Trello - List boards action (batch)

The **List boards** action retrieves the boards that the connected account can access.

## Input

| Field | Description |
| --- | --- |
| Filter | Specify which boards to return. Default is `Open`. |
| Page size | Specify the number of boards to return per page, from `1` to `100`. Default is `50`. |
| Offset | Provide the offset from a previous response to fetch the next page. Leave blank to start from the beginning. |

## Output

| Field | Description |
| --- | --- |
| Boards | A list of board objects. Each contains fields such as `ID`, `Name`, `ID organization`, `Desc`, `Closed`, `URL`, `Prefs`, `Memberships`, and `Short URL`. |
| Next offset | The offset to provide in a subsequent request to retrieve the next page of boards. |

---
