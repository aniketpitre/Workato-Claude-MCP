---
url: 'https://docs.workato.com/en/connectors/bill/update-record-action.md'
description: >-
  The Update record action in the BILL connector updates an existing object of
  the type you select using its internal ID in BILL.
---

# BILL - Update record action

The **Update record** action updates an existing object in BILL.

## Input

| Field | Description |
| --- | --- |
| Object | Select the object type to update. |
| ID | Provide the internal ID of the object to update. |

## Output

| Field | Description |
| --- | --- |
| Response status | Displays the status of the **Update record** action's API request. A value of `0` indicates success, and `1` indicates an error. |
| Response message | The response message returned from BILL's API. |
| Response data | A datatree that contains information about the object updated in BILL, such as its `ID`, `Name`, `Created` date, and `Active?` status. |

---
