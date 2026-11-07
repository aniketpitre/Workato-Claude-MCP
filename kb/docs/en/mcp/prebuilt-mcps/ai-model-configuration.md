---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/ai-model-configuration.md'
description: >-
  Configure your prebuilt MCP server with AI models including ChatGPT, Claude,
  Cursor, and Microsoft Copilot using your remote MCP URL.
---

# AI model configurations

You can use your `REMOTE_MCP_URL` to configure your prebuilt MCP server with the following AI models:

## ChatGPT MCP configuration

Complete the following steps to add your MCP server to ChatGPT:

1. Go to your ChatGPT account.
   
2. Go to **Settings > Apps & Connectors > Advanced settings** and enable the **Developer mode** toggle.
   
3. Go to **Settings > Apps & Connectors**.
   
4. Click **Create**. This button is only visible when the **Developer mode** toggle is enabled.
   
5. Enter a name for your MCP connector in the **Name** field.
   
   ![ChatGPT connector](/assets/chatgpt-connector.B98_tSbx.png)_Configure your ChatGPT MCP connector_
   
6. Paste your MCP URL and token in the **URL field**.
   
7. Optional. Enter a description in the **Description** field.
   
8. Use the **Authentication** drop-down menu to select **No Auth**.
   
9. Select the checkbox to accept the risk of adding a custom MCP server.
   
10. Click **Create**.
    
11. Create a new chat in ChatGPT to use your MCP tools.
    

Refer to [ChatGPT MCP server publication](/en/mcp/ai-model-publication#chatgpt-mcp-server-publication) to share your MCP server with your AI model organization.

## Claude MCP configuration

Complete the following steps to add your MCP server to Claude:

> **USE A SEPARATE WORKATO TOKEN FOR EACH CLAUDE TEAM**
> 
> Use a separate `wkt_token` for each Claude Team project when connecting to multiple instances to avoid `Unauthorized` errors.

1. Sign in to Workato.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Select the MCP server and copy the **Remote MCP URL**.
   
4. Go to your Claude account.
   
5. Go to **Settings > Connectors**.
   
6. Click **\+ Add new connector**.
   
7. Enter a name for your MCP connector in the **Name** field.
   
   ![Claude connector](/assets/claude-mcp-setup.CLtAsbY0.png)_Configure your Claude MCP connector_
   
8. Paste your MCP URL and token into the **Remote MCP server URL** field.
   
9. Click **Add**. The newly created MCP connector appears in the list of connectors.
   
10. Click **Configure**.
    
11. Use the permissions drop-down menu to select **Always ask permission** or **Allow unsupervised**. **Always ask permission** is selected by default.
    
12. Create a new chat in Claude to use your MCP tools.
    

Refer to [Claude MCP server publication](/en/mcp/ai-model-publication#claude-mcp-server-publication) to share your MCP server with your AI model organization.

## Cursor MCP configuration

The following process authenticates with an MCP URL and authentication token. Refer to [Cursor MCP remote server configuration with Workato Identity authentication](/en/mcp/developer-api-mcp#cursor-mcp-remote-server-configuration-with-workato-identity-authentication) if you plan to authenticate with [Workato Identity](/en/workato-identity).

Complete the following steps to add your MCP server to Cursor:

1. Go to **Settings > Cursor settings**.
   
2. Click **MCP & Integrations** in the sidebar.
   
3. Click **\+ New MCP Server** to open the `mcp.json` file.
   
   ![New MCP server](/assets/configure-cursor.DhhCFK4N.png)_Click **\+ New MCP Server**_
   
4. Update the configuration to use the MCP URL and token you copied in the preceding steps. For example:
   
   ```json
   
   {
     "mcpServers": {
       "snowflake-tools": {
         "url": "https://2255.apim.mcp.workato.com?wkt_token=YOUR_API_TOKEN"
       },
       "github-tools": {
         "url": "https://387.apim.mcp.workato.com/abc247/example-collection-name-v1?wkt_token=YOUR_API_TOKEN"
       }
     }
   }
   ```
   
5. Save your changes.
   
6. Create a new chat with your Cursor agent to use your MCP tools.
   
   You must start a new chat with your agent. Cursor agents only have access to the tools and capabilities available when a chat begins. Agents can't detect or use new MCP configurations, servers, or tools added after starting a chat.
   

Refer to [Cursor MCP server publication](/en/mcp/ai-model-publication#cursor-mcp-server-publication) to share your MCP server with your AI model organization.

## Microsoft Copilot MCP configuration

Microsoft Copilot supports OAuth authentication and API-based access for MCP servers. Refer to the [Microsoft Copilot MCP server configuration](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent) documentation for more information.

Complete the following steps to add your MCP server to Microsoft Copilot:

1. Sign in to your Microsoft Copilot Studio account.
   
2. Select **Agent** in the sidebar and create a new agent.
   
3. Provide a name for your agent in the **Name** field.
   
4. Optional. Provide a description for your agent in the **Description** field.
   
5. Add your MCP server as a tool. Steps for adding an MCP server vary based on your authentication method:
   
   **OAuth authentication**
   
   ##### Microsoft Copilot OAuth authentication
   
   1. Go to the **Tools** section and click **\+ Add tool > Model Context Protocol**.
      
      ![Add tools](/assets/microsoft-copilot-mcp-configuration.ClgqMr_0.png)_Add tools_
      
   2. Paste your MCP URL into the **Server URL** field.
      
   3. Go to the **Authentication** section and select **OAuth 2.0**.
      
   4. Go to the **Type** section and select **Dynamic discovery**.
      
   
   **API-based access**
   
   ##### Microsoft Copilot API-based access
   
   1. Go to the **Tools** section and click **\+ Add tool > Custom connector**. Microsoft redirects you to Power Apps to create the new connector.
      
   2. Click **\+ New custom connector** and select **Import an OpenAPI file**.
      
   3. Import the following YAML file, replacing `<MCP Server Name>`, `<MCP Server Description>`, `<MCP Server Path>`, and `<WKT_TOKEN>` with your MCP server configuration information:
      
      ```yml
      swagger: '2.0'
      info:
        title: <MCP Server Name> #Change name here
        description: <MCP Server Description> #Change description here
        version: 1.0.0
      host: 558.apim.mcp.workato.com
      basePath: /
      schemes:
        - https
      paths:
        <MCP Server Path>: #change path here, for example:/gregf247/github-jira-cursor-tools-v1
          post:
            summary: <MCP Server Name> #Change name here
            description: <MCP Server Description> #Change description here
            operationId: InvokeServer
            x-ms-agentic-protocol: mcp-streamable-1.0
            parameters:
              - name: wkt_token
                in: query
                required: true
                type: string
                enum:
                  - <WKT_TOKEN> # Add wkt_token from Workato here
                default: <WKT_TOKEN> # Add wkt_token from Workato here
            responses:
              '200':
                description: Immediate Response
      securityDefinitions: {}
      security: []
      ```
      
   
6. Return to Microsoft Copilot Studio and connect to the newly created MCP server.
   

Refer to [Microsoft Copilot MCP server publication](/en/mcp/ai-model-publication#chatgpt-mcp-server-publication) to share your MCP server with your AI model organization.

---
