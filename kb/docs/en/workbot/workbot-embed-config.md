---
url: 'https://docs.workato.com/en/workbot/workbot-embed-config.md'
description: >-
  Configure a Slack Enterprise Workbot for Embedded users, enabling partners to
  distribute a white-labeled Workbot to end customers.
---

# Configure a Slack Enterprise Workbot for Embedded users

This guide explains how Embedded partners can enable a Slack Enterprise Workbot for their end customers.

> **LIST YOUR BOT IN SLACK MARKETPLACE**
> 
> To list your white-labeled Workbot in the Slack Marketplace, contact your Customer Success Manager.

## Prerequisites

Before you begin, ensure you have a Slack Enterprise Workbot. Refer to the [Create a Slack Enterprise Workbot](/en/workbot/workbot-custom-bots) guide if you need to create one.

## Steps

Complete the following steps to configure a Slack Enterprise Workbot for Embedded customers:

1. [Activate the public distribution for your app](#step-1)
2. [Share the custom OAuth profile with an end customer](#step-2)
3. [Build your recipes](#step-3)
4. [Export the Workato manifest](#step-4)
5. [Import the package to the customer workspace](#step-5)
6. [Authenticate the customer's Workbot for Slack connection](#step-6)

### Activate the public distribution for your app

Complete the following steps to activate public distribution for your app:

1. Go to **[Your Apps](https://api.slack.com/apps)** on the Slack API website.
   
2. Select the Slack app you created in the [Create a Slack Enterprise Workbot](/en/workbot/workbot-custom-bots) guide.
   
3. Go to **Settings > Manage Distribution**.
   
4. Locate the **Share Your App With Other Workspaces** section and expand **Remove Hard Coded Information**.
   
5. Select the checkbox to confirm you've removed any hard-coded information from your app, such as OAuth tokens and webhook URLs.
   
6. Click **Activate Public Distribution** to enable public distribution for your app.
   

### Share the custom OAuth profile with an end customer

Share the custom OAuth profile created in the [Create a Slack Enterprise Workbot](/en/workbot/workbot-custom-bots) guide with your end customers. This profile enables their Slack account to access bot settings defined in your Slack account, so they don’t need to create an OAuth app in their Slack instance.

Complete the following steps to share the custom OAuth profile:

1. Sign in to your Workato account.
   
2. Go to **Manage customers**.
   
3. Select the customer.
   
4. Go to **Settings > Custom OAuth profiles**.
   
5. Click **Assign a profile** to set a custom OAuth profile for your customer workspace. The **Assign an OAuth profile** dialog appears.
   
6. Select **Workbot for Slack** from the **Select app** drop-down menu.
   
7. Select the custom OAuth profile created in the [Create a Slack Enterprise Workbot](/en/workbot/workbot-custom-bots) guide.
   

The customer workspace uses this profile by default when users create Workbot for Slack connections. You must share the OAuth profile individually with each customer workspace using this method. You can also manage OAuth profiles programmatically with [custom OAuth profiles API endpoints](/en/oem/oem-api/custom-oauth-profiles).

### Build your recipes

Develop recipes using the Workbot for Slack connection to deploy in customer workspaces.

### Export the Workato manifest

After building the recipes and sharing the OAuth profile, export a manifest containing the bot recipes to the customer workspace. Refer to the [Create a manifest](/en/recipe-development-lifecycle/export#create-a-manifest) guide or complete the following steps to export the Workato manifest:

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
   

### Authenticate the customer's Workbot for Slack connection

After importing the package in the customer workspace, the Workbot for Slack connection becomes available. Ask the customer to authenticate this connection with their Slack credentials for the workspace where they plan to install the bot.

The connection automatically uses the shared custom OAuth profile, ensuring the app package installed by the customer connects to the app configured in your Slack instance.

> **CUSTOM OAUTH PROFILE FIELD DISABLED FOR EMBEDDED CUSTOMERS**
> 
> When the customer authenticates the Workbot for Slack connection, the custom OAuth profile selector will be disabled. The connection will still use the shared custom OAuth profile, and no other custom OAuth profiles will be available for this app in this workspace.

## Outcome

The recipes in the customer workspace are ready to be started. With the custom OAuth profile included in the connection, the bot should function as expected in the customer’s Slack instance.

---
