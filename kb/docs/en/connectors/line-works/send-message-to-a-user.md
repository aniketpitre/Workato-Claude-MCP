---
url: 'https://docs.workato.com/en/connectors/line-works/send-message-to-a-user.md'
description: >-
  This action allows a bot to send a message to a specified user within LINE
  WORKS.
---

# LINE WORKS - Send message to a user action

The **Send message to a user** action uses a bot to send a message to a specified user within LINE WORKS.

![Line works Send message to a user action](/assets/line-works-send-message-to-a-user-action.QRlc8gjw.png)_LINE WORKS **Send message to a user** action_

## Input

| Input Field | Description |
| --- | --- |
| Bot ID | Enter the unique LINE WORKS identifier of the bot. |
| User ID | Enter the unique LINE WORKS identifier of the user. This field can use either the user ID or the login ID (email) of the user. |
| Message type | Enter the type of message the bot will send. Content fields dynamically load based on the selected message type. Refer to LINE WORKS' [Message Type](https://developers.worksmobile.com/jp/docs/bot-send-content) documentation for more information. |
| Content | Define the message content for the bot to send. The **Content** field varies based on the selected message type. |

## Output

The **Send message to a user** action's output fields change dynamically based on the selected message type. Map the relevant datapill from the data tree for downstream steps.

---
