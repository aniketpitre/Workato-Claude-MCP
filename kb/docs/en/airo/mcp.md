---
url: 'https://docs.workato.com/en/airo/mcp.md'
description: >-
  Connect an MCP-compatible AI client to the AIRO MCP server with OAuth 2.0 or
  an API token to build and manage Workato assets in natural language.
---

# AIRO MCP server

The AIRO MCP server exposes Workato AIRO's full platform capabilities to MCP-compatible AI clients, including Claude Code, Claude Desktop, Cursor, ChatGPT, and Codex CLI. This enables you to build recipes, manage Genies, create MCP servers, and manage data table schema directly from your AI development environment using natural language.

![AIRO as an MCP server](/assets/airo-mcp.DZD5VIs5.gif)_AIRO as an MCP server_

## How it works

The AIRO MCP server supports two authentication methods:

- **OAuth 2.0**: Recommended for interactive clients. Your MCP client opens a browser window the first time you connect. The window displays Workato's authorization screen, which lists the permissions requested by the client. Click **Authorize** to complete the connection. Refer to [Connect using OAuth 2.0](#connect-using-oauth-2-0) for the setup steps.
- **API token**: Recommended for headless or configuration-driven setups. Pass a Workato API token as a bearer header. Refer to [Connect using an API token](#connect-using-an-api-token) for the setup steps.

The server exposes tools organized into the following categories:

| Category | What you can do |
| --- | --- |
| Recipes | Create, edit, search, and manage recipes, including step-level operations, field mapping, conditions, and connections |
| Skills and MCP | Convert recipes to skills and create or manage MCP servers |
| Custom connectors | Build, edit, and save custom connector SDK code |
| Genies and knowledge bases | Create and configure Genies, manage knowledge bases, and assign knowledge sources |
| Blueprints and assets | Work with blueprints, asset maps, and asset metadata |
| Data | Create and manage data table schema |
| Jobs and tests | Inspect job history and manage test cases |

The tools available to you depend on your workspace features and the identity the connection uses:

- **OAuth 2.0**: The server uses the permissions of the authenticated user.
- **API token**: The server uses the workspace owner's identity and permissions. The **AIRO MCP Server** permission on the API client role gives the token access to the server and all the tools available in your workspace. Other privileges assigned to the role and the API client's project access settings don't limit the token's access to tools or projects in the workspace.

The [activity audit log](/en/features/activity-audit-log#airo-attribution) attributes actions that the AIRO MCP server takes to the authenticated user for OAuth 2.0 connections, or to the workspace owner for API token connections, with a `(via AIRO)` label.

Agents call the `docs_get` tool to get instructions, per-tool guides, and a live index of the tools available to them. Prompt your MCP client to call `docs_get` when you need information about a specific tool.

## Prerequisites

You must have the following before you configure the AIRO MCP server:

- A Workato account with AIRO access
- An MCP-compatible client installed, such as Claude Code, Claude Desktop, Cursor, ChatGPT, or Codex CLI

Some MCP client configurations use `npx`. These configurations require [Node.js](https://nodejs.org/) to be installed and available in your `PATH`. Run `node -v` in your terminal to verify your installation.

API token authentication also requires a Workato API token. Refer to [Generate an API token](#generate-an-api-token) for instructions.

## Data center server URLs

The AIRO MCP server URL depends on the [data center](/en/datacenter/datacenter-overview) where your Workato workspace is hosted. Developer Sandbox workspaces use the trial URL. Use the server URL that matches your workspace region:

| Data center | AIRO MCP server URL |
| --- | --- |
| US | `https://app.workato.com/airo_mcp` |
| EU | `https://app.eu.workato.com/airo_mcp` |
| JP | `https://app.jp.workato.com/airo_mcp` |
| SG | `https://app.sg.workato.com/airo_mcp` |
| AU | `https://app.au.workato.com/airo_mcp` |
| IL | `https://app.il.workato.com/airo_mcp` |
| KR | `https://app.kr.workato.com/airo_mcp` |
| UK | `https://app.uk.workato.com/airo_mcp` |
| Developer Sandbox | `https://app.trial.workato.com/airo_mcp` |

The AIRO MCP server isn't available in the CN data center. Refer to [feature availability in the China data center](/en/datacenter/cn-data-center#feature-availability) for more information.

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This page provides general guidance for all Workato users. If you're a Virtual Private Workato (VPW) customer, refer to your private documentation for detailed configuration guidance specific to your instances.

## Connect using OAuth 2.0

Complete the following steps to connect the AIRO MCP server to your MCP client using OAuth 2.0:

> **WORKSPACE AND ENVIRONMENT SCOPE**
> 
> OAuth 2.0 scopes each AIRO MCP server connection to the Workato workspace and environment active in your browser session. Sign in to the target workspace and environment before you start authorization. Repeat the authorization steps for a different workspace or environment, or create a separate connection for each workspace and environment you need to access at the same time.

**Claude Code**

1. Open your terminal.
   
2. Run the following command to add the AIRO MCP server, using the [URL for your data center](#data-center-urls):
   
   <api-code>

   ```bash
   claude mcp add --transport http workato-airo-mcp-server https://YOUR_DATA_CENTER/airo_mcp
   ```

   </api-code>
   
   For example, on the US data center, the URL is `https://app.workato.com/airo_mcp`.
   
3. Run the following command to start a new Claude Code session and open the `/mcp` panel:
   
   ```bash
   claude /mcp
   ```
   
4. Use the arrow keys to select `workato-airo-mcp-server`, then press **Enter** to confirm.
   
5. Press **Enter** on **Authenticate**.
   
6. Click **Authorize** in the browser window that opens, then close the tab and return to Claude Code.
   
7. Verify the connection by running `/mcp` again. `workato-airo-mcp-server` should appear with a connected status.
   
8. Confirm the server responds by prompting Claude Code. For example, `List my Workato projects.`
   

Refer to [Claude Code's MCP documentation](https://code.claude.com/docs/en/mcp#installing-mcp-servers) for more configuration options.

**Claude Desktop**

1. Open Claude Desktop.
   
2. Go to **Settings > Developer** and click **Edit Config** to open `claude_desktop_config.json`. You can also open the file directly:
   
   - Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
3. Add the following configuration, using the [URL for your data center](#data-center-urls):
   
   <api-code>

   ```json
   {
     "mcpServers": {
       "workato-airo-mcp-server": {
         "command": "npx",
         "args": [
           "mcp-remote",
           "https://YOUR_DATA_CENTER/airo_mcp",
           "--transport",
           "http-first"
         ]
       }
     }
   }
   ```

   </api-code>
   
   For example, on the US data center, the URL is `https://app.workato.com/airo_mcp`.
   
4. Save your changes, restart Claude Desktop, and start a new chat.
   
5. Complete Workato authentication in the browser window that opens, then click **Authorize**. Check the MCP server status under **Settings > Developer** if the connection fails.
   
6. Confirm the server responds by prompting Claude. For example, `List my Workato projects.`
   

**Cursor**

1. Open your Cursor MCP configuration file. Edit it directly for all projects, or use `.cursor/mcp.json` in a project root to scope the server to that project.
   
   - Mac and Linux: `~/.cursor/mcp.json`
   - Windows: `%USERPROFILE%\.cursor\mcp.json`
   
   You can also open the file from the **Customize** page in the Cursor desktop app by selecting **MCPs > + New MCP Server**.
   
2. Add the following configuration, using the [URL for your data center](#data-center-urls):
   
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
   > Start a new chat with your agent after saving changes. Cursor agents only have access to the tools and capabilities available when a chat begins. Agents can't detect or use MCP configurations, servers, or tools added after a chat starts.
   
   > **RUN THE AGENT ON YOUR COMPUTER**
   > 
   > Select the option for your own computer, such as **This Mac**, instead of **Cloud** in the **Run on** menu.
   > 
   > ![The Cursor menu that sets where the agent runs, with This Mac selected](/assets/cursor-run-on-dropdown.w9BXchGR.png)_Select This Mac in the menu that sets where the agent runs_
   > 
   > This configuration runs a local `npx` command on your computer, which Cloud agents on a remote virtual machine can't use. The agent fails silently and can't discover the AIRO tools when **Cloud** is selected.
   
5. Complete Workato authentication in the browser window that opens, then click **Authorize**.
   
6. Verify the connection. On the **Customize** page, select **MCPs** and confirm that the server appears with its tools and resources.
   
7. Prompt your Cursor agent to confirm that the server responds. For example, `List my Workato projects.`
   

Refer to [Cursor's MCP documentation](https://cursor.com/docs/mcp#using-mcpjson) for more configuration options.

**ChatGPT**

ChatGPT requires **Developer mode** to connect to remote MCP servers. Developer mode grants ChatGPT read and write access to your AIRO tools. OpenAI classifies developer mode as an advanced feature with elevated risk, so refer to [their developer mode guide](https://developers.openai.com/api/docs/guides/developer-mode) for details before you enable it.

1. Sign in to ChatGPT on the web with a Pro, Plus, Business, Enterprise, or Education account. Developer mode isn't available in the desktop or mobile apps.
   
2. Go to **Settings > Security and login > Developer mode** and enable the **Developer mode** toggle.
   
3. Go to [ChatGPT Plugins](https://chatgpt.com/plugins) and click **+** to add a new plugin. This button appears after you turn on developer mode.
   
4. Enter `workato-airo-mcp-server` in the **Name** field.
   
5. Optional. Enter a description for your MCP server in the **Description** field.
   
6. Set the server URL to the following value in the **Connection** field, using the [URL for your data center](#data-center-urls):
   
   <api-code>

   ```text
   https://YOUR_DATA_CENTER/airo_mcp
   ```

   </api-code>
   
   For example, on the US data center, the URL is `https://app.workato.com/airo_mcp`.
   
7. Use the **Authentication** drop-down menu to select **OAuth**.
   
8. Select the **I understand and want to continue** checkbox, then click **Create**.
   
9. Click **Sign in with workato-airo-mcp-server** in the dialog that appears.
   
10. Complete Workato authentication in the browser window that opens, then click **Authorize**.
    
11. Verify the connection by trying the app in a new conversation.
    
    1. Open a new chat in ChatGPT.
       
    2. Click the **+** button near the message composer, then select your app from the list of available tools to add it to the conversation context.
       
    3. Prompt the model to use the app. For example, `List my Workato projects.`
       

**Codex CLI**

1. Open your terminal.
   
2. Add the AIRO MCP server, using the [URL for your data center](#data-center-urls):
   
   <api-code>

   ```bash
   codex mcp add workato-airo-mcp-server \
     --url https://YOUR_DATA_CENTER/airo_mcp
   ```

   </api-code>
   
   For example, on the US data center, the URL is `https://app.workato.com/airo_mcp`.
   
3. Codex may detect that the server supports OAuth and open the authorization flow automatically.
   
   If the browser doesn't open or the authorization flow doesn't start, run:
   
   ```bash
   codex mcp login workato-airo-mcp-server
   ```
   
4. Complete Workato authentication in the browser window that opens, then click **Authorize**.
   
5. Verify that the server is configured:
   
   ```bash
   codex mcp list
   ```
   
   The output should include `workato-airo-mcp-server`.
   
6. Start a new Codex session so the MCP server and its tools are initialized:
   
   ```bash
   codex
   ```
   
   Inside Codex, enter `/mcp` to inspect the active MCP servers.
   
7. Confirm the server responds by prompting Codex. For example, `List my Workato projects.`
   

Refer to [Codex's MCP documentation](https://developers.openai.com/codex/extend/mcp) for more configuration options.

## Connect using an API token

API token authentication requires a Workato API token.

> **API TOKENS HAVE FULL WORKSPACE ACCESS**
> 
> Connections that authenticate with an API token perform actions with the workspace owner's identity and permissions. The **AIRO MCP Server** permission on the client role gives access to the server and all the tools available in your workspace. The role's other privileges and the API client's project access settings don't apply, so the MCP client can access every project in the workspace. Connect using [OAuth 2.0](#connect-using-oauth-2-0) to limit what an MCP client can access.

### Generate an API token

Complete the following steps to obtain an API token:

1. Sign in to Workato.
   
2. Go to **Workspace admin > API clients > Client roles**.
   
3. Open an existing client role or [create a client role](/en/workato-api/api-clients#create-a-client-role).
   
4. Go to the **Tools** tab.
   
5. Select the **AIRO MCP Server** checkbox in the **AIRO MCP tools** section.
   
   ![The AIRO MCP Server checkbox selected in the AIRO MCP tools section of a client role](/assets/client-role.4UySQl_y.png)_Select AIRO MCP Server on the Tools tab of the client role_
   
6. Click **Save changes**.
   
7. Assign this client role to an existing API client, or select the role when you [create a new API client](/en/workato-api/api-clients#create-an-api-client).
   
8. Copy and securely store the API client token.
   

### Configure your MCP client

Complete the steps for your MCP client:

**Claude Code**

1. Open your terminal.
   
2. Add the following line to your shell profile (`~/.zshrc`, `~/.bash_profile`, or equivalent), replacing `<YOUR_API_TOKEN>` with the token you generated:
   
   ```bash
   export WORKATO_API_TOKEN="<YOUR_API_TOKEN>"
   ```
   
3. Restart your terminal, or reload your profile:
   
   ```bash
   source ~/.zshrc  # or your shell's profile file
   ```
   
4. Add the server, using the [URL for your data center](#data-center-urls) and referencing the environment variable in the authorization header:
   
   <api-code>

   ```bash
   claude mcp add --transport http workato-airo-mcp-server https://YOUR_DATA_CENTER/airo_mcp \
     --header 'Authorization: Bearer ${WORKATO_API_TOKEN}'
   ```

   </api-code>
   
   For example, on the US data center, the URL is `https://app.workato.com/airo_mcp`.
   
   Use single quotes around the header. This stores the literal `${WORKATO_API_TOKEN}` reference in your configuration, and Claude Code expands it when it connects.
   
5. Run the following command to start a new Claude Code session and open the `/mcp` panel:
   
   ```bash
   claude /mcp
   ```
   
   `workato-airo-mcp-server` should appear with a connected status.
   
6. Confirm the server responds by prompting Claude Code. For example, `List my Workato projects.`
   

Refer to [Claude Code's MCP documentation](https://code.claude.com/docs/en/mcp#installing-mcp-servers) for more configuration options.

**Claude Desktop**

1. Open Claude Desktop.
   
2. Go to **Settings > Developer** and click **Edit Config** to open `claude_desktop_config.json`. You can also open the file directly:
   
   - Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
3. Add the following configuration, using the [URL for your data center](#data-center-urls) and replacing `<YOUR_API_TOKEN>` with the token you generated:
   
   <api-code>

   ```json
   {
     "mcpServers": {
       "workato-airo-mcp-server": {
         "command": "npx",
         "args": [
           "mcp-remote",
           "https://YOUR_DATA_CENTER/airo_mcp",
           "--transport",
           "http-first",
           "--header",
           "Authorization:${AUTH_HEADER}"
         ],
         "env": {
           "AUTH_HEADER": "Bearer <YOUR_API_TOKEN>"
         }
       }
     }
   }
   ```

   </api-code>
   
   For example, on the US data center, the URL is `https://app.workato.com/airo_mcp`.
   
4. Save your changes.
   
5. Restart Claude Desktop and start a new chat. Check the MCP server status under **Settings > Developer** if the connection fails.
   
6. Confirm the server responds by prompting Claude. For example, `List my Workato projects.`
   

**Cursor**

1. Open your Cursor MCP configuration file. Edit it directly for all projects, or use `.cursor/mcp.json` in a project root to scope the server to that project.
   
   - Mac and Linux: `~/.cursor/mcp.json`
   - Windows: `%USERPROFILE%\.cursor\mcp.json`
   
   You can also open the file from the **Customize** page in the Cursor desktop app by selecting **MCPs > + New MCP Server**.
   
2. Add the following configuration, using the [URL for your data center](#data-center-urls) and replacing `<YOUR_API_TOKEN>` with the token you generated:
   
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
   
5. Start a new chat and prompt your Cursor agent to confirm that the server responds. For example, `List my Workato projects.`
   
   > **START A NEW CHAT**
   > 
   > Start a new chat with your agent after saving changes. Cursor agents only have access to the tools and capabilities available when a chat begins. Agents can't detect or use MCP configurations, servers, or tools added after a chat starts.
   
   > **RUN THE AGENT ON YOUR COMPUTER**
   > 
   > Select the option for your own computer, such as **This Mac**, instead of **Cloud** in the **Run on** menu.
   > 
   > ![The Cursor menu that sets where the agent runs, with This Mac selected](/assets/cursor-run-on-dropdown.w9BXchGR.png)_Select This Mac in the menu that sets where the agent runs_
   > 
   > This configuration is saved in your local `mcp.json` file, which Cloud agents on a remote virtual machine can't access. The agent fails silently and can't discover the AIRO tools when **Cloud** is selected.
   > 
   > Cloud agents use servers added in the MCP drop-down menu at [cursor.com/agents](https://cursor.com/agents), or under **Plugins & MCPs** in the Cursor Team Dashboard. Refer to the Cursor [MCP tools](https://cursor.com/docs/cloud-agent/capabilities#mcp-tools) documentation for more information.
   

Refer to [Cursor's MCP documentation](https://cursor.com/docs/mcp#using-mcpjson) for more configuration options.

**ChatGPT**

ChatGPT requires **Developer mode** to connect to remote MCP servers. Developer mode grants ChatGPT read and write access to your AIRO tools. OpenAI classifies developer mode as an advanced feature with elevated risk, so refer to [their developer mode guide](https://developers.openai.com/api/docs/guides/developer-mode) for details before you enable it.

1. Sign in to ChatGPT on the web with a Pro, Plus, Business, Enterprise, or Education account. Developer mode isn't available in the desktop or mobile apps.
   
2. Go to **Settings > Security and login > Developer mode** and enable the **Developer mode** toggle.
   
3. Go to [ChatGPT Plugins](https://chatgpt.com/plugins) and click **+** to add a new plugin. This button appears after you turn on developer mode.
   
4. Enter `workato-airo-mcp-server` in the **Name** field.
   
5. Optional. Enter a description for your MCP server in the **Description** field.
   
6. Set the server URL to the following value in the **Connection** field, using the [URL for your data center](#data-center-urls):
   
   <api-code>

   ```text
   https://YOUR_DATA_CENTER/airo_mcp
   ```

   </api-code>
   
   For example, on the US data center, the URL is `https://app.workato.com/airo_mcp`.
   
7. Use the **Authentication** drop-down menu to select **Access token / API key**.
   
8. Use the **Header scheme** drop-down menu to select **Bearer**.
   
9. Select the **I understand and want to continue** checkbox, then click **Create**.
   
10. Enter your API token in the **Enter access token or API key** field, then click **Connect**.
    
11. Verify the connection by trying the app in a new conversation.
    
    1. Open a new chat in ChatGPT.
       
    2. Click the **+** button near the message composer, then select your app from the list of available tools to add it to the conversation context.
       
    3. Prompt the model to use the app. For example, `List my Workato projects.`
       

**Codex CLI**

1. Open your terminal.
   
2. Add the following line to your shell profile (`~/.zshrc`, `~/.bashrc`, `~/.bash_profile`, or equivalent), replacing `<YOUR_API_TOKEN>` with your Workato API token:
   
   ```bash
   export WORKATO_API_TOKEN="<YOUR_API_TOKEN>"
   ```
   
3. Reload your shell profile:
   
   ```bash
   source ~/.zshrc  # Replace with the profile file you edited
   ```
   
4. Optional. Confirm that the environment variable is available without displaying the token:
   
   ```bash
   test -n "$WORKATO_API_TOKEN" && echo "WORKATO_API_TOKEN is set"
   ```
   
5. Add the AIRO MCP server, using the [URL for your data center](#data-center-urls) and referencing the environment variable that contains the bearer token:
   
   <api-code>

   ```bash
   codex mcp add workato-airo-mcp-server \
     --url https://YOUR_DATA_CENTER/airo_mcp \
     --bearer-token-env-var WORKATO_API_TOKEN
   ```

   </api-code>
   
   For example, on the US data center, the URL is `https://app.workato.com/airo_mcp`.
   
   The `--bearer-token-env-var` option stores the environment variable's name in the Codex configuration, not the token itself.
   
6. Verify that the server is configured:
   
   ```bash
   codex mcp list
   ```
   
   The output should include `workato-airo-mcp-server`.
   
7. Start a new Codex session so the newly configured MCP server is initialized:
   
   ```bash
   codex
   ```
   
   Inside Codex, enter `/mcp` to inspect the active MCP servers.
   
8. Confirm the server responds by prompting Codex. For example, `List my Workato projects.`
   

Refer to [Codex's MCP documentation](https://developers.openai.com/codex/extend/mcp) for more configuration options.

### Connect to multiple workspaces or environments

You can connect to multiple Workato workspaces or environments by adding a separate server entry to your MCP configuration for each connection. Use a unique server name and API token for every entry.

Each API client is assigned to one [environment](/en/workato-api/api-clients#create-an-api-client) in workspaces with environments enabled. Its API token works only with that environment.

For example, the following Claude Desktop configuration uses the [URL for your data center](#data-center-urls) to connect to the Development and Production environments in the same workspace:

<api-code>

```json
{
  "mcpServers": {
    "workato-airo-mcp-server-dev": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://YOUR_DATA_CENTER/airo_mcp",
        "--transport",
        "http-first",
        "--header",
        "Authorization:${AUTH_HEADER}"
      ],
      "env": {
        "AUTH_HEADER": "Bearer <DEV_API_TOKEN>"
      }
    },
    "workato-airo-mcp-server-prod": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://YOUR_DATA_CENTER/airo_mcp",
        "--transport",
        "http-first",
        "--header",
        "Authorization:${AUTH_HEADER}"
      ],
      "env": {
        "AUTH_HEADER": "Bearer <PROD_API_TOKEN>"
      }
    }
  }
}
```

</api-code>

For example, on the US data center, the URL is `https://app.workato.com/airo_mcp` for both server entries above.

The other MCP clients use the same approach: repeat the setup steps with a distinct server name and token for each connection.

## Use cases

The following examples demonstrate common workflows with the AIRO MCP server.

### Build and test a recipe

Use AIRO to create a multi-step recipe from a natural language description, then save and test it without leaving your development environment.

```
Create a recipe that syncs new Salesforce opportunities to Jira issues.
Add an OpenAI step to summarize the opportunity before creating the Jira issue.
Save the recipe and show me the test cases.
```

### Create a genie with knowledge sources

Set up a genie and connect it to relevant knowledge bases so it can answer domain-specific questions.

```
Create a new genie called "Sales Intelligence" and assign the CRM knowledge base to it.
```

### Build an MCP server

Create an MCP server from your workspace assets so other AI clients can connect to your tools.

```
Build an MCP server called "Sales Tools" using the lead enrichment and deal scoring skills from the Sales Automation project.
```

### Investigate job failures

Inspect recent job history to diagnose errors in production recipes. The agent calls `job_list` to find a failed job, then `job_get` to analyze the job's status and suggest a fix for the recipe.

```
List the last 10 jobs for recipe 1555928 and show me any errors.
```

### Manage a data table

Create a data table and define its schema without leaving your development environment.

```
Create a data table to store approver thresholds by region.
```

### Build a custom connector

Build a connector for an API that isn't available as a platform connector, using your own development environment instead of the Workato SDK editor.

```
Build a connector for the National Weather Service API at https://www.weather.gov/documentation/services-web-api.
Add an action that retrieves active weather alerts for a state or territory.
```

Refer to [Build custom connectors with AIRO MCP](/en/airo/build/custom-connectors) for the full workflow, including how saving and releasing changes work.

---
