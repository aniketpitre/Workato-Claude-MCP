---
url: 'https://docs.workato.com/en/shopify-api-version-upgrade-faq.md'
description: >-
  Answers to common questions about the Workato Shopify connector API version
  upgrade, including what changes, how it affects you, and required actions.
---

# Shopify - API version upgrade to `2022-07`

## What is the update?

In **April 2023**, we will be upgrading the Shopify API version we are using to the latest stable `2022-07` version. Subsequently, we will be performing such upgrades on an annual basis.

> **Why are we doing this?**
> 
> Shopify generally releases a new version every 3 months, and maintains each release version for a maximum of 12 months. That means that there will be 4 stable versions supported at any point in time.
> 
> Once a released version passed its one year mark, Shopify will no longer maintain that version, and any API calls requesting that version will be **automatically routed to the oldest stable version** currently supported.
> 
> For instance, if the current available stable versions are `2021-01`, `2021-04`, `2021-07`, and `2021-10`, then any API calls requesting for `2020-04` version will be automatically routed to the `2021-01` version by Shopify.
> 
> To balance your convenience against Shopify's mandated version upgrade, we decided to perform the upgrade annually. Should you require a specific API version, you may use **custom action** to override the default version in the `path` parameter.
> 
> You may visit Shopify's [API versioning](https://shopify.dev/api/usage/versioning#release-schedule) page for more information.

## How does this affect me?

### Important action item

1. **Add scopes for fulfillment**: if you are using the “Create fulfillment” order, please add the following scopes into your connection:

- `read_assigned_fulfillment_orders`
- `write_assigned_fulfillment_orders`
- `read_merchant_managed_fulfillment_orders`
- `write_merchant_managed_fulfillment_orders`
- `read_third_party_fulfillment_orders`
- `write_third_party_fulfillment_orders`

Please take note that should you may need to [reconnect to Shopify using one of the new authentication methods](/en/connectors/shopify#how-to-connect-to-shopify-on-workato) we released in Q3 2022.

> **Important Notice**
> 
> It is imperative that the following change is implemented **_before 27 March 2023_**.

### Recommended action items

In addition to the above, it is recommended that you perform the following changes for:

1. **Create fulfillment**: Shopify is removing the endpoint for this action in favor of `fulfillmentOrder`\-based architecture. Unfortunately, the confirmation of the deprecation only came in January 2023. We have released a new “Create fulfillment” action that aligns with Shopify’s new fulfillment order based architecture. Please migrate any running recipes using the old “Create fulfillment” action to the new one at the soonest. More details can be found in this [Shopify Community post](https://community.shopify.com/c/announcements/action-required-migrate-to-fulfillment-orders-api-by-march-31/td-p/1920389).
   
2. **Create transaction:** we will be adding 2 optional fields: `authorization` and `parent ID`. While these are optional, it is recommended to provide at least one of the above parameters as omitting them may result in errors if you also use an order editing app. ![New fields supported](/assets/shopify-api-version-upgrade-faq-create-transaction-new-fields.DaALeR9l.png)_New fields supported_
   

### Other things to take note of

1. **Custom action:** while immediate action is not required, we want to take this time to inform you that Shopify will be removing XML response format starting from version `2022-07`. This means that regardless of the API version you specify in the `path` parameter, requests that expects an XML response will result in a 404 error, while requests that send an XML payload will result in a 415 error.

---
