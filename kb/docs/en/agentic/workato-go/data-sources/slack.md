---
url: 'https://docs.workato.com/en/agentic/workato-go/data-sources/slack.md'
description: >-
  Add Slack as a Workato GO data source with a custom OAuth profile to enable
  real-time federated search across workspace messages.
---

# Add a Slack data source to Workato GO

Slack federated search enables users to search Slack workspace messages in real time alongside other data sources in a unified search experience. Unlike indexed data sources, Slack search queries the Slack API with end-user OAuth credentials when a user performs a search, which prevents data leakage. Slack only permits federated search.

This data source configuration and search experience integrates Workato connector actions and runtime connections.

## Prerequisites

You must have the following to use the Slack data source connector:

- An existing parent connection in Workato to add Slack as a data source in Workato GO.
- A custom OAuth profile for Slack. Refer to [Custom OAuth profiles for Slack](/en/connectors/slack/custom-oauth) for more information.

## Create a custom OAuth profile

Complete the following steps to create a custom OAuth profile for Slack:

1. Sign in to your Workato account.
   
2. Go to **Tools > Custom OAuth profiles**.
   
3. Click **\+ New custom profile**.
   
   ![Create a new custom profile](/assets/new-custom-profile.Dp3wyeki.png)_Create a new custom profile_
   
4. Use the **Application** drop-down menu to select `Slack`.
   
5. Provide a name for your custom profile in the **Name** field.
   
6. Click **Create an app**. This opens the Slack API page in a new window. Keep Workato and Slack open, as you need both to complete the following steps.
   
7. Sign in to your Slack workspace if prompted, then select **Create an App**.
   
8. Choose how to configure your app's scopes and settings:
   
   **From a manifest**
   
   1. Use the **Pick a workspace to develop your app in** drop-down menu to select a workspace.
      
      ![Pick a workspace to develop your app in](/assets/pick-workspace-develop.DtYpCcXc.png)_Pick a workspace to develop your app in_
      
   2. Verify or edit the manifest configuration and click **Next**.
      
   3. Review the summary and click **Create**.
      
   
   **From scratch**
   
   1. Enter a name in the **App Name** field.
      
   2. Use the **Pick a workspace to develop your app in** drop-down menu to select a workspace.
      
      ![Name app and choose workspace](/assets/name-choose-workspace.CXu2un93.png)_Name app and choose workspace_
      
   3. Click **Create App**.
      
   
9. Go to the **App Credentials** section of the Slack **Basic Information** page, copy the following credentials and enter the values in the corresponding fields in Workato:
   
   - **Client ID**
   - **Client secret**
   - **Signing Secret**
10. Click **Save**.
    

## Configure your Slack app

You must configure redirect URLs, interactivity, and user token scopes in the Slack API platform after you create your custom OAuth profile.

### Configure redirect URLs

1. Go to **OAuth & Permissions > Redirect URLs** in the Slack API platform.
   
2. Add the following redirect URL:
   
   ```text
   https://www.workato.com/oauth/callback
   ```
   
3. Click **Save URLs**.
   

### Configure interactivity and shortcuts

Complete the following steps to configure interactivity and shortcuts:

1. Go to **Interactivity & Shortcuts > Interactivity** and turn it on in the Slack API platform.
   
2. Paste the following URL into the **Request URL** field:
   
   ```text
   https://www.workato.com/slack_webhooks/actions?sa_scope=adapter&coak_id=38630
   ```
   
3. Click **Save Changes**.
   

### Configure user token scopes

Complete the following steps to configure your user token scopes:

1. Go to **OAuth & Permissions > Scopes > User Token Scopes** in the Slack API platform.
   
2. Add the following scopes:
   
   | Scope | Access |
   | --- | --- |
   | `channels:read` | View basic channel information |
   | `channels:write` | Manage channels |
   | `chat:write` | Send messages |
   | `groups:read` | View private channel information |
   | `groups:write` | Manage private channels |
   | `im:read` | View direct message information |
   | `im:write` | Manage direct messages |
   | `mpim:read` | View group DM information |
   | `mpim:write` | Manage group DMs |
   | `search:read` | Search workspace messages and files |
   | `users:read` | View user information |
   | `users:read.email` | View user email addresses |
   
3. Return to the Workato platform and click **Done**.
   

## Create a Slack connection

Create a Slack connection in Workato before you add Slack as a data source in Workato GO. End users establish their own runtime connections after the data source is configured.

Complete the following steps to create a Slack connection:

1. Go to **Connections > Create > Connection** in the Workato platform.
   
2. Search for `Slack` and select it as your app.
   
3. Enter a descriptive name in the **Connection name** field.
   
   ![Connect to Slack](/assets/connect-slack.CQuPj2ya.png)_Connect to Slack_
   
4. Use the **Location** drop-down menu to select the appropriate project folder.
   
5. Optional. Expand **Advanced** to configure additional settings.
   
6. Use the **Custom OAuth profile** drop-down menu to select the OAuth profile you created in the preceding steps.
   
7. Click **Connect** and authorize the app in Slack when prompted.
   

## Add Slack as a data source

Complete the following steps to add Slack as a data source in Workato GO:

1. Sign in to your Workato GO account.
   
2. Expand the **Admin** menu in the sidebar and click **Data sources**.
   
3. Click **Add Data Source**. The **Add Data Source** page displays.
   
   ![Add data source](/assets/add-slack.Cb-LVfH3.png)_Add data source_
   
4. Select the Slack app.
   
5. Enter a descriptive name in the **Name** field.
   
6. Use the **Select a Slack connection** drop-down menu to select the connection you created in the preceding steps.
   
7. Click **Use connection > Next**. Slack now appears on the **Data Sources** page.
   
   ![Use Slack connection](/assets/use-slack-connection.DWg1Vvaw.png)_Use Slack connection_
   
8. Click your email in the bottom-left corner to open the selection menu.
   
9. Click **Connections** in the menu.
   
10. Go to **Discover new connections** and click **Connect** next to your Slack connection.
    
    ![Discover new connections](/assets/discover-new-connections.CoAhaQlY.png)_Discover new connections_
    
11. Click **Create Connection** in the **Create Runtime Connection** modal.
    
    ![Create runtime connection](/assets/create-runtime-connection.CtUQtaH6.png)_Create runtime connection_
    
12. Complete the authorization for the app in Slack when prompted. You can now use Slack as a data source in Workato GO.

---
