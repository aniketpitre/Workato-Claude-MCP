---
url: 'https://docs.workato.com/en/mcp/enterprise-context-mcp.md'
description: >-
  Give AI clients like Claude, Cursor, and ChatGPT governed, real-time access to
  your connected data sources and knowledge bases through a native MCP server.
---

# Enterprise Context MCP

Enterprise Context MCP (EC MCP) is a native MCP server that exposes your workspace's connected data sources and knowledge bases to external AI clients, such as Claude Desktop, Claude Code, Cursor, and ChatGPT, as governed search tools. Every entitled workspace gets a ready-made server instead of building and maintaining a separate integration for every AI client your teams use. Agents and end users can query the server directly, with the same permissions and governance you already rely on elsewhere in Workato.

> **FEATURE AVAILABILITY**
> 
> Enterprise Context MCP is available to select customers. Contact your Customer Success Manager to learn more.

## Why use Enterprise Context MCP

Enterprise Context MCP provides the following:

- **One governed MCP server to give agents access to all your enterprise data**. Connect Claude, Cursor, ChatGPT, or any MCP-compatible client to a single server instead of using multiple custom MCP servers for each enterprise data source, such as Jira and Confluence.
- **Answers stay grounded in what a user can actually see**. Search and traversal results are filtered by each caller's permissions at query time, not pre-computed or cached across users.
- **Admins decide what's exposed**. You choose which connected data sources and custom knowledge bases the server searches, and control access with Workato Identity groups, rate limits, and IP allowlisting.
- **Consistent answers everywhere**. Enterprise Context MCP uses the same retrieval and ranking pipeline as Workato GO and Agent Studio genies, so the same query returns consistent results no matter which client sends it.

## Capabilities

Enterprise Context MCP supports the following capabilities:

| Capability | Description |
| --- | --- |
| Data source and knowledge base allowlisting | Enable or disable individual connected data sources and custom knowledge bases the MCP server exposes. Knowledge bases are searchable as peers alongside crawler-connected data sources. |
| `list_data_sources` tool | Returns the enabled data sources and knowledge bases, along with the metadata keys each one supports for filtering. |
| `search_data_source` tool | Searches across enabled data sources and knowledge bases, with optional metadata filters. Results are filtered by the calling user's permissions. |
| Knowledge Graph traversal | Exposes relationship traversals across your connected systems as MCP tools, so agents can follow relationships instead of chaining multiple searches. Refer to [Knowledge Graph](/en/mcp/knowledge-graph) for more information. |
| Workato Identity group assignment | Restrict which Workato Identity groups can access the MCP server. |
| Limits and IP allowlisting | Set a server-level rate limit and restrict access to specific IP addresses. |
| Audit logging | Tool calls, including graph traversals, are logged with the same fields as other search activity. |

A newly provisioned MCP server starts with every connected data source enabled and no knowledge bases enabled, so you don't lose access to sources you already had while you decide what else to enable.

## Enable Enterprise Context MCP

Confirm the following before you begin:

- Your workspace has an Enterprise Search or Agent Studio entitlement. Only workspaces with these entitlements have access to an Enterprise Context MCP server.
- Enterprise Context MCP is enabled for your workspace. This feature is available to select customers. Contact your Customer Success Manager to request access if the MCP server isn't listed in your AI Hub.
- You have a builder role with permission to view and update MCP server settings.

Complete the following steps to configure your Enterprise Context MCP server:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise context**.
   
3. Go to the **Connected sources** section and turn off any connected data source you don't plan for this server to expose. Turn on any custom knowledge bases you plan for it to search.
   
4. Optional. Go to the **Access** section and assign the Workato Identity groups allowed to use this server.
   
5. Optional. Go to the **Limits** section to set a rate limit and add entries to the **Allowed IPs** field.
   
6. Click **Copy URL** to copy the workspace-specific MCP endpoint.
   
7. Add the URL to your AI client's MCP settings and authenticate through Workato Identity when prompted.
   

Refer to [Install remote MCP servers](/en/mcp/remote-mcp-servers) for client-specific configuration steps for Claude, Cursor, and ChatGPT.

## Limitations

Enterprise Context MCP has the following limitations:

- Each workspace has a single Enterprise Context MCP server. Per-server scoping to a subset of data sources for different audiences isn't supported.
- Knowledge Graph traversal requires separate access. Refer to [Knowledge Graph](/en/mcp/knowledge-graph) for more information.

---
