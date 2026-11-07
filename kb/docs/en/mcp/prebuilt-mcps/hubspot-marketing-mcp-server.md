---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/hubspot-marketing-mcp-server.md'
description: >-
  Use the HubSpot Marketing MCP server to connect your LLM to HubSpot with tools
  to create and organize marketing emails, forms, campaigns, contact lists, and
  events.
---

# HubSpot Marketing MCP server

The HubSpot Marketing MCP server enables LLMs to interact with HubSpot for marketing asset and audience management through natural conversation. It provides tools to create, clone, read, and update marketing emails and forms, organize campaigns and their assets, curate contact lists, and manage marketing events and attendance without requiring direct interaction with the HubSpot interface.

## Uses

Use the HubSpot Marketing MCP server to perform the following actions:

- Draft new marketing emails or clone existing emails into variants
- Create and maintain lead-capture forms
- Create marketing campaigns and organize which emails, forms, and events belong to them
- Build, search, and modify contact lists
- Create marketing events and register attendees
- Track attendance state for marketing events
- Retrieve marketing emails, forms, campaigns, and events

### Example prompts

Use the following example prompts to invoke HubSpot Marketing MCP server tools:

- `Clone last month's newsletter and rename it.`
- `Create a new lead-capture form for the landing page.`
- `Create a campaign for our Q3 product launch.`
- `Add these contacts to the VIP list.`
- `Find the list of contacts for our webinar send.`
- `Register Kiran Patel for the product demo webinar.`
- `What assets are attached to the Q3 campaign?`
- `Show me the recent marketing emails.`
- `Mark this attendee as having attended the webinar.`
- `Create a new dynamic list of contacts in the trial lifecycle stage.`

## HubSpot Marketing MCP server tools

