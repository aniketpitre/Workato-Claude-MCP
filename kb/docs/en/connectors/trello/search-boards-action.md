---
url: 'https://docs.workato.com/en/connectors/trello/search-boards-action.md'
description: >-
  The Search boards action in the Trello connector lets you retrieve information
  about a board you specify by name.
---

# Trello - Search boards action (batch)

The **Search boards** action is used to retrieve information about a board you specify.

## Input

| Field | Description |
| --- | --- |
| Board name | Specify the name of the board to search. |

## Output

| Field | Description |
| --- | --- |
| ID | The ID of the board. |
| Name | The name of the board. |
| ID organization | The ID of the organization this board belongs to. |
| Desc | Contains the board's description, up to 16384 characters. |
| Closed | Indicates whether the board is closed (archived). |
| Invited | Indicates whether the connected account has been invited to the board. |
| Pinned | Indicates whether the connected account has pinned the board. |
| Starred | Indicates whether the connected account has starred the board. |
| URL | The full URL for the board. |
| Prefs | An object that contains information about the board's settings, such as the `Permission level`, `Card aging`, and `Background color`. |
| Memberships | A datatree that contains information about the account that created the board, such as its `ID`, `Member type`, and `Deactivated` status. |
| Short link | An eight character ID for the board. |
| Subscribed | Indicates whether the connected account is subscribed to the board. |
| Label names | An object that contains the names of colors used in the board's labels. |
| Date last view | The date the board was last viewed. |
| Short URL | The URL of the board, shortened by removing the name slug. |

---
