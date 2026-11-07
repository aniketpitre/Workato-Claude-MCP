---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/insightly-sales-contacts-mcp-server.md
description: >-
  Use the Insightly Sales & Contacts MCP server to connect your LLM to Insightly
  with tools to find, create, and update contacts, organizations, leads, and
  opportunities.
---

# Insightly Sales & Contacts MCP server

The Insightly Sales & Contacts MCP server enables LLMs to interact with Insightly for sales-cycle record management through natural conversation. It provides tools to find and update contacts and organizations, capture and progress unqualified leads, convert qualified leads into contacts, and manage opportunities in the deal pipeline, without requiring direct interaction with the Insightly interface.

## Uses

Use the Insightly Sales & Contacts MCP server to perform the following actions:

- List contacts and organizations by name or owner
- Retrieve a specific contact or opportunity
- Log new, unqualified leads and update their details as qualification progresses
- Convert a qualified lead into a contact, and optionally an organization and opportunity
- Register an already-qualified contact without going through lead qualification
- Search, review, and open sales opportunities in the deal pipeline
- Progress an existing opportunity's stage, amount, state, or owner
- Update any field on an existing contact record

### Example prompts

Use the following example prompts to invoke Insightly Sales & Contacts MCP server tools:

- `Find the contact for Amal Hassan at Acme Corp.`
- `Log Dana Ortiz from the conference as a new lead.`
- `Update the title on this lead to VP of Operations.`
- `Convert this lead into a contact and opportunity.`
- `Qualify this lead but don't open a deal yet.`
- `Add Cruz Nguyen as a contact, they're a referral.`
- `What deals do I have open?`
- `Show me Acme Corp opportunities in Negotiation.`
- `Open a $50,000 Acme Corp renewal closing September 30.`
- `Mark the Acme Corp deal as Won.`

## Insightly Sales & Contacts MCP server tools

