---
url: 'https://docs.workato.com/en/connectors/uipath/get-queue-item-action.md'
description: >-
  The Get queue item action allows you to retrieve details about a queue item by
  ID from UiPath Orchestrator.
---

# UiPath - Get queue item action

The **Get queue item** action allows you to retrieve details about a queue item by ID from UiPath Orchestrator.

## Input

| Input field | Description |
| --- | --- |
| Queue item ID | Provide the queue item ID. |

## Output

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the queue item. |
| Key | Internal key used to track and reference the queue item. |
| Reference | Custom reference value provided when the item was added to the queue. |
| Start processing | Timestamp indicating when processing of the queue item began. |
| End processing | Timestamp indicating when processing of the queue item was completed. |
| Defer date | Date and time after which the queue item becomes available for processing. |
| Risk SLA date | The deadline by which the item should be processed to meet SLA requirements. |
| Due date | Optional date by which the queue item is expected to be completed. |
| Status | Current status of the queue item. |
| Review status | Indicates if the item is pending review or has already been reviewed. |
| Priority | Processing priority of the item. |

---
