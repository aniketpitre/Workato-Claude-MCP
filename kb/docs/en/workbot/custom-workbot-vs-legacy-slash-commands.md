---
url: 'https://docs.workato.com/en/workbot/custom-workbot-vs-legacy-slash-commands.md'
description: >-
  Compare Enterprise Workbot slash commands and legacy Slack slash commands to
  choose the right approach for triggering Workato recipes.
---

# Enterprise Workbot vs Legacy slash commands

Workato supports both [slash commands that are part of an Enterprise Workbot](https://api.slack.com/slash-commands) (i.e. a custom Slack app) and legacy slash commands (i.e. [Custom Integrations slash commands](https://slack.com/apps/A0F82E8CA-slash-commands)).

We strongly recommend using Enterprise Workbots to configure your slash command, as custom integrations is a legacy feature that will eventually be deprecated (no news as to when just yet). Legacy slash commands also does not support some functionalities that Enterprise Workbots have.

Enterprise Workbot slash commands requires [creating a new Slack app](/en/workbot/workbot-custom-bots), and connecting it to Workato via a custom OAuth profile, while legacy slash commands does not. You can add legacy slash commands to a Slack workspace directly from the Slack app directory.

Here is a detailed comparison table between the Enterprise Workbot slash commands and the legacy slash commands.

| Features | Enterprise Workbot slash commands | Legacy slash commands |
| --- | --- | --- |
| Can invoke dialogs? | Yes | No |
| Dialog for missing command input fields | Yes | No |
| Requires a custom Slack app | Yes | No |
| Supports ephemeral messages in Post command reply | Yes | No |
| Connection method | [Workbot with Custom OAuth profile](/en/workbot/configuring-slash-commands.html#workbot-connection) | [Slash command verification token](/en/workbot/legacy-slash-commands.html#configuring-the-workbot-connection) |
| Customize app icon | Yes, from Slack app page | Yes, from the [slash command page](https://slack.com/apps/A0F82E8CA-slash-commands) |
| Pass command input field values to subsequent messages/recipes | Yes | Yes |
| Posting in channels | Yes, but only in channels it is invited to. | Yes, can post in any channel within the Slack workspace it is installed to. |
| Multiple slash commands | Yes, each Workbot recipe can have its own unique slash command. | Yes, each Workbot connection can store the slash command verification tokens of multiple slash commands. |

## Notes for Enterprise Workbot slash commands

1. Make sure that Workbot is in the channel to run commands. Do this by inviting it to the channel.
2. When you invite Workbot into the channel, **anyone** in that channel can interact with Workbot via commands.

---

---
url: >-
  https://docs.workato.com/en/workbot/guides/setup-workbot-for-slack-enterprise-grid.md
description: >-
  Set up an Enterprise Workbot to work with Slack Enterprise Grid, including
  requirements, OAuth profiles, and org-readiness configuration.
---

# Set up Enterprise Workbot with Slack Enterprise Grid

This guide demonstrates how to configure a [Slack Enterprise Workbot](/en/workbot/workbot-custom-bots) to work with Slack Enterprise Grid.

> **WORKBOT COMPATIBILITY**
> 
> Enterprise Workbot is compatible with Slack Connect and can be used in shared channels.

## Setup requirements

You must use Enterprise Workbot to integrate with Slack Enterprise Grid. Standard Workbot isn't compatible. Ensure you have the following to configure Enterprise Workbot:

- **A [Slack Enterprise Grid](https://slack.com/enterprise) plan**
- **An Enterprise Workbot in Workato**. Refer to the [Create an Enterprise Workbot guide](/en/workbot/workbot-custom-bots) to create the bot before proceeding.
- **Access to [Custom OAuth profiles](/en/custom-oauth-profiles) in Workato.**
- Org-readiness enabled on your Slack app profile. Without this setting, the bot can’t integrate with Slack Enterprise Grid.

If you don’t see the **Workbot** or **Custom OAuth profiles** options in the **Platform** or **Tools** menu, ensure your Workato workspace has access to these features.

## Configuration overview

Complete the following steps to set up Enterprise Workbot with Slack Enterprise Grid:

- [Step 1: Obtain your Slack app’s application token](#step-1)
- [Step 2: Update the Workbot’s Custom OAuth profile in Workato](#step-2)
- [Step 3: Reconnect your Enterprise Workbot to Slack](#step-3)
- [Step 4: Approve the Workbot installation in Slack](#step-4)
- [Step 5: Add Enterprise Workbot to workspaces within your Slack Enterprise Grid](#step-5)

## Obtain your Slack app's application token

Complete the following steps to generate an app-level token from Slack. This token authorizes your Enterprise Workbot to interact with your Slack organization.

1. Go to [your Slack apps page](https://api.slack.com/apps/).
   
2. Click the app associated with the Workbot.
   
3. Go to **Basic Information > App-Level Tokens** and click **Generate Token and Scopes**.
   
4. Enter a name for the token in the **Token Name** field.
   
5. Click **Add Scope** and select `authorizations:read` from the drop-down menu.
   
6. Click **Generate**.
   
7. Copy the token and store it in a secure location.
   

## Update the Workbot's Custom OAuth profile

Complete the following steps to update your Workbot’s Custom OAuth profile in Workato with the Slack app token you generated. This ensures that your Workbot can authenticate correctly with Slack Enterprise Grid.

1. Go to **Tools > Custom OAuth profiles**.
   
2. Click the profile associated with the Enterprise Workbot.
   
3. Expand the **Step 1** section on your bot's Custom OAuth profile page.
   
4. Paste the token you generated in [Step 1](#step-1) in the **Application Token** field.
   
5. Click **Save**.
   
6. Click **Done**.
   

## Reconnect your Enterprise Workbot

Complete the following steps to reconnect your Enterprise Workbot to Slack. Updating the OAuth profile requires reauthorization to ensure the bot functions correctly in your organization.

1. Go to **Platform > Workbot**.
   
2. Click the Workbot connection.
   
3. Click **Edit connection** on the Workbot's overview page.
   
4. Click **Disconnect**.
   
5. Click **Reconnect**.
   
6. Confirm the app installs into the organization and not an individual workspace in the authorization window.
   
7. Complete the following steps to change the installation location:
   
   1. Click the drop-down menu in the app authorization window.
      
   2. Select the organization where you plan to install the Enterprise Workbot.
      
      ![Choosing an org for installation](/assets/install-into-org-1.2nzm0p5e.png)
      
8. Click **Allow**.
   

## Approve the bot installation in Slack

Complete the following steps to approve the Enterprise Workbot installation in Slack from the [Enterprise Grid admin dashboard](https://slack.com/help/articles/115005594006-Guide-to-the-Enterprise-Grid-admin-dashboard). This approval allows the bot to operate across your Slack organization.

> **NOTE**
> 
> You need **Org Admin** or **Org Owner** permissions in Slack for this step.

1. Open the Slack desktop app and select your workspace name from the menu.
   
2. Select **Settings & administration > Organization settings**. The admin dashboard opens in a new browser tab.
   
   ![Enterprise grid admin dashboard](/assets/grid-admin-dashboard.CBIMGhXV.png)
   
3. Click **Organizations > Apps** in the dashboard menu.
   
4. Find your Enterprise Workbot app in the **Installed Apps** tab.
   
5. Open the **three dots menu** next to the Enterprise Workbot app.
   
6. Click **Approve this app**.
   

## Add your Enterprise Workbot to workspaces

Complete the following steps to add the Enterprise Workbot to specific Slack workspaces within your Enterprise Grid. This makes the bot available for users in those workspaces.

1. Go to the **Apps** page in your Enterprise Grid admin dashboard.
   
2. Locate your Enterprise Workbot app in the **Installed Apps** tab.
   
3. Click the **three dots menu** next to the Enterprise Workbot app and select **Add to more workspaces**.
   
4. Select the workspaces where you plan to add the Enterprise Bot and then click **Next**.
   
5. Review the requested permissions for the Enterprise Workbot and click **Next**.
   
6. Click the **I'm ready to add this app** checkbox.
   
7. Click **Add App**.
   

## What's next?

Your Enterprise Workbot is now ready to use in Slack Enterprise Grid, which enables you to perform the following tasks:

- Create slash commands allowing users [to interact with the bot directly from Slack](/en/workbot/workbot-commands)
- Define command replies for how the bot [responds to user inputs](/en/workbot/workbot-command-reply)
- Perform actions such as [posting notifications, downloading attachments, and more](/en/workbot/workbot-actions)

---
