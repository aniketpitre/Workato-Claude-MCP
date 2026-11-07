---
url: 'https://docs.workato.com/en/mcp/faqs.md'
description: >-
  Answers to common questions about Model Context Protocol (MCP), including
  setup, authentication, Verified User Access, and troubleshooting.
---

# MCP - FAQ

Get answers to frequently asked questions about Model Context Protocol (MCP), including setup, authentication, Verified User Access, and troubleshooting.

## Overview

What is MCP?

[Model Context Protocol (MCP)](/en/mcp) is an open protocol that standardizes how AI models connect to external systems and data sources. MCP enables you to expose your Workato capabilities (API collections, API recipes, recipe functions, and skills) as tools that AI clients can use.

Key benefits of MCP include:

- **Connects AI to external resources**: Enables AI models to access external data and tools to improve versatility and capabilities
- **Standardizes interactions**: Provides a consistent way for AI models to communicate with different systems like Slack, Jira, or Google Drive
- **Reduces development**: MCP's standardization reduces the need for custom integrations for each new data source

What MCP capabilities does Workato provide?

Workato provides the following MCP capabilities:

- **[MCP servers](/en/mcp/mcp-servers)**: Enable you to provide Workato capabilities (API collections, recipe functions, API recipes, and skills) as tools to AI agents through remote, cloud-based MCP servers with unique, authenticated URLs.
- **[Verified User Access](/en/mcp/verified-user-access)**: Enables your MCP servers to use authenticated end-user credentials for external API calls instead of static tokens.
- **[Workato Developer API and Embedded API MCP](/en/mcp/developer-api-mcp)**: Enables AI-powered developer environments like Claude Desktop and Cursor to programmatically access your Workato workspace.

Which AI clients/LLMs are compatible with Workato MCP?

