---
url: 'https://docs.workato.com/en/connectors/gong.md'
description: Connects Workato to Gong to build automations.
---

# Gong

[Gong](https://www.gong.io/) is a revenue intelligence platform that captures customer interactions across phone, web conferencing, and email. Gong understands the content of these interactions and delivers actionable insights. Use the trigger from the Gong connector to run the recipe each time an event occurs in Gong, and the actions to add calls and media, and search for call data.

## API version

The Gong connector uses the [Gong API v2](https://app.gong.io/settings/api/documentation#overview).

## Connection setup

The Gong connector uses OAuth 2.0 authentication.

### Minimum and default scopes

Workato requires the `api:users:read` scope. Refer to the [Gong API documentation](https://app.gong.io/settings/api/documentation#overview) for more detailed information about the available scopes.

### Gong setup

Complete the following steps in Gong to generate credentials:

1. Sign in to your Gong developer instance. Refer to [Request a developer instance](https://help.gong.io/docs/create-an-app-for-gong#request-a-developer-instance) for more information.
   
2. Go to **Admin center**.
   
   ![Admin center](/assets/admin-center.ynD0MeHK.png)_Admin center_
   
3. Click **API** in the **Ecosystem** section.
   
4. Click **CREATE INTEGRATIONS** in the **INTEGRATIONS** tab.
   
5. Complete the **CREATE YOUR GONG INTEGRATION** page, including name, description, and required authorization scopes. Refer to [Submit your integration details to Gong](https://help.gong.io/docs/create-an-app-for-gong?highlight=client%20secret) for more information.
   
   > **SELF-SERVICE (WORKATO FREE, WORKATO PRO, OR DEVELOPER SANDBOX) WORKSPACES**
   > 
   > If you created your workspace as a [Self-service](https://www.workato.com/developers/sandbox) user, use `https://app.trial.workato.com/oauth/callback` as the redirect URI or callback URL when you configure the OAuth integration.
   
6. Click **Save**. Your integration information appears as a new row in the list of integrations.
   
7. Copy and save the **CLIENT ID** and **CLIENT SECRET** for use in Workato.
   

### Connect to Gong with OAuth 2.0

Complete the following steps to connect to Gong in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Gong.io` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Gong](/assets/connect.B5wWXAjX.png)_Connect to Gong_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Expand the **Advanced settings** section to configure **Scopes** for your connection. Workato requests all available scopes by default. You can select granular scopes from the multi-select list to limit access.
   
6. Enter the **Client ID** and **Client secret**. Refer to [Gong setup](#gong-setup) for more information.
   
7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
8. Click **Connect**.
   
9. Sign in to Gong using your credentials when prompted.
   
10. Click **Allow** to provision access to Workato.

---
