---
url: 'https://docs.workato.com/en/mcp/genies-as-mcp-clients.md'
description: >-
  Connect MCP servers as skills in an Agent Studio genie to call external APIs
  and third-party tools without building custom skills.
---

# Genies as MCP clients

Model context protocol (MCP) servers are consumable through [skill](/en/agentic/skills) recipes in your [Agent Studio genie](/en/agentic/agent-studio). Skills can call custom MCP servers and common provider MCP servers. This enables you to perform the following actions:

- Access external APIs
- Integrate with third-party tools without requiring custom skill development
- Call Workato-hosted [MCP servers](/en/mcp) and external MCP servers from a genie

Genie MCP clients provide the following authentication options:

- **Token authentication**: The MCP server uses header-based authentication with API token or query parameters.
  
  - No reference connection is required.
  - Single authentication context for all users.
  - All requests use same token.
  - Doesn't support [verified user access](/en/agentic/agent-studio/verified-user-access).
- **OAuth2 authentication**: The MCP server uses OAuth2 authentication.
  
  - Requires URL authentication. For example: `/your-application.com/mcp`
  - Uses a reference connection to discover available tools.
  - Supports optional [verified user access](/en/agentic/agent-studio/verified-user-access) for user-specific authentication.

## Add MCP server tools to an Agent Studio genie

The tools in your MCP server can be used as skills. Refer to [Create skills](/en/agentic/agent-studio/create-a-genie#create-skills) for more information.

Complete the following steps to add MCP server tools to your genie:

1. Sign in to Workato.
   
2. Go to **AI Hub > Agent Studio**.
   
3. Select the genie to edit.
   
4. Click **Edit**.
   
5. Go to the **Enterprise skills** section and click **\+ Add**.
   
6. Select **MCP server**.
   
7. Select a common provider MCP server or click **\+ Custom MCP server**.
   
   ![Select an MCP server option](/assets/add-mcp-server.DBvtu3EL.png)_Select an MCP server option_
   
8. Configure your MCP server:
   
   **Custom MCP server**
   
   #### Add skills from a custom MCP server
   
   1. Click **\+ Custom MCP server > Next**.
      
   2. Provide a name for your MCP server connection in the **Connection name** field.
      
      ![Set up your MCP server connection](/assets/add-a-custom-mcp-server._Gf5dUvn.png)_Set up your MCP server connection_
      
   3. Use the **Location** drop-down menu to select a location for your MCP server connection.
      
   4. Provide your MCP server URL in the **MCP Server URL** field.
      
   5. Use the **Authentication Type** drop-down menu to select your authentication method provide the necessary credentials. OAuth2 authentication is required if you plan to use [Workato Identity for your MCP server authentication](/en/mcp/mcp-authentication#oauth2-authentication-with-workato-identity).
      
   6. Click **Connect**.
      
   7. Select the checkbox for each tool you plan to add as a skill to your genie.
      
      ![Select MCP server tools](/assets/select-mcp-server-tools.HEk9Cf5a.png)_Select MCP server tools_
      
   8. Click **Done**. The MCP server tools you selected display in the **Enterprise skills** section on your genie **Overview** page.
      
   
   **Common provider MCP server**
   
   #### Add skills from a common provider MCP server
   
   1. Select the common provider MCP server you plan to use.
      
   2. Click **Next**.
      
   3. Provide a name for your MCP server connection in the **Connection name** field.
      
   4. Use the **Location** drop-down menu to select a location for your MCP server connection.
      
   5. Complete the remaining connection fields. These fields vary by provider and authentication method.
      
      ![Atlassian provider MCP server](/assets/atlassian-provider-mcp-server-example.BnXuiabO.png)_Atlassian provider MCP server_
      
   6. Click **Connect**.
      
   7. Select the checkbox for each tool you plan to add as a skill to your genie.
      
      ![Select MCP server tools](/assets/select-mcp-server-tools.HEk9Cf5a.png)_Select MCP server tools_
      
   8. Click **Done**. The MCP server tools you selected display in the **Enterprise skills** section on your genie **Overview** page.

---
