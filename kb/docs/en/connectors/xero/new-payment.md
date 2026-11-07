---
url: 'https://docs.workato.com/en/connectors/xero/new-payment.md'
description: >-
  The New/updated payment trigger in the Xero connector fires when a payment is
  created or updated in your connected Xero organization.
---

# Xero - New/updated payment trigger

The **New/updated payment** trigger activates when a payment is created or updated.

![New/updated payment trigger](/assets/new-payment-trigger.BesjzD3f.png)_Xero - New/updated payment trigger_

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Choose how often Workato checks for new or updated events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | Determine the starting point for the trigger to fetch events. You cannot change this value after the recipe has been run or tested. |

## Output

| Output field | Description |
| --- | --- |
| Payment ID | The unique identifier for the payment. |
| Date | The date when the payment was made. |
| Amount | The total amount of the payment. |
| Bank amount | The amount recorded in the bank for this payment. |
| Currency rate | The exchange rate of the currency used in the payment. |
| Payment type | The type of the payment. |
| Reference | A reference note or number for the payment. |
| Status | The current status of the payment. |
| Updated date | The date when the payment information was last updated. |
| Account | Account details associated with the payment. |
| Invoice | Invoice details associated with the payment. |

---
