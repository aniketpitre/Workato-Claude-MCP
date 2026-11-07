---
url: 'https://docs.workato.com/en/connectors/microsoft-onelake.md'
description: >-
  The Microsoft OneLake connector lets you automate data lake workflows by
  uploading and downloading files across your Microsoft Fabric tenant.
---

# Microsoft OneLake

[Microsoft OneLake](https://learn.microsoft.com/en-us/fabric/onelake/onelake-overview) is a unified data lake for the whole organization. It comes automatically with every Microsoft Fabric tenant.

## Install Microsoft OneLake from the community library

Complete the following steps to install the Microsoft OneLake connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

## Connection setup

The Microsoft OneLake connector supports the following authentication types:

- [Authorization code grant authentication (OAuth 2.0)](#authentication-auth-code): Acts as the Microsoft user who authorizes the connection
- [Client credentials-based authentication (OAuth 2.0)](#authentication-client-credentials): Acts as a service principal, without a signed-in user

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

Use authorization code grant authentication for delegated user access. The connection inherits the OneLake permissions of the Microsoft user who authorizes it.

#### Minimum and default scopes

The connector requests the `https://storage.azure.com/user_impersonation` scope automatically. You don't need to assign API permissions in the Azure portal or request additional scopes.

#### Microsoft OneLake setup for authorization code grant authentication

Complete the following steps to set up Microsoft OneLake for authorization code grant authentication:

- [Register the Workato app in the Azure portal](#auth-code-register)
- [Generate a client secret](#auth-code-secret)
- [Obtain the Application (client) ID and Directory (tenant) ID from the Azure portal](#auth-code-ids)

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
   

##### Generate a client secret

View generate a client secret steps

Complete the following steps to generate a client secret:

1. Go to **Manage > Certificates & Secrets > Client secrets**.
   
2. Click **\+ New client secret**.
   
3. Provide a **Description** for the client secret and specify an **Expires** date.
   
4. Click **Add**.
   
5. Copy and save the client secret **Value**—not the **Secret ID**—for use in Workato.
   
   ![Copy and save the client secret value](/assets/sharepoint-troubleshoot.DPBGyl4B.png)_Copy and save the client secret value_
   

##### Obtain the Application (client) ID and Directory (tenant) ID from the Azure portal

View obtain the Application (client) ID and Directory (tenant) ID steps

Complete the following steps to obtain the Application (client) ID and Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the **Application (client) ID** and **Directory (tenant) ID** for use in Workato.
   

#### Connect to Microsoft OneLake with authorization code grant authentication

View connect to Microsoft OneLake with authorization code grant authentication steps

Complete the following steps to set up an authorization code grant connection to Microsoft OneLake in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Microsoft OneLake` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Microsoft OneLake authorization code connection](/assets/microsoft-onelake-auth-code-connection.CpOr94tN.png)_Microsoft OneLake authorization code connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **OAuth2 Authorization Code**.
   
6. Enter the **Client ID** of your Azure application.
   
7. Enter the **Client secret** of your Azure application.
   
8. Use the **Account type** drop-down menu to select your Azure application's account type. Options are **Single tenant**, **Multitenant**, or **Active directory multitenant**. Defaults to **Single tenant**.
   
9. Enter the **Tenant ID** of your Azure application. The **Tenant ID** field is only available when **Account type** is **Single tenant**.
   
10. Click **Connect**.
    
11. Sign in to Microsoft when prompted to authorize the connection.
    

### Client credentials-based authentication (OAuth 2.0)

Use client credentials-based authentication for service principal access that connects using the app identity instead of a signed-in user. This authentication type suits server-to-server automation that runs without a user present.

This authentication type requires the following values:

- Client ID
- Client secret
- Tenant ID

> **ENABLE SERVICE PRINCIPAL ACCESS**
> 
> A Fabric administrator must enable **Service principals can use Fabric APIs** in **Admin portal > Tenant settings > Developer settings**. Microsoft enables this setting by default for new tenants. Refer to the Microsoft [Developer admin settings](https://learn.microsoft.com/en-us/fabric/admin/service-admin-portal-developer) documentation for more information.

#### Microsoft OneLake setup for client credentials-based authentication (OAuth 2.0)

Complete the following steps to set up Microsoft OneLake for client credentials-based authentication:

- [Register the Workato app in the Azure portal](#client-credentials-register)
- [Generate a client secret](#client-credentials-secret)
- [Obtain the Application (client) ID and Directory (tenant) ID from the Azure portal](#client-credentials-ids)
- [Grant the service principal access to your workspaces](#client-credentials-workspace-access)

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
   

##### Generate a client secret

View generate a client secret steps

Complete the following steps to generate a client secret:

1. Go to **Manage > Certificates & Secrets > Client secrets**.
   
2. Click **\+ New client secret**.
   
3. Provide a **Description** for the client secret and specify an **Expires** date.
   
4. Click **Add**.
   
5. Copy and save the client secret **Value**—not the **Secret ID**—for use in Workato.
   
   ![Copy and save the client secret value](/assets/sharepoint-troubleshoot.DPBGyl4B.png)_Copy and save the client secret value_
   

##### Obtain the Application (client) ID and Directory (tenant) ID from the Azure portal

View obtain the Application (client) ID and Directory (tenant) ID steps

Complete the following steps to obtain the Application (client) ID and Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the **Application (client) ID** and **Directory (tenant) ID** for use in Workato.
   

##### Grant the service principal access to your workspaces

View grant the service principal access to your workspaces steps

A service principal can only access the OneLake items you give it access to. Add the service principal to each Fabric workspace your recipes use and assign a workspace role that covers the operations you need.

> **DON'T ASSIGN API PERMISSIONS**
> 
> Don't add Azure Storage permissions to the app registration. OneLake authorizes a service principal through Fabric workspace roles and OneLake security instead. Refer to the Microsoft [Data security in OneLake](https://learn.microsoft.com/en-us/fabric/onelake/security/get-started-security) documentation for more information.

#### Connect to Microsoft OneLake with client credentials-based authentication

View connect to Microsoft OneLake with client credentials-based authentication steps

Complete the following steps to set up a client credentials-based connection to Microsoft OneLake in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Microsoft OneLake` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Microsoft OneLake client credentials connection](/assets/microsoft-onelake-client-credentials-connection.G3EkR_iq.png)_Microsoft OneLake client credentials connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **OAuth2 Client Credentials**.
   
6. Enter the **Client ID** of your Azure application's service principal.
   
7. Enter the **Client secret** of your Azure application.
   
8. Enter the **Tenant ID** of your Azure application in GUID or friendly name format.
   
9. Click **Connect**.
   

## Connect Microsoft Entra ID to the Microsoft OneLake connector

The Microsoft OneLake connector requests the `https://storage.azure.com/user_impersonation` delegated scope, which users can consent to themselves in most tenants. Complete this section only if your tenant restricts user consent and requires an admin to approve consent requests.

View connect Microsoft Entra ID to the Microsoft OneLake connector steps

To connect to the Microsoft OneLake connector using a Microsoft Entra ID account, ensure that all the consent requests are granted by admins.

Complete the following steps to grant admin consent using an admin account:

1. Sign in to your Azure portal and navigate to **Enterprise Applications > Activity > Admin consent requests**.
   
2. Approve the necessary consent requests.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-onelake/download-file-action.md
description: >-
  The Download file action downloads the contents of an existing file from
  Microsoft OneLake storage.
---

# Microsoft OneLake - Download file action

The **Download file** action downloads the contents of an existing file from Microsoft OneLake storage. Subsequent recipe steps can use the file contents to upload the file into another app.

There is no fixed limit on file size. The maximum file size depends on whether the download can finish within the [job timeout limit](/en/recipes/jobs#timeouts).

## Input

| Input field | Description |
| --- | --- |
| Workspace ID | Enter the ID of the workspace where the lakehouse is located. |
| Lakehouse ID | Enter the ID of the lakehouse where the file is located. |
| File path | Specify the path of the file. |

## Output

| Output field | Description |
| --- | --- |
| Contents | File contents of the downloaded file. |
| Name | Name of the file with its extension. |
| File size | Size of the file. |

---
