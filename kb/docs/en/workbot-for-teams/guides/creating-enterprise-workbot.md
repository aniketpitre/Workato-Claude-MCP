---
url: >-
  https://docs.workato.com/en/workbot-for-teams/guides/creating-enterprise-workbot.md
description: >-
  Create a Microsoft Teams Enterprise Workbot with custom branding, OAuth
  profile, and permissions using the Microsoft Teams Developer Portal.
---

# Create a Microsoft Teams Enterprise Workbot

Enterprise [Workbots](https://www.workato.com/platform/workbot?utm_source=docs&utm_medium=referral&utm_campaign=workbot) are Microsoft Teams apps you create that can leverage the Workato bot platform under the hood. You can fully customize your bot's identity, such as:

- Branding (bot name, bot logos, accent color)
- Custom OAuth profile (bot ID, App secret)
- Permissions

These Microsoft Teams apps can be sideloaded into your Microsoft Teams groups or channels for use by your members. If you want control over your bot's branding and permissions or multiple purpose-specific bots, Enterprise Workbots are for you.

> **FEATURE AVAILABILITY**
> 
> The Enterprise Workbot feature is available to customers on specific pricing plans. Refer to your pricing plan and contract to learn more.

> **DEPRECATION NOTICE**
> 
> This page uses the [Microsoft Teams Developer Portal](https://dev.teams.microsoft.com/) to create and manage an app. As of **January 1, 2022**, Microsoft has deprecated App Studio.
> 
> The approach outlined on this page is the new, recommended method, but the [App Studio instructions](/en/workbot-for-teams/guides/creating-enterprise-workbot-app-studio) have been retained for reference.

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This feature requires configuration steps that are specific to your Virtual Private Workato (VPW) instance. If you are a VPW customer, refer to your VPW private documentation for the configuration details for your instances.

## Prerequisites

To set up an Enterprise Bot, you must have the following:

- **In Workato**:
  
  - **Access to:**
    
    - **Workbot**: If you don’t see the **Platform > Workbot** option in your account, contact your Customer Success Manager.
    - [**Custom OAuth profiles**](/en/custom-oauth-profiles): If you don’t see the **Tools > Custom OAuth Profiles** option in your account, contact your Customer Success Manager.
  - **Privileges that allow you to:**
    
    - Create and configure Workbots.
    - Create and configure custom OAuth profiles.
- **In your Microsoft organization**:
  
  - **One of the following roles:**
    
    - Application administrator
    - Cloud application administrator
    - Global administrator
    - Privileged role administrator

> **DELEGATED PERMISSIONS AND APPLICATION PERMISSIONS**
> 
> You can set up an Enterprise Workbot to use either [Delegated or Application permissions](https://learn.microsoft.com/en-us/graph/permissions-overview?tabs=http#permission-types).
> 
> Delegated permissions, set as the default option, use the OAuth user's permissions to establish the connection in Workato. The user configuring the connection must have one of the required roles.
> 
> Application permissions offer enhanced security compared to Delegated permissions. This method keeps the connection independent of the user, preventing disconnection if the user logs out and allowing a non-administrator to set up the connection.
> 
> Refer to the [Set up Application permissions (optional)](#set-up-application-permissions-optional) step for more information.

Check your role assignments in [Microsoft](https://portal.azure.com/) by going to **Users > You (select your name) > Assigned roles**.

## Create the Workbot in Workato

Complete the following steps to create the Workbot in Workato:

1. Sign in to your Workato account.
   
2. Go to **Platform > Workbot**.
   
3. Click the **Custom bots** tab. If you don't see this tab, ensure your workspace has access to [Custom OAuth profiles](/en/custom-oauth-profiles).
   
4. Click **Create a custom bot** to open the **New bot** page.
   
5. Select **Workbot for Microsoft Teams** from the **Application** drop-down menu.
   
6. Enter a unique name for the bot in the **Name** field. The name may include spaces but cannot contain special characters.
   
7. Click **Create new app**. This opens the [Microsoft Teams Developer Portal](https://dev.teams.microsoft.com/home) in a new tab and reveals the **Bot endpoint address** for future configuration.
   
   Keep both the Workato tab and the Microsoft Teams Developer Portal tab open to complete the remaining steps.
   

## Create a Microsoft Teams app

1. [Create the bot in Microsoft Teams Developer Portal](#step-2-1)
2. [Create the app](#step-2-2)
3. [Configure the bot's permissions](#step-2-3)
4. [Configure authentication redirect URLs](#step-2-4)
5. [Add a client secret](#step-2-5)

### Create the bot in the Microsoft Teams Developer Portal

Complete the following steps to create the bot in the Microsoft Teams Developer Portal:

1. Go to **Tools > [Bot Management](https://dev.teams.microsoft.com/bots)**.
   
2. Click **\+ New Bot**.
   
3. Enter a name for the bot in the **Bot name** field. For consistency, use the same name as your Workato bot.
   
4. Click **Add** to add your bot to the Developer Portal.
   
5. Go to the Workato tab and copy the **Bot endpoint address**. It should resemble the following example:
   
   ```plaintext
   https://app.workato.com/skype_webhooks/event?coak_id=42
   ```
   
6. Return to the Developer Portal tab and paste the copied value in the **Bot endpoint address** field.
   
7. Click **Save**.
   
8. Copy the **Bot ID** from the Developer Portal page URL. It should resemble the following example:
   
   ```plaintext
   https://dev.teams.microsoft.com/bots/<YOUR-BOT-ID>/configure
   ```
   
   Store the **Bot ID** securely for later use.
   

### Create the app

Complete the following steps to create the app in the Microsoft Teams Developer Portal:

1. Go to [**Apps**](https://dev.teams.microsoft.com/apps) and click **\+ New app**.
   
2. Enter a name for your app in the **Name** field.
   
3. Click **Add** to create your app.
   
4. Select the app you just created and go to **Configure > Basic information**.
   
5. Fill in the following required fields:
   
   - **Short description**: Enter a high-level description of your app in 80 characters or less.
   - **Long description**: Enter a detailed description of your app in 4,000 characters or less.
   - **Developer or company name**: Enter the name of the developer or company associated with the app.
   - **Website**: Enter a valid HTTPS URL.
   - **Privacy policy**: Provide a link to your privacy policy.
   - **Terms of use**: Provide a link to your terms of use.
6. Copy the **Bot ID** from the [Create the bot in the Microsoft Teams Developer Portal](#step-2-1) step and paste it in the **Application (client) ID** field.
   
7. Click **Save**.
   
8. Optional. Go to **Configure > Branding** to set up bot branding.
   
9. Go to **Configure > Domains**.
   
10. Click **Create your first domain** to open the **Add domain** dialog.
    
11. Enter `*.workato.com`.
    
12. Click **Add**.
    

### Configure the bot's permissions

Complete the following steps to configure the bot's permissions in the Microsoft Teams Developer Portal:

1. Go to **Configure > App features** and click **Bot**.
   
2. Select your newly created bot from the **Select an existing bot** drop-down menu.
   
3. Select **Upload and download files** in the **What can your bot do?** field.
   
4. Select **Personal**, **Team**, and **Group Chat** in the **Select the scopes where people can use your bot** field.
   
5. Click **Save**.
   
6. Click **Add a command**.
   
7. Fill in the following fields:
   
   - **Command**: Enter `help`.
   - **Description (help text)**: Enter `Type 'help' to view available commands`.
   - **Select the scopes where people can use this command**: Select **Personal**, **Team**, and **Group Chat**.
8. Click **Add**.
   
9. Click **Save**.
   

### Configure authentication redirect URLs

Complete the following steps to configure authentication redirect URLs in your Microsoft Azure portal:

1. Sign in to your [Microsoft Azure Portal](https://portal.azure.com/).
   
2. Go to **App registrations**
   
3. Click your bot on the page that displays.
   
4. Go to **Manage > Authentication**.
   
5. In **Supported account types**, make sure that **Accounts in any organizational directory (Any Microsoft Entra ID tenant - Multitenant)** is selected.
   
6. Click **+Add a platform** in **Platform configurations** and select **Web**.
   
7. Enter the redirect URI, depending on your data center.
   
   ### Workato Enterprise customers
   
   - US Data Center: `https://www.workato.com/oauth/callback`
   - EU Data Center: `https://app.eu.workato.com/oauth/callback`
   - JP Data Center: `https://app.jp.workato.com/oauth/callback`
   - SG Data Center: `https://app.sg.workato.com/oauth/callback`
   - AU Data Center: `https://app.au.workato.com/oauth/callback`
   - IL Data Center: `https://app.il.workato.com/oauth/callback`
   - CN Data Center: `https://app.workatoapp.cn/oauth/callback`
   - KR Data Center: `https://app.kr.workato.com/oauth/callback`
   - UK Data Center: `https://app.uk.workato.com/oauth/callback`
   
   ### Self-service (Workato Free, Workato Pro, or Developer Sandbox) users
   
   - Self-service Data Center: `https://app.trial.workato.com/oauth/callback`
8. Click **Configure** to save your changes.
   

### Add a client secret

Complete the following steps to add a client secret to your bot in the Microsoft Azure portal:

> **CLIENT SECRETS**
> 
> Client secrets expire periodically, typically every year, and require renewal. This applies to both Embedded and Direct use cases. For Embedded scenarios, only the Embedded partner needs to refresh the token used in the shared custom OAuth profile; end customers don't need to take any action. You can check your access token's expiration date at [portal.azure.com](https://portal.azure.com).

1. Go to **Manage > Certificates & secrets > Client secrets**.
   
2. Select **\+ New client secret**.
   
3. Enter a description for the client secret in the **Description** field.
   
4. Set an expiration date using the **Expires** drop-down menu.
   
5. Click **Add** to add the client secret to your app.
   
6. Click **Copy to clipboard** next to the secret in the **Value** column. Client secret values cannot be viewed again after they are created. Ensure that you save the secret securely before leaving the page.
   

## Configure Workato to talk to the app

Complete the following steps in Workato to complete the custom OAuth profile setup:

1. Go back to the Workato page from the [Create the Workbot in Workato](#step-1) step.
   
2. Go to the **Step 3** section and fill in the following fields:
   
   - **Client ID - your bot ID**: Enter the **Bot ID** from the [Create the bot in the Microsoft Teams Developer Portal](#step-2-1) step. Also located in **Tools > Bot management > Your bot**.
   - **Client secret**: Enter the **client secret** from the [Add a client secret](#step-2-5) step.
   - **Application ID**: Provide the app ID. You can find this value in the Developer Portal by going to **Apps**, selecting your app, and clicking **Basic information**.
3. Click **Save**.
   

## Publish to your org

Complete the following steps to publish your app to your organization:

1. Go to the Microsoft Teams Developer Portal tab.
   
2. Go to **Publish > Publish to org**.
   
3. Click **Publish your app** to submit a publish request to your Microsoft Teams admin.
   
4. Ask your Microsoft Teams admin to approve the publish request to complete the process.
   

## Add the bot to Microsoft Teams

Complete the following steps to add the bot to your Microsoft Teams instance:

1. Go to a Microsoft Teams channel and open a one-on-one chat or a group chat.
   
2. Type `@` in the text box and select **Get bots**.
   
3. Locate and select your bot.
   
4. Click **Post** to add the bot to your Microsoft Teams channel.
   

> **CONFIGURE THE ENTERPRISE WORKBOT FOR EMBEDDED CUSTOMERS**
> 
> For Embedded partners, additional steps are required to enable Enterprise Workbots for your end customers. Refer to [Configure a Microsoft Teams Enterprise Workbot for Embedded users](/en/workbot-for-teams/guides/configure-enterprise-workbot-embed) for more information.

## Set up Application permissions (optional)

To configure the Workbot app with Application permissions instead of Delegated permissions, follow this [additional step](/en/workbot-for-teams/application-permissions) to configure them in Microsoft Teams.
