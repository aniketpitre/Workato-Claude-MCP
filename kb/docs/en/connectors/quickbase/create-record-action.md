---
url: 'https://docs.workato.com/en/connectors/quickbase/create-record-action.md'
description: >-
  The Create record action in the Quickbase connector lets you create a new
  record in a specified table by mapping values to its fields.
---

# Quickbase - Create record action

This action creates a new record in a specified Quickbase table.

## Input

| Field | Description |
| --- | --- |
| Application | Select an application in your Quickbase account. |
| Application token | This field is required if this application has been configured to require tokens for data access. You can obtain the token from the application's **Settings > App properties > Manage Application Token**. |
| Table | Select the table where you plan to create the record. |
| Table field list | Select which columns in your Quickbase table to do the mappings. Maximum 150 columns. |
| Field list | Select the fields you plan to use in the **Table field** list here. Workato can support a maximum of 150 fields from a Quickbase table. If your table has more than 150 fields, select the fields you plan to use in the Table field list here, and then add them with Show/hide optional fields at the bottom of this form. |

## Output

| Field | Description |
| --- | --- |
| Record ID | The ID of the created record. |

---
