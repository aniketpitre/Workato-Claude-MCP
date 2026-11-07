---
url: 'https://docs.workato.com/en/connectors/teams/list-chats-batch-action.md'
description: >-
  The List chats batch action lists chats the authenticated user participates
  in.
---

# Microsoft Teams - List chats (batch) action

The **List chats** batch action lists chats the authenticated user participates in on Microsoft Teams, including one-on-one, group, and meeting chats.

## Input

| Input field | Description |
| --- | --- |
| Include members | Optional. Select `Yes` to include the list of members. Select `No` to exclude the list of members. |

## Output

| Output field | Description |
| --- | --- |
| Chat ID | The chat unique identifier. |
| Topic | The topic name of the group chat. The value is `null` if the group chat is unnamed or a 1:1 chat. |
| Created date | The date the chat was created. |
| Last updated date | The date the chat was last updated. |
| Chat type | The chat type. Types include `oneOnOne` and `group`. |
| Web URL | The direct link to the chat. |
| Tenant ID | The chat tenant unique identifier. |
| Is hidden for all members | A boolean response (`true` or `false`) that indicates whether the chat is hidden for all its members. |
| Online meeting info | Details about an online meeting, such as the `joinUrl`, `conferenceId`, and dial-in phone numbers. |
| Last message preview | Preview information for the last message. Details include `Message ID`, `Created date`, `Body`, and `From`. |

---
