---
url: 'https://docs.workato.com/en/connectors/airtable/delete-record-action.md'
description: >-
  The Delete record action in the Airtable connector lets you delete a specific
  record from a base and table by its record ID.
---

# Airtable - Delete record action

The Delete record action deletes an Airtable record you specify.

## Input

| Input field | Description |
| --- | --- |
| Base | The database in which the record you plan to delete is located. |
| Table | The name or ID of the table in which the record you plan to delete is located. |
| Record ID | The ID of the record you plan to delete. You can find the record ID in Airtable by clicking the record and copying the ID from the record URL. The record ID is located at the end of the URL. For example, if the URL is `airtable.com/app123456789/tbl987654321/` `viw87654321/recJFjhekzhN0VWxB`, your record ID is `recJFjhekzhN0VWxB`. |

## Output

| Output field | Description |
| --- | --- |
| Deleted | Indicates whether the record was deleted or not. This value is `true` if the record was deleted successfully and `false` if the record was not deleted. |
| ID | The ID of the record deleted. For example: `recJFjhekzhN0VWxB`. |

---
