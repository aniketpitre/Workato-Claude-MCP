---
url: >-
  https://docs.workato.com/en/connectors/outsystems/new-updated-record-batch-trigger.md
description: >-
  The New or updated record batch trigger in the OutSystems connector runs when
  records are created or updated in a module, returning them in batches.
---

# OutSystems - New or updated record batch trigger

The New or updated record batch trigger runs when new records are detected in OutSystems or existing records are updated. The trigger checks for new or updated records every five minutes by default.

![New or updated record batch trigger](/assets/new-updated-record-batch-trigger.CA5okBPk.png)_New or updated record batch trigger_

## Input

| Input field | Description |
| --- | --- |
| Module | Select the module you plan to monitor for new or updated records. |
| Entity ID | Select the entity ID of the module you plan to monitor for new or updated records. |
| Batch size | This determines the maximum number of messages per trigger event. The minimum is `1`, the maximum is `10,000`, and the default is `100`. |

## Output

| Output field | Description |
| --- | --- |
| Entity | The entity ID of the module you selected. |
| Number of records | The number of new or updated records detected. |
