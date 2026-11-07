---
url: >-
  https://docs.workato.com/en/connectors/qualtrics/distribute-survey-via-email-action.md
description: >-
  Send a survey to recipients through email using a message template and
  specified recipients.
---

# Qualtrics - Distribute survey via email action

Use the **Distribute survey via email** action to send a survey to recipients through email. This action creates a distribution and sends the survey based on the message template and recipients you specify.

## Input

| Input field | Description |
| --- | --- |
| Library | Select the library containing your message template from the drop-down menu, or toggle to provide a custom Library ID. |
| Message | Select the message template to use for the email from the drop-down menu, or toggle to provide a custom Message ID. |
| Recipients | Configure the recipients for the survey. |
| Mailing list ID (Recipients) | Provide the ID of a mailing list to send the survey to. Alternatively, set Transaction batch ID. Refer to [Finding Qualtrics IDs](https://www.qualtrics.com/support/integrations/api-integration/finding-qualtrics-ids) for more information. |
| Transaction batch ID (Recipients) | Provide the ID of a transaction batch. Alternatively, set the Mailing list ID. |
| Contact ID (Recipients) | Provide a contact lookup ID for individual distribution. |
| Header | Configure the email header information. |
| From email (Header) | Enter the sender's email address. |
| From name (Header) | Enter the sender's display name. |
| Reply to email (Header) | Enter the reply-to email address. |
| Subject (Header) | Enter the email subject line. |
| Survey link | Configure the survey link settings. |
| Survey (Survey link) | Select the survey to distribute from the drop-down menu, or toggle to provide a custom Survey ID. |
| Expiration date (Survey link) | Enter the date and time when the survey link expires. |
| Type (Survey link) | Select the type of survey link (Individual, Multiple, or Anonymous). |
| Send date | Enter the date and time when the survey should be sent. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the created distribution. Use this ID to create reminder distributions or track the distribution status. |
