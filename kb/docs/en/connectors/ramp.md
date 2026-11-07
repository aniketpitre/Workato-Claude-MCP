---
url: 'https://docs.workato.com/en/connectors/ramp.md'
description: >-
  Automate spend management in Ramp: manage cards, transactions, reimbursements,
  vendors, and more from Workato recipes.
---

# Ramp

[Ramp](https://ramp.com/welcome) automates finance operations so businesses spend less time and money on expenses. The Ramp connector lets you create, retrieve, update, delete, and search Ramp records directly from Workato recipes. Refer to the Ramp [REST API](https://docs.ramp.com/developer-api/v1/api/) documentation for endpoint details.

Use the Ramp connector to:

- Manage accounts, cards, and spend limits.
- Track transactions, receipts, and reimbursements.
- Manage departments, locations, and subsidiaries.
- Manage users, vendors, and merchants.

You can also use [custom actions](/en/developing-connectors/custom-actions) to build a custom HTTP request to any Ramp API endpoint.

## Install Ramp from the community library

Complete the following steps to install the Ramp connector from the [community library](https://www.workato.com/browse/connectors):

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

The Ramp connector supports the following authentication types:

- [Authorization code](#authorization-code)
- [Client credentials](#client-credentials)

### Authorization code authentication

Use authorization code to connect as a specific Ramp user. Ramp redirects the user to sign in and approve access.

#### Ramp setup for authorization code authentication

Complete the following steps to create a Ramp app for authorization code authentication:

1. Open the [Developer apps](https://app.ramp.com/settings/ramp-developer/apps) page in Ramp.
   
2. Click **Start building** for your first app, or **Create new app** for additional apps.
   
3. Enter a descriptive name for your app, for example `Workato Integration`.
   
4. Select the checkbox to accept **Ramp's Developer Terms of Service**.
   
5. Click **Create app**.
   
6. Select your newly created app.
   
7. Enable **Authorization code** and **Refresh token** under **Grant types**.
   
8. Optional. Go to **Scopes** and click **Configure allowed scopes** to select scopes.
   
9. Copy and save the **Client ID** and **Client secret** for use in Workato.
   

#### Connect to Ramp using authorization code

Complete the following steps to set up an authorization code connection to Ramp in Workato:

1. Click **Create > Connection**.
   
2. Search for `Ramp` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Ramp connection setup with authorization code](/assets/ramp-auth-code-connect.BDxWTsoM.png)_Ramp authorization code connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select **Cloud**, or select an on-prem group to connect through an on-prem agent.
   
6. Use the **Auth type** drop-down menu to select **Authorization code**.
   
7. Enter the **Client ID** and **Client secret**. Refer to [Ramp setup for authorization code authentication](#auth-code-setup) for more information.
   
8. Use the **Environment** drop-down menu to select **Production** or **Sandbox**.
   
9. Optional. Use the **Scopes** field to select one or more scopes. The connection is granted every available scope if you don't select any.
   
10. Click **Connect**.
    
11. Sign in to Ramp when prompted, and click **Allow** to grant access.
    

### Client credentials authentication

Use client credentials to connect without a specific user, for server-to-server automation.

#### Ramp setup for client credentials authentication

Complete the following steps to create a Ramp app for client credentials authentication:

1. Open the [Developer apps](https://app.ramp.com/settings/ramp-developer/apps) page in Ramp.
   
2. Click **Start building** for your first app, or **Create new app** for additional apps.
   
3. Enter a descriptive name for your app, for example `Workato Integration`.
   
4. Select the checkbox to accept **Ramp's Developer Terms of Service**.
   
5. Click **Create app**.
   
6. Select your newly created app.
   
7. Enable **Client credentials** under **Grant types**.
   
8. Optional. Go to **Scopes** and click **Configure allowed scopes** to select scopes.
   
9. Copy and save the **Client ID** and **Client secret** for use in Workato.
   

#### Connect to Ramp using client credentials

Complete the following steps to set up a client credentials connection to Ramp in Workato:

1. Click **Create > Connection**.
   
2. Search for `Ramp` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Ramp connection setup with client credentials](/assets/ramp-client-credentials-connect.CXlBFJnH.png)_Ramp client credentials connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select **Cloud**, or select an on-prem group to connect through an on-prem agent.
   
6. Use the **Auth type** drop-down menu to select **Client credentials**.
   
7. Enter the **Client ID** and **Client secret**. Refer to [Ramp setup for client credentials authentication](#client-credentials-setup) for more information.
   
8. Use the **Environment** drop-down menu to select **Production** or **Sandbox**.
   
9. Optional. Use the **Scopes** field to select one or more scopes. The connection is granted every available scope if you don't select any.
   
10. Click **Connect**.

---
