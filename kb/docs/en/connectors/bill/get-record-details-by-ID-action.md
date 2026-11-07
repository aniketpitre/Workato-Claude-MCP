---
url: 'https://docs.workato.com/en/connectors/bill/get-record-details-by-ID-action.md'
description: >-
  The Get record details by ID action in the BILL connector retrieves data about
  an object of the type you select using its internal ID in BILL.
---

# BILL - Get record details by ID action

The **Get record details by ID** action retrieves data about an object in BILL.

## Input

| Field | Description |
| --- | --- |
| Object | Select the object type to retrieve data from. |
| ID | Provide the internal ID of the object to retrieve data from. |

## Output

| Field | Description |
| --- | --- |
| Response status | Displays the status of the **Get record details by ID** action's API request. A value of `0` indicates success, and `1` indicates an error. |
| Response message | The response message returned from BILL's API. |
| Response data | A datatree that contains information about the object found in BILL, such as its `ID`, `Name`, `Created` date, and `Active?` status. |

---
