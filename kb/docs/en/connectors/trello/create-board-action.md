---
url: 'https://docs.workato.com/en/connectors/trello/create-board-action.md'
description: >-
  The Create board action in the Trello connector lets you create a new board,
  set its permissions, and optionally copy from an existing board.
---

# Trello - Create board action

The **Create board** action creates a new board within Trello.

## Input

| Field | Description |
| --- | --- |
| Name | Provide a name for the board. |
| Organization | Specify the ID or short name of the organization to add the board to. |
| Self join | Determines whether users can join the boards themselves or have to be invited. |
| Description | Provide a description for the board. |
| Board source ID | Provide the source board's ID if you plan to copy an existing board. |
| Power ups | Specify any power ups you intend to add from Trello's library. |
| Keep from source | To keep cards from the original board, enter `cards`. |
| Permission level | Select the permission level of the new board. |
| Voting | Select which members can vote on board items. |
| Comments | Select which members can create comments. |
| Invitations | Select which members can create invitations. |
| Card covers | Select whether to allow card covers. |
| Card aging | Select the aging mode for the board if you intend to use the card aging power up. |
| Background color | Provide a color to use as the board's background. Valid values include: `blue`, `orange`, `green`, `red`, `purple`, `pink`, `lime`, `sky`, and `grey`. Default is `blue`. |

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
