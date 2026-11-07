---
url: 'https://docs.workato.com/en/connectors/microsoft-teams.md'
description: >-
  Microsoft Teams integrates group chat, video conferencing, secure file
  storage, and business apps in one hub.
---

# Microsoft Teams

[Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software) is a central, digital collaboration platform that integrates workspace chat, video conferencing, file storage, and application integration into one hub. It's designed for hybrid work, allowing teams to communicate, share files, and manage projects in real-time across desktop, mobile, and web.

## Connection setup

The Microsoft Teams connector supports the following authentication types:

- [Authorization code grant authentication (OAuth 2.0)](#authentication-auth-code)
- [Client credentials-based authentication (OAuth 2.0)](#authentication-client-credentials): _Only available for tenant-specific connections_

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

### Minimum scopes

The Microsoft Teams connector requires the following scopes. You must assign these permissions to the Workato app as **Delegated** permissions in the Azure portal.

- `Channel.ReadBasic.All`
- `ChannelMessage.Read.All`
- `ChannelMessage.Send`
- `Chat.Read`
- `Chat.ReadWrite`
- `ChatMessage.Send`
- `Team.ReadBasic.All`
- `User.Read`
- `offline_access`

### Authorization code grant authentication (OAuth 2.0)

Use the Tenant ID/Domain value with tenant-specific account types.

#### Microsoft Teams setup for authorization code grant authentication

Complete the following steps to set up Microsoft Teams for authorization code grant authentication:

- [Register the Workato app in the Azure portal](#auth-register)
- [Assign permissions to your app](#assign-permissions)
- [Obtain the Directory (tenant) ID from the Azure portal](#obtain-directory-id)

##### Register the Workato app in the Azure portal

View register the Workato app in the Azure portal steps

Complete the following steps to register the Workato app in the Azure portal:

1. Sign in to the [Azure portal](https://portal.azure.com/).
   
2. Select **App registrations > + New registration**.
   
3. Enter a unique name for the application.
   
4. Use the **Supported account types** drop-down menu to select an account type.
   
5. Select **Web** from the **Select a platform** drop-down menu.
   
6. Use the following URI for the **Redirect URI**:
   
   ```html
   https://www.workato.com/oauth/callback
   ```
   
7. Select **Register**.
   

##### Assign permissions to your app

View assign permissions to your app steps

Complete the following steps to assign permissions to your app:

1. Select **Manage > API permissions** in the navigation sidebar.
   
2. Click **\+ Add a permission** and select **Microsoft Graph APIs**.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
3. Add the required permissions. You must assign **Application** or **Delegated** permissions, depending on your connection type.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**.
   
   Admin consent is required for specific permissions.
   

##### Obtain the Directory (tenant) ID from the Azure portal

View obtain the Directory (tenant) ID from the Azure portal steps

Complete the following steps to obtain the Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the `Directory (tenant) ID` for use in Workato.
   

#### Connect to Microsoft Teams with authorization code grant authentication

View connect to Microsoft Teams with authorization code grant authentication steps

Complete the following steps to set up an authorization code grant connection to Microsoft Teams in Workato:

1. Click **Create > Connection**.
   
2. Search for `Microsoft Teams` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection account type** drop-down menu to select the type of account you plan to use. The available choices are **Common** and **Tenant-specific**.
   
   **Common**
   
   - **Common**: This option allows you to sign in using enterprise and multi-tenant accounts that aren't restricted to a specific organization (tenant).
   
   ![Microsoft Teams Common connection setup](/assets/teams-connect-common.CRs_A8zB.png)_Microsoft Teams Common connection setup_
   
   **Tenant specific**
   
   - **Tenant specific**: This option is specifically designed for users who belong to a particular organization (tenant).
   
   ![Microsoft Teams Tenant specific connection setup](/assets/teams-connect-tenant-auth-code.Dunozk1-.png)_Microsoft Teams Tenant specific connection setup_
   
   Provide the `tenant ID` of the Microsoft Entra ID tenant (a GUID), or its `tenant domain` in the **Tenant ID/Domain** field. This ensures that you access resources specifically configured for that tenant. Refer to [Obtain the Directory (tenant) ID from the Azure portal](#obtain-directory-id) for more information.
   
6. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
7. Optional. The connector requests a set of scopes necessary for all triggers and actions to function properly by default. Go to the **Advanced settings** section to manually select the permissions instead. The minimum permissions required to establish a connection are `User.Read` and `offline_access`. Workato requests these permissions regardless of the permissions you select. Refer to [Minimum scopes](#minimum-scopes) for more information.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
9. Click **Sign in with Microsoft**.
   

### Client credentials-based authentication (OAuth 2.0)

This authentication type requires the following values:

- Tenant ID/Domain
- User ID
- Client ID
- Client Secret

> **COMPATIBLE AUTHENTICATION**
> 
> Client credentials-based authentication is only compatible with tenant-specific connections.

#### Microsoft Teams setup for client credentials-based authentication (OAuth 2.0)

Complete the following steps to set up Microsoft Teams for client credentials-based authentication:

- [Register the Workato app in the Azure portal](#client-credentials-register)
- [Assign permissions to your app](#assign-permissions-client-credentials)
- [Generate a client secret](#generate-client-secret)
- [Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal](#obtain-ids)
- [Obtain the User ID from the Azure portal](#obtain-user-id)

##### Register the Workato app in the Azure portal

View register the Workato app in the Azure portal steps

Complete the following steps to register the Workato app in the Azure portal:

1. Sign in to the [Azure portal](https://portal.azure.com/).
   
2. Select **App registrations > + New registration**.
   
3. Enter a unique name for the application.
   
4. Use the **Supported account types** drop-down menu to select an account type.
   
5. Select **Web** from the **Select a platform** drop-down menu.
   
6. Use the following URI for the **Redirect URI**:
   
   ```html
   https://www.workato.com/oauth/callback
   ```
   
7. Select **Register**.
   

##### Assign permissions to your app

View assign permissions to your app steps

Complete the following steps to assign permissions to your app:

1. Select **Manage > API permissions** in the navigation sidebar.
   
2. Click **\+ Add a permission** and select **Microsoft Graph APIs**.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
3. Add the required permissions. You must assign **Application** or **Delegated** permissions, depending on your connection type.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**.
   
   Admin consent is required for specific permissions.
   

##### Generate a client secret

View generate a client secret steps

Complete the following steps to generate a client secret:

1. Go to **Manage > Certificates & Secrets > Client secrets**.
   
2. Click **\+ New client secret**.
   
3. Provide a **Description** for the client secret and specify an **Expires** date.
   
4. Click **Add**.
   
5. Copy and save the client secret **Value**—not the **Secret ID**—for use in Workato.
   
   ![Copy and save the client secret value](/assets/sharepoint-troubleshoot.DPBGyl4B.png)_Copy and save the client secret value_
   

##### Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal

View obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal steps

Complete the following steps to obtain the Application ID, Object ID, and Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the **Application (client) ID**, **Object ID**, and **Directory (tenant) ID** for use in Workato.
   

##### Obtain the User ID from the Azure portal

View obtain the User ID from the Azure portal steps

Complete the following steps to obtain the User ID from the Azure portal:

1. Go to **Home > Users** to obtain the `User ID`.
   
   ![Users](/assets/users.CuDgSGeL.png)_Select users_
   
2. Search for and select the default user you plan to use to perform operations. This user doesn't establish the connection but is required for performing certain operations that an app can't perform. It's also required in picklists to pull user data. For example, the folder picklist populates folders belonging to the default user.
   
3. Copy and save the **User principal name**. Use this value as the **User ID** in Workato.
   

#### Connect to Microsoft Teams with client credentials-based authentication

View connect to Microsoft Teams with client credentials-based authentication steps

Complete the following steps to set up a client credentials-based connection to Microsoft Teams in Workato:

1. Click **Create > Connection**.
   
2. Search for `Microsoft Teams` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select **Tenant specific** as the **Connection account type**. This option is specifically designed for users who belong to a particular organization (tenant).
   
   ![Microsoft Teams Tenant specific connection account type setup](/assets/teams-connect-tenant-client-cred.DUtPSHGJ.png)_Microsoft Teams Tenant specific connection account type setup_
   
6. Provide your **Tenant ID/Domain**. This is the `Directory (tenant) ID` for your app. Refer to [Register an app in Azure](#client-credentials-register) for more information.
   
7. Use the **Authentication type** drop-down menu to select **Client credentials**.
   
8. Supply the **User ID**, **Client ID**, and **Client secret** for your app. Refer to [Obtain the User ID from the Azure portal](#obtain-user-id), [Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal](#obtain-ids), and [Generate a client secret](#generate-client-secret) for more information.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Sign in with Microsoft**.
    

## Connect Microsoft Entra ID to the Microsoft Teams connector

View connect Microsoft Entra ID to the Microsoft Teams connector steps

To connect to the Microsoft Teams connector using a Microsoft Entra ID account, ensure that all the consent requests are granted by admins.

Complete the following steps to grant admin consent using an admin account:

1. Sign in to your Azure portal and navigate to **Enterprise Applications > Activity > Admin consent requests**.
   
2. Approve the necessary consent requests.

---
