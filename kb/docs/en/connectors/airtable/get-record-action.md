---
url: 'https://docs.workato.com/en/connectors/airtable/get-record-action.md'
description: >-
  The Get record action in the Airtable connector lets you fetch a single record
  from a base and table by its record ID.
---

# Airtable - Get record action

The Get record action fetches an Airtable record you specify.

## Input

| Input field | Description |
| --- | --- |
| Base | The database from which you plan to fetch the record. |
| Table | The name or ID of the table from which you plan to fetch the record. |
| Record ID | The ID of the record you plan to fetch. You can find the record ID in Airtable by clicking the record and copying the ID from the record URL. The record ID is located at the end of the URL. For example, if the URL is `airtable.com/app123456789/tbl987654321/` `viw87654321/recJFjhekzhN0VWxB`, your record ID is `recJFjhekzhN0VWxB`. |

## Output

The output for this action is returned in a table with the following columns:

| Output field | Description |
| --- | --- |
| ID | The ID of the record fetched. For example: `recJFjhekzhN0VWxB`. |
| Created time | The timestamp of when the record was fetched. For example: `2024-01-30T17:33:54.000000+00:00`. |
| Name | The name of the record fetched. |

---
