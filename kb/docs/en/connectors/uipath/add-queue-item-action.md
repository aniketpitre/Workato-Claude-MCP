---
url: 'https://docs.workato.com/en/connectors/uipath/add-queue-item-action.md'
description: >-
  The Add queue item action adds a queue item to the selected queue in UiPath
  orchestrator.
---

# UiPath - Add queue item action

The **Add queue item** action adds a queue item to the selected queue in UiPath orchestrator.

## Input

| Input field | Description |
| --- | --- |
| Queue | Select a queue from the drop-down menu. |
| Priority | Select the priority of the queue item from the drop-down menu. |
| Queue item from content | Set the data to pass to the queue item. |
| Reference | Enter optional text reference for the queue item. |
| Postponed until | Set the earliest date and time at which the item is available for processing. If empty, the item can be processed as soon as possible. |
| Deadline | Set the latest date and time at which the item should be processed. If empty, the item can be processed at any given time. |
| Risk SLA date | Set the date and time that is considered a risk zone for the item to be processed. |

## Output

| Output field | Description |
| --- | --- |
| Queue item ID | Unique identifier for the queue item. |

---
