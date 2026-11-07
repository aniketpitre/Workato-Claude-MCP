---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-finance-and-operations.md
description: >-
  The Microsoft Dynamics Finance and Operations connector lets you automate ERP
  workflows: create, batch create, update, get, and search records.
---

# Microsoft Dynamics Finance and Operations

[Microsoft Dynamics Finance and Operations](https://www.microsoft.com/en-us/dynamics-365) (MDSFO) is one of Microsoft's enterprise resource planning software products. It is part of the Microsoft Dynamics app suite.

## Connector comparison

Workato offers two connectors for Microsoft Dynamics 365, each designed for a different set of applications within the Dynamics ecosystem:

- [Microsoft Dynamics 365](/en/connectors/dynamics-crm) (CRM apps)
- Microsoft Dynamics Finance and Operations (ERP apps)

Use the following table to determine which connector aligns with your organization's integration needs:

|  | Microsoft Dynamics 365 | Microsoft Dynamics Finance and Operations |
| --- | --- | --- |
| Recommended for | Sales, Customer Service, Field Service, Marketing | Finance, Supply Chain Management, Commerce, Human Resources |
| Connector type | Platform | Community |
| Required permission | `user.impersonation` (Minimum scope) | `AX.FullAccess` (Recommended scope) |
| Authentication method | OAuth 2.0 with Microsoft Dataverse | OAuth 2.0 with Microsoft Entra ID |
| API documentation reference | [Dataverse Web API](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview) | [OData API](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-entities-overview) |
| Authentication reference | [Dataverse OAuth](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/authenticate-oauth) | [OData OAuth](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/services-home-page#authentication) |

## Prerequisites

To establish a connection to MDSFO you must have an active sandbox or general instance.

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

### Set up an MDSFO sandbox instance

Complete the following step to obtain a sandbox instance of MDSFO. If you already have an instance, you can skip these steps.

1. Visit the [Microsoft free trial page](https://www.microsoft.com/en-gb/dynamics-365/free-trial) to create a free trial instance.
   
2. Select **Finance and Operations**.
   
3. Enter your account details.
   

Microsoft redirects you to a page that states your instance is being prepared. This typically takes 15-20 minutes. Microsoft sends you an email notification when the instance is ready.

![Example instance](/assets/example-instance.CLHrvm8H.png)_Example instance_

If this does not work, you can set up your Microsoft account as a standard [Dynamics Customer Engagement Trial](https://aka.ms/axtry).

## Connection setup

Complete the following steps to establish a connection to MDSFO in Workato:

- [Register the Workato App in the Azure portal](#app-register)
- [Set up the application, user, roles, and privileges](#app-setup)
- [Complete setup in Workato](#connection-setup)

## Register the Workato App in the Azure portal (Microsoft Entra ID)

To connect to MDSFO on Workato, you must obtain the connection credentials by creating an application through Azure portal with the appropriate permissions.

Sign in to the Azure portal by using an account with administrator permission. You must use an account that belongs to the same Office 365 subscription (tenant) where you plan to register the app. For example, `yourEmail@yourOrganization.onmicrosoft.com`.

1. Register the Workato app in the Azure Portal
   
   If you already have an application, use your existing application. Otherwise, complete the following steps to create a new app registration.
   
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
   
   1. In the navigation sidebar, select **Manage > API permissions**.
      
   2. Click **\+ Add a permission** and select **Dynamics ERP** API.
      
      ![Dynamic ERP](/assets/dynamic-erp.DShXNrl6.png)_Dynamic ERP_
      
   3. Select **Delegated permissions**, then check the permissions required. At minimum, the following permission is required to connect:
      
      - `AX.FullAccess`
      
      Add additional permissions as required, according to your use case.
      
      ![AX-full-access](/assets/ax-full-access.BfBMIJhs.png)_AX-full-access_
      
   4. Click **Add permissions**.
      
   
3. Generate a client secret
   
   _This step is only required for Authorization code grant connections. You can skip this step if you plan to authenticate using client credentials._
   
   Complete the following steps to generate a client secret:
   
   1. Go to **Manage > Certificates & Secrets > Client secrets**.
      
   2. Click **\+ New client secret**.
      
   3. Provide a **Description** for the client secret and specify an **Expires** date.
      
   4. Click **Add**.
      
   5. Copy and save the client secret **Value**—not the **Secret ID**—for use in Workato.
      
      ![Copy and save the client secret value](/assets/sharepoint-troubleshoot.DPBGyl4B.png)_Copy and save the client secret value_
      
   
4. Obtain the Application (client ID) from the Azure portal
   
   _This step is only required for Authorization code grant connections. You can skip this step if you plan to authenticate using client credentials._
   
   1. In the [Azure portal](https://portal.azure.com/), go to **App registrations > Overview**.
      
   2. Copy the **Application (client ID)** for use in Workato.
      
   
   Obtain the Directory (tenant) ID from the Azure portal
   
   _This step is only required for Authorization code grant connections. You can skip this step if you plan to authenticate using client credentials._
   
   1. Go to the **Overview > Essentials** section.
      
      ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
      
   2. Copy the `Directory (tenant) ID` for use in Workato.
      
   

## Set up the application, user, roles, and privileges

Completer the following steps to set up the application, user, roles and privileges in MDSFO.

1. Set up the application registered in Azure
   
   1. Click **Modules** and navigate to **System administration > setup**. Select **Microsoft Entra ID applications**.
      
      ![Entra ID applications](/assets/entra-id-applications.ClxbaEFK.png)_Entra ID applications_
      
   2. Select **New** and paste the **Client ID**, which you can copy from the application registration in Azure.
      
   3. Assign a **Name,** and add the **User ID**. This user should have the necessary roles and privileges for the entities that you need to access.
      
   4. Click **Save**.
      
      ![Standard view](/assets/standard-view.C3FTQBe5.png)_Standard view_
      
   
2. Create a new user and assign roles and privileges for entities
   
   1. Click **Modules** and go to **System administration**. Select **Users** and click **New**.
      
      ![Users](/assets/users.CF9sqfe7.png)_Users_
      
   2. Add the details, including the roles you plan to assign and click **Save**.
      
      ![New record](/assets/new-record.Bn7Qp87s.png)_New record_
      
   
3. Provide access and privileges to a specific entity
   
   Complete the following steps to create a new role and assign it privileges. This is useful in situations where you don't plan to use prebuilt roles like **Admin**.
   
   1. Click **Modules** from the left side. Go to **Security configuration** and click the **Roles**.
      
   2. Click **Create new** and enter the new role name. Click **OK**.
      
      ![New role name](/assets/new-role-name.ycepE54a.png)_New role name_
      
   3. Select the new role from the **Roles list**.
      
   4. Click **Privileges** and select **Add references**. Search for the particular privileges and select the privilege.
      
   5. Click **OK**.
      
      ![Select privileges](/assets/select-privileges.Ch4ye_ab.png)_Select privileges_
      
   6. Similarly, you can add whichever privileges you need by clicking on **Add references**.
      
      ![Add references](/assets/add-references.BZUAPL4M.png)_Add references_
      
   7. After adding the privileges, you must publish the privileges.
      
      Click **Unpublished objects** and select the Role from the **Object type** list and click **Publish all**.
      
      ![Publish objects](/assets/publish-objects.D8RLzVb5.png)_Publish objects_
      
   
4. Add the role to your newly-created user
   
   1. Go to **Modules** and select **System administration**.
      
   2. Select **Users** then select the specific user from the User list.
      
   3. Click on **Assign roles** and select one or more roles you plan to assign to the user from the **Roles list** and then click **OK**.
      
      ![Role assignment](/assets/role-assignment.ClofWDhf.png)_Role assignment_
      
   

## Complete setup in Workato

Workato supports the following types of connections to MDSFO:

- [Authorization code grant authentication (OAuth 2.0)](#authentication-auth-code)
- [Client credentials-based authentication (OAuth 2.0)](#authentication-client-credentials)

## Authorization code grant authentication (OAuth 2.0)

Complete the following steps to establish your MDSFO connection in Workato using authorization code grant authentication.

1. Install the MDSFO connector from the community library
   
   Complete the following steps to install the MDSFO connector from the [community library](https://www.workato.com/browse/connectors):
   
   1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
      
      ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
      
   2. Select the community connector you plan to install.
      
   3. Click **Install** to install the connector from the community library.
      
      ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
      
   4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
      
      ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
      
   5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
      
      ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
      
   
2. Click **Create > Connection** or press C twice.
   
3. Search for and select `Microsoft Dynamics Finance and Operations` as your connection in the **New connection** page.
   
4. Provide a name for your connection in the **Connection name** field.
   
5. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
6. Select the **Connection type** you plan to use. Select `Cloud` for direct connections, or an [on-prem group](/en/on-prem/groups) from the drop-down.
   
7. In the **OAuth 2.0 grant type** field select `Authorization code` as the connection type.
   
8. Provide your **AD domain name**. Your subdomain is provided by your MDSFO application administrator. If your Dynamics URL is `https://abc.crm.dynamics.com/adfs`, the subdomain is **abc.crm.dynamics.com**. This step is mandatory for on-prem connections and optional for cloud connections.
   
9. Supply the **Client ID** and **Client secret**for your app. Refer to the [Register an app in Azure](#app-register) section to learn more.
   
10. Click **Connect**.
    
    ![Connect MS Dynamics F&O](/assets/connect-mdf_o.vpHM8t81.png)_Connect MDSFO_
    

## Client credentials-based authentication OAuth 2.0

Complete the following steps to establish your MDSFO connection in Workato using client credentials authentication.

1. Install the MDSFO connector from the community library
   
   Complete the following steps to install the MDSFO connector from the [community library](https://www.workato.com/browse/connectors):
   
   1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
      
      ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
      
   2. Select the community connector you plan to install.
      
   3. Click **Install** to install the connector from the community library.
      
      ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
      
   4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
      
      ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
      
   5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
      
      ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
      
   
2. Click **Create > Connection** or press C twice.
   
3. Search for and select `Microsoft Dynamics Finance and Operations` as your connection in the **New connection** page.
   
4. Provide a name for your connection in the **Connection name** field.
   
5. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
6. Select the **Connection type** you plan to use. Select `Cloud` for direct connections, or an [on-prem group](/en/on-prem/groups) from the drop-down.
   
7. In the **OAuth 2.0 grant type** field select `Client credentials` as the connection type.
   
8. Provide your **AD domain name**. Your subdomain is provided by your MDSFO application administrator. If your Dynamics URL is `https://abc.crm.dynamics.com/adfs`, the subdomain is `abc.crm.dynamics.com`. This step is mandatory for on-prem connections and optional for cloud connections.
   
9. Supply the **Client ID** and **Client secret** for your app into their corresponding fields in Workato. Refer to the [Register an app in Azure](#app-register) section to learn more.
   
10. Supply the **Directory (tenant) ID** for your app into its corresponding field in Workato. Refer to the [Register an app in Azure](#app-register) section to learn more.
    
11. Click **Connect**.
    
    ![Connect MS Dynamics F&O](/assets/connect-mdf_o.vpHM8t81.png)_Connect MDSFO_
    

### Supported resources

The MDSFO connector supports all the entities present in your instance.
