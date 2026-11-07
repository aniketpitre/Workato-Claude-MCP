---
url: 'https://docs.workato.com/en/workbot-for-teams/getting-started.md'
description: Learn how to set up and connect to Workbot for Microsoft Teams.
---

# Set up Workbot for Microsoft Teams

This guide explains how to set up a standard Workbot for Microsoft Teams connection.

> **STANDARD WORKBOT CONNECTION LIMIT**
> 
> Only one standard Workbot connection per Microsoft Teams organization is supported. Use [Enterprise Workbot](/en/workbot-for-teams/guides/creating-enterprise-workbot) instead if you need multiple Workbots in the same organization. Enterprise Workbot requires a custom OAuth profile.

## Prerequisites

Before you set up Workbot for Microsoft Teams, ensure you have the following:

- A [Microsoft work or school account](https://support.office.com/en-ie/article/what-account-do-i-use-with-office-and-why-do-i-need-one-914e6610-2763-47ac-ab36-602a81068235?ui=en-US&rs=en-IE&ad=IE#bkmk_msavsworkschool). These accounts are typically set up by your organization's administrator. Personal Microsoft accounts aren't supported.
- [Microsoft Graph permissions](#microsoft-graph-permissions).
- An [admin role](#required-roles) in the Azure portal.

> **MICROSOFT MFA ENFORCEMENT**
> 
> Microsoft is rolling out mandatory multifactor authentication (MFA) gradually to different applications and accounts in phases. This enforcement continues throughout 2025 and beyond. Refer to the Microsoft [Mandatory multifactor authentication for Azure and admin portals](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication?tabs=dotnet) documentation for more information.
> 
> We strongly recommend enabling MFA now for all Microsoft accounts used with Workato to avoid service disruptions from short-notice enforcement changes.
> 
> Complete the following steps to maintain uninterrupted service:
> 
> 1. Enable MFA for your Microsoft organization following the Microsoft MFA setup guide. Refer to [Set up multifactor authentication for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/set-up-multi-factor-authentication?view=o365-worldwide) for more information.
>    
> 2. Reconnect your Microsoft connection in Workato.
>    
> 3. Complete the OAuth flow with MFA when prompted.
>    
> 4. Test your recipes to ensure they work with the updated connection.
>    

### Microsoft Graph permissions

Workbot for Microsoft Teams requires the following [Microsoft Graph permissions](https://docs.microsoft.com/en-us/graph/permissions-reference):

| Permission | Type | Description |
| --- | --- | --- |
| [AppCatalog.Read.All](https://learn.microsoft.com/en-us/graph/permissions-reference#appcatalogreadall) | Delegated | Required to retrieve the installed app ID for a user from the Microsoft Teams app catalog. |
| [Channel.ReadBasic.All](https://learn.microsoft.com/en-us/graph/permissions-reference#channelreadbasicall) | Delegated | Lists channels used in **Post message** or **Post simple message** actions. |
| [Team.ReadBasic.All](https://learn.microsoft.com/en-us/graph/permissions-reference#teamreadbasicall) | Delegated | Retrieves the organization ID and name to track where the bot is installed. |
| [TeamsAppInstallation.ReadWriteAndConsentSelfForUser](https://learn.microsoft.com/en-us/graph/permissions-reference#teamsappinstallationreadwriteandconsentselfforuser) | Delegated | Required to install Workbot in the signed-in user's personal scope. |
| [User.Read](https://learn.microsoft.com/en-us/graph/permissions-reference#userread) | Delegated | Retrieves the authenticating user's ID and name to track who installed the bot. |
| [User.ReadBasic.All](https://learn.microsoft.com/en-us/graph/permissions-reference#userreadbasicall) | Delegated | Retrieves basic information about users. |
| [offline\_access](https://learn.microsoft.com/en-us/graph/permissions-reference#offline_access) | Delegated | Enables token refresh functionality. |

> **PROACTIVE MESSAGING REQUIRES APPLICATION PERMISSIONS**
> 
> These Delegated permissions install Workbot only for the signed-in user. Installing Workbot into another user's personal scope, which proactive messaging requires, needs an [Enterprise Workbot](/en/workbot-for-teams/guides/creating-enterprise-workbot) connection with [Application permissions](/en/workbot-for-teams/application-permissions). Refer to [Proactive messaging](/en/workbot-for-teams/proactive-messaging) for more information.

### Required roles

You must have one of the following roles to install Workbot in your Microsoft organization:

- Application administrator
- Cloud application administrator
- Global administrator
- Privileged role administrator

![Assigned roles](/assets/assigned-roles.BlQfGn8M.png)_Administrator Assigned Roles_

If you're installing Workbot as a global administrator, you can optionally select **Consent on behalf of your organization** during [connection setup](#complete-setup-in-workato). This allows you to reconnect Workbot in Workato without administrator approval during reauthorization.

![Installing as global admin](/assets/installing-as-global-admin.DFRKVG_H.png)_Extra checkbox to consent on behalf of organization when installing as global admin_

## Connection setup

- [Add Workbot to Microsoft Teams](#add-workbot-to-microsoft-teams)
- [Complete setup in Workato](#complete-setup-in-workato)

### Add Workbot to Microsoft Teams

Follow these steps to add Workbot to your Microsoft Teams instance:

1. Open **Microsoft Teams** and select **Apps** on the sidebar.
   
2. Search for `Workbot` in **Search for apps and more**, then select the [app](https://teams.microsoft.com/l/app/785b5e1d-93e7-48a1-bdad-2d150392935d?source=app-details-dialog) to view its details.
   
3. Select **Discover more apps** if you're installing Workbot from outside the US, then select the Workbot app specific to your region.
   
   > **NO WORKBOT SUPPORT FOR NEW DATA CENTERS**
   > 
   > Workato doesn't support Workbot in new data centers. Use one of the supported region-specific Workbot apps.
   
   Workato offers the following region-specific Workbot apps:
   
   - [Workbot AU](https://teams.microsoft.com/l/app/09559ad8-a775-4796-bb81-fe5e1c55491f?source=app-details-dialog)
   - [Workbot SG](https://teams.microsoft.com/l/app/5c479342-22b2-409d-aca3-4a69a036b390?source=app-details-dialog)
   - [Workbot EU](https://teams.microsoft.com/l/app/a671596c-9fb7-40ba-9915-c3420781b0db?source=app-details-dialog)
   - [Workbot JP](https://teams.microsoft.com/l/app/f8f326d8-577c-40d7-ad17-458dc1d6deac?source=app-details-dialog)
   
   ![Region-specific apps](/assets/region-specific-apps.i4uquFNZ.png)_Region-specific apps_
   

### Complete setup in Workato

Follow these steps to establish a Workbot for Microsoft Teams connection:

1. [Sign in](https://www.workato.com/users/sign_in) to Workato.
   
2. Select the **Connections** tab.
   
3. Click **Create > Connection** or press C+C.
   
4. Search for `Workbot for Microsoft Teams` on the **New connection** page and select it as your app.
   
5. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Workbot for Microsoft Teams](/assets/connect.DzD5vV2J.png)_Connect to Workbot for Microsoft Teams_
   
6. Select the project or folder where you plan to store the connection in the **Location** field.
   
7. Select **OAuth 2.0** as the **Auth type**. Alternatively, you can select **Application** to use app-only access. App-only access is supported only for [Enterprise Workbots](/en/workbot-for-teams/guides/creating-enterprise-workbot).
   
8. Optional. Expand **Advanced settings** and use the **API Scope(s)** drop-down menu to select additional permissions to request for the connection. For permissions Workato requests by default, see [Microsoft Graph permissions](#microsoft-graph-permissions).
   
9. Click **Sign in with Microsoft** and enter your credentials.
   
   ![Authorize Workbot](/assets/microsoft-login.7qSdItSy.png)_Authorize Workbot_
   
10. Click **Accept** when prompted to grant Workbot with its requested [permissions](#microsoft-graph-permissions).
    
    ![Global admin](/assets/installing-as-global-admin.DFRKVG_H.png)_Global admin_
    
    > **CONSENT ON BEHALF OF YOUR ORGANiZATION**
    > 
    > If you're installing Workbot as a global administrator, you can optionally select **Consent on behalf of your organization**. This allows you to reconnect Workbot in Workato without administrator approval during reauthorization.
    

You can now use your connection to build Workbot recipes. Visit the [community library](https://app.workato.com/browse/recipes?q=app:%22Workbot%20for%20Microsoft%20Teams%22) to get started.

"Bot already installed to the team" error

The **Bot already installed to the team** error means another standard Workbot connection is already active in your Microsoft Teams organization. Only one standard Workbot connection per Microsoft Teams organization is supported.

![Duplicate Workbot connection error](/assets/duplicate-workbot-connection-error.DkHC70lR.png)_Duplicate Workbot connection error_

Perform one of the following actions to resolve this:

- Find and disconnect the existing standard Workbot connection, then attempt to connect again.
- Use [Enterprise Workbot](/en/workbot-for-teams/guides/creating-enterprise-workbot) to run multiple Workbots in the same Microsoft Teams organization.

## Use Workbot in a recipe

Complete the following steps to use Workbot in a recipe:

1. Select the [View open opportunities](https://app.workato.com/recipes/916272-1-3-view-open-opportunities?community=us) recipe from the community library.
   
   ![Use recipe](/assets/use-recipe.0veiy1Fs.png)_Use recipe_
   
2. Click **Use this recipe** to make a copy of it in your workspace.
   
3. Select the project or folder where you plan to store this recipe.
   
4. Click **Copy and save**.
   
5. Click **or edit your recipe before testing**.
   
   ![Edit your recipe before testing](/assets/edit-recipe-before-testing.Bc1OK3x5.png)_Edit your recipe before testing_
   
6. Ensure you have active [Workbot for Microsoft Teams](#connection-setup) and [Salesforce](/en/connectors/salesforce#how-to-connect-to-salesforce-on-workato) connections.
   
7. Click **Save**.
   
8. Click **Exit** to leave the recipe editor, then click **Start recipe**.
   
9. Go to Microsoft Teams and send Workbot the `view_all_opportunities` command. Alternatively, you can type `help` and select **View opportunities**.
   

## The help command

The `help` command displays a list of available Workbot commands. You must have the following for this command to work correctly:

- A Workbot for Microsoft Teams connection.
- An active recipe with the Workbot for Microsoft Teams [New command trigger](/en/workbot-for-teams/workbot-triggers#workbot-command-trigger).

![Help command](/assets/teams-help._HPLQNvE.png)_Help command_

## Add Workbot to a team

Adding Workbot to your teams enables any team member to run Workbot commands by mentioning the bot.

![Help command](/assets/mentioning-workbot-in-team.DRrFx-E_.png)_Mention Workbot_

Complete the following steps to add Workbot to a team:

1. Open **Microsoft Teams**, select **Apps** from the left navigation bar, and search for `Workbot`.
   
   ![Searching for Workbot in App catalog](/assets/app-catalog.BeG9nBcI.png)_Search for Workbot in App catalog_
   
2. Select **Workbot**, then click **Open**.
   
   ![Add to team](/assets/add-workbot-to-team-1.aqhQxHf7.png)_Add to team_
   
3. Select the channel where you plan to add Workbot.
   
   ![Add to your team](/assets/add-workbot-to-team-2.BJYQAkMO.png)_Select your team_
   
4. Click **Go**.
   

You and your team members can now run Workbot commands by mentioning the bot. For example, enter and send `@workbot help` to retrieve a list of available Workbot commands.

## More resources

- [Proactive messaging](/en/workbot-for-teams/proactive-messaging)
- [Workbot triggers](/en/workbot-for-teams/workbot-triggers)
- [Workbot actions](/en/workbot-for-teams/workbot-actions)
- [Workbot buttons, pick lists, and task modules](/en/workbot-for-teams/buttons-choices-task-modules)

---
