---
url: 'https://docs.workato.com/en/airo/mcp/connect/cursor.md'
description: Set up AIRO Connect in Cursor with OAuth 2.0 or an API token.
---

# Set up AIRO Connect in Cursor

You can set up AIRO Connect in Cursor using OAuth 2.0 or an API token.

## Before you begin

You need a Workato account with AIRO access and Cursor installed. The OAuth 2.0 configuration uses `npx`, which requires [Node.js](https://nodejs.org/) to be installed and available in your `PATH`. Run `node -v` in your terminal to verify your installation.

API token authentication also requires a Workato API token. Refer to [Create an API token](/en/airo/mcp/connect#create-an-api-token-for-airo-connect) for instructions.

## Connect with OAuth 2.0

Complete the following steps to connect Cursor to AIRO Connect using OAuth 2.0:

1. Open your Cursor MCP configuration file. Edit it directly for all projects, or use `.cursor/mcp.json` in a project root to scope the server to that project:
   
   - Mac and Linux: `~/.cursor/mcp.json`
   - Windows: `%USERPROFILE%\.cursor\mcp.json`
   
   You can also open the file from the **Customize** page in the Cursor desktop app by selecting **MCPs > + New MCP Server**.
   
2. Add the following configuration, using the [URL for your data center](/en/airo/mcp/connect#airo-connect-endpoint-urls-by-data-center):
   
   <api-code>

   ```json
   {
     "mcpServers": {
       "workato-airo-mcp-server": {
         "command": "npx",
         "args": [
           "-y",
           "mcp-remote",
           "https://YOUR_DATA_CENTER/airo_mcp"
         ]
       }
     }
   }
   ```

   </api-code>
   
   For example, on the US data center, the URL is `https://app.workato.com/airo_mcp`.
   
3. Save your changes.
   
4. Start a new chat with the Cursor agent.
   
   > **START A NEW CHAT**
   > 
   > Cursor agents only have access to the tools and capabilities available when a chat begins, so they can't detect a server added after a chat starts.
   
   > **RUN THE AGENT ON YOUR COMPUTER**
   > 
   > Select the option for your own computer, such as **This Mac**, instead of **Cloud** in the **Run on** menu.
   > 
   > ![The Cursor menu that sets where the agent runs, with This Mac selected](/assets/cursor-run-on-dropdown.w9BXchGR.png)_Select This Mac in the menu that sets where the agent runs_
   > 
   > This configuration runs a local `npx` command on your computer, which Cloud agents on a remote virtual machine can't use. The agent fails silently and can't discover the AIRO tools when **Cloud** is selected.
   
5. Sign in to Workato in the browser window that opens if prompted, then click **Authorize**.
   
6. Verify the connection. On the **Customize** page, select **MCPs** and confirm that the server appears with its tools and resources.
   
7. Prompt your Cursor agent to confirm that the server responds. For example, `List my Workato projects.`
   

Refer to [Cursor's MCP documentation](https://cursor.com/docs/mcp#using-mcpjson) for more configuration options.

## Connect with an API token

Complete the following steps to connect Cursor to AIRO Connect using an API token:

1. Open your Cursor MCP configuration file. Edit it directly for all projects, or use `.cursor/mcp.json` in a project root to scope the server to that project.
   
   - Mac and Linux: `~/.cursor/mcp.json`
   - Windows: `%USERPROFILE%\.cursor\mcp.json`
   
   You can also open the file from the **Customize** page in the Cursor desktop app by selecting **MCPs > + New MCP Server**.
   
2. Add the following configuration, using the [URL for your data center](/en/airo/mcp/connect#airo-connect-endpoint-urls-by-data-center) and replacing `<YOUR_API_TOKEN>` with the [API token you generated](/en/airo/mcp/connect#create-an-api-token-for-airo-connect):
   
   <api-code>

   ```json
   {
     "mcpServers": {
       "workato-airo-mcp-server": {
         "url": "https://YOUR_DATA_CENTER/airo_mcp",
         "headers": {
           "Authorization": "Bearer <YOUR_API_TOKEN>"
         }
       }
     }
   }
   ```

   </api-code>
   
   For example, on the US data center, the URL is `https://app.workato.com/airo_mcp`.
   
3. Save your changes.
   
4. Verify the connection. On the **Customize** page, select **MCPs** and confirm that the server appears with its tools and resources.
   
5. Start a new chat.
   
   > **START A NEW CHAT**
   > 
   > Cursor agents only have access to the tools and capabilities available when a chat begins, so they can't detect a server added after a chat starts.
   
   > **RUN THE AGENT ON YOUR COMPUTER**
   > 
   > Select the option for your own computer, such as **This Mac**, instead of **Cloud** in the **Run on** menu.
   > 
   > ![The Cursor menu that sets where the agent runs, with This Mac selected](/assets/cursor-run-on-dropdown.w9BXchGR.png)_Select This Mac in the menu that sets where the agent runs_
   > 
   > This configuration is saved in your local `mcp.json` file, which Cloud agents on a remote virtual machine can't access. The agent fails silently and can't discover the AIRO tools when **Cloud** is selected.
   > 
   > Cloud agents use servers added in the MCP drop-down menu at [cursor.com/agents](https://cursor.com/agents), or under **Plugins & MCPs** in the Cursor Team Dashboard. Refer to the Cursor [MCP tools](https://cursor.com/docs/cloud-agent/capabilities#mcp-tools) documentation for more information.
   
   Prompt your Cursor agent to confirm that the server responds. For example, `List my Workato projects.`
   

Refer to [Cursor's MCP documentation](https://cursor.com/docs/mcp#using-mcpjson) for more configuration options.

## Connect another workspace or environment

Add a separate AIRO Connect server entry to your client configuration for each workspace or environment you need to access at the same time, using a unique server name and a separate API token for every entry.

Cursor caches the OAuth sign-in by server URL rather than by server name, so separate OAuth 2.0 entries to the same AIRO Connect URL share one sign-in and can't provide simultaneous access to more than one workspace or environment.

Repeat the steps in [Connect with an API token](#connect-with-an-api-token), adding another entry under `mcpServers` with a different key name in place of `workato-airo-mcp-server` for each one.

---
