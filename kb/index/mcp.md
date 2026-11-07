# MCP

27 pages. Paths are relative to the repository root.


## MCP

- **MCP** - `kb/docs/en/mcp.md` - Learn how Model Context Protocol (MCP) connects AI agents to business tools and data, and how to build and use Workato MCP servers in AI Hub.
- **Workato Developer API MCP server** - `kb/docs/en/mcp/developer-api-mcp.md` - Expose Workato Developer and Embedded APIs as a remote MCP server so AI tools like Claude Desktop and Cursor can manage assets and projects.
- **Enterprise Context MCP** - `kb/docs/en/mcp/enterprise-context-mcp.md` - Give AI clients like Claude, Cursor, and ChatGPT governed, real-time access to your connected data sources and knowledge bases through a native MCP server.
- **MCP - FAQs** - `kb/docs/en/mcp/faqs.md` - Answers to common questions about Model Context Protocol (MCP), including setup, authentication, Verified User Access, and troubleshooting.
- **MCP Gateway** - `kb/docs/en/mcp/mcp-gateway.md` - The MCP Gateway governs MCP servers across your organization, enforcing authorization, traffic limits, audit data, and governance policies.
- **MCP local servers** - `kb/docs/en/mcp/mcp-local-servers.md` - Learn how an MCP local server runs on your machine to connect AI models to local files, databases, and Workato API collections and Developer APIs.
- **MCP Registry** - `kb/docs/en/mcp/mcp-registry.md` - The MCP Registry is the central catalog of MCP servers in your Workato organization for discovering, adding, and reusing servers across teams.
- **MCP Runtime** - `kb/docs/en/mcp/mcp-runtime.md` - The MCP Runtime is the Workato-hosted layer that operates your MCP servers, handles client traffic, and runs each tool with the user's own identity.
- **Remote MCP servers** - `kb/docs/en/mcp/remote-mcp-servers.md` - Learn how remote MCP servers are hosted externally to serve multiple users and AI platforms, and install one with a URL or Workato Identity.
- **MCP - Troubleshoot errors** - `kb/docs/en/mcp/troubleshooting.md` - Troubleshoot common MCP errors, including Workato Identity access, end-user group setup, user access tracking, and SSL inspection.

## Enterprise Context MCP

- **Knowledge Graph** - `kb/docs/en/mcp/knowledge-graph.md` - Resolve entities and relationships across your connected systems and traverse them through Enterprise Context MCP.

## MCP Gateway

- **MCP servers dashboard** - `kb/docs/en/mcp/dashboard.md` - View MCP server tool call volume, success rate, response time, and estimated token usage across all MCP servers, filtered by period, server, client, and user.
- **MCP access methods** - `kb/docs/en/mcp/mcp-authentication.md` - Configure MCP server access with API token-based access, OAuth2 single sign-on through Workato Identity, or OpenID Connect (OIDC) and switch between access methods.
- **MCP verified user access configuration** - `kb/docs/en/mcp/verified-user-access-configuration.md` - Configure MCP verified user access by setting up Workato Identity, end-user groups, and OAuth 2.0 end user tool connections.
- **MCP verified user access** - `kb/docs/en/mcp/verified-user-access.md` - Learn how MCP verified user access uses runtime user connections so each end user authenticates to external tools with their own credentials.

## MCP Registry

- **Manage an MCP server registry** - `kb/docs/en/mcp/manage-mcp-registry.md` - Set up an MCP server registry to enable teams to browse, search, and add MCP servers from a single catalog.
- **Request MCP server registry access** - `kb/docs/en/mcp/request-mcp-registry-access.md` - Request access to MCP servers in your organization's registry that authenticate with Workato Identity or an API token.

## MCP composition

- **Manage MCP server tools** - `kb/docs/en/mcp/manage-tools.md` - Manage MCP server tools from the Details tab to start, stop, add, and remove tools and edit the LLM-facing server description.
- **MCP app development** - `kb/docs/en/mcp/mcp-app-development.md` - Build a Workato MCP app with HTML and JavaScript, including the SDK connection, calling tools, Content Security Policy, and debugging.
- **MCP Apps** - `kb/docs/en/mcp/mcp-apps.md` - MCP Apps lets tools return interactive tables, forms, and dashboards inside the LLM chat so users view, sort, and act on data without leaving the conversation.
- **MCP server design best practices** - `kb/docs/en/mcp/mcp-server-design.md` - Learn best practices for designing MCP servers, including how they differ from traditional APIs, tool scope, error handling, and LLM reasoning.
- **MCP server tool design** - `kb/docs/en/mcp/mcp-server-tool-design.md` - Learn best practices for designing MCP server tools, including tool breakdown, data optimization, error codes, and testing with AI agent workflows.
- **Start with a prebuilt MCP server** - `kb/docs/en/mcp/prebuilt-mcps.md` - Workato prebuilt MCP servers integrate AI tooling into your workflows with customizable tools, business logic, user provisioning, and rate limits.

## Use cases

- **MCP use cases - LLM, GitHub, and Workato Developer API** - `kb/docs/en/getting-started/use-cases/mcp/github-developer-api-llm.md` - Create an MCP integration that enables your LLM to create new issues in GitHub using the Workato Developer API.
- **MCP Use Cases - LLM, Snowflake, and Workato Developer API** - `kb/docs/en/getting-started/use-cases/mcp/snowflake-developer-api.md` - Create an MCP integration that enables an LLM to query Snowflake data using natural language commands through integration with the Workato Developer API.

## Work with MCP clients

- **Genies as MCP clients** - `kb/docs/en/mcp/genies-as-mcp-clients.md` - Connect MCP servers as skills in an Agent Studio genie to call external APIs and third-party tools without building custom skills.
- **MCP server access and configuration** - `kb/docs/en/mcp/mcp-server-access-and-configuration.md` - Access and configure your MCP servers in AI Hub, view server details and tools, and retrieve the MCP remote URL for your clients.
