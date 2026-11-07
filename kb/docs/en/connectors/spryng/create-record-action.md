---
url: 'https://docs.workato.com/en/connectors/spryng/create-record-action.md'
description: The Create record action creates a record in Spryng.
---

# Spryng - Create record action

The **Create record** action creates a record in Spryng.

## Input

Input fields load dynamically based on the object you select. For example, the following input fields are available if you select **Message**:

| Input field | Description |
| --- | --- |
| Object type | Select the Spryng object to create. Options include `Message` and `Subaccount`. |
| Encoding | Select or enter the type of encoding to use, such as `Auto`, `Plain (GSM 03.38)`, or `Unicode`. |
| Message body | Enter the content of the SMS message. |
| Route | Enter a custom route ID or `business` to use the default business route. |
| Originator | Enter the name of the sender. |
| Recipients | Enter the ID of the recipients of the message. |
| Reference | Enter the client reference for the message. |

## Output

Input fields load dynamically based on the object you select. For example, the following input fields are available if you select **Message**:

| Output field | Description |
| --- | --- |
| Message ID | The unique ID of the created message. |
| Encoding type | The encoding type of the created message. |
| Originator | The name of the sender of the created message. |
| Body | The body of the created message. |
| Reference | The reference linked to the created message. |
| Credits | The balance of credits in the account associated with the created message. |
| Scheduled at | The time when the message should be sent. |
| Canceled at | The time when the message was canceled. |
| Created at | The time when the message was created. |
| Updated at | The time when the message was updated. |
| Links | Links included in the created message. |

---
