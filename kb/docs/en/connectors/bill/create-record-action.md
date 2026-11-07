---
url: 'https://docs.workato.com/en/connectors/bill/create-record-action.md'
description: >-
  The Create record action in the BILL connector creates a new object of the
  type you select in BILL.
---

# BILL - Create record action

The **Create record** action creates a new object in BILL.

## Input

| Field | Description |
| --- | --- |
| Object | Select the object type to create. |

> **ADDITIONAL INPUT FIELDS**
> 
> The recipe editor generates additional input fields based on your **Object** selection. To learn more about the required input fields for each object type, see [BILL's API v2 documentation](https://developer.bill.com/v2/reference/api-reference-overview).

## Output

| Field | Description |
| --- | --- |
| Response status | Displays the status of the **Create record** action's API request. A value of `0` indicates success, and `1` indicates an error. |
| Response message | The response message returned from BILL's API. |
| Response data | A datatree that contains information about the object created in BILL, such as its `ID`, `Description`, `Created` date, and `Active?` status. |

---
