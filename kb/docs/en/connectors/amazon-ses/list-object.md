---
url: 'https://docs.workato.com/en/connectors/amazon-ses/list-object.md'
description: The List object action lists objects in Amazon SES.
---

# Amazon SES - List object action

The **List object** action lists objects in Amazon SES.

## Input

| Input field | Description |
| --- | --- |
| Object | **Required**. Select the object to list. You can choose from the following options: **Contact**: The end user who receives the email. You can add contacts to a contact list and associate with an SES topic.; **Contact list**: A list that contains contacts that subscribe to one or more specific topics.; **Email template**: An email template containing the subject line, HTML format, and text-body. The `/v2/email/templates` endpoint requires the `ListEmailTemplates` policy within Amazon SES. |
| Page size | Select the number of objects to be returned in a single page. |
| Next token | Type a token indicating additional records exist when outputs exceed the current page size. You can use the token in another **List object** action to retrieve the next page of records. |

## Output

Object specific output fields are dynamically generated based on the objects you select.

---
