---
url: 'https://docs.workato.com/en/connectors/aconex.md'
description: >-
  Aconex is a cloud-based project management and collaboration platform for the
  construction and engineering industries. The Aconex connector helps you manage
  documents, workflows, and communications across project teams globally.
---

# Aconex

[Aconex](https://www.oracle.com/construction-engineering/aconex/) is a cloud-based project management and collaboration platform for construction and engineering industries. The Aconex connector helps you manage documents, workflows, and communications across project teams globally.

This connector has the following capabilities:

- Monitor and retrieve new updated documents in real-time
- Download document files from Aconex projects
- Track document modifications with timestamps
- Integrate Aconex documents with other business systems

This connector supports the following objects:

- Documents
- Document files

## Install Aconex from the community library

Complete the following steps to install the Aconex connector from the [community library](https://www.workato.com/browse/connectors):

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

The Aconex connector supports the following authentication types:

- [OAuth 2.0 authentication](#oauth-2)
- [Basic authentication](#basic-auth)

### OAuth 2.0 authentication

Workato recommends using OAuth 2.0 authentication. OAuth 2.0 authentication provides security by using an access token to identify the authenticated user.

#### Set up OAuth 2.0 authentication

Complete the following steps to set up a connection using OAuth 2.0 authentication:

1. Sign into your Aconex account.
   
2. Create a new OAuth client.
   
   1. Select **OAuth Clients** from the main menu.
      
   2. Click **Add** to create a new OAuth client or select an existing OAuth client.
      
   3. Enter a **Name** for your OAuth client.
      
   4. Enter a **Description** for your OAuth client.
      
   5. Select the **Resource application** to connect to.
      
   6. Select the integration **Type** to register.
      
   7. Click the **eye icon** on the newly created OAuth client to view the client secret.
      
3. Identify your **Lobby URL**. Your lobby URL varies based on the type of Aconex instance you are using. The lobby URL for all commercial instances is `https://constructionandengineering.oraclecloud.com`. The lobby URL for Aconex Early Access instances is `https://constructionandengineering-ea.oraclecloud.com`.
   
4. Identify your Aconex instance hostname. Your hostname is found in you Aconex login URL. For example, if the login link is `eu1.aconex.com`, the instance hostname is `eu1`.
   

#### Connect to Aconex using OAuth 2.0

Complete the following steps to set up an OAuth 2.0 connection to Aconex in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Aconex` and select it as your app on the **New Connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Aconex](/assets/aconex-connection-setup.BynVQYyK.png)_Connect to Aconex_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **OAuth 2.0**.
   
6. Use the **Lobby URL** drop-down menu to select the Oracle construction and engineering lobby URL.
   
7. Enter the Aconex instance hostname, such as `us1.aconex.com`, in the **Instance Hostname** field.
   
8. Enter the OAuth 2.0 client ID from your registered web server app in the **Client ID** field.
   
9. Enter the client secret from your registered web server app in the **Client secret** field.
   
10. Click **Connect**.
    

### Basic authentication

Use basic authentication when you are setting up non-interactive integrations, with no user interface, in Aconex. Workato doesn't recommend using basic authentication with applications where users enter Aconex user account credentials.

#### Set up basic authentication

Complete the following steps to set up basic authentication in Aconex:

1. Identify your Aconex instance hostname. Your hostname is found in you Aconex login URL. For example, if the login link is `eu1.aconex.com`, the instance hostname is `eu1`.
   
2. Identify your Aconex username. This is the name you use to sign in to your Aconex account. Save this username to use when creating a connection in Workato.
   
3. Identify your Aconex password. This is the password you use to sign in to your Aconex account. Save this password to use when creating a connection in Workato.
   
4. Create an integration ID.
   
   1. Sign in to your Aconex account.
      
   2. Click **Setup >Integration IDs**.
      
   3. Click **Create Integration ID**.
      
   4. Enter a **Name** for your integration ID.
      
   5. Enter a **Description** for your Integration ID.
      
   6. Click to accept the Aconex terms of use. Refer to the [Aconex documentation](https://help.aconex.com/apis/create-an-integration-id-for-basic-auth/) for more information about Integration IDs.
      

#### Connect to Aconex using basic authentication

Complete the following steps to set up a basic authentication connection to Aconex in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Aconex` and select it as your app on the **New Connection** page.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Connect to Aconex](/assets/aconex-connection-setup.BynVQYyK.png)_Connect to Aconex_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Basic authentication**.
   
6. Enter the **Instance hostname** for your Aconex instance.
   
7. Enter your **Username** for your Aconex account.
   
8. Enter the **Password** for your Aconex account.
   
9. Enter the **Integration ID** for your Aconex instance.
   
10. Click **Connect**.

---
