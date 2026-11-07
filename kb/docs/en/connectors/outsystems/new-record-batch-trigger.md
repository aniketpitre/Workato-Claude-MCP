---
url: 'https://docs.workato.com/en/connectors/outsystems/new-record-batch-trigger.md'
description: >-
  The New record batch trigger in the OutSystems connector runs when new records
  are detected in a module, returning them in configurable batches.
---

# OutSystems - New record batch trigger

The New record batch trigger runs when new records are detected in OutSystems. The trigger checks for new records every five minutes by default.

![New record batch trigger](/assets/new-record-batch-trigger.ZU624mOI.png)_New record batch trigger_

## Input

| Input field | Description |
| --- | --- |
| Module | Select the module you plan to monitor for new records. |
| Entity ID | Select the entity ID of the module you plan to monitor for new records. |
| Batch size | This determines the maximum number of messages per trigger event. The minimum is `1`, the maximum is `10,000`, and the default is `100`. |

## Output

| Output field | Description |
| --- | --- |
| Entity | The entity ID you selected to monitor. |
| Number of records | The number of new records detected. |

---

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

---

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

---
