---
url: 'https://docs.workato.com/en/connectors/tango_card.md'
description: >-
  The Tango Card connector lets you automate rewards workflows: create and
  resend gift card orders, search processed orders, and get account details.
---

# Tango Card: Rewards Made Easy

[Tango Card](https://www.tangocard.com): Rewards Made Easy.

This connector allows you to plug in to Tango Card to power rewards and incentives in today’s apps and platforms. Drive consumer and employee engagement with gift cards that are easy to send and awesome to receive!

## API version

The Tango Card connector uses the [Tango Card RaaS® API](https://developers.tangocard.com/docs/getting-started).

## How to connect Tango Card on Workato

The Tango Card Connector uses BasicAuth authentication to authenticate with the RaaS API.

![Basic Auth on TC connector](/assets/connection.7kukUlos.png)

| Connection fields | Description |
| --- | --- |
| Connection name | Give this Tango Card connection a unique name. |
| Platform name | Enter the value provided by Tango Card within your free Rewards Genius account. If you don’t already have a Rewards Genius account, [sign up for a Rewards Genius account](https://www.rewardsgenius.com/signup/). |
| Platform Access Key (API Key) | Enter the value securely provided by Tango Card within your Rewards Genius account. Email [sales@tangocard.com](mailto:sales@tangocard.com) to gain access to your key. |
| Environment | Choose **Sandbox** to use fake funds for testing. Choose **Production** to place live orders, which will deduct funds from your Tango Card balance. |

## How to use the Tango Card connector

There are no Triggers needed. The primary Action is **Create an order in Tango Card**.

Primary Action

- _Create an order in Tango Card_: Create an order to be emailed to a recipient.

Secondary Actions

- _Search orders in Tango Card_: Get a list of processed orders.
- _Resend an order in Tango Card_: Resend a processed order to the same email address or a different email.
- _Get account by ID in Tango Card_: Retrieve information for a specific Tango Card account, such as current account balance.

## Creating an order with the Tango Card connector

1. First, enter the Tango Card account identifier, gift card amount, and customer identifier.
   
   ![Create order](/assets/create-order.BHK9o5Kx.png)
   
2. Next, configure your email and Unique Tango Card ID fields.
   
   - Select **Yes** for the `Send Email` configuration and the reward email will be sent by Tango Card to the recipient. _This is our recommendation for most programs._ Please contact Tango Card to learn more about this option.
   - Enter the Unique Tango Card ID (UTID) for the gift card item to be sent. This identifier can be found within Rewards Genius.
   
   ![Send Email](/assets/send-email.DOK3kccH.png)
   

## Tango Card terminology

The Tango Card connector uses the following terms:

| Term | Meaning |
| --- | --- |
| UTID | Unique Tango ID: This determines the merchant gift card to send. |
| ETID | Email Template ID: This determines the email template on which the gift card will be delivered. |
| Account Identifier | Your Tango Card Account ID. |
| Customer Identifier | Your Tango Card Customer ID. In Rewards Genius, this is also known as the Group Identifier. |
| Send Email | Boolean: Should Tango Card send a reward email? If set to ‘No,’ reward delivery must be handled in another step. |

---
