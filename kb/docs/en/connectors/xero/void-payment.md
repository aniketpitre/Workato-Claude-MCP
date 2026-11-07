---
url: 'https://docs.workato.com/en/connectors/xero/void-payment.md'
description: >-
  The Void payment action in the Xero connector lets you void a payment made
  toward an invoice, credit note, prepayment, or overpayment using its payment
  ID.
---

# Xero - Void payment action

The **Void payment** action allows you to void a payment made towards an invoice, credit note, prepayment, or overpayment using the payment ID. You cannot void payments created through batch payments and receipts.

![Void payment action](/assets/void-payment-action.Ean0PRpD.png)_Xero - Void payment action_

## Input

| Input field | Description |
| --- | --- |
| Payment ID | Enter the unique identifier of the payment you plan to void. |

## Output

| Output field | Description |
| --- | --- |
| Payment ID | The unique identifier of the voided payment. |
| Date | The date of the payment. |
| Bank amount | The amount in the bank currency. |
| Amount | The payment amount. |
| Payment type | The type of payment. |
| Currency rate | The currency exchange rate applied to the payment. |
| Status | The current status of the payment. |
| Reference | Reference information for the payment. |
| Is reconciled | Indicates whether the payment is reconciled. |
| Updated date | The date when the payment was last updated. |
| Account | Information about the account associated with the payment |
| Invoice | Information about the invoice associated with the payment |

---
