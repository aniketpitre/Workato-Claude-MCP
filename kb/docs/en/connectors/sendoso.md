---
url: 'https://docs.workato.com/en/connectors/sendoso.md'
description: >-
  The Sendoso connector enables you to automate direct mail and gifting
  workflows and trigger recipes on new users or send analytics updates.
---

# Sendoso

[Sendoso](https://sendoso.com/) is the leading Sending Platform that delivers modern direct mail, personalized gifts, eGifts, and other Physical Impressions™ at scale. Use the triggers in this connector to run a recipe when a new user is added or the send analytics are updated in Sendoso. Use the actions to manage your custom gift campaigns.

> **INFO**
> 
> This connector is released to the [community](https://app.workato.com/custom_adapters/22034/details?community=true). You have to [install it to your workspace](/en/developing-connectors/community/community#how-do-i-find-and-install-community-connectors) before using it.

## How to connect to Sendoso on Workato

Complete the following steps to set up your Sendoso connection:

1. Email `developers@sendoso.com` to request a client ID and client secret for your account.
   
2. [Install](https://app.workato.com/custom_adapters/22034/details?community=true) the connector from the community library.
   
3. Click **Release latest version** to use the connector in a recipe.
   
4. Create a new recipe and select a Sendoso trigger or action.
   
5. Provide a **Connection name** that identifies the instance Workato is connected to.
   
   ![Set up your Sendoso connection](/assets/sendoso-connection.C_NE-yj5.png)_Set up your Sendoso connection_
   
6. Enter your client ID in the **Client ID** field.
   
7. Enter your client secret in the **Client Secret** field.
   
8. Provide your Sendoso environment in the **Environment** field. You can find this in the Sendoso URL. For example: `https://app.sendoso.com`.
   
9. Click **Connect**.
   

## Using Sendoso with other apps

Sendoso is frequently used in recipes with a CRM app, such as in the following example recipes:

- [Send gift to new/updated opportunity](https://app.workato.com/recipes/1481742?st=df8655): sends a gift to a contact from Microsoft Dynamics 365 if the opportunity is valued at $10000 or more.
- [Update Microsoft Dynamics 365 with gift status](https://app.workato.com/recipes/1487243?st=226020): whenever a gift is sent, clicked, or delivered, creates a new contact in Microsoft Dynamics 365 or updates an existing contact and adds a note with the gift status.

> **TIP**
> 
> The Send Analytics trigger output contains the gift recipient’s email but not their name. If Microsoft Dynamics 365 doesn't have a contact with a matching email address, a new contact will be created in Dynamics with the recipient's email as the contact name.

---
