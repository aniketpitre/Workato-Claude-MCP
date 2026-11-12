---
url: 'https://docs.workato.com/en/mcp/verified-user-access-configuration.md'
description: >-
  Configure MCP verified user access by setting up either OIDC or Workato
  Identity with end-user groups, and OAuth 2.0 end user tool connections.
---

# MCP verified user access configuration

MCP [verified user access](/en/mcp/verified-user-access) is compatible with Workato Identity and OpenID Connect (OIDC). OIDC allows users to sign in with Workato Identity, then authorize the apps used by the MCP server's tools using the configured OIDC provider.

MCP verified user access requires the following Workato Identity or OIDC configuration:

**Workato Identity**

- Workato Identity access method with assigned end-user groups
- End-user tool connection with OAuth 2.0 authorization code grant

**OIDC**

- OIDC access method with optional end-user groups and end users

Refer to [Create an SDK connection for MCP verified user access](/en/developing-connectors/sdk/guides/walkthrough#create-an-sdk-connection-for-mcp-verified-user-access) if you plan to use the [Connector SDK](/en/developing-connectors/sdk) with MCP verified user access.

## Workato Identity configuration

Complete the following steps to configure Workato Identity for MCP verified user access:

1. [Configure SAML-based authentication](/en/workato-identity/saml-sso#configure-saml-based-authentication).
   
2. [Configure IdP user access](/en/workato-identity/saml-sso#configure-idp-user-access).
   
3. [Create an end-user group](/en/workato-identity/user-groups#create-a-user-group).
   

## MCP Workato Identity access method and end-user group configuration

Ensure that you have end-user group with assigned users in Workato Identity before following these steps.

Complete the following steps to set your MCP server access method to Workato Identity and add end-user groups:

1. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
2. Click the MCP server you plan to use.
   
3. Click **Settings > End user access**.
   
4. Go to the **Access Method** section and ensure that Workato Identity is selected.
   
5. Click **Add user groups**.
   
   ![Click Add user groups](/assets/add-user-groups.BG20fzRt.png)_Click **Add user groups**_
   
6. Use the **User groups** drop-down menu to select the user groups you plan to provide with access to the MCP server.
   
7. Click **Add**.
   

## Configure an OAuth 2.0 authorization code grant connection

The **End user's connection** option only supports OAuth 2.0 connections.

Complete the following steps to set up an OAuth 2.0 connection:

1. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
2. Click the MCP server you plan to use.
   
3. Select the tool you plan to use with the end user's connection. The recipe editor opens.
   
4. Click **Edit**.
   
5. Select the action step where you plan to add the connection.
   
6. Select **End user's connection**.
   
   ![Select End user's connection](/assets/users-connection.DrJMnyxd.png)_Select **End user's connection**_
   
7. Provide a name for your connection in the **Name** field.
   
   ![Authorization code grant connection example](/assets/coupa-authorization-code-grant-example.Bhbnc19V.png)_Authorization code grant connection example_
   
8. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
9. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
10. Enter your client ID in the **Client ID** field.
    
11. Enter your client secret in the **Client secret** field.
    
12. Provide your host or endpoint URL in the appropriate field. The required field name and value differ by application. For example, a Coupa connection requires the host URL in the **Host** field with the following URL format: `https://your-instance-name.coupacloud.com`.
    
13. Use the **Scopes** drop-down menu to select the scopes you plan to use for your connection.
    
14. Click **Connect**.
    

## OIDC configuration

Complete the following steps to configure OIDC for MCP verified user access:

1. Configure an OIDC server in your identity provider (IdP).
   
2. Create an OIDC profile to store the connection details for an OIDC server in your IdP, including how Workato retrieves the IdP's public keys and which audience values it accepts.
   
3. Add OIDC authentication for environments by going to **Workspace admin > End users > Environment access** and selecting the checkboxes for the environments the user can access. Options are DEV, TEST, and PROD.
   

## Configure app authorization behavior

Configure when users authorize apps for an MCP server that uses verified user access. The **App authorization** setting has two options:

- **When added to a client**: Users authorize their apps after they sign in with Workato Identity and add the MCP server to their client. This is the default.
- **When first used**: Users sign in without an app authorization prompt and authorize an app the first time a tool call requires an app authorization.

On-demand setup applies to both options. Only MCP servers that use Workato Identity or OIDC are compatible with verified user access.

Complete the following steps to configure app authorization behavior for verified user access connections:

1. Go to **AI Hub > Enterprise MCP**.
   
2. Click the MCP server where you plan to configure app authorization behavior.
   
3. Click the **End user access** tab.
   
4. Click **Edit**.
   
5. Use the **App authorization** drop-down menu to select **When added to a client** or **When first used**.
   
6. Click **Save changes**.

---
