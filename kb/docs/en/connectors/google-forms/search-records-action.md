---
url: 'https://docs.workato.com/en/connectors/google-forms/search-records-action.md'
description: The Search records action returns results that match your search criteria.
---

# Google Forms - Search records action

The **Search records** action returns results that match your search criteria.

## Input

| Input field | Description |
| --- | --- |
| Form ID | Provide the unique ID of the form. |
| Filter | Provide the supported [filters](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms.responses/list). |
| Page size | Specify the number of records to return in the response. |
| Page token | Provide the page token from a previous list response. If this field is set, the form and filter values must match those of the original request. |

## Output

| Output field | Description |
| --- | --- |
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
| Next page token | A token used to retrieve the next set of responses. To access the next page, use this token as the page token in a subsequent request. |

---
