---
url: 'https://docs.workato.com/en/connectors/xero/new-prepayment.md'
description: >-
  The New/updated prepayment trigger in the Xero connector fires when a
  prepayment is created or updated.
---

# Xero - New/updated prepayment trigger

The **New/updated prepayment** trigger activates when a prepayment is created or updated.

![New/updated prepayment trigger](/assets/new-prepayment-trigger.cJRHNE3H.png)_Xero - New/updated prepayment trigger_

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Choose how often Workato checks for new or updated events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | Determine the starting point for the trigger to fetch events. You cannot change this value after the recipe has been run or tested. |

## Output

| Output field | Description |
| --- | --- |
| Updated date UTC | The date and time of the last update in UTC. |
| Date | The date of the prepayment transaction. |
| Line amount types | Types of line amounts in the prepayment. |
| Line items | Detailed items in the prepayment. |
| Contact | Contact details associated with the prepayment. |
| Bank transaction types | Type of the bank transaction. |
| Is reconciled | Indicates whether the prepayment is reconciled. |
| Reference | Reference note or number for the prepayment. |
| Currency code | The currency code used in the prepayment. |
| Currency rate | The exchange rate of the currency used. |
| Bank transaction status | Status of the bank transaction. |
| Amounts are | Indicates whether amounts are tax inclusive or exclusive. |
| URL | URL link to the prepayment transaction in Xero. |
| Sub total | Subtotal amount before tax. |
| Total tax | Total tax amount in the prepayment. |
| Total | Total amount of the prepayment. |
| Date of transaction | The date when the transaction occurred. |
| Remaining credit | Remaining credit amount from the prepayment. |
| Has attachments | Indicates if there are attachments to the prepayment. |
| Payments | Payment details related to the prepayment. |
| Allocations | Allocation details for the prepayment. |
| Prepayment ID | The unique identifier for the prepayment. |

---
