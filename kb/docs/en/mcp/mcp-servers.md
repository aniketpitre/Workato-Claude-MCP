---
url: 'https://docs.workato.com/en/mcp/mcp-servers.md'
description: >-
  MCP servers expose your API recipe and AI gateway collections to AI agents as
  tools through authenticated, cloud-based Model Context Protocol URLs.
---

# MCP servers

MCP servers enable you to expose endpoints to AI agents as tools or sets of tools through a remote, cloud-based [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) server. Your API recipe collections and AI gateway collections generate unique, authenticated MCP URLs. You can add this MCP URL to your LLM settings to enable an AI agent to use your API endpoint collection to answer user prompts.

Watch a quick video guide: Getting started with MCP and Workato

[Video](https://www.youtube.com/embed/xwxL47rHhfs?rel=0&si=-ujcTLN91wOvADU4)

> **FEATURE AVAILABILITY**
> 
> MCP is available to all users in the US, EU, AU, JP, SG, IL, KR, and UK data centers. MCP servers are hosted in the US, EU, and APAC regions and respect data residency requirements where possible. MCP isn't available to workspaces in the CN data center. This reflects local regulatory requirements and Workato's commitment to data sovereignty and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.
> 
> Contact your Customer Success representative if you're interested in using MCP or require additional information.

## Create an MCP server

You can create an MCP server and add tools in the AI Hub.

> **NEED AN EXAMPLE?**
> 
> Review the [LLM, GitHub, and Workato Developer API](/en/getting-started/use-cases/mcp/github-developer-api-llm) use case for steps to create an MCP server integration that lets you create GitHub issues with natural-language commands in ChatGPT, Claude, or Cursor.

Watch a quick video guide: Search for leads in Salesforce with MCP

[Video](https://www.youtube.com/embed/eO-nG_q0woQ?rel=0&si=EDnWwRm7-T4dsykV)

### Create an MCP server with project assets

Complete the following steps to create an MCP server with project assets:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers** and click **\+ Create an MCP server**. Alternatively, you can create an MCP server from the **Projects** page by clicking **Create > MCP server** or pressing C+M.
   
3. Go to the **Start from scratch** section and click **New MCP server**. Refer to [Use a prebuilt MCP server](/en/mcp/prebuilt-mcps#use-a-prebuilt-mcp-server) if you plan to use a prebuilt MCP server template.
   
4. Select **Project assets** as your tool source.
   
   ![Select Project assets](/assets/project-assets.B_gBtpgE.png)_Select **Project assets**_
   
5. Use the **Project** drop-down menu to select the project where you plan to store the MCP server.
   
6. Select the tools you plan to use.
   
7. Enter a name for your MCP server in the **Server name** field.
   
8. Optional. Enter instructions for the LLM to understand the purpose and goals for the MCP server in the **Server instruction** field.
   
9. Click **Create MCP Server**. The MCP server tools, description, remote MCP URL, and additional server information displays in the **Details** tab.
   
   ![MCP server Details tab](/assets/mcp-tools-overview-page.2Q5AxJ3t.png)_MCP server **Details** tab admin view_
   

### Create an MCP server with an API collection

Complete the following steps to create an MCP with an API collection:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers** and click **\+ Create an MCP server**. Alternatively, you can create an MCP server from the **Projects** page by clicking **Create > MCP server** or pressing C+M.
   
3. Go to the **Start from scratch** section and click **New MCP server**. Refer to [Use a prebuilt MCP server](/en/mcp/prebuilt-mcps#use-a-prebuilt-mcp-server) if you plan to use a prebuilt MCP server template.
   
4. Select **API collection** as your tool source.
   
   ![Select API collection](/assets/api-collection.CGQye9Bl.png)_Select **API collection**_
   
5. Select the API collection you plan to use.
   
6. Enter a name for your MCP server in the **Server name** field.
   
7. Use the **Location to save this server** drop-down menu to select the project that contains the assets you plan to use for the MCP server, such as skills or API recipes.
   
   > **MCP SERVER ASSETS MUST BE IN THE SAME PROJECT**
   > 
   > You must store all assets in the same project folder. Error messages display if you select an unsupported asset type.
   
8. Optional. Enter instructions for the LLM to understand the purpose and goals for the MCP server in the **Server instruction** field.
   
9. Click **Create MCP Server**. The MCP server tools, description, remote MCP URL, and additional server information displays in the **Details** tab.
   
   ![MCP server Details tab](/assets/mcp-tools-overview-page.2Q5AxJ3t.png)_MCP server **Details** tab admin view_
   

### Create a proxy for external MCP servers

Complete the following steps to create a proxy MCP server:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers** and click **\+ Create an MCP server**. Alternatively, you can create an MCP server from the **Projects** page by clicking **Create > MCP server** or pressing C+M.
   
3. Go to the **Start from scratch** section and click **New MCP server**. Refer to [Use a prebuilt MCP server](/en/mcp/prebuilt-mcps#use-a-prebuilt-mcp-server) if you plan to use a prebuilt MCP server template.
   
4. Select **External MCP Server** as your tool source.
   
   ![Select External MCP Server](/assets/tool-source.B9il0kEF.png)_Select **External MCP Server**_
   
5. Enter your proxy MCP server URL in the **External MCP server URL** field.
   
6. Use the **Authentication Type** drop-down menu to select the authentication method you plan to use:
   
   OAuth 2.0
   
   #### OAuth 2.0
   
   1. Select **OAuth 2.0**.
      
   2. Optional. Expand **Custom Headers** and click **Add header** if you plan to use custom headers.
      
   3. Optional. Expand **Custom Query Parameters** and click **Add query parameter** if you plan to add query parameters to every request URL.
      
   4. Click **Connect**.
      
      > **OAUTH CLIENT ID METADATA DOCUMENT SUPPORT (CIMD)**
      > 
      > Workato registers itself with the external server's authorization server automatically. Dynamic client registration (RFC 7591) is used when available. Otherwise Workato provides the OAuth Client ID Metadata Document hosted URL for the authorization server to fetch.
      
   
   API Key (Header)
   
   #### API key header
   
   1. Select **API Key (Header)**.
      
   2. Enter the API key in the **API Key** field.
      
   3. Enter the header name in the **Custom Header Name** field. Defaults to `X-API-Key`.
      
   4. Optional. Expand **Custom Headers** and click **Add header** if you plan to use custom headers.
      
   5. Optional. Expand **Custom Query Parameters** and click **Add query parameter** if you plan to add query parameters to every request URL.
      
   6. Click **Connect**.
      
   
   API Key (Query Parameter)
   
   #### API key query parameter
   
   1. Select **API Key (Query Parameter)**.
      
   2. Enter the API key in the **API Key** field.
      
   3. Optional. Enter a name for the API key in the **Query Parameter Name** field. Defaults to `api_key`.
      
   4. Optional. Expand **Custom Headers** and click **Add header** if you plan to use custom headers.
      
   5. Optional. Expand **Custom Query Parameters** and click **Add query parameter** if you plan to add query parameters to every request URL.
      
   6. Click **Connect**.
      
   
   Bearer Token
   
   #### Bearer token
   
   1. Select **Bearer Token**.
      
   2. Enter the bearer token in the **Bearer Token** field.
      
   3. Optional. Expand **Custom Headers** and click **Add header** if you plan to use custom headers.
      
   4. Optional. Expand **Custom Query Parameters** and click **Add query parameter** if you plan to add query parameters to every request URL.
      
   5. Click **Connect**.
      
   
   OAuth 2.0 with Client Registration
   
   #### OAuth 2.0 with client registration
   
   1. Optional. Expand **Custom Headers** and click **Add header** if you plan to use custom headers.
      
   2. Optional. Expand **Custom Query Parameters** and click **Add query parameter** if you plan to add query parameters to every request URL.
      
   3. Select **OAuth 2.0 with Client Registration**.
      
   4. Enter your client ID in the **OAuth Client ID** field.
      
   5. Optional. Enter your client secret in the **OAuth Client Secret** field.
      
   6. Optional. Enter the OAuth scope you plan to use in the **OAuth Scopes** field. Scopes must be space separated.
      
   7. Optional. Enter the OAuth authorization endpoint in the **OAuth Authorization Endpoint** field. Defaults to `{server_url}/oauth/authorize`.
      
   8. Optional. Enter the OAuth token endpoint in the **OAuth Token Endpoint** field. Defaults to `{server_url}/oauth/token`.
      
   9. Click **Connect**.
      
   
   No Authentication
   
   #### No authentication
   
   1. Select **No Authentication**.
      
   2. Optional. Expand **Custom Headers** and click **Add header** if you plan to use custom headers.
      
   3. Optional. Expand **Custom Query Parameters** and click **Add query parameter** if you plan to add query parameters to every request URL.
      
   4. Click **Connect**.
      
   
7. Enter a name for the MCP server in the **Server name** field.
   
8. Use the **Location to save this server** drop-down menu to select the project that contains the assets, such as skills or API recipes, that you plan to use for your MCP server.
   
   > **MCP SERVER ASSETS MUST BE IN THE SAME PROJECT**
   > 
   > You must store all assets in the same project folder. Error messages display if you select an unsupported asset type.
   
9. Click **Create MCP Server**. The MCP server tools, description, remote MCP URL, and additional server information displays in the **Details** tab.
   
   ![MCP server Details tab](/assets/mcp-tools-overview-page.2Q5AxJ3t.png)_MCP server **Details** tab admin view_

---
