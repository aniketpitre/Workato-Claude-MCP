---
url: >-
  https://docs.workato.com/en/connectors/sap-ariba/new-updated-record-batch-trigger.md
description: >-
  The New/updated events (batch) trigger monitors SAP Ariba for new or updated
  events. These events are processed as a batch.
---

# SAP Ariba - New/updated events (batch) trigger

The **New/updated events (batch)** trigger monitors SAP Ariba for new or updated events. These events are processed as a batch.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Select a value for how frequently to check for new events. Defaults to minutes if left blank. |
| Object | Select the type of object to monitor for new or updated events. |
| When first started, this recipe should pick up events from | Enter the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

Output fields are generated dynamically based on the object you select. Refer to the [SAP Ariba](https://www.sap.com/india/products/spend-management/ariba-network.html) documentation for a complete list of outputs.
