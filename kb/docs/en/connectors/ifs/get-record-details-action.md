---
url: 'https://docs.workato.com/en/connectors/ifs/get-record-details-action.md'
description: Use the Get record details action to retrieve a record in IFS using its ID.
---

# IFS connector - Get record details by ID action

The **Get record details by ID** action retrieves the details of a record in Industrial and Financial Systems (IFS) Cloud. You can select an IFS service to work with. IFS service availability depends on your IFS instance configuration.

## Input

| Input field | Description |
| --- | --- |
| IFS Service | Select the IFS service to work with from the list. Alternatively, you can enter the service name. |
| Object | Select the object type to retrieve details for. The list of available objects is generated dynamically based on the service you select. |
| {Object} ID | Provide the ID of the object to retrieve. You can map in the object ID from the output of other IFS connector actions, such as the [Search records in IFS action](/en/connectors/ifs/search-records-action). |

## Output

The output for this action contains is dynamically generated and depends on the IFS Service and object you select. You can map action output to downstream recipe steps.

---
