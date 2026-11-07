---
url: 'https://docs.workato.com/en/connectors/microsoft-word.md'
description: >-
  Set up and connect the Microsoft Word connector in Workato using OAuth 2.0
  authorization code or client credentials authentication.
---

# Microsoft Word

[Microsoft Word](https://www.microsoft.com/en-us/microsoft-365/word) is a word processing application from Microsoft that's part of the Microsoft 365 suite. Workato's Microsoft Word connector enables you to integrate and automate workflows between Word documents and third-party applications.

## API version

The Microsoft Word connector uses the [Microsoft Graph API v1.0](https://learn.microsoft.com/en-us/graph/overview?context=graph%2Fapi%2F1.0&view=graph-rest-1.0).

## Connection setup

The Microsoft Word connector supports the following authentication types:

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

Authorization code grant authentication requires the following value for tenant-specific account types:

- Tenant ID

#### Minimum and default scopes

The Microsoft Word connector requests the following scopes for authorization code grant connections by default. These scopes are necessary to use all of the connector's triggers and actions. Additionally, you must assign these permissions to the Workato app as **Delegated** permissions in the Azure portal.

- `Files.Read`
- `Files.ReadWrite`
- `Files.Read.All`
- `Files.ReadWrite.All`
- `User.Read`
- `offline_access`

The following minimum scopes are required to establish a connection to Microsoft Word using authorization code grant authentication:

- `User.Read`
- `offline_access`

#### Microsoft Word setup for authorization code grant authentication

Complete the following steps to set up Microsoft Word for authorization code grant authentication:

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

1. Go to your newly registered app and select **Manage > API permissions** in the navigation sidebar.
   
2. Click **\+ Add a permission** and select **Microsoft Graph**.
   
3. Add the required permissions. You must assign **Application** or **Delegated** permissions based on your connection type.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**. If specific permissions require admin consent, refer to [Connect Microsoft Entra ID to the Microsoft Word connector](/en/connectors/microsoft-word#admin-consent) to learn more.
   

##### Obtain the Directory (tenant) ID from the Azure portal

View obtain the Directory (tenant) ID from the Azure portal steps

Complete the following steps to obtain the Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the `Directory (tenant) ID` for use in Workato.
   

#### Connect to Microsoft Word with authorization code grant authentication

View connect to Microsoft Word with authorization code grant authentication steps

Complete the following steps to set up an authorization code grant connection to Microsoft Word in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Microsoft Word` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Account type** drop-down menu to select the type of account you plan to use. The available choices are **Common** and **Tenant specific**.
   
   **Common**
   
   - **Common**: This option allows you to sign in using enterprise and multi-tenant accounts that are not restricted to a specific organization (tenant).
   
   ![Microsoft Word common connection setup](/assets/word-common-auth-code-grant-connection.B7q0iZ4k.png)_Microsoft Word common connection setup_
   
   **Tenant specific**
   
   - **Tenant specific**: This option is specifically designed for users who belong to a particular organization (tenant).
   
   ![Microsoft Word Tenant specific connection setup](/assets/word-tenant-specific-auth-code-grant-connection.BRrvVsyi.png)_Microsoft Word tenant specific connection setup_
   
   Provide the `tenant ID` of the Microsoft Entra ID tenant (a GUID) or its `tenant domain` in the **Tenant ID** field. This ensures that you access resources specifically configured for that tenant. Refer to [Register the Workato app in the Azure portal](#auth-register) for more information.
   
6. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
7. Optional. The connector requests a set of scopes necessary for all triggers and actions to function properly by default. Go to the **Advanced settings** section to manually select the permissions instead. The minimum permissions required to establish a connection are `User.Read` and `offline_access`. Workato requests these permissions regardless of the permissions you select. Refer to [Minimum and default scopes](#authorization-code-grant-scopes) for more information.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
9. Click **Sign in with Microsoft**.
   

### Client credentials-based authentication (OAuth 2.0)

This authentication method requires the following values:

- Tenant ID
- User ID
- Client ID
- Client secret

> **COMPATIBLE AUTHENTICATION**
> 
> Client credentials-based authentication is only compatible with tenant-specific connections.

#### Microsoft Word setup for client credentials-based authentication

Complete the following steps to set up Microsoft Word for client credentials-based authentication:

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

1. Go to your newly registered app and select **Manage > API permissions** in the navigation sidebar.
   
2. Click **\+ Add a permission** and select **Microsoft Graph**.
   
3. Add the required permissions. You must assign **Application** or **Delegated** permissions based on your connection type.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**. If specific permissions require admin consent, refer to [Connect Microsoft Entra ID to the Microsoft Word connector](/en/connectors/microsoft-word#admin-consent) to learn more.
   

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
   

#### Connect to Microsoft Word with client credentials-based authentication

View connect to Microsoft Word with client credentials-based authentication steps

Complete the following steps to set up a client credentials-based connection to Microsoft Word in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Microsoft Word` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select **Tenant specific** as the **Account type**. This option supports accounts tied to a specific organization (tenant).
   
   ![Microsoft Word client credentials-based connection setup](/assets/word-client-credentials-connection.CeEI1P8j.png)_Microsoft Word client credentials-based connection setup_
   
6. Provide your **Tenant ID**. This is the **Directory (tenant) ID** for your app. Refer to [Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal](#obtain-ids) for more information.
   
7. Use the **Authentication type** drop-down menu to select **Client credentials**.
   
8. Provide the **User ID**, **Client ID**, and **Client secret** for your app. Refer to [Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal](#obtain-ids) and [Generate a client secret](#generate-client-secret) for more information.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Sign in with Microsoft**.
    

## Connect Microsoft Entra ID to the Microsoft Word connector

View connect Microsoft Entra ID to the Microsoft Word connector steps

To connect to the Microsoft Word connector using a Microsoft Entra ID account, ensure that all the consent requests are granted by admins.

Complete the following steps to grant admin consent using an admin account:

1. Sign in to your Azure portal and navigate to **Enterprise Applications > Activity > Admin consent requests**.
   
2. Approve the necessary consent requests.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-word/accept-tracked-change-action.md
description: >-
  The Accept tracked change action accepts a specific tracked change in a Word
  document by its ID.
---

# Microsoft Word - Accept tracked change action

The **Accept tracked change** action accepts a specific tracked change by its ID. The action makes inserted text permanent and removes deleted text.

## Input

| Input field | Description |
| --- | --- |
| File source | Select where the document is stored. Options are **OneDrive** and **SharePoint**. |
| Document | Select the Word document from a folder-tree list scoped to the file source you selected. |
| Change ID | Enter the ID of the tracked change to accept. |

## Output

The following are a representative set of output fields. Refer to the Microsoft Graph [driveItem](https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Action taken | The operation performed, such as `accepted_insertion` or `accepted_deletion`. |
| Document ID | The document's unique identifier. |
| ETag | The ID representing the document version after the tracked change was accepted. |
| Last modified date | The date and time the document was last modified. |
| Last modified by | The application and user that last modified the document. |
| File name | The document file name, including its extension. |
| Download URL | A pre-authenticated URL you can use to download the document. |
| Web URL | The URL to view the document in the browser. |
| Parent reference | Details about the document's parent folder, including drive type, drive ID, folder name, and path. |
| Size (bytes) | The document size in bytes. |

---
