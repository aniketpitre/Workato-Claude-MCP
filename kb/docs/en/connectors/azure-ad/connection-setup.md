---
url: 'https://docs.workato.com/en/connectors/azure-ad/connection-setup.md'
description: >-
  Set up and connect Microsoft Entra ID in Workato, including registering an
  app, granting Microsoft Graph permissions, and generating a client secret.
---

# How to connect to Microsoft Entra ID

Connecting to Microsoft Entra ID (formerly Azure Active Directory) on Workato is a multistep process involving configuration steps in Microsoft Entra ID and Workato.

- [Create the Workato app in Microsoft Entra ID](#step-1)
- [Connect to Microsoft Entra ID in Workato](#step-2)

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

* * *

## Create the Workato app in Microsoft Entra ID

You must complete the following steps to create the Workato app in Microsoft Entra ID:

- [Register your application](#step-1-1)
- [Grant your application permissions](#step-1-2)
- [Generate a client secret for your application](#step-1-3)

* * *

### Register your application

Register your Workato application with Microsoft Entra ID.

1. Sign in to [Microsoft Entra ID](https://portal.azure.com/).
   
2. Select **App registrations**.
   
3. On the resulting page, click **\+ New registration**.
   
4. Name your application. This is the user-facing display name for this application. Microsoft allows you to change this name later.
   
5. In **Supported account types**, select the option that matches your use case:
   
   - **Single tenant only - <Your organization name>**: Select this if only users within your own Microsoft Entra ID directory will connect to Workato.
   - **Multiple Entra ID tenants**: Select this if users from other organizations need to connect. For example, in a vendor, partner, or multi-company deployment scenario.
   - **Any Entra ID tenants + Personal Microsoft accounts**: Select this if users from other organizations or personal account users need to connect. For example, `xxx@live.com` or `xxx@outlook.com`.
   - **Personal accounts only**: Select this if only users with personal accounts need to connect.
   
   > **UPDATE APP MANIFEST**
   > 
   > If you registered your app as a single tenant and need to switch to multitenant later, you must first update "requestedAccessTokenVersion" to 2 in the app **Manifest** before changing the account type. If you don't update the Manifest, you might encounter this error: `Property api.requestedAccessTokenVersion is invalid on the Microsoft Entra platform`. Refer to the [Microsoft Entra app manifest (Azure AD Graph format)](https://learn.microsoft.com/en-us/entra/identity-platform/reference-app-manifest) documentation for more information.
   > 
   > ![Update app Manifest](/assets/update-app-manifest.D3dNlGYn.png)_Update app Manifest_
   
6. In the **Redirect URI** field, set the platform type to **Web** and provide the following redirect URI: `https://www.workato.com/oauth/callback`.
   
7. The next page displays the details of the newly-created application. Pay attention to the **Application (client) ID** and the **Directory (tenant) ID**. You will need these values later to authenticate in Workato. Refer to step 5 in [Connect to Microsoft Entra ID in Workato](#step-2) for more information.
   
   ![App registered](/assets/app-registered.Bh9rd_SS.png)_Take note of the Application (client) ID and Directory (tenant) ID_
   

* * *

### Assign permissions to your application

Now it's time to assign permissions to our Workato application.

These instructions demonstrate how to grant the minimum permissions necessary to establish a connection with Workato. The permissions you need are variable and based on your use case. See the [Microsoft Entra ID permissions](#permissions) section for additional permissions you may need to assign to your Workato application in order for it to perform optimally.

1. Select **API permissions** from the left navigation sidebar.
   
2. Click **\+ Add a permission**.
   
3. Click **Microsoft Graph** to open the permissions interface.
   
   ![Open the permissions interface](/assets/azure-ad-permissions-api.LJRakV_a.png)_Open the permissions interface_
   
4. Select **Application permissions**.
   
   ![Application permissions](/assets/application-permissions.DhRYaUjg.png)_Select application permissions_
   
5. Scroll to **User**. Add the following permissions, along with any other necessary permissions. Refer to [Permissions](#permissions) for more information.
   
   - `Directory.Read.All`
   - `Directory.ReadWrite.All`
   - `Group.ReadWrite.All`
   - `Group.Create`
   - `Group.Read.All`
   - `GroupMember.Read.All`
   - `GroupMember.ReadWrite.All`
   - `User.ManageIdentities.All`
   - `User.Read.All`
   - `User.ReadWrite.All`
   
   ![Add the necessary permissions](/assets/azure-ad-select-permissions.wao2zArw.png)_Select the necessary permissions_
   
6. Click **Add permissions**.
   
7. You will see these permissions added to **Microsoft Graph**. However, you will need admin approval to grant them to your application officially.
   
   If you are logged in with an administrator account, click **Grant admin consent for \[your organization\]**.
   
8. Once admin consent is granted, Microsoft updates the **Status** column to **Granted**.
   
   ![Admin consent](/assets/azure-ad-permissions-granted.xuy-oQEd.png)_Once admin consent is granted, Microsoft updates the Status column_
   

* * *

### Generate a client secret for your application

1. Select **Certificates & secrets** from the left navigation sidebar.
   
2. Click **\+ New client secret**.
   
   ![Create a new client secret](/assets/azure-ad-certificates-secrets.ByQB54ul.png)_Create a new client secret_
   
3. In the interface that appears, provide a description of the secret and determine when the secret will expire.
   
4. Copy and save the **Value** in a safe place. This is the only time Microsoft Entra ID displays this value.
   

* * *

## Connect to Microsoft Entra ID in Workato

Configure the following fields in Workato.

![Connect to Microsoft Entra ID in Workato](/assets/azure-ad-connect.CS41TU-F.png)_Connect to Microsoft Entra ID in Workato_

1. - Connection name
   - Name your connection.
2. - Location
   - Choose a location (folder) for your connection.
3. - Client ID
   - Provide your Client ID, which Azure refers to as the **Application (client) ID**. Obtain this value by navigating to **Azure portal > App registrations**. Select your application and copy the **Application (client) ID**.
4. - Client secret
   - Provide your client secret, which Azure refers to as the secret **Value**. This was obtained in [Step 1.3](#step-1-3).
5. - Tenant
   - Provide the directory tenant from which you plan to request permission. Azure refers to this as the **Directory (tenant) ID**. Obtain this value by navigating to **Azure portal > App registrations**. Select your application and copy the **Directory (tenant) ID**. You can also enter the tenant domain name.
6. Click **Connect**.
   

* * *

## Permissions

There are two types of permissions **Delegated permissions** and **Application permissions** that you can assign to your application. To perform optimally, Microsoft Entra ID requires the following Microsoft Graph permissions.

Application permissions

- `Directory.Read.All`
- `Directory.ReadWrite.All`
- `Group.ReadWrite.All`
- `Group.Create`
- `Group.Read.All`
- `GroupMember.Read.All`
- `GroupMember.ReadWrite.All`
- `User.ManageIdentities.All`
- `User.Read.All`
- `User.ReadWrite.All`

Delegated permissions

- `Directory.Read.All`
- `Directory.ReadWrite.All`
- `Directory.AcessAsUser.All`
- `Group.ReadWrite.All`
- `GroupMember.ReadAll`
- `Group.Read.All`
- `Group.Read.All`
- `GroupMember.ReadWrite.All`
- `User.Read`
- `User.ReadBasic.All`
- `User.Read.All`
- `User.ReadWrite.All`

---
