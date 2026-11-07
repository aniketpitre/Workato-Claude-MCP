---
url: 'https://docs.workato.com/en/getting-started/use-cases/mcp/mcp-use-cases.md'
description: >-
  Explore MCP use cases that show how to implement MCP servers, local servers,
  Developer API access, and MCP apps with Workato.
---

# MCP use cases

MCP use cases provide steps on how to implement the following MCP capabilities:

- [MCP servers](/en/mcp/mcp-servers) uses your API recipe collections and AI gateway collections to generate unique, authenticated MCP URLs. You can add this MCP URL to your LLM settings to enable an AI agent to use your API endpoint collection to answer user prompts.
  
- [MCP local server](/en/mcp/mcp-local-servers) acts as a regular API platform user and supports all API platform authentication methods. This lets you securely connect an MCP client to any API collection using standard credentials without remote setup. This enables AI models to access and interact with data sources like files, databases, and APIs.
  
- [Workato Developer API MCP](/en/mcp/developer-api-mcp#expose-workato-developer-apis) enables AI-powered developer environments like Claude Desktop and Cursor to programmatically access your Workato workspace and interact with the platform.
  
- [MCP apps](/en/mcp/mcp-apps) is an open standard that enables tools to return interactive elements, such as images, tables, forms, buttons, or dashboards directly inside the LLM chat as an embedded application.
  

Get started with Workato MCP servers in [AI Hub > Enterprise MCP > Custom servers](https://app.workato.com/mcp/custom).

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> Use cases are intended to serve as examples. MCP server and tool modifications, such as access method, tool configuration, and conditional logic may require adjustments if you plan to include these MCP tools in your own workflows.

### [Create a new GitHub issue in an LLM](https://docs.workato.com/en/getting-started/use-cases/mcp/github-developer-api-llm.html)

This use case integrates an [LLM, GitHub, and Workato Developer API](https://docs.workato.com/getting-started/use-cases/mcp/github-developer-api-llm.html) to create a new GitHub issue based on the instructions you give your agent in a chat.

### [Analyze Snowflake data in an LLM](https://docs.workato.com/en/getting-started/use-cases/mcp/snowflake-developer-api.html)

This use case integrates an [LLM, Snowflake, and Workato Developer API](https://docs.workato.com/en/getting-started/use-cases/mcp/snowflake-developer-api.html) to create analyze Snowflake data based on instructions you give your agent in a chat.

### [Interact with GitHub repo images in an LLM](https://docs.workato.com/en/getting-started/use-cases/mcp/github-mcp-app.html)

This use case integrates a [custom GitHub MCP app](https://docs.workato.com/en/getting-started/use-cases/mcp/github-mcp-app.html) to render pannable and zoomable images from your GitHub repo directly in a chat.

## More resources

- [MCP](/en/mcp)
- [Create an MCP server](/en/mcp/mcp-servers#create-an-mcp-server)
- [Manage MCP server tools](/en/mcp/manage-tools#manage-mcp-server-tools)
- [MCP Apps](/en/mcp/mcp-apps)

---
