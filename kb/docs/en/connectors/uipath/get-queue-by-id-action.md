---
url: 'https://docs.workato.com/en/connectors/uipath/get-queue-by-id-action.md'
description: >-
  The Get queue by ID action allows you to retrieve details of a specific queue
  by its ID in UiPath Orchestrator.
---

# UiPath - Get queue by ID action

The **Get queue by ID** action allows you to retrieve details of a specific queue by its ID in UiPath Orchestrator.

## Input

| Input field | Description |
| --- | --- |
| Queue ID | Provide the queue ID. |

## Output

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the queue. |
| Key | Internal key associated with the queue for referencing within Orchestrator. |
| Name | Display name of the queue. |
| Description | Optional text providing details about the queue’s purpose or usage. |
| Max number of retries | Maximum number of retry attempts allowed for failed queue items. |
| Process schedule ID | Identifier of the schedule linked to the queue, if any. |
| Creation time | Timestamp when the queue was created. |
| Risk SLA date | SLA deadline for items in the queue considered at risk if not processed. |
| Due date | General due date for processing items in the queue. |
| Release ID | Identifier of the release (process version) associated with the queue. |
| Is process in current folder | Boolean value indicating if the process is located in the current folder. |
| Folders count | Number of folders where the queue is available or shared. |
| Organization unit ID | ID of the organization unit where the queue resides. |
| Organization unit fully qualified name | Full hierarchical name of the organization unit. |

---
