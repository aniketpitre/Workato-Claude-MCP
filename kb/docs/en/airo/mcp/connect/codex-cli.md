---
url: 'https://docs.workato.com/en/airo/mcp/connect/codex-cli.md'
description: Set up AIRO Connect in Codex CLI with OAuth 2.0 or an API token.
---

# Set up AIRO Connect in Codex CLI

You can set up AIRO Connect in Codex CLI using OAuth 2.0 or an API token.

## Before you begin

You need a Workato account with AIRO access and Codex CLI installed. API token authentication also requires a Workato API token. Refer to [Create an API token](/en/airo/mcp/connect#create-an-api-token-for-airo-connect) for instructions.

## Connect with OAuth 2.0

Complete the following steps to connect Codex CLI to AIRO Connect using OAuth 2.0:

1. Open your terminal.
   
2. Add AIRO Connect, using the [URL for your data center](/en/airo/mcp/connect#airo-connect-endpoint-urls-by-data-center):
   
   <api-code>

   ```bash
   codex mcp add workato-airo-mcp-server \
     --url https://YOUR_DATA_CENTER/airo_mcp
   ```

   </api-code>
   
   For example, on the US data center, the URL is `https://app.workato.com/airo_mcp`.
   
3. Sign in to Workato in the browser window that opens if prompted, then click **Authorize**. If the browser doesn't open or the authorization flow doesn't start, run `codex mcp login workato-airo-mcp-server`.
   
4. Verify that the server is configured:
   
   ```bash
   codex mcp list
   ```
   
   The output should include `workato-airo-mcp-server`.
   
5. Start a new Codex session so the MCP server and its tools are initialized:
   
   ```bash
   codex
   ```
   
   Inside Codex, enter `/mcp` to inspect the active MCP servers.
   
6. Confirm the server responds by prompting Codex. For example, `List my Workato projects.`
   

Refer to [Codex's MCP documentation](https://developers.openai.com/codex/extend/mcp) for more configuration options.

## Connect with an API token

Complete the following steps to connect Codex CLI to AIRO Connect using an API token:

1. Open your terminal.
   
2. Add the following line to your shell profile (`~/.zshrc`, `~/.bashrc`, `~/.bash_profile`, or equivalent), replacing `<YOUR_API_TOKEN>` with the [API token you generated](/en/airo/mcp/connect#create-an-api-token-for-airo-connect):
   
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
   
5. Add AIRO Connect, using the [URL for your data center](/en/airo/mcp/connect#airo-connect-endpoint-urls-by-data-center) and referencing the environment variable that contains the bearer token:
   
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

## Connect another workspace or environment

Add a separate AIRO Connect server entry to your client configuration for each workspace or environment you need to access at the same time, using a unique server name and a separate API token for every entry.

Repeat the steps in [Connect with an API token](#connect-with-an-api-token), using a different server name in place of `workato-airo-mcp-server` and a different environment variable name in place of `WORKATO_API_TOKEN` for each entry.

---
