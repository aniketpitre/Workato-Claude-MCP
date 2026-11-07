---
url: >-
  https://docs.workato.com/en/connectors/email-custom/send-email-with-attachment-action.md
description: >-
  The Send email with attachment action enables you to send an email with
  attachments using the SMTP protocol in Email (Custom).
---

# Email (Custom) - Send email with attachment action

The **Send email with attachment** action sends an email with attachments using the **SMTP** protocol.

## Input

| Input field | Description |
| --- | --- |
| From | Specify the sender's email address. |
| To | Enter the recipients of the email. Accepts a list of email address objects. |
| Subject | Specify the subject of the email. |
| Body type | Choose the message body type. |
| Body | Enter the email message body to send. |
| CC | Enter the recipients to include as CC. Accepts a list of email addresses. CC recipients see all recipients in **To** and **CC**. |
| BCC | Enter the recipients to be BCC-ed. Recipients added to the list will not have their email addresses revealed to other recipients. Accepts a list of email address objects. |
| Attachments | Specify the attachments to include with the email. Accepts a list of attachment objects. |

## Output

| Output field | Description |
| --- | --- |
| Result | Indicates whether the action successfully sent the email or not. |
