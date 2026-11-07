---
url: 'https://docs.workato.com/en/connectors/airtable/new-record-trigger.md'
description: >-
  The New record trigger in the Airtable connector fires when a new record is
  detected in a table you monitor, checking every five minutes by default.
---

# Airtable - New record trigger

The New record trigger runs when a new record is detected in Airtable. The trigger checks for new records every five minutes by default.

## Input

| Input field | Description |
| --- | --- |
| Base | The database you plan to monitor for new records. |
| Table | The name or ID of the table you plan to monitor for new records. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the record created. For example: `rec2NmM3zbe5QaZhob`. |
| Created time | The timestamp of when the record was created. For example: `2024-01-30T17:33:54.000000+00:00`. |
| Name | The name of the record created. |

---
