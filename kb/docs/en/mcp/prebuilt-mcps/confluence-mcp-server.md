---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/confluence-mcp-server.md'
description: >-
  Use the Confluence MCP server to connect your LLM to Confluence with a curated
  set of tools to retrieve content, create pages, view attachments, update
  pages, and archive pages.
---

# Confluence MCP server

The Confluence MCP server enables LLMs to read and write documentation stored in Confluence Cloud through natural conversation. It provides tools to retrieve content, create pages, view attachments, update pages, and archive pages directly from AI environments without requiring direct interaction with the Confluence interface.

## Uses

Use the Confluence MCP server when you plan to perform the following actions:

- Search for Confluence pages by keywords or natural language queries
- Retrieve and read page content for summarization or analysis
- Understand page hierarchy and document structure
- View attachments associated with specific pages
- Create new documentation pages in specified spaces
- Update existing pages with revised content
- Append new sections to existing pages without rewriting
- Archive pages to retire content without deletion

### Example prompts

Use the following example prompts to invoke Confluence MCP server tools:

- `Find pages about the API authentication process.`
- `Read the onboarding documentation page.`
- `Show me the page hierarchy for the project requirements doc.`
- `What attachments are on the architecture design page?`
- `Create a new page in the Engineering space for the deployment guide.`
- `Update the troubleshooting page with the new error codes.`
- `Append this week's status update to the project log page.`
- `Archive the deprecated product specification page.`

## Confluence MCP server tools

