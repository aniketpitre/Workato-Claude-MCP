---
url: 'https://docs.workato.com/en/connectors/stripe/new-object-event-trigger.md'
description: >-
  The New object event trigger in the Stripe connector fires in real time when
  new events related to a selected object type occur in Stripe.
---

# Stripe - New object event trigger (real-time)

This trigger checks for new events related to specified objects in Stripe, in real time. Supported objects are:

- Account
- Application fee
- Capability
- Charge
- Customer
- Dispute
- File
- Invoice
- Invoice item
- Payment intent
- Payout
- Refund
- Setup intent

> **REQUIRES API KEY AUTHENTICATION**
> 
> This real-time trigger only works if you connect to Stripe using **API key** authentication method.

## Input

<dl><dt>Object</dt><dd>Select the object that you plan to monitor.</dd><dt>Events to monitor</dt><dd>Select the events that you plan to monitor.</dd></dl>

## Output

The output of this action is a data tree containing information about the [Stripe event](https://docs.stripe.com/api/events/object) related to the selected object.

---
