---
url: 'https://docs.workato.com/en/workbot-for-teams/workbot-ms-faqs.md'
description: >-
  Answers to common questions about Workbot for Microsoft Teams, including how
  it works with Workato recipes and runs business workflows.
---

# Workbot for Microsoft Teams FAQs

Get answers to frequently asked questions about Workbot for Microsoft Teams.

How does Workbot for Microsoft Teams work with Workato?

[Workbot for Microsoft Teams](/en/workbot-for-teams/workbot#workbot-for-microsoft-teams) is a bot platform built on top of the Workato integration platform. This allows you to run business workflows directly from Microsoft Teams.

What are the main functions of Workbot for Microsoft Teams?

Workbot for Microsoft Teams allows you to execute [business workflows](/en/workbot-for-teams/using-workbot-for-teams#using-workbot-for-microsoft-teams) from within Microsoft Teams using Workbot commands. For example, you can use Workbot commands to:

- Initiate workflows
- Create ServiceNow tickets
- List Salesforce opportunities

How do Workato recipes work with Workbot for Microsoft Teams?

Workato recipes are automated workflows that span multiple apps. When integrated with Workbot for Microsoft Teams, these recipes can be triggered by specific Workbot commands within Microsoft Teams, allowing you to perform tasks across different apps.

What are Workbot commands and how do they function?

Workbot commands are instructions given to Workbot in Microsoft Teams to execute specific tasks or workflows. When a command is sent to Workbot, it triggers the corresponding recipe in Workato to execute the workflow steps.

What are the requirements to use Workbot for Microsoft Teams?

To use Workbot for Microsoft Teams, a Microsoft work or school account is [required](/en/workbot-for-teams/getting-started#prerequisites). These accounts are typically set up by an organization’s administrator. Personal Microsoft accounts aren't supported.

What Microsoft Graph permissions are required for Workbot for Microsoft Teams?

Workbot for Microsoft Teams requires various [Microsoft Graph permissions](/en/workbot-for-teams/getting-started#microsoft-graph-permissions), including:

- `User.Read`
- `Channel.ReadBasic.All`
- `Team.ReadBasic.All`

These permissions allow Workbot to retrieve necessary user and team information without admin consent.

Who can install Workbot into a Microsoft organization and what roles are required?

The following [roles](/en/workbot-for-teams/getting-started#required-roles) are required to install Workbot within a Microsoft organization:

- Application administrator
- Cloud application administrator
- Global administrator
- Privileged role administrator

Note that Global administrators have the additional ability to consent on behalf of the organization during installation.

How do I set up Workbot for Microsoft Teams in Workato?

Complete the following steps to [set up Workbot](/en/workbot-for-teams/getting-started#connection-setup) for Microsoft Teams:

1. Navigate to the top search bar in Microsoft Teams, search for `Workbot`, and then select the **Workbot** app. Alternatively, you can go to **Apps** in the left navigation bar, search for `Workbot`, and select **Add for me**.
   
2. Type `help` and press **Send** to start a conversation with Workbot. You should see a welcome message with setup instructions.
   
3. Select the **Login** link in the welcome message to log in to your Workato account. If you don't have a Workato account, select [create a new one](https://www.workato.com/users/sign_up?_gl=1*1se4dfj*_gcl_au*MjA0Nzk3OTE4Ny4xNzA2Mjg0Njg1) instead.
   
4. Click **App Connection > create a new connection** and then search for Workbot for `Microsoft Teams`.
   
5. Click **Connect** and log in using your Microsoft credentials.
   
6. Click **Yes** when prompted to allow Workato to access your information. If you are a Global administrator, you can optionally Consent on behalf of your organization. This allows users to perform reconnection in Workato without requiring an administrator during reauthorization. Teams app permission policies must allow the Workbot app for your user.
   

How do I create and start my first Workbot recipe?

Basic steps to start your [first Workbot recipe](/en/workbot-for-teams/getting-started#use-workbot-in-a-recipe) include:

- Select a pre-built recipe from the Workato community, such as **View open opportunities in Salesforce**.
- Link your Microsoft Teams and Salesforce accounts to Workbot.
- Start the recipe.

How do I add Workbot to a team in Microsoft Teams?

To [add Workbot to a team](/en/workbot-for-teams/getting-started#add-workbot-to-a-team) in Microsoft Teams:

1. Search for `Workbot` in the **Apps** section of Microsoft Teams.
   
2. Select **Workbot** and click **Add to a team**. Team members can then interact with Workbot by mentioning it in commands.

---

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

---

---
url: >-
  https://docs.workato.com/en/workbot-for-teams/guides/configure-enterprise-workbot-embed.md
description: >-
  Configure a Microsoft Teams Enterprise Workbot for Embedded customers, from
  app package download to authenticating the customer connection.
---

# Configure a Microsoft Teams Enterprise Workbot for Embedded users

This guide explains how Embedded partners can enable a Microsoft Teams Enterprise Workbot for their end customers.

> **LIST YOUR BOT IN THE MICROSOFT TEAMS APP MARKETPLACE**
> 
> To list your white-labeled Workbot in the Microsoft Teams app marketplace, contact your Customer Success Manager.

## Prerequisites

Before you begin, ensure you have a Microsoft Teams Enterprise Workbot. If you haven’t created one, refer to the [Create a Microsoft Teams Enterprise Workbot](/en/workbot-for-teams/guides/creating-enterprise-workbot) guide.

## Steps

Complete the following steps to configure a Microsoft Teams Enterprise Workbot for Embedded customers:

1. [Download and store the Microsoft Teams app package](#step-1)
2. [Share the custom OAuth profile with an end customer](#step-2)
3. [Build your recipes](#step-3)
4. [Export the Workato manifest](#step-4)
5. [Import the package to the customer workspace](#step-5)
6. [Ask the customer to install the bot in their Microsoft Teams instance](#step-6)
7. [Authenticate the customer's Workbot for Teams connection](#step-7)

### Download and store the Microsoft Teams app package

Complete the following steps to download and store the Microsoft Teams app package:

1. Sign in to the [Microsoft Teams Developer Portal](https://dev.teams.microsoft.com/).
   
2. Go to **Apps** and select the app you created in the [Create a Microsoft Teams Enterprise Workbot](/en/workbot-for-teams/guides/creating-enterprise-workbot#step-2-2) guide.
   
3. Go to **Publish > App package**.
   
4. Click **Download app package** to download the app package. Save this file without modification to share with your customers.
   

### Share the custom OAuth profile with an end customer

Share the custom OAuth profile created in the [Create a Microsoft Teams Enterprise Workbot](/en/workbot-for-teams/guides/creating-enterprise-workbot) guide with your end customers. This profile allows their Microsoft Teams account to access bot settings defined in your Microsoft Teams account, so they don’t need to create an OAuth app in their Microsoft Teams instance.

Complete the following steps to share the custom OAuth profile:

1. Sign in to your Workato account.
   
2. Go to **Manage customers**.
   
3. Select the customer.
   
4. Go to **Settings > Custom OAuth profiles**.
   
5. Click **Assign a profile** to set a custom OAuth profile for your customer workspace. The **Assign an OAuth profile** dialog appears.
   
6. Select **Workbot for Teams** from the **Select app** drop-down menu.
   
7. Select the custom OAuth profile created in the [Create a Microsoft Teams Enterprise Workbot](/en/workbot-for-teams/guides/creating-enterprise-workbot#step-3) guide.
   

The customer workspace uses this profile by default when users create Workbot for Teams connections. You must share the OAuth profile individually with each customer workspace using this method. You can also manage OAuth profiles programmatically with [custom OAuth profiles API endpoints](/en/oem/oem-api/custom-oauth-profiles).

### Build your recipes

Develop recipes using the Workbot for Teams connection to deploy in customer workspaces.

### Export the Workato manifest

After building recipes and sharing the OAuth profile, export the manifest containing bot recipes to the customer workspace. To export the Workato manifest, refer to the [Create a manifest](/en/recipe-development-lifecycle/export#create-a-manifest) guide or complete the following steps:

Export the Workato manifest

1. Go to **Tools > Recipe lifecycle management > Export**.
   
2. Click **Create a new manifest**.
   
3. Enter a name for the manifest in the **Manifest name** field.
   
4. Use the **Source folder** drop-down menu to select the source folder. All recipes and dependent assets from this folder and any subfolders become part of the manifest.
   
5. Click **Next**.
   
6. Click **Create manifest**.
   
7. Click **Build and export package**.
   
8. Click **Download** to download a zip file containing the manifest content.
   

### Import the package to the customer workspace

To import the package to the customer workspace, refer to the [Import a package](/en/recipe-development-lifecycle/import#import-a-package) guide or complete the following steps:

Import the package to the customer workspace

1. Switch to the customer workspace where you plan to import the manifest.
   
2. Go to **Tools > Recipe lifecycle management > Import**.
   
3. Click **Import**.
   
4. Select the zip file containing the package in **Select zip file**.
   
5. Use the **Target folder** drop-down menu to choose the import location.
   
6. Click **Next**.
   
7. Review the package details to confirm how it integrates with the customer workspace.
   
8. Click **Next** to start the import.
   
9. Click **Finish** when the import completes.
   

### Ask the customer to install the bot in their Microsoft Teams instance

Complete the following steps to guide the customer in installing the bot in their Microsoft Teams instance:

1. Share the generated zip file containing the Microsoft Teams app package with the customer. This file was created in the [Download and store the Microsoft Teams app package](#step-1) step.
   
2. Instruct the customer’s Microsoft Teams admin to upload the app package. They should sign in to Microsoft Teams, go to **Apps > Manage your apps > Upload an app**, and select **Upload a custom app** to complete the installation.
   

### Authenticate the Microsoft Teams bot connection in the customer’s Workato account

After importing the package in the customer workspace, the Workbot for Teams connection becomes available. Ask the customer to authenticate this connection using their credentials for the Microsoft Teams instance where they plan to install the bot.

The connection automatically uses the shared custom OAuth profile, ensuring the app package installed by the customer connects to the app configured in your Microsoft Teams instance.

> **CUSTOM OAUTH PROFILE FIELD DISABLED FOR EMBEDDED CUSTOMERS**
> 
> When the customer authenticates the Workbot for Teams connection, the custom OAuth profile selector will be disabled. The connection will still use the shared custom OAuth profile, and no other custom OAuth profiles will be available for this app in this workspace.

## Outcome

The recipes in the customer workspace are ready to be started. With the custom OAuth profile included in the connection, the bot should function as expected in the customer’s Microsoft Teams instance.

---
