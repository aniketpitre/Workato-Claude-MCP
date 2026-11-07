---
url: 'https://docs.workato.com/en/connectors/typeform/new-form-response-trigger.md'
description: >-
  The New form response trigger monitors Typeform for form responses in
  real-time.
---

# Typeform - New form response trigger (real-time)

The **New form response** trigger monitors Typeform for form responses in real-time.

## Input

| Input field | Description |
| --- | --- |
| Workspace name | Select the workspace that contains the form to monitor. |
| Form name | Select the form to monitor. |
| Hidden fields | Enter the JSON structure of hidden fields to retrieve. |

## Output

| Output field | Description |
| --- | --- |
| Form ID | The form's unique identifier. |
| Token | The response's unique identifier. |
| Landed at | The date and time when the respondent opened the form. |
| Submitted at | The date and time when the respondent submitted the form. |
| Hidden | Contains the hidden field values passed to the form. |
| Definition | Contains information about the form's structure. For example, `Fields` and `Endings`. |
| Answers | Contains the respondent's answers to the form's questions. |
| Ending | Contains information about the ending screen shown to the respondent. For example, `Title` and `Properties`. |

---
