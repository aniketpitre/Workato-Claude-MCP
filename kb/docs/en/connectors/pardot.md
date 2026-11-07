---
url: 'https://docs.workato.com/en/connectors/pardot.md'
description: >-
  Create, update, delete, and search objects, get object details, and trigger on
  new or updated objects in Salesforce Account Engagement (Pardot).
---

# Salesforce Account Engagement (Pardot)

[Salesforce Account Engagement (Pardot)](https://www.pardot.com/about-pardot/) is a marketing automation platform by Salesforce that provides email automation, targeted email campaigns, and lead management for B2B sales and marketing teams.

## Install Salesforce Account Engagement (Pardot) from the community library

Complete the following steps to install the Salesforce Account Engagement (Pardot) connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

## Connection setup

The Salesforce Account Engagement (Pardot) connector supports the following authentication types:

- [OAuth 2.0 (Password)](#oauth-password)
- [OAuth 2.0 (Authorization Code)](#oauth-auth-code)
- [OAuth 2.0 (Authorization Code with PKCE)](#oauth-auth-code-pkce)
- [OAuth 2.0 (Client Credentials)](#oauth-client-credentials)

All authentication types require the following:

- A Salesforce admin to create a connected app.
- A Salesforce user account linked to an Account Engagement user.
- Your Account Engagement business unit ID.

### Retrieve your business unit ID

Complete the following steps to retrieve your business unit ID:

1. Log in to your [Account Engagement](https://pi.pardot.com/) account.
   
2. Go to **Pardot > Settings > Users**.
   
3. Verify that the CRM username of the selected user is synced with a Salesforce user.
   
4. Log in to your Salesforce account as an admin.
   
5. Go to **Setup**.
   
6. Enter `Pardot Account Setup` in the **Quick Find** box and select it.
   
7. Copy the **Business unit ID** for your business unit. The ID begins with `0Uv` and has 18 characters.
   

### Minimum and default scopes

The Salesforce Account Engagement (Pardot) connector requires the following scopes in your Salesforce connected app:

| Scope | Description | Required for |
| --- | --- | --- |
| **Access Pardot Services** (`pardot_api`) | Allows the app to access Account Engagement APIs. | All authentication types. |
| **Perform requests on your behalf at any time** (`refresh_token`, `offline_access`) | Allows the app to obtain a refresh token so the connection stays valid after the access token expires. | OAuth 2.0 (Password), OAuth 2.0 (Authorization Code), and OAuth 2.0 (Authorization Code with PKCE). |

### OAuth 2.0 (Password) authentication

Use OAuth 2.0 (Password) authentication to connect with the username and password of a Salesforce user account linked to an Account Engagement user.

#### Salesforce setup

Complete the following steps to set up Salesforce for OAuth 2.0 (Password) authentication:

1. Go to **Home > App Manager > New Connected App** to create a connected app.
   
2. Enter basic details such as application name, API name, and contact email.
   
3. Select **Enable OAuth settings**.
   
4. Enter `https://www.workato.com/oauth/callback` in the **Callback URL** field.
   
5. Add the OAuth scopes. Refer to [Minimum and default scopes](#minimum-scopes) for more information.
   
6. Save the connected app.
   
7. Copy the **Consumer Key** and **Consumer Secret** for use in Workato. Refer to the Salesforce [Authentication](https://developer.salesforce.com/docs/marketing/pardot/guide/authentication.html) documentation for more information.
   

#### Connect to Salesforce Account Engagement (Pardot) using OAuth 2.0 (Password)

Complete the following steps to set up an OAuth 2.0 (Password) connection to Salesforce Account Engagement (Pardot) in Workato:

1. Click **Create > Connection**.
   
2. Search for `Salesforce Account Engagement (Pardot)` and select it as your app.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Salesforce Account Engagement (Pardot) OAuth 2.0 (Password) connection](/assets/pardot-oauth2-password-connection.B0BS6IIq.png)_Salesforce Account Engagement (Pardot) OAuth 2.0 (Password) connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication** drop-down menu to select **OAuth 2.0 (Password)**.
   
6. Use the **API version** drop-down menu to select the Account Engagement API version.
   
7. Use the **Environment** drop-down menu to select **Production**, **Developer Org**, or **Sandbox**. You must select an environment to connect.
   
8. Enter the **Consumer key** and **Consumer secret** from your Salesforce connected app. Refer to [Salesforce setup](#oauth-password-setup) for more information.
   
9. Enter the **Email** and **Password** of your Salesforce user account linked to an Account Engagement user.
   
10. Use the **Salesforce domain** drop-down menu to select **Production Account or Pardot Developer** or **Sandbox**.
    
11. Enter the **Business unit ID** that you copied from your Account Engagement account. Refer to [Retrieve your business unit ID](#business-unit-id) for more information.
    
12. Click **Connect**.
    

### OAuth 2.0 (Authorization Code) authentication

Use OAuth 2.0 (Authorization Code) authentication to authorize Workato to access Account Engagement on behalf of a user, without sharing the user's password with Workato.

#### Salesforce setup

Complete the following steps to set up Salesforce for OAuth 2.0 (Authorization Code) authentication:

1. Go to **Home > App Manager > New Connected App** to create a connected app.
   
2. Enter basic details such as application name, API name, and contact email.
   
3. Select **Enable OAuth settings**.
   
4. Enter `https://www.workato.com/oauth/callback` in the **Callback URL** field.
   
5. Add the OAuth scopes. Refer to [Minimum and default scopes](#minimum-scopes) for more information.
   
6. Save the connected app.
   
7. Copy the **Consumer Key** and **Consumer Secret** for use in Workato. Refer to the Salesforce [Authentication](https://developer.salesforce.com/docs/marketing/pardot/guide/authentication.html) documentation for more information.
   

#### Connect to Salesforce Account Engagement (Pardot) using OAuth 2.0 (Authorization Code)

Complete the following steps to set up an OAuth 2.0 (Authorization Code) connection to Salesforce Account Engagement (Pardot) in Workato:

1. Click **Create > Connection**.
   
2. Search for `Salesforce Account Engagement (Pardot)` and select it as your app.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Salesforce Account Engagement (Pardot) OAuth 2.0 (Authorization Code) connection](/assets/pardot-oauth2-auth-code-connection.DIxp1MXU.png)_Salesforce Account Engagement (Pardot) OAuth 2.0 (Authorization Code) connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication** drop-down menu to select **OAuth 2.0 (Authorization Code)**.
   
6. Use the **API version** drop-down menu to select the Account Engagement API version.
   
7. Use the **Environment** drop-down menu to select **Production**, **Developer Org**, or **Sandbox**. You must select an environment to connect.
   
8. Enter the **Consumer key** and **Consumer secret** from your Salesforce connected app. Refer to [Salesforce setup](#oauth-auth-code-setup) for more information.
   
9. Enter the **Account Engagement business unit ID** that you copied from your Account Engagement account. Refer to [Retrieve your business unit ID](#business-unit-id) for more information.
   
10. Click **Connect**.
    
11. Sign in to Salesforce when prompted, and click **Allow** to grant access.
    

### OAuth 2.0 (Authorization Code with PKCE) authentication

Use OAuth 2.0 (Authorization Code with PKCE) authentication if your Salesforce connected app requires Proof Key for Code Exchange (PKCE).

#### Salesforce setup

Complete the following steps to set up Salesforce for OAuth 2.0 (Authorization Code with PKCE) authentication:

1. Go to **Home > App Manager > New Connected App** to create a connected app.
   
2. Enter basic details such as application name, API name, and contact email.
   
3. Select **Enable OAuth settings**.
   
4. Enter `https://www.workato.com/oauth/callback` in the **Callback URL** field.
   
5. Add the OAuth scopes. Refer to [Minimum and default scopes](#minimum-scopes) for more information.
   
6. Select **Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows**.
   
7. Save the connected app.
   
8. Copy the **Consumer Key** and **Consumer Secret** for use in Workato. Refer to the Salesforce [Authentication](https://developer.salesforce.com/docs/marketing/pardot/guide/authentication.html) documentation for more information.
   

#### Connect to Salesforce Account Engagement (Pardot) using OAuth 2.0 (Authorization Code with PKCE)

Complete the following steps to set up an OAuth 2.0 (Authorization Code with PKCE) connection to Salesforce Account Engagement (Pardot) in Workato:

1. Click **Create > Connection**.
   
2. Search for `Salesforce Account Engagement (Pardot)` and select it as your app.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Salesforce Account Engagement (Pardot) OAuth 2.0 (Authorization Code with PKCE) connection](/assets/pardot-oauth2-auth-code-pkce-connection.CD0v7b6L.png)_Salesforce Account Engagement (Pardot) OAuth 2.0 (Authorization Code with PKCE) connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication** drop-down menu to select **OAuth 2.0 (Authorization Code with PKCE)**.
   
6. Use the **API version** drop-down menu to select the Account Engagement API version.
   
7. Use the **Environment** drop-down menu to select **Production**, **Developer Org**, or **Sandbox**. You must select an environment to connect.
   
8. Enter the **Consumer key** and **Consumer secret** from your Salesforce connected app. Refer to [Salesforce setup](#oauth-auth-code-pkce-setup) for more information.
   
9. Enter the **Account Engagement business unit ID** that you copied from your Account Engagement account. Refer to [Retrieve your business unit ID](#business-unit-id) for more information.
   
10. Click **Connect**.
    
11. Sign in to Salesforce when prompted, and click **Allow** to grant access.
    

### OAuth 2.0 (Client Credentials) authentication

Use OAuth 2.0 (Client Credentials) authentication for server-to-server connections that don't require a user to sign in. Workato requests a new access token with your client credentials when the previous token expires. This flow doesn't issue a refresh token.

#### Salesforce setup

Complete the following steps to set up Salesforce for OAuth 2.0 (Client Credentials) authentication:

1. Go to **Home > App Manager > New Connected App** to create a connected app.
   
2. Enter basic details such as application name, API name, and contact email.
   
3. Select **Enable OAuth settings**.
   
4. Enter `https://www.workato.com/oauth/callback` in the **Callback URL** field.
   
5. Add the `pardot_api` scope. Refer to [Minimum and default scopes](#minimum-scopes) for more information.
   
6. Select **Enable Client Credentials Flow**.
   
7. Save the connected app.
   
8. Open the connected app's policies and set **Run As** to an integration user that has Account Engagement access.
   
9. Copy the **Consumer Key** and **Consumer Secret** for use in Workato.
   
10. Go to **Setup**.
    
11. Enter `My Domain` in the **Quick Find** box, and copy your My Domain hostname. For example, `acme.my.salesforce.com`.
    

#### Connect to Salesforce Account Engagement (Pardot) using OAuth 2.0 (Client Credentials)

Complete the following steps to set up an OAuth 2.0 (Client Credentials) connection to Salesforce Account Engagement (Pardot) in Workato:

1. Click **Create > Connection**.
   
2. Search for `Salesforce Account Engagement (Pardot)` and select it as your app.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Salesforce Account Engagement (Pardot) OAuth 2.0 (Client Credentials) connection](/assets/pardot-oauth2-client-cred-connection.Ds04QkMU.png)_Salesforce Account Engagement (Pardot) OAuth 2.0 (Client Credentials) connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication** drop-down menu to select **OAuth 2.0 (Client Credentials)**.
   
6. Use the **API version** drop-down menu to select the Account Engagement API version.
   
7. Use the **Environment** drop-down menu to select **Production**, **Developer Org**, or **Sandbox**. You must select an environment to connect.
   
8. Enter the **Consumer key** and **Consumer secret** from your Salesforce connected app. Refer to [Salesforce setup](#oauth-client-credentials-setup) for more information.
   
9. Enter your **Salesforce My Domain** hostname without `https://` or a trailing slash. For example, `acme.my.salesforce.com`, `acme-dev-ed.develop.my.salesforce.com`, or `acme--sandbox.sandbox.my.salesforce.com`.
   
10. Enter the **Account Engagement business unit ID** that you copied from your Account Engagement account. Refer to [Retrieve your business unit ID](#business-unit-id) for more information.
    
11. Click **Connect**.

---