The Insightly Sales & Contacts MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_contacts](#search-contacts-tool) | Lists contacts by name or owner. |
| [get\_contact](#get-contact-tool) | Retrieves a contact by ID. |
| [create\_contact](#create-contact-tool) | Adds a known or qualified contact. |
| [update\_contact](#update-contact-tool) | Updates fields on an existing contact. |
| [search\_organizations](#search-organizations-tool) | Lists organizations by name or owner. |
| [create\_organization](#create-organization-tool) | Adds a new organization record. |
| [search\_leads](#search-leads-tool) | Lists leads by name, email, organization name, or owner. |
| [create\_lead](#create-lead-tool) | Logs a new, unqualified lead. |
| [update\_lead](#update-lead-tool) | Updates fields on an existing lead, including its qualification status. |
| [convert\_lead](#convert-lead-tool) | Converts a qualified lead into a contact, and optionally an organization and opportunity. |
| [search\_opportunities](#search-opportunities-tool) | Lists opportunities by name, owner, state, or stage. |
| [get\_opportunity](#get-opportunity-tool) | Retrieves an opportunity by ID. |
| [create\_opportunity](#create-opportunity-tool) | Opens a new sales opportunity outside of lead conversion. |
| [update\_opportunity](#update-opportunity-tool) | Updates fields on an existing opportunity, including stage, amount, and state. |

## Install the Insightly Sales & Contacts MCP server

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
    

## Insightly Sales & Contacts connection setup

View Insightly Sales & Contacts connection setup steps

The Insightly connector uses API key authentication.

### API version

The Insightly connector uses the [Insightly API v2.1](https://api.insight.ly/v2.1/Help).

### Insightly setup for API key authentication

Refer to the Insightly [API Key and URL](https://support.insight.ly/en-US/Knowledge/article/2775#API%20Key%20and%20URL) guide to create an API key.

### Connect to Insightly on Workato

View connect to Insightly with an API key steps

Complete the following steps to set up an API key connection to Insightly in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Insightly` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your API key in the **API Key** field.
   
6. Click **Connect**.
   

### Project property configuration

The Insightly Sales & Contacts MCP server supports the following project-level properties to control behavior and defaults:

| Project-level property | Description |
| --- | --- |
| search\_results\_default | Enter the maximum number of results to return from **search\_contacts**, **search\_organizations**, **search\_leads**, and **search\_opportunities** when a user doesn't specify a limit in their request. Defaults to `25`. |
| search\_results\_max | Enter the maximum number of results to return from **search\_contacts**, **search\_organizations**, **search\_leads**, and **search\_opportunities**, regardless of whether a user specifies a limit. Defaults to `100`. |

View project-level property configuration steps

Complete the following steps to configure your project-level properties:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Click the **Settings** tab.
   
   ![Click the Settings tab](/assets/project-settings.99X6TiYd.png)_Click the **Settings** tab._
   
4. Select **Project properties**.
   
5. Go to the project property you plan to update and click the **Edit** (pencil) icon.
   
6. Go to the **Value** field and make your changes. For example, set `search_results_max` to `50`.
   

## How to use Insightly Sales & Contacts MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_contacts tool

The **search\_contacts** tool lists contacts by name or owner. Your LLM uses this tool to find a contact's ID.

**Try asking**:

- `Find the contact for Amal Hassan.`
- `List contacts owned by Cruz Nguyen.`
- `Find the contact named Dana Ortiz.`
- `Show me the next page of contacts owned by Dana Ortiz.`

### get\_contact tool

The **get\_contact** tool retrieves a contact by ID. Your LLM uses this tool to review a contact's email, phone, linked organization, or opportunity IDs.

**Try asking**:

- `Show me the full details for this contact.`
- `What organization is this contact linked to?`
- `Pull up Amal Hassan's contact record.`
- `What opportunities are linked to this contact?`

### create\_contact tool

The **create\_contact** tool adds a known or qualified contact. Your LLM uses this tool to register a referral or an already-qualified prospect without going through lead qualification.

**Try asking**:

- `Add Cruz Nguyen as a contact, they're a referral.`
- `Create a contact for Dana Ortiz at Acme Corp.`
- `Register this person as a contact, no lead needed.`
- `Add a new contact and link them to Acme Corp.`

### update\_contact tool

The **update\_contact** tool updates fields on an existing contact. Your LLM uses this tool to change any field on a contact, such as a phone number, email address, or job title.

**Try asking**:

- `Update the phone number on this contact.`
- `Change this contact's email address.`
- `Update Amal Hassan's title to VP of Sales.`
- `Correct the spelling of this contact's name.`

### search\_organizations tool

The **search\_organizations** tool lists organizations by name or owner. Your LLM uses this tool to find a specific organization, for example, to check whether a company already exists before creating a new record.

**Try asking**:

- `Find the organization record for Acme Corp.`
- `List organizations owned by Cruz Nguyen.`
- `Confirm whether Acme Corp already exists as an organization.`
- `Show me the next page of organizations.`

### create\_organization tool

The **create\_organization** tool adds a new organization record. Your LLM uses this tool to create a company record when one doesn't already exist for a new contact or opportunity.

**Try asking**:

- `Add Acme Corp as a new organization.`
- `Create a company record for this contact.`
- `Add a new organization owned by Dana Ortiz.`
- `Create an organization record before I link this deal.`

### search\_leads tool

The **search\_leads** tool lists leads by name, email, organization name, or owner. Your LLM uses this tool to find a lead's ID.

**Try asking**:

- `Find the lead for Amal Hassan.`
- `Show me leads at Acme Corp.`
- `Find the lead with the email dana@example.com.`
- `Search for leads owned by Cruz Nguyen.`

### create\_lead tool

The **create\_lead** tool logs a new, unqualified lead. Your LLM uses this tool to capture a prospect from an event, inbound inquiry, or referral before there's enough information to qualify the lead.

**Try asking**:

- `Log Dana Ortiz from the conference as a new lead.`
- `Add a new lead for Acme Corp, owned by Cruz Nguyen.`
- `Create a lead with just a last name and owner.`
- `Log this inbound inquiry as an unqualified lead.`

### update\_lead tool

The **update\_lead** tool updates fields on an existing lead. Your LLM uses this tool to correct a lead's details or move it through qualification statuses.

**Try asking**:

- `Update the title on this lead to VP of Operations.`
- `Move this lead's status to Qualified.`
- `Correct the phone number on this lead.`
- `Update this lead's organization name.`

### convert\_lead tool

The **convert\_lead** tool converts a qualified lead into a contact, and optionally an organization and opportunity. Your LLM uses this tool when a lead is confirmed ready to move into an active sales process.

**Try asking**:

- `Convert this lead into a contact and opportunity.`
- `Qualify this lead but don't open a deal yet.`
- `Convert this lead and link it to the existing Acme Corp organization.`
- `Move Amal Hassan's lead into an active deal.`

### search\_opportunities tool

The **search\_opportunities** tool lists opportunities by name, owner, state, or stage. Your LLM uses this tool to review open deals, deals in a specific stage, or deals owned by a specific rep.

**Try asking**:

- `What deals do I have open?`
- `Show me Acme Corp opportunities in Negotiation.`
- `List opportunities owned by Cruz Nguyen.`
- `Find the opportunity named Acme Corp Renewal.`

### get\_opportunity tool

The **get\_opportunity** tool retrieves an opportunity by ID. Your LLM uses this tool to review a deal's amount, stage, and linked contact or organization.

**Try asking**:

- `Show me the full details on this opportunity.`
- `What's the current stage on the Acme Corp deal?`
- `Who is this opportunity linked to?`
- `Pull up the details for this deal.`

### create\_opportunity tool

The **create\_opportunity** tool opens a new sales opportunity outside of lead conversion. Your LLM uses this tool to open a deal directly, without going through lead qualification first.

**Try asking**:

- `Open a $50,000 Acme Corp renewal closing September 30.`
- `Create a new opportunity for this contact.`
- `Open a deal in the Negotiation stage.`
- `Add a new opportunity owned by Cruz Nguyen.`

### update\_opportunity tool

The **update\_opportunity** tool updates fields on an existing opportunity, including stage, amount, and state. Your LLM uses this tool to progress a deal through its pipeline or reassign its owner.

**Try asking**:

- `Move this deal to Negotiation stage.`
- `Mark the Acme Corp deal as Won.`
- `Update the amount on this opportunity to $75,000.`
- `Reassign this opportunity to Cruz Nguyen.`

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
