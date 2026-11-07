---
url: 'https://docs.workato.com/en/connectors/shopify/send-email-invoice.md'
description: >-
  The Send email invoice action in the Shopify connector lets you email an
  invoice for an existing draft order to a customer.
---

# Shopify - Send email invoice action

This action sends an invoice for any existing draft orders on Shopify. A draft order represents the intent of ordering by a customer. It can be transitioned into an order.

Refer to the [Shopify documentation](https://shopify.dev/api/admin-rest/2022-01/resources/draftorder) for more information on the draft order resource.

## Input

| Field | Description |
| --- | --- |
| Draft order ID | The ID of the draft order to be sent out for invoicing. |
| To address | The invoice recipient’s email address. |
| From address | Optional. The invoice sender's email address. |
| BCC addresses | Optional. The list of email addresses to include in the bcc field of the email. Emails must be associated with staff accounts on the shop. |
| Custom subject | Optional. The custom email subject. Reverts to Shopify default if left blank. |
| Custom message | Optional. The custom message displayed in the email. Reverts to Shopify default if left blank. |

## Output

The output of this action is a datatree that summarizes the draft order invoice sent. It contains information such as to, from, bcc list, subject, and custom message.

Learn more about the [draft order invoice object](https://shopify.dev/api/admin-rest/2024-04/resources/draftorder#post-draft-orders-draft-order-id-send-invoice).

---
