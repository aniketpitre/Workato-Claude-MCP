---
url: 'https://docs.workato.com/en/connectors/telegram/get-chat-member-action.md'
description: >-
  Check a Telegram chat member's role and permissions, such as admin rights,
  before granting bot access to a feature.
---

# Telegram - Get chat member action

The **Get chat member** action returns a chat member's status and permissions in Telegram. Use this action to check a member's permissions before allowing access to features.

## Input

| Input field | Description |
| --- | --- |
| Chat ID | Enter the unique identifier for the target chat or the username of the target supergroup or channel, for example `@channelusername`. |
| User ID | Enter the unique identifier of the target user. |

## Output

This action's output fields vary based on the member's status, such as `creator`, `administrator`, `member`, `restricted`, `left`, or `kicked`. The following table contains frequently returned fields. Refer to the Telegram Bot API [ChatMember](https://core.telegram.org/bots/api#chatmember) documentation for the more information on available output fields.

| Output field | Description |
| --- | --- |
| Status | The member's status in the chat. |
| User | The user's ID, name, and username. |
| Custom title | The member's custom title. Only for owners and administrators. |
| Is anonymous | A boolean response (`true` or `false`) that indicates if the member's presence in the chat is hidden. Only for owners and administrators. |
| Can delete messages | A boolean response (`true` or `false`) that indicates if the administrator can delete messages from other users. |
| Can invite users | A boolean response (`true` or `false`) that indicates if the member can invite new users to the chat. |
| Can pin messages | A boolean response (`true` or `false`) that indicates if the member can pin messages. |
| Is member | A boolean response (`true` or `false`) that indicates if the user is a member of the chat. Only for restricted members. |
| Until date | The Unix timestamp the member's restriction or ban is lifted, if applicable. |

---
