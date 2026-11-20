---
url: 'https://docs.workato.com/en/airo/mcp/connect/claude-code.md'
description: Set up AIRO Connect in Claude Code with OAuth 2.0 or an API token.
---

# Set up AIRO Connect in Claude Code

You can set up AIRO Connect in Claude Code using OAuth 2.0 or an API token.

## Before you begin

You need a Workato account with AIRO access and Claude Code installed. API token authentication also requires a Workato API token. Refer to [Create an API token](/en/airo/mcp/connect#create-an-api-token-for-airo-connect) for instructions.

## Connect with OAuth 2.0

Complete the following steps to connect Claude Code to AIRO Connect using OAuth 2.0:

1. Open your terminal.
   
2. Run the following command to add AIRO Connect, using the [URL for your data center](/en/airo/mcp/connect#airo-connect-endpoint-urls-by-data-center):
   
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

## Connect with an API token

Complete the following steps to connect Claude Code to AIRO Connect using an API token:

1. Open your terminal.
   
2. Add the following line to your shell profile (`~/.zshrc`, `~/.bash_profile`, or equivalent), replacing `<YOUR_API_TOKEN>` with the [API token you generated](/en/airo/mcp/connect#create-an-api-token-for-airo-connect):
   
   ```bash
   export WORKATO_API_TOKEN="<YOUR_API_TOKEN>"
   ```
   
3. Restart your terminal, or reload your profile:
   
   ```bash
   source ~/.zshrc  # or your shell's profile file
   ```
   
4. Add the server, using the [URL for your data center](/en/airo/mcp/connect#airo-connect-endpoint-urls-by-data-center) and referencing the environment variable in the authorization header:
   
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

## Connect another workspace or environment

Add a separate AIRO Connect server entry to your client configuration for each workspace or environment you need to access at the same time, using a unique server name and a separate API token for every entry.

Claude Code caches the OAuth sign-in by server URL rather than by server name, so separate OAuth 2.0 entries to the same AIRO Connect URL share one sign-in and can't provide simultaneous access to more than one workspace or environment.

Repeat the steps in [Connect with an API token](#connect-with-an-api-token), using a different server name in place of `workato-airo-mcp-server` and a different environment variable name in place of `WORKATO_API_TOKEN` for each entry.

---
