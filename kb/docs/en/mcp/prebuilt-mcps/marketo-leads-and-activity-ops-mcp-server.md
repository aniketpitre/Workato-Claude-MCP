---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/marketo-leads-and-activity-ops-mcp-server.md
description: >-
  Use the Marketo Leads and Activity Ops MCP server to connect your LLM to
  Marketo with tools to retrieve, create, update leads, review activity history,
  and manage static list membership through natural language.
---

# Marketo Leads and Activity Ops MCP server

The Marketo Leads and Activity Ops MCP server enables LLMs to interact with Marketo lead data through natural conversation. It provides tools to retrieve, create, and update lead records, inspect activity history, and manage static list membership, supporting day-to-day operational workflows for Marketing Ops teams without requiring direct interaction with the Marketo interface.

## Uses

Use the Marketo Leads and Activity Ops MCP server to perform the following actions:

- Retrieve leads using filters such as email or Marketo ID
- Get specific lead details by Marketo ID
- Create new lead records with field values
- Update fields on existing lead records
- Review activity history for specific leads
- List and discover static lists with filters
- Get metadata for specific static lists
- Retrieve members of static lists
- View static lists associated with specific leads
- Add leads to static lists
- Remove leads from static lists

### Example prompts

Use the following example prompts to invoke Marketo Leads and Activity Ops MCP server tools:

- `Find the lead with email jade@example.com.`
- `Get details for lead ID 1207345.`
- `Create a new lead for Marco Reyes at techcorp.com.`
- `Update this lead's job title to VP of Marketing.`
- `Show me the activity history for this lead.`
- `List all static lists in the Q1 Campaign program.`
- `Get details about the Webinar Attendees list.`
- `Who are the members of the Enterprise Prospects list?`
- `What lists is this lead a member of?`
- `Add these leads to the Trade Show Contacts list.`
- `Remove this lead from the Nurture Campaign list.`

## Marketo Leads and Activity Ops MCP server tools

