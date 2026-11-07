---
url: 'https://docs.workato.com/en/connectors/typeform/get-form-details-action.md'
description: >-
  The Get form details action retrieves the details of a Typeform form by its
  ID.
---

# Typeform - Get form details action

The **Get form details** action retrieves the details of a Typeform form by its ID.

## Input

| Input field | Description |
| --- | --- |
| Form ID | Enter the ID of the form to retrieve. You can find this value in the form's URL. For example, the ID in `https://mysite.typeform.com/to/abc123` is `abc123`. |

## Output

| Output field | Description |
| --- | --- |
| ID | The form's unique identifier. |
| Title | The title of the form. |
| Language | The language the form is in. |
| Fields | Contains information about the form's fields. For example, `Properties`, `Layout`, and `Type`. |
| Hidden | Contains information about hidden fields. For example, `Value`. |
| Welcome screens | Contains information about the form's **Welcome** screens. For example, `Properties`, `Title`, and `Reference`. |
| Thankyou screens | Contains information about the form's **Thank you** screens. For example, `Properties`, `Title`, and `Reference`. |
| Logic | Contains information about the form's branching logic. For example, `Actions`, `Type`, and `Reference`. |
| Theme | The API endpoint URL for the form's theme. |
| Workspace | Contains information about the workspace containing the form. For example, `HREF`. |
| Links | Contains links relevant to the form. For example, `Display`. |
| Settings | Contains information about the form's settings. For example, `Language`, `Is public`, and `Google analytics`. |

---
