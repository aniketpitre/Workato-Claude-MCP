---
url: 'https://docs.workato.com/en/connectors/discord.md'
description: >-
  Connect Discord to Workato to automate workflows with your communications
  platform.
---

# Discord

Discord is a real-time communications platform that lets users interact using text, voice calls, video calls, and screen sharing. The Discord connector allows you to automate workflows to create messages and assign roles.

## Install Discord from the community library

Complete the following steps to install the Discord connector from the [community library](https://www.workato.com/browse/connectors):

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

The Discord connector uses OAuth2 authentication.

### Minimum and default scopes

These are the minimum required scopes to establish a connection. If you don't select these scopes, they're automatically added to your requested scopes.

- `Bot`
- `Identify`

### Discord setup for OAuth2 authentication

Complete the following steps to retrieve credentials from Discord:

1. Go to the Discord [Applications](https://discord.com/developers/applications) page.
   
2. Click your application. To create a new application, refer to the Discord [Step 1: Creating an app](https://docs.discord.com/developers/quick-start/getting-started#step-1-creating-an-app) guide.
   
3. Click the **OAuth2** page under the **Overview** tab.
   
4. Copy and save the **Client ID** and **Client Secret** for use in Workato.
   
   > **SAVE YOUR SECRET**
   > 
   > The client secret only displays once. If you lose it, you must reset it.
   
5. Click **Add Redirect** under the **Redirect** section.
   
6. Add the following URI:
   
   ```html
   https://www.workato.com/oauth/callback
   ```
   
7. Click **Save Changes**.
   
8. Click the **Bot** page.
   
9. Click **Reset Token** to generate a new token.
   
10. Copy and save the **Token** for use in Workato.
    
    > **SAVE YOUR TOKEN**
    > 
    > The token only displays once. If you lose it, you must reset it.
    

### Connect to Discord with OAuth2 authentication

Complete the following steps to connect to Discord in Workato:

1. Click **Create > Connection**.
   
2. Search for `Discord` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Discord connection setup](/assets/discord-connection-setup.DaFj6OAG.png)_Discord connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Client ID**. Refer to [Discord setup for OAuth2 authentication](#discord-setup) for instructions on how to retrieve the **Client ID**, **Client secret**, and **Bot token**.
   
6. Enter the **Client secret**.
   
7. Enter the **Bot token**.
   
8. Optional. Use the **Requested permissions (Oauth scopes)** drop-down menu to select the scopes you plan to add to this connection. Refer to [Minimum and default scopes](#scopes) for more information.
   
9. Optional. Use the **Bot permissions** drop-down menu to select the bot permissions you plan to include for this connection. This setting defaults to **Administrator** if left blank.
   
10. Click **Connect**.
    
11. Authorize access to the account.

---
