---
url: 'https://docs.workato.com/en/connectors/power-bi.md'
description: >-
  Connect Power BI to Workato to automate business intelligence workflows,
  building reports and dashboards with Microsoft analytics tools.
---

# Power BI

[Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi/) is a Microsoft business analytics platform that offers interactive visualizations and business intelligence tools. It enables users to create reports and dashboards.

## API version

The Power BI connector uses the [Power BI REST API v1.0](https://learn.microsoft.com/en-us/rest/api/power-bi/).

## Prerequisites

Complete the following steps before you establish a connection to Power BI:

- [Register an application in Azure portal](#app-registration)
- [Generate a client ID (application ID)](#client-id)
- [Generate a client secret](#client-secret)
- [Assign API permissions](#api-permission)
- [Retrieve a tenant ID (for single-tenant accounts)](#tenant-id)

After you complete these prerequisites, proceed to [connect to Power BI on Workato](#connection-setup).

### Register an application in Azure portal

Complete the following steps to register an application in Azure portal:

1. Go to the [Microsoft Entra admin center](https://entra.microsoft.com/) and sign in with your **Azure admin credentials**.
   
2. Go to **Microsoft Entra ID** (formerly Azure Active Directory) in the left-hand menu.
   
3. Click **App registrations**.
   
4. Click **New registration**.
   
5. Enter the following details:
   
   - **Name**: Enter a unique name for your application.
   - **Supported Account Type**: Choose **Single Tenant** (only your organization) or **Multi-Tenant** (multiple organizations).
   - **Redirect URI**: Optional. Enter `https://www.workato.com/oauth/callback`
6. Click **Register** to create the app.
   

### Generate a client ID (application ID)

Complete the following steps to generate a client ID (application ID):

1. Go to the **Overview** page after the app is registered.
   
2. Copy the **Application (client) ID**. This is your **Client ID**. Refer to the [Set up Power BI Embedded](https://learn.microsoft.com/en-us/power-bi/developer/embedded/register-app?tabs=customers) article for more information.
   

### Generate a client secret

1. Go to **Certificates & secrets**.
   
2. Click **New client secret** in the **Client secrets** section.
   
3. Provide a **Description** and choose an **Expiration period**, such as 6 months, 1 year, or 2 years.
   
4. Click **Add** to generate the client secret.
   
5. Copy and save the client secret **Value** immediately. You can't view it later.
   
   ![Power BI Certificate](/assets/power-bi-certificate.BHZaiY9Z.png)_Power BI Certificate_
   

### Assign API permissions

Complete the following steps to assign API permissions for Power BI:

1. Go to **API permissions**.
   
2. Click **Add a permission** and select **Power BI Service**.
   
3. Select the required permissions, such as `App.Read.All`, `Dataset.ReadWrite.All`, and `Workspace.Read.All`.
   
4. Click **Add permissions**, then **Grant admin consent** if required.
   

### Retrieve a tenant ID (for single-tenant accounts)

Complete the following steps to retrieve your tenant ID:

1. Open Microsoft Entra ID, then select **Overview**.
   
2. Copy the **Directory (tenant) ID**. This is your **tenant ID**.
   
   ![Power BI Tenant ID](/assets/power-bi-tenant-id.BssKSmvy.png)_Power BI Tenant ID_
   

## How to connect to Power BI

The Power BI connector supports OAuth 2.0 authentication. Choose one of the following authentication methods based on your workspace requirements:

- [OAuth 2.0 Authorization code](#oauth-2-0-authorization-code)
- [OAuth 2.0 Client credentials](#oauth-2-0-client-credentials)

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

### OAuth 2.0 Authorization code

Use this method to access the user's default workspace (**My workspace**). This workspace is tied to a single user's identity and doesn't support sharing with service principals, groups, or other users.

Complete the following steps to establish a Power BI connection using OAuth 2.0 Authorization Code authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Power BI` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Power BI](/assets/authorization-code.Cjx8qaNn.png)_Connect to Power BI_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store your connection.
   
5. Select **OAuth2 Authorization code** as the **Auth type**.
   
6. Enter the **Client ID** used for authentication with Power BI.
   
7. Provide the **Client secret** required for authentication with Power BI.
   
8. Specify the **API version** to use.
   
9. Select your registered **Account type** in Power BI from the following options:
   
   - Single tenant
   - Multitenant
   - Active directory multitenant
10. Enter the **Tenant ID** for authentication if you selected **Single tenant** as the **Account type**.
    
11. Click **Connect**.
    

### OAuth 2.0 Client credentials

Use this method to access shared workspaces with a service principal. You must grant the service principal access to each shared workspace. This method doesn't support **My workspace**.

Complete the following steps to establish a Power BI connection using OAuth 2.0 client credentials authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Power BI` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Power BI](/assets/client-credentials.B0k3-N67.png)_Connect to Power BI_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store your connection.
   
5. Select **OAuth2 Client credentials** as the **Auth type**.
   
6. Enter the **Client ID** used for authentication.
   
7. Enter the **Client secret** used for authentication.
   
8. Specify the **API version** to use.
   
9. Enter the **Tenant ID**. This can be in GUID format or a friendly name format.
   
10. Click **Connect**.

---
