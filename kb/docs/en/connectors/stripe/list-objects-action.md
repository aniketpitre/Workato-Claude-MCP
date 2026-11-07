---
url: 'https://docs.workato.com/en/connectors/stripe/list-objects-action.md'
description: >-
  The List objects batch action in the Stripe connector lets you retrieve a list
  of objects in Stripe, with search criteria to refine the results.
---

# Stripe - List objects (batch) action

This action retrieves a list containing the details of an object in Stripe. You can apply search criteria to refine the results. Supported objects are:

- Accounts
- Application fees
- Balance transactions
- Capabilities
- Charges
- Customers
- Disputes
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

<dl><dt>Object</dt><dd>Select the object that you plan to retrieve.</dd><dt>Date created (filter)</dt><dd>Specify values to filter charges based on their created date.</dd><dt>Ending before</dt><dd>Provide a record ID for pagination to fetch records preceding it in the sorted order.</dd><dt>Starting after</dt><dd>Provide a record ID for pagination to fetch records following it in the sorted order.</dd><dt>Quota</dt><dd>Limit the number of records to retrieve. The minimum value is 1 and the maximum value is 100. This field defaults to 10 if unspecified.</dd></dl>

## Output

The output of this action is a list of data trees that contain information about the selected [Stripe object](https://docs.stripe.com/api).

---
