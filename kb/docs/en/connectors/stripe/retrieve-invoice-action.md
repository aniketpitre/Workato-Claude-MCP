---
url: 'https://docs.workato.com/en/connectors/stripe/retrieve-invoice-action.md'
description: >-
  The Retrieve invoice by ID action in the Stripe connector lets you retrieve
  the details of a specific invoice using its invoice ID.
---

# Stripe - Retrieve invoice by ID action

This action retrieves an invoice by ID in Stripe.

![Retrieve invoice by ID](/assets/retrieve-invoice-by-id.CwkzGCPC.png)_Retrieve invoice by ID action_

## Input

| Input field | Description |
| --- | --- |
| Invoice ID | The ID of the invoice you plan to retrieve. To find the invoice ID: Log in to Stripe > click **Customers** > select the appropriate customer > click the **Invoice** tab > select the invoice and copy the ID from the end of the URL. |

## Output

The output of this action is a datatree that contains information about the [Stripe object](https://stripe.com/docs/api/invoices/object).

---
