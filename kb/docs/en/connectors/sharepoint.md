---
url: 'https://docs.workato.com/en/connectors/sharepoint.md'
description: >-
  The SharePoint connector lets you automate document workflows: upload,
  download, and search files and manage list rows, with triggers on new files
  and rows.
---

# SharePoint

[SharePoint](https://products.office.com/en-us/sharepoint/collaboration) is a web-based collaboration, document management and storage system integrated with Microsoft Office. It is primarily used for document management and storage but is highly configurable and usage varies substantially among organizations.

Workato's SharePoint connector enables you to build integrations and automations around SharePoint and other third-party applications.

## API version

The SharePoint connector uses the [SharePoint REST API v1](https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service).

## How to connect to SharePoint

To connect SharePoint to Workato, you must have an Azure account. Workato supports the following authentication methods:

- [Authorization code grant connection](#authentication-auth-code-grant)
- [Client credentials grant connection](#authentication-client-cred)

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

### Authorization code grant connection

This method requires the following fields:

- **Subdomain**
- **Client ID** (optional)
- **Client Secret** (optional)

#### Register the Workato app in the Azure Portal

Complete the following steps to register the Workato app and generate a client ID and secret for authorization code grant connections.

1. Register the Workato app in the Azure Portal
   
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
      
   
2. Assign permissions to your app
   
   1. Go to **Manage > API permissions** in the navigation sidebar.
      
   2. Click **\+ Add a permission** and select **SharePoint**.
      
   3. Add the required permissions listed in the [Permissions required to connect](/en/connectors/sharepoint#permissions) section. Assign **Application** or **Delegated** permissions based on your connection type.
      
   4. Click **Add permissions**.
      
      Admin consent is required for specific permissions. Refer to the [Granting admin consent](/en/connectors/sharepoint#admin-consent) section to learn more.
      
   
3. Generate a client secret
   
   Complete the following steps to generate a client secret:
   
   1. Go to **Manage > Certificates & Secrets > Client secrets**.
      
   2. Click **\+ New client secret**.
      
   3. Provide a **Description** for the client secret and specify an **Expires** date.
      
   4. Click **Add**.
      
   5. Copy and save the client secret **Value**—not the **Secret ID**—for use in Workato.
      
      ![Copy and save the client secret value](/assets/sharepoint-troubleshoot.DPBGyl4B.png)_Copy and save the client secret value_
      
   
4. Obtain the Application (client) ID from the Azure Portal
   
   1. Go to the **Overview > Essentials** section.
      
      ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
      
   2. Copy the `Application (client) ID` for use in Workato.
      
   

After you complete these steps, configure the SharePoint connection in Workato using the API permissions you set up in the Azure portal.

#### Complete setup in Workato

1. Sign in to Workato.
   
2. Select the project where you plan to store the connection.
   
3. Click **Create > Connection** or press C twice.
   
4. Search for and select `SharePoint` as your connection on the **New connection** page.
   
5. Provide a name for your connection in the **Connection name** field.
   
   ![Connect to SharePoint](/assets/auth-code-grant.CCWdwLi0.png)_Connect to SharePoint_
   
6. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
7. Select the **Authorization code grant** option from the **Authentication type** drop-down menu.
   
8. Enter your SharePoint **Subdomain**. You can find it in your SharePoint URL. For example, if your SharePoint URL is `https://abc.sharepoint.com`, the subdomain is `abc`.
   
9. Provide the **Client ID** generated in SharePoint.
   
10. Provide the **Client secret** generated in SharePoint.
    
11. Provide the name of your SharePoint site in the **Site name** field. Enter the name as it appears in the site URL. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If left blank, Workato connects to your default home site.
    
12. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
    
13. Click **Sign in with Microsoft**.
    

### Client credentials grant connection

This method requires the following values:

- **Subdomain**
- **API Scope**
- **Tenant ID**
- **Client ID**
- **Certificate**
- **Private Key**

> **USE SEPARATE CONNECTIONS FOR RECIPES AND DATA PIPELINES**
> 
> Recipe triggers and actions require a client credentials connection with the **SharePoint API** or **SharePoint & Graph API** API scope. Data pipelines require the **Graph API (Data-Pipelines only)** scope, which doesn't work with recipes. Create a separate SharePoint connection for data pipelines. Refer to [Configure Microsoft SharePoint as a data pipeline source](/en/data-orchestration/data-pipeline-recipe/configure-sharepoint) for more information.

#### Register the Workato app in the Azure Portal

Complete the following steps to register the Workato app and obtain the required values for client credentials grant connections.

1. Register the Workato app in the Azure Portal
   
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
      
   
2. Assign permissions to your app
   
   1. Go to **Manage > API permissions** in the navigation sidebar.
      
   2. Click **\+ Add a permission** and select **SharePoint**.
      
   3. Add the required permissions listed in the [Permissions required to connect](/en/connectors/sharepoint#permissions) section. Assign **Application** or **Delegated** permissions based on your connection type.
      
   4. Click **Add permissions**.
      
      Admin consent is required for specific permissions. Refer to the [Granting admin consent](/en/connectors/sharepoint#admin-consent) section to learn more.
      
   
3. Obtain the Application (client) ID and Directory (tenant) ID from the Azure Portal
   
   1. Go to the **Overview > Essentials** section.
      
      ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
      
   2. Copy the `Application (client) ID` and `Directory (tenant) ID` for use in Workato.
      
   
4. Generate a certificate and private key
   
   You need a certificate and private key to authenticate using client credentials. You can generate these locally using OpenSSL or PowerShell.
   
   Complete the following steps to generate a self-signed certificate with OpenSSL:
   
   1. Open terminal, or another CLI (command-line interface) tool.
      
   2. Create a password-protected, 2048-bit RSA private key named `domain.key`:
      
      ```bash
      openssl genrsa -out domain.key 2048
      ```
      
   3. Create a Certificate Signing Request (CSR) `domain.csr` from the private key. Provide values for the required fields when prompted:
      
      ```bash
      openssl req -key domain.key -new -out domain.csr
      ```
      
   4. Create a self-signed certificate named `domain.crt` with your private key and CSR:
      
      ```bash
      openssl x509 -signkey domain.key -in domain.csr -req -days 365 -out domain.crt
      ```
      
   5. Open `domain.crt` and copy the entire certificate string, including the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines. Use this as your **Certificate** value in Workato.
      
   6. Open `domain.key` and copy the entire private key string, including the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` lines. Use this as your **Private key** value in Workato.
      
   7. Go to **Manage > Certificates & secrets > Certificates** in the Azure Portal.
      
   8. Click **Upload certificate** and select the `domain.crt` file.
      
   9. Provide a description for the certificate.
      
   10. Click **Add**.
       
   

Return to Workato to finish [setting up your connection](#complete-setup-in-workato).

#### Complete setup in Workato

Complete the following steps to create a SharePoint connection in Workato after you configure your app in the Azure Portal:

1. Sign in to Workato.
   
2. Select the project where you plan to store the connection.
   
3. Click **Create > Connection** or press C twice.
   
4. Search for and select `SharePoint` as your connection on the **New connection** page.
   
5. Provide a name for your connection in the **Connection name** field.
   
   ![Connect to SharePoint](/assets/client-credentials-grant.DFDSyhpW.png)_Connect to SharePoint_
   
6. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
7. Select the **Client credentials** option from the **Authentication type** drop-down menu.
   
8. Enter your SharePoint **Subdomain**. You can find it in your SharePoint URL. For example, if your SharePoint URL is `https://abc.sharepoint.com`, the subdomain is `abc`.
   
9. Use the **API Scope** drop-down menu to select **SharePoint API** or **SharePoint & Graph API**. Don't select **Graph API (Data-Pipelines only)**, because it doesn't work with recipe triggers and actions.
   
10. Provide the **Directory (tenant) ID** from the Azure portal in the **Tenant ID** field.
    
11. Provide the **Application (client) ID** from the Azure portal in the **Client ID** field.
    
12. Provide the certificate string you generated in the **Certificate** field.
    
13. Provide the private key string you generated in the **Private key** field.
    
14. Provide the name of your SharePoint site in the **Site name** field. Enter the name as it appears in the site URL. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If left blank, Workato connects to your default home site.
    
15. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
    
16. Click **Sign in with Microsoft**.
    

## Permissions required to connect

You must assign the correct SharePoint REST API permissions to the Workato app in the Azure Portal before you can create a connection. The required scopes vary by authentication type.

### Minimum scopes for authorization code grant connections

The following minimum scopes are required to establish a connection to SharePoint using authorization code grant authentication:

- `Sites.Selected (Delegated)`

The `Sites.Selected` permission doesn't grant your app access to any sites by itself. A SharePoint or Global admin must grant your app access to each site you plan to use. Refer to [Grant site access for Sites.Selected](/en/data-orchestration/data-pipeline-recipe/configure-sharepoint#grant-site-access-for-sites-selected) for more information.

### Recommended scopes for authorization code grant connections

We recommend the following scopes for authorization code grant connections. These scopes are necessary to use all of this connector's triggers and actions. Additionally, you must assign these permissions to the Workato app as a **Delegated** permission in the Azure Portal:

- `AllSites.Write (Delegated)`

### Minimum scopes for client credentials grant connections

The following minimum scopes are required to establish a connection to SharePoint using client credentials grant authentication:

- `Sites.Selected (Application)`

The `Sites.Selected` permission doesn't grant your app access to any sites by itself. A SharePoint or Global admin must grant your app access to each site you plan to use. Refer to [Grant site access for Sites.Selected](/en/data-orchestration/data-pipeline-recipe/configure-sharepoint#grant-site-access-for-sites-selected) for more information.

### Recommended scopes for client credentials grant connections

We recommend the following scopes for client credentials connections. These scopes are necessary to use all of the SharePoint connector triggers and actions. Additionally, you must assign these permissions to the Workato app as an **Application** permission in the Azure Portal:

- `Sites.ReadWrite.All (Application)`

## Connect Microsoft Entra ID to the SharePoint connector

To connect to the SharePoint connector using a Microsoft Entra ID account, ensure that all the consent requests are granted by admins.

Complete the following steps to grant admin consent using an admin account:

1. Sign in to your Azure portal and navigate to **Enterprise Applications > Activity > Admin consent requests**.
   
2. Approve the necessary consent requests.

---

---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/deleted-file-folder-trigger.md
description: >-
  The Deleted file or folder trigger monitors the SharePoint Recycle Bin for
  newly deleted items.
---

# SharePoint - Deleted file or folder trigger

The **Deleted file or folder** trigger monitors the SharePoint Recycle Bin for newly deleted items. This trigger requires the [Authorization code grant](/en/connectors/sharepoint#authentication-auth-code-grant) connection type.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. Minimum value is five minutes. |
| Site name | Provide the SharePoint site name to connect to. Use the site name from the URL. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, enter `product`. Workato uses the site name from your connection setup if the field is left blank. The base URL is `https://company-name.sharepoint.com/sites`. Enter an absolute URL to override the base URL, such as `https://company-name.sharepoint.com/teams/product`. |
| When first started, this recipe should pick up events from | Specify the timestamp to start monitoring deletions from. Leave blank to start from one hour ago. You can't change this value after running or testing the recipe. |

## Output

| Output field | Description |
| --- | --- |
| Item ID | The unique ID of the deleted file or folder. |
| Title | The title of the deleted file or folder. |
| Deleted Date | The date the file or folder was deleted. |
| Deleted By | The user who deleted the file or folder. |
| Item Type | Indicates whether the item was a file or folder. |
| Directory Name | The name of the directory where the file or folder was located. |
| File/Folder Name | The name of the deleted file or folder. |
| Size (bytes) | The size in bytes of the deleted file or folder. |

---
