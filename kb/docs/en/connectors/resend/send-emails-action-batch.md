---
url: 'https://docs.workato.com/en/connectors/resend/send-emails-action-batch.md'
description: >-
  Send up to 100 emails in one Resend API request, with per-email recipients,
  templates, and tags.
---

# Resend - Send emails action (batch)

The **Send emails (batch)** action sends up to 100 emails in one request in Resend. Provide an **HTML** or **Text** body, or use a published template. This action doesn't support attachments.

## Input

The following are a representative set of input fields. Refer to the Resend [API](https://resend.com/docs/api-reference/emails/send-batch-emails) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Emails | Add between 1 and 100 emails to send. |
| From (Emails) | Enter the sender's email address. |
| To (Emails) | Enter the recipients' email addresses as a list. For example, `["a@example.com", "b@example.com"]`. You can add up to 50 recipients. |
| Subject (Emails) | Enter the subject of the email. |
| HTML (Emails) | Optional. Enter the HTML body of the email. You can't use this field with **Template**. |
| Text (Emails) | Optional. Enter the plain text body of the email. You can't use this field with **Template**. Leave blank to have Resend generate it from the **HTML** body. Enter an empty string to disable generation. |
| CC (Emails) | Optional. Enter the CC recipients' email addresses as a list. Leave blank to send no CC copies. |
| Tags (Emails) | Optional. Add tracking tags to the email. Leave blank to send the email without tags. |
| Template (Emails) | Optional. Enter the ID of a published template and its variables. You can't use this field with **HTML** or **Text**. The **From** and **Subject** fields override the template defaults. Leave blank to send the email without a template. |
| Idempotency key | Optional. Enter a unique key to prevent duplicate emails if you retry the request. Enter up to 256 characters. Keys expire after 24 hours. Leave blank to send the request without an idempotency key. |

## Output

| Output field | Description |
| --- | --- |
| Data | The list of emails sent. |
| Email ID (Data) | The unique ID of the email. |

---
