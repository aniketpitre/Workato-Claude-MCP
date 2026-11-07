---
url: 'https://docs.workato.com/en/connectors/stripe/get-object-by-id-action.md'
description: >-
  The Get object by ID action in the Stripe connector lets you retrieve the
  details of a specified object type using its object ID in Stripe.
---

# Stripe - Get object by ID action

This action retrieves the details of a specified object type by its ID in Stripe. Supported objects are:

- Accounts
- Application fees
- Balance transactions
- Capabilities
- Charges
- Customers
- Disputes
- File links
- Files
- Invoice items
- Invoices
- Payment intents
- Payouts
- Refunds
- Setup intents

## Input

<dl><dt>Object</dt><dd>Select the object that you plan to list.</dd><dt>Object ID</dt><dd>Provide the ID of the selected object to retrieve its data.</dd></dl>

## Output

The output of this action is a data tree that contains information about the selected [Stripe object](https://docs.stripe.com/api).

---