The HubSpot Marketing MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [create\_marketing\_email](#create-marketing-email-tool) | Creates a new marketing email asset as a draft. |
| [clone\_marketing\_email](#clone-marketing-email-tool) | Clones an existing marketing email into a new named copy. |
| [update\_marketing\_email](#update-marketing-email-tool) | Updates editable fields on an existing marketing email. |
| [get\_marketing\_email](#get-marketing-email-tool) | Lists marketing emails, or retrieves a specific marketing email by ID. |
| [create\_form](#create-form-tool) | Creates a new marketing lead-capture form. |
| [update\_form](#update-form-tool) | Updates fields, name, or settings of an existing form. |
| [get\_form](#get-form-tool) | Lists forms, or retrieves a specific form by ID. |
| [create\_campaign](#create-campaign-tool) | Creates a new marketing campaign. |
| [get\_campaign](#get-campaign-tool) | Lists campaigns, or retrieves a specific campaign by GUID. |
| [manage\_campaign\_assets](#manage-campaign-assets-tool) | Associates, removes, or lists assets belonging to a campaign. |
| [create\_list](#create-list-tool) | Creates a new marketing contact list. |
| [search\_lists](#search-lists-tool) | Searches contact lists by name and processing type, or retrieves a specific list by ID. |
| [manage\_list\_members](#manage-list-members-tool) | Adds or removes contacts on a static list. |
| [create\_marketing\_event](#create-marketing-event-tool) | Creates, retrieves, or lists external marketing events. |
| [record\_event\_attendance](#record-event-attendance-tool) | Sets a subscriber's attendance state for a marketing event. |

## Install the HubSpot Marketing MCP server

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
    

## HubSpot Marketing connection setup

View HubSpot Marketing connection setup steps

### API version

The HubSpot connector uses the [HubSpot REST API v3](https://developers.hubspot.com/docs/api/overview).

### How to connect to HubSpot on Workato

Complete the following steps to authenticate with HubSpot using OAuth 2.0:

1. Click **Create > Connection** or press C twice.
   
2. Search for `HubSpot` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project or folder to store your connection.
   
5. Optional. Go to the **Advanced settings** section and select the scopes to provide to Workato. The connector requests the minimum set of scopes for its recipe triggers and actions by default. Refer to the complete list of [available scopes](/en/connectors/hubspot/scopes#full-list-scopes) for more information.
   
6. Optional. Use the **Custom OAuth profile** drop-down menu to select a [custom OAuth profile](/en/custom-oauth-profiles) for your connection.
   
7. Click **Connect**.
   
8. Select the HubSpot account where you plan to authorize Workato and click **Choose Account**.
   
   ![Choose account](/assets/select-account.BvvC0buZ.png)_Select an account_
   

### HubSpot role requirements

Each tool's availability depends on the scopes granted to the connected account and the HubSpot Marketing Hub tier to which the account belongs. Forms, contact lists, and marketing events are available on the Free tier, while marketing emails and campaigns require Marketing Hub Professional or above. HubSpot doesn't support per-user authentication for this connector, so every tool runs under a single connected account. A request made without the required scope or tier returns a permission-denied outcome rather than a partial result. Refer to the HubSpot [Scopes](https://developers.hubspot.com/docs/api/scopes) documentation for the complete list of scope requirements.

## How to use HubSpot Marketing MCP server tools

Refer to the following sections for detailed information on available tools:

### create\_marketing\_email tool

The **create\_marketing\_email** tool creates a new marketing email asset as a draft. Your LLM uses this tool to start a new email for an upcoming send, leaving it as a draft for you to finish and send in HubSpot.

**Try asking**:

- `Create a new marketing email for our fall product launch.`
- `Draft an email announcing the webinar.`
- `Start a new marketing email named "October Newsletter."`
- `Create a marketing email with the subject "You're invited."`

### clone\_marketing\_email tool

The **clone\_marketing\_email** tool clones an existing marketing email into a new named copy. Your LLM uses this tool to build a variant of an email without recreating the content from scratch.

**Try asking**:

- `Clone last month's newsletter and rename it.`
- `Make a copy of this email for our EMEA audience.`
- `Duplicate the welcome email as a Spanish version.`
- `Clone this email and call it "October Newsletter - Variant B."`

### update\_marketing\_email tool

The **update\_marketing\_email** tool updates editable fields on an existing marketing email. Your LLM uses this tool to change a draft email's name, subject, or type.

**Try asking**:

- `Change the subject line on this draft email.`
- `Rename this marketing email to "November Newsletter."`
- `Update this email's type to automated.`
- `Fix the subject on the webinar invite email.`

### get\_marketing\_email tool

The **get\_marketing\_email** tool lists marketing emails, or retrieves a specific email by ID. Your LLM uses this tool to inspect a specific email or browse recent emails for discovery.

**Try asking**:

- `Show me the recent marketing emails.`
- `Find the draft email named "October Newsletter."`
- `What's the subject line on this email?`
- `List all draft emails I haven't sent yet.`

### create\_form tool

The **create\_form** tool creates a new marketing lead-capture form. Your LLM uses this tool to build a form for a landing page or campaign from the fields and configuration you describe.

**Try asking**:

- `Create a lead-capture form for the landing page.`
- `Build a form with fields for name, email, and company.`
- `Make a new form for our webinar signup.`
- `Create a contact form with reCAPTCHA enabled.`

### update\_form tool

The **update\_form** tool updates fields, name, or settings of an existing form. Your LLM uses this tool to add a field, rename a form, or change the configuration.

**Try asking**:

- `Add a phone number field to this form.`
- `Rename this form to "Webinar Signup - Q3."`
- `Change the submit button text on this form.`
- `Update the thank-you message on this form.`

### get\_form tool

The **get\_form** tool lists forms, or retrieves a specific form by ID. Your LLM uses this tool to inspect a form's fields or browse forms for discovery.

**Try asking**:

- `Show me the fields on this form.`
- `Find the form for the landing page.`
- `List the forms I've created this quarter.`
- `What forms do we have set up?`

### create\_campaign tool

The **create\_campaign** tool creates a new marketing campaign. You can specify a name, start and end dates, a currency, notes, and a UTM value. Your LLM uses this tool to start a campaign with the attributes you provide.

**Try asking**:

- `Create a campaign for our Q3 product launch.`
- `Start a new campaign named "Fall Webinar Series," running from October 1 to October 31.`
- `Create a campaign with the UTM value "fall-webinar-series."`
- `Add a note to this campaign about the target audience.`

### get\_campaign tool

The **get\_campaign** tool lists campaigns, or retrieves a specific campaign by GUID. Your LLM uses this tool to find a campaign's GUID or browse existing campaigns.

**Try asking**:

- `Find the campaign named "Fall Webinar Series."`
- `Show me our active campaigns.`
- `What's the GUID for the Q3 product launch campaign?`
- `List the campaigns created this year.`

### manage\_campaign\_assets tool

The **manage\_campaign\_assets** tool associates, removes, or lists assets belonging to a campaign. Your LLM uses this tool to attach an email, form, or event to a campaign, remove an attached asset, or see what's currently attached.

**Try asking**:

- `Attach this email to the Q3 product launch campaign.`
- `What assets are on the Fall Webinar Series campaign?`
- `Remove this form from the campaign.`
- `Add the webinar event to this campaign.`

### create\_list tool

The **create\_list** tool creates a new marketing contact list. Your LLM uses this tool to build a static or dynamic contact list to use as an audience for a campaign.

**Try asking**:

- `Create a static list called "VIP Customers."`
- `Make a dynamic list of contacts in the trial lifecycle stage.`
- `Create a new list for our webinar attendees.`
- `Build a snapshot list of this quarter's leads.`

### search\_lists tool

The **search\_lists** tool searches contact lists by name and processing type, or retrieves a specific list by ID. Your LLM uses this tool to locate a list before curating its membership.

**Try asking**:

- `Find the VIP Customers list.`
- `Show me our static contact lists.`
- `Search for lists with "webinar" in the name.`
- `Find the list I need to add these contacts to.`

### manage\_list\_members tool

The **manage\_list\_members** tool adds or removes contacts on a static list. Your LLM uses this tool to curate a list by adding or removing specific contacts.

**Try asking**:

- `Add these contacts to the VIP list.`
- `Remove this contact from the webinar attendee list.`
- `Add Kiran Patel to the "Fall Webinar Series" list.`
- `Take these five contacts off the newsletter list.`

### create\_marketing\_event tool

The **create\_marketing\_event** tool creates a new external marketing event when you provide event details, retrieves a single event when you provide an external event ID, or lists events when you give neither. Your LLM uses this tool to set up a new marketing event or to browse and inspect existing events. The connection that creates an event is the only one that can update it.

**Try asking**:

- `Create a webinar event for next Thursday.`
- `Show me our upcoming marketing events.`
- `Find the event named "Product Demo Webinar."`
- `Create a marketing event organized by Jade Chen.`

### record\_event\_attendance tool

The **record\_event\_attendance** tool sets a subscriber's attendance state for a marketing event. Your LLM uses this tool to register, check in, or cancel an attendee for a marketing event. Only the connection that created the event can record attendance for it. A permission-denied response means this connection doesn't own the event.

**Try asking**:

- `Register Kiran Patel for the product demo webinar.`
- `Mark this attendee as having attended the webinar.`
- `Cancel this registrant's spot in the event.`
- `Check in ariel@example.com to today's webinar.`

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

---
