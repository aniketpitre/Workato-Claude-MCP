---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/new-email-trigger.md
description: The New email trigger activates when a new email is received.
---

# Microsoft Graph API - New email trigger

The **New email** trigger activates when a new email is received.

## Input

This trigger doesn’t have any input fields.

## Output

| Output field | Description |
| --- | --- |
| OData ETag | Entity tag for concurrency control. |
| Message ID | Unique identifier for the message. |
| Created DateTime | Date and time when the message was created. |
| Last Modified DateTime | Date and time when the message was last modified. |
| Change Key | Identifies a specific version of the message. |
| Categories | List of categories associated with the message. |
| Received DateTime | Date and time when the message was received. |
| Sent DateTime | Date and time when the message was sent. |
| Has Attachments | Indicates whether the message has attachments (`Yes`/`No`). |
| Internet Message ID | Unique identifier for the message in internet format. |
| Subject | Subject of the message. |
| Body Preview | Preview text of the message body. |
| Importance | Importance level of the message. For example, `Low`, `Normal`, `High`. |
| Parent Folder ID | ID of the parent folder containing the message. |
| Conversation ID | ID of the conversation thread. |
| Conversation Index | Position of the message in the conversation thread. |
| Delivery Receipt Requested | Indicates if a delivery receipt was requested (`Yes`/`No`). |
| Read Receipt Requested | Indicates if a read receipt was requested (`Yes`/`No`). |
| Is Read | Indicates if the message has been read (`Yes`/`No`). |
| Is Draft | Indicates if the message is a draft (`Yes`/`No`). |
| Web Link | URL to access the message in a web browser. |
| Inference Classification | Classification of the message. For example, `Focused`, `Other`. |
| Body Content Type | Type of content in the message body. For example, `Text`, `HTML`. |
| Body Content | Actual content of the message body. |
| Sender Name | Name of the sender. |
| Sender Email Address | Email address of the sender. |
| From Name | Name of the person who sent the message. |
| From Email Address | Email address of the sender. |
| To Recipient Name | Name of the recipient. |
| To Recipient Email Address | Email address of the recipient. |
| CC Recipients | List of CC recipients. |
| BCC Recipients | List of BCC recipients. |
| Reply To | List of reply-to email addresses. |
| Flag Status | Status of the message flag. For example, `Not Flagged`, `Complete`, `Flagged`. |
