---
url: >-
  https://docs.workato.com/en/connectors/email-custom-opa/send-email-with-attachment-action.md
description: >-
  Send an email with an attachment using SMTP through the Email (Custom) OPA
  on-prem agent extension.
---

# Email (Custom) OPA - Send email with attachment action

The **Send email with attachment** action sends an email with one or more attachments using the **SMTP** protocol through your on-prem agent extension.

## Input

| Input field | Description |
| --- | --- |
| From | Enter the sender's email address. |
| To | Enter the recipients of the email. |
| Email (To) | Enter the recipient's email address. |
| CC | Optional. Enter the recipients to include as CC. CC recipients see all recipients in **To** and **CC**. |
| BCC | Optional. Enter the recipients to include as BCC. BCC recipients are hidden from other recipients. |
| Subject | Enter the subject of the email. |
| Body type | Select whether the email body contains plain text or HTML content. Defaults to **Plain text**. |
| Body | Enter the email body content. Use HTML tags if **Body type** is **HTML**. |
| Attachments | Optional. Enter the files to attach to the email. |
| File name (Attachments) | Enter the attachment's file name. |
| File content (Attachments) | Enter the attachment's content. File contents must be base64 encoded. |

## Output

| Output field | Description |
| --- | --- |
| Result | A message confirming the email was sent, for example `Email with attachment(s) sent successfully`. |
