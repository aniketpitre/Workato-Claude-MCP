---
url: 'https://docs.workato.com/en/connectors/qualtrics/create-mailing-list-action.md'
description: >-
  Create a new mailing list in your Qualtrics library to organize and manage
  groups of contacts for survey distributions.
---

# Qualtrics - Create mailing list action

Use the **Create mailing list** action to create a new mailing list in your Qualtrics library. Mailing lists are used to organize and manage groups of contacts for survey distributions.

## Input

| Input field | Description |
| --- | --- |
| Library | Select the library to create the mailing list in from the drop-down menu, or toggle to provide a custom Library ID. |
| Name | Provide a name for the mailing list. |
| Category | Provide a category to associate with the mailing list. This helps organize mailing lists within your library. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the created mailing list. You can use this ID in other actions such as distributing surveys. |

---

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

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/qualtrics/get-mailing-list-details-action.md
description: Retrieve the details of an existing mailing list using its mailing list ID.
---

# Qualtrics - Get mailing list details action

Use the **Get mailing list details** action to retrieve the details of an existing mailing list through its mailing list ID.

## Input

| Input field | Description |
| --- | --- |
| Mailing list ID | Provide the unique identifier of the mailing list to retrieve. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the mailing list. |
| Library ID | The identifier of the library containing the mailing list. |
| Name | The name of the mailing list. |
| Category | The category associated with the mailing list, used for organization. |

---

---
url: >-
  https://docs.workato.com/en/connectors/qualtrics/get-response-details-action.md
description: Retrieve the complete details of a survey response using its response ID.
---

# Qualtrics - Get response details action

Use the **Get response details** action to retrieve the complete details of a survey response through its response ID.

## Input

| Input field | Description |
| --- | --- |
| Survey | Select the survey from the drop-down list, or toggle to provide a custom Survey ID. |
| Response ID | Provide the unique identifier of the response to retrieve. |

## Output

| Output field | Description |
| --- | --- |
| Response ID | The unique identifier of the survey response. |
| Values | An object containing all response values. |
| Start date (Values) | When the respondent started the survey. |
| End date (Values) | When the respondent completed the survey. |
| Status (Values) | The completion status code. |
| IP address (Values) | The respondent's IP address. |
| Progress (Values) | Completion percentage (0-100). |
| Duration (Values) | Time spent on the survey in seconds. |
| Finished (Values) | Whether the survey was completed (1 for finished, 0 for unfinished). |
| Recorded date (Values) | When the response was recorded. |
| Location latitude (Values) | Geographic latitude of the respondent. |
| Location longitude (Values) | Geographic longitude of the respondent. |
| Distribution channel (Values) | How the survey was distributed. |
| User language (Values) | The respondent's language. |
| Question responses (Values) | Values for each question in the survey. |
| Labels | An object containing human-readable labels for response values. |
| Displayed fields | An array of field names that were displayed to the respondent. |
| Displayed values | An object containing the displayed values for fields. |

---
