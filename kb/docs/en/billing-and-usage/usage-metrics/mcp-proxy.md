---
url: 'https://docs.workato.com/en/billing-and-usage/usage-metrics/mcp-proxy.md'
description: >-
  Learn how Workato measures MCP proxy usage in MCP Proxy Calls, counted per
  request routed from an MCP client to an external MCP server.
---

# MCP proxy usage

Workato measures MCP proxy usage in MCP Proxy Calls. Each successful proxied request counts as 1 MCP Proxy Call.

## How MCP Proxy Calls are measured

A [proxy MCP server](/en/mcp/mcp-gateway#proxy-to-third-party-mcp-servers) is a Workato-hosted MCP server that fronts an external third-party MCP server. An MCP client, such as Claude, Cursor, or Windsurf, connects to the proxy MCP server, which authenticates the request and routes it to the external MCP server. Each request that completes end-to-end counts as 1 MCP Proxy Call.

```mermaid
%%{init: {'themeVariables': {'fontSize': '18px'}, 'flowchart': {'padding': 4, 'nodePadding': 4}}}%%
flowchart LR
    MC["<br/><br/><br/>MCP<br/>client<br/><br/><br/><br/>"] -->|calls| MP["<br/><br/><br/>Workato<br/>proxy MCP<br/>server<br/><br/><br/>"]
    MP -->|routes to| TS["<br/><br/><br/>External<br/>MCP server<br/><br/><br/><br/>"]
    classDef default fill:#fff,stroke:#67eadd,stroke-width:2px,color:#000;
    classDef External fill:#fff,stroke:#b3e0e1,stroke-width:2px,color:#666,stroke-dasharray: 5 5;
    classDef Focus fill:#e2e0f5,stroke:#5159f6,stroke-width:2px,color:#000;
    class MC External
    class MP Focus
    class TS External
```

Total usage: 1 MCP Proxy Call

## MCP proxy calculation rules

MCP proxy usage calculations follow the general [usage calculation rules](/en/pricing/usage-metrics#rules). In addition:

- Each successful proxied request counts as 1 MCP Proxy Call, regardless of how long the external MCP server takes to respond.
- Failed requests don't contribute to usage. Customer-handled `4xx`/`5xx` responses that reach a terminal state count as successful.

## MCP proxy usage examples

The following example demonstrates how Workato calculates MCP proxy usage when an MCP client invokes a tool exposed by a Workato proxy MCP server.

### MCP client calls a proxied tool

**Overview**

```mermaid
%%{init: {'themeVariables': {'fontSize': '18px'}, 'flowchart': {'padding': 4, 'nodePadding': 4}}}%%
flowchart LR
    MC["<br/><br/><br/>MCP<br/>client<br/>(Claude)<br/><br/><br/>"] -->|calls| MP["<br/><br/><br/>Workato<br/>proxy MCP<br/>server<br/>(1 MCP Proxy Call)<br/><br/>"]
    MP -->|routes to| TS["<br/><br/><br/>Salesforce<br/>MCP server<br/><br/><br/><br/>"]
    classDef default fill:#fff,stroke:#67eadd,stroke-width:2px,color:#000;
    classDef External fill:#fff,stroke:#b3e0e1,stroke-width:2px,color:#666,stroke-dasharray: 5 5;
    classDef Focus fill:#e2e0f5,stroke:#5159f6,stroke-width:2px,color:#000;
    class MC External
    class MP Focus
    class TS External
```

Total usage: 1 MCP Proxy Call

**Explanation**

An MCP client, such as Claude, invokes a Salesforce record-lookup tool exposed by a Workato proxy MCP server. The proxy authenticates the request and routes it to Salesforce's MCP server. The proxied request counts as 1 MCP Proxy Call. Additional tools invoked in the same session each count as their own MCP Proxy Call.

#### Usage totals

- **MCP Proxy Calls**: 1
- **Total usage per proxied request**: 1 MCP Proxy Call

---
