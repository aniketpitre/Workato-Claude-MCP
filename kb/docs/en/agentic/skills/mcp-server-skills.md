---
url: 'https://docs.workato.com/en/agentic/skills/mcp-server-skills.md'
description: >-
  Add MCP server skills to a genie so it can call custom and common provider MCP
  servers and access external APIs without custom skill logic.
---

# MCP server skills

[Skills](/en/agentic/skills) can consume [MCP servers](/en/mcp). Skills can call custom MCP servers and common provider MCP servers. This enables you to perform the following actions:

- Access external APIs
- Integrate with third-party tools without requiring custom skill development
- Call Workato-hosted [MCP servers](/en/mcp) and external MCP servers from a genie

## Add MCP server skills to a genie

The tools in your MCP server can be used as skills. Refer to [Create skills](/en/agentic/agent-studio/create-a-genie#create-skills) for more information.

Complete the following steps to add MCP server skills to your genie:

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
