---
url: 'https://docs.workato.com/en/workato-identity/oidc/configure-oidc.md'
description: >-
  Configure OpenID Connect (OIDC) to enable authentication and profile retrieval
  for agents, MCP servers, and other agentic apps.
---

# Configure OIDC

Configure OpenID Connect (OIDC) to enable authentication and profile retrieval for agents, MCP servers, and other agentic apps.

## Prerequisite

You must configure complete the following requirements before you can create an OIDC profile:

- Configure an OIDC server in your identity provider (IdP)

### Okta OIDC server configuration example

Complete the following steps to configure an OIDC server in Okta:

1. Go to **Security > API** and click **Add Authorization Server**.
   
2. Define the name, audience, and provide a useful description.
   
3. Create the server.
   
4. Copy and store the **[Discovery URL](https://developer.okta.com/docs/reference/api/oidc/#well-known-openid-configuration)** for later use.
   

## Create an OIDC profile

An OIDC profile stores the connection details for an OIDC server in your IdP, including how Workato retrieves the IdP's public keys and which audience values it accepts. Workato uses these details to validate the tokens on incoming requests and to retrieve the caller's profile information. An OIDC profile enables authorization for workspaces and AI agents.

Complete the following steps to create an OIDC profile:

1. Sign in to your Workato account.
   
2. Go to **Workspace admin**. The **Access control** page displays.
   
3. Go to the **Solutions access** section and click **OpenID Connect profiles**.
   
4. Click **Create OIDC profile**.
   
5. Enter a name for the OIDC profile in the **Name** field.
   
   ![Create an OIDC profile](/assets/create-oidc.DouX9g9R.png)_Create an OIDC profile_
   
6. Use the **Discovery method** drop-down menu to select the method your IdP uses:
   
   **Discovery URL**
   
   1. Enter the OIDC discovery endpoint in the **Discovery URL** field.
      
      ![Enter the OIDC discovery endpoint](/assets/discovery-url.BNDKdPzw.png)_Enter the OIDC discovery endpoint_
      
   
   **JSON web key set**
   
   1. Enter the JSON web key set (JWKS) URL in the **JSON web key set (JWKS) URL** field. Workato uses the public keys to verify JWT signatures.
      
      ![Enter the JSON web key set (JWKS) URL](/assets/jwks-url.CVtL8pcs.png)_Enter the JSON web key set (JWKS) URL_
      
   2. Provide the **Issuer URL**.
      
   
7. Click **\+ Add audience** to add the audience value. This confirms that a token was issued specifically for Workato. For example: `api://workato-mcp`. Validation uses permissive mode if no audience is specified.
   
8. Click **Create profile**.
   

## Add OIDC authentication

You must [create an OIDC profile](#create-an-oidc-profile) before you can configure OIDC authentication.

Assigning an OIDC profile to an environment makes that profile available to the assets in the environment. Assets, such as MCP servers can then use the profile to authenticate and authorize incoming requests.

You can assign multiple OIDC profiles to a single environment. Asset builders choose which of the assigned profiles an individual asset uses.

Complete the following steps to add OIDC authentication to your OIDC profile:

1. Go to **Workspace admin**. The **Access control** page displays.
   
2. Go to **Authentication & Groups** in the sidebar.
   
3. Select the environment you plan to configure. The environment **End-user group** page displays by default.
   
   > **ENVIRONMENT AVAILABILITY**
   > 
   > Workspaces without [Environments](/en/features/environments) provisioned only have one environment available.
   
4. Select the **Authentication** tab.
   
5. Ensure that the **OpenID Connect authentication** toggle is enabled.
   
   ![Enable the OpenID Connect authentication toggle](/assets/oidc-authentication-toggle.9QLpklCI.png)_Enable the **OpenID Connect authentication** toggle_
   
6. Use the **OpenID Connect profile** drop-down menu to select the OIDC profile you plan to use. You can select multiple OIDC profiles.
   
7. Click **Save**.

---
