---
url: 'https://docs.workato.com/en/connectors/microsoft-fabric.md'
description: >-
  Connect Microsoft Fabric to Workato to automate data engineering, warehousing,
  real-time analytics, and Power BI business intelligence workflows.
---

# Microsoft Fabric

[Microsoft Fabric](https://www.microsoft.com/en-us/microsoft-fabric) is a unified analytics platform that integrates data engineering, data integration, data warehousing, real-time analytics, and business intelligence (Power BI).

## Install Microsoft Fabric from the community library

Complete the following steps to install the Microsoft Fabric connector from the [community library](https://www.workato.com/browse/connectors):

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

The Microsoft Fabric connector supports the following authentication types:

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

Use authorization code grant authentication for delegated user access. The connection inherits the Fabric permissions of the Microsoft user who authorizes it.

#### Minimum and default scopes

The Microsoft Fabric connector requests the following scopes automatically. You don't need to assign these scopes in the Azure portal.

- `Tenant.ReadWrite.All`
- `Lakehouse.ReadWrite.All`
- `Lakehouse.Execute.All`
- `Workspace.ReadWrite.All`
- `DataPipeline.ReadWrite.All`
- `Item.Execute.All`
- `Item.Read.All`

Use the **Scopes** field to request additional scopes for custom actions. Enter the scopes as a comma-separated list, for example `Capacity.Read.All, Pipeline.Read.All`. The connector adds the default scopes for you.

#### Microsoft Fabric setup for authorization code grant authentication

Complete the following steps to set up Microsoft Fabric for authorization code grant authentication:

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
   

#### Connect to Microsoft Fabric with authorization code grant authentication

View connect to Microsoft Fabric with authorization code grant authentication steps

Complete the following steps to set up an authorization code grant connection to Microsoft Fabric in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Microsoft Fabric` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Microsoft Fabric authorization code connection](/assets/microsoft-fabric-auth-code-connection.DRcK17i3.png)_Microsoft Fabric authorization code connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **OAuth2 Authorization Code**.
   
6. Enter the **Client ID** of your Azure application.
   
7. Enter the **Client secret** of your Azure application.
   
8. Use the **Account type** drop-down menu to select your Azure application's account type. Options are **Single tenant**, **Multitenant**, or **Active directory multitenant**. Defaults to **Single tenant**.
   
9. Enter the **Tenant ID** of your Azure application. The **Tenant ID** field is only available when **Account type** is **Single tenant**.
   
10. Optional. Enter additional **Scopes** as a comma-separated list. Refer to [Minimum and default scopes](#auth-code-scopes) for more information.
    
11. Click **Connect**.
    
12. Sign in to Microsoft when prompted to authorize the connection.
    

### Client credentials-based authentication (OAuth 2.0)

Use client credentials-based authentication for service principal access that connects using the app identity instead of a signed-in user. This authentication type suits server-to-server automation that runs without a user present.

This authentication type requires the following values:

- Client ID
- Client secret
- Tenant ID

> **ENABLE SERVICE PRINCIPAL ACCESS**
> 
> A Fabric administrator must enable **Service principals can use Fabric APIs** in **Admin portal > Tenant settings > Developer settings**. Microsoft enables this setting by default for new tenants. Refer to the Microsoft [Developer admin settings](https://learn.microsoft.com/en-us/fabric/admin/service-admin-portal-developer) documentation for more information.

#### Microsoft Fabric setup for client credentials-based authentication (OAuth 2.0)

Complete the following steps to set up Microsoft Fabric for client credentials-based authentication:

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

A service principal can only access the workspaces you add it to. Add the service principal to each Fabric workspace your recipes use and assign a workspace role that covers the operations you need.

> **DON'T ASSIGN API PERMISSIONS**
> 
> Don't add Power BI Service permissions to the app registration. Microsoft recommends against it for service principals because the permissions go unused and can cause errors that are hard to troubleshoot. Refer to the Microsoft [Automate Premium workspace and semantic model tasks with service principals](https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-service-principal) documentation for more information.

#### Connect to Microsoft Fabric with client credentials-based authentication

View connect to Microsoft Fabric with client credentials-based authentication steps

Complete the following steps to set up a client credentials-based connection to Microsoft Fabric in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Microsoft Fabric` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Microsoft Fabric client credentials connection](/assets/microsoft-fabric-client-credentials-connection.C4P4xdHP.png)_Microsoft Fabric client credentials connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **OAuth2 Client Credentials**.
   
6. Enter the **Client ID** of your Azure application's service principal.
   
7. Enter the **Client secret** of your Azure application.
   
8. Enter the **Tenant ID** of your Azure application in GUID or friendly name format.
   
9. Click **Connect**.
   

## Connect Microsoft Entra ID to the Microsoft Fabric connector

View connect Microsoft Entra ID to the Microsoft Fabric connector steps

To connect to the Microsoft Fabric connector using a Microsoft Entra ID account, ensure that all the consent requests are granted by admins.

Complete the following steps to grant admin consent using an admin account:

1. Sign in to your Azure portal and navigate to **Enterprise Applications > Activity > Admin consent requests**.
   
2. Approve the necessary consent requests.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-fabric/cancel-item-job-instance-action.md
description: >-
  The Cancel item job instance action enables you to cancel an under execution
  job instance for an item in Microsoft Fabric.
---

# Microsoft Fabric - Cancel item job instance action

The **Cancel item job instance** action enables you to cancel an under execution job instance for an item in Microsoft Fabric.

## Input

| Input field | Description |
| --- | --- |
| Workspace ID | Select or enter the ID of the workspace where the item is located. |
| Item ID | Enter the ID of the item for which an under-executing job is present and is supposed to be cancelled. |
| Job instance ID | Enter the ID of the job you wish to cancel. |

## Output

| Output field | Description |
| --- | --- |
| Success | Status of the cancel operation. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-fabric/create-record-action.md
description: >-
  The Create record action enables you to create the specified record in
  Microsoft Fabric.
---

# Microsoft Fabric - Create record action

The **Create record** action enables you to create the specified record in Microsoft Fabric.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to create its record. Fields load dynamically based on the selected object. |

For example, if the selected object is **Lakehouse**, the input schema is as follows:

| Input field | Description |
| --- | --- |
| Workspace ID | Select or enter the ID of the workspace where the item should be created. |
| Display name | Enter the name of the lakehouse. |
| Creation payload | Enter the payload containing information for the lakehouse to be created. |
| Description | Enter the description for the lakehouse. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. For example, the output for the **Lakehouse** object, includes the following fields:

| Output field | Description |
| --- | --- |
| Description | Description of the lakehouse. |
| Display name | Name of the lakehouse. |
| Folder ID | ID of the folder where the lakehouse is created. |
| ID | ID of the lakehouse. |
| Properties | Properties of the lakehouse include the following data. Type, Default schema, One lake files path, One lake tables path, SQL endpoint properties, Connection string, ID, Provisioning status. |
| Item tag | The list of tags attached to the lakehouse is any. |
| Type | Type of the item. Lakehouse in this case. |
| Workspace ID | ID of the workspace where the Lakehouse was created. |
| Status | Status of provisioning of the lakehouse. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-fabric/delete-record-action.md
description: The Delete record action enables you to delete a record in Microsoft Fabric.
---

# Microsoft Fabric - Delete record action

The **Delete record** action enables you to delete a record in Microsoft Fabric.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to delete its record. Fields load dynamically based on the selected object. |

For example, if the selected object is **Lakehouse**, the input schema is as follows:

| Input field | Description |
| --- | --- |
| Workspace ID | Select or enter the ID of the workspace where the item is located. |
| Lakehouse ID | Select or enter the ID of the lakehouse to delete. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. To take an example of the **Lakehouse** object, the following are the output fields.

| Output field | Description |
| --- | --- |
| Success | Status of the delete operation. |

---
