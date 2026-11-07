---
url: 'https://docs.workato.com/en/mcp/remote-mcp-servers.md'
description: >-
  Learn how remote MCP servers are hosted externally to serve multiple users and
  AI platforms, and install one with a URL or Workato Identity.
---

# Remote MCP servers

Remote Model Context Protocol (MCP) servers are hosted externally and accessed by AI assistants over the network instead of running tools and integrations locally. This means a single MCP server can serve multiple users and multiple AI platforms, such as Claude, ChatGPT, Microsoft Copilot, or Cursor. You can update and maintain remote MCP servers centrally without requiring changes to your client configurations.

> **FEATURE AVAILABILITY**
> 
> MCP is available to all users in the US, EU, AU, JP, SG, IL, KR, and UK data centers. MCP servers are hosted in the US, EU, and APAC regions and respect data residency requirements where possible. MCP isn't available to workspaces in the CN data center. This reflects local regulatory requirements and Workato's commitment to data sovereignty and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.
> 
> Contact your Customer Success representative if you're interested in using MCP or require additional information.

## Install remote MCP servers

You can install a remote MCP with a URL that authenticates with a token or through [Workato Identity](/en/workato-identity) after you [create an MCP server](/en/mcp/mcp-servers#create-an-mcp-server). The configurations in this section use Cursor and Claude Desktop.

> **NEED AN EXAMPLE?**
> 
> Review the [LLM, GitHub, and Workato Developer API](/en/getting-started/use-cases/mcp/github-developer-api-llm) use case for steps to create an MCP server integration that lets you create GitHub issues with natural-language commands in ChatGPT, Claude, or Cursor.

Complete the following steps to install the MCP remote server with a URL:

1. Sign in to Workato.
   
2. Configure your MCP integration:
   
   **Cursor token authentication**
   
   ### Cursor MCP remote server configuration with token authentication
   
   Complete the following steps to configure an MCP integration in Cursor that authenticates using a token:
   
   1. Go to **AI Hub > Enterprise MCP > Custom servers**.
      
   2. Click the MCP server you plan to use for your MCP remote server integration.
      
   3. Click **Settings > End user access**.
      
   4. Go to the **Access Method** section and ensure that **Token-based access** is selected.
      
   5. Go to the **Developer MCP Token** section and click **Copy**.
      
      ![Copy the MCP URL and token](/assets/copy-developer-mcp-token.Chp0BlZi.png)_Copy the MCP URL and token_
      
   6. Sign in to Cursor.
      
   7. Go to **Settings > Cursor settings**.
      
   8. Click **MCP & Integrations** in the sidebar.
      
   9. Click **\+ New MCP Server** to open the `mcp.json` file.
      
      ![New MCP server](/assets/configure-cursor.DhhCFK4N.png)_Click **\+ New MCP Server**_
      
   10. Update the configuration to use the MCP URL and token you copied in the preceding steps. Your MCP URL must begin with `https`. For example:
       
       ```json
       
       {
         "mcpServers": {
           "github-tools": {
             "url": "https://387.apim.mcp.workato.com/abc247/example-collection-name-v1?wkt_token=YOUR_API_TOKEN"
           }
         }
       }
       ```
       
   11. Save your changes.
       
   12. Create a new chat with your Cursor agent to use the tools you added.
       
       You must start a new chat with your agent. Cursor agents only have access to the tools and capabilities available when a chat begins. Agents can't detect or use new MCP configurations, servers, or tools added after starting a chat.
       
   
   **Cursor Workato Identity authentication**
   
   ### Cursor MCP remote server configuration with Workato Identity authentication
   
   Complete the following steps to configure a Cursor MCP integration that authenticates using Workato Identity:
   
   1. Go to **AI Hub > Enterprise MCP > Custom servers**.
      
   2. Click the MCP server you plan to use for your remote integration.
      
   3. Click **Settings > End user access**.
      
   4. Go to the **Access Method** section and ensure that Workato Identity is selected.
      
   5. Click **Add user groups**.
      
      ![Click Add user groups](/assets/add-user-groups.BG20fzRt.png)_Click **Add user groups**_
      
   6. Use the **User groups** drop-down menu to select the user groups you plan to provide with access to the MCP server.
      
   7. Click the **Details** tab.
      
   8. Go to the **Remote MCP URL** section and click **Copy URL**.
      
      ![Copy your remote MCP URL](/assets/workato-identity-mcp-url.CmzKl5uu.png)_Copy your remote MCP URL_
      
   9. Sign in to Cursor.
      
   10. Go to **Settings > Cursor settings**.
       
   11. Click **MCP & Integrations** in the sidebar.
       
   12. Click **\+ New MCP Server** to open the `mcp.json` file.
       
       ![New MCP server](/assets/configure-cursor.DhhCFK4N.png)_Click **\+ New MCP Server**_
       
   13. Update the configuration to use the MCP URL you copied in the preceding steps. For example:
       
       ```json
       
       {
         "mcpServers": {
           "github-tools": {
             "url": "https://201.apim.mcp.workato.com/abc247/example-collection-name-v1"
           }
         }
       }
       ```
       
   14. Save your changes.
       
   15. Restart Cursor.
       
   16. Go to **Settings > Cursor settings** > **MCP & Integrations** in Cursor.
       
   17. Locate the MCP tools you added and click **Connect**. Tools that require authentication are labeled with **Needs authentication**.
       
       ![Click connect](/assets/connect-cursor.AZlTwMzQ.png)_Click **Connect**_
       
   18. Click **Open** when Cursor prompts **Do you want Cursor to open the external website?**. This opens your organization's SSO login page.
       
       ![Open external site prompt](/assets/open-external-site.xzf8vHq2.png)_Click **Open**_
       
   19. Sign in to your organization's SSO provider.
       
   20. Click **Open Cursor** when prompted.
       
   21. Create a new chat with your Cursor agent to use the tools you added.
       
       You must start a new chat with your agent. Cursor agents only have access to the tools and capabilities available when a chat begins. Agents can't detect or use new MCP configurations, servers, or tools added after starting a chat.
       
   
   **ChatGPT**
   
   ### ChatGPT MCP remote server configuration
   
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
       
   
   **Claude Desktop**
   
   ### Claude Desktop MCP remote server configuration with token authentication
   
   Complete the following steps create an MCP integration with Claude Desktop using an MCP URL and token:
   
   1. Go to **AI Hub > Enterprise MCP > Custom servers**.
      
   2. Click the MCP server you plan to use for your remote integration.
      
   3. Click **Settings > End user access**.
      
   4. Go to the **Access Method** section and ensure that **Token-based access** is selected.
      
   5. Go to the **Developer MCP Token** section and click **Copy**.
      
      > Use a separate `wkt_token` for each Claude Team project when connecting to multiple instances to avoid `Unauthorized` errors.
      
      ![Copy the MCP URL and token](/assets/copy-developer-mcp-token.Chp0BlZi.png)_Copy the MCP URL and token_
      
   6. Sign in to Claude Desktop.
      
   7. Go to **Settings > Connectors**.
      
   8. Click **\+ Add new connector**.
      
   9. Enter a name for your MCP connector in the **Name** field.
      
      ![Claude connector](/assets/claude-mcp-setup.CLtAsbY0.png)_Configure your Claude MCP connector_
      
   10. Paste your MCP URL and token into the **Remote MCP server URL** field.
       
   11. Click **Add**. The newly created MCP connector appears in the list of connectors.
       
   12. Click **Configure**.
       
   13. Use the permissions drop-down menu to select **Always ask permission** or **Allow unsupervised**. **Always ask permission** is selected by default.
       
   

## Add a remote MCP server to an AI model

You can use your `REMOTE_MCP_URL` to configure your remote server with the following AI models:

- [ChatGPT](#chatgpt-mcp-configuration)
- [Claude](#claude-mcp-configuration)
- [Cursor](#cursor-mcp-configuration)
- [Gemini Enterprise](#gemini-enterprise-mcp-configuration-with-workato-identity-authentication)
- [Microsoft Copilot](#microsoft-copilot-mcp-configuration)

### ChatGPT MCP configuration

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

### Claude MCP configuration

Complete the following steps to add your MCP server to Claude:

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

### Cursor MCP configuration

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

### Gemini Enterprise MCP configuration with Workato Identity authentication

Gemini Enterprise asks you to enter a Client ID, Client Secret, and Scopes on its own OAuth setup screen. Workato Identity issues these values through Dynamic Client Registration (DCR) when you send a registration request.

Ensure the following before you begin:

- The MCP server uses Workato Identity access. Refer to [Use Workato Identity for access](/en/mcp/mcp-authentication#use-workato-identity-for-authentication) to switch the access method.
- Users belong to an end-user group that has access to the server. Refer to [End-user groups](/en/mcp/mcp-authentication#user-groups) for more information.

Each registration request creates a new Client ID and Client Secret pair. You receive both values from the registration response, not from **Workspace admin > API clients**.

Complete the following steps to add your MCP server to Gemini Enterprise:

1. Go to the **Details** tab of your MCP server and copy the **Remote MCP URL**.
   
   ![Details tab showing Workato Identity as the authentication method and the Remote MCP URL with a Copy button.](/assets/mcp-server-remote-mcp-url.B8WwzPP8.png)_Remote MCP URL on the MCP server Details tab_
   
2. Open `MCP_SERVER_URL/.well-known/oauth-protected-resource` in a browser, replacing `MCP_SERVER_URL` with the Remote MCP URL you copied.
   
3. Copy the authorization server URL from the `authorization_servers` array, without the brackets or quotation marks.
   
4. Open `AUTHORIZATION_SERVER_URL/.well-known/oauth-authorization-server` in a browser. Replace `AUTHORIZATION_SERVER_URL` with the value from the previous step. The page that opens is the OAuth discovery document. Copy the following values:
   
   - `registration_endpoint`
   - `authorization_endpoint`
   - `token_endpoint`
   - `scopes_supported`
5. Run the following command in a terminal, replacing the following placeholders:
   
   - `REGISTRATION_ENDPOINT`: the `registration_endpoint` value from the discovery document.
   - `REDIRECT_URI`: the redirect URI that the external MCP client provides. Use `https://vertexaisearch.cloud.google.com/oauth-redirect` for Gemini Enterprise.
   - `CLIENT_NAME`: a name for the client.
   - `SCOPES`: a space-separated list of values from `scopes_supported`. Commas aren't valid.
   
   ```shell
   curl -X POST "REGISTRATION_ENDPOINT" \
     -H "Content-Type: application/json" \
     -d '{
       "client_name": "CLIENT_NAME",
       "redirect_uris": ["REDIRECT_URI"],
       "grant_types": ["authorization_code", "refresh_token"],
       "response_types": ["code"],
       "token_endpoint_auth_method": "client_secret_post",
       "scope": "SCOPES"
     }'
   ```
   
6. Copy `client_id`, `client_secret`, and `scope` from the JSON response. The server can add scopes beyond those you requested.
   
   Example response
   
   ```json
   {
     "client_id": "CLIENT_ID",
     "client_id_issued_at": 1700000000,
     "client_secret_expires_at": 0,
     "token_endpoint_auth_method": "client_secret_post",
     "redirect_uris": ["REDIRECT_URI"],
     "grant_types": ["authorization_code", "refresh_token"],
     "response_types": ["code"],
     "scope": "openid profile email claudeai",
     "client_secret": "CLIENT_SECRET"
   }
   ```
   
7. Enter the following values in the external MCP client. The field names match Gemini Enterprise and might differ in other MCP clients.
   
   | Field | Value |
   | --- | --- |
   | MCP Server URL | The **Remote MCP URL** from the **Details** tab of your MCP server |
   | Authorization URL | `authorization_endpoint` from the [discovery document](#oauth-discovery-document) |
   | Token URL | `token_endpoint` from the [discovery document](#oauth-discovery-document) |
   | Client ID | `client_id` from the [registration response](#oauth-registration-response) |
   | Client Secret | `client_secret` from the [registration response](#oauth-registration-response) |
   | Scopes | `scope` from the [registration response](#oauth-registration-response) |
   
   Refer to [Create the custom MCP server data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server#create_the_custom_mcp_server_data_store) in the Google Cloud documentation for where to enter these values in Gemini Enterprise.
   

### Microsoft Copilot MCP configuration

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
