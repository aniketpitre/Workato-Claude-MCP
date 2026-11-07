---
url: 'https://docs.workato.com/en/connectors/stripe/new-object-trigger.md'
description: >-
  The New object trigger in the Stripe connector periodically checks for new
  objects, such as charges, customers, invoices, and payouts, in Stripe.
---

# Stripe - New object trigger

This trigger periodically checks for new objects in Stripe. Supported objects are:

- Accounts
- Application fees
- Balance transactions
- Charges
- Customers
- Events
- File links
- Files
- Invoice items
- Invoices
- Payment intents
- Payouts
- Refunds
- Setup attempts
- Setup intents

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object that you plan to monitor. |
| When first started, this recipe should pick up events from | Specify a date and time for picking up existing charges when starting the recipe for the first time. This value remains unchanged after you run or test the recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

The output of this action is a data tree containing information about the selected [Stripe object](https://docs.stripe.com/api).

---
