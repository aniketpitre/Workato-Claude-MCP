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
