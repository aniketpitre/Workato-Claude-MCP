---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/xero-ap-and-expenses-mcp-server.md
description: >-
  Use the Xero AP and Expenses MCP server to connect your LLM to Xero with tools
  to create, approve, and void supplier bills, and import batches of spend-money
  expenses with duplicate detection.
---

# Xero AP and Expenses MCP server

The Xero AP and Expenses MCP server enables LLMs to interact with Xero for the accounts-payable side of the ledger through natural conversation. It provides tools to create and manage supplier bills and import batches of spend-money expenses, without requiring direct interaction with the Xero interface.

## Uses

Use the Xero AP and Expenses MCP server to perform the following actions:

- Discover the Xero organizations associated with the connected account before you target a write.
- Create and approve supplier bills for payment queues.
- Approve draft supplier bills, including drafts that arrived through Hubdoc.
- Void duplicate or erroneous approved bills after explicit confirmation.
- Import batches of spend-money expenses through a preview-then-commit safety check.
- Resolve a bill or supplier contact before approving, voiding, or creating a bill.

### Example prompts

Use the following example prompts to invoke Xero AP and Expenses MCP server tools:

- `Which Xero organizations are connected to this account?`
- `Enter a supplier bill from Acme Corp for $2,400, already approved for payment.`
- `Bill our facilities account for this month's rent from Acme Corp, already approved.`
- `Approve the draft bill from Acme Corp due September 15.`
- `Void the duplicate bill I created for Acme Corp yesterday.`
- `Import this batch of card expenses and flag any duplicates before posting.`
- `Check whether this bill has any payments applied before I void it.`
- `Find the contact record for Acme Corp.`

## Xero AP and Expenses MCP server tools

The Xero AP and Expenses MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_organizations](#list-organizations-tool) | Lists the Xero organizations available to the connected account. |
| [create\_bill](#create-bill-tool) | Creates a supplier bill directly in approved status in a chosen Xero organization. |
| [authorize\_bill](#authorize-bill-tool) | Approves an existing draft supplier bill and sets its status to `AUTHORISED`. |
| [void\_bill](#void-bill-tool) | Voids a supplier bill after explicit confirmation. |
| [import\_expenses](#import-expenses-tool) | Imports a batch of spend-money expenses through a preview-then-commit flow with duplicate detection. |
| [resolve\_bill](#resolve-bill-tool) | Looks up one bill's write-gate preconditions: status, outstanding amount, payments, and credit allocations. |
| [resolve\_supplier\_contact](#resolve-supplier-contact-tool) | Resolves a supplier name to a contact ID by exact match. |

## Install the Xero AP and Expenses MCP server

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
    

## Xero AP and Expenses connection setup

View Xero AP and Expenses connection setup steps

### API version

The Xero connector uses the [Xero Accounting API](https://developer.xero.com/documentation/api/api-overview). Review the Xero Accounting API documentation to fully understand the integration possibilities with Workato recipes.

### How to connect to Xero in Workato

View OAuth connection setup steps

Complete the following steps to connect to Xero in Workato:

1. Enter a unique **Connection name** to identify the Xero instance you plan to connect with Workato.
   
2. Select `Yes` if your Xero account is enabled for **Payroll**. Payroll connectivity is available only for AU and US editions.
   
3. Provide the exact **Tenant name** for the connection. This field is case-sensitive.
   
4. Specify the required **Decimal precision** for line item calculations. This field defaults to 2 if left blank.
   
5. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
6. Click **Connect** to sign in to your Xero account and complete the setup process.
   
   ![Xero login](/assets/xero-login.HXP2RUNj.png)_Xero login_
   

#### Xero role requirements

Each tool's availability depends on the permissions granted to the connected account. A request made without the required permission returns a permission-denied outcome rather than a partial result. Refer to the Xero [User roles and permissions in Xero Business edition](https://central.xero.com/s/article/User-roles-and-permissions-in-Xero-Business-edition-US) guide for the complete list of role capabilities.

## How to use Xero AP and Expenses MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_organizations tool

The **list\_organizations** tool lists the Xero organizations available to the connected account, each with its Tenant ID, name, and type. Your LLM uses this tool to discover or disambiguate the target organization before any write when more than one organization may be connected.

**Try asking**:

- `Which Xero organizations are connected to this account?`
- `Show me the Tenant ID for our UK entity.`
- `List every Xero organization I can act on.`

### create\_bill tool

The **create\_bill** tool creates a new supplier bill directly in approved status in a chosen Xero organization, with a known supplier contact and line items. Your LLM uses this tool to enter a bill and immediately queue it for payment. The tool uses an account code that already exists in the organization's chart of accounts instead of creating a new one.

**Try asking**:

- `Enter a supplier bill from Acme Corp for $2,400, already approved for payment.`
- `Bill our facilities account for this month's rent from Acme Corp.`
- `Record an approved bill for 10 hours of contractor work at $150 an hour.`

### authorize\_bill tool

The **authorize\_bill** tool approves an existing draft supplier bill, including drafts that arrived through Hubdoc, and sets its status to `AUTHORISED`. You must supply a due date. Your LLM uses this tool to approve a bill without changing its contents.

**Try asking**:

- `Approve the draft bill from Acme Corp due September 15.`
- `Authorize the Hubdoc bill that's still in draft due by the end of the month.`
- `Approve bill 7e11f003-5c8f-47be-465b-83f9649a13d0 due in thirty days.`

### void\_bill tool

The **void\_bill** tool irreversibly voids a supplier bill after your explicit confirmation. Your LLM uses this tool to void a specific bill.

**Try asking**:

- `Void the duplicate bill I created for Acme Corp yesterday.`
- `Cancel this bill, it was entered by mistake.`
- `Yes, void that bill, I'm sure it's a duplicate.`

### import\_expenses tool

The **import\_expenses** tool imports a batch of spend-money expenses through a preview-then-commit flow, validates every item, and flags suspected duplicates before anything posts. Your LLM uses this tool to preview the batch, show you the results, and commit only after you confirm.

**Try asking**:

- `Import this batch of card expenses and flag any duplicates before posting.`
- `Preview these spend-money transactions before we post them.`
- `Commit the previewed expense batch now, everything looks right.`

### resolve\_bill tool

The **resolve\_bill** tool looks up one bill's write-gate preconditions, including its status, outstanding amount, payments, and credit allocations. Your LLM uses this tool immediately before approving or voiding a bill, or to convert a bill number you gave it into a bill ID.

**Try asking**:

- `Check whether this bill has any payments applied before I void it.`
- `Look up the status of bill INV-0042 before I approve it.`
- `Does this bill have any credit notes allocated against it?`

### resolve\_supplier\_contact tool

The **resolve\_supplier\_contact** tool resolves a supplier name to a contact ID by exact match only, and doesn't create a new contact. Your LLM uses this tool immediately before creating a bill when you've given it a supplier name rather than a contact ID.

**Try asking**:

- `Find the contact record for Acme Corp.`
- `Look up the supplier contact for Acme Corp before I bill them.`
- `Is Acme Corp already set up as a supplier in this organization?`

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
