---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/quickbooks-online-ap-and-expenses-mcp-server.md
description: >-
  Use the QuickBooks Online AP and Expenses MCP server to connect your LLM to
  QuickBooks Online with tools to list, review, and record expenses, and look up
  vendors and accounts through natural language.
---

# QuickBooks Online AP and Expenses MCP server

The QuickBooks Online AP and Expenses MCP server enables LLMs to work with QuickBooks Online expense workflows through natural conversation. This MCP server supports accounts payable and expense workflows. It helps you track spending, analyze how money flows, and record transactions with accurate classification. It provides tools to list expenses, retrieve expense details, and record new expenses without interacting directly with the QuickBooks Online interface.

## Uses

Use the QuickBooks Online AP and Expenses MCP server to perform the following actions:

- List expense transactions with optional filters such as date range and account
- Retrieve detailed information for a specific expense transaction
- Record a new expense transaction using vendor and account references
- Search for vendors by name or partial identifier
- Retrieve full details for a specific vendor
- Search for accounts (categories) by name or partial identifier
- Retrieve full details for a specific account

### Example prompts

Use the following example prompts to invoke QuickBooks Online AP and Expenses MCP server tools:

- `Show me all expenses from the past 30 days.`
- `List expenses charged to the Travel account this quarter.`
- `Get the details for this expense transaction.`
- `Record a $250 expense from Office Depot for office supplies.`
- `Find the vendor record for Staples.`
- `Look up the Office Supplies account before I log this expense.`
- `Get the full details for this vendor.`
- `Retrieve the details for this account category.`

## QuickBooks Online AP and Expenses MCP server tools

The QuickBooks Online AP and Expenses MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_expenses](#list-expenses-tool) | Retrieves a list of expense transactions with optional filters, such as date range and account. |
| [get\_expense](#get-expense-tool) | Retrieves detailed information for an expense transaction you specify. |
| [record\_expense](#record-expense-tool) | Creates a new expense transaction using vendor and account references. |
| [search\_vendors](#search-vendors-tool) | Searches for vendors using a name or partial identifier. |
| [get\_vendor](#get-vendor-tool) | Retrieves full details for a vendor you specify. |
| [search\_accounts](#search-accounts-tool) | Searches for accounts or categories using a name or partial identifier. |
| [get\_account](#get-account-tool) | Retrieves full details for an account you specify. |

## Install the QuickBooks Online AP and Expenses MCP server

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
    

### QuickBooks Online connection setup

View QuickBooks Online connection setup steps

### Supported editions and versions

View Supported editions and versions

The QuickBooks connector works with the following QuickBooks Online versions:

- QuickBooks Self-Employed
- QuickBooks Simple Start
- QuickBooks Essentials
- QuickBooks Plus

Workato doesn't support QuickBooks Desktop/Enterprise versions.

### How to connect to QuickBooks on Workato

View How to connect to QuickBooks on Workato steps

Complete the following steps to establish a connection to QuickBooks Online in Workato:

1. Provide a **Connection name** that identifies which QuickBooks instance Workato is connected to.
   
   ![QuickBooks online connection](/assets/QBO_connect1.D_Fk-JGJ.png)_QuickBooks online connection_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **Sandbox** drop-down menu to specify whether the QuickBooks Online account is a sandbox account.
   
4. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
5. Click **Connect to QuickBooks** to open the QuickBooks sign in window.
   
   ![Connect to QuickBooks Online](/assets/QBO_connect2.DOeG2fRE.png)_Connect to QuickBooks Online_
   
6. Enter your QuickBooks Online account email address and password.
   
7. Click **Sign in** to complete the connection.
   

## How to use QuickBooks Online AP and Expenses MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_expenses tool

The **list\_expenses** tool retrieves a list of expense transactions with optional filters, such as date range and account. Your LLM uses this tool to view, list, or review expenses, including requests for recent expenses or expenses within a specific date range.

**Try asking**:

- `Show me all expenses from the past 30 days.`
- `List expenses charged to the Travel account this quarter.`
- `What have we spent in the last week?`
- `Show me all expenses from last month.`

### get\_expense tool

The **get\_expense** tool retrieves detailed information for an expense transaction you specify. Your LLM uses this tool to retrieve details for a expense.

**Try asking**:

- `Get the details for this expense transaction.`
- `Show me the full breakdown for this expense.`
- `What vendor and account is this expense recorded under?`
- `Pull up the details for the expense I logged yesterday.`

### record\_expense tool

The **record\_expense** tool creates a new expense transaction using vendor and account references. Your LLM resolves these references and prompts for any missing details before it records the expense.

**Try asking**:

- `Record a $250 expense from Office Depot for office supplies.`
- `Log a travel expense from last week.`
- `Record a software subscription charge under the Software account.`
- `Add this receipt as an expense transaction.`

### search\_vendors tool

The **search\_vendors** tool searches for vendors using a name or partial identifier. Your LLM uses this tool to find a vendor reference for an expense workflow when you provide a name or partial identifier.

**Try asking**:

- `Find the vendor record for Staples.`
- `Search for a vendor named Office Depot.`
- `Look up this vendor before I record the expense.`
- `Find all vendors matching this partial name.`

### get\_vendor tool

The **get\_vendor** tool retrieves full details for a vendor you specify. Your LLM uses this tool to search by vendor ID to obtain complete vendor details for an expense workflow.

**Try asking**:

- `Get the full details for this vendor.`
- `Show me all information for this vendor record.`
- `Retrieve the payment details for this vendor.`
- `Pull up the full profile for this vendor.`

### search\_accounts tool

The **search\_accounts** tool searches for accounts or categories using a name or partial identifier. Your LLM uses this tool to provide an account or category reference for expense classification.

**Try asking**:

- `Look up the Office Supplies account before I log this expense.`
- `Search for the Travel and Entertainment account.`
- `Find the right expense category for this transaction.`
- `What accounts are available for classifying this expense?`

### get\_account tool

The **get\_account** tool retrieves full details for an account you specify. Your LLM uses this tool to search by account ID to obtain complete account details for expense classification.

**Try asking**:

- `Retrieve the details for this account category.`
- `Show me the full details for the Travel account.`
- `Get the account information before I classify this expense.`
- `Pull up the details for this expense account.`

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
