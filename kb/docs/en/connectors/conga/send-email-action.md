---
url: 'https://docs.workato.com/en/connectors/conga/send-email-action.md'
description: The Send email action sends an email in Conga.
---

# Conga - Send email action

The **Send email** action sends an email in Conga.

## Input

| Input field | Description |
| --- | --- |
| From | Enter the email address of the sender. Fields include **Address** and **Display name**. |
| From email option | Enter the sender's email address or configure the email options, such as `LoggedInUser`, `OrgWideEmail`, or `Emailprofile`. |
| To | Enter the recipient email addresses. Fields include `To source list`, `Address`, and `Display name`. |
| Subject | Enter the email subject line. |
| Plain text body | Enter the body of the email in plain text. |
| Html body | Enter the HTML formatting of the email body. |

## Output

| Output field | Description |
| --- | --- |
| Success | A boolean response that indicates if the action was successful. |
| Data | Email status code: A code indicating the status of the sent email, such as `OK`, `BadRequest`, `Unauthorized`, and more.; Message: A message providing more information about the success of the send email action. |
| Status code | A code indicating the status of the action, such as `OK`, `BadRequest`, `Unauthorized`, and more. |

---
