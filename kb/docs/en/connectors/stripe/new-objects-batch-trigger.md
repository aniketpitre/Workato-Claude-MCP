---
url: 'https://docs.workato.com/en/connectors/stripe/new-objects-batch-trigger.md'
description: >-
  The New objects batch trigger in the Stripe connector periodically checks for
  new objects in Stripe and retrieves them in configurable batches.
---

# Stripe - New objects trigger (batch)

This trigger periodically checks for new objects in Stripe and retrieves them in batches. Supported objects are:

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
| When first started, this recipe should pick up events from | Specify a date and time to pick up existing charges when starting the recipe for the first time. This value remains unchanged after you run or test the recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Batch size | Specify the maximum number of records to retrieve per trigger event. The minimum is 1 and the maximum is 100. This field defaults to 100 if unspecified. |

## Output

The output of this action is a datatree that contains information about the [Stripe object](https://docs.stripe.com/api) selected.

---
