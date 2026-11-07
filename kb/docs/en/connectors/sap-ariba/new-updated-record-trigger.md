---
url: 'https://docs.workato.com/en/connectors/sap-ariba/new-updated-record-trigger.md'
description: >-
  The New/updated object trigger monitors SAP Ariba for new or updated records,
  such as a new contract workspace or event.
---

# SAP Ariba - New/updated object trigger

Use the **New/updated object** trigger to monitor SAP Ariba for new or updated records, such as a new contract workspace or event.

> **COMPATIBLE APIS**
> 
> The SAP Ariba connector supports multiple APIs, and each API provides access to different objects and operations. Refer to the [Available APIs](/en/connectors/sap-ariba#available-apis) section to identify the APIs compatible with this action.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Determine how frequently to check for new events. |
| Object | Use the drop-down to select the type of object to activate trigger events, such as a Contract workspace. |
| When first started, this recipe should pick up events from | When you start recipe for the first time, it picks up trigger events from this specified date and time. Leave empty to get records created or updated one hour ago. This value can't be changed once the recipe has been run or tested. |

## Output

The output of this action is determined by the object selected in the input. Use the data tree in the recipe editor to see all available output fields for your specific object and map them to subsequent steps.

---

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

---
