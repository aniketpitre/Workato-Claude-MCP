---
url: 'https://docs.workato.com/en/connectors/sage-intacct/apply-ar-payment-action.md'
description: The Apply AR payment action applies the AR payment in Sage Intacct.
---

# Sage Intacct (Custom) - Apply AR payment action

The **Apply AR payment** action applies the AR payment in Sage Intacct.

## Input

| Input field | Description |
| --- | --- |
| AR payment key | Provide the AR payment key. |
| Payment date | Provide payment date in year, month and day fields. |
| Memo | Provide the memo for AR payment. |
| Overpayment location ID | Provide the overpayment location ID. |
| Overpayment department ID | Provide the overpayment department ID. |
| AR payment items | Provide the AR payment item list here in the Amount and Invoice key fields. |

## Output

| Output fields | Description |
| --- | --- |
| Status | Returns the status of apply action. |
| Function | The action performed in the API call. |
| Control ID | A unique string to track the transaction. |
| Record key | A unique internal identifier assigned by Intacct to the newly created AR payment application record. |

---

---
url: >-
  https://docs.workato.com/en/connectors/sage-intacct/create-contract-mea-allocation-action.md
description: >-
  The Create contract MEA allocation action creates the contract MEA allocation
  in Sage Intacct.
---

# Sage Intacct (Custom) - Create contract MEA allocation action

The **Create contract MEA allocation** action creates the contract MEA allocation in Sage Intacct.

## Input

| Input field | Description |
| --- | --- |
| Contract ID | Provide the contract ID for MEA allocation. |
| Name | Provide the name for MEA allocation. |
| Description | Provide the description. |
| Effective date | Select the effective date for allocation from the calendar. |
| Adjustment process | Select the suitable adjustment process from the drop-down menu. |
| Type | Select the suitable type from the drop-down menu. |
| Apply to journal 1 | Select the boolean value from the drop-down menu. |
| Apply to journal 2 | Select the boolean value from the drop-down menu. |
| Comments | Provide comments for the action. |
| Contract MEA bundle entries | Provide contract MEA bundle entries fields such as Contract detail line number, Bundle number and MEA amount. |

## Output

| Output fields | Description |
| --- | --- |
| Record number | A unique record number returned for the action. |

---
