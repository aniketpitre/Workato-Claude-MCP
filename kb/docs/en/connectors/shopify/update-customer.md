---
url: 'https://docs.workato.com/en/connectors/shopify/update-customer.md'
description: >-
  The Update customer action in the Shopify connector lets you update the
  details of an existing customer in your store.
---

# Shopify - Update customer action

This action updates a customer in Shopify.

## Input

| Field | Description |
| --- | --- |
| First name | The customer's first name. |
| Last name | The customer's last name. |
| Email | The unique email address of the customer. |
| Customer ID | A unique identifier for the customer. |

## Output

| Field | Description |
| --- | --- |
| Customer ID | A unique identifier for the customer. |
| First name | The customer's first name. |
| Last name | The customer's last name. |
| Email | The unique email address of the customer. |
| Phone | The unique phone number for this customer. |
| Admin GraphQL API ID | The Admin GraphQL API ID. |
| Marketing opt in level (deprecated) | The marketing subscription opt-in level that the customer gave when they consented to receive marketing material by email. If the customer does not accept email marketing, then this property is set to null. Use **Email marketing consent** instead. |
| Accepts marketing (deprecated) | Whether the customer has consented to receive marketing material via email. Use **Email marketing consent** instead. |
| Email marketing consent | Information that describes when a customer consented to receiving marketing material by email, including: - State - Opt in level - Consent updated at |
| Created at | The date and time when the customer was created. |
| Updated at | The date and time when the customer was updated. |
| Orders count | The number of orders associated with this customer. |
| State | The state of the customer's account with a shop. |
| Total spent | The total amount of money that the customer has spent across their order history. |
| Last order ID | The ID of the customer's last order. |
| Note | A note about the customer. |
| Verified email | Whether the customer has verified their email address. |
| Multipass identifier | A unique identifier for the customer that's used with Multipass login. Find out more about Shopify [Multipass login](https://shopify.dev/docs/admin-api/rest/reference/plus/multipass). |
| Tax exempt | Whether the customer is exempt from paying taxes on their order. If true, then taxes won't be applied to an order at checkout. If false, then taxes will be applied at checkout. |
| Tags | Tags that the shop owner has attached to the customer, formatted as a string of comma-separated values. A customer can have up to 250 tags. Each tag can have up to 255 characters. |
| Last order name | The name of the customer's last order. This is directly related to the name field on the Order resource. |
| Default address | The default address for the customer. The default address has the following properties: - ID - First name - Last name - Name - Company - Address 1 - Address 2 - City - Province code - Province - Country code - Country - Country name - Zip - Phone - Default |
| Addresses | A list of the ten most recently updated addresses for the customer. Each address has the following properties: - ID - First name - Last name - Name - Company - Address 1 - Address 2 - City - Province code - Province - Country code - Country - Country name - Zip - Phone - Default |
| Metafields | A list of metafields for the customer. Each metafield has the following properties: - ID - Key - Metafield name - Value - Value type - Description - Owner - ID - Owner resource - Created at - Updated at |

---
