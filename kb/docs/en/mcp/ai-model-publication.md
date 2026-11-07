---
url: 'https://docs.workato.com/en/mcp/ai-model-publication.md'
description: >-
  Publish a Workato MCP server to your AI model organization so team members can
  discover and connect to it from ChatGPT and other clients.
---

# Publish MCP servers to AI model organizations

Register your Workato MCP server and publish it for organizational or team use. This enables your team members to discover and connect to the published MCP server.

## ChatGPT MCP server publication

Ensure you meet the following prerequisite before you publish your MCP server for Enterprise or Business use:

- Verify that you have ChatGPT Admin or Owner privileges.
- Complete the steps in the [ChatGPT MCP configuration](/en/mcp/prebuilt-mcps/ai-model-configuration#chatgpt-mcp-configuration) section.

Complete the following steps to publish your MCP server for organization-wide use:

1. Sign in to your ChatGPT account.
   
2. Go to **Workspace Settings > Apps**.
   
3. Click **Drafts** and locate the app you added in the [ChatGPT MCP configuration](/en/mcp/prebuilt-mcps/ai-model-configuration#chatgpt-mcp-configuration) section.
   
4. Click the **Publish** button. Published apps appear in the workspace's approved connectors list and in users' **Apps settings** with the label **custom** next to the app name.
   

### Connect to a published MCP server in ChatGPT

Complete the following steps to connect to a published MCP server in ChatGPT:

1. Sign in to your [ChatGPT](https://chatgpt.com) account.
   
2. Go to **Settings > Apps & Connectors**.
   
3. Select the app published by your organization and click **Connect**.
   
4. Complete the authorization flow and authenticate with your credentials.
   
5. Open a new chat and enter a prompt. ChatGPT automatically invokes the relevant MCP server tools based on your input.
   

## Claude MCP server publication

Ensure you meet the following prerequisites before you publish your MCP server for Enterprise or Team use:

- Verify that you have Claude Admin or Owner privileges.
- Complete the steps in the [Claude MCP configuration](/en/mcp/prebuilt-mcps/ai-model-configuration#claude-mcp-configuration) section.

> **USE A SEPARATE WORKATO TOKEN FOR EACH CLAUDE TEAM**
> 
> Use a separate `wkt_token` for each Claude Team project when connecting to multiple instances to avoid `Unauthorized` errors.

Complete the following steps to publish your MCP server for organization-wide use:

1. Sign in to your Claude account.
   
2. Go to **Organization Settings > Connectors**.
   
3. Click **Add connector** and enter your remote MCP server URL.
   
4. Click **Add**. The connector is available to everyone in your team to connect and authenticate.
   

### Connect to a published MCP server in Claude

Complete the following steps to connect to a published MCP server in Claude:

1. Sign in to your [Claude](https://claude.ai) account.
   
2. Click the **+** (add) button and select **Connectors**.
   
3. Locate the MCP server connector published by your organization and select it.
   
4. Select **Connect**.
   
5. Complete the authorization flow and authenticate with your credentials.
   
6. Open a new chat and enter a prompt. Claude automatically invokes the relevant MCP tools based on your input.
   

## Cursor MCP server publication

You can define an MCP server at the project level to make MCP server tools available in a specific project. Cursor reads configuration files from the `.cursor/` directory at the project root, such as `.cursor/mcp.json`.

Ensure you meet the following prerequisites before you publish your MCP server for team distribution:

- Verify that you have the correct permissions to modify project-level files in your repository.
- Complete the steps in the [Cursor MCP configuration](/en/mcp/prebuilt-mcps/ai-model-configuration#cursor-mcp-configuration) section.

Complete the following steps to publish your MCP server for team-wide use:

1. Open Cursor.
   
2. Go to your repository root and create a `.cursor/mcp.json` file with the following code:
   
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
   
3. Commit the `.cursor/mcp.json` file to your repository. This ensures all project team members can access the MCP server tools.
   

### Connect to a published MCP server in Cursor

Complete the following steps to connect to a project-wide MCP server in Cursor:

1. Pull the latest changes from your repository to ensure you have the `.cursor/mcp.json` file locally.
   
2. Open the project folder in Cursor. Cursor automatically detects and connects to the MCP server configured in `.cursor/mcp.json` on startup.
   
3. Optional. Go to **Settings > Features > MCP Tools** to verify the connection. The server appears with a green indicator and a list of its available tools.
   
4. Provide your credentials if your MCP server requires authentication:
   
   - **API key**: Set the required environment variable locally on your machine.
   - **OAuth**: Cursor prompts you to authenticate on first use.
5. Restart Cursor to load the new configuration in the `.cursor/mcp.json` file.
   
6. Open the Cursor AI chat panel and enter a prompt. Cursor automatically invokes the relevant MCP tools based on your input.
   

## Microsoft Copilot MCP server publication

Ensure you meet the following prerequisites before you publish your MCP server for organizational use:

- Verify that you have Administrator privileges.
- Complete the steps in the [Microsoft Copilot MCP configuration](/en/mcp/prebuilt-mcps/ai-model-configuration#microsoft-copilot-mcp-configuration) section.

Complete the following steps to publish your MCP server for organization-wide use:

1. Sign in to your Microsoft Copilot account.
   
2. Go to the agent where you plan to publish the MCP server.
   
3. Go to the **Overview** page and select **Publish** in the navigation menu.
   
4. Complete the fields in the publish form. This information populates the catalog entry in your organization's Office and Teams Catalogs and the Microsoft Admin Center Integrated Apps list.
   
5. Click **Publish**. This provisions a bot resource in the Microsoft Entra ID tenant environment that corresponds to your Copilot agent.
   
6. Go to the **Teams and Microsoft 365 Copilot** channel and open the configuration panel.
   
7. Go to **Turn on Microsoft 365** and ensure that **Make agent available in Microsoft 365 Copilot** is selected.
   
8. Select **Add channel**.
   
9. Select **Availability options** to configure who can access the agent.
   
10. Select **Share with specific users or groups** or **Deploy org-wide** as your distribution method:
    
    **Share with specific users or groups**
    
    1. Select **Show to my teammates and shared users**.
       
    2. Confirm the **Show in Built By Your Colleagues** checkbox is selected.
       
    3. Click **Update**. The agent appears in the **Built with Power Platform** section of the Teams app store.
       
    
    **Share organization-wide**
    
    1. Select **Download .zip** to download the agent package.
       
    2. Open the Microsoft 365 admin center.
       
    3. Go to **Copilot > Agents > Upload custom agent**.
       
    4. Upload the ZIP file and select the users or groups who can access the MCP server tools.
       
    

### Connect to a published MCP server in Microsoft Copilot

Complete the following steps to connect to a published MCP server in Microsoft Copilot:

1. Sign in to Microsoft 365 Copilot.
   
2. Locate the agent where you plan to add the published MCP server and select it to open the chat interface.
   
3. Select **Open Connection Manager** if this is your first time using the agent and you're prompted to authenticate.
   
4. Select **Connect** then select **Add new connection**.
   
5. Enter your credentials and select **Sign in**.
   
6. Return to the chat window and enter a prompt. Microsoft Copilot automatically invokes the relevant MCP tools based on your input.

---
