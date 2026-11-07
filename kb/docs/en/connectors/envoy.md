---
url: 'https://docs.workato.com/en/connectors/envoy.md'
description: >-
  The Envoy connector lets you automate workplace workflows: create, update,
  delete, search, and get records, and trigger on new or updated events.
---

# Envoy

[Envoy](https://envoy.com) is a workplace management platform that helps teams coordinate office space, desk reservations, and meeting room bookings. It includes tools for visitor management, employee check-in, workspace management, and capacity planning.

## Prerequisites

To establish an Envoy connection in Workato, you must enroll in Envoy's developer program and complete the following steps:

- [Create an Envoy app](#creating-an-app)

### Create an Envoy app

Complete the following steps to create an Envoy app:

1. Sign in to the Envoy [Dev Dashboard](https://dashboard.envoy.com/dev-dashboard).
   
   > **INFO**
   > 
   > "Apps" may appear as "Integrations" on your dashboard.
   
2. Click **Create New**.
   
3. Name your app/integration.
   
4. Select API scopes. This step is optional but recommended.
   
5. In the **Where will customers install your app?** field, select **Externally using OAuth2**.
   
6. Enter the Workato callback URL `https://www.workato.com/oauth/callback`.
   
7. Fill out the rest of the form and click **Save** when you're done.
   
8. Copy the **Client ID**, **Client Secret**, and **Client API Key** and store them securely. These values are required to establish the connection in Workato.
   

You can modify your app at any time by clicking **Configure**.

## How to connect to Envoy

The Envoy connector supports the following authentication methods:

- [OAuth 2.0](#oauth-2)
- [API key](#api-key)

### OAuth 2.0 authentication

Complete the following steps to connect to Envoy using OAuth 2.0 authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Envoy** as your connection on the **New connection** page.
   
3. Provide a unique name for your connection in the **Connection name** field.
   
   ![Connect to Envoy using OAuth 2.0 authentication](/assets/envoy-connection-oauth2.tsKo8H91.png)_Connect to Envoy using OAuth 2.0 authentication_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store your connection.
   
5. Select **OAuth2** as the **Authentication type**.
   
6. Enter the **Client ID** and **Client secret** for your Envoy app.
   
7. Select the **Scopes** to request for the Envoy connection if you didn't define scopes when creating the app. If not specified, Workato requests the minimum required scopes.
   
8. Click **Connect**.
   

### API key authentication

Complete the following steps to connect to Envoy using API key authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Envoy** as your connection on the **New connection** page.
   
3. Provide a unique name for your connection in the **Connection name** field.
   
   ![Connect to Envoy using API key authentication](/assets/envoy-connection-api-key.BnkTNLat.png)_Connect to Envoy using API key authentication_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store your connection.
   
5. Select **API Key** as the **Authentication type**.
   
6. Enter the **Client API Key** for your Envoy app.
   
7. Click **Connect**.

---
