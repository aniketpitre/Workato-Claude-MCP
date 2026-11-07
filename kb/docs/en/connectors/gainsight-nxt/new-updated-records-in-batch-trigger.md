---
url: >-
  https://docs.workato.com/en/connectors/gainsight-nxt/new-updated-records-in-batch-trigger.md
description: >-
  The New/updated records in batch trigger monitors Gainsight NXT for records
  created or updated since the last time the recipe triggered.
---

# Gainsight NXT - New/updated records in batch trigger

The **New/updated records in batch** trigger monitors `Gainsight NXT` for records created or updated since the last time the recipe triggered. The maximum batch size is 1000.

## Input

| Input field | Description |
| --- | --- |
| Object type | Use the drop-down menu to select the object to monitor for new or updated records. Options include **Company** and **Person**. |
| When first started, this recipe should pick up events from | Select the date and time when the recipe picks up records created from. Leave blank to fetch records created one hour ago. This value can't be changed after the recipe has been run or tested. |

## Output

Output fields are dynamically generated based on the object type you select. Refer to the [Gainsight NXT API](https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Company_and_Relationship_API/Company_API_Documentation) documentation for a complete list of output fields.
