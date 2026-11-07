---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/batch-upsert-standard-objects.md
description: >-
  The Batch upsert standard objects action upserts standard objects in batches
  in Zoho CRM.
---

# Zoho CRM - Batch upsert standard objects action

The **Batch upsert standard objects** action upserts standard objects in batches in Zoho CRM.

## Input

| Input field | Description |
| --- | --- |
| Module name | Select the standard module for the objects. |
| Data | Provide the data for the objects to upsert. |
| Data source list (Data) | Provide the source list for the data. |
| Duplicate check fields (Data) | Select the fields to check for duplicates. |

Additional fields appear based on the module you select.

## Output

The output is a list of the objects that were upserted in Zoho CRM.

| Output field | Description |
| --- | --- |
| {Objects} | A list of objects that were upserted in Zoho CRM. |
| {Object} ID | The unique identifier of the object. |
| Created time | The timestamp when the object was created. |
| Modified time | The timestamp when the object was modified. |
| Created by | The user who created the object. |
| Modified by | The user who last modified the object. |
| ID | The unique identifier of the object. |
