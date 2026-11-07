---
url: 'https://docs.workato.com/en/workbot-for-teams/application-permissions.md'
description: >-
  Set up Application permissions to authenticate Workbot for Microsoft Teams
  Enterprise bots without a user-dependent connection or admin role.
---

# Application permissions for Enterprise Workbots

This guide describes how to authenticate and manage permissions for Workbot for Microsoft Teams using [Application permissions](https://learn.microsoft.com/en-us/graph/permissions-overview?tabs=http#application-permissions). This configuration is available for Enterprise Workbots only.

To use Application permissions, you must complete an additional setup in Microsoft Teams. This method secures connections more effectively than Delegated permissions. It enables setting up a Workato connection without requiring the user to have all the necessary application permissions, to be an Administrator, or to maintain a user-dependent connection (for example, the connection does not disconnect when the user logs out).

## Setup requirements

To set up Application permissions, you must have one of the following roles in your Microsoft organization:

- Application administrator
- Cloud application administrator
- Global administrator
- Privileged role administrator

You can view your role assignments in [Microsoft](https://portal.azure.com/) by navigating to **Users > {Your name} > Assigned roles**.

> **WORKATO CONNECTION SETUP**
> 
> You are not required to have one of the preceding roles to set up the connection in Workato if Application permissions are used. Completing the connection setup is a one-time task.

## How to set up Application permissions

To configure Application permissions, [set up your bot app](/en/workbot-for-teams/guides/creating-enterprise-workbot). Then, follow these steps to add the necessary permissions to your bot app:

1. Navigate to [Microsoft Azure](https://portal.azure.com/).
   
2. Click **App registrations** and select your app.
   
3. Navigate to **Manage > API permissions**.
   
4. Click **\+ Add a permission**, then select **Microsoft Graph > Application permissions**.
   
5. Add the following permissions to your app:
   
   > **MINIMUM PERMISSIONS**
   > 
   > This guide describes the minimum permissions necessary to authenticate and operate Workbot in your workspace. You can add additional permissions to meet the requirements for your specific use case. For example, if you plan to use custom HTTP actions that require additional permissions, you can incorporate them at this stage.
   
   AppCatalog.Read.All
   
   - **Graph API request**: `/appCatalogs/teamsApps`
   - Description: Proactive messages. Get the ID of the installed app.
   - [Link to docs](https://learn.microsoft.com/en-us/graph/api/appcatalogs-list-teamsapps?view=graph-rest-1.0&tabs=http)
   
   Channel.ReadBasic.All
   
   - **Graph API request**: `/teams/{team-id}/channels`
   - Description: Populates the channels listed under each team in the **Message recipient** drop-down when configuring the **Post message** action.
   - [Link to docs](https://learn.microsoft.com/en-us/graph/api/channel-list?view=graph-rest-1.0&tabs=http)
   
   Organization.Read.All
   
   - **Graph API request**: `GET /organization`
   - Description: Get data about the organization where the bot is installed.
   - [Link to docs](https://learn.microsoft.com/en-us/graph/api/organization-get?view=graph-rest-1.0&tabs=http)
   
   TeamsAppInstallation.ReadWriteAndConsentSelfForUser.All
   
   This permission provides access to the following Graph API endpoints:
   
   - **Graph API request**: `GET /users/{user-id}/teamwork/installedApps`
   - Description: Proactive messages, get the bot ID in a particular user scope
   - [Link to docs](https://learn.microsoft.com/en-us/graph/api/userteamwork-list-installedapps?view=graph-rest-1.0&tabs=http)
   
   - **Graph API request**: `POST /users/{user-id}/teamwork/installedApps`
   - Description: Install the bot into the user scope
   - [Link to docs](https://learn.microsoft.com/en-us/graph/api/userteamwork-post-installedapps?view=graph-rest-1.0&tabs=http)
   
   - **Graph API request**: `GET /users/{user-id}/teamwork/installedApps/{app-installation-id}/chat`
   - Description: Get chat ID between the user and installed app
   - [Link to docs](https://learn.microsoft.com/en-us/graph/api/userscopeteamsappinstallation-get-chat?view=graph-rest-1.0&tabs=http)
   
   Team.ReadBasic.All
   
   - **Graph API request**: `/teams`
   - Description: Populates the teams listed in the **Message recipient** drop-down when configuring the **Post message** action.
   - [Link to docs](https://learn.microsoft.com/en-us/graph/api/teams-list?view=graph-rest-1.0&tabs=http)
   
   User.Read.All
   
   - **Graph API request**: `GET /users/id`
   - Description: Get user information
   - [Link to docs](https://learn.microsoft.com/en-us/graph/api/user-get?view=graph-rest-1.0&tabs=http)
   
6. Click **Add permissions** to complete the process.
   

## Complete connections in Workato

1. In Workato, navigate to **Connections**, click **Create**, and select **Connection** from the list.
   
2. Search for **Workbot for Microsoft Teams** and select it from the available apps.
   
3. Complete the following fields to connect your bot:
   
   - Connection name
     
   - Provide a unique name for your connection. You can reuse it in multiple recipes.
     
   - Location
     
   - Choose a project or folder in which to store this connection.
     
   - Auth type
     
   - Select **Application \[beta\]**.
     
   - Tenant ID \[beta\]
     
   - Provide your organization's Azure tenant ID. You can obtain this value by going to the [Azure developer portal](https://portal.azure.com/), navigating to **Microsoft Entra ID > Overview**, and copying the **Tenant ID**. Note that the value of the **Tenant ID** is identical to the **Directory ID**. You can find this in the [Azure developer portal](https://portal.azure.com/) in **Settings > Directories + Subscriptions**.
     
   - Custom OAuth profile
     
   - Select the Custom Oauth profile for your workbot.
     
4. Click **Sign in with Microsoft**. This button redirects you to the Microsoft developer portal where you can log in with your organizational credentials.
   
   ![Complete setup](/assets/complete-setup.B60p1UX8.png)_Complete setup in Workato_
   

> **PUBLISH YOUR APP**
> 
> Before you can connect and activate your Workbot, your Microsoft Teams Admin must approve your [request to publish your app](/en/workbot-for-teams/guides/creating-enterprise-workbot#step-4) to your organization. Without this approval, Workato displays an error when you try to establish a connection. Administrators can verify the approval status of your app in the [Microsoft admin interface](https://admin.teams.microsoft.com/policies/manage-apps).

---
