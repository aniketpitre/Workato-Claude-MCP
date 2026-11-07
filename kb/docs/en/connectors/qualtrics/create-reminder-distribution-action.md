---
url: >-
  https://docs.workato.com/en/connectors/qualtrics/create-reminder-distribution-action.md
description: >-
  Create a reminder distribution for a previously sent survey to send follow-up
  emails to non-respondents.
---

# Qualtrics - Create reminder distribution action

Use the **Create reminder distribution** action to create a reminder distribution for a previously sent survey. This action sends a follow-up email to recipients who haven't completed the survey from the original distribution.

## Input

| Input field | Description |
| --- | --- |
| Parent distribution ID | Provide the unique identifier of the original survey distribution to send a reminder for. |
| Library | Select the library containing your message template from the drop-down menu, or toggle to provide a custom Library ID. |
| Message | Select the message template to use for the reminder email from the drop-down menu, or toggle to provide a custom Message ID. |
| Header | Configure the email header information. |
| From email (Header) | Enter the sender's email address. |
| From name (Header) | Enter the sender's display name. |
| Reply to email (Header) | Enter the reply-to email address. |
| Subject (Header) | Enter the email subject line. |
| Send date | Enter the date and time when the reminder should be sent. |

## Output

| Output field | Description |
| --- | --- |
| Distribution ID | The unique identifier of the created reminder distribution. |