The Marketo Leads and Activity Ops MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_leads](#list-leads-tool) | Retrieves leads using explicit filters such as email or Marketo ID. |
| [get\_lead](#get-lead-tool) | Retrieves a Marketo lead by ID. |
| [create\_lead](#create-lead-tool) | Creates a new lead record with provided field values. |
| [update\_lead](#update-lead-tool) | Updates fields on an existing lead record. |
| [get\_lead\_activities](#get-lead-activities-tool) | Retrieves activity history for a lead you specify. |
| [list\_static\_lists](#list-static-lists-tool) | Retrieves static lists using supported filters. |
| [get\_static\_list](#get-static-list-tool) | Retrieves metadata for a static list you specify. |
| [get\_static\_list\_members](#get-static-list-members-tool) | Retrieves members of a static list you specify. |
| [get\_lead\_list\_memberships](#get-lead-list-memberships-tool) | Retrieves static lists associated with a specific lead. |
| [add\_leads\_to\_static\_list](#add-leads-to-static-list-tool) | Adds one or more leads to a static list. |
| [remove\_leads\_from\_static\_list](#remove-leads-from-static-list-tool) | Removes one or more leads from a static list. |

## Install the Marketo Leads and Activity Ops MCP server

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
    

## Marketo connection setup

View Marketo connection setup steps

The Marketo connector uses custom authentication.

> **CUSTOM SERVICE CLIENTS**
> 
> Marketo exposes REST endpoints to enable integration platforms like Workato to remotely access and execute core functionalities. We recommend you create a custom service client specifically for Workato to facilitate this integration.
> 
> Key benefits of using a custom service client include:
> 
> - **Isolated logging**: All operations are logged under a dedicated custom service client for integration and workflow processes. This approach enhances tracking and troubleshooting by isolating issues related to specific integration platforms.
> - **Customized permissions**: A custom service client allows for tailored permissions and security profiles, independent of individual employee user accounts.
> 
> Ensure that the custom service client is granted all necessary permissions to perform the required actions for your integration scenario. If a `403` error occurs during recipe execution, it indicates that the service client lacks the appropriate permissions for the action.

### Minimum scopes

View minimum scopes

You must select the following minimum role scopes when you create a new API role. Refer to [Create an API role](#create-an-api-role) for more information.

- `Read-Only Activity`
- `Read-Write Activity`
- `Read-Only Lead`
- `Read-Write Lead`
- `Read-Only Asset`
- `Read-Write Asset`

### Marketo setup for custom authentication

Complete the following steps to set up a custom authentication connection to Marketo in Workato:

- [Retrieve the REST API endpoint](#retrieve-rest-api-endpoint)
- [Create an API role](#create-an-api-role)
- [Create an API user](#create-an-api-user)
- [Create a custom service for Workato](#create-a-custom-service-for-workato)
- [Retrieve client credentials](#retrieve-client-credentials)

#### Retrieve the REST API endpoint

View retrieve the REST API endpoint steps

Complete the following steps to retrieve the REST API Endpoint in Marketo:

1. Sign in to your Marketo instance as a user with administrator privileges.
   
2. Go to **Admin > Web Services**.
   
3. In the **REST API** section, copy and save the **Endpoint** for use in Workato.
   

#### Create an API role

View create an API role steps

Complete the following steps to create an API role in Marketo:

1. Go to **Admin > Users & Roles** and select the **Roles** tab.
   
2. Click **New Role**.
   
3. Provide a name for your new role in the **Role Name** field. Optionally, add a description in the **Description** field.
   
4. Select the **Access API** checkbox in the **Permissions** field.
   
5. Click **Create** to create the API role.
   

#### Create an API user

View create an API user steps

Complete the following steps to create an API user in Marketo:

1. Go to **Admin > Users & Roles** and select the **Users** tab.
   
2. Click **Create API Only User**.
   
3. Fill out the **Email**, **First Name**, and **Last Name** fields.
   
4. Select the checkbox for the API role you created in the previous step from the **Roles** menu.
   
5. Click **CREATE API ONLY USER**.
   

#### Create a custom service

View create a custom service steps

Creating a custom service enables you to retrieve the client ID and client secret used to establish a connection in Workato. Refer to the [Marketo Engage Developer Documentation](https://developers.marketo.com/rest-api/custom-services/) for more information about custom services.

Complete the following steps to create a custom service in Marketo:

1. Go to **Admin > LaunchPoint**.
   
2. Click **New > New Service**.
   
3. Enter a descriptive **Display name** and select **Custom** from the **Service** drop-down menu.
   
4. Enter a description in the **Description** field.
   
5. Select the user you created in the previous step from the **API Only User** drop-down menu.
   
6. Click **Create**.
   

#### Retrieve client credentials

View retrieve client credentials steps

Complete the following steps to retrieve client credentials in Marketo:

1. Select **View details** for the new custom service you created in the previous step.
   
   ![View custom service](/assets/view-details-marketo.DY2NcPr5.png)_View custom service_
   
2. Copy and save the **Client Id** and **Client Secret** for use in Workato.
   

### Connect to Marketo with custom authentication

View connect to Marketo with custom authentication steps

Complete the following steps to connect to Marketo in Workato:

1. Select **Create > Connection** or press C twice.
   
2. Search for `Marketo` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Name your connection](/assets/marketo-connection.BpjczBep.png)_Name your connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the base URL of your Marketo instance in the **REST Endpoint** field. For example, if your REST endpoint is `https://123-ABC-456.mktorest.com/rest`, enter `123-ABC-456` in this field. Refer to [Retrieve the REST API endpoint](#retrieve-rest-api-endpoint) for more information.
   
6. Enter the **Client Id** from Marketo in the **Custom Service client ID** field. Refer to [Retrieve client credentials](#retrieve-client-credentials) for more information.
   
7. Enter the **Client Secret** from Marketo in the **Custom Service client secret** field. Refer to [Retrieve client credentials](#retrieve-client-credentials) for more information.
   
8. Click **Connect**.
   

### Project property configuration

The Marketo Leads and Activity Ops MCP server supports the following project-level properties to control behavior and defaults:

| Project-level property | Description |
| --- | --- |
| `default_activity_time_window` | Defines the default time range applied when **get\_lead\_activities** is invoked without a **time\_window** parameter. This ensures bounded and predictable activity retrieval. |
| `default_activity_type_ids` | Defines the set of activity type IDs used when **get\_lead\_activities** is invoked without an **activity\_type\_ids** parameter. Defaults to a standard engagement activity set, including: `1 — Visit Webpage`, `2 — Fill Out Form`, `6 — Send Email`, `7 — Email Delivered`, `8 — Email Bounced`, `9 — Unsubscribe Email`, `10 — Open Email`, `11 — Click Email`, and `27 — Email Bounced Soft`. |
| `max_records` | Defines the maximum number of records returned in a single response for collection-returning tools, such as **list\_leads**, **get\_lead\_activities**, **get\_static\_list\_members**, and **get\_lead\_list\_memberships**. This quota applies per response page, not the total retrievable dataset. |
| `max_batch_size` | Defines the maximum number of lead IDs allowed in batch operations. Applies to **add\_leads\_to\_static\_list** and **remove\_leads\_from\_static\_list**. This value can't exceed the Marketo API limit of `300`. |

View project-level property configuration steps

Complete the following steps to configure your project-level properties:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Click the **Settings** tab.
   
   ![Click the Settings tab](/assets/project-settings.99X6TiYd.png)_Click the **Settings** tab._
   
4. Select **Project properties**.
   
5. Go to the project property you plan to update and click the **Edit** (pencil) icon.
   
   ![Click the Edit (pencil) icon](/assets/zendesk-knowledge-base-project-property.DGAT1hbT.png)_Click the **Edit** (pencil) icon._
   
6. Go to the **Value** field and make your changes. For example, set `max_batch_size` to `250` or `max_records` to `25`.
   

## How to use Marketo Leads and Activity Ops MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_leads tool

The **list\_leads** tool retrieves leads using explicit filters, such as email or Marketo ID. Your LLM uses this tool to find or look up a lead using email or Marketo ID.

**Try asking**:

- `Find the lead with email jade@example.com.`
- `Look up leads with Marketo IDs 12345 and 67890.`
- `Search for the lead with email marco@acme.com.`
- `Get leads matching these email addresses.`

### get\_lead tool

The **get\_lead** tool retrieves a Marketo lead by ID. Your LLM uses this tool when a lead has been uniquely identified by Marketo ID.

**Try asking**:

- `Get details for lead ID 1207345.`
- `Show me the complete information for Marketo lead 67890.`
- `Retrieve lead 54321 from Marketo.`
- `What are the details for this lead ID?`

### create\_lead tool

The **create\_lead** tool creates a new lead record with provided field values. Your LLM uses this tool when you explicitly ask to create a new lead.

**Try asking**:

- `Create a new lead for Marco Reyes at acme.com.`
- `Add Jade Anderson as a lead with email jade@acme.com.`
- `Create a lead record for Alex Chen, VP of Sales.`
- `Add a new Marketo lead for this contact.`

### update\_lead tool

The **update\_lead** tool updates fields on an existing lead record. Your LLM uses this tool to modify an existing lead after ensuring the lead is uniquely identified.

**Try asking**:

- `Update this lead's job title to VP of Marketing.`
- `Change the company name for lead 1207345 to Acme Inc.`
- `Update Mei's phone number to 555-0123.`
- `Modify this lead's status to Qualified.`

### get\_lead\_activities tool

The **get\_lead\_activities** tool retrieves activity history for a lead you specify. Your LLM uses this tool to view a lead's activity or engagement.

**Try asking**:

- `Show me the activity history for this lead.`
- `What engagement activities has lead 1207345 had?`
- `Get the activity log for Jade Anderson.`
- `Review this lead's interaction history.`

### list\_static\_lists tool

The **list\_static\_lists** tool retrieves static lists using supported filters. Your LLM uses this tool to discover or browse static lists, using the exact list name when provided or program name when you request lists belonging to a specific program.

**Try asking**:

- `List all static lists in the Q1 Campaign program.`
- `Show me static lists named 'Webinar Attendees'.`
- `What static lists exist in Marketo?`
- `Find lists in the Product Launch program.`

### get\_static\_list tool

The **get\_static\_list** tool retrieves metadata for a static list you specify. Your LLM uses this tool to get details about a specific list.

**Try asking**:

- `Get details about the Webinar Attendees list.`
- `Show me metadata for list ID 456.`
- `What are the details of the Enterprise Prospects list?`
- `Get information about this static list.`

### get\_static\_list\_members tool

The **get\_static\_list\_members** tool retrieves members of a static list you specify with pagination support for large lists. Your LLM uses this tool to view the members of a list.

**Try asking**:

- `Who are the members of the Enterprise Prospects list?`
- `Show me all leads in the Webinar Attendees list.`
- `List members of the Trade Show Contacts list.`
- `Get the leads in list ID 789.`

### get\_lead\_list\_memberships tool

The **get\_lead\_list\_memberships** tool retrieves static lists associated with a lead you specify. Your LLM uses this tool to view which lists a lead belongs to.

**Try asking**:

- `What lists is this lead a member of?`
- `Show me all static lists containing lead 12345.`
- `Which lists include Jade Anderson?`
- `What static lists is Marco in?`

### add\_leads\_to\_static\_list tool

The **add\_leads\_to\_static\_list** tool adds one or more leads to a static list. Your LLM uses this tool to add leads to a list, first resolving lead identities using `list_leads` or `get_lead`.

**Try asking**:

- `Add these leads to the Trade Show Contacts list.`
- `Put lead 12345 in the Enterprise Prospects list.`
- `Add Jade and Marco to the Webinar Attendees list.`
- `Include this lead in the Nurture Campaign list.`

### remove\_leads\_from\_static\_list tool

The **remove\_leads\_from\_static\_list** tool removes one or more leads from a static list. Your LLM uses this tool to remove leads from a list.

**Try asking**:

- `Remove this lead from the Nurture Campaign list.`
- `Take lead 12345 out of the Enterprise Prospects list.`
- `Remove Jade from the Webinar Attendees list.`
- `Remove these leads from the Trade Show Contacts list.`

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
