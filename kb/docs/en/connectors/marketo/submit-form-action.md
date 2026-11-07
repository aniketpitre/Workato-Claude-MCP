---
url: 'https://docs.workato.com/en/connectors/marketo/submit-form-action.md'
description: >-
  The Submit form action in the Marketo connector upserts a lead and generates a
  Fill out Form activity tied to a program or campaign.
---

# Marketo - Submit form action

This action submits a form in Marketo. It upserts a lead and generates a **Fill out Form** activity, which is associated with a program and/or campaign.

## Input

| Field | Description |
| --- | --- |
| Form ID | Select or provide the ID of the form to submit. Only the first 200 forms are displayed in the list. If you do not find your form in the list, set the toggle to **Provide form ID**. |
| Input | Expand to configure the list of input fields for the form. |
| Input source list | Input a list datapill from which lead forms are derived. Learn more about [list input](/en/features/list-management#list-batch-action). |
| Lead form fields | Expand to configure the object containing the lead form fields. |
| First name | Provide the first name of the lead. |
| Last name | Provide the last name of the lead. |
| Email address | Specify the email address of the lead. |
| Company name | Provide the name of the company associated with the lead. |
| Postal code | Enter the postal code associated with the lead. |
| Cookie | Provide the Munchkin cookie value. |
| Visitor data | Expand to configure the object containing the visitor data. |
| Page URL | Specify the web page that hosts the form. This field must be a fully formed URL. |
| Query string | Enter the web page query string. This field can contain one or more ampersand `&` delimited key-value pairs. For example, `Unsubscribed=yes`. |
| Lead client IP address | Provide the client IP address in IPv4 format. For example, `192.150.22.5`. |
| User agent string | Enter the user agent of the browser hosting the form. |

## Output

| Field | Description |
| --- | --- |
| Success | Indicates whether the operation was successful. |
| Request ID | The request ID of the operation. |
| Result | A list containing details of the lead that was upserted. |
| ID (result) | The ID of the lead. |
| Status (result) | The status of the operation for the lead. |
| Reasons (result) | An array of reasons if the operation failed for the lead. |
| Code (reasons) | The error code if the operation failed. |
| Message (reasons) | The error message if the operation failed. |

---
