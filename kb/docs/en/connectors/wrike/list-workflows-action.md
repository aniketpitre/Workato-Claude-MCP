---
url: 'https://docs.workato.com/en/connectors/wrike/list-workflows-action.md'
description: >-
  The List workflows batch action in the Wrike connector retrieves all workflows
  and statuses and their IDs from the connected Wrike instance.
---

# Wrike - List workflows action (batch)

The **List workflows** batch action retrieves all workflows and statuses in the connected Wrike instance. You can use workflow and status IDs in subsequent Wrike actions.

## Input

This action doesn't require any input.

## Output

| Output field | Description |
| --- | --- |
| Workflow | List of retrieved workflows. |
| Workflow ID | Unique identifier for the workflow. |
| Space ID | Unique identifier of the space associated with the workflow. |
| Workflow name | Name of the workflow. |
| Standard workflow | Indicates whether this is a standard workflow. |
| Hidden | Indicates whether the workflow is hidden from selection. |
| Statuses | List of statuses associated with the workflow. |
| List size | Total number of workflows retrieved in the batch. |
| List index | Position of the current workflow in the batch. |

---
