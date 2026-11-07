---
url: 'https://docs.workato.com/en/connectors/dynamics-crm.md'
description: >-
  The Microsoft Dynamics 365 connector enables you to automate sales, customer
  service, field service, and marketing CRM workflows in Workato.
---

# Microsoft Dynamics 365

[Microsoft Dynamics 365](https://dynamics.microsoft.com/en-us/) is a customer relationship management software package developed by Microsoft. It is built on the Microsoft Dynamics 365 platform, allowing users to easily extend and tailor the application for their business.

## Connector comparison

Workato offers two connectors for Microsoft Dynamics 365, each designed for a different set of applications within the Dynamics ecosystem:

- Microsoft Dynamics 365 (CRM apps)
- [Microsoft Dynamics Finance and Operations](/en/connectors/microsoft-dynamics-finance-and-operations) (ERP apps)

Use the following table to determine which connector aligns with your organization's integration needs:

|  | Microsoft Dynamics 365 | Microsoft Dynamics Finance and Operations |
| --- | --- | --- |
| Recommended for | Sales, Customer Service, Field Service, Marketing | Finance, Supply Chain Management, Commerce, Human Resources |
| Connector type | Platform | Community |
| Required permission | `user.impersonation` (Minimum scope) | `AX.FullAccess` (Recommended scope) |
| Authentication method | OAuth 2.0 with Microsoft Dataverse | OAuth 2.0 with Microsoft Entra ID |
| API documentation reference | [Dataverse Web API](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview) | [OData API](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-entities-overview) |
| Authentication reference | [Dataverse OAuth](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/authenticate-oauth) | [OData OAuth](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/services-home-page#authentication) |

## API version

The Microsoft Dynamics 365 connector uses the Microsoft Dynamics 365 API v8.0 and v9.0.

Select your preferred version during [connection setup](#how-to-connect-to-microsoft-dynamics-crm-on-workato).

## How to connect to Microsoft Dynamics 365

The Microsoft Dynamics 365 connector supports the following authentication methods:

- [Authorization code grant authentication](#authentication-auth-code)
- [Client credentials authentication](#authentication-client-credentials)
- [Resource owner password credentials grant authentication](#authentication-resource-owner-password-credentials)

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

### Authorization code grant authentication

This authentication method requires the following values:

- Client ID
- Client secret

#### Register the Workato app in the Azure Portal

Complete the following steps to register the Workato app and assign it permissions for authorization code grant connections.

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
   
   1. In the navigation sidebar, select **Manage > API permissions**.
      
   2. Click **\+ Add a permission** and select **Dynamics CRM**.
      
      ![Select Dynamics CRM](/assets/dynamics-crm.DFHMudAF.png)_Select Dynamics CRM_
      
   3. Select **Delegated permissions**, then select the `user_impersonation` checkbox.
      
      ![Select permissions](/assets/app-permissions-dynamics.TGgAEhVP.png)_Select permissions_
      
   4. Click **Add permissions**.
      
   
   **Note**: Admin consent is required for specific permissions. Refer to the [Granting admin consent](/en/connectors/dynamics-crm#admin-consent) section to learn more.
   
   ![Admin consent screen](/assets/dynamics-admin-consent.D-ilQt9x.png)_Admin consent screen_
   
3. Obtain the Application (client) ID from the Azure Portal
   
   1. Go to the **Overview > Essentials** section.
      
      ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
      
   2. Copy the `Application (client) ID` for use in Workato.
      
   
4. Generate a client secret
   
   Complete the following steps to generate a client secret:
   
   1. Go to **Manage > Certificates & Secrets > Client secrets**.
      
   2. Click **\+ New client secret**.
      
   3. Provide a **Description** for the client secret and specify an **Expires** date.
      
   4. Click **Add**.
      
   5. Copy and save the client secret **Value**—not the **Secret ID**—for use in Workato.
      
      ![Copy and save the client secret value](/assets/sharepoint-troubleshoot.DPBGyl4B.png)_Copy and save the client secret value_
      
   

Return to Workato to finish setting up your connection.

#### Complete setup in Workato

Complete the following steps to establish a Microsoft Dynamics 365 connection using authorization code grant authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Microsoft Dynamics 365` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Microsoft Dynamics 365](/assets/auth-code-grant.AitXdIwi.png)_Connect to Microsoft Dynamics 365_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** to specify a cloud connection or select an on-prem group for the connection.
   
   > **ON-PREM CONNECTIONS**
   > 
   > If using an on-prem connection, you must obtain a client ID by registering your Microsoft Dynamics 365 app with the Active Directory Federation Service. [Learn more](https://technet.microsoft.com/itpro/powershell/windows/adfs/add-adfsclient).
   
6. Select **Authorization code grant** as the **Authentication type**.
   
7. Enter your Microsoft Dynamics 365 environment’s full domain, such as `abc.crm.dynamics.com`, in the **Subdomain** field.
   
8. Use the **Account type** drop-down menu to specify whether the account you're connecting to is hosted in the cloud or on-prem.
   
9. Fill in the **AD domain name** field. This field is required if you select **On-premise** as the **Account type**. For example, if your AD server is `https://abc.adfs.dynamics.com/adfs`, the AD domain name is `abc.adfs.dynamics.com`.
   
10. Enter your [client ID](#auth-register) in the **Client ID** field.
    
11. Enter your [client secret](#auth-register) in the **Client secret** field.
    
12. _Optional_. Use the **Version** drop-down menu to specify the API version you plan to use in your connection. Options include:
    
    - Version 8
    - Version 9
13. _Optional_. Expand the **Advanced settings** section to configure the **Resource URI** for which connection should be authorized. If left empty, all resources in the subdomain will be authorized. For example, `https://abc.crm.dynamics.com/api/data/v9.0/`.
    
14. _Optional_. Select a custom OAuth profile to use for the connection from the **Custom OAuth profile** drop-down menu.
    
15. Click **Sign in with Microsoft**.
    

### Client credentials authentication

This authentication method requires the following values:

- Tenant ID
- Client ID
- Client secret

#### Register the Workato app in the Azure Portal

Complete the following steps to register the Workato app and assign it permissions for client credentials-based connections.

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
   
   1. In the navigation sidebar, select **Manage > API permissions**.
      
   2. Click **\+ Add a permission** and select **Dynamics CRM**.
      
      ![Select Dynamics CRM](/assets/dynamics-crm.DFHMudAF.png)_Select Dynamics CRM_
      
   3. Select **Delegated permissions**, then select the `user_impersonation` checkbox.
      
      ![Select permissions](/assets/app-permissions-dynamics.TGgAEhVP.png)_Select permissions_
      
   4. Click **Add permissions**.
      
   
   **Note**: Admin consent is required for specific permissions. Refer to the [Granting admin consent](/en/connectors/dynamics-crm#admin-consent) section to learn more.
   
   ![Admin consent screen](/assets/dynamics-admin-consent.D-ilQt9x.png)_Admin consent screen_
   
3. Generate a client secret
   
   Complete the following steps to generate a client secret:
   
   1. Go to **Manage > Certificates & Secrets > Client secrets**.
      
   2. Click **\+ New client secret**.
      
   3. Provide a **Description** for the client secret and specify an **Expires** date.
      
   4. Click **Add**.
      
   5. Copy and save the client secret **Value**—not the **Secret ID**—for use in Workato.
      
      ![Copy and save the client secret value](/assets/sharepoint-troubleshoot.DPBGyl4B.png)_Copy and save the client secret value_
      
   
4. Obtain the Application (client) ID and Directory (tenant) ID from the Azure Portal
   
   Complete the following steps to obtain the Directory (tenant) ID from the Azure portal:
   
   1. Go to the **Overview > Essentials** section.
      
      ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
      
   2. Copy and save the `Directory (tenant) ID` for use in Workato.
      
   
5. Create an application user
   
   1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
      
   2. Select **Manage** in the navigation pane.
      
   3. In the **Manage** pane, select **Environments**. Then, select an environment from the table.
      
      ![Select an environment](/assets/power-platform-admin-center.CdyLGghH.png)_Select an environment_
      
   4. Select **Settings**.
      
   5. Select **Users + permissions**, and then select **Application users**.
      
   6. Select **\+ New app user** to open the **Create a new app user** page.
      
   7. Select **\+ Add an app** to choose the registered Microsoft Entra application that was created for the selected user, and then select **Add**.
      
   8. Select the **Business Unit** associated with the environment (subdomain) you plan to connect to in Workato.
      
      The business unit you choose determines which environment your application user can access. For example, if your environment URL is `https://abc.crm.dynamics.com`, select the business unit associated with the `abc` environment.
      
   9. Click the pencil icon next to **Security roles** to choose security roles to add to the new application user. You must select a role with at least the `prvReadEntity` privilege, such as the **Basic User** role.
      
   10. Click **Save**, then click **Create**.
       
   

Return to Workato to finish setting up your connection.

#### Complete setup in Workato

Complete the following steps to establish a Microsoft Dynamics 365 connection using client credentials authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Microsoft Dynamics 365` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Microsoft Dynamics 365](/assets/client-credentials.Dd9wiWyv.png)_Connect to Microsoft Dynamics 365_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** to specify a cloud connection or select an on-prem group for the connection.
   
   > **ON-PREM CONNECTIONS**
   > 
   > If using an on-prem connection, you must obtain a client ID by registering your Microsoft Dynamics 365 app with the Active Directory Federation Service. [Learn more](https://technet.microsoft.com/itpro/powershell/windows/adfs/add-adfsclient).
   
6. Select **Client credentials** as the **Authentication type**.
   
7. Enter your Microsoft Dynamics 365 environment’s full domain, such as `abc.crm.dynamics.com`, in the **Subdomain** field.
   
8. Use the **Account type** drop-down menu to specify whether the account you're connecting to is hosted in the cloud or on-prem.
   
9. Fill in the **AD domain name** field. This field is required if you select **On-premise** as the **Account type**. For example, if your AD server is `https://abc.adfs.dynamics.com/adfs`, the AD domain name is `abc.adfs.dynamics.com`.
   
10. Enter your [client ID](#client-credentials-register) in the **Client ID** field.
    
11. Enter your [client secret](#client-credentials-register) in the **Client secret** field.
    
12. Enter your [tenant ID](#client-credentials-register) in the **Tenant ID** field.
    
13. _Optional_. Use the **Version** drop-down menu to specify the API version you plan to use in your connection. Options include:
    
    - Version 8
    - Version 9
14. _Optional_. Expand the **Advanced settings** section to configure the **Resource URI** for which connection should be authorized. If left empty, all resources in the subdomain will be authorized. For example, `https://abc.crm.dynamics.com/api/data/v9.0/`.
    
15. _Optional_. Select a custom OAuth profile to use for the connection from the **Custom OAuth profile** drop-down menu.
    
16. Click **Sign in with Microsoft**.
    

### Resource owner password credentials grant authentication

This authentication method requires the following values:

- Client ID
- Client secret
- Username
- Password
- Tenant ID

#### Register the Workato app in the Azure Portal

Complete the following steps to register the Workato app and assign it permissions for resource owner password credentials grant connections.

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
   
   1. In the navigation sidebar, select **Manage > API permissions**.
      
   2. Click **\+ Add a permission** and select **Dynamics CRM**.
      
      ![Select Dynamics CRM](/assets/dynamics-crm.DFHMudAF.png)_Select Dynamics CRM_
      
   3. Select **Delegated permissions**, then select the `user_impersonation` checkbox.
      
      ![Select permissions](/assets/app-permissions-dynamics.TGgAEhVP.png)_Select permissions_
      
   4. Click **Add permissions**.
      
   
   **Note**: Admin consent is required for specific permissions. Refer to the [Granting admin consent](/en/connectors/dynamics-crm#admin-consent) section to learn more.
   
   ![Admin consent screen](/assets/dynamics-admin-consent.D-ilQt9x.png)_Admin consent screen_
   
3. Generate a client secret
   
   Complete the following steps to generate a client secret:
   
   1. Go to **Manage > Certificates & Secrets > Client secrets**.
      
   2. Click **\+ New client secret**.
      
   3. Provide a **Description** for the client secret and specify an **Expires** date.
      
   4. Click **Add**.
      
   5. Copy and save the client secret **Value**—not the **Secret ID**—for use in Workato.
      
      ![Copy and save the client secret value](/assets/sharepoint-troubleshoot.DPBGyl4B.png)_Copy and save the client secret value_
      
   
4. Obtain the Application (client) ID and Directory (tenant) ID from the Azure Portal
   
   Complete the following steps to obtain the Directory (tenant) ID from the Azure portal:
   
   1. Go to the **Overview > Essentials** section.
      
      ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
      
   2. Copy and save the `Directory (tenant) ID` for use in Workato.
      
   
5. Create an application user
   
   1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
      
   2. Select **Manage** in the navigation pane.
      
   3. In the **Manage** pane, select **Environments**. Then, select an environment from the table.
      
      ![Select an environment](/assets/power-platform-admin-center.CdyLGghH.png)_Select an environment_
      
   4. Select **Settings**.
      
   5. Select **Users + permissions**, and then select **Application users**.
      
   6. Select **\+ New app user** to open the **Create a new app user** page.
      
   7. Select **\+ Add an app** to choose the registered Microsoft Entra application that was created for the selected user, and then select **Add**.
      
   8. Select the **Business Unit** associated with the environment (subdomain) you plan to connect to in Workato.
      
      The business unit you choose determines which environment your application user can access. For example, if your environment URL is `https://abc.crm.dynamics.com`, select the business unit associated with the `abc` environment.
      
   9. Click the pencil icon next to **Security roles** to choose security roles to add to the new application user. You must select a role with at least the `prvReadEntity` privilege, such as the **Basic User** role.
      
   10. Click **Save**, then click **Create**.
       
   

Return to Workato to finish setting up your connection.

#### Complete setup in Workato

Complete the following steps to establish a Microsoft Dynamics 365 connection using resource owner password credentials grant authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Microsoft Dynamics 365` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Microsoft Dynamics 365](/assets/resource-owner-password-creds.BrlgU8eF.png)_Connect to Microsoft Dynamics 365_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** to specify a cloud connection or select an on-prem group for the connection.
   
   > **ON-PREM CONNECTIONS**
   > 
   > If using an on-prem connection, you must obtain a client ID by registering your Microsoft Dynamics 365 app with the Active Directory Federation Service. [Learn more](https://technet.microsoft.com/itpro/powershell/windows/adfs/add-adfsclient).
   
6. Select **Resource owner password credentials grant** as the **Authentication type**.
   
7. Enter your Microsoft Dynamics 365 environment’s full domain, such as `abc.crm.dynamics.com`, in the **Subdomain** field.
   
8. Use the **Account type** drop-down menu to specify whether the account you're connecting to is hosted in the cloud or on-prem.
   
9. Fill in the **AD domain name** field. This field is required if you select **On-premise** as the **Account type**. For example, if your AD server is `https://abc.adfs.dynamics.com/adfs`, the AD domain name is `abc.adfs.dynamics.com`.
   
10. Enter your [client ID](#resource-owner-password-credentials-register) in the **Client ID** field.
    
11. Enter your [client secret](#resource-owner-password-credentials-register) in the **Client secret** field.
    
12. Enter the username of the user who has access to Microsoft Dynamics 365 in the **Username** field. Ensure that multi-factor authentication isn't enabled for that user.
    
13. Provide password of the user who has access to Microsoft Dynamics 365 in the **Password** field.
    
14. Enter your [tenant ID](#resource-owner-password-credentials-register) in the **Tenant ID** field.
    
15. _Optional_. Use the **Version** drop-down menu to specify the API version you plan to use in your connection. Options include:
    
    - Version 8
    - Version 9
16. _Optional_. Expand the **Advanced settings** section to configure the **Resource URI** for which connection should be authorized. If left empty, all resources in the subdomain will be authorized. For example, `https://abc.crm.dynamics.com/api/data/v9.0/`.
    
17. _Optional_. Select a custom OAuth profile to use for the connection from the **Custom OAuth profile** drop-down menu.
    
18. Click **Sign in with Microsoft**.
    

## Connect Microsoft Entra ID to the Microsoft Dynamics 365 connector

To connect to the Microsoft Dynamics 365 connector using a Microsoft Entra ID account, ensure that all the consent requests are granted by admins.

Complete the following steps to grant admin consent using an admin account:

1. Sign in to your Azure portal and navigate to **Enterprise Applications > Activity > Admin consent requests**.
   
2. Approve the necessary consent requests.
   

## Extend the refresh token expiration time

When you connect to a Microsoft Dynamics 365 app, Workato uses an access token to read and write to your Dynamics instance. This access token is valid until it expires. Workato receives an accompanying refresh token with the access token. When the access token expires, Workato uses the refresh token to request a new one. If the refresh token has also expired or been revoked, the connection becomes invalid and must be re-established.

To ensure your recipes run continuously without requiring intervention, extend your refresh token expiration time. You can apply and scope your token to an OAuth application instead of applying it to the entire organization.

Learn more about token lifetimes in the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/active-directory/active-directory-configurable-token-lifetimes).

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/deleted-object-trigger.md
description: >-
  The Deleted object trigger in the Microsoft Dynamics 365 connector picks up
  deleted objects each polling interval when auditing is enabled.
---

# Microsoft Dynamics 365 - Deleted object trigger

This trigger checks for deleted objects in Microsoft Dynamics 365 after a specified interval lapses and processes each deleted object as a single trigger event. You must enable **Auditing** for Lead to use this trigger. You can enable auditing by visiting **Lead view page > Customize Entity > Enable Auditing**.

## Input

| Field | Description |
| --- | --- |
| Object | Select a standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| Trigger poll interval | Determine how frequently to check for new events. This defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | Specify the date and time to start processing events. This value can't be changed after you run or test the recipe. |

## Output

| Field | Description |
| --- | --- |
| ID | The ID of the deleted object. |
| Deleted time | The time when the object was deleted. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/export-new-updated-records-trigger.md
description: >-
  The deprecated Export new or updated records bulk trigger in the Microsoft
  Dynamics 365 connector retrieves records in batches and streams them as CSV.
---

# Microsoft Dynamics 365 - Export new or new/updated records trigger (bulk)

This trigger activates when a record in Microsoft Dynamics 365 is created or updated. This trigger retrieves records in batches and streams them as a CSV.

> **DEPRECATION NOTICE**
> 
> Workato has deprecated bulk triggers across platform connectors. You can't add new bulk triggers to recipes. Existing recipes with bulk triggers continue to run unless you delete the trigger from the recipe.
> 
> For batch processing use cases, we recommend that you use batch triggers or other [batch processing features](/en/features/batch-processing) instead.

You can use this trigger in conjunction with the [Get object schema](/en/connectors/dynamics-crm/actions/get-object-schema) action to retrieve the name and schema of a specific object and copy it to a database or data warehouse.

[Learn more about bulk triggers and ELT/ETL processes](/en/features/etl-elt-guide#bulk-vs-batch).

## Input

| Input field | Description |
| --- | --- |
| Object | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| CSV columns | Select the object fields you plan to use as columns in the CSV file content. If this field is left blank, Workato returns all fields as columns. |
| Filter condition | Condition to filter the records. Use OData $filter syntax. For example, `contains(name, 'sample')` and `revenue gt 1000000`. [Learn more about filters](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query-data-web-api#filter-results). |
| When first started, this recipe should pick up events from | When you start recipe for the first time, it picks up trigger events from this specified date and time. Defaults to one hour after the recipe starts. After the recipe runs or is tested, this value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| When exporting records to form the CSV, fetch them in batches of | _Optional_. This trigger fetches the records in a set batch before streaming it. Use this to control the size of the batch of records obtained from Microsoft Dynamics 365. The maximum value is 100. Defaults to 100 records. In most cases, Workato recommends using the default value. |

## Output

| Field | Description |
| --- | --- |
| File content | This datapill contains the output of the trigger. Take note to utilize it primarily alongside streaming compatible actions like S3 upload file streaming action. |
| Object name | Name of the object being retrieved. The object name is issue for this trigger. |
| Object schema | The schema of the object being retrieved, based on the fields the user has selected. Each field has with it the associated name, label, original datatype, and mapped datatype. This allows for easy processing. |
| Created or updated from | The time and date the record was created or updated. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/monitor-changes-entities-trigger.md
description: >-
  The Monitor changes in entities trigger in the Microsoft Dynamics 365
  connector tracks entity changes using delta links for change-tracked objects.
---

# Microsoft Dynamics 365 - Monitor changes in entities trigger

The Monitor Changes in Entities trigger in Microsoft Dynamics 365 monitors changes in entities using delta links. It is recommended to use this trigger for entities that don't have a modified on timestamp.

## Input

| Field | Description |
| --- | --- |
| Entity | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. Only objects eligible for change tracking are supported. |
| Output fields | Select the fields of the selected objects you plan to use in your recipe. All fields are returned if left blank. |
| Fetch only new changes? | Choose `Yes` to return only changes in the records after the recipe has started. Defaults to `Yes`. Recommended to avoid large number of initial jobs. |
| Trigger poll interval | Determine how frequently to check for new events. This defaults to five minutes if left blank. The minimum value allowed is five minutes. |

## Output

| Field | Description |
| --- | --- |
| Change details | This contains information about the changed object, including the fields specified in the output fields. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/monitor-changes-entities-trigger-batch.md
description: >-
  The Monitor changes in entities batch trigger in the Microsoft Dynamics 365
  connector tracks entity changes using delta links and returns them in batches.
---

# Microsoft Dynamics 365 - Monitor changes in entities trigger (batch)

The Monitor Changes in Entities Trigger (Batch) in Microsoft Dynamics 365 monitors changes in entities using delta links and retrieves changes in batches.

## Input

| Field | Description |
| --- | --- |
| Entity | Select a standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. Only objects eligible for change tracking are supported. |
| Output fields | Select the fields of the selected objects you plan to use in your recipe. All fields are returned if left blank. |
| Fetch only new changes? | Choose `Yes` to return only changes in the records after the recipe has started. Defaults to `Yes`. Recommended to avoid large number of initial jobs. |
| Batch size | Maximum number of records per trigger event. Minimum is 1, maximum is 200, default is 200. |
| Trigger poll interval | Determine how frequently to check for new events. This defaults to five minutes if left blank. The minimum value allowed is five minutes. |

## Output

| Field | Description |
| --- | --- |
| Range | The range of record IDs retrieved from the search. |
| Records | This contains a list of records. Each record contains information about the changed object, including the fields specified in the output fields. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/new-object-trigger.md
description: >-
  The New object trigger in the Microsoft Dynamics 365 connector picks up newly
  created objects each polling interval as single trigger events.
---

# Microsoft Dynamics 365 - New object trigger

The New Object trigger in Microsoft Dynamics 365 checks for newly created objects every specified interval and processes each new object as a single trigger event.

## Input

| Field | Description |
| --- | --- |
| Object | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| From | Fetch new object from the specified time. |
| Output fields | Select the fields of the selected objects you plan to use in your recipe. All fields are returned if left blank. |
| Filter condition | Condition to filter the records. Use OData $filter syntax. For example, `contains(name, 'sample')` and `revenue gt 1000000`. [Learn more about filters](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query-data-web-api#filter-results). |

## Output

| Field | Description |
| --- | --- |
| Change details | This contains information about the new object, including the fields specified in the output fields. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/new-object-trigger-real-time.md
description: >-
  The New object real-time trigger in the Microsoft Dynamics 365 connector fires
  immediately when a record is created in Microsoft Dynamics 365.
---

# Microsoft Dynamics 365 - New object trigger (real-time)

The New Object trigger (real-time) in Microsoft Dynamics 365 triggers immediately when a record is created in Microsoft Dynamics 365.

## Input

| Field | Description |
| --- | --- |
| Event name | Use a unique name to generate webhook URL. |
| Object | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| From | Fetch object from the specified time. |
| Output fields | Select the fields of the selected objects you plan to use in your recipe. All fields are returned if left blank. |

## Output

| Field | Description |
| --- | --- |
| Change details | This contains information about the new object, including the fields specified in the output fields. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/new-updated-object-trigger.md
description: >-
  The New or updated object trigger in the Microsoft Dynamics 365 connector
  picks up newly created or updated objects each polling interval.
---

# Microsoft Dynamics 365 - New or updated object trigger

The New or updated object trigger checks for newly created or updated objects when a specified interval lapses and processes each object as a single trigger event.

## Input

| Field | Description |
| --- | --- |
| Object | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| From | Fetch new or updated object from the specified time. |
| Output fields | Select the fields of the selected objects you plan to use in your recipe. All fields are returned if left blank. |
| Filter condition | Condition to filter the records. Use OData $filter syntax. For example, `contains(name, 'sample')` and `revenue gt 1000000`. [Learn more about filters](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query-data-web-api#filter-results). |

## Output

| Field | Description |
| --- | --- |
| Change details | This contains information about the changed object, including the fields specified in the output fields. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/new-updated-object-trigger-batch.md
description: >-
  The New or updated object batch trigger in the Microsoft Dynamics 365
  connector picks up newly created or updated records in batches each interval.
---

# Microsoft Dynamics 365 - New or updated object trigger (batch)

New or updated object trigger (batch) in Microsoft Dynamics 365 checks for newly created or updated objects every specified interval and retrieves a batch of new or updated records as a single trigger event.

## Input

| Field | Description |
| --- | --- |
| Object | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| From | Fetch new or updated object from the specified time. |
| Output fields | Select the fields of the selected objects you plan to use in your recipe. All fields are returned if left blank. |
| Filter condition | Condition to filter the records. Use OData $filter syntax. For example, `contains(name, 'sample')` and `revenue gt 1000000`. [Learn more about filters](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query-data-web-api#filter-results). |
| Batch size | Number of records in a single trigger event, default batch size is 100. Minimum size is 1, maximum size is 1000. |

## Output

| Field | Description |
| --- | --- |
| Range | The range of record IDs retrieved from the search. |
| Time | The time range of the records retrieved. |
| First ID | The ID of the first record in the batch. |
| Last ID | The ID of the last record in the batch. |
| Change details | This contains information about the changed object, including the fields specified in the output fields. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/new-updated-object-trigger-real-time.md
description: >-
  The New or updated object real-time trigger in the Microsoft Dynamics 365
  connector runs immediately when a record is created or updated.
---

# Microsoft Dynamics 365 - New or updated object trigger (real-time)

The New or updated object trigger (real-time) runs immediately when a record is created or updated in Microsoft Dynamics 365.

## Input

| Field | Description |
| --- | --- |
| Event name | Use a unique name to generate webhook URL. |
| Object | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| From | Fetch object from the specified time. |
| Output fields | Select the fields of the selected objects you plan to use in your recipe. All fields are returned if left blank. |
| When first started, this recipe should pick up events from | Specify the date and time to start processing events. This value can't be changed after you run or test the recipe. |

## Output

| Field | Description |
| --- | --- |
| Change details | This contains information about the changed object, including the fields specified in the output fields. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/scheduled-object-search-trigger.md
description: >-
  The Scheduled object search trigger in the Microsoft Dynamics 365 connector
  searches for objects on a set schedule and returns matching records.
---

# Microsoft Dynamics 365 - Scheduled object search trigger

The Scheduled object search trigger allows you to search for objects on a specified schedule and return results as a list of records.

## Input

| Field | Description |
| --- | --- |
| Object | Select a standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| Output fields | Select the fields of the selected objects you plan to use in your recipe. All fields are returned if left blank. |
| Filter condition | Condition to filter the records. Use OData $filter syntax. For example, `contains(name, 'sample')` and `revenue gt 1000000`. [Learn more about filters](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query-data-web-api#filter-results). |
| Batch size | Number of records in a single trigger event, default batch size is 100. Minimum size is 1, maximum size is 1000. |
| Schedule | Define the schedule for the trigger. |
| Timezone | Define the timezone of the schedule. |

## Output

| Field | Description |
| --- | --- |
| Range | The range of record IDs retrieved from the search. |
| Time | The time range of the records retrieved. |
| First ID | The ID of the first record in the batch. |
| Last ID | The ID of the last record in the batch. |
| First batch | Whether this is the first batch of records. |
| Last batch | Whether this is the last batch of records. |
| Starting offset | The offset number for the first record of this batch. |
| Ending offset | The offset number for the last record of this batch. |
| Records | This contains a list of records. Each record contains information about the object, including the fields specified in the output fields. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/close-case-action.md
description: >-
  The Close case action in the Microsoft Dynamics 365 connector lets you close a
  case with a resolution type, details, and billable time.
---

# Microsoft Dynamics 365 - Close case action

This action closes a case in Microsoft Dynamics 365.

## Input

| Field | Description |
| --- | --- |
| Case ID | Provide the Case ID. This is located in the URL of the case page. |
| Resolution type | Select the type of resolution. Available options include `Problem solved` and `Information provided`. |
| Resolution | Provide details about the resolution. |
| Billable time | Specify the amount of billable time spent on the case. |
| Remarks | Provide remarks or comments about the case. |

## Output

There is no output for this action.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/create-object-action.md
description: >-
  The Create object action in the Microsoft Dynamics 365 connector lets you
  create a new record for a standard or custom object.
---

# Microsoft Dynamics 365 - Create object action

This action creates a new record for a specified object in Microsoft Dynamics 365.

## Input

| Field | Description |
| --- | --- |
| Object | Select a standard or custom Microsoft Dynamics 365 object to create. For example, `Lead`. |
| Object Fields | Specify fields for the new object that you plan to create. |

## Output

The output datatree contains the details of the newly created object. Each field corresponds to the attributes of the object in Microsoft Dynamics 365.

| Field | Description |
| --- | --- |
| Object Fields | Fields of the created object. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/create-object-action-batch.md
description: >-
  The Create object batch action in the Microsoft Dynamics 365 connector lets
  you create multiple records for a specified object in a single batch.
---

# Microsoft Dynamics 365 - Create object batch action

This action creates multiple records for a specified object in Microsoft Dynamics 365 in a single batch.

> **BATCH FAILURE BEHAVIOR**
> 
> Microsoft Dynamics 365 fails the entire batch if any record creation encounters an error when the **Allow partial batch create** field is set to **No**. None of the records create, even if some are valid.
> 
> Set the **Allow partial batch create** field to **Yes** to create all valid records and skip those that fail. Dynamics 365 then returns mixed results that show which records succeed and which fail.

## Input

| Field | Description |
| --- | --- |
| Object | Select any standard or custom Microsoft Dynamics 365 object to create in batches. For example, `Lead`. |
| Allow partial batch create | Select **Yes** to allow successful records to be created even if some records fail (commonly due to invalid field input). You can receive a mixed result, in which some operations may succeed while others fail. This allows for more flexibility in handling requests, but it also requires that you manage potential inconsistencies. Select **No** to roll back the entire batch if any record creation fails. This ensures that either all operations succeed or none do. If one creation fails, none of the records in the batch are created. Defaults to **No**. |
| Object Fields | Specify fields for the new object that you plan to create. |

## Output

The output datatree contains the IDs of the newly created objects.

| Field | Description |
| --- | --- |
| Batch IDs | A list of IDs for the successfully created objects. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/get-object-id-action.md
description: >-
  The Get object by ID action in the Microsoft Dynamics 365 connector lets you
  retrieve the details of a specific object using its ID.
---

# Microsoft Dynamics 365 - Get object by ID action

This action retrieves the details of a specific object in Microsoft Dynamics 365 using its ID.

## Input

| Field | Description |
| --- | --- |
| Object | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| Accounts ID | Dynamics ID of the record to retrieve. |

## Output

The output datatree contains the details of the specified object. Each field corresponds to the attributes of the object in Microsoft Dynamics 365.

| Field | Description |
| --- | --- |
| Object Fields | Fields of the retrieved object. |

---

---
url: >-
  https://docs.workato.com/en/connectors/dynamics-crm/actions/get-object-schema.md
description: >-
  The Get object schema action in the Microsoft Dynamics 365 connector retrieves
  an object's name and field schema to replicate to a database.
---

# Microsoft Dynamics 365 - Get object schema action

This action retrieves the name and schema of a specific object in Microsoft Dynamics 365. Use this action to retrieve a schema and replicate it to a database or data warehouse.

* * *

## How It Works

- [Basics](#basics)
- [Data typing](#data-typing)

### Basics

When the action runs, Workato requests the schema of the object you specify from the Microsoft Dynamics 365 API.

If the request is successful, the Microsoft Dynamics 365 API will respond with the object's `name`, `label`, and a list of `fields` that it contains.

For example: An `account` object contains `name`, `emailaddress`, and `alternate_address` fields. Click below to view the JSON response for this example object.

See example JSON response

```json
{
   "name":"account",
   "label":"Account",
   "fields":[
      {
         "name":"name",
         "label":"Name",
         "length":100,
         "scale":0,
         "precision":0,
         "original_type":"#Microsoft.Dynamics.365.StringAttributeMetadata",
         "mapped_type":"STRING",
         "custom":false
      },
      {
         "name":"emailaddress",
         "label":"Email address ",
         "length":100,
         "scale":0,
         "precision":0,
         "original_type":"#Microsoft.Dynamics.365.StringAttributeMetadata",
         "mapped_type":"STRING",
         "custom":false
      },
      {
         "name":"alternate_address",
         "label":"Alternate Address",
         "length":0,
         "precision":0,
         "scale":0,
         "original_type":"#Microsoft.Dynamics.365.PicklistAttributeMetadata",
         "mapped_type":"STRING",
         "custom":true,
         "fields":[
            {
               "name":"label",
               "label":"Label",
               "length":0,
               "scale":0,
               "precision":0,
               "original_type":null,
               "mapped_type":"STRING",
               "custom":false
            },
            {
               "name":"value",
               "label":"Internal value",
               "length":0,
               "scale":0,
               "precision":0,
               "original_type":null,
               "mapped_type":"INTEGER",
               "custom":false
            }
         ]
      }
   ]
}
```

### Data Typing

Every `field` object also contains `original_type` and `mapped_type` properties. These properties indicate the data type of the field in Microsoft Dynamics 365 and the data type it maps to in Workato. These properties determine how data is typed when loaded into a database.

For example:

```json
{
   "name":"budget_amount",
   "label":"Budget Amount",
   "length":1000,
   "scale":0,
   "precision":10000,
   "original_type":"#Microsoft.Dynamics.365.MoneyAttributeMetadata",
   "mapped_type":"DECIMAL",
   "custom":false
}
```

In this example, the `budget_amount` field is typed as `MoneyAttributeMetadata` in Microsoft Dynamics 365 and maps to `DECIMAL` in Workato.

Refer to the [Data type mapping section](#data-type-mapping) for more info.

* * *

## Input

| Field | Description |
| --- | --- |
| **Object** | The object to retrieve from Microsoft Dynamics 365. You can select from a list of available objects or enter the name of an object. **If entering the name of an object**, you may need to retrieve it from your app first.
> View steps for app In your Dynamics 365 app, navigate to **Settings (gear icon) > Advanced Settings**.; In the **Settings** menu, click **Customization > Customizations**.; Next, select **Customize the System**, then **Entities**.; In the navigation on the left side of the page, locate and select the entity.; In the **General** tab for the entity, locate the **Name** field.

 |

* * *

## Output

The **Output** of this recipe will be an object detailing the Microsoft Dynamics 365 object's schema. This object contains a list of **Field** objects that describe the object's fields.

- [Object schema](#object)
- [Fields schema](#fields)

To view an example JSON object, refer to the [Basics](#basics) section.

### Object

| Field | Description |
| --- | --- |
| **Name** | The name of the object. For example: `account` |
| **Label** | The display label of the object. For example: `Account` |
| **Custom** | If `true`, the object was created by a user. |
| **Fields** | A list of fields the object contains. Refer to the [Field object](#field-object) section to view the schema fields have. |

### Fields

Every field in the retrieved [object](#object) will contain the following fields:

| Field | Description |
| --- | --- |
| **Name** | The name of the field. For example: `emailaddress` |
| **Label** | The display label of the field. For example: `Email Address` |
| **Length** | The maximum number of characters the field can hold. This value will be `0` for `BOOLEAN` fields or fields without a limit. |
| **Scale** | The maximum number of digits to the right of the decimal point. This value will be `0` for non-numeric fields. |
| **Precision** | The maximum number of digits that the column can store, including numbers to the left and right of the decimal point. This value will be `0` for non-numeric fields. |
| **Original type** | The data type of the field in Microsoft Dynamics 365. For example: `StringAttributeMetadata` |
| **Mapped type** | The data type that `original_type` maps to in Workato. This type is used to determine the column's data type when it's loaded into a database. [Learn more](#data-type-mapping). |
| **Custom** | If `true`, this field was created by a user. |
| **Fields** | **Applicable only to fields with an `Original type` value of `BooleanAttributeMetadata`, `PicklistAttributeMetadata`, `StatusAttributeMetadata`, or `StateAttributeMetadata`.** When present, the `fields` property will contain two nested fields: `label` and `value`. These fields have the same schema as a top-level field. For example:
{
   \[...\],
   "fields":\[
      {
         "name":"label",
         "label":"Label",
         "length":0,
         "scale":0,
         "precision":0,
         "original\_type":null,
         "mapped\_type":"STRING",
         "custom":false
      },
      {
         "name":"value",
         "label":"Internal value",
         "length":0,
         "scale":0,
         "precision":0,
         "original\_type":null,
         "mapped\_type":"INTEGER",
         "custom":false
      }
   \]
}

**Note**: The `mapped_type` value for a nested field is dependent on the `name` of the nested field: `label` - This value will be `STRING`; `value` - If the parent field has an `Original type` value of `BooleanAttributeMetadata`, this value will be `BOOLEAN`. Otherwise, this value will be `INTEGER`. |

* * *

## Reference

- [Data type mapping](#data-type-mapping)

### Data Type Mapping

The following table details how Microsoft Dynamics 365 data types map to Workato data types.

The columns in this table are as follows:

- **Microsoft Dynamics 365 Data Type** - The field's `original_type` value
- **Workato Mapping Type** - The field's `mapped_type` value

For example: A field with a `original_type: BigIntAttributeMetadata` value maps to a `mapped_type: BIGINT` value.

| Microsoft Dynamics 365 Data Type | Workato Mapping Type |
| --- | --- |
| BigIntAttributeMetadata | BIGINT |
| BooleanAttributeMetadata | STRING |
| DateTimeAttributeMetadata | DATETIME\_TZ |
| DecimalAttributeMetadata | DECIMAL |
| DoubleAttributeMetadata | FLOAT |
| EntityNameAttributeMetadata | STRING |
| FileAttributeMetadata | STRING |
| ImageAttributeMetadata | STRING |
| IntegerAttributeMetadata | INTEGER |
| LookupAttributeMetadata | STRING |
| MemoAttributeMetadaMemoAttributeMetadatata | STRING |
| MoneyAttributeMetadata | DECIMAL |
| MultiSelectPicklistAttributeMetadata | STRING |
| PicklistAttributeMetadata | STRING |
| StateAttributeMetadata | STRING |
| StatusAttributeMetadata | STRING |
| StringAttributeMetadata | STRING |
| UniqueIdentifierAttributeMetadata | STRING |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/search-objects-action.md
description: >-
  The Search objects action in the Microsoft Dynamics 365 connector lets you
  retrieve a list of objects that match your specified search criteria.
---

# Microsoft Dynamics 365 - Search objects action (batch)

This action retrieves a list of objects in Microsoft Dynamics 365 that match the specified search criteria.

## Input

| Field | Description |
| --- | --- |
| Object name | Select a standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| Result list size | Number of records retrieved. Minimum is 1, maximum is 5000. Defaults to 200. |
| Output fields | Select the fields of the selected objects you plan to use in your recipe. |
| Filter condition | Condition to filter the records. Use OData $filter syntax. For example, `contains(name, 'sample')` and `revenue gt 1000000`. [Learn more about filters](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query-data-web-api#filter-results). |
| Order by | Specify the order in which items are returned. |
| Expand | Expand navigation properties in the related entity set. |
| Next page URL | Next page URL, returned by a previous call, to request the next page of results. |

## Output

The output datatree contains a list of objects that match the search criteria. Each object contains information, such as ID and other attributes.

| Field | Description |
| --- | --- |
| Records | A list of records that match the search criteria. |
| Next page URL | URL to fetch the next page of results. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/update-object-action.md
description: >-
  The Update object action in the Microsoft Dynamics 365 connector lets you
  update an existing record for a specified object using its ID.
---

# Microsoft Dynamics 365 - Update object action

This action updates an existing record for a specified object in Microsoft Dynamics 365 using its ID.

## Input

| Field | Description |
| --- | --- |
| Object | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| ID | Dynamics ID of the record to update. |
| Object Fields | Fields of the object that you plan to update. |

## Output

The output datatree contains the version number and details of the updated object. Each field corresponds to the attributes of the object in Microsoft Dynamics 365.

| Field | Description |
| --- | --- |
| Version number | Version number of the updated object. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/update-object-action-batch.md
description: >-
  The Update object batch action in the Microsoft Dynamics 365 connector lets
  you update multiple records for a specified object in a single batch.
---

# Microsoft Dynamics 365 - Update object batch action

This action updates multiple records for a specified object in Microsoft Dynamics 365 in a single batch.

> **BATCH FAILURE BEHAVIOR**
> 
> Microsoft Dynamics 365 fails the entire batch if any record update encounters an error when the **Allow partial batch create field** is set to **No**. None of the records update, even if some are valid.
> 
> Set the **Allow partial batch create field** to **Yes** to update all valid records and skip those that fail. Dynamics 365 then returns mixed results that show which records succeed and which fail.

## Input

| Field | Description |
| --- | --- |
| Object | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| Objects | List of objects to update. |
| Allow partial batch create | Select **Yes** to allow successful records to be updated even if some records fail (commonly due to invalid field input). You can receive a mixed result, in which some operations may succeed while others fail. This allows for more flexibility in handling requests, but it also requires that you manage potential inconsistencies. Select **No** to roll back the entire batch if any record update attempt fails. This ensures that either all operations succeed or none do. If one update attempt fails, none of the records are updated. Defaults to **No**. |
| ID | Dynamics ID of the records to update. |

## Output

The output datatree contains the IDs of the updated objects.

| Field | Description |
| --- | --- |
| Batch IDs | A list of IDs for the successfully updated objects. |

---
