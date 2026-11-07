---
url: 'https://docs.workato.com/en/connectors/uipath/mark-queue-item-action.md'
description: >-
  The Mark queue item action allows you to mark the queue item of a selected
  queue in UiPath Orchestrator.
---

# UiPath - Mark queue item action

The **Mark queue item** action allows you to mark the queue item of a selected queue in UiPath Orchestrator.

## Input

| Input field | Description |
| --- | --- |
| Queue item ID | Provide the queue item ID. |
| Is successful | Select the boolean value from the drop-down menu. |
| Processing exception | Provide the details of processing exception, if any. It is an object containing fields such as **Reason**, **Details**, and **Type**. |
| Output | Set the data to pass to the queue item. |
| Analytics | Set the data to pass to the queue item. |
| Progress | An optional text field indicating progress details or a status message of the update. |
| Postpone until | Set the earliest date and time at which the item is available for processing. If empty, the item can be processed as soon as possible. |
| Deadline | Set the latest date and time at which the item should be processed. If empty, the item can be processed at any given time. |
| Operation ID | Provide the unique identifier of the marking operation, used for tracking the update action. |

## Output

| Output field | Description |
| --- | --- |
| Success | Returns the status of the mark action. |

---
