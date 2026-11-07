---
url: 'https://docs.workato.com/en/connectors/ifs/new-updated-record-trigger-batch.md'
description: >-
  Use the New/updated record (batch) trigger to monitor IFS for new or updated
  objects and process the results in batches.
---

# IFS connector - New/updated record (batch)

The **New/updated record (batch)** trigger runs when a record of the selected object is created or updated in Industrial and Financial Systems (IFS) Cloud. Workato processes each batch as a separate job. You can select an IFS service and object to work with. IFS service availability depends on your IFS instance configuration.

The required information for handling time ranges and pagination are auto-detected after you select an object. You may need to provide additional information in some situations.

## Input

| Input field | Description |
| --- | --- |
| IFS Service | Select the IFS service to work with from the list. Alternatively, you can enter the service name. |
| Object | Select the object type to monitor. The list of available objects is generated dynamically based on the service you select. |
| When first started, this recipe should pick up events from | When you start recipe for the first time, it picks up trigger events from this specified date and time. Leave empty to get events created one hour ago. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Determine how frequently to check for new events. Defaults to five minutes if left blank. Minimum value allowed is five minutes. |

## Output

The output for this trigger is dynamically generated based on the IFS service and object you select.

---
