---
url: 'https://docs.workato.com/en/connectors/canva-connect.md'
description: >-
  Canva Connect is an online template editor that helps you create social media
  graphics, presentations, and other designs, with collaboration features for
  team workspaces.
---

# Canva Connect

[Canva](https://www.canva.com/) is an online template editor that helps you create social media graphics, presentations, and other designs, with collaboration features for team workspaces. The Canva Connect connector uses the Canva Connect APIs to let you create, import, and export designs, upload and manage assets, autofill brand templates, and manage folders and comments in Canva from Workato recipes.

## Install Canva Connect from the community library

Complete the following steps to install the Canva Connect connector from the [community library](https://www.workato.com/browse/connectors):

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

The Canva Connect connector uses OAuth 2.0 authentication.

### Minimum and default scopes

Canva Connect grants the connection every available scope if you don't select any scopes when you connect. Available scopes include:

- `Asset:read`
- `Asset:write`
- `Brandtemplate:content:read`
- `Brandtemplate:meta:read`
- `Collaboration:event`
- `Comment:read`
- `Comment:write`
- `Design:content:read`
- `Design:content:write`
- `Design:meta:read`
- `Design:permission:read`
- `Design:permission:write`
- `Folder:permission:read`
- `Folder:permission:write`
- `Folder:read`
- `Folder:write`
- `Profile:read`

### Canva setup

Complete the following steps to create a Canva integration and generate credentials for Workato:

1. Sign in to Canva and go to the [Connect API integrations](https://www.canva.com/developers/integrations/connect-api) in the Canva Developer Portal.
   
2. Click **Create an integration** to create a new integration.
   
3. Select the **Integration type**.
   
4. Provide a name for your integration in the **Name** field.
   
5. Scroll down to the **Credentials** tab to access your **Client ID** and **Client secret**.
   
6. Copy the **Client ID** and save it securely.
   
7. Click **Generate secret** to reveal your **Client secret**.
   
8. Copy the **Client secret** and save it securely.
   
9. Click the **Scopes** tab and provide any scopes you plan to use. Refer to [Minimum and default scopes](#scopes) for more information.
   

### Connect to Canva Connect using OAuth 2.0

Complete the following steps to connect to Canva Connect in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Canva Connect` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your client ID in the **Client ID** field.
   
6. Enter your client secret in the **Client secret** field.
   
7. Optional. Select the **Scopes** to request for this connection. Refer to [Minimum and default scopes](#scopes) for more information.
   
8. Click **Connect**.
   
9. Sign in to Canva when prompted and click **Allow** to authorize the connection.

---
