---
url: 'https://docs.workato.com/en/connectors/tiktok-shop.md'
description: >-
  Connect TikTok Shop to Workato to automate e-commerce workflows, monitoring
  and retrieving order information from the in-app selling platform.
---

# TikTok Shop

[TikTok Shop](https://seller.tiktok.com/) is an e-commerce platform integrated into TikTok that allows businesses and creators to sell directly to the app's users. Use this connector to monitor and retrieve information about orders.

## Prerequisites

Before using the TikTok Shop connector in Workato, ensure you have an active [developer account](https://partner.tiktokshop.com/docv2/page/6789f73f18828103147a8ca1) in the [TikTok Shop Partner Center](https://partner-sso.tiktok.com/account/login).

Complete the following steps to retrieve the **App key** and **App Secret** required to establish a connection to TikTok Shop in Workato:

1. Sign in to the [TikTok Shop Partner Center](https://partner-sso.tiktok.com/account/login).
   
2. Go to the **App & Service** page.
   
   ![TikTok Shop account](/assets/tiktok-shop-account.D-AUdnI_.png)_TikTok Shop Account_
   
3. Select an existing app or refer to TikTok's [Create a TikTok Shop App (OAuth client)](https://partner.tiktokshop.com/docv2/page/6789f74e23ae4b030c389e76) guide to create a new app.
   
4. Ensure that your app has **Enable API** toggled and that the **Redirect URL** is correct.
   
5. Go to the **Developing** tab for your app.
   
6. Copy and save your **App key** and **App Secret** for future use in Workato.
   

> **SELLER ACCOUNTS**
> 
> Refer to TikTok's [Create a test seller account](https://partner.tiktokshop.com/docv2/page/6789f75a38b3f103167690dc#Back%20To%20Top) guide to create a test seller account if you require sample data and don't have sellers or creators to collect it from.

## Connection Setup

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **TikTok Shop** as your connection in the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![TikTok Shop connection setup](/assets/tiktok-shop-connection-setup.wSJ0oni-.png)_TikTok Shop connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **App key** for your TikTok Shop account. Refer to [Prerequisites](#prerequisites) to retrieve this value.
   
6. Enter the **App Secret** for your TikTok Shop account. Refer to [Prerequisites](#prerequisites) to retrieve this value.
   
7. Click **Connect**.

---
