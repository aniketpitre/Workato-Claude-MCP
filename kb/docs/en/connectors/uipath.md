---
url: 'https://docs.workato.com/en/connectors/uipath.md'
description: >-
  Connect Workato to UiPath to automate RPA workflows, manage robots, and
  orchestrate processes across your enterprise.
---

# UiPath

[UiPath](https://www.uipath.com/) combines core Robotic Process Automation (RPA) capabilities with tools for process discovery and analytics, making it easy to automate thousands of workflows across various applications. With UiPath, companies can easily build, manage, and run robots that emulate human interactions with digital systems.

## Install UiPath from the community library

Complete the following steps to install the UiPath connector from the [community library](https://www.workato.com/browse/connectors):

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

The UiPath connector supports the following authentication types:

- [Personal access token](#personal-access-token)
- [On-premise](#on-premise)
- [OAuth 2.0 (Authorization code)](#oauth-2-0-authorization-code)
- [OAuth 2.0 (Client credentials)](#oauth-2-0-client-credentials)

### Personal access token authentication

Use personal access token authentication to connect to UiPath Automation Cloud using a token scoped to specific resources.

#### Retrieve the account and tenant logical names

Complete the following steps to retrieve the account and tenant logical names:

1. Sign in to UiPath Automation Cloud.
   
2. Copy the part of the URL that appears after `https://cloud.uipath.com/` or `https://platform.uipath.com/`. This is the account logical name.
   
3. Go to the **Services** tab and locate your Orchestrator service.
   
4. Click the three dots next to the service and select **API Access**.
   
5. Copy the tenant logical name.
   
   Alternatively, you can find both names directly in the Orchestrator URL. For example, in `https://cloud.uipath.com/yourSite/yourTenant`:
   
   - The account logical name is `yourSite`
   - The tenant logical name is `yourTenant`

#### Generate the client ID and secret

Complete the following steps to generate the client ID and secret:

1. Go to **Tenant > Machines**.
   
2. Create a machine template or a standard machine.
   
3. Configure the required fields and click **Provision** to create the machine object.
   
4. Copy the client ID and client secret.
   

Refer to the [UiPath documentation](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/robot-authentication-with-client-credentials#generating-authorization-credentials) for more information.

#### Generate a personal access token

Complete the following steps to generate the personal access token:

1. Click the user icon in the top-right corner of UiPath Automation Cloud and select **Preferences**.
   
2. Go to **Personal Access Token** and click **Create token**.
   
3. Enter a name for the token and set an expiration date.
   
4. Click **Add scopes**, select a **Resource**, and select scopes to request for your connection.
   
5. Click **Save** to generate the token.
   
6. Copy the token immediately, as it's only displayed once.
   

Refer to the UiPath documentation for more information on generating a [personal access token](https://docs.uipath.com/automation-cloud/automation-cloud/latest/api-guide/personal-access-tokens#generating-a-token).

#### Connect to UiPath using personal access token

Complete the following steps to set up a personal access token connection to UiPath in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `UiPath` and select it as your app.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![UiPath Personal access token](/assets/personal-access-token.B-Cy0r0I.png)_UiPath Personal access token_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to specify whether the connection is a cloud or on-prem connection.
   
6. Use the **Authentication type** drop-down menu to select **Personal Access Token**.
   
7. Enter the fully qualified folder name in the **Folder** field. For example, `Shared`. You can view available folders in UiPath under Orchestrator.
   
8. Enter your [account logical name](#account-tenant-logical-names) in the **Account logical name** field.
   
9. Enter your [tenant logical name](#account-tenant-logical-names) in the **Tenant logical name** field. For example, `DefaultTenant`.
   
10. Enter the [client ID](#pat-client-id-secret) from your machine configuration in the **Client ID** field.
    
11. Enter your [personal access token](#pat-retrieve) in the **Personal access token** field.
    
12. Click **Connect**.
    

### On-premise authentication

Use on-premise authentication to connect to a self-hosted UiPath Orchestrator instance using a tenant username and password.

#### Retrieve the orchestration URL

Complete the following steps to retrieve the orchestration URL:

1. Sign in to your UiPath Orchestrator instance, either cloud-based or on-premises.
   
2. Navigate to the **Management** tab and click **Machines**.
   
3. Locate the machine object associated with your robot or UiPath Studio.
   
4. Click the machine name to view its details.
   
5. Copy the orchestrator URL. This is typically the base URL found before `/orchestrator_` in the browser address bar.
   
6. Copy the machine key displayed in the machine details section.
   
7. Use the copied orchestrator URL and machine key to configure UiPath Assistant or Studio and connect to Orchestrator.
   

#### Create a tenant

Complete the following steps to create a tenant:

1. Sign in to the Orchestrator host portal as a system administrator.
   
2. Go to the **Tenants** page and click **Add Tenant**.
   
3. Enter the **Tenant Name** and **Password** in the **Provision Tenant** dialog, then click **Confirm Password**.
   
4. Optional. Fill in the **First Name**, **Last Name**, and **Email Address** fields.
   
5. Click **Provision** to create the tenant and tenant admin.
   

The new tenant now appears on the **Tenants** page. Refer to the UiPath documentation for more information on [creating a tenant](https://docs.uipath.com/orchestrator/standalone/2023.4/user-guide/managing-tenants#creating-a-tenant).

#### Connect to UiPath using on-premise authentication

Complete the following steps to set up an on-premise connection to UiPath in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `UiPath` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![UiPath On-premise](/assets/on-prem.BBotT_ov.png)_UiPath On-premise_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to specify whether the connection is a cloud or on-prem connection.
   
6. Use the **Authentication type** drop-down menu to select **On Premise**.
   
7. Enter the fully qualified folder name in the **Folder** field. For example, `Shared`. You can view available folders in UiPath under Orchestrator.
   
8. Enter the [orchestration URL](#orchestration-url) in the **Orchestration URL** field.
   
9. Enter the [tenant](#tenant-credentials) to connect to in the **Tenant** field.
   
10. Enter the user name or email address associated with the tenant in the **User** field.
    
11. Enter the password associated with the tenant in the **Password** field.
    
12. Click **Connect**.
    

### OAuth 2.0 (Authorization code) authentication

Use OAuth 2.0 authorization code authentication for user-delegated access to UiPath. This method requires **User scopes** when registering your external application in UiPath.

#### Register an external application in UiPath

Registering an external application generates an **App ID** and **App Secret** in UiPath, which correspond to the **Client ID** and **Client secret** fields in Workato.

Complete the following steps to register an external application:

1. Sign in to UiPath Automation Cloud and go to **Admin**.
   
2. Select **External Applications**.
   
3. Click **\+ Add Application** and enter a name for your application.
   
4. Select **Confidential application** as the **Application type**.
   
5. Click **Add scopes**, select **Orchestrator API Access** as the resource, and select the **User scopes** required for your integration.
   
   > **SELECT USER SCOPES ONLY**
   > 
   > Select **User scopes** only. Selecting **Application scopes** instead results in a `400 Bad Request` error when connecting.
   
6. Enter `https://www.workato.com/oauth/callback` in the **Redirect URL** field.
   
7. Click **Add** to register the application.
   
8. Copy the **App ID** and **App Secret**. These values correspond to the **Client ID** and **Client secret** fields in Workato.
   

#### Retrieve the account and tenant logical names

Retrieve your account and tenant logical names following the steps in the [Personal access token](#account-tenant-logical-names) section.

#### Connect to UiPath using OAuth 2.0 (Authorization code)

Complete the following steps to set up an OAuth 2.0 (Authorization code) connection to UiPath in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `UiPath` and select it as your app.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![UiPath OAuth 2.0](/assets/oauth2-auth-code.CnCeBzj1.png)_UiPath OAuth 2.0_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to specify whether the connection is a cloud or on-prem connection.
   
6. Use the **Authentication type** drop-down menu to select **OAuth2 (Authorization Code)**.
   
7. Enter the fully qualified folder name in the **Folder** field. For example, `Shared`. You can view available folders in UiPath under Orchestrator.
   
8. Enter the [app ID](#oauth-2-0-authorization-code-setup) from your external application registration in the **Client ID** field.
   
9. Enter the [app secret](#oauth-2-0-authorization-code-setup) from your external application registration in the **Client secret** field.
   
10. Enter your [account logical name](#oauth-auth-code-account-tenant) in the **Account logical name** field.
    
11. Enter your [tenant logical name](#oauth-auth-code-account-tenant) in the **Tenant logical name** field. For example, `DefaultTenant`.
    
12. Enter user scopes in the **Scopes** field. Separate each scope with a space.
    
13. Click **Connect**.
    

### OAuth 2.0 (Client credentials) authentication

Use OAuth 2.0 client credentials authentication for machine-to-machine access to UiPath without user interaction. This method requires **Application scopes** when registering your external application in UiPath.

#### Register an external application in UiPath

Registering an external application generates an **App ID** and **App Secret** in UiPath, which correspond to the **Client ID** and **Client secret** fields in Workato.

Complete the following steps to register an external application:

1. Sign in to UiPath Automation Cloud and go to **Admin**.
   
2. Select **External Applications**.
   
3. Click **\+ Add Application** and enter a name for your application.
   
4. Select **Confidential application** as the **Application type**.
   
5. Click **Add scopes**, select **Orchestrator API Access** as the resource, and select the **Application scopes** required for your integration.
   
   > **SELECT APPLICATION SCOPES ONLY**
   > 
   > Select **Application scopes** only. Selecting **User scopes** instead results in a `400 Bad Request` error when connecting.
   
6. Enter `https://www.workato.com/oauth/callback` in the **Redirect URL** field.
   
7. Click **Add** to register the application.
   
8. Copy the **App ID** and **App Secret**. These values correspond to the **Client ID** and **Client secret** fields in Workato.
   

#### Retrieve the account and tenant logical names

Retrieve your account and tenant logical names following the steps in the [Personal access token](#account-tenant-logical-names) section.

#### Connect to UiPath using OAuth 2.0 (Client credentials)

Complete the following steps to set up an OAuth 2.0 (Client credentials) connection to UiPath in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `UiPath` and select it as your app.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![UiPath OAuth 2.0](/assets/oauth2-client-creds.CNbEMqRZ.png)_UiPath OAuth 2.0_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to specify whether the connection is a cloud or on-prem connection.
   
6. Use the **Authentication type** drop-down menu to select **OAuth2 (Client Credentials)**.
   
7. Enter the fully qualified folder name in the **Folder** field. For example, `Shared`. You can view available folders in UiPath under Orchestrator.
   
8. Enter the [app ID](#oauth-2-0-client-credentials-setup) from your external application registration in the **Client ID** field.
   
9. Enter the [app secret](#oauth-2-0-client-credentials-setup) from your external application registration in the **Client secret** field.
   
10. Enter your [account logical name](#oauth-client-creds-account-tenant) in the **Account logical name** field.
    
11. Enter your [tenant logical name](#oauth-client-creds-account-tenant) in the **Tenant logical name** field. For example, `DefaultTenant`.
    
12. Enter application scopes in the **Scopes** field. Separate each scope with a space.
    
13. Click **Connect**.

---
