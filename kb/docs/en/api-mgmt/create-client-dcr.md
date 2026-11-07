---
url: 'https://docs.workato.com/en/api-mgmt/create-client-dcr.md'
description: >-
  Create an API client that uses a dynamic client registration provider so
  consumers can generate their own credentials in the developer portal.
---

# Create an API client with DCR

You can create an API client that uses a dynamic client registration (DCR) provider for authentication. This enables API consumers to generate their own credentials in the Developer Portal instead of requiring manual provisioning by an API Platform Admin.

> **PREREQUISITES**
> 
> Before you begin, ensure you have completed the following tasks:
> 
> - You have [configured at least one DCR provider](/en/api-mgmt/api-dynamic-client#add-a-dcr-provider) in your API platform settings.
> - You have API Platform Admin privileges.

## Set up client details

Complete the following steps to set up the client details. These steps are the same for all authentication methods.

1. Add an API client
   
   1. Go to **Platform > API Platform**.
      
   2. Select the **Clients** tab.
      
   3. Click **\+ Add new client**.
      
      ![Add new client](/assets/add-a-client.CzD77CsN.png)_Add new client_
      
   
2. Set up client details
   
   1. Enter a **Name** for your client. Use a descriptive identifier, such as the client's company or department name.
      
      ![Set up client details](/assets/add-client-details.DQ-ipDux.png)_Set up client details_
      
   2. Enter a **Description** for the client.
      
   3. Upload a **Client logo**. Drag and drop a JPG/PNG image or click **Upload from device** to select a file. This logo visually identifies your client in the portal.
      
   4. Enable the **Grant client access to portal** toggle to enable portal access. This grants your client permission to browse published API collections and manage their API keys. If your client only requires API tokens for testing or internal purposes, you can leave the toggle disabled.
      
   5. Provide the client identity based on your portal's [authentication method](/en/api-mgmt/configure-developer-portal#configure-authentication-settings):
      
      **Workato Identity**
      
      Use the **Client** drop-down menu to select the client. The list only includes end users already added to Workato Identity.
      
      **Magic link**
      
      Enter the client's email address in the **Email** field. Workato sends the client an email with a portal invitation.
      
   6. Click **Next** to proceed to the **Define access configuration** screen, where you can configure your client's API access.
      
   

## Define access configuration

The access configuration step determines how the client authenticates with your APIs. Select an authentication method and configure the DCR-specific settings.

The following sections describe the DCR-enabled configuration for each supported authentication method:

- [OpenID Connect with DCR](#openid-connect-with-dcr)
- [OAuth 2.0 Token Introspection with DCR](#oauth-token-introspection-with-dcr)

### OpenID Connect with DCR

Complete the following steps to configure an API client that uses OpenID Connect with a DCR provider.

1. Use the **Authentication method** drop-down menu to select **OpenID Connect (DCR enabled)**.
   
   ![Select authentication method](/assets/select-auth-dcr.Ch_icZx5.png)_Select authentication method_
   
2. Use the **API collections to include** drop-down menu to select one or more API collections. This defines the APIs your client can access and invoke in the portal. You can also create a client without collections to allow discovery before you grant API access.
   
3. Optional. Assign a **Policy** to control your client's API usage. Policies define rules such as rate limits or usage quotas.
   
4. Click **Next**.
   
5. Use the **Discovery method** drop-down menu to select **DCR provider**.
   
   The **DCR provider** option appears in the **Discovery method** drop-down menu only after you configure at least one DCR provider in **Settings > Developer Portal > Dynamic client registration**. The other **Discovery URL** and **JSON Web key set (JWKS) URL** options follow the existing OpenID Connect configuration flow. Refer to [OpenID Connect authentication](/en/api-mgmt/oidc) for more information.
   
6. Use the **DCR provider** drop-down menu to select the provider you plan to use for this client. The drop-down lists all DCR providers you configured that use the OpenID Connect authentication method.
   
   ![Select DCR provider](/assets/select-dcr-provider-client.jvFKPyU8.png)_Select DCR provider_
   
7. Click **Next** to proceed to the **Set up authentication** step and complete the remaining configuration.
   

After you complete the configuration, Workato creates the API client. The client appears on the **Clients** page with its authentication method and DCR provider details.

### OAuth 2.0 Token Introspection with DCR

Complete the following steps to configure an API client that uses OAuth Token Introspection 2.0 with a DCR provider.

1. Use the **Authentication method** drop-down menu to select **OAuth 2.0 Token introspection (DCR enabled)**.
   
   ![Select authentication method](/assets/select-auth-dcr-oauth.q8NwyJFU.png)_Select authentication method_
   
2. Use the **DCR provider** drop-down menu to select the provider you plan to use for this client. The drop-down lists all DCR providers you configured that use the OAuth 2.0 Token Introspection authentication method.
   
   Select **No provider (Manual setup)** to configure Token Introspection manually without a DCR provider. This requires you to configure the HTTP connection and introspection endpoint individually. Refer to [OAuth 2.0 Token Introspection authentication](/en/api-mgmt/oauth2-token-introspection) for more information.
   
3. Use the **API collections to include** drop-down menu to select one or more API collections. This defines the APIs your client can access and invoke in the portal. You can also create a client without collections to allow discovery before you grant API access.
   
4. Optional. Assign a **Policy** to control your client's API usage. Policies define rules such as rate limits or usage quotas.
   
5. Click **Next** to create the client.
   

After you complete the configuration, Workato creates the API client. The client appears on the **Clients** page with its authentication method and DCR provider details.

---
