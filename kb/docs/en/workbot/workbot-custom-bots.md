---
url: 'https://docs.workato.com/en/workbot/workbot-custom-bots.md'
description: >-
  Create a Slack Enterprise Workbot with custom branding, OAuth, and permissions
  to run multiple purpose-specific bots in one workspace.
---

# Create a Slack Enterprise Workbot

Enterprise [Workbots](https://www.workato.com/platform/workbot?utm_source=docs&utm_medium=referral&utm_campaign=workbot) are custom Slack apps you create that can leverage the Workato bot platform under the hood. Each Enterprise Workbot has its own unique custom OAuth profile, allowing full customization of your bot's identity. This includes:

- Branding (bot name, bot logo, background color)
- Permissions

Enterprise bots also unlock access to additional features like slash commands, shortcuts, and App Home.

If you want multiple, purpose-specific bots in your Slack workspace, Enterprise bots are just what you need. Using Enterprise bots, you can create **HRBot**, **ITBot**, and **DevOps** bots and install them in your workspace.

Enterprise Workbots make use of Slack's [V2 OAuth 2.0 flow](https://api.slack.com/authentication/oauth-v2).

> **FEATURE AVAILABILITY**
> 
> The Enterprise Workbot feature is available to customers on specific pricing plans. Refer to your pricing plan and contract to learn more.

## Prerequisites

To create an Enterprise Workbot, you need:

- Access to [Workbot](/en/workbot/workbot) in Workato.
- Access to [Custom OAuth profiles](/en/custom-oauth-profiles) in Workato.

If you don't see these options in the **Tools** menu, make sure your workspace has access to this feature.

## Choose Workbot for Slack

1. [Sign in to your Slack workspace](https://slack.com/signin#/signin) from your browser.
   
2. Open a new tab and sign in to Workato.
   
3. Go to **Platform > Workbot**. If the [Workbot](/en/workbot/workbot) option isn't available, ensure your workspace has access to this feature.
   
4. Click the **Custom bots** tab. If the **Custom bots** tab isn't available, ensure your workspace has access to [Custom OAuth profiles](/en/custom-oauth-profiles).
   
5. Click **Create a custom bot**. The **New bot** page appears.
   
6. Select **Workbot for Slack** in the **Application** field if it isn't already selected.
   
7. Enter a name for the bot in the **Name** field.
   
8. Click **Create new app**. This opens the [Your Apps](https://api.slack.com/apps) page on the Slack API website. Keep both the Workato and Slack tabs open to complete the remaining steps.
   

## Create a new Slack app

1. Open the new Slack tab, select the workplace where you plan to develop the bot, and then click **Next**.
   
2. Review the app summary and click **Create** to create your app.
   
3. Click **Got It** in the **Welcome to your app's configurations** dialog.
   
4. Go to **Settings** in your app and select **Basic Information**. Locate **App Credentials** and copy the following values:
   
   - Client ID
   - Client secret
   - Signing secret
   
   ![Slack App Credentials](/assets/workbot-slack-app-cred.BJOOYxYO.png)_Example Slack App Credentials_
   

## Configure Workato to talk to your Slack app

1. Go back to the Workato tab.
   
2. Paste the **Client ID** value from Slack into the **Client ID** field.
   
3. Paste the **Client secret** value from Slack into the **Client secret** field.
   
4. Paste the **Signing Secret** value from Slack into the **Signing Secret** field.
   
5. Optional. Paste the **App-Level Token** from Slack into the **Application token** field. Use this token only if you plan to enable [Org Apps/Enterprise Grid](/en/workbot/guides/setup-workbot-for-slack-enterprise-grid#setting-up-enterprise-workbot-with-slack-enterprise-grid) capabilities.
   
   ![Custom OAuth profile for Slack](/assets/workbot-oauth-profile-signing-secret.GvXOCgtq.png)_Configure your Custom OAuth profile_
   
6. Click **Save** when you're finished.
   

## Complete the connection in Workato

Complete the following steps to create a new Workbot for Slack connection in Workato:

1. Go to the open Workato tab and click **Done**. A new Workbot for Slack connection page opens with the **Custom OAuth profile** field pre-filled with your custom bot's name.
   
2. Enter a name for the connection in the **Connection name** field.
   
3. Use the **Location** drop-down menu to select the project or folder where you plan to store this connection.
   
4. Click **Connect**. A dialog appears, prompting you to review the requested permissions for your custom bot to access your Slack workspace.
   
5. Click **Allow** to authorize the app you created.
   

## What's next?

Your Enterprise Workbot is now ready for use in Workato recipes. Refer to the following guides to learn how to configure its functionality:

- **Configure the bot to work with Slack Enterprise Grid**, allowing you to [centrally manage the bot for your entire organization](/en/workbot/guides/setup-workbot-for-slack-enterprise-grid)
- **Create slash commands**, allowing users [to command the bot from Slack](/en/workbot/workbot-commands)
- **Create command replies**, defining how the bot [responds to user commands](/en/workbot/workbot-command-reply)
- **Perform a variety of actions** such as [posting notifications, downloading attachments, and more](/en/workbot/workbot-actions)

> **CONFIGURE THE ENTERPRISE WORKBOT FOR EMBEDDED CUSTOMERS**
> 
> Embedded partners must complete additional steps to enable Enterprise Workbots for end customers. Refer to [Configure a Slack Enterprise Workbot for Embedded users](/en/workbot/workbot-embed-config) for more information.

## Updating your existing Slack Workbot to use Signing Secrets

Workbots created with the legacy Verification tokens still function as normal, however, we recommend that you use Slack's newer Signing Secrets tokens.

You can do this by visiting your [Apps Credentials page](https://api.slack.com/apps) on Slack and copying the Apps new Signing Secret value over to your Workbot OAuth profile details on Workato.

Signing Secrets is located under **Platform > Workbot > [Custom bots](https://app.workato.com/workbots#custom)**. Select the Workbot for Slack you plan to add Signing Secrets to and update the value in the field provided.

---
