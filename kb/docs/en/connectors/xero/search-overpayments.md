---
url: 'https://docs.workato.com/en/connectors/xero/search-overpayments.md'
description: >-
  The Search overpayments batch action in the Xero connector lets you find
  overpayments using criteria such as the overpayment ID.
---

# Xero - Search overpayments batch action

The **Search overpayments** batch action allows you to search for overpayments using specific criteria, such as the overpayment ID. You must provide at least one search field.

![Search overpayments action](/assets/search-overpayments-action.D_E7GQhL.png)_Xero - Search overpayments batch action_

## Input

| Input field | Description |
| --- | --- |
| Overpayment ID | Enter the unique identifier for the overpayment you plan to locate. |
| Type | Specify the type of overpayment you are searching for. Valid options include `RECEIVE-OVERPAYMENT` for customer overpayments and `SPEND-OVERPAYMENT` for supplier overpayments. |
| Date | Set a date to find overpayments created after this specific date. |
| Status | Choose the status of the overpayment records you plan to retrieve. Valid options include `AUTHORISED`, `PAID`, and `VOIDED`. |

## Output

| Output field | Description |
| --- | --- |
| Overpayments | A list of overpayments. |

---
