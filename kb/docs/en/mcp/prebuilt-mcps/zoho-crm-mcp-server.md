---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/zoho-crm-mcp-server.md'
description: >-
  Use the Zoho CRM MCP server to connect your LLM to Zoho CRM with tools to
  find, create, update, and delete leads, accounts, contacts, and deals.
---

# Zoho CRM MCP server

The Zoho CRM MCP server lets LLMs work with Zoho CRM for core CRM record management through natural conversation. It provides tools to search, retrieve, create, update, and delete leads, accounts, contacts, and deals, convert qualified leads, look up related records, and check a module's field metadata, without requiring direct interaction with the Zoho CRM interface.

## Uses

Use the Zoho CRM MCP server to perform the following actions:

- Search leads, accounts, contacts, and deals
- Retrieve a specific record
- Create new leads, accounts, contacts, and deals
- Update a record's fields
- Apply a field change to a batch of records
- Upsert a record from an external source
- Delete a record that's no longer needed
- Convert a qualified lead into an account, contact, and optionally a deal
- List records related to a parent record through a named related list
- Search vendor and campaign records
- Look up a module's field names, required fields, and picklist values before writing a record

### Example prompts

Use the following example prompts to invoke Zoho CRM MCP server tools:

- `Find the deal for Acme Corp that's closing this month.`
- `Create a new lead for Kiran Patel at Acme Corp.`
- `Update the stage on this deal to Negotiation.`
- `Move every deal in the Qualification stage to Needs Analysis.`
- `Sync this contact from our database into Zoho, and update it if it already exists.`
- `What contacts are linked to this account?`
- `Delete this duplicate lead.`
- `Convert this lead into an account, contact, and deal.`
- `What fields are required to create a new deal?`
- `Search for vendors matching "Acme".`

## Zoho CRM MCP server tools

