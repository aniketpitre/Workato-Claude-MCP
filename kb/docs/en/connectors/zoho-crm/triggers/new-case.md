---
url: 'https://docs.workato.com/en/connectors/zoho-crm/triggers/new-case.md'
description: >-
  The New case trigger checks for new cases in Zoho CRM once every polling
  interval.
---

# Zoho CRM - New case trigger

The **New case** trigger checks for new cases in Zoho CRM once every polling interval.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |
| When first started, this recipe should pick up events from | Specify the date and time from which the recipe picks up trigger events. You can't change this value after running or testing the recipe. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the case. |
| Case number | The case identification number. |
| Case owner | The user to whom the case is assigned. |
| SM owner ID | The ID of the user who owns the case. |
| Deal name | The name of the related deal. |
| Deal ID | The unique identifier of the related deal. |
| SM creator ID | The ID of the user who created the case. |
| Phone | The phone number of the customer. |
| Email | The email address of the customer. |
| Created by | The user who created the case. |
| Description | Complete details about the case. |
| Internal comments | Follow-up notes about the case. |
| Add comment | Follow-up notes about the solution. |
| Number of comments | The total number of comments on the case. |
| Related to | The name of the contact who submitted the case. |
| Who ID | The unique identifier of the related contact. |
| Subject | The title of the case. |
| Case origin | The source from which the case has been generated. |
| Modified by (ID) | The ID of the user who last modified the case. |
| Modified by | The user who last modified the case. |
| Stage (deprecated) | The deprecated stage field. |
| Solution | The solution provided for the case. |
| Reported by | The name of the person who reported the case. |
| Status | The status of the case. |
| Priority | The priority of the case. |
| Type | The type of problem. |
| Case reason | The reason for the case. |
| Product ID | The unique identifier of the related product. |
| Product name | The name of the related product. |
| Account ID | The unique identifier of the related account. |
| Account name | The name of the related account. |
| Currency symbol | The currency symbol for monetary values. |
| Process flow | The process flow associated with the case. |
| Approved | Indicates if the case has been approved. |
| Editable | Indicates if the case record is editable. |
| Approval | The approval details for the case. |
| Delegate (Approval) | Indicates if approval can be delegated. |
| Approve (Approval) | Indicates if the case can be approved. |
| Reject (Approval) | Indicates if the case can be rejected. |
| Resubmit (Approval) | Indicates if the case can be resubmitted. |
| Created time | The timestamp when the case was created. |
| Modified time | The timestamp when the case was modified. |

---
