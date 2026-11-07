---
url: 'https://docs.workato.com/en/mcp/mcp-local-servers.md'
description: >-
  Learn how an MCP local server runs on your machine to connect AI models to
  local files, databases, and Workato API collections and Developer APIs.
---

# MCP local servers

An MCP local server is a program that runs on your machine and implements [Model Context Protocol](https://modelcontextprotocol.io/introduction)(MCP). It enables AI models to access and interact with local tools and data sources like files, databases, and APIs by running the server on the same machine as the AI model.

> **FEATURE AVAILABILITY**
> 
> MCP is available to all users in the US, EU, AU, JP, SG, IL, KR, and UK data centers. MCP servers are hosted in the US, EU, and APAC regions and respect data residency requirements where possible. MCP isn't available to workspaces in the CN data center. This reflects local regulatory requirements and Workato's commitment to data sovereignty and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.
> 
> Contact your Customer Success representative if you're interested in using MCP or require additional information.

Your MCP server acts as a regular API platform user and supports all API platform authentication methods. This lets you securely connect an MCP client to the following API resources:

- **API collections**: Custom API endpoints you've created in API Platform.
- **Developer APIs and Embedded APIs**: Workato Developer APIs and Embedded APIs for managing recipes, connections, tags, folders, and workspace assets. Refer to [Developer API and Embedded API MCP server](/en/mcp/developer-api-mcp) for more information.

All Workato API collections are compatible with this feature.

## MCP local server requirements

You must have the following components to use an MCP local server:

- Node.js v18.0.0 or later
- npm v8.0.0 or later
- An LLM client, such as Claude Desktop, Cursor, or Windsurf
- A [Workato MCP server](/en/mcp/mcp-servers#create-an-mcp-server)

## Install a local MCP server

Complete the following steps to install a local MCP server:

1. Open your preferred MCP client. For example, Claude, Cursor, or Windsurf.
   
2. Locate your MCP configuration settings in the client, and update the config to use the Workato MCP server with the authentication token in the MCP URL or with the authentication token as a separate environment variable:
   
   > **USE A SEPARATE WORKATO TOKEN FOR EACH CLAUDE TEAM**
   > 
   > Use a separate `wkt_token` for each Claude Team project when connecting to multiple instances to avoid `Unauthorized` errors.
   
   **Authentication token in the MCP URL**
   
   1. Replace the `REMOTE_MCP_URL` value with the [remote MCP URL](#retrieve-your-remote-mcp-url) generated for your API collection.
      
      Example configuration:
      
      ```bash
      {
        "mcpServers": {
          "workato-apim": {
            "command": "npx",
            "args": ["@workato/mcp-server"],
            "env": {
              "TYPE": "apim",
              "REMOTE_MCP_URL": "https://mcp.workato.com/your-username/your-collection-id?wkt_token={YOUR_API_TOKEN}"
            }
          }
        }
      }
      ```
      
   
   **Authentication token as a separate environment variable**
   
   1. Replace the `REMOTE_MCP_URL` and `AUTH_TOKEN` values with the [remote MCP URL](#retrieve-your-remote-mcp-url) generated for your API collection and your authentication token.
      
      Example configuration:
      
      ```bash
      {
        "mcpServers": {
          "workato-apim": {
            "command": "npx",
            "args": ["@workato/mcp-server"],
            "env": {
              "TYPE": "apim",
              "REMOTE_MCP_URL": "https://mcp.workato.com/your-username/your-collection-id",
              "AUTH_TOKEN": "YOUR_API_TOKEN"
            }
          }
        }
      }
      ```
      
   

## Retrieve your remote MCP URL

You can access and manage your MCP servers and retrieve your MCP URL in the **AI Hub**.

Complete the following steps to retrieve your MCP URL:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**. A list of your existing MCP servers displays.
   
3. Click the MCP server card you plan to view. The MCP server displays the following information:
   
   - Description
   - Installation link
   - Tools available on the MCP server, such as `Tasks Create` and `CRM Get Company Properties`
   - The MCP remote URL
4. Click **Settings > End user access**.
   
5. Go to the **Developer MCP Token** section and click **Copy**.
   
   ![Copy the MCP URL](/assets/copy-developer-mcp-token.Chp0BlZi.png)_Copy the MCP URL_
   

## Troubleshoot errors

This section explains how to resolve errors you may encounter while using your MCP server.

### CORS setup required

You may encounter a CORS (Cross-Origin Resource Sharing) setup required error when using a browser client to connect to the Workato MCP service with key authentication. For example:

```plaintext

CORS Setup Required:

Your MCP server must enable CORS headers to allow browser connections. Add these headers to your server:

Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: POST
Access-Control-Allow-Headers: Content-Type
```

CORS is a security feature built into web browsers that controls which websites can make requests to which servers. This error is related to Chrome security restrictions. You must disable web security the session to enable Chrome to ignore CORS and make requests to your MCP server.

Complete the following steps to disable web security for your session in Chrome:

> **BROWSERS MAY HAVE DIFFERENT STEPS**
> 
> The steps in this section are specific to Chrome. Steps for other browsers may vary.

1. Close all Chrome windows.
   
2. Complete the following steps for your operating system:
   
   **Mac**
   
   1. Open Terminal. Press `Cmd` + `Space` and type `Terminal`.
      
   2. Run the following command:
      
      ```bash
      open -n -a "Google Chrome" --args --user-data-dir="/tmp/chrome_dev_session" --disable-web-security
      ```
      
        
      - `--disable-web-security`: Disables CORS enforcement in this Chrome session. Chrome allows requests between any domains, regardless of CORS headers.
      - `--user-data-dir="/tmp/chrome_dev_session"`: Creates a separate, temporary Chrome profile so this session doesn't affect your regular browsing.
   3. Press **Return**. Chrome opens a new window with a warning banner: `You are using an unsupported command-line flag: --disable-web-security`.
      
   4. Go to the URL where your MCP is running. For example: `http://localhost:3000`.
      
   5. Test your MCP server.
      
   
   **Windows**
   
   1. Open Command Prompt. Press `Win` + `R`, type `cmd`, and press **Enter**.
      
   2. Go to Chrome directory and run the following command:
      
      ```bash
      "C:\Program Files\Google\Chrome\Application\chrome.exe" --user-data-dir="C:\temp\chrome_dev_session" --disable-web-security
      ```
      
        
      - `--user-data-dir="/tmp/chrome_dev_session"`: Creates a separate, temporary Chrome profile so this session doesn't affect your regular browsing.
      - `--disable-web-security`: Disables CORS enforcement in this Chrome session. Chrome allows requests between any domains, regardless of CORS headers.
   3. Go to the URL where your MCP is running. For example: `http://localhost:3000`.
      
   4. Test your MCP server.
      
   
   **Linux**
   
   1. Open Terminal. Press `Cmd` + `Space` and type `Terminal`.
      
   2. Run the following command:
      
      ```bash
      google-chrome --user-data-dir="/tmp/chrome_dev_session" --disable-web-security
      ```
      
        
      - `--user-data-dir="/tmp/chrome_dev_session"`: Creates a separate, temporary Chrome profile so this session doesn't affect your regular browsing.
      - `--disable-web-security`: Disables CORS enforcement in this Chrome session. Chrome allows requests between any domains, regardless of CORS headers.
   3. Go to the URL where your MCP is running. For example: `http://localhost:3000`.
      
   4. Test your MCP server.
      
   

### Claude unauthorized errors

You may receive an unauthorized error if you use the same `wkt_token` to connect to multiple Claude Team projects.

Use a separate `wkt_token` for each Claude Team project when connecting to multiple instances to avoid `Unauthorized` errors.

---
