---
url: 'https://docs.workato.com/en/connectors/calendly.md'
description: >-
  The Calendly connector lets you automate scheduling workflows: trigger recipes
  on new scheduled events and list your available event types.
---

# Calendly

[Calendly](https://calendly.com/) is a scheduling automation platform that allows users to easily book meetings and appointments online without the need for back-and-forth emails. It syncs with your calendar, allowing you to share a link where others can select a time that works for everyone.

## Prerequisites

To establish a Calendly connection in Workato, complete the steps that correspond to the authentication method you plan to use:

- If you plan to use a **personal access token**, [create a personal access token](#create-personal-access-token).
- If you plan to use **OAuth 2.0**, [generate an OAuth client ID and secret](#generate-oauth-credentials).

### Create a personal access token

Complete the following steps to create a personal access token in Calendly:

1. [Sign in](https://calendly.com/login) to your Calendly account.
   
2. Select [Integrations & apps](https://calendly.com/integrations).
   
3. Search for and select [API and webhooks](https://calendly.com/integrations/api_webhooks).
   
4. Generate a new token. If you don't have an existing personal access token, select **Get a token now**. If you already have one, select **Generate new token**.
   
5. Enter a token name and click **Create token**.
   
6. Click **Copy token** to retrieve the token.
   

### Generate an OAuth client ID and secret

Complete the following steps to generate your OAuth credentials in Calendly:

1. Go to the [Calendly Developer](https://developer.calendly.com/) page.
   
2. Sign in to your developer account or create a new one.
   
   > **DEVELOPER ACCOUNTS**
   > 
   > Calendly developer accounts are separate from your Calendly user account.
   
3. Select your profile icon and go to **My apps**.
   
4. Click **Create new app** to create an OAuth application.
   
5. Enter the name of your application in the **Name of app** field. For example, `Workato`.
   
6. Select **Web** in the **Kind of app** field.
   
7. Select the environment you plan to associate your application with:
   
   - **Sandbox**
   - **Production**
8. Enter `https://www.workato.com/oauth/callback` in the **Redirect URI** field.
   
9. Click **Save & continue**.
   
10. Copy your **Client ID**, **Client Secret**, and **Webhook signing key**. Store these values securely, as you won't be able to access the **Client ID** and **Client Secret** again.
    

## How to connect to Calendly

The Calendly connector supports the following authentication methods:

- [Personal access token](#personal-access-token)
- [OAuth 2.0](#oauth-2-0)

### Personal access token

Complete the following steps to set up a personal access token authentication connection to { $frontmatter.connector\_name }} in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Calendly` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Personal access token**.
   
6. Enter the **Personal access token**.
   
   ![Connect to Calendly using personal access token authentication](/assets/calendly-pat.CHojATVR.png)_Connect to Calendly using personal access token authentication_
   
7. Click **Connect**.
   

### OAuth 2.0

Complete the following steps to set up an OAuth 2.0 authentication connection to Calendly in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Calendly` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **OAuth 2.0**.
   
6. Enter the **Client ID** and associated **Client secret**.
   
   ![Connect to Calendly using OAuth 2.0 authentication](/assets/calendly-oauth2.6CfIiBOR.png)_Connect to Calendly using OAuth 2.0 authentication_
   
7. Click **Connect**.

---
