---
url: 'https://docs.workato.com/en/mcp/troubleshooting.md'
description: >-
  Troubleshoot common MCP errors, including Workato Identity access, end-user
  group setup, user access tracking, and SSL inspection.
---

# Troubleshoot MCP errors

Use this document to troubleshoot MCP errors you may encounter.

## Can't access an MCP server with Workato Identity

MCP servers using [Workato Identity](/en/workato-identity) (OAuth 2.0) authentication don't grant automatic access to any users. All users must be added to an end-user group to access MCP servers, including administrators.

Complete the following steps to grant access:

1. Create or select an end-user group in Workato Identity.
   
2. Add users to the group.
   
3. Add the group to your MCP server's **Settings > End user access** page.
   

You must have admin privileges to manage user groups. Token-based authentication only requires the MCP URL and token.

Refer to [MCP access methods user groups](/en/mcp/mcp-authentication#user-groups) for step-by-step instructions.

## Track MCP server user access

[MCP server logs](/en/mcp/mcp-server-access-and-configuration#view-mcp-server-logs) provide a unified usage and access overview for governance and tracking. Logs include:

- **User ID**: Who accessed the server
- **Request IP address**: Where the request came from
- **Creation timestamp**: When the access occurred
- **Which tools/APIs were called**: What actions were performed

You can access logs in the [Workato Logging Service](/en/features/logging-service). Go to **Tools > Logs**, then click the **Log type** filter, select **MCP server**, and click **Apply** to view only MCP server logs.

## SSL certificate mismatch

You may experience MCP connectivity failures if you're using certain network security appliances that perform SSL inspection (also called TLS inspection or TLS decryption). An active SSL inspection intercepts https traffic and re-signs it with its own certificate. This causes the MCP client to reject the connection because the certificate doesn't match the Workato SSL certificate.

A targeted exemption must be created. This doesn't disable SSL inspection globally.

Complete the following steps to resolve this issue:

1. Contact your network or security team to confirm that SSL inspection is enabled on your network.
   
2. Ask your network or security team to add an SSL inspection bypass (TLS decryption exemption) for `*.apim.mcp.workato.com`.
   
3. Retry the MCP client connection to your Workato MCP endpoint.
   

Open a support case with Workato if the issue persists.

---
