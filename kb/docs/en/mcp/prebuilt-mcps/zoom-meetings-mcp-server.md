---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/zoom-meetings-mcp-server.md'
description: >-
  Use the Zoom Meetings MCP server to connect your LLM to Zoom with a curated
  set of tools to search for past meetings, retrieve recordings and transcripts,
  check attendance, and create or update meetings.
---

# Zoom Meetings MCP server

The Zoom Meetings MCP server enables LLMs to interact with Zoom meeting functionality through natural conversation. It provides tools to search for past meetings, retrieve recordings and transcripts, check attendance, and create or update meetings without requiring direct interaction with the Zoom interface.

## Uses

Use the Zoom Meetings MCP server to perform the following actions:

- Search for past meetings you've hosted or attended
- Retrieve detailed information about specific meetings
- Access cloud recording links for meetings
- Retrieve auto-generated transcripts for meeting review
- Check who attended a meeting and for how long
- Create new scheduled Zoom meetings
- Update existing scheduled meetings

### Example prompts

Use the following example prompts to invoke Zoom Meetings MCP server tools:

- `Find my meetings with Mei from last week.`
- `Get the details for meeting ID 12345678.`
- `Share the recording link for yesterday's standup.`
- `Show me the transcript from the client call on Monday.`
- `Who attended the team meeting on Friday?`
- `Schedule a Zoom meeting for tomorrow at 2pm with the engineering team.`
- `Update the product review meeting to start at 3pm instead.`

## Zoom Meetings MCP server tools