The Zoho CRM MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_records](#search-records-tool) | Searches leads, accounts, contacts, or deals by field value, email address, phone number, or keyword. |
| [get\_record](#get-record-tool) | Retrieves a single lead, account, contact, or deal. |
| [create\_lead](#create-lead-tool) | Creates a new lead. |
| [create\_account](#create-account-tool) | Creates a new account. |
| [create\_contact](#create-contact-tool) | Creates a new contact. |
| [create\_deal](#create-deal-tool) | Creates a new deal. |
| [update\_record](#update-record-tool) | Updates fields on an existing lead, account, contact, or deal. |
| [bulk\_update\_records\_by\_id](#bulk-update-records-by-id-tool) | Applies the same field change to up to 100 records. |
| [upsert\_record](#upsert-record-tool) | Creates or updates a record. |
| [delete\_record](#delete-record-tool) | Deletes a lead, account, contact, or deal. |
| [list\_related\_records](#list-related-records-tool) | Lists records linked to a parent record through a named related list. |
| [search\_vendor](#search-vendor-tool) | Searches vendor records. |
| [search\_campaigns](#search-campaigns-tool) | Searches campaign records. |
| [convert\_lead](#convert-lead-tool) | Converts a lead into an account, contact, and optionally a deal. |
| [get\_module\_fields](#get-module-fields-tool) | Returns a module's field API names, required and read-only flags, and picklist values. |

## Install the Zoho CRM MCP server

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
    

## Zoho CRM connection setup

View Zoho CRM connection setup steps

The Zoho CRM connector uses OAuth 2.0 authentication.

### API version

The Zoho CRM connector uses the following Zoho CRM API versions:

- [V2](https://www.zoho.com/crm/developer/docs/api/v2/)
- [V5](https://www.zoho.com/crm/developer/docs/api/v5/)
- [V7](https://www.zoho.com/crm/developer/docs/api/v7/)

### How to connect to Zoho CRM

Complete the following steps to establish a Zoho CRM connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Zoho CRM` on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Zoho CRM](/assets/connect.Ci6gBkOa.png)_Connect to Zoho CRM_
   
4. Use the **Location** drop-down menu to select the project or folder to store your connection.
   
5. Use the **Account timezone** drop-down menu to select your account timezone as specified in Zoho CRM.
   
6. Use the **Data center** drop-down menu to select your data center. You can find your data center at the end of your Zoho URL.
   
7. Expand the **Advanced settings** section to configure **Scopes** for your connection.
   
   The following scopes are requested by default:
   
   - `ZohoCRM.modules.contacts.READ`
   - `ZohoCRM.settings.modules.READ`
   
   Defaults to `ZohoCRM.modules.all`, `ZohoCRM.settings.all` if left blank.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
9. Click **Connect**.
   

### Zoho CRM role requirements

Each tool's availability depends on the permissions granted to the connected account. A request made without the required permission returns a permission-denied outcome rather than a partial result. Refer to [Manage Users, Roles, and Permissions](https://help.zoho.com/portal/en/kb/crm/users-and-control/data-security-types/articles/get-started-manage-users) for the complete list of role capabilities.

## How to use Zoho CRM MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_records tool

The **search\_records** tool searches leads, accounts, contacts, or deals by a field value, email address, phone number, or keyword. Your LLM uses this tool to find records before reading or writing them. A field search can match a field's exact value, or match if any word within it begins with the given text. Field search doesn't support broader partial-word matching.

**Try asking**:

- `Find leads from the West region.`
- `Show me deals over $50,000 closing this month.`
- `Find the contact with email ariel@example.com.`
- `Search accounts for the keyword "Acme".`

### get\_record tool

The **get\_record** tool retrieves a single lead, account, contact, or deal by its ID. Your LLM uses this tool to read a record's full details before acting on it.

**Try asking**:

- `Show me the full details for this deal.`
- `What are the current fields on this contact?`
- `Get the details for this account.`

### create\_lead tool

The **create\_lead** tool creates a new lead. Your LLM uses this tool when you ask to add a new lead.

**Try asking**:

- `Create a new lead for Kiran Patel at Acme Corp.`
- `Add a lead for the contact I just described.`
- `Log a new lead from this morning's call.`

### create\_account tool

The **create\_account** tool creates a new account. Your LLM uses this tool when you ask to add a new account.

**Try asking**:

- `Create a new account for Acme Corp.`
- `Add an account record for this organization.`
- `Log Acme Corp as a new account.`

### create\_contact tool

The **create\_contact** tool creates a new contact. Your LLM uses this tool when you ask to add a new contact.

**Try asking**:

- `Create a new contact for Jade Chen at Acme Corp.`
- `Add a contact for the person I just spoke with.`
- `Log Dana Smith as a new contact under this account.`

### create\_deal tool

The **create\_deal** tool creates a new deal. Your LLM uses this tool when you ask to add a new deal.

**Try asking**:

- `Create a new deal for the Acme Corp renewal.`
- `Add a deal closing at the end of the quarter.`
- `Log a new deal for this account.`

### update\_record tool

The **update\_record** tool updates fields you specify on an existing lead, account, contact, or deal. It shows a preview for your approval before it applies the change. Your LLM uses this tool when you ask to change a field on a record whose ID is already known.

**Try asking**:

- `Update the stage on this deal to Negotiation.`
- `Change the phone number on this contact.`
- `Correct the company name on this lead.`
- `Show me what this change will look like before you apply it.`

### bulk\_update\_records\_by\_id tool

The **bulk\_update\_records\_by\_id** tool applies the same field change to up to 100 records. It shows the record count and a preview for your approval before it applies the change. Your LLM uses this tool when you ask to apply the same update to multiple already identified records, typically from a prior search.

**Try asking**:

- `Move every deal in the Qualification stage to Needs Analysis.`
- `Update the owner on these 20 leads.`
- `Change the region on all of these accounts.`

### upsert\_record tool

The **upsert\_record** tool creates a record, or updates it if the Zoho duplicate-check finds an existing match. It shows a preview for your approval before it applies the change. Your LLM uses this tool when a record needs to exist with certain values regardless of whether it already exists in Zoho, such as when syncing from an external system.

**Try asking**:

- `Sync this contact from our database into Zoho, and update it if it already exists.`
- `Make sure this account exists in Zoho with these details.`
- `Upsert this deal from our external system.`

### delete\_record tool

The **delete\_record** tool deletes a lead, account, contact, or deal. It shows a preview for your approval before it removes the record. The delete is permanent. An account delete also removes its linked contacts and deals in Zoho. Your LLM uses this tool when you ask to delete a record.

**Try asking**:

- `Delete this duplicate lead.`
- `Remove this test deal.`
- `Delete this account. I created it by mistake.`

### list\_related\_records tool

The **list\_related\_records** tool lists records linked to a parent record through one named related list, such as the contacts under an account or the notes on a deal, optionally narrowed to specific fields. Your LLM uses this tool when you ask what's linked to a record.

**Try asking**:

- `What contacts are linked to this account?`
- `Show me the notes on this deal.`
- `List everything related to this lead.`
- `Just show me the names of the contacts linked to this account.`

### search\_vendor tool

The **search\_vendor** tool searches vendor records by specific field values. Your LLM only uses this tool to find vendor records. It can't create, update, or delete them.

**Try asking**:

- `Search for vendors matching "Acme".`
- `Find the vendor record for this supplier.`

### search\_campaigns tool

The **search\_campaigns** tool searches campaign records by specific field values. Your LLM only uses this tool to find campaign records. It can't create, update, delete, or manage membership for them.

**Try asking**:

- `Find campaigns running this quarter.`
- `Search for the campaign named "Fall Promo".`

### convert\_lead tool

The **convert\_lead** tool converts a lead into an account, contact, and optionally a deal. It shows a preview for your approval before it completes the conversion. Your LLM uses this tool when you ask to convert a specific lead whose record ID is already known. Conversion can't be undone through this tool, and it reports an already-converted lead as not found rather than already converted.

**Try asking**:

- `Convert this lead into an account, contact, and deal.`
- `Qualify this lead, but don't create a deal yet.`
- `Promote this lead now that it's qualified.`

### get\_module\_fields tool

The **get\_module\_fields** tool returns a module's field API names, required and read-only flags, and picklist values. Your LLM uses this tool to inspect field metadata before a write or search. Write operations don't validate values against picklist options, so Zoho saves values outside those options exactly as provided.

**Try asking**:

- `What fields are required to create a new deal?`
- `What are the valid values for the lead status field?`
- `Which fields on a contact are read-only?`

## Zoho CRM MCP apps

The Zoho CRM MCP server includes five [MCP apps](/en/mcp/mcp-apps) that preview changes for your approval: **Record Preview Update**, **Record Preview Upsert**, **Record Preview Delete**, **Bulk Update**, and **Convert Lead**. **Convert Lead** prompts you to fill fields it couldn't populate from the lead. You can't commit changes until all required fields are filled.

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
