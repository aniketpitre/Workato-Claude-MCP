---
url: 'https://docs.workato.com/en/connectors/slack/custom-oauth.md'
description: >-
  Use custom OAuth profiles to run your own Slack apps through the Workato Slack
  connector, customizing branding, bot identity, and permission scopes.
---

# Custom OAuth profiles for Slack

## What are custom OAuth profiles?

Use custom OAuth profiles so your Slack apps can leverage the Workato Slack connector in the background. You can fully customize your Slack app's identity, including:

- Branding (bot name, bot logos, background color)
- Permissions

## When would I need custom OAuth profiles for Slack

- You want multiple apps, and each app performs workspace orchestration as part of its automations. For example, an EscalationBot can create a private conversation, invite crisis management team members, and archive the conversation after the issue's resolved. BirthdayBot can perform the same actions, but for a very different purpose: create a private conversation, invite party planners, and archive the conversation after the birthday's over.
  
- You want control over your app's branding and appearance.
  
- You want control over your bot's permissions. The following minimum permissions are for optimal use.
  

| Token type | Scope | Reason |
| --- | --- | --- |
| Bot | None | No bot scopes required. |
| User | channels:read | Retrieves list of public conversations. |
| User | channels:write | Create or update public conversations. |
| User | groups:read | Retrieves list of private conversations. |
| User | groups:write | Create or update private conversations. |
| User | im:read | Retrieves list of direct message conversations. |
| User | im:write | Create or update direct message conversations. |
| User | mpim:write | Create or update multi-party group conversations. |
| User | mpim:read | Retrieves list of multi-party group conversations. |
| User | chat:write | Post messages as user. |
| User | users:read | Get user info. |
| User | users:read.email | Get user info by email. |

### Creating a custom OAuth profile

Complete the following steps to create a custom OAuth profile in Workato:

1. Click **Tools > Custom OAuth profiles**.
   
2. Click **\+ New custom profile**.
   
3. Use the **Application** drop-down menu to select **Slack**.
   
4. Provide a unique name for the app in the **Name** field.
   
5. Click **Create new app**. This opens the [Slack API](https://api.slack.com/apps) page in a new window. Keep Workato and Slack open because you'll need both to complete the next steps.
   
6. In Slack, sign in to your workspace (if you're prompted) and select **Create New App**.
   
7. Choose how to configure your app's scopes and setting. There are two ways to configure them:
   
   **From a manifest**
   
   a. Use the **Pick a workspace to develop your app in:** drop-down menu to select a workspace.
   
   b. Verify or edit the manifest configuration and click **Next**.
   
   c. Review the summary and click **Create**.
   
   **From scratch**
   
   a. Enter a name in the **App Name** field.
   
   b. Use the **Pick a workspace to develop your app in:** drop-down menu to select a workspace.
   
   c. Click **Create App**.
   
8. The **Basic Information** page opens in Slack. Copy the following information to add to Workato in the **App Credentials** section:
   
   - **Client ID**
   - **Client Secret**
   - **Signing Secret**
9. Add the following information in Workato:
   
   - **Client ID**
   - **Client secret**
   - **Signing Secret**
10. Click **Save**.
    
11. Optional. Follow the on-screen instructions in Workato to manually configure redirect URLs, interactivity settings, and user token scopes for your Slack app. You must define at least one permission scope before you can install the app in your workspace. Your Slack app must have permission scopes to use Event subscriptions. Slack automatically adds required permission scopes when you subscribe to events.
    

### Enabling event subscriptions

For a New event trigger to pick up events, Workato generates a Request URL, so your app knows where to send these events to. This Request URL is generated after you've entered an **Event name** in the trigger. After your app sends events to your recipe's request URL, the recipe takes over and executes your recipe actions. Refer to [New event trigger (real-time)](/en/connectors/slack/triggers#new-event-trigger-real-time) for more information.

To enable Event Subscriptions in Slack, complete the following steps:

1. Click **Event Subscriptions** from the navigation bar.
   
2. Click the **Enable Events** toggle to **On**.
   
3. Paste the URL from your New event trigger in the **Request URL** field.
   
4. Click **Save**.
   

### Subscribing to workspace events

Slack provides an entire list of workspace events that you can subscribe to. Subscribing to events automatically add scopes that your app doesn't already have. This might give your app unintended permissions. To confirm your app permission scopes, go to **OAuth & Permissions > Scopes**.

### Installing your app

A permission scope is automatically added after you subscribe to at least one workspace event. This allows you to install the Slack app to your workspace.

Complete the following steps to install the Slack app:

1. Click **Install App > Install to Workspace** from the navigation bar.
   
2. Review app permissions and click **Allow**.
   

To finish configuration in your Workato custom OAuth profile, click **Done** . You can now use this custom OAuth profile in other Slack connections in Workato.

### Using your custom OAuth profile

After you create a custom OAuth profile, anyone in your Workato workspace can use it in their own Slack connections without creating and configuring a new Slack app.

> **CUSTOM OAUTH PROFILE LIMITATION**
> 
> Custom OAuth profiles can only connect to a single Slack workspace.

Refer to [Token request endpoint](/en/api-mgmt/oauth2#token-request-endpoint) for more information about data center specific custom OAuth profiles.

---
