---
url: 'https://docs.workato.com/en/connectors/salesloft.md'
description: >-
  Connect Salesloft to Workato to automate sales engagement workflows across
  your revenue and sales pipeline tools.
---

# Salesloft

[SalesLoft](https://salesloft.com/) is a sales engagement solution offering an end-to-end selling experience from anywhere so you can connect to your customers more often, increase revenue, and build stronger relationships.

## Prerequisites

Complete the following steps to generate credentials required to establish a connection to Salesloft:

1. Navigate to **[Salesloft Account](https://accounts.salesloft.com/) > Your Applications > OAuth Applications > Create New** to create a new application in Salesloft.
   
2. Enter **Name** as the application need and provide a suitable description in the **Description** field.
   
3. Provide the Workato callback URL for your data center. For example, `https://www.workato.com/oauth/callback`. Refer to the [Callback URL](/en/developing-connectors/registering-new-client#callback-url) documentation for more information.
   
4. Select the following application type:
   
   - **No** – this application will be used for internal purposes only.
5. Go to the **Grant type** field and select **Client Credentials**.
   
6. Select the scopes relevant to your application by clicking the checkmark next to the scope. ![Salesloft scopes](/assets/scopes.BCWZ4kEs.png)_Salesloft scopes_
   
7. Click **Submit**.
   
8. Salesloft displays your Application ID (Client ID), Secret (Client secret), and other information. Save the Client ID and Client secret for connection setup in Workato. Refer to the [Salesloft authentication page](https://developers.salesloft.com/docs/platform/api-basics/client-creds/) for more information.
   

### **Steps to connect with Salesloft on Workato**

Workato supports OAuth (Client credentials) authentication to connect to Salesloft. Follow the steps below to establish a connection with Salesloft on Workato.

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Salesloft** as your connection in the New Connection page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Provide the **Client ID** and **Client secret** from your Salesloft account, retrieved in the previous step.
   
6. Click **Connect** to establish the connection.
   
   ![Salesloft connection](/assets/connection.BU7qDari.png)_Salesloft connection_

---
