---
url: >-
  https://docs.workato.com/en/connectors/azure-devops/new-updated-work-item-trigger.md
description: >-
  The New/Updated work item (batch) trigger monitors Azure DevOps for new or
  updated work items.
---

# Azure DevOps - New/Updated work item (batch) trigger

The **New/Updated work item (batch)** trigger monitors Azure DevOps for new or updated work items.

## Input

| Input field | Description |
| --- | --- |
| Batch size | Enter the batch size. Default is `100`. Maximum is `200`. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Project | Select the project to monitor. |

## Output

| Output field | Description |
| --- | --- |
| Work items | Information about the new or updated work item, including `Work item ID`, `Work item URL`, `Revision number`, and `Fields`. |
