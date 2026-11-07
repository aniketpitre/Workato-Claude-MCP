---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/calendly-scheduling-mcp-server.md
description: >-
  Use the Calendly MCP server to connect your LLM to Calendly with tools to
  book, cancel, and prep for external-facing meetings, share scheduling links,
  and manage event type availability.
---

# Calendly MCP server

The Calendly MCP server enables LLMs to interact with Calendly for external-facing scheduling through natural conversation. It provides tools to access event types, scheduled events, invitee data, and the availability rules governing each event type, so AI-driven workflows can book, modify, and gather context on customer-facing meetings without requiring direct interaction with the Calendly interface.

## Uses

Use the Calendly MCP server to perform the following actions:

- Schedule a meeting with an external party directly, instead of sending a booking link
- Cancel an existing Calendly booking through the Calendly notification lifecycle
- Pull invitee details and intake-question responses before a call
- See who's booked time with you this week, including cancellations and no-shows
- Grab the right Calendly link for an outbound email or message, or generate a single-use link
- Block or open availability on your Calendly event types without logging into Calendly
- List scheduled events and filter by time range, status, event type, or invitee
- Retrieve full booking-level detail, including location specifics and cancellation reason

### Example prompts

Use the following example prompts to invoke Calendly MCP server tools:

- `Book a 30-minute intro call with jane@acme.com for next Tuesday afternoon.`
- `Cancel my call with Sarah Chen on Thursday.`
- `What do I know about my 2pm meeting tomorrow?`
- `Who's booked time with me this week?`
- `Did anyone cancel on me this week?`
- `Give me my intro call booking link.`
- `Generate a single-use scheduling link for my enterprise demo event type.`
- `Turn off my Calendly availability next week.`
- `I'm traveling to London next month — update my available hours to UK business hours.`
- `Show me my upcoming Calendly meetings, grouped by event type.`

## Calendly MCP server tools

