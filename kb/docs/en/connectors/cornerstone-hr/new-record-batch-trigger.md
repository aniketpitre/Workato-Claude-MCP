---
url: >-
  https://docs.workato.com/en/connectors/cornerstone-hr/new-record-batch-trigger.md
description: >-
  The New record batch trigger activates when records, such as users, are
  created in Cornerstone, and returns them in batches.
---

# Cornerstone HR - New record batch trigger

The **New record batch** trigger activates when records, such as users, are created in Cornerstone HR, and returns them in batches.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object you plan to monitor for new records. Options are **User** and **Training**. |
| When first started, this recipe should pick up events from | Select the date and time this recipe starts picking up events from when you run it for the first time. Leave blank to pick up records created one hour ago. |

## Output

Output fields dynamically generate based on the object you select, returned as an array of records. Refer to the [Cornerstone API documentation](https://apiexplorer.csod.com) for a complete list of output fields.
