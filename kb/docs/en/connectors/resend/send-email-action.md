---
url: 'https://docs.workato.com/en/connectors/resend/send-email-action.md'
description: Send an email to one or more recipients in Resend.
---

# Resend - Send email action

The **Send email** action sends an email to one or more recipients in Resend. Provide an **HTML** or **Text** body, or use a published template. Use the [Send emails (batch)](/en/connectors/resend/send-emails-action-batch) action to send up to 100 emails in one request instead.

## Input

The following are a representative set of input fields. Refer to the Resend [API](https://resend.com/docs/api-reference/emails/send-email) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| From | Enter the sender's email address. |
| To | Enter the recipients' email addresses as a list. For example, `["a@example.com", "b@example.com"]`. You can add up to 50 recipients. |
| Subject | Enter the subject of the email. |
| HTML | Optional. Enter the HTML body of the email. You can't use this field with **Template**. |
| Text | Optional. Enter the plain text body of the email. You can't use this field with **Template**. Leave blank to have Resend generate it from the **HTML** body. Enter an empty string to disable generation. |
| CC | Optional. Enter the CC recipients' email addresses as a list. Leave blank to send no CC copies. |
| BCC | Optional. Enter the BCC recipients' email addresses as a list. Leave blank to send no BCC copies. |
| Scheduled at | Optional. Select the date and time to send the email. Leave blank to send the email immediately. |
| Attachments | Optional. Add files to attach to the email. Attachments can't exceed 40 MB per email after Base64 encoding. Leave blank to send no attachments. |
| Template | Optional. Enter the ID of a published template and its variables. You can't use this field with **HTML** or **Text**. The **From** and **Subject** fields override the template defaults. Leave blank to send the email without a template. |

## Output

| Output field | Description |
| --- | --- |
| Email ID | The unique ID of the email. |

---
