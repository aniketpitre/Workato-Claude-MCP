---
url: 'https://docs.workato.com/en/connectors/resend/get-record-action.md'
description: 'Retrieve a record, such as a sent email, from Resend by its ID.'
---

# Resend - Get record action

The **Get record** action retrieves a sent or scheduled email from Resend by its ID.

## Input

| Input field | Description |
| --- | --- |
| Object type | Select the type of record to retrieve. **Email** is the only option. |
| Email ID | Enter the unique ID of the email to retrieve. |

## Output

The following are a representative set of output fields. Refer to the Resend [API](https://resend.com/docs/api-reference/emails/retrieve-email) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Object | The type of record retrieved. For example, `email`. |
| Email ID | The unique ID of the email. |
| To | The recipients' email addresses. |
| From | The sender's email address. |
| Created at | The date and time the email was created. |
| Subject | The subject of the email. |
| HTML | The HTML body of the email. |
| Text | The plain text body of the email. |
| Last event | The most recent delivery event for the email. For example, `delivered`. |
| Scheduled at | The date and time Resend sends the scheduled email. This field is blank for emails you didn't schedule. |

---
