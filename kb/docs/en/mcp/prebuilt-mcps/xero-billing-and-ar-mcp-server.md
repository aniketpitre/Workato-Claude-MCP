---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/xero-billing-and-ar-mcp-server.md
description: >-
  Connect your LLM to Xero with tools to find, create, approve, send, and
  correct sales invoices, record payments, and set up repeating invoices across
  every connected Xero organization.
---

# Xero Billing and AR MCP server

The Xero Billing and AR MCP server enables LLMs to interact with Xero for the complete accounts-receivable lifecycle through natural conversation. It provides tools to find and inspect invoices and customers, create and manage invoices, issue credit notes, and set up recurring billing across every connected Xero organization, without requiring direct interaction with the Xero interface.

## Uses

Use the Xero Billing and AR MCP server to perform the following actions:

- Find and inspect sales invoices and customer contacts by natural description, including overdue balances.
- Create sales invoices as drafts with line items, account codes, and tax rates.
- Edit a draft invoice's contents before it's approved.
- Approve, void, and email invoices as they move through the sales-invoice lifecycle.
- Issue credit notes to correct an approved or paid invoice.
- Record customer payments against approved invoices.
- Set up repeating-invoice templates for retainers, subscriptions, and other recurring billing.
- Create and search customer contacts.
- Look up reference data such as account codes, tax rates, items, tracking categories, and branding themes.

### Example prompts

Use the following example prompts to invoke Xero Billing and AR MCP server tools:

- `Show me Acme Corp's open invoices.`
- `Find invoice INV-0042.`
- `Invoice Acme Corp $5,000 for consulting.`
- `Approve the draft invoice for Acme Corp and send it.`
- `Void the duplicate invoice I raised yesterday.`
- `Acme Corp paid invoice INV-0042 today. Record the payment.`
- `Issue Acme Corp a $500 credit note for a billing error.`
- `Bill Acme Corp $2,000 on the first of every month for their retainer.`
- `Which Xero organizations are connected to this account?`
- `Find the contact record for Acme Corp.`

## Xero Billing and AR MCP server tools

