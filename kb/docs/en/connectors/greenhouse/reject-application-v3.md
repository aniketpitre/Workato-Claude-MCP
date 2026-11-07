---
url: 'https://docs.workato.com/en/connectors/greenhouse/reject-application-v3.md'
description: >-
  The Reject application (v3) action rejects an application in Greenhouse using
  the v3 API.
---

# Greenhouse - Reject application (v3) action

The **Reject application (v3)** action rejects an application in Greenhouse using the v3 API.

This action is available for OAuth 2.0 connections only.

## Input

| Input field | Description |
| --- | --- |
| Application ID | Enter the ID of the application to reject. |
| Rejection reason ID | Select the reason for rejecting the application. |
| Notes | Enter notes explaining why the application is rejected. |
| Send email at | Specify the date and time to send the rejection email. |
| Email template ID | Select the email template to use for the rejection email. |
| Email from user ID | Enter the user ID to use as the sender for the rejection email. |
| Custom fields | Provide additional custom fields for the rejection. |

## Output

| Output field | Description |
| --- | --- |
| Application ID | ID of the application. |
| Rejected | Indicates whether the application was successfully rejected. |

---
