---
url: 'https://docs.workato.com/en/connectors/hubspot/custom-oauth.md'
description: >-
  Create a Custom OAuth profile for the HubSpot connector in Workato to add
  extra authentication security for internal users or customers.
---

# Create a Custom OAuth profile for HubSpot

Admins can configure Custom OAuth with the HubSpot connector to add extra authentication security for their internal users or customers. Refer to [Custom OAuth profiles](/en/custom-oauth-profiles) for more information.

A Custom OAuth profile for HubSpot requires an OAuth app in your HubSpot account. You create the app in HubSpot, then enter its credentials in Workato.

> **LEGACY PUBLIC APPS**
> 
> Existing legacy public apps continue to work with Custom OAuth profiles and require no changes. HubSpot recommends the Projects-based developer platform for new apps, which the following steps use.

## Prerequisites

Creating a HubSpot OAuth app requires the HubSpot CLI, which needs Node 20 or higher. Install the CLI with `npm install -g @hubspot/cli`, then authenticate it with `hs account auth`, which opens HubSpot in your browser to generate a personal access key. Refer to the [Install the HubSpot CLI](https://developers.hubspot.com/docs/developer-tooling/local-development/hubspot-cli/install-the-cli) documentation for setup instructions.

## Create the HubSpot app

Complete the following steps to create an OAuth app in HubSpot:

1. Run `hs project create` in a terminal and respond to the prompts:
   
   | Prompt | Answer |
   | --- | --- |
   | `--name` | Enter a name for the project. |
   | `--dest` | Enter a local directory for the project. |
   | `--project-base` | Select **App**. |
   | `--distribution` | Select **Privately**. |
   | `--auth` | Select **OAuth**. |
   | `--features` | Continue without selecting features. A Custom OAuth profile doesn't require app features. |
   
2. Change to your project directory. `hs project create` prints the full path when it finishes, and the remaining `hs` commands fail outside this directory.
   
   ```shell
   cd PROJECT_DIRECTORY
   ```
   
3. Open `src/app/app-hsmeta.json` in your project directory. This file contains your app's configuration.
   
4. Add the Workato callback URL to the `redirectUrls` array, and add the scopes your connections use to the `requiredScopes` and `optionalScopes` arrays. The following example shows the fields this setup requires:
   
   ```json
   {
     "uid": "workatocustomoauth_app",
     "type": "app",
     "config": {
       "name": "workato custom oauth-App",
       "description": "Custom OAuth profile for the Workato HubSpot connector.",
       "distribution": "private",
       "auth": {
         "type": "oauth",
         "redirectUrls": ["https://www.workato.com/oauth/callback"],
         "requiredScopes": ["oauth", "crm.objects.contacts.read"],
         "optionalScopes": []
       },
       "permittedUrls": {
         "fetch": ["https://api.hubapi.com"],
         "iframe": [],
         "img": []
       }
     }
   }
   ```
   
   Keep the `oauth` scope, which HubSpot requires. HubSpot displays `name` and `description` on the authorization screen when users connect. Change the `uid` only before your first upload, because HubSpot treats a changed `uid` as a different app in later builds.
   
   > **SCOPE CONFIGURATION**
   > 
   > The preceding example includes only the scopes required to establish a connection. Your app must also list every scope users select in **Advanced settings** during connection setup, or the connection fails. Refer to the [scopes](/en/connectors/hubspot/scopes) documentation for the scopes Workato requests by default and the configuration approaches available to admins.
   
5. Run the following command to upload your configuration to HubSpot:
   
   ```shell
   hs project upload
   ```
   
6. Run the following command to open the project in HubSpot:
   
   ```shell
   hs project open
   ```
   
7. Select your app, then select the **Auth** tab.
   
8. Copy the **Client ID**. Click **Show** to reveal the **Client secret**, then copy it. HubSpot disables copying while the secret is masked.
   

Refer to HubSpot's [Create a new app using the CLI](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/create-an-app) guide for more information.

## Create the profile in Workato

Complete the following steps to create a Custom OAuth profile in Workato:

1. Go to **Tools > Custom OAuth profiles** using the navigation sidebar.
   
2. Click **\+ New custom profile**.
   
3. Select **HubSpot** from the **Application** drop-down.
   
   ![Select HubSpot](/assets/custom-oauth-embedded-create-step1.DYq6pOuX.png)_Select HubSpot_
   
4. Provide a **Name** for this account.
   
   ![Name the application](/assets/custom-oauth-embedded-create-step2.hE5048CU.png)_Name your application_
   
5. Click **Create new app** to display the credential fields.
   
6. Enter the **Client ID** and **Client secret** from your HubSpot app.
   
7. Click **Save** and **Done**.
   

## Next steps

Create a HubSpot connection in Workato, select your Custom OAuth profile, and click **Connect** to authorize the app in HubSpot. The connection displays **Connected** when authorization succeeds. Refer to [HubSpot connection setup](/en/connectors/hubspot#connection-setup) for more information.

> **UNVERIFIED APP WARNING**
> 
> HubSpot marks apps that aren't listed on the HubSpot Marketplace as unverified. Select **I understand the risks of connecting an unverified app to my account** on the authorization screen, then click **Connect app** to complete the connection.

---
