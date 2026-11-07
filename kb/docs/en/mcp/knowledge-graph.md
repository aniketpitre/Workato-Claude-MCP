---
url: 'https://docs.workato.com/en/mcp/knowledge-graph.md'
description: >-
  Resolve entities and relationships across your connected systems and traverse
  them through Enterprise Context MCP.
---

# Knowledge Graph

Knowledge Graph is a capability of [Enterprise Context MCP](/en/mcp/enterprise-context-mcp) that resolves entities and relationships across your connected systems and lets agents traverse them in a single call, instead of running separate searches against each system and stitching the results together themselves.

> **FEATURE AVAILABILITY**
> 
> Knowledge Graph is available to select customers. Contact your Customer Success Manager to learn more.

## How it works

Workato continuously crawls your connected data sources and indexes what it finds. Knowledge Graph adds a layer on top of that index that recognizes when records from different sources refer to the same person, account, or topic, and links them together. When an agent asks a question, it doesn't write the underlying traversal itself. Workato interprets the request, queries the graph on the agent's behalf, and returns the connected results.

## Why use Knowledge Graph

Knowledge Graph offers the following advantages when a request spans more than one connected system:

- **Answers questions that span multiple systems.** A request like `Give me a summary of all the sales calls and key action items that my team had this week` requires joining call records to the right accounts and owners, then pulling in related work items. Without a graph, an agent has to query each system separately and join the results itself. Knowledge Graph turns this into a single traversal.
- **Fixes searches that come back empty.** Filtered searches that rely on matching names or account references across systems often return no results, because a name on a call transcript rarely matches the account record exactly. Knowledge Graph resolves entities across sources so these queries succeed instead of silently returning nothing.
- **Results respect what each user can see.** Traversals are filtered by the calling user's permissions at query time. A record the user isn't permitted to see is left out of the result entirely, rather than returned in a redacted form.
- **Traversals are logged like any other search.** Graph tool calls appear in your audit log with the same fields as search activity.

## Capabilities

Knowledge Graph currently supports the following:

| Capability | Description |
| --- | --- |
| Cross-source entity resolution | Links the same person, account, or record across connected systems, so a query doesn't depend on an exact name match. |
| Relationship traversal | Retrieve related records across your connected systems through an Enterprise Context MCP tool. |
| Org chart traversal | Retrieve a person's reporting structure, including their manager and their direct reports. |
| Permission-aware traversal | Records the calling user can't see are omitted from the traversal rather than shown in a redacted form. |
| Audit logging | Graph tool calls are logged alongside other Enterprise Context MCP search activity. |

## Enable Knowledge Graph

Knowledge Graph is available to select customers. Contact your Customer Success Manager to request access for your workspace before you complete the following steps.

Confirm the following before you begin:

- Your workspace has an Enterprise Context MCP server. Refer to [Enable Enterprise Context MCP](/en/mcp/enterprise-context-mcp#enable-enterprise-context-mcp) if you haven't set one up yet.
- Your workspace has access to Knowledge Graph.
- You have a builder role with permission to update MCP server settings.

Complete the following steps to enable Knowledge Graph traversal:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise context**.
   
3. Go to the **Connected sources** section and turn on **Knowledge Graph**.
   
4. Click **Save**. Relationship traversal tools become available to any client already connected to this server. No separate URL or reconnection is required.

---