The Calendly MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_event\_types](#list-event-types-tool) | Returns the authenticated user's Calendly event types with names, durations, descriptions, scheduling URLs, and active status. |
| [get\_event\_type\_available\_times](#get-event-type-available-times-tool) | Returns the bookable time slots for a specific event type within a given time range, honoring the host's availability schedule, existing bookings, buffers, daily quotas, and minimum notice period. |
| [create\_booking](#create-booking-tool) | Creates a Calendly booking on behalf of an invitee for a given event type and time slot, flowing through the full Calendly lifecycle including calendar invites, reminders, workflow notifications, and integrations. |
| [list\_calendly\_bookings](#list-calendly-bookings-tool) | Returns the authenticated user's Calendly bookings matching the provided filters, including time range, status, event type, and invitee. |
| [get\_calendly\_booking](#get-calendly-booking-tool) | Returns booking-level details for a single Calendly booking: event type, start/end times, host(s), location, status, cancellation reason, and no-show marker. |
| [cancel\_calendly\_booking](#cancel-calendly-booking-tool) | Cancels the specified Calendly booking through the Calendly cancellation flow, triggering invitee notifications and downstream workflows. |
| [get\_invitee\_details](#get-invitee-details-tool) | Returns invitee-level data for a Calendly booking: name, email, time zone, custom question responses, status, and per-invitee reschedule and cancel URLs. |
| [get\_event\_type\_availability](#get-event-type-availability-tool) | Returns the availability rules currently attached to a specific event type: time zone, the recurring weekly schedule, and date-specific overrides. |
| [update\_event\_type\_availability](#update-event-type-availability-tool) | Updates the availability rules attached to a specific event type with overwrite semantics, supporting time zone changes, weekly hours adjustments, and date-specific overrides. |
| [create\_single\_use\_scheduling\_link](#create-single-use-scheduling-link-tool) | Generates a single-use scheduling URL tied to a specific event type that expires after one booking, for use in high-velocity outbound workflows. |

## Install the Calendly MCP server

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
    

## Calendly connection setup

View Calendly connection setup steps

The Calendly connector supports the following authentication types:

- [Personal access token](#personal-access-token)
- [OAuth 2.0](#oauth)

### Personal access token setup

View personal access token setup steps

Complete the following steps to create a personal access token in Calendly:

1. [Sign in](https://calendly.com/login) to your Calendly account.
   
2. Select [Integrations & apps](https://calendly.com/integrations).
   
3. Search for and select [API and webhooks](https://calendly.com/integrations/api_webhooks).
   
4. Generate a new token. If you don't have an existing personal access token, select **Get a token now**. If you already have one, select **Generate new token**.
   
5. Enter a token name and click **Create token**.
   
6. Click **Copy token** to retrieve the token.
   

### Connect to Calendly with personal access token authentication

View connect to Calendly with personal access token authentication steps

Complete the following steps to set up a personal access token authentication connection to { $frontmatter.connector\_name }} in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Calendly` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Personal access token**.
   
6. Enter the **Personal access token**.
   
   ![Connect to Calendly using personal access token authentication](/assets/calendly-pat.CHojATVR.png)_Connect to Calendly using personal access token authentication_
   
7. Click **Connect**.
   

### OAuth client ID and secret setup

View OAuth client ID and secret steps

Complete the following steps to generate your OAuth credentials in Calendly:

1. Go to the [Calendly Developer](https://developer.calendly.com/) page.
   
2. Sign in to your developer account or create a new one.
   
   > **DEVELOPER ACCOUNTS**
   > 
   > Calendly developer accounts are separate from your Calendly user account.
   
3. Select your profile icon and go to **My apps**.
   
4. Click **Create new app** to create an OAuth application.
   
5. Enter the name of your application in the **Name of app** field. For example, `Workato`.
   
6. Select **Web** in the **Kind of app** field.
   
7. Select the environment you plan to associate your application with:
   
   - **Sandbox**
   - **Production**
8. Enter `https://www.workato.com/oauth/callback` in the **Redirect URI** field.
   
9. Click **Save & continue**.
   
10. Copy your **Client ID**, **Client Secret**, and **Webhook signing key**. Store these values securely, as you won't be able to access the **Client ID** and **Client Secret** again.
    

### Connect to Calendly with OAuth 2.0 authentication

View connect to Calendly with OAuth 2.0 authentication steps

Complete the following steps to set up an OAuth 2.0 authentication connection to Calendly in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Calendly` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **OAuth 2.0**.
   
6. Enter the **Client ID** and associated **Client secret**.
   
   ![Connect to Calendly using OAuth 2.0 authentication](/assets/calendly-oauth2.6CfIiBOR.png)_Connect to Calendly using OAuth 2.0 authentication_
   
7. Click **Connect**.
   

## How to use Calendly MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_event\_types tool

The **list\_event\_types** tool returns the authenticated user's Calendly event types with names, durations, descriptions, scheduling URLs, and active status. Your LLM uses this tool to see what meeting types are configured, to find the right booking URL to share, or as the first step before booking on an invitee's behalf.

**Try asking**:

- `What Calendly event types do I have set up?`
- `What's my booking link for enterprise demos?`
- `Show me all my active event types.`
- `Find my discovery call event type so I can book with a prospect.`

### get\_event\_type\_available\_times tool

The **get\_event\_type\_available\_times** tool returns the bookable time slots for a specific event type within a given time range, honoring the host's availability schedule, existing bookings, buffers, daily quotas, and minimum notice period. Your LLM uses this tool to find open slots before booking on an invitee's behalf.

**Try asking**:

- `What times am I free for a 30-minute intro call this week?`
- `Find an open slot for a demo call next Tuesday afternoon.`
- `Show me my available times for a partnership discussion in the next 7 days.`

### create\_booking tool

The **create\_booking** tool creates a Calendly booking on behalf of an invitee for a given event type and time slot, flowing through the full Calendly lifecycle including calendar invites, reminders, workflow notifications, and integrations. Your LLM uses this tool to lock in a meeting immediately instead of sending a link and waiting for the invitee to self-schedule.

**Try asking**:

- `Book a 30-minute intro call with jane@acme.com for next Tuesday at 2pm.`
- `Schedule a demo with the contact I just met at the conference for this Thursday morning.`
- `Book my 3pm discovery call slot with mike@partner.com.`

### list\_calendly\_bookings tool

The **list\_calendly\_bookings** tool returns the authenticated user's Calendly bookings matching the provided filters, including time range, status, event type, and invitee. Your LLM uses this tool to answer questions about upcoming or past bookings. **list\_calendly\_bookings** provides a top-level overview of each booking, while **get\_calendly\_booking** provides more detailed information about a specific booking.

**Try asking**:

- `Who's booked time with me this week?`
- `Show me my canceled meetings from last week.`
- `How many demo requests came in this month?`
- `List my upcoming bookings with jane@acme.com.`

### get\_calendly\_booking tool

The **get\_calendly\_booking** tool returns booking-level details for a single Calendly booking, including event type, start and end times, host(s), location, status, cancellation reason, and no-show marker. Your LLM uses this tool when a question needs more than the summary fields `list_calendly_bookings` provides.

**Try asking**:

- `What's the meeting link for my 2pm call with Sarah Chen?`
- `Why did the prospect cancel their call yesterday?`
- `Did my 10am meeting today get marked as a no-show?`

### cancel\_calendly\_booking tool

The **cancel\_calendly\_booking** tool cancels the specified Calendly booking through the Calendly cancellation flow, triggering invitee notifications and downstream workflows. Your LLM uses this tool when a rep needs to cancel a meeting rather than simply deleting the calendar event.

**Try asking**:

- `Cancel my call with Sarah Chen on Thursday.`
- `Cancel my 2pm tomorrow — the deal fell through.`
- `Cancel my meeting with jane@acme.com and let her know I had a scheduling conflict.`

### get\_invitee\_details tool

The **get\_invitee\_details** tool returns invitee-level data for a Calendly booking, including name, email, time zone, custom question responses, status, and per-invitee reschedule and cancel URLs. Your LLM uses this tool to build pre-meeting context or to retrieve a reschedule link.

**Try asking**:

- `What do I know about my 2pm meeting tomorrow?`
- `Who am I meeting with on Thursday, and what did they say they wanted to discuss?`
- `Get me the reschedule link for my call with jane@acme.com.`

### get\_event\_type\_availability tool

The **get\_event\_type\_availability** tool returns the availability rules currently attached to a specific event type, including time zone, the recurring weekly schedule, and date-specific overrides. Your LLM uses this tool as the required read step before updating availability, because the update operation overwrites the full rule set.

**Try asking**:

- `What are my current availability hours for my discovery call event type?`
- `Show me the availability rules on my demo event type before I make changes.`
- `What time zone is my intro call event type using?`

### update\_event\_type\_availability tool

The **update\_event\_type\_availability** tool updates the availability rules attached to a specific event type with overwrite semantics, supporting time zone changes, weekly hours adjustments, and date-specific overrides. Your LLM uses this tool to block off time, adjust working hours, or change time zone. The **update\_event\_type\_availability** tool uses the **get\_event\_type\_availability** tool to read rules before updating them.

**Try asking**:

- `Turn off my Calendly availability next week.`
- `Block off my Calendly for Monday through Wednesday.`
- `I'm traveling to London next month — update my available hours to UK business hours.`
- `I'm back from PTO, turn my availability back on.`

### create\_single\_use\_scheduling\_link tool

The **create\_single\_use\_scheduling\_link** tool generates a single-use scheduling URL tied to a specific event type that expires after one booking, for use in high-velocity outbound workflows. Your LLM uses this tool when each prospect should get a personalized, non-shareable link.

**Try asking**:

- `Generate a single-use scheduling link for my demo event type.`
- `Give me a one-time booking link for this prospect's intro call.`
- `Create a personalized scheduling link for my outbound email to mike@partner.com.`

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
