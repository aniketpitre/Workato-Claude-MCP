---
url: 'https://docs.workato.com/en/connectors/teams/get-chat-action.md'
description: The Get chat action gets details of a specified chat in Microsoft Teams.
---

# Microsoft Teams - Get chat action

The **Get chat** action gets details of a specified chat in Microsoft Teams.

## Input

| Input field | Description |
| --- | --- |
| Chat ID | Enter the chat ID. You can retrieve this value from the **List chats** action. Alternatively, you can retrieve it from the chat link by copying the part after `https://teams.microsoft.com/l/chat/`. |
| Include members | Optional. Select `Yes` to include the list of members. Select `No` to exclude the list of members. |

## Output

| Output field | Description |
| --- | --- |
| @odata.context | The metadata URL property in the OData JSON response. It describes the structure, type, and location of the returned data. |
| Chat ID | The chat unique identifier. |
| Topic | The group chat topic name. The value is `null` if the group chat is unnamed or a 1:1 chat. |
| Created date | The date the chat was created. |
| Last updated date | The date the chat was last updated. |
| Chat type | The chat type. Types include `oneOnOne` and `group`. |
| Web URL | The direct link to the chat. |
| Tenant ID | The chat tenant unique identifier. |
| Is hidden for all members | A boolean response (`true` or `false`) that indicates whether the chat is hidden for all its members. |
| Online meeting info | Details about an online meeting, such as the `joinUrl`, `conferenceId`, and dial-in phone numbers. |

---
