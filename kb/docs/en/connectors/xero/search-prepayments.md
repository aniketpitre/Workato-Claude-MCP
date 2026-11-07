---
url: 'https://docs.workato.com/en/connectors/xero/search-prepayments.md'
description: >-
  The Search prepayments batch action in the Xero connector lets you find
  prepayments using criteria such as the prepayment ID.
---

# Xero - Search prepayments batch action

The **Search prepayments** batch action allows you to search for prepayments using specific criteria, such as the prepayment ID. You must provide at least one search field.

![Search prepayments action](/assets/search-prepayments-action.Di_EssIU.png)_Xero - Search prepayments batch action_

## Input

| Input field | Description |
| --- | --- |
| Prepayment ID | Enter the unique identifier of the prepayment you plan to search for. |
| Type | Select whether the prepayment is a `RECEIVE-PREPAYMENT` or `SPEND-PREPAYMENT`. |
| Date | Search for prepayments created after this date. |
| Status | Choose the prepayment status to search for. Valid values include `AUTHORISED`, `PAID`, and `VOIDED`. |
| Line amount types | Specify the line amount type. |
| Invoice number | Enter the invoice number related to the prepayment if available. |

## Output

| Output field | Description |
| --- | --- |
| Prepayments | Details about the prepayment records. |

---
