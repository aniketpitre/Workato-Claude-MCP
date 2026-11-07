---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/workday-end-user-mcp-server.md'
description: >-
  Use the Workday End User MCP server to connect your LLM to Workday with a
  curated set of tools to manage employee profiles, time-off balances, and
  approval workflows.
---

# Workday End User MCP server

The Workday End User MCP server enables your LLM to access employee self-service workflows within Workday HCM through natural conversation. It provides tools to manage everyday HR tasks by allowing you to check your profile and reporting chain, view your team if you're a manager, check time-off balances, submit or cancel time-off requests, and approve or reject requests without requiring direct interaction with the Workday interface.

## Uses

Use the Workday End User MCP server when you plan to perform the following actions:

- View your employee profile, including job title, manager, and contact details
- Check who your direct manager is
- View your complete reporting chain
- See your direct reports if you're a manager
- Check your time-off balances by type
- View your time-off request history and status
- Submit new time-off requests
- Cancel pending time-off requests
- View time-off requests for your direct reports
- Approve or reject time-off requests for team members
- List available time-off types
- Get details about specific time-off plans

### Example prompts

Use the following example prompts to invoke Workday End User MCP server tools:

- `What's my job title and who is my manager?`
- `Show me my complete reporting chain.`
- `Who are my direct reports?`
- `How much PTO do I have available?`
- `Show me my time-off request history.`
- `Request 3 days of vacation for next week.`
- `Cancel my pending PTO request.`
- `Who on my team has pending time-off requests?`
- `Approve Mei's vacation request.`
- `What types of time off can I request?`

## Workday End User MCP server tools

