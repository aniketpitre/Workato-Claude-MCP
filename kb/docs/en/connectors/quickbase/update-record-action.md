---
url: 'https://docs.workato.com/en/connectors/quickbase/update-record-action.md'
description: >-
  The Update record action in the Quickbase connector lets you update an
  existing record in a specified table using its record ID.
---

# Quickbase - Update record action

This action updates an existing record in a specified Quickbase table.

## Input

| Field | Description |
| --- | --- |
| Application | Select an application in your Quickbase account. |
| Application token | This is required if this application has been configured to require tokens for data access. You can obtain the token from the application's **Settings > App properties > Manage Application Token**. |
| Table | Select the table where you plan to update the record. You can either select the table from the drop-down, or provide the table ID. |
| Table field list | Select which columns in your Quickbase table to map to. Workato can support a maximum of 150 fields from a Quickbase table. If your table has more than 150 columns, select the fields you plan to use. These fields are dynamic and change based on the **Table** you select. |
| Record ID | The ID of the record to update. |

## Output

| Field | Description |
| --- | --- |
| Record ID | The ID of the updated record. |

---
