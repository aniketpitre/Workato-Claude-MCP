---
url: 'https://docs.workato.com/en/connectors/stripe/create-charge-action.md'
description: >-
  The Create charge action in the Stripe connector lets you create a charge for
  a specified amount, currency, account, and card in Stripe.
---

# Stripe - Create charge action

This action creates a charge in Stripe.

![Create charge action](/assets/create-charge-action.DmNMJGWC.png)_Create charge action_

## Input

| Input field | Description |
| --- | --- |
| Amount | Enter the monetary amount you plan to charge. This must be a positive number. |
| Currency | The currency type for the charge. You must use the three-letter ISO code for currency. For example, USD for the United States. |
| Account ID | Click the **Destination** drop-down menu and enter the account ID of the customer. |
| Object | Click the **Card** drop-down menu and enter `card` as the payment source. This is the only object accepted. |
| Expiration month | Enter the month that the card expires. This must be two digits, for example, `04` or `12`. |
| Expiration year | Enter the year that the card expires. This can be either two or four digits, for example, `27` or `2027`. |
| Card number | Enter the card number to which you plan to apply the charge. Do not use separators. |

## Output

The output of this action is a datatree that contains information about the [Stripe object](https://stripe.com/docs/api/charges/object).

---
