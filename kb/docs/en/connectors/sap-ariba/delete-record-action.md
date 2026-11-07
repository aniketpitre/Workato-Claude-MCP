---
url: 'https://docs.workato.com/en/connectors/sap-ariba/delete-record-action.md'
description: >-
  Use the Delete record action to delete a record in SAP Ariba, such as a
  contract workspace.
---

# SAP Ariba - Delete record action

Use the **Delete record** action to delete a record in SAP Ariba, such as a contract workspace.

> **COMPATIBLE APIS**
> 
> The SAP Ariba connector supports multiple APIs, and each API provides access to different objects and operations. Refer to the [Available APIs](/en/connectors/sap-ariba#available-apis) section to identify the APIs compatible with this action.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to delete. |
| {Object name} ID | Enter the unique identifier of the object to delete. This is typically a numeric or alphanumeric ID from SAP Ariba. You can obtain this ID using the [Search objects action](/en/connectors/sap-ariba/search-objects-action). |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates whether the record was deleted successfully. |

---
