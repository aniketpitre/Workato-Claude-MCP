---
url: 'https://docs.workato.com/en/connectors/microsoft-dynamics-business-central.md'
description: >-
  The Microsoft Dynamics Business Central connector enables you to manage
  records, entities, and business data using the Business Central API v2.0.
---

# Microsoft Dynamics Business Central

[Microsoft Dynamics Business Central](https://dynamics.microsoft.com/en-us/business-central/overview/) is an enterprise resource planning (ERP) software solution used for managing finances, operations, sales, and customer service. It includes business management capabilities such as financial management, supply chain management, and project management.

## Prerequisites

Complete the following steps before establishing a Microsoft Dynamics Business Central connection in Workato:

- [Get your tenant ID](#get-your-tenant-id)
- [Get your environment name](#get-your-environment-name)
- [Register an application in the Azure portal](#register-an-application-in-azure-portal)
- [Get your client ID](#get-your-client-id)
- [Generate a client secret](#generate-a-client-secret): This is required for OAuth2 (Authorization code) authentication and optional for OAuth2 (Client credentials) authentication.

### Get your tenant ID

Complete the following steps to retrieve your tenant ID:

1. Sign in to the [Microsoft Azure portal](https://portal.azure.com/) using an account with administrator permissions.
   
2. Search for and select **Microsoft Entra ID**. Alternatively, you can select it from the menu.
   
3. Go to the **Basic information** section and locate the **Tenant ID**.
   
4. Copy the **Tenant ID**.
   

Alternatively, you can select **Properties** from the Microsoft Entra ID menu. The Tenant ID is listed as the **Directory ID**.

### Get your environment name

Complete the following steps to retrieve your environment name:

1. Sign in to [Microsoft Dynamics Business Central](https://businesscentral.dynamics.com/).
   
2. Go to **Admin Center**. The **Environments** section displays a list of available environments.
   
3. Copy the **Environment name** from the list of available environments.
   

### Register an application in the Azure portal

Complete the following steps to register an application in the Azure portal:

1. Sign in to the [Microsoft Azure portal](https://portal.azure.com/) using an account with administrator permissions.
   
2. Go to **Microsoft Entra ID > App registrations**.
   
3. Click **New registration**.
   
4. Enter a **Name** for your application and select the appropriate **Supported account types**.
   
5. Click **Register**.
   
6. Go to **API permissions** and click **Add a permission**.
   
7. Select **Dynamics 365 Business Central** and add the required permissions, such as `Financials.ReadWrite.All` or `Financials.Read.All`.
   
8. Click **Grant admin consent** to approve the permissions.
   

Refer to the [Register an application with the Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app) documentation for more information.

### Get your client ID

Complete the following steps to get your client ID:

1. In the Azure portal, go to **Microsoft Entra ID > App registrations** and select your application.
   
2. Go to the **Overview** page.
   
3. Copy the **Application (client) ID**. This is your Client ID.
   

### Generate a client secret

The client secret is required when using OAuth2 (Authorization code) authentication and optional for OAuth2 (Client credentials) authentication. Complete the following steps to generate a client secret:

1. In the Azure portal, go to **Microsoft Entra ID > App registrations** and select your application.
   
2. Go to **Certificates & secrets**.
   
3. Go to the **Client secrets** section and click **New client secret**.
   
4. Enter a **Description** and select an **Expiration period**, such as 190 days (6 months), 365 days(12 months), or 740 days (24 months).
   
5. Click **Add**.
   
6. Copy and save the client secret **Value** immediately. You can't view it later.
   

## How to connect to Microsoft Dynamics Business Central

Complete the following steps to connect Workato to Microsoft Dynamics Business Central:

1. Select your **Authentication** method. You can choose **OAuth2 (Client credentials)** or **OAuth2 (Authorization code)**.
   
2. Enter your **Tenant** ID. For example, `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`.
   
3. Enter your **Environment name**.
   
4. Enter your **Client ID** from your Azure application registration.
   
5. Enter your **Client secret** from your Azure application registration. This is required for Authorization code grant and optional for Client credentials authentication.
   
6. Optional. Enter your **Base URI** to use a custom base URI. Leave blank to use the default: `https://api.businesscentral.dynamics.com/v2.0/{environment}/api`.
   
7. Optional. Enter your **Company ID** to use a default Company ID for all actions and triggers that require it. You can override this value using the **Company ID** field in individual actions or triggers.
   
8. Click **Connect** to establish the connection.
   
   ![Business Central connection](/assets/connection.Df6oZgae.png)_Create a Microsoft Dynamics Business Central connection_

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-business-central/new-updated-record-trigger.md
description: >-
  Monitor for new or updated records in Microsoft Dynamics Business Central.
  Triggers when a record is created or updated.
---

# Microsoft Dynamics Business Central - New/updated record trigger

Use the **New/updated record** trigger to monitor Microsoft Dynamics Business Central for new or updated records. When a record is created or updated, the trigger activates and provides the complete record information. The trigger checks for new events every five minutes.

## Input

| Input field | Description |
| --- | --- |
| Entity name | Select the entity type to monitor from the drop-down menu. Examples include Item, Customer, Vendor, Sales Order, Purchase Order, and more. |
| Company ID | Enter a Company ID to monitor records from. If provided, this overrides the Company ID from the connection settings. Leave blank to use the Company ID specified in the connection. |
| Filter criteria | Additional OData filter expression to further filter the records. For example, `totalTaxAmount lt 96.5`. Refer to the [OData Filter](https://docs.microsoft.com/en-us/odata/concepts/queryoptions-overview#filter) documentation for filter syntax help. Don't include `systemModifiedAt` or `lastModifiedDateTime` as part of the filter, because these are automatically handled by the trigger. |
| Expand | Specify additional related objects to be returned in the output. For example, enter `purchaseOrderLines` to include purchase order lines in the results. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up trigger events from this specified date and time. Leave empty to get records created or updated one hour ago. |

## Output

| Output field | Description |
| --- | --- |
| Record data | The complete record data that was created or updated, including all fields returned by Business Central. The structure depends on the entity type selected. |
| ETag | The entity tag (ETag) for the record. |
| ID | The unique identifier of the record. |
| Last modified date time | The date and time when the record was last modified. For Company entities, this field is named **System modified at**. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-business-central/new-updated-record-batch-trigger.md
description: >-
  Monitor for new or updated records in Microsoft Dynamics Business Central,
  returning results in batches. Triggers when records are created or updated.
---

# Microsoft Dynamics Business Central - New/updated record (batch) trigger

Use the **New/updated record (batch)** trigger to monitor Microsoft Dynamics Business Central for new or updated records and return results in batches. When records are created or updated, the trigger activates with a batch of records. The trigger checks for new events every five minutes.

## Input

| Input field | Description |
| --- | --- |
| Entity name | Select the entity type to monitor from the drop-down menu. Examples include Item, Customer, Vendor, Sales Order, Purchase Order, and more. |
| Batch size | The number of records to return per batch. Defaults to 30 if left blank. Maximum batch size is 100. |
| Company ID | Enter the Company ID to monitor records from. If provided, this overrides the Company ID from the connection settings. Leave blank to use the Company ID specified in the connection. |
| Filter criteria | Additional OData filter expression to further filter the records. For example, `totalTaxAmount lt 96.5`. Refer to the [OData Filter](https://docs.microsoft.com/en-us/odata/concepts/queryoptions-overview#filter) documentation for filter syntax help. Don't include `systemModifiedAt` or `lastModifiedDateTime` as part of the filter, because these are automatically handled by the trigger. |
| Expand | Specify additional related objects to be returned in the output. For example, enter `purchaseOrderLines` to include purchase order lines in the results. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up trigger events from this specified date and time. Leave empty to get records created or updated one hour ago. |

## Output

| Output field | Description |
| --- | --- |
| Records | An array of records that were created or updated. Each record includes the complete record data with all fields returned by Business Central, the entity tag (ETag) for the record, the unique identifier (ID) of the record, and the date and time when the record was last modified. For Company entities, the last modified field is named **System modified at**. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-business-central/create-record-action.md
description: >-
  Create a new record (for example, Item, Customer, Vendor) in Microsoft
  Dynamics Business Central.
---

# Microsoft Dynamics Business Central - Create record action

Use the **Create record** action to create a new record in Microsoft Dynamics Business Central. This action supports creating various entity types such as Items, Customers, Vendors, Sales Orders, Purchase Orders, and other business entities available in your Business Central instance.

## Input

| Input field | Description |
| --- | --- |
| Entity name | Select the entity type to create from the drop-down menu. Examples include Item, Customer, Vendor, Sales Order, Purchase Order, and more. |
| Company ID | Enter a Company ID to create the record in a specific company. If provided, this overrides the Company ID from the connection settings. Leave blank to use the Company ID specified in the connection. |
| Record fields | Provide the data for creating the record. The available fields depend on the selected entity type and are dynamically generated based on your Business Central instance's metadata. |
| Display name (Record fields) | The display name of the record. |
| Number (Record fields) | The unique number identifier. |
| Type (Record fields) | The type or category of the record. |
| Status (Record fields) | The status of the record. |

## Output

| Output field | Description |
| --- | --- |
| Record data | The complete record data that was created, including all fields returned by Business Central. The structure depends on the entity type selected. |
| ETag | The entity tag (ETag) for the created record. Use this ETag when updating the record to ensure data consistency. |
| ID | The unique identifier of the created record. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-business-central/get-record-details-action.md
description: >-
  Retrieve the details of a specific record through its ID in Microsoft Dynamics
  Business Central.
---

# Microsoft Dynamics Business Central - Get record details by ID action

Use the **Get record details by ID** action to retrieve the complete details of a specific record in Microsoft Dynamics Business Central using its unique identifier. This action supports retrieving various entity types such as Items, Customers, Vendors, Sales Orders, Purchase Orders, and other business entities.

## Input

| Input field | Description |
| --- | --- |
| Entity name | Select the entity type to retrieve from the drop-down menu. Examples include Item, Customer, Vendor, Sales Order, Purchase Order, and more. |
| ID | The unique identifier of the record to retrieve. |
| Company ID | Enter the Company ID where the record exists. If provided, this overrides the Company ID from the connection settings. Leave blank to use the Company ID specified in the connection. |
| Journal ID | The unique identifier of the journal that contains the journal line. Required for Journal Line entity. |

## Output

| Output field | Description |
| --- | --- |
| Record data | The complete record data, including all fields returned by Business Central. The structure depends on the entity type selected and includes all properties defined in your Business Central instance. |
| ETag | The entity tag (ETag) for the record. Use this ETag when updating the record to ensure data consistency. |
| ID | The unique identifier of the retrieved record. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-business-central/list-records-action.md
description: >-
  Retrieve a list of records for a specific entity type in Microsoft Dynamics
  Business Central.
---

# Microsoft Dynamics Business Central - List records action

Use the **List records** action to retrieve a list of records for a specific entity type in Microsoft Dynamics Business Central. This action returns all available records for the selected entity type, such as Items, Customers, Vendors, Sales Orders, Purchase Orders, Companies, or Environments.

## Input

| Input field | Description |
| --- | --- |
| Entity name | Select the entity type to list from the drop-down menu. Examples include Item, Customer, Vendor, Sales Order, Purchase Order, Company, Environment, and more. |
| Company ID | Enter the Company ID to list records from. If provided, this overrides the Company ID from the connection settings. Leave blank to use the Company ID specified in the connection. |

## Output

| Output field | Description |
| --- | --- |
| Objects | An array of records for the selected entity type. Each record includes all entity-specific fields as defined in your Business Central instance, the entity tag (ETag) for each record for most entity types, and the unique identifier (ID) of each record. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-business-central/search-records-action.md
description: >-
  Search for records matching specific criteria using OData query options in
  Microsoft Dynamics Business Central.
---

# Microsoft Dynamics Business Central - Search records action

Use the **Search records** action to search for records in Microsoft Dynamics Business Central that match your specified criteria. This action uses OData query options to filter, search, and sort results. You must provide at least one search criteria (Search query or Filter criteria).

## Input

| Input field | Description |
| --- | --- |
| Entity name | Select the entity type to search from the drop-down menu. Examples include Item, Customer, Vendor, Sales Order, Purchase Order, Environment, and more. |
| Search query | A free-text search expression using OData `$search` syntax. The search query allows clients to request entities matching a free-text search expression. Refer to the [OData Search](https://docs.microsoft.com/en-us/odata/concepts/queryoptions-overview#search) documentation for syntax format. |
| Filter criteria | An OData filter expression to filter records. For example, `totalTaxAmount lt 96.5`. Refer to the [OData Filter](https://docs.microsoft.com/en-us/odata/concepts/queryoptions-overview#filter) documentation for filter syntax help. |
| Expand | Specify additional related objects to be returned in the output. For example, enter `purchaseOrderLines` to include purchase order lines in the results. |
| Order by | Sort the results by field in ascending or descending order. For example, `displayName asc` or `displayName desc`. |
| Limit | The maximum number of results to display per page. |
| Offset | Skip the number of records before starting to return results from the query. |
| Company ID | Enter a Company ID to search records in a specific company. If provided, this overrides the Company ID from the connection settings. Leave blank to use the Company ID specified in the connection. |

> **SEARCH CRITERIA REQUIRED**
> 
> You must provide at least one of the following to use this action:
> 
> - **Search query**
> - **Filter criteria**

## Output

| Output field | Description |
| --- | --- |
| Objects | An array of records that match your search criteria. Each record includes all entity-specific fields as defined in your Business Central instance, the entity tag (ETag) for each record, and the unique identifier (ID) of each record. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-business-central/update-record-action.md
description: Update an existing record in Microsoft Dynamics Business Central.
---

# Microsoft Dynamics Business Central - Update record action

Use the **Update record** action to update an existing record in Microsoft Dynamics Business Central. This action supports updating various entity types such as Items, Customers, Vendors, Sales Orders, Purchase Orders, and other business entities available in your Business Central instance.

## Input

| Input field | Description |
| --- | --- |
| Entity name | Select the entity type to update from the drop-down menu. Examples include Item, Customer, Vendor, Sales Order, Purchase Order, and more. |
| ID | The unique identifier of the record to update. |
| ETag | The entity tag (ETag) of the record to update. The ETag ensures data consistency and prevents overwriting changes made by other users. |
| Company ID | Enter the Company ID where the record exists. If provided, this overrides the Company ID from the connection settings. Leave blank to use the Company ID specified in the connection. |
| Record fields | Provide the fields to update. Only include the fields you plan to change. The available fields depend on the selected entity type and are dynamically generated based on your Business Central instance's metadata. |

## Output

| Output field | Description |
| --- | --- |
| Record data | The complete updated record data, including all fields returned by Business Central. The structure depends on the entity type selected. |
| ETag | The new entity tag (ETag) for the updated record. Use this ETag for subsequent updates to ensure data consistency. |
| ID | The unique identifier of the updated record. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-finance-and-operations/create-record-action.md
description: >-
  The Create record action in the Microsoft Dynamics Finance and Operations
  connector lets you create a record for a selected object in your environment.
---

# Microsoft Dynamics Finance and Operations - Create record action

The **Create record** action enables you to create a record in Microsoft Dynamics Finance and Operations (MSDFO).

![Create record action](/assets/create-record-action.CHJ4vVo5.png)_Create record action_

## Input

| Input Field | Description |
| --- | --- |
| Object | Specify the object you plan to create. Fields load dynamically based on the object you select. |

## Output

The output fields are determined by the object you select in the input. Map the relevant datapill from the data tree for downstream steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-finance-and-operations/create-record-in-batch-action.md
description: >-
  The Create records in batch action in the Microsoft Dynamics Finance and
  Operations connector lets you create multiple records of a selected object at
  once.
---

# Microsoft Dynamics Finance and Operations - Create records in batch action

The **Create records in batch** action enables you to create records in batch in Microsoft Dynamics Finance and Operations (MSDFO).

![Create record in batch action](/assets/create-record-batch-action.DR4CXcJa.png)_Create record in batch action_

## Input

| Input Field | Description |
| --- | --- |
| Object | Specify the object you plan to create. Fields load dynamically based on the object you select. |

## Output

The output fields are determined by the object you select in the input. Map the relevant datapill from the data tree for downstream steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-finance-and-operations/get-record-action.md
description: >-
  The Get record action in the Microsoft Dynamics Finance and Operations
  connector lets you retrieve a single record for a selected object.
---

# Microsoft Dynamics Finance and Operations - Get record action

The **Get record** action enables you to retrieve a record in Microsoft Dynamics Finance and Operations (MSDFO).

![Get record action](/assets/get-record-action._N5ZkI5l.png)_Get record action_

## Input

| Input Field | Description |
| --- | --- |
| Object | Specify the object you plan to create. Fields load dynamically based on the object you select. |

## Output

The output fields are determined by the object you select in the input. Map the relevant datapill from the data tree for downstream steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-finance-and-operations/search-records-action.md
description: >-
  The Search records action in the Microsoft Dynamics Finance and Operations
  connector returns records that match your search criteria, filters, and
  sorting.
---

# Microsoft Dynamics Finance and Operations - Search records action

The **Search records** action enables you to return the list of the records that match the search criteria in Microsoft Dynamics Finance and Operations (MSDFO)

![Search records action](/assets/search-records-action.ZGlj2IoI.png)_Search records action_

## Input

| Input Field | Description |
| --- | --- |
| Object | Specify the object you plan to search. |
| Entity fields | Select the fields that you require in the output data tree from the multi-select drop-down. All fields are returned if left blank. |
| Search query | Provide free-text expressions for searching the entities. [Learn more about Search expressions](https://docs.oasis-open.org/odata/odata/v4.0/errata02/os/complete/part2-url-conventions/odata-v4.0-errata02-os-part2-url-conventions-complete.html#_Toc406398092). |
| Filter criteria | Specify conditions that data must meet to be included in query results. [Learn more about Filters](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/odata?toc=%2Ffin-and-ops%2Ftoc.json). |
| Expand(related resources) | Specify the related resources that should be included along with the retrieved resources. |
| Order by | Specify the sorting order of the retrieved data. For example, `asc` (ascending) or `desc` (descending). |
| No. of objects returned in the query result | Specify the number of items to include in the result. |
| Skip items | Specify how many items from the beginning of the collection should be ignored and not included. |

## Output

The output fields are determined by the object you select in the input. Map the relevant datapill from the data tree for downstream steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-finance-and-operations/update-record-action.md
description: >-
  The Update record action in the Microsoft Dynamics Finance and Operations
  connector lets you update an existing record for a selected object.
---

# Microsoft Dynamics Finance and Operations - Update record action

The **Update record** action enables you to update the record in Microsoft Dynamics Finance and Operations (MSDFO).

![Update record action](/assets/update-record-action.-qy87_a7.png)_Update record action_

## Input

| Input Field | Description |
| --- | --- |
| Object | Specify the object you plan to create. Fields load dynamically based on object you select. |

## Output

The output fields are determined by the object you select in the input. Map the relevant datapill from the data tree for downstream steps.

---
