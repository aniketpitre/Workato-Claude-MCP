---
url: 'https://docs.workato.com/en/connectors/bill/delete-record-action.md'
description: >-
  The Delete record action in the BILL connector deletes an object of the type
  you select using its internal ID in BILL.
---

# BILL - Delete record action

The **Delete record** action deletes an object in BILL.

## Input

| Field | Description |
| --- | --- |
| Object | Select the object type to delete. |
| ID | Provide the internal ID of the object to delete. |

## Output

| Field | Description |
| --- | --- |
| Response status | Displays the status of the **Delete record** action's API request. A value of `0` indicates success, and `1` indicates an error. |
| Response message | The response message returned from BILL's API. |
| Response data | A datatree that contains information about the object deleted in BILL, such as its `ID`, `Name`, `Created` date, and `Active?` status. |

---
