---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/coupa-approval-operations-mcp-server.md
description: >-
  Use the Coupa Approval Operations MCP server to manage pending approvals
  through natural conversation.
---

# Coupa Approval Operations MCP server

The Coupa Approval Operations MCP server enables LLMs to manage Coupa approvals through natural conversation. It provides tools to find pending approvals, retrieve full approval context, and approve, reject, hold, or request more information on approvals without requiring direct interaction with the Coupa interface.

## Uses

Use the Coupa Approval Operations MCP server to perform the following actions:

- Find pending approvals in your queue, sorted by how long items have been waiting
- Retrieve the full context of a specific approval, including document details and requester information
- Approve pending approvals after reviewing the complete document summary
- Reject approvals with a documented reason
- Place approvals on hold when you need additional review before deciding
- Request more information from requesters by posting comments on documents
- Monitor organization-wide approval health across all approvers and document types

### Example prompts

Use the following example prompts to invoke Coupa Approval Operations MCP server tools:

- `What approvals are waiting for my decision?`
- `Show me my most stalled pending approvals.`
- `Get the details for approval ID 12345.`
- `Approve this requisition.`
- `Reject this invoice because it exceeds the approved budget.`
- `Place this purchase order on hold for further review.`
- `Ask the requester for more details before I approve this.`
- `Show me all stalled approvals across the organization.`
- `What has been pending for more than 5 days?`

## Coupa Approval Operations MCP server tools