The Confluence MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_pages](#search-pages-tool) | Searches for Confluence pages that match a natural-language or keyword query. |
| [get\_page](#get-page-tool) | Retrieves the full content and metadata of a single Confluence page. |
| [get\_page\_hierarchy](#get-page-hierarchy-tool) | Retrieves the parent and immediate children of a page to provide structural context. |
| [get\_attachments](#get-attachments-tool) | Retrieves metadata and access URLs for attachments associated with a page. |
| [create\_page](#create-page-tool) | Creates a new Confluence page in a space or under a specific parent. |
| [update\_page](#update-page-tool) | Performs a full-content update of an existing Confluence page. |
| [append\_to\_page](#append-to-page-tool) | Appends new content to the bottom of an existing Confluence page. |
| [archive\_page](#archive-page-tool) | Archives an existing page without deleting it. |

## Install the Confluence MCP server

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
    

## Confluence connection setup

View Confluence connection setup steps

The Confluence connector supports the following authentication types:

- [Basic](#basic)
- [API token](#api-token)
- [OAuth 2.0](#oauth)

### Basic authentication

Use basic authentication with your Confluence username and password.

View basic authentication steps

Complete the following steps to set up a basic authentication connection to Confluence in Workato:

1. Click **Create > Connection**.
   
2. Search for `Confluence` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Confluence basic connection](/assets/confluence-basic-connection.C9dhQeh0.png)_Basic connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select **Cloud** for Confluence cloud instances or the corresponding option for on-prem connections. Refer to [Connections using an on-prem agent](/en/on-prem/agents/connection) for more information.
   
6. Use the **Auth type** drop-down menu to select **Basic**.
   
7. Enter your subdomain for cloud instances in the **Confluence subdomain** field. This is typically found in the Confluence URL. For example, your subdomain is `acme` if your URL is `https://acme.atlassian.net`.
   
8. Optionally, select **Enter on-prem URI** from the drop-down menu and enter your Confluence URI in the **Confluence domain** field. This is the root URI of your on-prem Confluence host. For example, `https://confluence.intranet.acme.com:7654`. You might need to add Workato's IP address to the allowlist to connect. Refer to [IP allowlists](/en/security/ip-allowlists) for more information.
   
9. Enter your Confluence **Username** and **Password**.
   
10. Click **Connect**.
    

### API token authentication

You must generate an API token to use API token authentication.

#### Confluence setup for API token authentication

View generate API token steps

Complete the following steps to generate an API token in Confluence:

1. Go to the Atlassian [API Tokens](https://id.atlassian.com/manage/api-tokens) page.
   
2. Click **Create API token**.
   
3. Enter a **Name** and select an **Expires on** date.
   
4. Click **Create**.
   
5. Copy and save the **API token** for use in Workato.
   

#### Connect to Confluence with API token authentication

View connect to Confluence with API token authentication steps

Complete the following steps to set up an API token connection to Confluence in Workato:

1. Click **Create > Connection**.
   
2. Search for `Confluence` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Confluence API token connection](/assets/confluence-api-token-connection.U-D2amgE.png)_API token connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select **Cloud** for Confluence cloud instances or the corresponding option for on-prem connections. Refer to [Connections using an on-prem agent](/en/on-prem/agents/connection) for more information.
   
6. Use the **Auth type** drop-down menu to select **API token**.
   
7. Enter your subdomain for cloud instances in the **Confluence subdomain** field. This is typically found in the Confluence URL. For example, your subdomain is `acme` if your URL is `https://acme.atlassian.net`.
   
8. Optionally, select **Enter on-prem URI** from the drop-down menu and enter your Confluence URI in the **Confluence domain** field. This is the root URI of your on-prem Confluence host. For example, `https://confluence.intranet.acme.com:7654`. You might need to add Workato's IP address to the allowlist to connect. Refer to [IP allowlists](/en/security/ip-allowlists) for more information.
   
9. Enter your **Email** and **API token**.
   
10. Click **Connect**.
    

### OAuth 2.0 authentication

You must generate a client ID and secret to use OAuth 2.0 authentication.

#### Confluence setup for OAuth 2.0 authentication

View generate client ID and secret steps

Complete the following steps to generate a client ID and secret in Confluence:

1. Log in to the Atlassian [Developer Console](https://developer.atlassian.com/console/myapps/).
   
2. Click **Create > OAuth 2.0 integration**.
   
3. Enter a **Name**.
   
4. Agree to the terms.
   
5. Click **Create**.
   
6. Click **Authorization** and then click **Add**.
   
7. Enter `https://www.workato.com/oauth/callback` in the **Callback URL** field and then click **Save changes**.
   
8. Click **Permissions**.
   
9. Click **Add** for the Confluence API.
   
10. Click **Configure**.
    
11. Click **Edit Scopes** under **Classic scopes**.
    
12. Select the following scopes:
    
    - `manage:confluence-configuration`
    - `read:confluence-groups`
    - `read:confluence-content.all`
    - `read:confluence-content.permission`
    - `read:confluence-content.summary`
    - `read:confluence-props`
    - `read:confluence-space.summary`
    - `read:confluence-user`
    - `read:page:confluence`
    - `readonly:content.attachment:confluence`
    - `search:confluence`
    - `write:confluence-content`
    - `write:confluence-file`
    - `write:confluence-groups`
    - `write:confluence-space`
13. Click **Save**.
    
14. Select **Settings**.
    
15. Copy and save the **Client ID** and **Secret** for use in Workato.
    

#### Connect to Confluence with OAuth 2.0 authentication

View connect to Confluence with OAuth 2.0 authentication steps

Complete the following steps to set up an OAuth 2.0 connection to Confluence in Workato:

1. Click **Create > Connection**.
   
2. Search for `Confluence` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Confluence OAuth connection](/assets/confluence-oauth-connection.Ck6ynxBz.png)_OAuth connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select **Cloud** for Confluence cloud instances or the corresponding option for on-prem connections. Refer to [Connections using an on-prem agent](/en/on-prem/agents/connection) for more information.
   
6. Use the **Auth type** drop-down menu to select **OAuth 2.0**.
   
7. Enter your subdomain for cloud instances in the **Confluence subdomain** field. This is typically found in the Confluence URL. For example, your subdomain is `acme` if your URL is `https://acme.atlassian.net`.
   
8. Optionally, select **Enter on-prem URI** from the drop-down menu and enter your Confluence URI in the **Confluence domain** field. This is the root URI of your on-prem Confluence host. For example, `https://confluence.intranet.acme.com:7654`. You might need to add Workato's IP address to the allowlist to connect. Refer to [IP allowlists](/en/security/ip-allowlists) for more information.
   
9. Enter the **Client ID** and **Client secret**.
   
10. Optionally, expand **Advanced settings** and select **Classic scopes** or **Granular scopes**.
    
11. Click **Connect**.
    
12. Choose a site from the **Use app on** drop-down menu. This is the Atlassian account your app accesses.
    
13. Click **Accept**.
    

## How to use Confluence MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_pages tool

The **search\_pages** tool searches for Confluence pages that match a natural-language or keyword query and returns a list of matching pages you're permitted to view. Your LLM uses this tool to find, look up, identify, or search for information that may exist in Confluence.

**Try asking**:

- `Find pages about API authentication.`
- `Search for documentation on the deployment process.`
- `Look up pages related to customer onboarding.`
- `Find the troubleshooting guides in the Engineering space.`

### get\_page tool

The **get\_page** tool retrieves the full content and metadata of a single Confluence page. Your LLM uses this to read, open, retrieve, or summarize a specific page.

**Try asking**:

- `Read the API documentation page.`
- `Show me the content of the onboarding guide.`
- `Summarize the project requirements page.`
- `Get the deployment instructions page.`

### get\_page\_hierarchy tool

The **get\_page\_hierarchy** tool retrieves the parent and immediate children of a page to provide context for document structure and placement. Your LLM uses this to understand how a page is organized, where it sits in the documentation structure, or where a newly created page should be placed.

**Try asking**:

- `Show me the page hierarchy for the product documentation.`
- `Where does the API guide page sit in the structure?`
- `What are the child pages under the onboarding documentation?`
- `How is the engineering wiki organized around this page?`

### get\_attachments tool

The **get\_attachments** tool retrieves metadata and access URLs for attachments associated with a page. Your LLM uses this tool to retrieve information about attachments on a specific page.

**Try asking**:

- `What attachments are on the architecture design page?`
- `Show me the files attached to the deployment guide.`
- `List the attachments on the API documentation.`
- `What documents are attached to the requirements page?`

### create\_page tool

The **create\_page** tool creates a new Confluence page in a space or under a specific parent, using content generated by your LLM. Your LLM uses this tool to create, draft, or publish a new document, specification, summary, or knowledge artifact in Confluence.

**Try asking**:

- `Create a new page in the Engineering space for the deployment guide.`
- `Draft a troubleshooting page under the API documentation.`
- `Publish a new onboarding checklist in the HR space.`
- `Create a meeting notes page for today's planning session.`

### update\_page tool

The **update\_page** tool performs a full-content update of an existing Confluence page. Your LLM uses this tool to revise, rewrite, or replace the content of an existing page.

**Try asking**:

- `Update the API authentication page with the new OAuth flow.`
- `Revise the troubleshooting guide with the latest error codes.`
- `Rewrite the deployment instructions to include the new steps.`
- `Update the product requirements page with the revised specs.`

### append\_to\_page tool

The **append\_to\_page** tool appends new content to the bottom of an existing Confluence page without rewriting the entire page body. Your LLM uses this tool to add a section, add a log entry, post a weekly update, or append content without modifying the existing body.

**Try asking**:

- `Append this week's status update to the project log page.`
- `Add a new troubleshooting entry to the FAQ page.`
- `Post today's meeting notes to the weekly updates page.`
- `Add a new section about the feature to the product documentation.`

### archive\_page tool

The **archive\_page** tool archives an existing page without deleting it to preserve full recoverability and traceability. Your LLM uses this tool to retire, deprecate, or archive a page to remove it from active use without deleting it.

**Try asking**:

- `Archive the deprecated product specification page.`
- `Retire the old API documentation page.`
- `Archive the Q3 planning page now that Q4 has started.`
- `Remove the outdated onboarding guide from active documentation.`

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

---

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

---

---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/coupa-procurement-receiving-mcp-server.md
description: >-
  Use the Coupa Procurement & Receiving MCP server to connect your LLM to Coupa
  with tools to create and track purchase requests, review and change purchase
  orders, record goods receipts, and search the approved catalog.
---

# Coupa Procurement & Receiving MCP server

The Coupa Procurement & Receiving MCP server enables LLMs to manage Coupa procurement and receiving through natural conversation. It provides tools to create and track purchase requests, review and close purchase orders, submit purchase order change requests, record goods receipts to enable three-way invoice matching, and search the approved catalog. The server resolves its own suppliers, accounts, and users, so it can be deployed on its own, without requiring direct interaction with the Coupa interface.

## Uses

Use the Coupa Procurement & Receiving MCP server to perform the following actions:

- Create purchase requests with catalog or free-form lines and submit them for native Coupa approval.
- Track a purchase request's status and approval position, and confirm purchase order generation once approved.
- Search and review purchase orders by supplier, status, date, or requester.
- Request changes to an issued purchase order, with protection against acting on stale data.
- Close purchase orders that are fully received and no longer expect further invoices.
- Record goods receipts against purchase order lines to enable three-way invoice matching.
- Search the approved catalog for line-ready item detail before adding items to a request.
- Monitor pending approval steps across purchase requests and purchase orders.
- Resolve suppliers, accounts, and users to compact reference records before a write.

### Example prompts

Use the following example prompts to invoke Coupa Procurement & Receiving MCP server tools:

- `Create a purchase request for 10 laptop stands from Acme Corp, coded to the Facilities account.`
- `Submit my draft purchase request for approval.`
- `Where does my purchase request for office chairs stand?`
- `Show me all purchase orders from Acme Corp issued this quarter.`
- `Has this purchase order been received yet?`
- `Request a quantity change on this purchase order before I approve the invoice.`
- `Close this purchase order, everything on it has been received.`
- `Record a receipt of 5 units against this purchase order line.`
- `Find approved catalog items for standing desks.`
- `What's waiting in my approval queue right now?`

## Coupa Procurement & Receiving MCP server tools

The Coupa Procurement & Receiving MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [create\_requisition](#create-requisition-tool) | Creates a purchase request with resolved references, and optionally submits it for approval. |
| [submit\_requisition](#submit-requisition-tool) | Submits a draft purchase request for native Coupa approval routing. |
| [get\_requisition](#get-requisition-tool) | Retrieves a purchase request's status, paged lines, line suppliers, and available approval summary. |
| [search\_requisitions](#search-requisitions-tool) | Finds purchase requests by requester, supplier, status, or date range. |
| [search\_purchase\_orders](#search-purchase-orders-tool) | Searches purchase orders by supplier, status, date range, or requester. |
| [get\_purchase\_order](#get-purchase-order-tool) | Retrieves full purchase order header, paged lines, version, and available approval summary. |
| [search\_pending\_approvals](#search-pending-approvals-tool) | Finds pending approval steps on purchase requests and purchase orders, filterable by approver and elapsed time. |
| [request\_po\_change](#request-po-change-tool) | Creates a concurrency-checked purchase order change request and submits it for approval. |
| [close\_purchase\_order](#close-purchase-order-tool) | Closes an eligible, fully received purchase order. |
| [create\_receipt](#create-receipt-tool) | Records a positive goods-receipt transaction against a purchase order line. |
| [search\_catalog\_items](#search-catalog-items-tool) | Searches the approved catalog and returns line-ready item detail. |
| [search\_suppliers](#search-suppliers-tool) | Finds suppliers by name and returns compact reference records. |
| [search\_accounts](#search-accounts-tool) | Finds account and cost-center codes and returns compact reference records. |
| [search\_users](#search-users-tool) | Finds Coupa users by name or email and returns compact reference records. |

## Install the Coupa Procurement & Receiving MCP server

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
    

## Coupa Procurement & Receiving connection setup

View Coupa Procurement & Receiving connection setup steps

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

Each tool's availability depends on the permissions granted to the connected account. Actions run with the authenticated user's own Coupa permissions through [Verified user access](/en/mcp/verified-user-access), using an OAuth 2.0 Authorization Code Grant connection instead of a shared service account. A request made without the required permission returns a permission-denied outcome rather than a partial result.

### Project property configuration

The Coupa Procurement & Receiving MCP server supports the following project-level properties to control behavior and defaults:

| Project-level property | Description |
| --- | --- |
| `requisition_custom_field_schema` | Specify the tenant-required purchase request custom fields, and how to supply them to **create\_requisition**. |
| `po_change_allowed_fields` | Specify header and line fields the tenant permits in a purchase order change request. |
| `po_change_reason_mapping` | Specify valid purchase order change reason values, the Coupa field they map to, and whether a reason is required. |
| `default_receiving_warehouse_id` | Configure the default receiving warehouse used by **create\_receipt**. This isn't exposed as a tool parameter. |
| `default_receiving_warehouse_location_id` | Configure the default receiving warehouse location used by **create\_receipt**. This isn't exposed as a tool parameter. |
| `idempotency_retention_days` | Enter the retention window, in days, for the server-layer duplicate-protection store. The minimum is `1`, the maximum is `30`, and the default is `7`. |
| `budget_enforcement` | Configure the MCP-layer budget preflight policy that applies when submitting a purchase request. Options include `block`, `advisory`, and `off`. The default is `block`. This doesn't override Coupa's own native budget validation, which still applies in every mode. |

View project-level property configuration steps

Complete the following steps to configure your project-level properties:

1. Sign in to your Workato account and select **Projects**.
   
2. Select the project that contains your MCP server.
   
3. Click the **Settings** tab.
   
   ![Click the Settings tab](/assets/project-settings.99X6TiYd.png)_Click the **Settings** tab._
   
4. Select **Project properties**.
   
5. Locate the project property you plan to update and click the **Edit** (pencil) icon.
   
6. Enter your changes in the **Value** field.
   

## How to use Coupa Procurement & Receiving MCP server tools

Refer to the following sections for detailed information on available tools:

### create\_requisition tool

The **create\_requisition** tool creates a purchase request with resolved references and optionally submits it for approval. Your LLM uses this tool after you select catalog items or specify free-form lines and confirm the requester, lines, coding, ship-to, need-by date, and total.

**Try asking**:

- `Create a purchase request for 10 laptop stands from Acme Corp, coded to the Facilities account.`
- `Draft a request for 5 units of the standing desk from the catalog.`
- `Create and submit a purchase request for a contractor invoice, need-by end of month.`
- `Start a purchase request for office supplies, I'll submit it later.`

### submit\_requisition tool

The **submit\_requisition** tool submits a draft purchase request for native Coupa approval routing. Your LLM uses this tool to submit the draft for approval when you confirm it's ready.

**Try asking**:

- `Submit my draft purchase request for approval.`
- `I've reviewed the request, go ahead and submit it.`
- `Send the office supplies request for approval now.`

### get\_requisition tool

The **get\_requisition** tool retrieves a purchase request's status, paged lines, line suppliers, and available approval summary. Your LLM uses this tool to check a specific request's detail or approval position after locating it with **search\_requisitions**.

**Try asking**:

- `Where does my purchase request for office chairs stand?`
- `Show me the lines and suppliers on this purchase request.`
- `Who still needs to approve this request?`
- `Pull up the full detail for this purchase request.`

### search\_requisitions tool

The **search\_requisitions** tool finds purchase requests by requester, supplier, status, or date range and presents candidates for you to choose from when several match. Your LLM uses this tool to locate a request when you can't identify it by internal ID.

**Try asking**:

- `Find my purchase requests from this month.`
- `Show me all pending purchase requests for Acme Corp.`
- `Find the purchase request I submitted last week.`
- `List requests that are still in draft status.`

### search\_purchase\_orders tool

The **search\_purchase\_orders** tool searches purchase orders by supplier, status, date range, or requester. Your LLM uses this tool to find, review, or list purchase orders, or to confirm that a purchase order was generated after a request was approved.

**Try asking**:

- `Show me all purchase orders from Acme Corp issued this quarter.`
- `Did my purchase request turn into a purchase order yet?`
- `Find open purchase orders for the Facilities account.`
- `List purchase orders issued in the last 30 days.`

### get\_purchase\_order tool

The **get\_purchase\_order** tool retrieves full purchase order header, paged lines, version, and available approval summary. Your LLM uses this tool to capture the current version before requesting a change, or to obtain the order-line ID before recording a receipt.

**Try asking**:

- `Has this purchase order been received yet?`
- `Show me the full detail for this purchase order.`
- `What's the remaining balance on this purchase order's lines?`
- `Pull up this purchase order before I request a change.`

### search\_pending\_approvals tool

The **search\_pending\_approvals** tool finds pending approval steps on purchase requests and purchase orders, filterable by approver and elapsed time. Your LLM uses this tool to check what's awaiting approval, who holds it, or what's been pending the longest. This tool is read-only and doesn't act on approvals.

**Try asking**:

- `What's waiting in my approval queue right now?`
- `Which approvals have been pending the longest?`
- `Show me approvals that have been stuck for more than 5 days.`
- `What purchase requests are waiting on my approval?`

### request\_po\_change tool

The **request\_po\_change** tool creates a concurrency-checked purchase order change request and submits it for approval. Your LLM retrieves the current purchase order first, shows you the before and after values, and only proceeds after you confirm.

**Try asking**:

- `Request a quantity change on this purchase order before I approve the invoice.`
- `Change the need-by date on this purchase order to next Friday.`
- `Update the ship-to address on this purchase order.`
- `Reduce the quantity on this line to match what we actually ordered.`

### close\_purchase\_order tool

The **close\_purchase\_order** tool closes an eligible, fully received purchase order, which stops further receiving and invoicing against it. Your LLM uses this tool to close the order when you confirm it's fully received and no more invoices are expected.

**Try asking**:

- `Close this purchase order, everything on it has been received.`
- `This order is complete, go ahead and close it.`
- `Stop any further invoicing against this purchase order.`

### create\_receipt tool

The **create\_receipt** tool records a positive goods-receipt transaction against a purchase order line. Your LLM uses this tool to record the receipt once you confirm physical receipt of goods, using the order-line ID from **get\_purchase\_order**.

**Try asking**:

- `Record a receipt of 5 units against this purchase order line.`
- `We received the full order today, log the receipt.`
- `Record a partial receipt of 3 units for this line.`
- `Log today's delivery against this purchase order.`

### search\_catalog\_items tool

The **search\_catalog\_items** tool searches the approved catalog and returns line-ready item detail. Your LLM uses this tool to find items when you want to buy from the approved catalog, and presents results for you to select before creating a purchase request line.

**Try asking**:

- `Find approved catalog items for standing desks.`
- `Search the catalog for wireless keyboards.`
- `What laptop stands are available in the catalog from Acme Corp?`
- `Show me catalog items under the office furniture commodity.`

### search\_suppliers tool

The **search\_suppliers** tool finds suppliers by name and returns compact reference records. Your LLM uses this tool to resolve a supplier reference before a write, and presents candidates for you to choose from when several match.

**Try asking**:

- `Find the supplier record for Acme Corp.`
- `Search for active suppliers matching "Acme".`
- `Look up this supplier before I add a line to my request.`

### search\_accounts tool

The **search\_accounts** tool finds account and cost-center codes and returns compact reference records. Your LLM uses this tool to resolve account coding before a write, and presents candidates for you to choose from when several match.

**Try asking**:

- `Find the Facilities account for coding this request.`
- `Search for accounts matching "Marketing".`
- `Look up the right cost-center code before I submit this line.`

### search\_users tool

The **search\_users** tool finds Coupa users by name or email and returns compact reference records. Your LLM uses this tool to resolve a requester reference, and presents candidates for you to choose from when several match.

**Try asking**:

- `Find the user record for sasha@example.com.`
- `Search for Coupa users named Chen.`
- `Look up this requester before I create the request on their behalf.`

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

---
