---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/okta-end-user-mcp-server.md'
description: >-
  Use the Okta End User MCP server to connect your LLM to Okta with a curated
  set of tools to retrieve your identity, access, and authentication
  information.
---

# Okta End User MCP server

The Okta End User MCP server enables LLMs to understand and retrieve your identity, access, and authentication information in Okta through natural conversation. The Okta End User MCP server helps you understand your identity profile, discover which applications you have access to, and quickly launch applications with SSO links directly from your AI conversation.

## Uses

Use the Okta End User MCP server when you plan to perform the following actions:

- View your own Okta profile information including role, department, and manager
- Discover which applications you currently have access to
- Get direct SSO links to launch applications without navigating Okta
- Understand your organizational context and reporting relationships
- Check your profile attributes and identity information

### Example prompts

Use the following example prompts to invoke Okta End User MCP server tools:

- `What's my job title and department in Okta?`
- `Who is my manager?`
- `What applications do I have access to?`
- `Show me my Okta profile information.`
- `Get me the SSO link to launch Salesforce.`
- `What apps can I access?`

## Okta End User MCP server tools

The Okta End User MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [get\_my\_user\_profile](#get-my-user-profile-tool) | Retrieves profile and organizational information for the authenticated user. |
| [list\_assigned\_applications](#list-assigned-applications-tool) | Retrieves the set of applications currently assigned to the authenticated user. |
| [get\_application\_sso\_link](#get-application-sso-link-tool) | Retrieves the single sign-on (SSO) link for an application assigned to the authenticated user. |

## Install the Okta End User MCP server

Complete the following steps to install a prebuilt MCP server to your project:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Click **\+ Create MCP server**.
   
4. Go to the **Start with pre-built MCP Servers using your connected apps** section and select the prebuilt MCP server you plan to use.
   
5. Click **Use this server**.
   
6. Provide a name for your MCP server in the **Server name** field.
   
7. Use the **Location** drop-down menu to select the project for the MCP server.
   
8. Go to the **Connections** section and connect to your app account.
   
9. Select the connection type you plan to use for the MCP server template.
   
   - **User's connection**: MCP server tools perform actions based on the identity and permissions of the user who connects to the application. Users authenticate with their own credentials to execute the skill.
   - **Your connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
   
   ![Select your connection type](/assets/connection-type.Cor-6PJN.png)_Select your connection type_
   
   > **VERIFIED USER ACCESS AUTHENTICATION REQUIREMENTS**
   > 
   > Only app connections that use OAuth 2.0 authorization code grant are available for user's connection. Refer to [Verified user access](/en/mcp/verified-user-access) for more information.
   
10. Complete the app-specific connection setup steps in the following section.
    

## Okta connection setup

View Okta connection setup steps

Okta supports the following authentication types:

- [Authorization code grant authentication (OAuth 2.0)](#authorization-code-grant-authentication)
- [Client credentials-based authentication (OAuth 2.0)](#client-credentials-based-authentication)
- [API key-based authentication](#api-key-based-authentication)

Workato recommends using either authorization code grant authentication (OAuth 2.0) or client credentials-based authentication (OAuth 2.0) for improved security in your connection. These methods also let you define granular permissions that control which resources Workato can access in Okta.

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This feature requires configuration steps that are specific to your Virtual Private Workato (VPW) instance. If you are a VPW customer, refer to your VPW private documentation for the configuration details for your instances.

### Authorization code grant authentication

Authorization code grant authentication requires creating an app integration and secret in Okta.

View authorization code grant connection setup steps

#### Minimum and default scopes

OAuth 2.0 scopes define the level of access Workato has to your Okta instance. Review the following sections to determine which scopes to assign to your app integration for OAuth 2.0 authorization code grant authentication.

View minimum scopes

The Okta connector requires the following minimum scopes to establish a connection to Okta using authorization code grant authentication:

- `okta.logs.read`
- `okta.schemas.read`
- `offline_access`
- `openid`

View additional scopes

Select any additional scopes required for your use case from those defined in your Okta instance in \*\*Applications > Applications > Okta API Scopes\*\*. Select \`okta.users.read\` to connect using a custom role.

View default scopes

Workato requests the following default scopes if you don't select specific scopes:

- `okta.logs.read`
- `okta.schemas.read`
- `offline_access`
- `openid`
- `okta.eventHooks.manage`
- `okta.users.manage`
- `okta.groups.manage`
- `okta.apps.read`

#### Create an app integration and secret for authorization code grant authentication

Complete the following steps to create an app integration and secret for authorization code grant authentication:

1. Sign in to your Okta organization as a user with administrator privileges.
   
2. Go to the Okta **Admin Console** and select **Applications > Applications**.
   
3. Click **Create App Integration**.
   
4. Find the **Sign-in method** section, and select **OIDC - OpenID Connect**.
   
5. Go to the **Application type** section and select **Web Application**.
   
6. Enter a unique **App integration name** on the **New Web App Integration** page.
   
   ![Create a new app integration](/assets/okta-create-new-app-integration.BLeNUhIg.png) _Create a new app integration_
   
7. Ensure the **Require Demonstrating Proof of Possession (DPoP) header in token requests** field is deselected.
   
8. Select the following checkboxes in the **Client acting on behalf of a user** field of the **Grant type** section:
   
   - Authorization Code
   - Refresh Token
9. Enter the following Workato callback URI in the **Sign-in redirect URIs** section: `https://www.workato.com/oauth/callback`
   
   ![Sign-in redirect URIs](/assets/okta-sign-in-redirect-urls.D-UnaPCS.png) _Sign-in redirect URIs_
   
10. Select an **Assignment** option according to your preference and then select **Save**. Okta creates the app integration.
    
11. Go to the **General** tab and copy the **Client ID** and **Client Secret** so you can enter these credentials in Workato.
    
    ![Copy the Client ID and Client Secret](/assets/okta-client-id-secret.DFWv3q9Z.png) _Copy the **Client ID** and **Client Secret**_
    
12. Go to **General Settings** and ensure the **Proof of possession** field is deselected.
    
13. Go to the **Okta API Scopes** tab and assign the necessary [scopes](#authorization-code-grant-scopes) to the app integration. The connection requires the following scopes at a minimum:
    
    - `okta.logs.read`
    - `okta.schemas.read`
    
    `offline_access` and `openid` permissions are assigned automatically.
    
    The connection requires the following additional scope if you are using a custom role:
    
    - `okta.users.read`
    
    ![Assign Okta API scopes](/assets/okta-api-scopes.CKj9Yhd-.png) _Assign Okta API scopes_
    

#### Connect to Okta using authorization code grant authentication

Complete the following steps to create an authorization code grant connection to Okta in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Okta** as your connection on the **New connection** page.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Name your connection](/assets/authorization-code-grant-setup.D0_C8vq4.png)_Name your connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
6. Enter your Okta domain name in the **Okta domain** field. For example, `mycompany.okta.com` or `mytest.oktapreview.com`. Ensure that the domain name you enter doesn't include `-admin`, such as `mycompany-admin.okta.com`, as this URL is used to access the Okta admin console from the UI and isn't an OAuth endpoint.
   
7. Enter your **Client ID**.
   
8. Provide your **Client secret**.
   
9. Expand the **Advanced settings** section and use the **OAuth 2.0 scopes** drop-down menu to select additional OAuth 2.0 scopes for this connection. The scopes must match the scopes defined in your Okta instance in **Applications > Applications > Okta API Scopes**.
   
   Workato requests the scopes you specify in addition to the [minimum required scopes](#authorization-code-grant-scopes). Workato requests the default scopes if you don't select specific scopes.
   
10. Click **Connect**.
    

### Client credentials authentication

Client credentials authentication requires creating an app integration and private key in Okta.

View client credentials connection setup steps

#### Minimum and default scopes

OAuth 2.0 scopes define the level of access Workato has to your Okta instance. Review the following sections to determine which scopes to assign to your app integration for OAuth 2.0 client credentials authentication. Your app integration must be assigned the `Read-only Administrator` role in Okta if your connection uses more than the minimum required scopes. If your app integration uses a custom role, you can assign it an applicable custom role instead.

View minimum scopes

The Okta connector requires the following minimum scopes to establish a connection to Okta using client credentials authentication:

- `okta.logs.read`
- `okta.schemas.read`

View additional scopes

Select any additional scopes required for your use case from those defined in your Okta instance in \*\*Applications > Applications > Okta API Scopes\*\*. Select \`okta.users.read\` to connect using a custom role.

View default scopes

Workato requests the following default scopes if you don't select specific scopes:

- `okta.logs.read`
- `okta.schemas.read`
- `okta.eventHooks.manage`
- `okta.users.manage`
- `okta.groups.manage`
- `okta.apps.read`

#### Create an app integration and private key for client credentials authentication

Complete the following steps to create an app integration and private key for client credentials-based authentication:

1. Sign in to your Okta organization as a user with administrator privileges.
   
2. Go to the Okta **Admin Console** and select **Applications > Applications**.
   
3. Click **Create App Integration**.
   
4. Select **API Services** in the **Sign-in method** section of the **Create a new app integration** page.
   
   ![Select API Services](/assets/okta-api-services.By5Puj_h.png) _Select **API Services**_
   
5. Enter a unique **App integration name** and click **Save** on the **New API Services App Integration** page.
   
   ![App integration name](/assets/okta-api-services-app-integration-name.Kl3_tnG1.png) _Enter an **App integration name**_
   
6. Click **Edit** and select **Public key / Private key** in the **Client authentication** section.
   
7. Go to the **Public keys** section and click **Edit**.
   
8. Click **Add key**.
   
9. Click **Generate new key** to generate a new key pair.
   
   ![Add a public key](/assets/okta-public-key-example.C6KyA7vk.png) _Add a public key_
   
10. Go to the **Private key** section and select **PEM**.
    
11. Click **Copy to clipboard** to copy the private key. Enter this key in Workato's [Okta connection settings](#client-credentials-based-authentication). You can't retrieve the private key again after leaving the page.
    
    ![Copy the private key](/assets/okta-private-key-example.Dk65gSw1.png) _Click **Copy to clipboard** to copy the private key_
    
12. Click **Done**.
    
13. Click **Save** in the new app integration's **General** tab to store and activate the key. You must save the key before you can use it to connect to Workato.
    
    Click **Save** if you see the message **Existing client secrets will no longer be used**.
    
    Verify that the key status changes to **Active**.
    
14. Go to **General > General Settings** and ensure the **Proof of possession** field is deselected.
    
15. Go to the **Okta API Scopes** tab and assign the necessary [scopes](#client-credentials-scopes) to the app integration. The connection requires the following minimum scopes:
    
    - `okta.logs.read`
    - `okta.schemas.read`
    
    The connection requires the following additional scope if you are using a custom role:
    
    - `okta.users.read`
    
    ![Assign Okta API scopes](/assets/okta-api-scopes-client-creds.DBmEdH4Y.png) _Assign Okta API scopes_
    
16. Go to the **Admin roles** tab and click **Edit assignments**.
    
17. Use the **Roles** drop-down menu to select `Read-only Administrator` or an applicable custom role.
    
18. Click **Save changes**.
    

#### Connect to Okta using client credentials authentication

Complete the following steps to create a client credentials connection to Okta in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Okta** as your connection on the **New connection** page.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Name your connection](/assets/client-credentials-setup.pekF4yj9.png)_Name your connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Client credentials**.
   
6. Enter your Okta domain name in the **Okta domain** field. For example, `mycompany.okta.com` or `mytest.oktapreview.com`. Ensure that the domain name you enter doesn't include `-admin`, such as `mycompany-admin.okta.com`. This URL is used to access the Okta admin console from the UI and isn't an OAuth endpoint.
   
7. Enter your **Client ID**.
   
8. Provide the private key generated in Okta in PEM format in the **Private key** field. Ensure to include `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----`.
   
9. Expand the **Advanced settings** section and use the **OAuth 2.0 scopes** drop-down menu to select additional OAuth 2.0 scopes for this connection. The scopes must match the scopes defined in your Okta instance in **Applications > Applications > Okta API Scopes**.
   
   Workato requests the scopes you specify in addition to the [minimum required scopes](#client-credentials-scopes). Workato requests the default scopes if you don't select specific scopes.
   
10. Click **Connect**.
    

### API key-based authentication

API key-based authentication requires creating an API key in Okta.

View API key connection setup steps

#### Generate an API key

  

> **API KEY PRIVILEGES AND LIMITATIONS**
> 
> You must have administrator privileges in Okta to create an API key. Ensure that you're logged in as an administrator before you proceed.
> 
> Workato requires that the user and API key used in the connection have **Organization Administrator** or **Super Administrator** permissions. API keys inherit all permissions from the administrator who created them and can't be restricted to specific resources or operations. We recommend that you use a scoped OAuth 2.0 access token for improved security.
> 
> Refer to [Create an API token](https://developer.okta.com/docs/guides/create-an-api-token/create-the-token/) for more information.

Complete the following steps to generate an API key in Okta:

1. Sign in to Okta.
   
2. Go to **Security > API > Token**.
   
3. Click **Create token** to generate an API key. The key inherits the permissions of the administrator who created it.
   

#### Connect to Okta using API key-based authentication

Complete the following steps to create an API key connection to Okta in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Okta** as your connection on the **New connection** page.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Okta API key connection setup](/assets/connection-setup-api.VbvzwXfa.png)_Okta API key connection setup_
   
4. Use the **Authentication type** drop-down menu to select **API key**.
   
5. Enter your Okta domain name in the **Okta domain** field. For example, `mycompany.okta.com` or `mytest.oktapreview.com`. Ensure that the domain name you enter doesn't include `-admin`, such as `mycompany-admin.okta.com`, as this URL is used to access the Okta admin console from the UI and isn't an OAuth endpoint.
   
6. Enter the API key generated in your Okta instance.
   
7. Click **Connect**.
   

## How to use Okta End User MCP server tools

Refer to the following sections for detailed information on available tools:

### get\_my\_user\_profile tool

The **get\_my\_user\_profile** tool retrieves your profile and organizational information. Your LLM uses this tool to provide detailed identity context, including your role, department, title, manager, and other profile attributes.

**Try asking**:

- `What's my official job title and department?`
- `Show me my Okta profile information.`
- `Who is my manager in Okta?`
- `What's my role and organizational information?`

### list\_assigned\_applications tool

The **list\_assigned\_applications** tool retrieves the applications currently assigned to you. Your LLM uses this tool to show you what applications you can already access through Okta, helping you understand your current access permissions.

**Try asking**:

- `What applications do I have access to in Okta?`
- `Show me all my assigned apps.`
- `List the applications I can use.`
- `What tools and services can I access through Okta?`

### get\_application\_sso\_link tool

The **get\_application\_sso\_link** tool retrieves the single sign-on (SSO) link for an application assigned to the authenticated user. Your LLM uses this tool to launch specific apps without navigating to the Okta UI.

**Try asking**:

- `Get me the SSO link to launch Salesforce.`
- `Give me the direct link to access Google Workspace.`
- `Open the SSO link for Zoom.`
- `How do I access the HR portal? Get me the link.`

## Getting started

View and manage your MCP server tools in the **Details** tab **Tools** section. Tool management provides the following capabilities:

- [Start tools](/en/mcp/manage-tools#start-tools)
- [Remove tools](/en/mcp/manage-tools#remove-tools)
- [Edit tools](/en/mcp/manage-tools#edit-tools)
- [Add tools](/en/mcp/manage-tools#add-tools)
- [Edit your LLM-facing MCP server description](/en/mcp/prebuilt-mcps#edit-llm-facing-mcp-server-description)

> **TOOLS MUST BE STARTED**
> 
> Your LLM can only access active tools in your MCP server connector.

---
