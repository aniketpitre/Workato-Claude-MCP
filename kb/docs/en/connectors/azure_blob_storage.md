---
url: 'https://docs.workato.com/en/connectors/azure_blob_storage.md'
description: >-
  Azure Blob Storage enables you to create data lakes for analytics and provides
  storage for building powerful cloud-native and mobile apps.
---

# Azure Blob Storage

[Azure Blob Storage](https://azure.microsoft.com/en-gb/services/storage/blobs/) enables you to create data lakes for analytics and provides storage for building powerful cloud-native and mobile apps.

Azure Blob Storage enables you to store large amounts of unstructured object data. All Azure Blob Storage data is stored within containers. You must create a storage container before you can upload data with your Workato connection.

> **CONTAINERS ARE REQUIRED**
> 
> Log streams stop and Workato sends a notification email if you delete a container.

Workato's Azure Blob Storage connector allows you to automate cloud storage tasks and build data pipelines that automatically pull or push data to Azure Blob Storage from various apps.

## API version

The Azure Blob Storage connector uses the [Azure Blob Storage REST API](https://docs.microsoft.com/en-us/rest/api/storageservices/blob-service-rest-api).

> **MICROSOFT MFA REQUIREMENTS**
> 
> Starting October 1, 2025, Microsoft will begin to enforce [multi-factor authentication (MFA)](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication?tabs=dotnet) for accounts that sign in to [Azure Resource Manager API](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/control-plane-and-data-plane#control-plane) endpoints to perform Create, Update, or Delete operations.
> 
> These endpoints are used in the Azure Blob Storage connector to create and manage webhook subscriptions through `https://management.azure.com/subscriptions`.
> 
> This change affects the following triggers:
> 
> - [New blob trigger (real-time)](/en/connectors/azure_blob_storage/new-blob-trigger)
> - [New event trigger (real-time)](/en/connectors/azure_blob_storage/new-event-trigger)
> 
> Choose one of the following options to maintain uninterrupted service:
> 
> **Option 1: Enable MFA and re-authenticate**
> 
> 1. Set up MFA for your Azure organization following [Microsoft's MFA setup guide](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/set-up-multi-factor-authentication?view=o365-worldwide).
>    
> 2. Reconnect your Azure Blob Storage connection in Workato.
>    
> 3. Complete the OAuth flow with MFA when prompted.
>    
> 4. Test the recipe to ensure it works with the connection.
>    
> 
> **Option 2: Migrate to Client Credentials authentication**
> 
> Configure a [Client Credentials Grant connection](#create-a-client-credentials-grant), which uses a service principal and is exempt from MFA enforcement.

## How to connect to Azure Blob Storage on Workato

There are two ways to authenticate to Azure Blob Storage:

- Using an [Authorization Code Grant](#create-an-auth-code-grant-isu)
- Using a [Client Credentials Grant](#create-a-client-credentials-grant)

### Create an Authorization Code Grant and Integration System User

Use an Authorization Code Grant connection to allow Workato to perform actions on behalf of a user by leveraging Integration System User (ISU) permissions. This setup is required to use Azure Blob Storage's capabilities, including the event webhook trigger.

> **NETWORK ACCESS REQUIRED**
> 
> Your Azure Blob Storage account must allow network access from Workato. You can enable public access from all networks or restrict access to specific IP addresses. If you restrict access, you must add [Workato IP addresses](/en/security/ip-allowlists#traffic-from-workato) to your allowlist.

> **ISU ACCOUNT ACCESS**
> 
> The ISU must have access solely to the storage account specified in your Workato connection.

Complete the following steps to create an ISU in your Microsoft Entra ID account:

1. Go to **Microsoft Entra ID**.
   
   ![Go to Microsoft Entra ID](/assets/nav-microsoft-entra.BLQ9IIbI.png)_Access Microsoft Entra ID from your Azure portal_
   
2. Select **Add > User > Create new user**.
   
   ![Select new user](/assets/nav-new-user-2.BHIlqnAr.png)_Create a new user_
   
3. Enter the **Identity** details for the ISU, such as the **User principal name**, **Display name**, and **Password**.
   
   ![Fill in new user details](/assets/nav-user-details.B8EsQnj_.png)_Provide details for the new user._
   
4. Select **Review + create > Create** to create your ISU.
   

#### Configure the ISU

Complete the following steps to configure your Workato connection through the Azure portal, ensuring that your ISU has the appropriate permissions and scopes:

1. In your Azure portal, go to **Storage accounts**.
   
   ![Go to storage accounts](/assets/nav-storage-account-2.Cz7z0nut.png)_Navigate to **Storage accounts** from your Azure portal_
   
2. Select your **Storage account**.
   
   ![Go to specific Storage Account](/assets/nav-storage-name-2.RXV3WBxE.png)_Specify the **Storage account** to grant access to Workato_
   
3. Select the resource group within your Azure Blob Storage account.
   
   ![Navigate to specific Storage Account](/assets/nav-resource-group.BPleRzad.png)_Navigate to the resource group_
   
4. Go to **Access Control (IAM)** within the resource group.
   
   ![Navigate to Access Control](/assets/nav-iam-2.CRLmosh7.png)_Navigate to **Access Control (IAM)**_
   
5. Click **Add > Add role assignment** to begin assigning roles to the ISU.
   
   ![Select Add Role Assignment](/assets/nav-add-role-assignment-2.p9W6J0nZ.png)_Add a role assignment to the ISU_
   
6. Provision the required roles for the ISU:
   
   - **Storage Blob Data Contributor**: Grants full read and write access to Azure Blob Storage.
     
   - **Storage Blob Data Reader**: Provides read-only access to Azure Blob Storage.
     
   - **EventGrid Event Subscription Contributor**: Enables the ISU to establish and manage event subscriptions within Azure Blob Storage. This is required for using the new event webhook trigger.
     
7. Configure network access for your storage account
   
   1. Go to your Storage account in the Azure portal.
      
   2. Go to **Security + networking > Networking**.
      
   3. Click **Manage** in the **Public network access** section.
      
   4. Ensure **Public network access** is set to **Enable**.
      
   5. Select one of the following options under **Public network access scope**:
      
      - **Enable from all networks**: Allows access from any network
      - **Enable from selected networks**: Restricts access to specific networks. If you select this option, add the [Workato IP addresses](/en/security/ip-allowlists#traffic-from-workato) in the **IPv4 Addresses** section
   6. Click **Save**.
      
   
8. Verify that the **Storage Data Contributor** role is active for write access and the container access level is set to public.
   

### Create a Client Credentials Grant

You can use a Client Credentials Grant to establish a connection with Azure Blob Storage. Use this grant type for:

- Working with tenant-specific connection account types, which are the only supported account type for this grant.
- Service-to-service authentication, where you access Azure with managed identities.

> **NETWORK ACCESS REQUIRED**
> 
> Your Azure Blob Storage account must allow network access from Workato. You can enable public access from all networks or restrict access to specific IP addresses. If you restrict access, you must add [Workato IP addresses](/en/security/ip-allowlists#traffic-from-workato) to your allowlist.

Complete the following steps to set up a Client Credentials Grant connection in Azure Blob Storage:

1. Go to **App registrations** in your Azure portal.
   
   ![Navigate to App registrations](/assets/nav-app-registration.CTFsJtMV.png)_Go to **App registrations** in your Azure portal_
   
2. Select **New registration**.
   
3. Enter the **Name** of the application you plan to register.
   
   ![Register an application](/assets/register-app.BftVj5fd.png)_Register an application_
   
4. Select the **Supported account types** that can use the application and access the API.
   
5. Select **Web** as the platform and enter `https://www.workato.com/oauth/callback` in the **Redirect URI** field.
   
6. Click **Register** to create the application and view the **Overview** page.
   
7. Record the **Client ID** and **Tenant ID** for connection setup in Workato.
   
   ![Record IDs](/assets/record-ids.CPWtV8bi.png)_Record IDs_
   
8. Go to **Manage > API permissions**.
   
9. Select **Add a permission**.
   
   ![Add a permission](/assets/add-a-permission.BtwxmH_r.png)_Add a permission_
   
10. Select permissions for **Azure Storage** and **Azure Service Management** on the **Request API permissions** page, including **user\_impersonation**.
    
11. Click **Add permissions** to grant the permissions.
    
    ![Grant perrmisions](/assets/grant-permissions.BzqU0QHA.png)_Grant permissions_
    
12. Go to **Certificates & secrets > Client secrets**.
    
    ![Navigate to Client secrets](/assets/generate-secret.BJ2oIzm6.png)_Navigate to Client secrets_
    
13. Generate a **New client secret** and securely record its **Value**.
    
    ![Generate a Client secret](/assets/client-secrets.pHjFGyxC.png)_Generate a client secrets_
    
14. Assign required roles to the application
    
    You must assign the **Storage Blob Data Contributor** and **EventGrid Event Subscription Contributor** roles to the application. These roles enable full functionality with Azure Blob Storage actions, triggers, and the new event webhook trigger.
    
    1. Go to your **Storage account** in the Azure portal.
       
    2. Go to the resource group.
       
    3. Select **Access Control (IAM)**.
       
    4. Click **Add > Add role assignment**.
       
    5. Search for and select **Storage Blob Data Contributor**.
       
    6. Click **Next**.
       
    7. Select **User, group, or service principal**.
       
    8. Click **Select members** and search for your registered application by name.
       
    9. Select your application and click **Select**.
       
    10. Click **Review + assign** to complete the role assignment.
        
    11. Repeat steps 4-10 to assign the **EventGrid Event Subscription Contributor** role.
        
    
15. Configure network access for your storage account
    
    1. Go to your Storage account in the Azure portal.
       
    2. Go to **Security + networking > Networking**.
       
    3. Click **Manage** in the **Public network access** section.
       
    4. Ensure **Public network access** is set to **Enable**.
       
    5. Select one of the following options under **Public network access scope**:
       
       - **Enable from all networks**: Allows access from any network
       - **Enable from selected networks**: Restricts access to specific networks. If you select this option, add the [Workato IP addresses](/en/security/ip-allowlists#traffic-from-workato) in the **IPv4 Addresses** section
    6. Click **Save**.
       
    
16. Use the recorded **Client ID**, **Tenant ID**, and **Client secret** to establish a Client Credentials Grant connection.
    

Continue to set up your Azure Blob Storage connection in Workato.

### Complete setup in Workato

Complete the following steps to connect to Azure Blob Storage in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select the `Azure Blob Storage` as your connection on the **New connection** page.
   
3. Enter a **Connection name** that uniquely identifies the connection.
   
4. Select the project where you plan to store the connection from the **Location** drop-down menu.
   
5. Enter the name of your **Storage account** from Azure Blob Storage.
   
6. Select the **Connection account type**:
   
   - **Common**: Supports personal, enterprise, and multi-tenant accounts that are not tenant-specific.
     
   - **Organization**: Supports multi-tenant enterprise accounts.
     
   - **Tenant-specific**: Requires you to provide the **Tenant ID** or **Domain**.
     
   
   The default is the **Common** type.
   
7. Go to **Advanced settings** to manage additional configurations.
   
8. **Authorization Code Grant**
   
   For an Authorization Code Grant connection:
   
   - Add necessary scopes in **OAuth 2.0 authorization code scopes**, including **Management** to create dynamic webhooks through the EventGrid API.
   - If left blank, the **Offline\_access**, **Storage**, and **Management** scopes are added.
   
   **Client Credentials Grant**
   
   For a Client Credentials Grant connection:
   
   - Add necessary scopes in **OAuth 2.0 client credentials scopes**, including **Management** to create dynamic webhooks through the EventGrid API.
   - Ensure that the specified scopes are also defined in your Azure app registration.
   - If left blank, the **Storage** and **Management** scopes are added.
   
9. Enter the **Client ID** from your Azure portal.
   
10. Enter the **Client secret** from **Certificates & secrets** in the Azure portal.
    
11. Optional. Enter an **Access key** for pre-signed URL functionality.
    
12. Click **Sign in with Microsoft**.
    
13. Authorize the necessary permissions when prompted to complete the connection setup.

---