The Workday End User MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [get\_my\_profile](#get-my-profile-tool) | Retrieves the employee's core worker profile information. |
| [get\_my\_manager](#get-my-manager-tool) | Retrieves the employee's direct manager information. |
| [get\_my\_reporting\_chain](#get-my-reporting-chain-tool) | Retrieves the employee's upward reporting hierarchy. |
| [list\_my\_direct\_reports](#list-my-direct-reports-tool) | Retrieves a manager's direct reports and their core profile information. |
| [get\_my\_time\_off\_balances](#get-my-time-off-balances-tool) | Retrieves the employee's time-off balances grouped by type. |
| [get\_direct\_report\_time\_off\_requests](#get-direct-report-time-off-requests-tool) | Retrieves time-off requests for a direct report. Your LLM uses this tool to view PTO requests for a direct report. |
| [submit\_time\_off\_request](#submit-time-off-request-tool) | Submits a new time-off request for the employee. |
| [cancel\_time\_off\_request](#cancel-time-off-request-tool) | Cancels a pending time-off request. |
| [action\_time\_off\_request](#action-time-off-request-tool) | Approves or rejects a time-off request for a direct report. |
| [list\_time\_off\_types](#list-time-off-types-tool) | Retrieves the employee's available time-off types. |
| [get\_direct\_report\_time\_off\_balances](#get-direct-report-time-off-balances-tool) | Retrieves a direct report's PTO balances for vacation days, sick days, or leave. |
| [list\_my\_time\_off\_requests](#list-my-time-off-requests-tool) | Lists the user's PTO history and time-off request status. |

## Install the Workday End User MCP server

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
    

## Workday REST connection setup

View Workday REST connection setup steps

The Workato Workday connector is categorized into three distinct types: the main Workday connector, the Workday Web Services connector, and the Workday REST connector. Each type follows a similar authentication pattern but differs slightly in support capabilities and functionalities.

The Workday REST API requires authentication through an OAuth client setup.

> **API CLIENTS FOR INTEGRATION NOT SUPPORTED**
> 
> Register a standard Workday API client to complete this connection. Workday API clients for Integration aren't supported in the Workday End User MCP server.

### Minimum permissions

View minimum permissions

The Workday End User MCP server requires the following minimum permissions:

**API client scopes for functional areas**

Add the following scopes:

- Organizations and Roles
- Staffing
- Tenant non-configurable
- Time Off and Leave

**Business process security policies for Request Time Off type**

Add the following scopes for each group:

**Employee As Self service security group**

- Request Time Off (REST Service)
- Cancel
- ViewAll

**Manager security group**

- Approve
- Deny
- ViewAll

**Business process security policies for Correct Time Off type**

**Employee As Self service security group**

- Correct Time Off Entry (REST Service)
- Cancel
- ViewAll

**Manager security group**

- Approve
- Deny
- ViewAll

### Register a new API client in Workday

View API client setup steps

The Workday End User MCP server authenticates each user individually through their own Workday login. The server doesn't use an Integration System User (ISU) like the Workday connector.

#### Register a new API client

Complete the following steps to register an API client in Workday REST:

1. Sign in to your Workday REST account.
   
2. Enter `Register API Client` to locate the **Register API Client** task.
   
3. Enter a name for your API client in the **Client Name** field.
   
4. Go to the **Client Grant Type** section and select **Authorization Code Grant**.
   
5. Go to the **Access Token Type** section and select **Bearer**.
   
6. Enter `https:www.workato.com/oauth/callback` in the **Redirection URI** field.
   
7. Enter `30` in the **Refresh Token Timeout (in days)** field.
   
8. Enter the scopes for the connection in the **Scope (Functional Areas)** field. Refer to [Workday End User MCP server Minimum permissions](/en/mcp/prebuilt-mcps/workday-end-user-mcp-server#minimum-permissions) if you're connecting to the Workday End User MCP server.
   
   ![Enter the scopes for the connection in the Scope (Functional Areas) field](/assets/api-client-rest.CIUw1iB9.png)_Enter the scopes for the connection in the **Scope (Functional Areas)** field_
   
9. Enter your client ID in the **Client ID** field.
   
10. Enter your REST API endpoint in the **Workday REST API Endpoint** field. You can find this endpoint in your API client details page in Workday. For example: `https://wd2-impl-services1.workday.com/xxx/api/v1/example`
    
11. Enter your token endpoint in the **Token Endpoint** field. You can find this endpoint in your API client details page in Workday. For example: `https://wd2-impl-services1.workday.com/xxx/oauth2/example/token`
    
12. Enter your authorization endpoint in the **Authorization Endpoint** field. You can find this endpoint in your API client details page in Workday. For example: `https://impl.workday.com/example/authorize`
    
13. Click **Done**.
    

#### Find your token endpoint URL

Complete the following steps to find your token endpoint URL in Workday:

1. Enter **View API Clients** into the search field in Workday.
   
2. Access the **View API Clients** report from the search results.
   
3. Save the URLs listed in the **Token Endpoint** and **Authorization Endpoint** fields. These URLs are required for the OAuth 2.0 connection.
   
   ![Save the token endpoint and authorization endpoint URLs](/assets/save-url.BkmumQyc.png)_Save the token endpoint and authorization endpoint URLs_
   

### Complete setup in Workato

Complete the following steps to configure your Workday connection in Workato using OAuth 2.0 authentication:

View OAuth 2.0 authentication steps

1. Enter a unique **Connection name** to identify your Workday account in Workato.
   
   ![Set up your connection](/assets/workday-rest-connection.IzDCKMEG.png)_Set up your connection_
   
2. Use the **Location** drop-down to select the project or folder to store this connection.
   
3. Use the **Connection type** drop-down menu to select **Cloud**.
   
4. Enter your REST API endpoint in the **REST API endpoint** field. You can find this endpoint in your API client details page in Workday. For example: `https://wd2-impl-services1.workday.com/xxx/api/v1/example`
   
5. Enter your authorization endpoint in the **Authorization endpoint** field. You can find this value in your Workday API client details. For example: `https://impl.workday.com/example/authorize`
   
6. Enter your token endpoint in the **Token endpoint** field. You can find this endpoint in your API client details page in Workday. For example: `https://wd2-impl-services1.workday.com/xxx/oauth2/example/token`
   
7. Enter your client ID in the **Client ID** field.
   
8. Enter your client secret in the **Client Secret** field.
   
9. Enter your refresh token in the **Refresh token** field.
   
   > **DON'T PROVIDE A REFRESH TOKEN FOR MCP SERVERS**
   > 
   > Don't provide a refresh token if you're connecting Workday to an MCP server.
   
10. Click **Connect**.
    

## How to use Workday End User MCP server tools

Refer to the following sections for detailed information on available tools:

### get\_my\_profile tool

The **get\_my\_profile** tool retrieves your worker profile information, including job title, manager, location, contact details, employment status, and hire date. Your LLM uses this tool to retrieve information about your employee profile.

**Try asking**:

- `What's my job title?`
- `Show me my employee profile.`
- `Who is my manager?`
- `What's my work location?`
- `When did I start working here?`

### get\_my\_manager tool

The **get\_my\_manager** tool retrieves your direct manager information. Your LLM uses this tool to retrieve your manager's information.

**Try asking**:

- `Who is my manager?`
- `Show me my direct manager's information.`
- `Who do I report to?`
- `Get my manager's contact details.`

### get\_my\_reporting\_chain tool

The **get\_my\_reporting\_chain** tool retrieves your upward reporting hierarchy. Your LLM uses this tool to retrieve your management hierarchy or to see who your manager reports to.

**Try asking**:

- `Show me my complete reporting chain.`
- `Who does my manager report to?`
- `What's my management hierarchy?`
- `Show me the chain of command up to the CEO.`

### list\_my\_direct\_reports tool

The **list\_my\_direct\_reports** tool retrieves your direct reports and their profile information. Your LLM uses this tool to see who reports to you or view your team.

**Try asking**:

- `Who are my direct reports?`
- `Show me my team.`
- `List everyone who reports to me.`
- `Get the profiles of my direct reports.`

### get\_my\_time\_off\_balances tool

The **get\_my\_time\_off\_balances** tool retrieves your time-off balances grouped by type. Your LLM uses this tool to check your PTO, vacation, or sick leave balances.

**Try asking**:

- `How much PTO do I have available?`
- `Show me my vacation balance.`
- `What's my sick leave balance?`
- `How many days off do I have remaining?`

### get\_direct\_report\_time\_off\_requests tool

The **get\_direct\_report\_time\_off\_requests** tool retrieves time-off requests for a direct report. Your LLM uses this tool to view PTO requests.

**Try asking**:

- `Show me time-off request history for Marco.`
- `List PTO requests pending approval for Sarah.`
- `List all the vacation requests from this year for Josh.`

### submit\_time\_off\_request tool

The **submit\_time\_off\_request** tool submits a new time-off request. Your LLM uses this tool to request time off.

**Try asking**:

- `Request 3 days of vacation for next week.`
- `Submit a PTO request for December 20-22.`
- `Request sick leave for tomorrow.`
- `I need to take vacation from March 1-5.`

### cancel\_time\_off\_request tool

The **cancel\_time\_off\_request** tool cancels a pending time-off request. Your LLM uses this tool to cancel a pending request.

**Try asking**:

- `Cancel my pending PTO request.`
- `Cancel my vacation request for next week.`
- `Remove my time-off request for March 1-5.`
- `I need to cancel my pending sick leave request.`

### get\_direct\_report\_time\_off\_balances tool

The **get\_direct\_report\_time\_off\_balances** tool retrieves the time-off balances for a direct report. Your LLM uses this tool view a direct report's vacation days, sick days, and leave balances.

**Try asking**:

- `Show me how many sick days Josh has available?`
- `How many vacation days does Sarah have?`
- `How many vacation days has Marco taken this year?`

### action\_time\_off\_request tool

The **action\_time\_off\_request** tool approves or rejects a time-off request for a direct report. Your LLM uses this tool to approve or reject a team member's request.

**Try asking**:

- `Approve Josh's vacation request.`
- `Reject the PTO request from Marco with a note about coverage.`
- `Approve the time-off request for March 1-5.`
- `I need to deny this sick leave request.`

### list\_time\_off\_types tool

The **list\_time\_off\_types** tool retrieves your available time-off types. Your LLM uses this tool when you need to know what types of time off are available.

**Try asking**:

- `What types of time off can I request?`
- `Show me all available PTO types.`
- `What are my time-off options?`
- `List the different types of leave I can take.`

### list\_my\_time\_off\_requests tool

The **list\_my\_time\_off\_requests** tools retrieves your PTO history or time-off request status. Your LLM uses this tool retrieve PTO balances and availability, and the status of submitted time-off requests.

**Try asking**:

- `How many vacation days have I taken this year?`
- `What's the status of time-off request submitted last week?`
- `What's my sick day balance?`
- `Do I have vacation days available?`

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

---

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

---
