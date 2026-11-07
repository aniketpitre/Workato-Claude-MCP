---
url: 'https://docs.workato.com/en/mcp/verified-user-access-configuration.md'
description: >-
  Configure MCP verified user access by setting up Workato Identity, end-user
  groups, and OAuth 2.0 end user tool connections.
---

# MCP verified user access configuration

MCP [verified user access](/en/mcp/verified-user-access) requires the following configuration:

- Workato Identity access method with assigned end user groups.
  
- End user tool connection with OAuth 2.0 authorization code grant.
  

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

---
