---
url: 'https://docs.workato.com/en/connectors/onedrive.md'
description: >-
  The OneDrive connector enables you to integrate and automate workflows to
  support file processing use cases.
---

# OneDrive

[OneDrive](https://www.microsoft.com/en-sg/microsoft-365/onedrive/online-cloud-storage) is a cloud storage and file hosting service by Microsoft, fully integrated with Microsoft Office. Workato's OneDrive connector enables you to seamlessly integrate and automate workflows between OneDrive and third-party applications, supporting a wide range of file processing use cases.

> **FEATURE AVAILABILITY**
> 
> The OneDrive connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## API version

The OneDrive connector uses the [Microsoft Graph API v1.0 for OneDrive](https://docs.microsoft.com/en-us/graph/api/resources/onedrive?view=graph-rest-1.0).

## Connection setup

The OneDrive connector supports the following authentication types:

- [Authorization code grant authentication (OAuth 2.0)](#authentication-auth-code)
- [Client credentials-based authentication (OAuth 2.0)](#authentication-client-credentials)

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

### Authorization code grant authentication (OAuth 2.0)

Use the Tenant ID/Domain value with tenant-specific account types.

#### Minimum and default scopes

The OneDrive connector requests the following scopes by default. These scopes support all triggers and actions. You must assign these as **Delegated** permissions in the Azure portal:

- `Files.ReadWrite`
- `Group.Read.All`
- `Files.Read`
- `offline_access`

You must add the following minimum scopes to establish a connection to OneDrive with authorization code grant authentication:

- `Files.Read`
- `offline_access`

#### OneDrive setup for authorization code grant authentication

Complete the following steps to set up OneDrive for authorization code grant authentication:

- [Register the Workato app in Azure portal](#auth-register)
- [Assign permissions to your app](#assign-permissions)
- [Obtain the Directory (tenant) ID from the Azure portal](#obtain-directory-id)

##### Register the Workato App in Azure portal

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

1. Go to your newly registered app and select **Manage > API permissions** in the navigation sidebar.
   
2. Click **\+ Add a permission** and select **Microsoft Graph APIs**.
   
3. Add the required permissions. Depending on your connection type, you must assign **Application** or **Delegated** permissions.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**. If specific permissions require admin consent, refer to [Connect Microsoft Entra ID to the Outlook connector](/en/connectors/onedrive#admin-consent) to learn more.
   

  

##### Obtain the Directory (tenant) ID from the Azure portal

View obtain the Directory (tenant) ID from the Azure portal steps

Complete the following steps to obtain the Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the `Directory (tenant) ID` for use in Workato.
   

  

#### Connect to OneDrive with authorization code grant authentication

View connect to OneDrive with authorization code grant authentication steps

Complete the following steps to set up a authorization code grant connection to OneDrive in Workato:

1. Click **Create > Connection**.
   
2. Search for `OneDrive` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection account type** drop-down menu to select the type of account you plan to use. The available choices are **Personal**, **Business**, and **Tenant-specific**.
   
   **Personal**
   
   - **Personal**: This option allows you to sign in using a personal account that isn't restricted to a specific organization (tenant).
   
   ![Personal connection](/assets/connect-personal.kBRKqbGY.png)_Personal connections_
   
   **Business**
   
   - **Business**: This option allows you to sign in using a user account that belongs to a company or organization.
   
   ![Business connection](/assets/connect-business.BTxzvVgS.png)_Business connections_
   
   **Tenant specific**
   
   - **Tenant specific**: This option is specifically designed for users who belong to a particular organization (tenant).
   
   ![Provide the tenant ID/domain](/assets/connect-tenant-specific.CTOJkWIZ.png)_Tenant specific connections_
   
   Enter the **Tenant ID/Domain**. Use either the `Directory (tenant) ID` or the tenant domain for your Microsoft Entra ID tenant. This ensures that you are accessing resources that are specifically configured for that tenant. Refer to [Obtain the Directory (tenant) ID from the Azure portal](#obtain-directory-id) for more information.
   
6. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
7. Optional. Use the **Requested permissions (OAuth scopes)** field to select specific permissions. The minimum permissions required to establish a connection are `Files.Read` and `offline_access`. Workato requests these permissions regardless of the permissions you select. Refer to [Minimum and default scopes](#authorization-code-grant-scopes) for more information.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
9. Click **Sign in with Microsoft**.
   

### Client credentials-based authentication (OAuth 2.0)

This authentication type requires the following values:

- Tenant ID/Domain
- User ID
- Client ID
- Client secret

#### Minimum and default scopes

We recommend the following scopes for client credentials-based connections. These scopes support all triggers and actions. You must assign these as **Application** permissions in the Azure portal:

- `Files.Read.All`
- `Files.ReadWrite.All`
- `Group.Read.All`
- `Sites.ReadWrite.All`

You must add the following minimum scopes to establish a connection to OneDrive with client credentials-based authentication:

- `Files.Read.All`

#### OneDrive setup for client credentials-based authentication

Complete the following steps to set up OneDrive for client credentials-based authentication:

- [Register the Workato app in the Azure portal](#client-credentials-register)
- [Assign permissions to your app](#assign-permissions-client-credentials)
- [Generate a client secret](#generate-client-secret)
- [Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal](#obtain-ids)
- [Obtain the User ID from the Azure portal](#obtain-user-id)

> **COMPATIBLE AUTHENTICATION**
> 
> Client credentials-based authentication is only compatible with tenant-specific connections.

##### Register the Workato App in the Azure portal

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

1. Go to your newly registered app and select **Manage > API permissions** in the navigation sidebar.
   
2. Click **\+ Add a permission** and select **Microsoft Graph APIs**.
   
3. Add the required permissions. Depending on your connection type, you must assign **Application** or **Delegated** permissions.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**. If specific permissions require admin consent, refer to [Connect Microsoft Entra ID to the Outlook connector](/en/connectors/onedrive#admin-consent) to learn more.
   

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
   

#### Connect to OneDrive with client credentials-based authentication

View connect to OneDrive with client credential-based authentication steps

Complete the following steps to set up a client credentials-based connection to OneDrive in Workato:

1. Click **Create > Connection**.
   
2. Search for `OneDrive` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select **Tenant specific** as the **Connection account type**. This option supports accounts tied to a specific organization (tenant).
   
   ![Tenant specific connection type](/assets/connect-tenant-specific-2.Bc0pu37N.png)_Tenant specific account connection type_
   
6. Provide your **Tenant ID/Domain**. This is the `Directory (tenant) ID` for your app. Refer to [Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal](#obtain-ids) for more information.
   
7. Use the **Authentication type** drop-down menu to select **Client credentials**.
   
8. Provide the **User ID**, **Client ID**, and **Client secret** for your app. Refer to [Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal](#obtain-ids) and [Generate a client secret](#generate-client-secret) for more information.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Sign in with Microsoft**.
    

## Connect Microsoft Entra ID to the OneDrive connector

View connect Microsoft Entra ID to the OneDrive connector steps

To connect to the OneDrive connector using a Microsoft Entra ID account, ensure that all the consent requests are granted by admins.

Complete the following steps to grant admin consent using an admin account:

1. Sign in to your Azure portal and navigate to **Enterprise Applications > Activity > Admin consent requests**.
   
2. Approve the necessary consent requests.

---
