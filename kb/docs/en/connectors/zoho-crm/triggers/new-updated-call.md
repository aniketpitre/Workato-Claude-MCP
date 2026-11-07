---
url: 'https://docs.workato.com/en/connectors/zoho-crm/triggers/new-updated-call.md'
description: >-
  The New/updated call trigger checks for new/updated calls in Zoho CRM once
  every polling interval.
---

# Zoho CRM - New/updated call trigger

The **New/updated call** trigger checks for new/updated calls in Zoho CRM once every polling interval.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |
| When first started, this recipe should pick up events from | Specify the date and time from which the recipe picks up trigger events. You can't change this value after running or testing the recipe. |

## Output

| Output field | Description |
| --- | --- |
| Subject | The subject of the call. |
| Call type | The type of call: `inbound` or `outbound`. |
| Call purpose | The purpose of the call. |
| Activity ID | The unique identifier of the call activity. |
| SM owner ID | The ID of the user who owns the call. |
| Contact ID | The unique identifier of the related contact. |
| Contact name | The name of the related contact. |
| Related to ID | The unique identifier of the related record. |
| SE module | The module of the related record. |
| Related to | The record to which the call is related. |
| Call details (deprecated) | The deprecated call details field. |
| Call start time | The date and time when the call started. |
| Call duration | The duration of the call. |
| Call status | The status of the call. |
| Reminder | The reminder settings for the call. |
| Description | Additional details about the call. |
| Billable | Indicates if the call is considered for billing. |
| Call result | The result of the call. |
| SM creator ID | The ID of the user who created the call. |
| Created by | The user who created the call record. |
| Modified by (ID) | The ID of the user who last modified the call. |
| Modified by | The user who last modified the call. |
| Currency symbol | The currency symbol for monetary values. |
| Process flow | The process flow associated with the call. |
| Approved | Indicates if the call has been approved. |
| Editable | Indicates if the call record is editable. |
| Approval | The approval details for the call. |
| Delegate (Approval) | Indicates if approval can be delegated. |
| Approve (Approval) | Indicates if the call can be approved. |
| Reject (Approval) | Indicates if the call can be rejected. |
| Resubmit (Approval) | Indicates if the call can be resubmitted. |
| SE module name | The name of the related module. |
| Calendar booking call | Indicates if the call was booked through calendar. |
| Created time | The timestamp when the call was created. |
| Modified time | The timestamp when the call was modified. |

---
