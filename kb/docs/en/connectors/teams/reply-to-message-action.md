---
url: 'https://docs.workato.com/en/connectors/teams/reply-to-message-action.md'
description: The Reply to message action replies to a message in Microsoft Teams.
---

# Microsoft Teams - Reply to message action

The **Reply to message** action replies to a message in an existing channel message thread in Microsoft Teams. Only channel messages support threaded replies. This action requires authorization code grant authentication. It doesn't support client credentials authentication.

## Input

| Input field | Description |
| --- | --- |
| Team name (or team ID) | Enter the team name or ID. Only teams you're a member of are options. You can retrieve the team ID from the **List teams** action output. |
| Channel name (or channel ID) | Enter the channel name or ID. You can retrieve this value from the **List channels** action output. |
| Message ID | Enter the message ID. You can retrieve this value from the **Get messages** or **Search messages** action. |
| Message content | Enter the message body. Supports plain text or HTML depending on the **Content type** field. |
| Content type | Optional. Enter the type of message body content. Types include `HTML` and `Text`. Defaults to `Text`. |

## Output

| Output field | Description |
| --- | --- |
| Reply message ID | The unique identifier for the reply message. |
| Reply to ID | The unique identifier of the parent message that was replied to. |
| Body | Details about the message body. Includes the `content` (text/HTML) and `contentType` of the reply. |
| From | The message sender details. Details include `Email address` and `Name`. |
| Created date time | The date and time the message was sent. |
| Last modified date time | The date and time the message was last modified. |

---
