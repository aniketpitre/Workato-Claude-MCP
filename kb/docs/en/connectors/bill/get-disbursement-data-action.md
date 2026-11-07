---
url: 'https://docs.workato.com/en/connectors/bill/get-disbursement-data-action.md'
description: >-
  The Get disbursement data action in the BILL connector retrieves data about a
  payment, including its type, disbursement status, and vendor name.
---

# BILL - Get disbursement data action

The **Get disbursement data** action retrieves data about a payment in BILL.

## Input

| Field | Description |
| --- | --- |
| Bill payment ID | Provide the internal ID of the payment to retrieve data about. |

## Output

| Field | Description |
| --- | --- |
| Response status | Displays the status of the **Get disbursement data** action's API request. A value of `0` indicates success, and `1` indicates an error. |
| Response message | The response message returned from BILL's API. |
| Response data | A datatree that contains information about the payment found in BILL, such as its `Payment type`, `Disbursement status`, and `Vendor name`. |

---
