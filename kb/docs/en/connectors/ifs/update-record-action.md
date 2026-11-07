---
url: 'https://docs.workato.com/en/connectors/ifs/update-record-action.md'
description: Use the Update record action to update a record in IFS.
---

# IFS connector - Update record action

The **Update record** action updates a record in Industrial and Financial Systems (IFS) Cloud. You can select an IFS service to work with. IFS service availability depends on your IFS instance configuration.

## Input

| Input field | Description |
| --- | --- |
| IFS Service | Select the IFS service to work with from the list. Alternatively, you can enter the service name. |
| Object | Select the object to update. The list of available objects is generated dynamically based on the service you select. |
| {Object} ID | Provide the ID of the object to update. You can map in the object ID from the output of the [Search records in IFS action](/en/connectors/ifs/search-records-action). |

Additional input fields are available based on the object you select. You must update at least one field for the action to complete successfully.

## Output

The output for this action is dynamically generated based on the IFS service and object you select. You can map action output to downstream recipe steps.

---