The Coupa Approval Operations MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_pending\_approvals](#search-pending-approvals-tool) | Finds pending approvals. |
| [get\_approval](#get-approval-tool) | Retrieves an approval, including its status, document summary, and available actions. |
| [approve\_approval](#approve-approval-tool) | Approves a pending approval if it hasn't changed since it was last reviewed. |
| [reject\_approval](#reject-approval-tool) | Rejects a pending approval for a reason you specify. |
| [hold\_approval](#hold-approval-tool) | Places a pending approval on hold if Coupa reports it eligible for hold. |
| [request\_approval\_info](#request-approval-info-tool) | Posts a comment on the underlying document asking the requester for more detail, without deciding the approval. |

## Install the Coupa Approval Operations MCP server

Complete the following steps to install a prebuilt MCP server to your project:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Click **\+ Create MCP server**.
   
4. Go to the **Start with pre-built MCP Servers using your connected apps** section and select the prebuilt MCP server you plan to use.
   
5. Click **Use this server**.
   
6. Provide a name for your MCP server in the **Server name** field.
   
7. Use the **Location** drop-down menu to select the project for the MCP server.
   
8. Go to the **Connections** section and connect to your app account.
   
9. Select the connection type you plan to use for the MCP server template.
   
   - **User's connection**: MCP server tools perform actions based on the identity and permissions of the user who connects to the application. Users authenticate with their own credentials to execute the skill.
   - **Your connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
   
   ![Select your connection type](/assets/connection-type.Cor-6PJN.png)_Select your connection type_
   
   > **VERIFIED USER ACCESS AUTHENTICATION REQUIREMENTS**
   > 
   > Only app connections that use OAuth 2.0 authorization code grant are available for user's connection. Refer to [Verified user access](/en/mcp/verified-user-access) for more information.
   
10. Complete the app-specific connection setup steps in the following section.
    

## Coupa Approval Operations connection setup

View Coupa Approval Operations connection setup steps

### API version

The Coupa connector uses the [Coupa Core REST API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api).

### How to connect to Coupa with OAuth 2.0

The Coupa connector has supported OAuth 2.0-based connectivity since January 2022. OAuth connections are more secure than API key-based connections. OAuth lets you specify the exact scopes you plan to use in the Workato connection settings. The Coupa connector supports OAuth 2.0 Client Credentials and OAuth 2.0 Authorization Code Grant connections. Refer to [OpenID Connect Clients](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/oauth-2.0-and-oidc/openid-connect-clients) for more information.

View OAuth connection setup steps

1. Sign in to your Coupa instance, for example `https://[your-instance-name].coupacloud.com/oauth2/clients`.
   
2. Click **Create** to create a new OAuth client.
   
3. Use the **Grant type** drop-down menu to select **Authorization Code** or **Client Credentials**. You must select the same option in Workato for the **Authentication type**.
   
4. Provide a name in the **Name** field. For example: `Workato Coupa OAuth connection`.
   
5. Enter the redirect URIs you plan to use in the **Redirect URIs** field. Add the link `https://www.workato.com/oauth/callback` if you plan to use **Authorization code**.
   
6. Select the scopes you plan to provide to Workato. Include all objects and features you plan to automate with the Coupa connector. The scopes you select must match the scopes you configure in Workato. You must include the `core.common.read` and `offline_access` scopes at a minimum to establish a connection.
   
   ![Coupa creating a client](/assets/coupa-create-client.BgDfen2E.png)_Create a new client_
   
7. Click **Save**.
   
8. Copy and store the **Identifier** and the **Secret** for use in Workato.
   
9. Return to your Workato account and go to the project where you plan to add your connection.
   
10. Click **Create > Connection** or press C twice.
    
11. Search for and select `Coupa` as your connection on the **New connection** page.
    
12. Provide a unique name for the connection in the **Connection name** field.
    
13. Use the **Location** drop-down menu to select the project where you plan to store the connection.
    
14. Use the **Authentication** drop-down to select the **Grant type** provided in Coupa.
    
15. Enter the **Client ID** and **Client secret**.
    
16. Enter the Coupa URL for your instance in the **Host** field. For example, enter `acme` if your URL is `http://acme.coupacloud.com`.
    
17. Use the **Scopes** drop-down menu to select the same scopes you configured in Coupa. Include the required scopes `core.common.read` and `offline_access` to connect successfully.
    
18. Click **Connect**.
    

#### Coupa role requirements

Each tool's availability depends on the permissions granted to the connected account. Actions run with the authenticated approver's own Coupa permissions through [Verified user access](/en/mcp/verified-user-access), using an OAuth 2.0 Authorization Code Grant connection instead of a shared service account. A request made without the required permission returns a permission-denied outcome.

## How to use Coupa Approval Operations MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_pending\_approvals tool

The **search\_pending\_approvals** tool finds pending approvals and surfaces the oldest pending items first by default. You can also sort by newest pending items and filter by approver and elapsed time. Your LLM uses this tool to discover what approvals are awaiting your decision, identify stalled items, and monitor organization-wide approval queues.

**Try asking**:

- `What approvals are waiting for my decision?`
- `Show me my most stalled pending approvals.`
- `What has been pending for more than 5 days?`
- `Show me all stalled approvals across the organization.`

### get\_approval tool

The **get\_approval** tool retrieves an approval, including its status, document summary, and available actions. Your LLM uses this tool to inspect an approval before taking action.

**Try asking**:

- `Get the details for approval ID 12345.`
- `Show me the full context for this approval.`
- `Retrieve the document summary for the pending invoice.`
- `What are the details and who requested this approval?`

### approve\_approval tool

The **approve\_approval** tool approves a pending approval. The tool refuses the action if the approval has changed since it was last reviewed. Your LLM uses this tool to approve a pending item after showing the document summary and obtaining confirmation.

**Try asking**:

- `Approve this requisition.`
- `Approve the pending purchase order.`
- `I approve this expense report.`
- `Go ahead and approve this approval.`

### reject\_approval tool

The **reject\_approval** tool rejects a pending approval. The tool requires you to specify a reason for rejection. Your LLM uses this tool to reject a pending item and record the reason for the rejection.

**Try asking**:

- `Reject this invoice because it exceeds the approved budget.`
- `I'm rejecting this requisition because it exceeds the approved amount.`
- `Decline this approval because supporting documentation is missing.`
- `Reject this contract approval because it needs legal review before proceeding.`

### hold\_approval tool

The **hold\_approval** tool places a pending approval on hold. The tool refuses to place an approval on hold if the approval is ineligible. Your LLM uses this tool to pause a decision pending further review.

**Try asking**:

- `Place this purchase order on hold for further review.`
- `Hold this approval pending additional clarification.`
- `I need to put this requisition on hold temporarily.`
- `Hold this approval while we wait for more information.`

### request\_approval\_info tool

The **request\_approval\_info** tool posts a comment on the underlying document asking the requester for more detail, without deciding the approval. Your LLM uses this tool to request missing details before approving, rejecting, or holding.

**Try asking**:

- `Ask the requester for more details before I approve this.`
- `Request more information from the requester about the project scope.`
- `Ask for the budget justification for this approval.`
- `Post a comment asking the requester to provide the missing supporting documents.`

## Getting started

View and manage your MCP server tools in the **Details** tab **Tools** section. Tool management provides the following capabilities:

- [Start tools](/en/mcp/manage-tools#start-tools)
- [Remove tools](/en/mcp/manage-tools#remove-tools)
- [Edit tools](/en/mcp/manage-tools#edit-tools)
- [Add tools](/en/mcp/manage-tools#add-tools)
- [Edit your LLM-facing MCP server description](/en/mcp/prebuilt-mcps#edit-llm-facing-mcp-server-description)

> **TOOLS MUST BE STARTED**
> 
> Your LLM can only access active tools in your MCP server connector.
