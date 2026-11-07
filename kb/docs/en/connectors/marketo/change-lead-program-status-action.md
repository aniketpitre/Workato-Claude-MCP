---
url: >-
  https://docs.workato.com/en/connectors/marketo/change-lead-program-status-action.md
description: >-
  The Change lead program status action in the Marketo connector lets you change
  the program status of a batch of leads in your instance.
---

# Marketo - Change lead program status action (batch)

This action changes the program status of leads in Marketo.

## Input

| Field | Description |
| --- | --- |
| Program ID | Enter the unique identifier of the program where the status is changed. |
| Status | Specify the new status to assign to the leads. |
| Leads | Expand this field to configure the leads for the program status change. |
| Leads source list (leads) | Input a list datapill from which the leads are derived. Learn more about [list input](/en/features/list-management#list-batch-action). |
| Lead ID (leads) | Provide the unique identifier of a lead record. |

## Output

| Field | Description |
| --- | --- |
| Result | An array of results for individual records in the operation. |
| ID (result) | The ID of the lead. |
| Status (result) | The new status of the lead. |
