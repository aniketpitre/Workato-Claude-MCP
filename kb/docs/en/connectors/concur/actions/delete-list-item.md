---
url: 'https://docs.workato.com/en/connectors/concur/actions/delete-list-item.md'
description: The Delete list item action deletes a list item in SAP Concur.
---

# SAP Concur - Delete list item action

The **Delete list item** action deletes a list item in SAP Concur. Use the [Get all lists batch action](/en/connectors/concur/actions/get-all-lists-batch) to retrieve the list ID and the [Get all list item batch action](/en/connectors/concur/actions/get-all-list-item-batch) to retrieve the list item ID.

## Input

| Input field | Description |
| --- | --- |
| List ID | Select the list containing the list item to delete or enter the unique ID of the list. |
| Item ID | Enter the unique ID of the list item to delete. |

## Output

This action doesn't return any output.

---

---
url: >-
  https://docs.workato.com/en/connectors/concur/actions/get-all-attendee-types-batch.md
description: >-
  The Get all attendee types batch action retrieves all attendee types from SAP
  Concur.
---

# SAP Concur - Get all attendee types action (batch)

The **Get all attendee types** batch action retrieves all attendee types from SAP Concur.

> **DEPRECATION NOTICE**
> 
> This action uses the SAP Concur v3 API, which is deprecated. Migrate to the [Get attendee types](/en/connectors/concur/actions/get-attendee-types-v4) action.

## Input

This action doesn't require any input configuration.

## Output

| Output field | Description |
| --- | --- |
| Attendee types | List of attendee type objects. |
| Code (Attendee types) | The type code indicator. |
| Name (Attendee types) | The attendee type name. |

---
