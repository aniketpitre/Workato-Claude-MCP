---
url: 'https://docs.workato.com/en/mcp/mcp-registry.md'
description: >-
  The MCP Registry is the central catalog of MCP servers in your Workato
  organization for discovering, adding, and reusing servers across teams.
---

# MCP Registry

The MCP Registry is the central catalog of MCP servers available in your Workato organization. It provides a unified view of:

- MCP servers your teams compose from scratch or add through Workato [prebuilt MCP servers](/en/mcp/prebuilt-mcps)
- Third-party MCP servers added through [MCP proxy](/en/mcp/mcp-servers#create-a-proxy-mcp-server)

## Discovery and adoption

Teams can browse, search, and add MCP servers across the enterprise from a single catalog. Each MCP server entry includes the name, description, available tools, and ownership metadata. Clients connect to MCP servers discovered through the registry rather than manually configuring MCP server endpoints.

> **MCP REGISTRY IS ENVIRONMENT SPECIFIC**
> 
> An MCP registry is available only within the environment where you created it. MCP registries aren't shared across workspaces, AHQ managed workspaces, or Embedded customer accounts.

![MCP Registry](/assets/mcp-registry.DYkUjtXK.png)_MCP Registry_

## Centralized visibility

The MCP Registry maintains an inventory of all MCP activity across your organization. Workato-hosted MCP servers and third-party proxy MCP servers are subject to the policies defined in the MCP Gateway.

![Centralized visibility](/assets/centralized-visibility.BkQN_5CL.png)_Centralized visibility_

## Reuse across teams

MCP servers composed by one team are available to other teams across the organization. This eliminates duplicate integration work.

---
