---
url: 'https://docs.workato.com/en/connectors/stripe.md'
description: >-
  Connect Stripe to Workato to automate payment processing, payouts, and
  financial workflows.
---

# Stripe

[Stripe](https://stripe.com/) provides a fast and secure payment processing platform with low- and no-code configuration options. Stripe allows you to accept payments, send payouts, and automate financial processes. For example, a B2B business can use Stripe to collect one-time or recurring payments from customers.

> **DEPRECATION NOTICE: STRIPE EXTENSIONS**
> 
> All Stripe connections created before **December 10, 2024** used Stripe extensions, which Stripe sunset on **January 1, 2025**.
> 
> Migrate extension-based connections to [Stripe Apps](https://stripe.com/apps) to avoid disruptions. Refer to the [Stripe Apps migration guide](/en/connectors/stripe/migration) for detailed migration steps.

## API version

The Stripe connector uses the [Stripe REST API v1](https://stripe.com/docs/api). This API offers a comprehensive set of tools and functionalities that help platforms and marketplaces manage and route payments, in addition to verifying seller identities.

## Connection setup

Workato supports two methods for authenticating to Stripe: [API key](#api-key) or [Authorization code grant](#authorization-code-grant).

### API key

Complete the following steps to connect Workato to Stripe using an API key:

### Authorization code grant

Complete the following steps to create a Stripe connection in Workato.

## Locate Stripe Customer ID

Several actions for the Stripe connector require your Customer ID. Complete the following steps to find your Stripe Customer ID:

1. Log in to your Stripe account.
   
2. Click **Customers** in the left-side navigation menu.
   
3. Select the customer you plan to use from the **Customers** table.
   
4. Go to the **Details** section and copy the **Customer ID**.

---
