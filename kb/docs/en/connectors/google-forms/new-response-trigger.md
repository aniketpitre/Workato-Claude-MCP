---
url: 'https://docs.workato.com/en/connectors/google-forms/new-response-trigger.md'
description: >-
  The New response trigger activates when a response is submitted to a Google
  Form.
---

# Google Forms - New response trigger

The **New response** trigger activates when a response is submitted to a Google Form.

## Input

| Input field | Description |
| --- | --- |
| Form ID | Provide the unique ID of the form. |

## Output

| Output field | Description |
| --- | --- |
| Response ID | A unique identifier assigned to the response submitted to the Google Form. |
| Create time | The timestamp when the response was created. |
| Last submitted time | The timestamp when the response was last submitted. |
| Respondent email | The email address of the respondent (if email collection is enabled). |
| Answers | The collection of responses provided by the respondent for each question. |
| Question ID | A unique identifier assigned to each question in the form. |
| Grade | The score assigned to a response if the form includes quiz grading. |
| Text answers | Responses given in text format for open-ended questions. |
| File upload answers | Files uploaded by the respondent (if the form includes file upload questions). |
| Total score | The final score achieved by the respondent if the form is set as a quiz with grading enabled. |

---

---
url: >-
  https://docs.workato.com/en/connectors/google-forms/get-record-details-action.md
description: >-
  The Get record details action retrieves the details of any record, such as a
  form response, using the record's ID.
---

# Google Forms - Get record details action

The **Get record details** action retrieves the details of any record, such as a form response, using the record's ID.

## Input

| Input field | Description |
| --- | --- |
| Form ID | Provide the unique ID of the form. |
| Response ID | Provide the ID of the form response you plan to retrieve. |

## Output

| Output field | Description |
| --- | --- |
| Form ID | A unique identifier assigned to the Google Form. |
| Response ID | A unique identifier assigned to each response submitted to the Google Form. |
| Create time | The timestamp when the response was created. |
| Last submitted time | The timestamp when the response was last submitted. |
| Respondent email | The email address of the respondent (if email collection is enabled). |
| Answers | The collection of responses provided by the respondent for each question. |
| Question ID | A unique identifier assigned to each question in the form. |
| Grade | The score assigned to a response if the form includes quiz grading. |
| Text answers | Responses given in text format for open-ended questions. |
| File upload answers | Files uploaded by the respondent (if the form includes file upload questions). |
| Total score | The final score achieved by the respondent if the form is set as a quiz with grading enabled. |

---
