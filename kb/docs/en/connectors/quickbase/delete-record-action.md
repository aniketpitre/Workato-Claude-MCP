---
url: 'https://docs.workato.com/en/connectors/quickbase/delete-record-action.md'
description: >-
  The Delete record action in the Quickbase connector lets you delete a record
  from a specified table using its record ID.
---

# Quickbase - Delete record action

This action deletes a record in a specified Quickbase table using its record ID.

## Input

| Field | Description |
| --- | --- |
| Application | Select an application in your Quickbase account. |
| Application token | This field is required if this application has been configured to require tokens for data access. You can obtain the token from the application's **Settings > App properties > Manage Application Token**. |
| Table | Select the table that contains the record you plan to delete. You can either select the table from the drop-down, or provide the table ID. |
| Record ID | The ID of the record to delete. |

## Output

| Field | Description |
| --- | --- |
| Record ID | The ID of the deleted record. |

---
