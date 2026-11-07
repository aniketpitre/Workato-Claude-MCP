---
url: 'https://docs.workato.com/en/connectors/marketo/add-leads-to-list-action.md'
description: >-
  The Add leads to lead list action in the Marketo connector lets you add a
  batch of leads to a list by list ID or name in your instance.
---

# Marketo - Add leads to lead list action (batch)

This action adds leads to a lead list in Marketo.

## Input

| Field | Description |
| --- | --- |
| List ID / List name | Enter the ID or name of the list to add leads to. |
| Lead IDs | Expand to configure the lead IDs to be added to the list. |
| Lead IDs source list (lead IDs) | Input a list datapill from which lead IDs are derived. Learn more about [list input](/en/features/list-management#list-batch-action). |
| Lead ID (lead IDs) | Enter the unique identifier of the lead. |

## Output

| Field | Description |
| --- | --- |
| Result | A list containing information about the result of the action. |
| ID (result) | The unique identifier of the lead. |
| Status (result) | The status of the operation for the lead. |
| Reasons | An array of reasons if the operation failed for the lead. |
| Code (reasons) | The error code if the operation failed. |
| Message (reasons) | The error message if the operation failed. |

---
