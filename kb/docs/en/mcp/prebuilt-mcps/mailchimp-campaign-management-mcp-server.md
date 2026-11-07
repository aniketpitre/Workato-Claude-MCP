---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/mailchimp-campaign-management-mcp-server.md
description: >-
  Use the Mailchimp Campaign Management MCP server to connect your LLM to
  Mailchimp with audience curation, campaign authoring, and sending through
  natural conversation.
---

# Mailchimp Campaign Management MCP server

The Mailchimp Campaign Management MCP server enables LLMs to interact with MailChimp for the email-marketing lifecycle through natural conversation. It provides tools to curate audiences, add and tag contacts, assemble campaigns from supplied content, and send or schedule them without requiring direct interaction with the MailChimp interface.

> **MARKETING REPORTS MCP SERVER**
> 
> Use the [Mailchimp Marketing Reports](/en/mcp/prebuilt-mcps/mailchimp-marketing-reports-mcp-server) MCP server for read-only discovery and analytics across audiences, campaigns, and contacts.

## Uses

Use the Mailchimp Campaign Management MCP server to perform the following actions:

- Create audiences and organize the contacts a campaign will reach.
- Add contacts to an audience with a supplied subscription status.
- Update an existing contact's profile fields or status.
- Apply tags to contacts for grouping and targeting.
- Search for contacts to resolve identifiers before updating or tagging.
- Assemble a campaign draft from content you provide, with subject and sender.
- Edit a campaign's subject, sender, or recipient audience.
- Send a test email to preview a campaign before the real send.
- Send a campaign immediately, with explicit user confirmation.
- Schedule a campaign for a future time, or unschedule it before it sends.

### Example prompts

Use the following example prompts to invoke Mailchimp Campaign Management MCP server tools:

- `Add these contacts to my launch list.`
- `Create a new audience for our fall product launch.`
- `Tag these contacts as VIP so we can target them.`
- `Find the contact for jordan@example.com in my newsletter audience.`
- `Draft a campaign to my newsletter audience using this HTML content.`
- `Change the subject line on my draft campaign to "Summer Sale is here".`
- `Send a test of this campaign to me and my teammate.`
- `Send my newsletter campaign now.`
- `Schedule this campaign to send Tuesday at 9am.`
- `Unschedule the campaign I set for tomorrow morning.`

## Mailchimp Campaign Management MCP server tools

