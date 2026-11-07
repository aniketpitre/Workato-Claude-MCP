---
url: 'https://docs.workato.com/en/workbot/workbot-for-slack-setup.md'
description: >-
  Set up a Workbot for Slack connection, configure OAuth, connect an NLU
  provider, and invite Workbot to your Slack channels.
---

# Set up Workbot for Slack

Watch our 2 minute video guide instead

[Video](https://www.youtube.com/embed/JVW3-dwA_Vc)

This guide demonstrates how to set up a standard Workbot for Slack connection.

> **STANDARD WORKBOT CONNECTION LIMIT**
> 
> Only one standard Workbot connection per Slack workspace is supported. Use [Enterprise Workbot](/en/workbot/workbot-custom-bots) instead if you need multiple Workbots in the same workspace. Enterprise Workbot requires a custom OAuth profile.

Complete the following steps to set up Workbot for Slack:

- [Step 1: Connect to the NLU provider](#_1-connect-to-the-nlu-provider) if you plan to use an NLU provider for the Workbot conversational interface. Otherwise, skip this step.
- [Step 2: Configure a custom OAuth profile](#_2-configure-a-custom-oauth-profile) if you plan to set up an Enterprise Workbot. Otherwise, skip this step.
- [Step 3: Create a Workbot for Slack connection](#_3-create-a-workbot-for-slack-connection)
- [Step 4: Invite Workbot to channels](#_4-invite-workbot-to-channels)

## Prerequisites

You must complete the following prerequisites before you set up Workbot for Slack:

- Confirm or obtain privileges to connect Workbot to Slack. Some organizations allow all members of a Slack workspace to install third-party apps, while other organizations restrict this privilege to admins only.
- Confirm that your organization uses an [integration user](/en/connections#creating-a-dedicated-user-for-workato) account to configure the connection. This prevents disruptions if a human user’s account permissions change.

> **ENTERPRISE GRID REQUIREMENT**
> 
> If your organization uses Slack Enterprise Grid, you must set up Enterprise Workbot. The standard Workbot isn't compatible with Enterprise Grid environments. Refer to the [Set up Enterprise Workbot with Slack Enterprise Grid](/en/workbot/guides/setup-workbot-for-slack-enterprise-grid#setup-requirements) guide for more information.

## Permissions

| Token type | Scope | Reason |
| --- | --- | --- |
| User | `users:read` | View information about the user's identity. |
| `users:read.email` | Get user info by email. |
| Bot | `app_mentions:read` | Listen for bot mentions in conversations which the bot is involved in. |
| `channels:read` | Retrieves list of public conversations. |
| `chat:write` | Create/update public conversations. |
| `files:read` | Retrieves list of private conversations. |
| `files:write` | Create/update private conversations. |
| `groups:read` | Retrieves list of direct message conversations. |
| `im:history` | Create/update direct message conversations. |
| `im:write` | Create/update multi-party group conversations. |
| `mpim:read` | Retrieves list of multi-party group conversations. |
| `users:read` | Get user info. |
| `users:read.email` | Get user info by email. |

## 1\. Connect to the NLU provider

Workbot for Slack supports Google DialogFlow and Amazon Lex. If you would like to use one of these NLU providers, you must connect the NLU provider to Workato before you connect with Workbot for Slack.

To connect to your NLU provider, go to **App Connections** and select **Create a new connection**. Search for your NLU provider.

## 2\. Configure a custom OAuth profile

You can customize the Workbot for Slack identity, including the branding (bot name, bot logo, and background color) and permissions with a custom OAuth profile. Go to **Tools > Custom OAuth profiles > Create custom profile** to configure a new custom OAuth profile.

1. In the **Application** field, select **Workbot for Slack**. Click **Create new app**.
   
   This will open [your Slack apps](https://api.slack.com/apps) in a new tab.
   
2. Select **Create new app** from the Slack window.
   
3. Select **From scratch**. This allows you to define the scope and permission according to your use case.
   
4. Enter a descriptive name for your app and choose which Slack workspace this app belongs to. Click **Create App**.
   
5. You will be redirected to your newly created Slack app's **Basic Information** page.
   
6. Scroll to the **App credentials** section and save the following information.
   
   - Client ID
   - Client secret
   - Verification token
   
7. Return to Workato setup. Provide the app credentials information from your Slack app. Click **Save** when done.
   
   > **Application token field**
   > 
   > Leave this field empty. The Application Token is a configuration for Org-level Apps.
   
8. Return to your Slack settings. Select **OAuth & Permission** on the left-side navigation.
   
9. Select `Add a new Redirect URL`. Copy the callback URL into your Slack settings. Click **Save URLs**. `https://www.workato.com/oauth/callback`
   
   > **This doesn’t seem like a proper link**
   > 
   > If you get an error saying 'This doesn’t seem like a proper link' please check to make sure there are no extra spaces at the start/end of the link.
   
10. Still on **OAuth & Permissions**. Navigate to **Scopes**, select the following **Bot Token Scopes**:
    
    - app\_mentions:read
    - chat:write
    - channels:read
    - commands
    - files:read
    - files:write
    - groups:read
    - im:history
    - im:write
    - mpim:read
    - users:read
    - users:read.email
    
11. Still on **OAuth & Permissions**. Navigate to **Scopes**, select the following **User Token Scopes**:
    
    - users:read
    - users:read.email
    
12. Select **App home** from the left-side navigation.
    
    - Provide the Display name and Default username.
    - Select `ON` to _Always Show My Bot as Online_
    
13. Still on **App home**. Navigate to **Show Tabs**.
    
    - Enable the **Messages Tab** toggle and select **Allow users to send Slash commands and messages from the messages tab**. This lets users send messages directly to the bot.
    - Optional. Enable the **Home Tab** toggle if you plan to let users interact with your bot through an app home view. [Learn more](/en/workbot/workbot-actions#publish-app-home-view).
14. Select **Event Subscriptions** from the left-side navigation.
    
    - Select `ON`
    - Provide the **Request URL** provided in your Workato configuration. A sample URl is provided below `https://app.workato.com/slack_webhooks/event?coak_id=9690`
    
15. Still on **Event Subscriptions**. Navigate to the **Subscribe to Bot Events** subsection. Add the following **Bot User Events**:
    
    - app\_mention
    - file\_shared
    - message.im
    - app\_home\_opened
    
    Select **Save Changes** at the bottom on the page.
    
16. Select **Interactivity & Shortcuts** from the left-side navigation.
    
    - Select `ON`
    - Provide the **Request URL** and **Options Load URL** provided in your Workato configuration. A sample URl is provided below `https://app.workato.com/slack_webhooks/event?coak_id=9690`
    
    Select **Save Changes** at the bottom on the page.
    
17. Lastly, it is time to install your Slack app into your workspace!
    
    Select **Install App** from the left-side navigation.
    
    - Select **Install to Workspace**.
    - Click **Allow** when prompted.
    

## 3\. Create a Workbot for Slack connection

Connecting a Workbot for Slack connection will add Workbot to your Slack team. To create a new Workbot for Slack connection, go to **App Connections** and click **Create a new connection**. Search for **Workbot for Slack** to begin.

| Workbot for Slack connection fields |
| --- |
| Application | Workbot for Slack |
| Connection name | Choose an appropriate name for this connection |
| NLU provider | You can optionally select the DialogFlow or Amazon Lex NLU. You must connect to the NLU provider for it to appear in the drop-down list. |
| Advanced | Slash commands verification tokens | Used for invoking legacy Custom Integration slash commands. Each slash command has a token. Separate tokens with commas to support multiple slash commands. [Learn more.](https://docs.workato.com/workbot/legacy-slash-commands.html#configuring-the-workbot-connection) |
| Custom help | Provide simple text help OR rich help using a JSON document corresponding to Slack message. You can build a rich help message using the [Slack message builder](https://api.slack.com/docs/messages/builder). |
| Is this a Classic Slack app? | Select **Yes** if you have not migrated your app yet. |
| Custom OAuth profile | Custom OAuth profiles allow your Slack apps to leverage the Workato Slack connector under the hood. When selected, all requests to the app will use the profile specified. [Learn more](https://docs.workato.com/workbot/workbot-custom-bots.html). |

After you install Workbot into your Slack team, Workbot detects the latest app connections in your Workato account and automatically connects to them.

You can interact with Workbot via direct messages after adding Workbot to your Slack organization. Direct messages with Workbot are not visible to anyone but you.

To enable other users to interact with Workbot or to allow Workbot to post notifications, you must invite it to specific channels. Proceed to the next section.

"Slack team already has Workbot installed" error

The **Slack team already has Workbot installed** error means another standard Workbot for Slack connection is already active in your workspace. Only one standard Workbot for Slack connection per workspace is supported.

![Duplicate Workbot connection error](/assets/duplicate-workbot-connection-error.BKUXF_aL.png)_Duplicate Workbot connection error_

Perform one of the following actions to resolve this:

- Contact the user listed in the error and ask them to remove the existing Workbot connection from the workspace.
- Connect to a different Slack workspace.
- Use [Enterprise Workbot](/en/workbot/workbot-custom-bots) to run multiple Workbots in the same Slack workspace.

## 4\. Invite Workbot to channels

To invite Workbot to a channel, do one of the following:

- Mention Workbot via `@workbot` ![Invite Workbot to channels via mention](/assets/invite-workbot-to-channels-via-mention.DlvzoTme.png)
- Use the **Invite new members to join** menu option in the channel details ![Invite Workbot to channels via the menu option](/assets/invite-workbot-via-menu-option.BXTr6Kwa.gif)

After you add Workbot to a channel, use `@workbot` to begin an interaction.

> **WORKBOT VISIBILITY**
> 
> Conversations with Workbot in a channel are visible to all team members in that channel.

  

> **NOT REQUIRED FOR ENTERPRISE WORKBOT USERS**
> 
> You don't need to invite Workbot to your channels if you're using Enterprise Workbot.

  

> **DIRECT MESSAGING**
> 
> When you send a direct message to Workbot, you don't need to use `@workbot`.

## Next

Now that you have set up Workbot in Slack, proceed to [build your first Workbot](/en/workbot/workbot-commands).

---
