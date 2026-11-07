---
url: 'https://docs.workato.com/en/connectors/uipath/add-queue-item-bulk-action.md'
description: >-
  The Add queue item bulk action adds multiple queue items to the selected queue
  in UiPath orchestrator.
---

# UiPath - Add queue item action (bulk)

The **Add queue item** bulk action adds multiple queue items to the selected queue in UiPath orchestrator.

## Input

| Input field | Description |
| --- | --- |
| Queue name | Select a queue from the drop-down menu. |
| Commit type | Select the commit type from the drop-down menu. |
| Priority | Select the priority of queue item from the drop-down menu. |
| Queue item from content | Set the data to pass to the queue item. |
| Reference | Enter optional text reference for the queue item. |
| Postponed until | Set the earliest date and time at which the item is available for processing. |
| Deadline | Set the latest date and time at which the item should be processed. If empty, the item can be processed at any given time. |
| Progress | Enter a text value representing the current progress or status of the queue item. |
| Source | Specify the origin of the queue item. |
| Parent operation ID | Set the date and time that is considered a risk zone for the item to be processed. |

## Output

| Output field | Description |
| --- | --- |
| Success | Unique identifier for the campaign. |
| Message | Name of the campaign. |

---

---
url: >-
  https://docs.workato.com/en/connectors/uipath/check-status-of-a-specific-queue-item-action.md
description: >-
  The Check status of a specific queue item action retrieves the status of a
  specific queue item in the UiPath Orchestrator.
---

# UiPath - Check status of a specific queue item action

The **Check status of a specific queue item** action retrieves the status of a specific queue item in the UiPath Orchestrator.

## Input

| Input field | Description |
| --- | --- |
| Queue item ID | Provide the queue item ID. |

## Output

| Output field | Description |
| --- | --- |
| ID | A unique identifier for the queue item. |
| Status | The current state of the queue item. |
| Review status | Indicates whether the item has been reviewed. |

---

---
url: >-
  https://docs.workato.com/en/connectors/uipath/get-count-of-items-in-queue-action.md
description: >-
  The Get counts of items in queue action allows you to retrieve the count of
  items in a queue in UiPath Orchestrator.
---

# UiPath - Get count of items in queue action

The **Get counts of items in queue** action allows you to retrieve count of items in a queue in UiPath Orchestrator.

## Input

| Input field | Description |
| --- | --- |
| Status | Optional. Filter the count based on the status of the queue items (such as `New`). |
| Reference | Optional. Filter the count by a specific reference value associated with queue items. |

## Output

| Output field | Description |
| --- | --- |
| Count | The count of items in the queue. |

---