The Zoom Meetings MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_meetings](#search-meetings-tool) | Searches for Zoom meetings the user has hosted or attended. |
| [get\_meeting\_details](#get-meeting-details-tool) | Retrieves detailed information about a specific Zoom meeting. |
| [get\_meeting\_recording](#get-meeting-recording-tool) | Retrieves cloud recording links for a Zoom meeting. |
| [get\_meeting\_transcript](#get-meeting-transcript-tool) | Retrieves the auto-generated transcript for a Zoom meeting. |
| [get\_meeting\_participants](#get-meeting-participants-tool) | Retrieves the attendance list for a Zoom meeting that has occurred. |
| [create\_meeting](#create-meeting-tool) | Creates a new Zoom meeting. |
| [update\_meeting](#update-meeting-tool) | Updates an existing scheduled Zoom meeting. |
| [get\_recording\_vtt](#get-recording-vtt-tool) | Reads the VTT caption file content for a Zoom cloud recording. |

## Install the Zoom Meetings MCP server

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
    

## Zoom connection setup

View Zoom connection setup steps

The Zoom connector uses OAuth 2.0 authentication.

Complete the following steps to connect to Zoom in Workato with OAuth 2.0 authentication:

- [Add an API user](#add-an-api-user)
- [Create a custom OAuth profile](#create-custom-oauth-profile)
- [Connect to Zoom with OAuth 2.0 authentication](#connect)

> **RECOMMENDED SETUP**
> 
> We recommend that you set up a dedicated API user account in Zoom or create a custom OAuth profile to authorize Workato. This allows you to assign the API user to a role with only the necessary permissions.
> 
> Alternatively, you can use an existing Zoom owner or admin account if it has the required permissions. Some admin accounts may have restricted access based on their configuration.

### Add an API user

View add an API user steps

Complete the following steps to set up a provisioned API user for Workato:

1. Sign into your [Zoom account](https://zoom.us/signin).
   
2. Go to **Admin > User Management > Users**.
   
   ![Add users](/assets/users-tab.CCrDasMU.png)_Add users_
   
3. Click **Add Users**.
   
4. Enter an appropriate email for the API user. We recommend an IT admin alias.
   
5. Enter `N/A` or make selections based on your requirements for the following fields: **Department**, **Manager**, **Job Title**, **Location**, and **User Groups**.
   
6. Click **Add**.
   
7. Go to **Admin > Roles**.
   
8. Select **Add Role**.
   
9. Provide a **Role Name** and **Description**.
   
10. Click **Add**.
    
11. Go to **Roles > Roles Settings** and add the following permissions to your Zoom role. Role permissions are required to allow the Workato Zoom connector to perform account-level actions, such as scheduling meetings or webinars on behalf of other Zoom users.
    
    - `Users: View and Edit`
    - `Role management: View and Edit`
    - `Groups: View and Edit`
    - `Recording management: View and Edit`
    - `Zoom rooms: View and Edit`
    - `Meetings: View`
    - `Webinars: View`
    - `Usage reports: View`
    - `Schedule tracking fields: View and Edit`
12. Click **Save Changes**.
    
13. Go to **User Management > Users** and locate the user you created in the preceding steps.
    
14. Click **Edit** and use the **User Role** drop-down menu to select the role you created.
    
15. Click **Save**.
    

### Create a custom OAuth profile

View create a custom OAuth profile steps

Complete the following steps to create a custom OAuth profile for Workato:

1. Go to **Tools > Custom OAuth profiles** in Workato.
   
2. Click **\+ New custom profile**.
   
3. Search for `Zoom` and select it as your app.
   
4. Enter a name for your custom OAuth profile in the **Name** field.
   
5. Click **Create new app**.
   
6. Go to the [Zoom App Marketplace](https://marketplace.zoom.us/) and sign in to your Zoom account if you're not signed in already.
   
7. Click **Develop > Build App**.
   
   ![Build app](/assets/build-app.EiC2eXFV.png)_Build app_
   
8. Choose the kind of app to create from the following options: **General App**, **Server to Server OAuth App**, or **Webhook Only App**. If you can't select the options, you must enable the **Zoom for developers** role. Refer to the Zoom [Select general app features](https://developers.zoom.us/docs/build-flow/create-oauth-apps/#prerequisites) page to learn how to enable the **Zoom for developers** role.
   
9. Click **Create**.
   
10. Enter a name for your app and select how the app is managed. Refer to the Zoom [Step 2: Maintain basic information](https://developers.zoom.us/docs/build-flow/create-oauth-apps/#step-2-maintain-basic-information) page for more information.
    
11. Copy and save the **Client ID** and **Client Secret** for use in Workato.
    
    ![Copy the Client ID and Client Secret](/assets/client-id-client-secret.rM4DBfar.png)_Copy the Client ID and Client Secret_
    
12. Enter `https://www.workato.com/oauth/callback` in the **OAuth Redirect URL** field.
    
13. Optional. Configure settings in the **Access**, **Surface**, and **Embed** tabs as required.
    
14. Go to **Scopes** and click **\+ Add Scopes** to add the required scopes.
    
15. Search for and select the required scopes for your connection.
    
    **MCP server**
    
    The Zoom Meetings MCP server requires the following scopes for tool functionality:
    
    - `meeting:read:list_past_participants`
    - `user:read:user`
    - `meeting:read:list_past_instances`
    - `cloud_recording:read:meeting_transcript`
    - `cloud_recording:read:list_recording_files`
    - `meeting:read:meeting`
    - `meeting:write:meeting`
    - `meeting:update:meeting`
    - `meeting:read:list_meetings`
    
    **Connector**
    
    The Zoom connector requires the following minimum scope:
    
    `user:read:user`
    
16. Click **Done**.
    
17. Go to the **Local Test** tab and select **Preview your app listing page** to ensure your settings are properly configured.
    
18. Return to the **New custom profile** page in Workato and paste the **Client ID** and **Client secret** into their respective fields.
    
    ![Paste the client ID and client secret](/assets/enter-client-id-client-secret.BjbVOHtd.png)_Paste the client ID and client secret_
    
19. Click **Save**.
    

### Connect to Zoom with OAuth 2.0 authentication

View connect to Zoom with OAuth 2.0 authentication steps

Complete the following steps to connect to Zoom in Workato:

1. Click **Create > Connection**.
   
2. Search for `Zoom` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Zoom Connection Setup](/assets/connection-setup-zoom.i8W0drY7.png)_Name your connection_
   
4. Optional. Expand the **Advanced settings** section and use the **OAuth 2.0 scopes** drop-down menu to specify OAuth scopes to request for your connection.
   
5. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile to use for the connection.
   
6. Click **Connect**.
   
7. Sign in to your Zoom account.
   

### Project property configuration

The Zoom Meetings **ZOOM\_SEARCH\_TOPIC\_MAX\_RANGE\_DAYS** defaults to 60 days when you provide a topic filter. A maximum of 60 days prevents the API request from timing out.

You can configure the default search topic maximum days range for your Zoom Meetings MCP server at the project level.

Complete the following steps to configure your search topic maximum days range:

View Project property configuration steps

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Click the **Settings** tab.
   
   ![Click the Settings tab](/assets/project-settings.99X6TiYd.png)_Click the **Settings** tab._
   
4. Select **Project properties**.
   
5. Go to the **ZOOM\_SEARCH\_TOPIC\_MAX\_RANGE\_DAYS** property and click the **Edit** (pencil) icon.
   
   ![Click the Edit (pencil) icon](/assets/zoom-days-range.CevmToFZ.png)_Click the **Edit** (pencil) icon._
   
6. Go to the **Value** field and enter the maximum number of days you plan for Zoom to search through by topic. For example: `30` or `15`.
   

## How to use Zoom Meetings MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_meetings tool

The **search\_meetings** tool searches for Zoom meetings you have hosted or attended with optional filters for participant email, date range, and topic keywords. Your LLM uses this tool to find a past meeting even when you don't have the meeting ID. Results are limited to 50 meetings. Use date range filters to narrow results if needed.

**Try asking**:

- `Find my meetings with Josh from last week.`
- `Search for meetings about the product launch.`
- `Show me all meetings from December.`
- `Find the client call we had on Monday.`

### get\_meeting\_details tool

The **get\_meeting\_details** tool retrieves detailed information about a specific Zoom meeting including topic, scheduled time, duration, host, participant list, join URL, and passcode. Your LLM uses this tool to provide full details about a meeting, either using a known meeting ID or through a general search.

**Try asking**:

- `Get the details for meeting ID 12345678.`
- `Show me the full information for yesterday's standup.`
- `What's the join URL for the team meeting?`
- `Get the passcode for this meeting.`

### get\_meeting\_recording tool

The **get\_meeting\_recording** tool retrieves cloud recording links for a Zoom meeting including video, audio, and chat files if available. Your LLM uses this tool to access or share a meeting recording. Recording links are subject to Zoom access controls and retention policies. Recipients may need Zoom authentication or a passcode to access recordings.

**Try asking**:

- `Get the recording link for yesterday's standup.`
- `Share the recording from the client call on Monday.`
- `Is the recording available for meeting ID 12345678?`
- `Get all recording files from the product demo.`

### get\_meeting\_transcript tool

The **get\_meeting\_transcript** tool retrieves the auto-generated transcript for a Zoom meeting with speaker labels and timestamps if available. Your LLM uses this tool to provide a meeting summary, action items, or to search for what was said. Transcript availability depends on the host's Zoom settings. Large transcripts may truncate due to response size limits.

**Try asking**:

- `Show me the transcript from the client call on Monday.`
- `Get the transcript for yesterday's team meeting.`
- `What was discussed in the product review meeting?`
- `Summarize the key points from the meeting transcript.`

### get\_meeting\_participants tool

The **get\_meeting\_participants** tool retrieves the attendance list for a completed Zoom meeting, including participant names, emails (if available), join and leave times, and total duration. Your LLM uses this tool to verify who attended a meeting or check attendance patterns.

**Try asking**:

- `Who attended the team meeting on Friday?`
- `Show me the attendance list for yesterday's standup.`
- `How long did Marco stay in the client call?`
- `Get the participant list for meeting ID 12345678.`

### create\_meeting tool

The **create\_meeting** tool creates a new Zoom meeting with specified topic, start time, duration, agenda, and invitees. Your LLM uses this tool to schedule a new Zoom meeting.

**Try asking**:

- `Schedule a Zoom meeting for tomorrow at 2pm with the engineering team.`
- `Create a meeting called 'Product Demo' for next Monday at 10am.`
- `Set up a 30-minute standup for Friday morning.`
- `Schedule a client call for next Wednesday at 3pm and invite jade@acme.com.`

### update\_meeting tool

The **update\_meeting** tool updates an existing scheduled Zoom meeting including topic, start time, duration, or agenda. Your LLM uses this tool to modify an existing meeting's time, title, or description.

**Try asking**:

- `Update the product review meeting to start at 3pm instead.`
- `Change the topic of tomorrow's meeting to 'Q1 Planning'.`
- `Extend the client call duration to 90 minutes.`
- `Move Friday's standup to 10am.`

### get\_recording\_vtt tool

The **get\_recording\_vtt** tool fetches the VTT caption file content for a Zoom cloud recording. Your LLM uses this tool to read the captions of recordings. This tool requires the `download_url` returned by a prior `get_meeting_recording` call because it doesn't perform its own recording lookup.

**Try asking**:

- `Get the captions from the recording we pulled earlier.`
- `Show me the VTT file content for this recording.`
- `Fetch the caption file from yesterday's meeting recording.`
- `Read the VTT captions for the client call recording.`

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
