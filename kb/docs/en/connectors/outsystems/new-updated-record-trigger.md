---
url: >-
  https://docs.workato.com/en/connectors/outsystems/new-updated-record-trigger.md
description: >-
  The New or updated record trigger in the OutSystems connector runs when a new
  record is detected or an existing record is updated in a module you select.
---

# OutSystems - New or updated record trigger

The New or updated record trigger runs when a new record is detected in OutSystems or an existing record is updated. The trigger checks for new or updated records every five minutes by default.

![New or updated record trigger](/assets/new-updated-record-trigger.DYd8InTc.png)_New or updated record trigger_

## Input

| Input field | Description |
| --- | --- |
| Module | Select the module you plan to monitor for new or updated records. |
| Entity ID | Select the entity ID of the module you plan to monitor for new or updated records. |

## Output

| Output field | Description |
| --- | --- |
| Record | This entry contains information specific to the record attributes and other configurations, such as `Label` and record ID, you selected for the OutSystems object. |
