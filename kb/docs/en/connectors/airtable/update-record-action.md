---
url: 'https://docs.workato.com/en/connectors/airtable/update-record-action.md'
description: >-
  The Update record action in the Airtable connector lets you update a specific
  record in a base and table by its record ID.
---

# Airtable - Update record action

The Update record action creates a record in the table you select.

## Input

| Input field | Description |
| --- | --- |
| Base | The database in which the record you plan to update is located. |
| Table | The name or ID of the table in which the record you plan to update is located. |
| Record ID | The ID of the record you plan to update. You can find the record ID in Airtable by clicking the record and copying the ID from the record URL. The record ID is located at the end of the URL. For example, if the URL is `airtable.com/app123456789/tbl987654321/` `viw87654321/recJFjhekzhN0VWxB`, your record ID is `recJFjhekzhN0VWxB`. |
| Name | The name of the record you plan to update. |
| Typecast | This parameter determines whether the Airtable API performs an automatic data conversion from string values or not. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the record updated. For example: `recJFjhekzhN0VWxB`. |
| Created time | The timestamp of when the record was updated. For example: `2024-01-30T17:33:54.000000+00:00`. |
| Name | The name of the record updated. |

---
