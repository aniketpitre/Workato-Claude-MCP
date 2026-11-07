---
url: 'https://docs.workato.com/en/connectors/azure-devops.md'
description: >-
  The Azure DevOps connector lets you work with Azure DevOps projects, boards,
  builds, and pipelines in Workato.
---

# Azure DevOps

[Azure DevOps](https://azure.microsoft.com/en-us/services/devops/) provides version control, work item tracking, pipelines, and release management for software development teams. The Azure DevOps connector lets you work with Azure DevOps projects, boards, builds, and pipelines in Workato.

This connector supports the following objects:

- Project
- Board
- Board columns
- Build
- Build log
- Run
- Work item

## API version

The Azure DevOps connector uses the [Azure DevOps API v6 and later](https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/rest-api-versioning?view=azure-devops). Previous versions may be compatible, but Workato has not tested earlier versions.

## Install Azure DevOps from the community library

Complete the following steps to install the Azure DevOps connector from the [community library](https://www.workato.com/browse/connectors):

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

The Azure DevOps connector supports the following authentication types:

- [Authorization code grant](#auth-code-grant)
- [Personal access token](#pat-auth)
- [Service principal](#service-principal-auth)

### Authorization code grant authentication

You can use authorization code grant authentication to create an Azure DevOps connection in Workato. Use this method when you want recipes to run with a specific user's permissions, or when you want users to authorize Workato through a browser consent flow.

To use OAuth 2.0, you must first register an application and configure it to access Azure DevOps.

#### Azure DevOps setup

Complete the following steps to set up Azure DevOps for authorization code grant authentication:

1. Sign in to your [Azure portal](https://portal.azure.com) with an account that has permission to register applications in your Microsoft Entra tenant.
   
2. Go to **Microsoft Entra ID > App registrations**, then click **New registration**.
   
3. Enter a name for your application in the **Name** field.
   
4. Enter supported tenants that can use this application in the **Supported account types** field.
   
5. Select `Web` and enter `https://www.workato.com/oauth/callback` in the **Redirect URI** field.
   
6. Click **Register**.
   
7. Copy and save the **Application (client) ID** and the **Directory (tenant) ID** from the On the application's **Overview** page. You need these values to configure the Workato connection.
   
8. Select **Certificates & secrets > New client secret**. Enter a description and expiration, then click **Add**.
   
9. Copy and save the **client secret** for use in Workato. The secret is only displayed once.
   
10. Select **API permissions > Add a permission**.
    
11. Select **Azure DevOps > Delegated permissions**. Select the `user_impersonation` scope. Select additional scopes as needed for your Azure DevOps instance.
    
12. Click **Add permissions**. Click **Grant admin consent** if your tenant requires admin consent.
    

#### Connect to Azure DevOps with authorization code grant authentication

Complete the following steps to set up an authorization code grant authentication connection to Azure DevOps in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Azure DevOps` and select it as your app.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Authorization code grant authentication](/assets/auth-code-connection-setup.CZ89UeM_.png)_Set up Authorization code grant authentication in Azure DevOps_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **OAuth 2.0 grant type** drop-down menu to select **Authorization code**.
   
6. Enter your Azure DevOps organization name in the **Organization** field.
   
7. Enter your **API version**.
   
8. Enter the **Client ID**.
   
9. Enter the **Client secret**.
   
10. Enter any scopes from the client app in the **Scopes** field.
    
11. Click **Connect**.
    
12. Click **Authorize** to grant Workato access to Azure DevOps. After you authorize the application, Microsoft redirects you back to Workato and the connection becomes active.
    

### Personal access token grant authentication

You can use a personal access token (PAT) grant to authenticate an Azure DevOps connection in Workato. Use a PAT for development, testing, or recipes owned by a single user.

#### Azure DevOps setup

Complete the following steps to set up a personal access token in Azure DevOps:

1. Sign in to your Azure DevOps organization at `https://dev.azure.com/{your_organization}`.
   
2. Select **User settings (the user icon) > Personal access tokens**.
   
   ![User profile settings icon](/assets/azure-devops-user-settings.CVqp3kls.png)_User profile settings icon_
   
3. Click **New Token**.
   
4. Enter a name for the token in the **Name** field.
   
5. Enter the Azure DevOps organization the token applies to in the **Organization** field.
   
6. Enter the date the token expires in the **Expiration** field. Maximum is one year.
   
7. Enter the minimum scopes required for the recipes you plan to build in the **Scopes** field.
   
   Refer to [Azure DevOps scopes](https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/oauth#scopes) for more information about scopes.
   
8. Click **Create**.
   
9. Copy and save the token for use in Workato. The token is only displayed once.
   

#### Connect to Azure DevOps with a personal access token

Complete the following steps to set up a connection to Azure DevOps with a personal access token in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Azure DevOps` and select it as your app.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Personal access token](/assets/pat-connection-setup.C9pGephh.png)_Set up personal access token with Azure DevOps_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **OAuth 2.0 grant type** drop-down menu to select **Personal access token**.
   
6. Enter your Azure DevOps organization name in the **Organization** field. This is the value that appears in your Azure DevOps URL: `https://dev.azure.com/{organization}`.
   
7. Enter your **API version**.
   
8. Enter your **Username**.
   
9. Enter your **Personal access token**.
   
10. Click **Connect**.
    
11. Click **Authorize** to grant Workato access to Azure DevOps. After you authorize the application, Microsoft redirects you back to Workato and the connection becomes active.
    

### Service principal grant authentication

You can use a service principal OAuth 2.0 grant to create an Azure DevOps connection in Workato.

Service principals and managed identities authenticate to Azure DevOps as a non-human identity, using Microsoft Entra ID. Use this method for production workflows, scheduled jobs, or recipes that should run without a specific user's credentials.

> **REQUIRED PERMISSIONS**
> 
> Adding service principals or managed identities to an Azure DevOps organization requires Project Collection Administrator permissions.

#### Azure DevOps setup

Create an identity and client secret in Microsoft Entra ID for service principal grant authentication in Azure DevOps :

1. Create the identity in Microsoft Entra ID.
   
2. Go to **Microsoft Entra ID > App registrations > New registration**.
   
3. Enter a name for your application in the **Name field**.
   
4. Enter `tenant support` in the **Account types** field.
   
5. Enter a **Redirect URI**. Leave blank for service-to-service scenarios.
   
6. Go to **Certificates & secrets > New client secret**.
   
7. Copy and save the **Application (client) ID**, **Directory (tenant) ID**, and the secret **Value** for use in Workato.
   
8. Sign in to your Azure DevOps organization at `https://dev.azure.com/{your_organization}`.
   
9. Go to **Organization settings > Users**, then click **Add users**.
   
10. Enter the display name of the service principal in the **Users or service principals** field.
    
11. Enter the access level you plan to grant in the **Access level** field. Select **Basic** for full Azure DevOps functionality.
    
12. Add the projects the identity can access in the **Add to projects** field.
    
13. Select **Project Contributors**, or another group that grants the required permissions, in the **Azure DevOps groups** field.
    
14. Click **Add**.
    
15. Confirm that the identity appears in the **Users** list with the access level you assigned.
    

#### Connect to Azure DevOps with service principal grant authentication

Complete the following steps to set up a service principal grant connection to Azure DevOps in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Azure DevOps` and select it as your app.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Service principal grant authentication](/assets/service-principal-connection-setup.CbiX-4XN.png)_Set up service principal grant authentication in Workato_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Service principal**.
   
6. Enter your Azure DevOps organization name in the **Organization** field.
   
7. Enter your **API version**.
   
8. Enter the **Client ID**.
   
9. Enter the **Client secret**.
   
10. Enter the **Tenant ID**.
    
11. Click **Connect**.
    
12. Click **Authorize** to grant Workato access to Azure DevOps. After you authorize the application, Microsoft redirects you back to Workato and the connection becomes active.

---
