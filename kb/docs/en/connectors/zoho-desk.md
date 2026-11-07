---
url: 'https://docs.workato.com/en/connectors/zoho-desk.md'
description: >-
  [Zoho Desk](https://www.zoho.com/en-in/desk/) is a web-based help desk
  software that helps businesses manage customer support. It allows businesses
  to handle customer queries and feedback through multiple channels, including
  email, phone, and social media.
---

# Zoho Desk

[Zoho Desk](https://www.zoho.com/en-in/desk/) is a web-based help desk software that helps businesses manage customer support. It allows businesses to handle customer queries and feedback through multiple channels, including email, phone, and social media.

## Prerequisites

Before using the Zoho Desk connector in Workato, ensure that you have an active Zoho Desk account with permissions to access APIs and permissions to use the Developer Portal. If you do not have an account, follow the steps to [register](https://www.zoho.com/desk/signup.html).

### Registering an Application

Register an app in the Zoho Desk Account to integrate with the Workato platform and automate tasks.

1. Log in to your [Zoho Desk](https://api-console.zoho.com/) account.
   
2. Click **New Client** on the Applications page. ![Zoho Desk API Console](/assets/zohodesk-applications.UGRkrASp.png)_Zoho Desk API Console_
   
3. Select **Server-based Applications** as the Client Type. ![Zoho Desk Applications](/assets/zohodesk-server.B6j6t_Rm.png)_Zoho Desk Applications_
   
4. Enter the **Client Name** and **Homepage URL**.
   
5. Enter your **Authorized Redirect URIs** provided by Workato for OAuth. Refer to the [Workato Redirect URL guide](/en/developing-connectors/registering-new-client#callback-url) for more information. ![Zoho Desk New Application](/assets/zohodesk-new-application.CC3hnJ8x.png)_Zoho Desk New Application_
   
6. Click **Create** > **Continue**.
   
7. Copy the **Client ID** and **Client Secret** and store them in a secure location.
   
8. Click **Save** to complete the app registration.
   

Refer to the [Zoho Desk Documentation](https://desk.zoho.com/DeskAPIDocument#OauthTokens) for more information.

## How to connect to Zoho Desk

Zoho Desk connector supports OAuth2 authentication to connect to Zoho Desk. Follow the steps below to connect to the Zoho Desk connector in Workato.

1. Click **Create** > **Connection**.
   
2. Search for and select **Zoho Desk** as your connection on the New Connection page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Client ID and Client Secret** for your Zoho Desk account, which you saved during the previous steps.
   
6. Select the [**Scopes**](https://desk.zoho.com/support/APIDocument.do#OauthTokens#OAuthScopes) required for your integration. If no scopes are selected, the minimum set of required scopes are automatically applied.
   
7. Select the necessary **Region** required for your integration. If no region is selected, then `US(zoho.com)` will be automatically applied.
   
8. Click on **Connect**.
   

![Zoho Desk Connection Setup](/assets/zohodesk-connection-setup.Cfmy338l.png)_Zoho Desk Connection Setup_

---
