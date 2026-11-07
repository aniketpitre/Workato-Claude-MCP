---
url: 'https://docs.workato.com/en/connectors/excel.md'
description: Connect Excel to Workato to automate workflows with your workbook data.
---

# Excel

[Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel) is a spreadsheet software program and a powerful data visualization and analysis tool.

Workato's Excel connector enables you to read data from Excel workbooks stored in OneDrive for Business, SharePoint sites, or shared Group drives.

> **SQL TRANSFORMATIONS FOR EXCEL FILE SOURCES**
> 
> The Excel connector only supports working with files stored in [SharePoint](/en/connectors/sharepoint) and [OneDrive](/en/connectors/onedrive). For processing or transforming large-volume Excel files from other sources, such as [Google Drive](/en/connectors/google-drive) or [SFTP](/en/connectors/sftp), use [SQL Transformations](/en/features/sql-transformations).

## API version

The Excel connector uses the [Excel REST API v1](https://docs.microsoft.com/en-us/graph/api/resources/excel?view=graph-rest-1.0).

## Connection setup

The Excel connector supports the following authentication types:

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

### Authorization code grant authentication (OAuth 2.0)

This authentication method requires the following value for tenant-specific account types:

- Tenant ID/Domain

#### Minimum and default scopes

The Excel connector requests the following scopes for authorization code grant connections by default. These scopes are necessary to use all of this connector's triggers and actions. Additionally, you must assign these permissions to the Workato app as **Delegated** permissions in the Azure portal.

| Permission | Description | Relevant action or trigger |
| --- | --- | --- |
| `Files.Read` | Allows the app to read the signed-in user's files. | Get cells, Get rows, List tables, List worksheets, and Search workbooks |
| `Files.ReadWrite` | Allows the app to read and write to the signed-in user's files. | All actions in `Files.Read` and Add a table, Add a worksheet, Add rows in batch, Delete row, and Update row. |
| `Group.Read.All` | Allows the app to read files for all groups the signed-in user can access. | Get cells, Get rows, List tables, List worksheets, and Search workbooks |
| `Sites.Read.All` | Allows the app to read documents in all SharePoint site collections on behalf of the signed-in user. | Get cells, Get rows, List tables, List worksheets, and Search workbooks |
| `Sites.ReadWrite.All` | Allows the app to read and write to documents in all SharePoint site collections on behalf of the signed-in user. On the consent page, this scope appears as the `Maintain access to data you have given it access to` permission. | All actions in `Sites.Read.All` and Add a table, Add a worksheet, Add rows in batch, Delete row, and Update row. Add this permission for all actions to preserve the connection's validity. |
| `User.Read` | Allows the app to sign in and read the profile of signed-in users. | Add this permission for all actions. |
| `offline_access` | Allows the app to access Microsoft Graph data after the user has signed out or the session has expired. | You must add this permission to establish a connection. |

To limit the connection to specific SharePoint sites instead of all sites, add the following scope:

- `Sites.Selected`

This scope doesn't grant your app access to any sites by itself. A SharePoint or Global admin must grant your app access to each site you plan to use. After access is granted, Excel actions can work with files on that site. Refer to [Grant site access for Sites.Selected](/en/data-orchestration/data-pipeline-recipe/configure-sharepoint#grant-site-access-for-sites-selected) for more information.

When you use `Sites.Selected`, file and table pick lists show only the files that the connected user can access.

You must add the following minimum scopes to establish a connection to Excel with authorization code grant authentication:

- `Files.Read`
- `offline_access`
- `User.Read`

#### Excel setup for authorization code grant authentication

Complete the following steps to set up Excel for authorization code grant authentication:

- [Register the Workato App in the Azure portal](#auth-register)
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

1. In the navigation sidebar, select **Manage > API permissions**.
   
2. Click **\+ Add a permission** and select **Microsoft Graph APIs**.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
3. Add the required permissions. Depending on your connection type, you must assign **Application** or **Delegated** permissions.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**.
   
   Admin consent is required for specific permissions. Refer to the [Connect Microsoft Entra ID to the Excel connector](/en/connectors/excel#admin-consent) to learn more.
   

##### Obtain the Directory (tenant) ID from the Azure portal

View obtain the Directory (tenant ID) from the Azure portal steps

Complete the following steps to obtain the Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the `Directory (tenant) ID` for use in Workato.
   

#### Connect to Excel with authorization code grant authentication

View connect to Excel with authorization code grant authentication steps

Complete the following steps to set up an authorization code grant connection to Excel in Workato:

1. Click **Create > Connection**.
   
2. Search for `Excel` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection account type** drop-down menu to select the type of account you plan to use. The available choices are **Common** and **Tenant-specific**.
   
   **Common**
   
   - **Common**: This option allows you to sign in using enterprise and multi-tenant accounts that aren't restricted to a specific organization (tenant).
   
   ![Common connection](/assets/connect-common.B1wFCm02.png)_Common connections_
   
   **Tenant specific**
   
   - **Tenant specific**: This option is specifically designed for users who belong to a particular organization (tenant).
   
   ![Provide the tenant ID/domain](/assets/connect-tenant-specific.QonywkYE.png)_Tenant specific connections_
   
   Provide the `tenant ID` of the Microsoft Entra ID tenant (a GUID), or its `tenant domain` in the **Tenant ID/Domain** field. This ensures that you access resources specifically configured for that tenant. Refer to [Obtain the Directory (tenant) ID from the Azure portal](#obtain-directory-id) for more information.
   
6. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
7. Optional. The connector requests a set of scopes necessary for all triggers and actions to function properly by default. Go to the **Advanced settings** section to manually select the permissions instead. The minimum permissions required to establish a connection are `Files.Read` and `offline_access`. Workato requests these permissions regardless of the permissions you select. Refer to [Minimum and default scopes](#code-grant-minimum-scopes) for more information.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
9. Click **Sign in with Microsoft**.
   

### Client credentials-based authentication (OAuth 2.0)

This method requires the following fields:

- Tenant ID/Domain
- User ID
- Client ID
- Client Secret

> **COMPATIBLE AUTHENTICATION**
> 
> Client credentials-based authentication is only compatible with tenant-specific connections.

#### Minimum and default scopes

The Excel connector requests the following scopes for client credentials-based connections by default. These scopes are necessary to use all of this connector's triggers and actions. Additionally, you must assign these permissions to the Workato app as **Application** permissions in the Azure portal.

| Permission | Description | Relevant action or trigger |
| --- | --- | --- |
| `Files.Read.All` | Allows the app to read the signed-in user's files. | Get cells, Get rows, List tables, List worksheets, and Search workbooks |
| `Files.ReadWrite.All` | Allows the app to read and write to the signed-in user's files. | All actions in `Files.Read` and Add a table, Add a worksheet, Add rows in batch, Delete row, and Update row. |
| `Sites.Read.All` | Allows the app to read documents in all SharePoint site collections on behalf of the signed-in user. | Get cells, Get rows, List tables, List worksheets, and Search workbooks |
| `Sites.ReadWrite.All` | Allows the app to read and write to documents in all SharePoint site collections on behalf of the signed-in user. On the consent page, this scope appears as the `Maintain access to data you have given it access to` permission. | All actions in `Sites.Read.All` and Add a table, Add a worksheet, Add rows in batch, Delete row, and Update row. This permission is recommended for all actions to preserve the connection's validity. |
| `User.Read.All` | Allows the app to sign in and read the profile of signed-in users. | This permission is recommended for all actions. |

You must add the following minimum scopes to establish a connection to Excel with client credentials-based authentication:

- `Files.Read.All`
- `User.Read.All`

#### Excel setup for client credentials-based authentication (OAuth 2.0)

Complete the following steps to set up Excel for client credentials-based authentication:

- [Register the Workato App in the Azure portal](#client-credentials-register)
- [Assign permissions to your app](#assign-permissions-client-credentials)
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

1. In the navigation sidebar, select **Manage > API permissions**.
   
2. Click **\+ Add a permission** and select **Microsoft Graph APIs**.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
3. Add the required permissions. Depending on your connection type, you must assign **Application** or **Delegated** permissions.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**.
   
   Admin consent is required for specific permissions. Refer to the [Connect Microsoft Entra ID to the Excel connector](/en/connectors/excel#admin-consent) to learn more.
   

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

View obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure Portal steps

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
   

#### Connect to Excel with client credentials-based authentication

View connect to Excel with client credentials-based authentication steps

Complete the following steps to set up a client credentials-based connection to Excel in Workato:

1. Click **Create > Connection**.
   
2. Search for `Excel` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select **Tenant specific** as the **Connection account type**. This option is specifically designed for users who belong to a particular organization (tenant).
   
   ![Tenant specific connection type](/assets/connect-tenant-specific-2.C8paKuNY.png)_Tenant specific account connection type_
   
6. Provide your **Tenant ID/Domain**. This is the `Directory (tenant) ID` for your app. Refer to [Register an app in Azure](#client-credentials-register) for more information.
   
7. Use the **Authentication type** drop-down menu to select **Client credentials**.
   
8. Supply the **User ID**, **Client ID**, and **Client secret** for your app. Refer to [Register an app in Azure](#client-credentials-register) for more information.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Sign in with Microsoft**.
    

## Connect Microsoft Entra ID to the Excel connector

View connect Microsoft Entra ID to the Excel connector steps

To connect to the Excel connector using a Microsoft Entra ID account, ensure that all the consent requests are granted by admins.

Complete the following steps to grant admin consent using an admin account:

1. Sign in to your Azure portal and navigate to **Enterprise Applications > Activity > Admin consent requests**.
   
2. Approve the necessary consent requests.

---
