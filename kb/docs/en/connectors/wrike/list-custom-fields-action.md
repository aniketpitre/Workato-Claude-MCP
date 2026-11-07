---
url: 'https://docs.workato.com/en/connectors/wrike/list-custom-fields-action.md'
description: >-
  The List custom fields batch action in the Wrike connector retrieves all
  custom fields and their IDs from the connected Wrike account.
---

# Wrike - List custom fields action (batch)

The **List custom fields** batch action retrieves all custom fields available in the connected Wrike account. You can use these field IDs in subsequent Wrike actions.

## Input

This action doesn't require any input.

## Output

| Output field | Description |
| --- | --- |
| Custom fields | List of retrieved custom fields. |
| Field ID | Unique identifier for the custom field. |
| Field name | Name of the custom field. |
| Field type | Data type of the custom field. |
| Space ID | Unique identifier of the space where the custom field is available. |
| Shared user IDs | List of user IDs that have access to this custom field. |
| Field settings | Additional configuration details for the custom field. |
| List size | Total number of custom fields retrieved in the batch. |
| List index | Position of the current custom field in the batch. |

---
