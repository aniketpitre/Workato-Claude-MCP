---
url: 'https://docs.workato.com/en/connectors/xero/new-overpayment.md'
description: >-
  The New/updated overpayment trigger in the Xero connector fires when an
  overpayment is created or updated.
---

# Xero - New/updated overpayment trigger

The **New/updated overpayment** trigger activates when an overpayment is created or updated.

![New/updated overpayment trigger](/assets/new-overpayment-trigger.CLSv418J.png)_Xero - New/updated overpayment trigger_

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Choose how often Workato checks for new or updated events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | Determine the starting point for the trigger to fetch events. You cannot change this value after the recipe has been run or tested. |

## Output

| Output field | Description |
| --- | --- |
| Updated date UTC | The date and time of the last update in UTC. |
| Date | The date of the overpayment transaction. |
| Line amount types | Types of line amounts in the overpayment. |
| Line items | Detailed items in the overpayment. |
| Contact | Contact details associated with the overpayment. |
| Bank transaction types | Type of the bank transaction. |
| Is reconciled | Indicates whether the overpayment is reconciled. |
| Reference | Reference note or number for the overpayment. |
| Currency code | The currency code used in the overpayment. |
| Currency rate | The exchange rate of the currency used. |
| Bank transaction status | Status of the bank transaction. |
| Amounts are | Indicates whether amounts are tax inclusive or exclusive. |
| URL | URL link to the overpayment transaction in Xero. |
| Sub total | Subtotal amount before tax. |
| Total tax | Total tax amount in the overpayment. |
| Total | Total amount of the overpayment. |
| Date of transaction | The date when the transaction occurred. |
| Remaining credit | Remaining credit amount from the overpayment. |
| Has attachments | Indicates if there are attachments to the overpayment. |
| Payments | Payment details related to the overpayment. |
| Allocations | Allocation details for the overpayment. |
| Overpayment ID | The unique identifier for the overpayment. |

---
