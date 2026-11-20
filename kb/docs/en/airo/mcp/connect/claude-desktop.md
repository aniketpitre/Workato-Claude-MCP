---
url: 'https://docs.workato.com/en/airo/mcp/connect/claude-desktop.md'
description: Set up AIRO Connect in Claude Desktop with OAuth 2.0 or an API token.
---

# Set up AIRO Connect in Claude Desktop

You can set up AIRO Connect in Claude Desktop using OAuth 2.0 or an API token.

## Before you begin

You need a Workato account with AIRO access and Claude Desktop installed. These configurations use `npx`, which requires [Node.js](https://nodejs.org/) to be installed and available in your `PATH`. Run `node -v` in your terminal to verify your installation.

API token authentication also requires a Workato API token. Refer to [Create an API token](/en/airo/mcp/connect#create-an-api-token-for-airo-connect) for instructions.

## Connect with OAuth 2.0

Complete the following steps to connect Claude Desktop to AIRO Connect using OAuth 2.0:

1. Open Claude Desktop.
   
2. Go to **Settings > Desktop app > Extensions** and click **Edit config** to open `claude_desktop_config.json`. You can also open the file directly:
   
   - Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
3. Add the following configuration, using the [URL for your data center](/en/airo/mcp/connect#airo-connect-endpoint-urls-by-data-center):
   
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
   
5. Sign in to Workato in the browser window that opens if prompted, then click **Authorize**.
   
6. Confirm the server responds by prompting Claude. For example, `List my Workato projects.`
   

## Connect with an API token

Complete the following steps to connect Claude Desktop to AIRO Connect using an API token:

1. Open Claude Desktop.
   
2. Go to **Settings > Desktop app > Extensions** and click **Edit config** to open `claude_desktop_config.json`. You can also open the file directly:
   
   - Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
3. Add the following configuration, using the [URL for your data center](/en/airo/mcp/connect#airo-connect-endpoint-urls-by-data-center) and replacing `<YOUR_API_TOKEN>` with the [API token you generated](/en/airo/mcp/connect#create-an-api-token-for-airo-connect):
   
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
   
5. Restart Claude Desktop and start a new chat.
   
6. Confirm the server responds by prompting Claude. For example, `List my Workato projects.`
   

## Connect another workspace or environment

Add a separate AIRO Connect server entry to your client configuration for each workspace or environment you need to access at the same time, using a unique server name and a separate API token for every entry.

Claude Desktop caches the OAuth sign-in by server URL rather than by server name, so separate OAuth 2.0 entries to the same AIRO Connect URL share one sign-in and can't provide simultaneous access to more than one workspace or environment.

For example, the following configuration uses an API token and the [URL for your data center](/en/airo/mcp/connect#airo-connect-endpoint-urls-by-data-center) to connect to the Development and Production environments in the same workspace:

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

For example, on the US data center, the URL is `https://app.workato.com/airo_mcp` for both of the preceding server entries.

---
