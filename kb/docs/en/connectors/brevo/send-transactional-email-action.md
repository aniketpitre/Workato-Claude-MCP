---
url: >-
  https://docs.workato.com/en/connectors/brevo/send-transactional-email-action.md
description: >-
  The Send transaction email action sends a transactional email with static or
  dynamic content in Brevo.
---

# Brevo - Send transaction email action

The **Send transaction email** action sends a transactional email with static or dynamic content in Brevo. Transactional emails are automated, non-promotional messages triggered by user actions.

## Input

| Input field | Description |
| --- | --- |
| Template ID | Enter the template identifier for the email. HTML and text content are ignored if you provide a template ID. |
| Sender | Enter information about the sender. Required when you don't provide a template ID. |
| Message versions | Enter an array of message version objects for customized email variants. Maximum total recipients per API request is 2000. Maximum recipients per message version is 99. Individual parameter objects must not exceed 100 KB. Cumulative parameters across all versions must not exceed 1000 KB. |
| To | Enter an array of email recipients. Required when **Message versions** is not provided. Ignored when **Message versions** is provided. |
| CC | Enter an array of CC email recipients. |
| BCC | Enter an array of BCC gmail recipients. |
| Reply to | Enter the email address and display name recipients can reply to. |
| Subject | Enter a subject line for the email. |
| HTML content | Enter the HTML body of the email. Ignored when you provide a **Template ID**. |
| Text content | Enter body content of the email in plain text. Ignored when you provide a **Template ID**. |
| Template parameters | Enter key-value pairs used for variable substitution in the template. Applies only when you use the `New Template Language` format. |
| Attachments | Enter an array of email attachments. Each attachment requires an absolute URL or base64-encoded content and the attachment name. |
| Custom headers | Enter any custom headers for your email. Headers must use title case. |
| Tags | Enter any tags to assign to the email. |
| Scheduled at | Enter the date and time to send the email. |
| Batch ID | Enter a batch identifier to group related transactional emails. |

## Output

| Output field | Description |
| --- | --- |
| Message ID | The ID of the email message used to track delivery. |
| Message IDs | Multiple IDs of email messages used to track delivery. |
