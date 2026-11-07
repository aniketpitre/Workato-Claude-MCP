---
url: 'https://docs.workato.com/en/connectors/wiz/get-record-details-action.md'
description: >-
  The Get record details by ID action retrieves a single cloud resource record
  from Wiz using its unique identifier. You can optionally specify which fields
  to return.
---

# Wiz - Get record details by ID action

The **Get record details by ID** action retrieves a single record from Wiz using its unique identifier. Use this action to return details for a specific cloud resource.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type to retrieve details for. |
| ID | Enter the unique ID of the cloud resource to retrieve. |
| Fields to retrieve | Optional. Select the specific fields to include in the response to improve performance. All fields return if left blank. |
| Nodes | Optional. Expand this section to specify nested node options, if required. |

## Output

By default, the output includes all available fields for the specified record. These vary depending on the object's type and structure. Common output fields may include the following:

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the record. |
| Name | Name of the record. |
| Description | Description or metadata associated with the record. |
| Resource type | The type or category of the record. |

The full set of output fields depends on the structure of the retrieved resource.

---