The Xero Billing and AR MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_organizations](#list-organizations-tool) | Lists the Xero organizations connected to this connection. |
| [search\_invoices](#search-invoices-tool) | Searches sales invoices in a chosen Xero organization by contact, status, number, reference, date range, or overdue state. |
| [get\_invoice](#get-invoice-tool) | Retrieves one sales invoice in full, including the precondition state this server's write tools gate on. |
| [create\_invoice](#create-invoice-tool) | Creates a sales invoice in a chosen Xero organization, as a draft or directly approved. |
| [update\_draft\_invoice](#update-draft-invoice-tool) | Updates the contents of an existing draft sales invoice. |
| [authorize\_invoice](#authorize-invoice-tool) | Approves an existing draft sales invoice, making it payable and shareable. |
| [void\_invoice](#void-invoice-tool) | Voids an unpaid sales invoice, canceling it irreversibly while preserving the audit trail. |
| [send\_invoice](#send-invoice-tool) | Emails a sales invoice to its contact using the organization's default template. |
| [create\_credit\_note](#create-credit-note-tool) | Creates a credit note in a chosen Xero organization. |
| [record\_payment](#record-payment-tool) | Records a customer payment against an approved sales invoice in a chosen Xero organization. |
| [create\_repeating\_invoice](#create-repeating-invoice-tool) | Creates a repeating sales-invoice template that generates invoices on a schedule. |
| [search\_customers](#search-customers-tool) | Searches customer contacts in a chosen Xero organization by name or email. |
| [create\_customer](#create-customer-tool) | Creates a customer contact in a chosen Xero organization. |
| [list\_reference\_data](#list-reference-data-tool) | Returns read-only reference data for a chosen organization. |

## Install the Xero Billing and AR MCP server

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
    

## Xero Billing and AR connection setup

View Xero Billing and AR connection setup steps

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

## How to use Xero Billing and AR MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_organizations tool

The **list\_organizations** tool lists the Xero organizations connected to this connection, each with its Tenant ID, name, and type. Your LLM uses this tool to discover or disambiguate the target organization before writing when more than one organization may be connected.

**Try asking**:

- `Which Xero organizations are connected to this account?`
- `Show me the Tenant ID for our UK entity.`
- `List every Xero organization I can act on.`

### search\_invoices tool

The **search\_invoices** tool searches sales invoices in a chosen Xero organization by contact, status, number, reference, date range, or overdue state. Your LLM uses this tool to find invoices from a natural reference and obtain the invoice ID needed before acting on one.

**Try asking**:

- `Show me Acme Corp's open invoices.`
- `Find everything unpaid over 30 days.`
- `List all invoices dated last month for Acme Corp.`
- `Which invoices are overdue right now?`

### get\_invoice tool

The **get\_invoice** tool retrieves one sales invoice in full, including the precondition state this server's write tools gate on: status, amount outstanding, payments and credit allocations applied, and whether the contact has an email on file. Your LLM uses this tool before any lifecycle write, so no second lookup is needed.

**Try asking**:

- `Show me the full details for invoice INV-0042.`
- `What's the status and amount outstanding on this invoice?`
- `Check whether this invoice's contact has an email on file before I send it.`

### create\_invoice tool

The **create\_invoice** tool creates a sales invoice in a chosen Xero organization for a known contact and line items, as a draft or directly approved. Your LLM uses this tool to issue a new invoice, looking up account codes and tax rates rather than inventing them.

**Try asking**:

- `Invoice Acme Corp $5,000 for consulting.`
- `Create a draft invoice for Acme Corp so I can review it before approving.`
- `Bill Acme Corp for 10 hours of consulting at $150 an hour.`

### update\_draft\_invoice tool

The **update\_draft\_invoice** tool updates a draft sales invoice's contents, such as its contact, dates, line items, reference, and currency. Your LLM uses this tool to modify a draft before approval.

**Try asking**:

- `Change the quantity on the Acme Corp draft invoice to 15 hours.`
- `Fix the due date on this draft invoice.`
- `Update the reference on the draft invoice for Acme Corp.`

### authorize\_invoice tool

The **authorize\_invoice** tool approves an existing draft sales invoice, making it payable and shareable. Your LLM uses this tool when you want to approve a draft without changing its contents.

**Try asking**:

- `Approve the draft invoice for Acme Corp.`
- `Authorize invoice INV-0042 so I can send it.`
- `Approve this draft now that the amounts look right.`

### void\_invoice tool

The **void\_invoice** tool irreversibly voids an unpaid sales invoice while preserving the audit trail. Your LLM uses this tool only with your explicit confirmation, and only when no payments or credit allocations are applied.

**Try asking**:

- `Void the duplicate invoice I raised yesterday.`
- `Cancel invoice INV-0042 because it wasn't meant to be issued.`
- `Yes, void that invoice, I'm sure it's a duplicate.`

### send\_invoice tool

The **send\_invoice** tool emails a shareable sales invoice to its contact using the organization's default template. Your LLM uses this tool to send or resend an invoice, confirming the shareable status and a contact email on file first.

**Try asking**:

- `Email the approved invoice to Acme Corp.`
- `Resend invoice INV-0042 to the customer.`
- `Send this invoice now that it's approved.`

### create\_credit\_note tool

The **create\_credit\_note** tool creates a customer credit note (the sanctioned correction for an approved or paid sales invoice) as a draft or approved. Your LLM uses this tool to correct or partially refund a sent invoice, and doesn't invent the amount or codes.

**Try asking**:

- `Issue Acme Corp a $100 credit note for a billing error.`
- `Issue a standalone credit note for Acme Corp.`
- `Credit Acme Corp for an overcharge on their account.`

### record\_payment tool

The **record\_payment** tool records a payment received from a customer against one approved sales invoice. It uses the amount, date, and the receiving account you provide. Your LLM uses this tool to book a payment you report without inferring which invoice it settles.

**Try asking**:

- `Acme Corp paid invoice INV-0042 today. Record $5,000 into the main account.`
- `Record a partial payment of $2,000 against this invoice.`
- `Log the payment we just received from Acme Corp.`

### create\_repeating\_invoice tool

The **create\_repeating\_invoice** tool creates a repeating sales-invoice template on a schedule, set to either save each generated invoice as a draft or approve and email it. Your LLM uses this tool to set up recurring billing, confirming the cadence and generation mode back to you.

**Try asking**:

- `Bill Acme Corp $2,000 on the first of every month for their retainer.`
- `Set up a weekly repeating invoice for this subscription.`
- `Create a recurring invoice template that auto-approves and emails each month.`

### search\_customers tool

The **search\_customers** tool searches customer contacts in a chosen Xero organization by name or email. Your LLM uses this tool to obtain a contact ID before creating an invoice, credit note, or repeating invoice, and to check whether a contact has an email on file before sending.

**Try asking**:

- `Find the contact record for Acme Corp.`
- `Look up jordan@example.com in this organization.`
- `Does Acme Corp have an email address on file?`

### create\_customer tool

The **create\_customer** tool creates a new customer contact with a name and optional email and details. Your LLM uses this tool to create a new customer contact after the **search\_customers** tool confirms no existing contact matches.

**Try asking**:

- `Create a new customer record for Acme Corp.`
- `Add a contact for Acme Corp with their billing email.`
- `Set up a new customer so I can invoice them.`

### list\_reference\_data tool

The **list\_reference\_data** tool returns one type of reference data for an organization each call (chart-of-accounts codes, tax rates, items, tracking categories, or branding themes). Your LLM uses this tool to supply valid codes instead of inventing them, and to find the receiving account for a payment.

**Try asking**:

- `Which account codes are available for consulting revenue?`
- `Show me the tax rates set up in this organization.`
- `Find a payments-enabled account to record this payment against.`

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