[Workato MCP](/en/mcp#getting-started) is compatible with:

- Claude (Anthropic)
- Cursor
- Windsurf
- ChatGPT
- Any MCP client that supports the Model Context Protocol standard

## Setup and access

Is MCP available in my region?

**[MCP](/en/mcp) is available in the US, EU, AU, SG, and JP data centers.**

Contact your Customer Success representative if you're interested in using MCP or require additional information. Refer to your pricing plan and contract to learn more.

How do I create an MCP server in Workato?

You can create an MCP server in the AI Hub by [starting with a prebuilt template](/en/mcp/prebuilt-mcps#install-a-prebuilt-mcp-server-in-workato) or [building your own from scratch](/en/mcp/mcp-servers#create-an-mcp-server). The setup steps vary depending on which approach you choose.

What prebuilt MCP server templates are available?

Workato provides prebuilt MCP server templates for common collaboration and productivity apps, such as [Slack](/en/mcp/prebuilt-mcps/slack-mcp-server), [Google Calendar](/en/mcp/prebuilt-mcps/google-calendar-mcp-server), and [Google Sheets](/en/mcp/prebuilt-mcps/google-sheets-mcp-server), project and development apps, such as [Jira](/en/mcp/prebuilt-mcps/jira-mcp-server) and [GitHub](/en/mcp/prebuilt-mcps/github-mcp-server), identity management apps, such as [Google Directory End User](/en/mcp/prebuilt-mcps/google-directory-end-user-mcp-server) and [Okta End User](/en/mcp/prebuilt-mcps/okta-end-user-mcp-server), and sales operations apps, such as [Gong](/en/mcp/prebuilt-mcps/gong-mcp-server).

Refer to the [Prebuilt MCP servers](/en/mcp/prebuilt-mcps/mcp-servers) page for a complete list of available templates.

What types of assets can I add as tools to an MCP server?

You can select one of two tool source types when creating an MCP server from scratch:

**API collection**

Expose an entire API collection as MCP tools. This includes standard API recipe collections and AI gateway collections (API proxy collections). API collections don't support Verified User Access.

**Project assets**

Select individual assets from a project folder to expose as MCP tools:

- Recipe functions
- API recipes
- Skills

With project assets, you can mix multiple asset types in the same MCP server. All assets must be in the same project folder.

Learn more about [MCP servers](/en/mcp/mcp-servers) and [Verified User Access](/en/mcp/verified-user-access).

How do I configure an AI client to use my MCP server?

Configuration steps vary by AI client:

- [ChatGPT](/en/mcp/remote-mcp-servers#chatgpt-mcp-configuration)
- [Claude Desktop](/en/mcp/remote-mcp-servers#claude-mcp-configuration)
- [Cursor](/en/mcp/remote-mcp-servers#cursor-mcp-configuration)
- [Microsoft Copilot](/en/mcp/remote-mcp-servers#microsoft-copilot-mcp-configuration)

What are the best practices for designing MCP tools?

Follow these key principles when [designing MCP tools](/en/mcp/mcp-server-tool-design):

**Tool design principles**:

- **Simple**: Each tool performs exactly one specific action or retrieval
- **Composable**: Tools act as building blocks that work together seamlessly
- **Predictable**: Tools behave consistently and return standard errors

**Data strategy**:

- Return only necessary fields to preserve context windows
- Use AI preprocessing to summarize large datasets before returning to the agent

**Developer experience**:

- Write clear tool names and detailed descriptions
- Include sample requests and responses in tool documentation
- Use consistent naming conventions across all tools
- Implement standard HTTP status codes (200, 400, 404, 500)

**Monitoring and refinement**:

- Test tools with real AI workflows
- Monitor usage patterns and refine based on which tools are used most frequently

## Authentication and access control

What authentication methods does MCP support?

MCP supports [two authentication methods](/en/mcp/mcp-authentication):

**Token-based authentication** (default):

- Simple authentication with minimal configuration
- Tokens generated automatically and managed in MCP server settings
- Assigned by default to new MCP servers

**OAuth 2.0 integration with Workato Identity**:

- Required for Verified User Access (VUA)
- Provides centralized user access management
- Enables user-level audit trails and identity-aware authorization

**Important**: Switching from token-based authentication to Workato Identity revokes the MCP token, requiring all clients to be reconfigured for OAuth 2.0 authentication.

What is Verified User Access and when should I use it?

[Verified User Access (VUA)](/en/mcp/verified-user-access) enables end users to authenticate with their own credentials when interacting with MCP tools, bringing enterprise-grade governance and user-level security to AI workflows.

**How it works**:

- End users authenticate once when first accessing the MCP server
- Credentials are securely stored and reused across tools
- All tool calls respect individual user permissions
- Each action executes with the user's own identity and access rights

**When to use VUA**:

- You need user-level audit trails for compliance
- Tools access sensitive data requiring individual permissions
- You want to eliminate shared credentials for security
- Your organization requires identity-aware authorization

**Requirements**:

- MCP server must use [Workato Identity (OAuth 2.0) authentication](/en/mcp/mcp-authentication#oauth2-authentication-with-workato-identity)
- MCP server must use project assets as the tool source. API collections aren't supported.
- Selected tools must be recipe functions or skills
- Connected applications must support OAuth 2.0 authorization code grant. API keys, basic auth, and other OAuth 2.0 grant types don't work with VUA.

How do I enable Verified User Access for my MCP server?

Complete the following steps to use [Verified User Access (VUA)](/en/mcp/verified-user-access) with your MCP server:

1. Configure your MCP server to use [Workato Identity authentication](/en/mcp/mcp-authentication#oauth2-authentication-with-workato-identity).
   
2. Create recipe functions or skills as your MCP tools.
   
3. Configure connections to use **end-user connections**.
   

This allows each user to interact with your MCP tools using their own credentials, ensuring actions are performed as the authenticated user rather than the builder's credentials.

## Limitations

Can I limit MCP server usage?

Yes. You can [configure MCP server quotas](/en/mcp/mcp-server-access-and-configuration#configure-mcp-server-limits) by going to your MCP server's **Settings > Limits** page:

- **Rate limits** (throttling): Control request speed to prevent traffic bursts with customizable time intervals. No rate limits are enforced by default. Requests are unlimited if left blank.
- **Usage limits** (cumulative): Limit total consumption over time with aggregate request quotas. No usage limits are enforced by default. Consumption is unlimited if left blank.
- **IP restrictions**: Configure IP allowlists and blocklists to control which IP addresses can access your server. Blocked IPs take precedence over allowed IPs.

When rate limits or usage quotas are exceeded, all requests are blocked until the quota interval passes or the quota resets.

How many tokens can I have active on an MCP server at once?

Up to 50.

What's the maximum size of the Allowed IPs and Blocked IPs lists?

Each list holds up to 500 entries. The same quota applies to the **Allowed IPs** and **Blocked IPs** lists independently.

How long can an MCP tool call run before it times out?

A tool call returns inline within 30 seconds. After that, the call detaches and continues in the background up to a total of 300 seconds. Requests that exceed the asynchronous timeout don't return a response to the MCP client. Set the asynchronous timeout in your recipe settings.

## Troubleshooting

Why can't I access my MCP server with Workato Identity?

MCP servers using Workato Identity (OAuth 2.0) authentication don't grant automatic access to any users. All users must be added to an end-user group to access MCP servers, including administrators.

Complete the following steps to grant access:

1. Create or select an end-user group in Workato Identity.
   
2. Add users to the group.
   
3. Add the group to your MCP server's **Settings > End user access** page.
   

You must have admin privileges to manage user groups. If using token-based authentication instead, you only need the MCP URL and token.

Refer to [MCP access methods user groups](/en/mcp/mcp-authentication#user-groups) for step-by-step instructions.

How can I track who is accessing my MCP server?

[MCP server logs](/en/mcp/mcp-server-access-and-configuration#view-mcp-server-logs) provide a unified usage and access overview for governance and tracking. Logs include:

- **User ID**: Who accessed the server
- **Request IP address**: Where the request came from
- **Creation timestamp**: When the access occurred
- **Which tools/APIs were called**: What actions were performed

You can access logs in the [Workato Logging Service](/en/features/logging-service). Go to **Tools > Logs**, then click the **Log type** filter, select **MCP server**, and click **Apply** to view only MCP server logs.

---