The Mailchimp Campaign Management MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_audiences](#list-audiences-tool) | Lists the audiences (lists) in the Mailchimp account. |
| [list\_campaigns](#list-campaigns-tool) | Lists campaigns in the account, with optional status filtering. |
| [get\_campaign](#get-campaign-tool) | Retrieves a single campaign's settings and content. |
| [search\_contacts](#search-contacts-tool) | Searches for contacts by email or name, with optional filtering by an audience. |
| [create\_audience](#create-audience-tool) | Creates a new audience (list) in the account. |
| [add\_contact](#add-contact-tool) | Adds a contact to an audience with a subscription status. |
| [update\_contact](#update-contact-tool) | Updates an existing contact's fields within an audience. |
| [tag\_contact](#tag-contact-tool) | Applies or updates tags on a contact within an audience. |
| [draft\_campaign](#draft-campaign-tool) | Creates a campaign draft from supplied content and settings. |
| [update\_campaign](#update-campaign-tool) | Updates a campaign's subject, sender, or recipient audience. |
| [send\_test](#send-test-tool) | Sends a test email of a campaign to specified addresses. |
| [send\_campaign](#send-campaign-tool) | Sends a campaign immediately. |
| [schedule\_campaign](#schedule-campaign-tool) | Schedules a campaign to send at a future time. |
| [unschedule\_campaign](#unschedule-campaign-tool) | Cancels the schedule of a campaign that has not started sending. |

## Install the Mailchimp Campaign Management MCP server

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
    

## API version

Workato's Mailchimp connector uses Mailchimp's API v2. Refer to Mailchimp's [API documentation](https://mailchimp.com/developer/marketing/docs/fundamentals/#api-versions) for more information.

## Mailchimp Campaign Management connection setup

View Mailchimp Campaign Management connection setup steps

Complete the following steps to connect to Mailchimp in Workato:

> **FEATURE AVAILABILITY**
> 
> The MailChimp connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

1. Provide a **Connection name** that identifies which MailChimp instance Workato is connected to.
   
   ![MailChimp connection](/assets/connection-setup.DX-BBZvF.png)_Create your connection_
   
2. Use the **Location** drop-down menu to select a location for your connection.
   
3. Click **Connect**. This opens a MailChimp login window.
   
4. Enter your MailChimp account username and password. A window opens displaying a summary of the access Workato is provided with for the connection.
   
5. Click **Accept** to complete the connection setup.
   

### Mailchimp role requirements

Each tool's availability depends on the authenticating user's Mailchimp role. A user without the required role receives a permission-denied outcome rather than a partial result. Refer to the Mailchimp [Manage User Levels in Your Account](https://mailchimp.com/help/manage-user-levels-in-your-account/) guide for the complete list of role capabilities.

## How to use Mailchimp Campaign Management MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_audiences tool

The **list\_audiences** tool lists the audiences (lists) in the Mailchimp account. Your LLM uses this tool to return audiences with their identifiers, names, and member counts so it can choose the right audience to add contacts to or target with a campaign, typically before adding contacts or drafting a campaign when the target audience is not yet resolved.

**Try asking**:

- `Show me all the audiences in my Mailchimp account.`
- `Which lists do I have and how many contacts are in each?`
- `Find the audience I should add these contacts to.`

### list\_campaigns tool

The **list\_campaigns** tool lists campaigns in the account, with optional status filtering. Your LLM uses this tool to return campaigns with their identifiers, titles, subjects, status, and target audience so it can find a draft to send or schedule, filtering by status when you specify drafts, scheduled, or sent campaigns.

**Try asking**:

- `List my draft campaigns.`
- `Which campaigns are scheduled to send?`
- `Show me all my sent campaigns.`

### get\_campaign tool

The **get\_campaign** tool retrieves a single campaign's settings and content. Your LLM uses this tool to confirm a campaign's subject, sender, recipient audience, status, and current content before updating, sending, or scheduling it.

**Try asking**:

- `Show me the details of my launch campaign.`
- `What's the current subject and sender on this campaign?`
- `Confirm the recipient audience for this draft before I send it.`

### search\_contacts tool

The **search\_contacts** tool searches for contacts by email or name, with optional filtering by an audience. Your LLM uses this tool to resolve a contact's identifier before updating or tagging it, scoping the search to a single audience when you name one or spanning the account otherwise.

**Try asking**:

- `Find the contact for jordan@example.com.`
- `Search for contacts named Smith in my newsletter audience.`
- `Look up whether this person is already in my launch list.`

### create\_audience tool

The **create\_audience** tool creates a new audience (list) in the account. Your LLM uses this tool when you want to stand up a fresh audience for a campaign, using the name and the required audience settings you supply, such as default campaign settings, a permission reminder, the email-type option, and the physical contact details Mailchimp requires. If this tool fails, check whether your Mailchimp plan has reached its audience quota.

**Try asking**:

- `Create a new audience called "Fall Launch".`
- `Set up a fresh list for our newsletter subscribers.`
- `Make a new audience with these default sender details.`

### add\_contact tool

The **add\_contact** tool adds a contact to an audience with a subscription status. Your LLM uses this tool when you want to add a person to an audience. You can specify whether to set a member to `subscribed`, which immediately adds and asserts pre-existing consent, or send them a double opt-in confirmation email.

**Try asking**:

- `Add jordan@example.com to my newsletter audience as subscribed.`
- `Add these contacts to my launch list and send them a confirmation.`
- `Add this person with their first and last name to my audience.`

### update\_contact tool

The **update\_contact** tool updates an existing contact's fields within an audience. Your LLM uses this tool to change a contact's profile fields or subscription status, resolving the contact first when its identifier is unknown and leaving other fields unchanged.

**Try asking**:

- `Update the first name on this contact to "Jordan".`
- `Change the profile fields for jordan@example.com in my newsletter list.`
- `Fix the last name on this contact record.`

### tag\_contact tool

The **tag\_contact** tool applies or updates tags on a contact within an audience. Your LLM uses this tool to label or group a contact for targeting, adding or removing one or more tags and resolving the contact first when its identifier is unknown.

**Try asking**:

- `Tag jordan@example.com as VIP.`
- `Add the "early access" tag to these contacts.`
- `Remove the "prospect" tag from this contact.`

### draft\_campaign tool

The **draft\_campaign** tool creates a campaign draft from supplied content and settings. Your LLM uses this tool to turn ready content into a Mailchimp campaign, assembling a draft against the chosen audience with the subject and sender you provide and attaching the supplied HTML or plain-text content. The server doesn't generate, design, or modify the content. Subject lines longer than approximately 150 characters are truncated by Mailchimp.

**Try asking**:

- `Draft a campaign to my newsletter audience using this HTML.`
- `Turn this content into a Mailchimp campaign with the subject "Summer Sale".`
- `Create a draft campaign from this plain-text email for my launch list.`

### update\_campaign tool

The **update\_campaign** tool updates a campaign's subject, sender, or recipient audience. Your LLM uses this tool to change a campaign's settings before sending or scheduling, leaving other settings unchanged. It doesn't change body content or send and schedule the campaign.

**Try asking**:

- `Change the subject line on this campaign to "Summer Sale is here".`
- `Update the sender name on my draft campaign.`
- `Switch the recipient audience for this campaign to my VIP list.`

### send\_test tool

The **send\_test** tool sends a test email of a campaign to specified addresses. Your LLM uses this tool to let you preview a campaign safely before the real send by emailing a test to yourself or colleagues, without sending to the campaign's audience. The campaign must have HTML content; a plain-text-only draft can't be tested.

**Try asking**:

- `Send a test of this campaign to me.`
- `Email a preview of my launch campaign to my teammate.`
- `Send a test of this campaign to these addresses.`

### send\_campaign tool

The **send\_campaign** tool sends a campaign immediately. Once sent, a campaign cannot be recalled. The server requires explicit user confirmation that you want to send the campaign now before using this tool.

**Try asking**:

- `Send my newsletter campaign now.`
- `Yes, send the launch campaign to my audience.`
- `Confirm and send this campaign immediately.`

### schedule\_campaign tool

The **schedule\_campaign** tool schedules a campaign to send at a future time. Your LLM uses this tool when you want a campaign to go out at a specific time in the future, after confirming the campaign's settings. Scheduling remains reversible until the send begins. The campaign must have HTML content to be scheduled.

**Try asking**:

- `Schedule this campaign to send Tuesday at 9am.`
- `Set my launch campaign to go out next Monday morning.`
- `Schedule this campaign for tomorrow at noon.`

### unschedule\_campaign tool

The **unschedule\_campaign** tool cancels the schedule of a campaign that has not started sending. Your LLM uses this tool to cancel or change a scheduled send before it goes out, returning the campaign to a paused state. It has no effect once a send has started.

**Try asking**:

- `Unschedule the campaign I set for tomorrow morning.`
- `Cancel the scheduled send on my launch campaign.`
- `Stop this campaign from sending on Tuesday.`

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
