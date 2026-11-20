---
url: 'https://docs.workato.com/en/airo/mcp/connect/chatgpt.md'
description: Set up AIRO Connect in ChatGPT with OAuth 2.0.
---

# Set up AIRO Connect in ChatGPT

You can set up AIRO Connect in ChatGPT as a custom MCP plugin using OAuth 2.0.

## Before you begin

You need the following:

- A Workato account with AIRO access.
- Access to ChatGPT Plugins on ChatGPT web.

Workspace permissions and security restrictions can limit who can add or use custom MCP plugins. Refer to the OpenAI [Add custom MCP server](https://developers.openai.com/api/docs/guides/custom-mcp-server) documentation for current ChatGPT requirements and controls.

> **REVIEW TOOL-CALL CONFIRMATIONS**
> 
> AIRO Connect can give ChatGPT read and write tools. Review the information you share and each tool-call confirmation before allowing ChatGPT to take action.

## Add AIRO Connect as a plugin

Complete the following steps to connect ChatGPT to AIRO Connect using OAuth 2.0:

1. Open ChatGPT on the web.
   
2. Go to [ChatGPT Plugins](https://chatgpt.com/plugins).
   
3. Select **+**, then select **Add custom MCP server**.
   
4. Enter **AIRO Connect** in the **Name** field.
   
5. Optional. Enter a description for the plugin.
   
6. Enter the following server URL in the **Connection** field, using the [URL for your data center](/en/airo/mcp/connect#airo-connect-endpoint-urls-by-data-center):
   
   <api-code>

   ```text
   https://YOUR_DATA_CENTER/airo_mcp
   ```

   </api-code>
   
   For example, on the US data center, the URL is `https://app.workato.com/airo_mcp`.
   
7. Select **OAuth** in the **Authentication** field.
   
8. Review the risk warning, select **I understand and want to continue**, then select **Create as a plugin**.
   
9. Sign in to Workato and select **Authorize** when prompted.
   
10. Open the newly created plugin and select **Install**.
    

## Use AIRO Connect in a conversation

Complete the following steps to use AIRO Connect in a conversation:

1. Open a new Work chat in ChatGPT.
   
2. In the prompt box, type **@**, then select **AIRO Connect**.
   
3. Prompt ChatGPT to use AIRO Connect. For example:
   
   ```text
   List my Workato projects.
   ```
   

## Connect another workspace or environment

Create a separate AIRO Connect plugin for each additional Workato workspace or environment. Use a distinct name for each plugin, such as **AIRO Connect (Development)** and **AIRO Connect (Production)**.

Sign in to the workspace and environment the new plugin should access, then repeat the steps in [Add AIRO Connect as a plugin](#add-airo-connect-as-a-plugin).

---
