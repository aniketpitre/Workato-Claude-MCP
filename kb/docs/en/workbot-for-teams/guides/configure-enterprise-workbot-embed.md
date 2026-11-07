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
