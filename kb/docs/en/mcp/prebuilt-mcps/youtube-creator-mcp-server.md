---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/youtube-creator-mcp-server.md'
description: >-
  Use the YouTube Creator MCP server to connect your LLM to YouTube with a
  curated set of tools to retrieve structured YouTube data, analyze videos and
  channels, manage comments, and organize playlists.
---

# YouTube Creator MCP server

The YouTube Creator MCP server enables LLMs to research YouTube content and manage your channels through natural conversation. It provides tools to retrieve structured YouTube data, analyze videos and channels, manage comments, organize playlists, and update video metadata without requiring direct interaction with the YouTube interface.

## Uses

Use the YouTube Creator MCP server to perform the following actions:

- Search for YouTube videos using keywords and filters
- Retrieve video metadata and public metrics
- Retrieve channel information including subscriber counts and playlists
- List videos published by specific channels
- View and manage comment threads on videos
- Reply to comments on your videos
- Access video caption tracks and transcripts
- List and manage playlists for your channel
- Create new playlists and add videos to them
- Update video titles, descriptions, and tags

### Example prompts

- `Search for videos about Python tutorials from this month.`
- `Get the details for video dQw4w9WgXcQ.`
- `Show me information about the Workato YouTube channel.`
- `List the recent videos from this channel.`
- `Show me the top comments on my latest video.`
- `Reply to that comment thanking them for the feedback.`
- `Get the captions for this video.`
- `Create a new playlist called 'Product Demos'.`
- `Add this video to my Tutorials playlist.`
- `Update the title of my latest video.`

## YouTube Creator MCP server tools

The YouTube Creator MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_videos](#search-videos-tool) | Searches YouTube videos using keywords and optional filters. |
| [get\_video\_details](#get-video-details-tool) | Retrieves metadata and public metrics for a YouTube video you specify. |
| [get\_channel\_info](#get-channel-info-tool) | Retrieves metadata and public metrics for a YouTube channel. |
| [list\_channel\_videos](#list-channel-videos-tool) | Lists videos published by a YouTube channel you specify. |
| [list\_video\_comment\_threads](#list-video-comment-threads-tool) | Retrieves top-level comment threads for a YouTube video. |
| [list\_thread\_replies](#list-thread-replies-tool) | Retrieves replies within a comment thread you specify. |
| [reply\_to\_comment](#reply-to-comment-tool) | Posts a reply to an existing YouTube comment. |
| [list\_video\_caption\_tracks](#list-video-caption-tracks-tool) | Lists available caption tracks for a YouTube video. |
| [download\_caption\_track](#download-caption-track-tool) | Retrieves transcript content for a caption track you specify. |
| [list\_playlists](#list-playlists-tool) | Lists playlists for a YouTube channel. |
| [get\_playlist\_items](#get-playlist-items-tool) | Retrieves videos contained within a playlist you specify. |
| [create\_playlist](#create-playlist-tool) | Creates a new playlist in the authenticated creator's channel. |
| [update\_playlist](#update-playlist-tool) | Updates metadata for an existing playlist. |
| [add\_to\_playlist](#add-to-playlist-tool) | Adds a video to a playlist. |
| [remove\_from\_playlist](#remove-from-playlist-tool) | Removes a video from a playlist. |
| [update\_video\_metadata](#update-video-metadata-tool) | Updates metadata for a YouTube video owned by the authenticated creator. |

## Install the YouTube Creator MCP server

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
    

## YouTube connection setup

You can connect to YouTube with an API key or OAuth 2.0 authorization.

View YouTube connection setup steps

### API key

View API key connection set up steps

#### YouTube setup for API key authentication

Complete the following steps to set up for API key authentication:

> **PREREQUISITES**
> 
> You must have a project in the Google Cloud Console. Refer to the Google [Create a Google Cloud project](https://developers.google.com/workspace/guides/create-project) guide for more information.

1. Sign in to your [Google Cloud Console](https://console.cloud.google.com/).
   
2. Open the navigation menu and select **APIs & Services > Library**.
   
3. Search for `YouTube Data API v3` and select the API.
   
4. Click **Enable**.
   
5. Use the project drop-down menu next to the Google Cloud logo to select the project for which you plan to create credentials.
   
6. Go to **APIs & Services > Credentials**.
   
7. Select **\+ Create credentials > API key**.
   
8. Enter a name for the API key.
   
9. Use the **Select API restrictions** drop-down menu to select `YouTube Data API v3`. This restriction allows the key to call only the YouTube Data API v3.
   
10. Click **OK**.
    
11. Optional. Select the **Authenticate API calls through a service account** checkbox to bind the key to a service account.
    
12. Optional. Select an application type to restrict where you can use the key.
    
13. Click **Create**.
    
14. Copy and save the API key for use in Workato.
    

#### Connect to YouTube with API key authentication

Complete the following steps to set up an API key connection to in Workato:

1. Click **Create > Connection**.
   
2. Search for `YouTube` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![YouTube API key connection setup](/assets/youtube-api-key-connection.BKtrv_au.png)_YouTube API key connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authorization type** drop-down menu to select **API key**.
   
6. Enter the **API key**. Refer to [YouTube setup for API key authentication](#api-key-setup) for more information.
   
7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
8. Click **Connect**.
   

### OAuth 2.0

View OAuth 2.0 connection set up steps

#### Default scopes

You can customize the OAuth scope that Workato requests in the **Scopes** field. Workato requests `read-only` access by default. The following scopes are available:

- `Read-only access (search, comments)`
- `Force SSL (secure access)`
- `YouTube Analytics reports`
- `YouTube Analytics monetary reports`
- `Manage YouTube account`
- `YouTube Partner access`

#### YouTube setup for OAuth 2.0 authentication

Complete the following steps to set up for OAuth 2.0 authentication:

> **PREREQUISITES**
> 
> You must have a project in the Google Cloud Console. Refer to the Google [Create a Google Cloud project](https://developers.google.com/workspace/guides/create-project) guide for more information.

1. Sign in to your [Google Cloud Console](https://console.cloud.google.com/).
   
2. Use the project drop-down menu next to the Google Cloud logo to select the project for which you plan to create credentials.
   
3. Go to **Google Auth platform > Clients**.
   
4. Click **Create Client**.
   
5. Use the **Application type** drop-down menu to select **Web application**.
   
6. Enter a name for the OAuth 2.0 client. Google Cloud Console only displays this name internally.
   
7. Click **\+ Add URI** under **Authorized redirect URIs**.
   
8. Enter `https://www.workato.com/oauth/callback` as the authorized redirect URI.\`
   
9. Click **Create**.
   
10. Copy and save the **Client ID** and **Client secret** for use in Workato.
    
    > **SAVE YOUR SECRET**
    > 
    > Google only displays the client secret once. You must create a new one if you lose the client secret.
    

#### Create a custom OAuth profile

You must create a custom OAuth profile with your client ID and secret before you can connect. Complete the following steps to create a custom OAuth profile for your connection:

1. Go to **Tools > Custom OAuth profiles** in Workato.
   
2. Click **\+ New custom profile**.
   
3. Search for `YouTube` and select it as your app.
   
4. Provide a **Name** for this account.
   
5. Click **Create new app**.
   
6. Create a new OAuth app in your Google Cloud Console account.
   
7. Enter the **Client ID** and **Client secret** in Workato. Refer to [YouTube setup for OAuth 2.0 authentication](#oauth2-setup) for more information.
   
8. Click **Save**.
   
9. Click **Done**.
   

#### Connect to YouTube with OAuth 2.0 authentication

Complete the following steps to set up an OAuth 2.0 connection to in Workato:

1. Click **Create > Connection**.
   
2. Search for `YouTube` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![YouTube OAuth 2.0 connection setup](/assets/youtube-connection.Bp_Re1i_.png)_YouTube OAuth 2.0 connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authorization type** drop-down menu to select **OAuth 2.0**.
   
6. Optional. Expand the **Advanced settings** section to configure **Scopes** for your connection. Defaults to `read-only` if left empty.
   
7. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection. Refer to [Create a custom OAuth profile](#create-a-custom-oauth-profile) for more information.
   
8. Click **Connect**.
   
9. Select a Google account if prompted.
   
10. Click **Allow** to grant Workato access to your Google account.
    

## How to use YouTube Creator MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_videos tool

The **search\_videos** tool searches YouTube videos using keywords and optional filters. Your LLM uses this tool to find videos by topic, keyword, or specific criteria, such as upload date or channel.

**Try asking**:

- `Search for videos about machine learning from this year.`
- `Find Python tutorial videos uploaded this month.`
- `Look for videos about web development with high view counts.`
- `Search for recipe videos from the Food Network channel.`

### get\_video\_details tool

The **get\_video\_details** tool retrieves metadata and public metrics for a YouTube video you specify including title, description, tags, publish date, and engagement metrics. Your LLM uses this tool to provide detailed information about a video.

**Try asking**:

- `Get the details for video dQw4w9WgXcQ.`
- `Show me the metadata for this YouTube video.`
- `What are the tags and description for video dK983ksdls9?`
- `Get the view count and publish date for this video.`

### get\_channel\_info tool

The **get\_channel\_info** tool retrieves metadata and public metrics for a YouTube channel, including title, description, subscriber count (if visible), and uploads. Your LLM uses this tool to provide information about a specific channel.

**Try asking**:

- `Show me information about the Workato YouTube channel.`
- `Get the subscriber count for this channel.`
- `What's the description and metadata for this YouTube channel?`
- `Get channel details for UCxxxxxxxxxxxxxx.`

### list\_channel\_videos tool

The **list\_channel\_videos** tool lists videos published by a YouTube channel you specify. Your LLM uses this tool to browse or retrieve a channel's uploaded content.

**Try asking**:

- `List the recent videos from the Workato channel.`
- `Show me all videos published by this channel.`
- `What videos has this creator uploaded recently?`
- `Get the video list for channel UCxxxxxxxxxxxxxx.`

### list\_video\_comment\_threads tool

The **list\_video\_comment\_threads** tool retrieves top-level comment threads for a YouTube video including comment text, author, timestamp, and reply count. Your LLM uses this tool to review comments on a video.

**Try asking**:

- `Show me the top comments on my latest video.`
- `Get the comment threads for this YouTube video.`
- `What are people saying in the comments on video mawxyl9382?`
- `List the comments on my product demo video.`

### list\_thread\_replies tool

The **list\_thread\_replies** tool retrieves replies within a specific comment thread. Your LLM uses this tool to view the conversation within a comment thread.

**Try asking**:

- `Show me the replies to this comment.`
- `Get all responses in this comment thread.`
- `What did people reply to the top comment?`
- `List the conversation in this comment thread.`

### reply\_to\_comment tool

The **reply\_to\_comment** tool posts a reply to an existing YouTube comment. Your LLM uses this tool to respond to comments on your videos.

**Try asking**:

- `Reply to that comment thanking them for the feedback.`
- `Respond to this comment with the link to the documentation.`
- `Post a reply to the top comment addressing their question.`
- `Thank the commenter for their suggestion.`

### list\_video\_caption\_tracks tool

The **list\_video\_caption\_tracks** tool lists available caption tracks for a YouTube video, including language and track type metadata. Your LLM uses this tool to view available captions for a video.

**Try asking**:

- `What caption tracks are available for this video?`
- `List the languages with captions on this YouTube video.`
- `Show me the available subtitles for video dWls9s8fgsx5.`
- `What caption options does this video have?`

### download\_caption\_track tool

The **download\_caption\_track** tool retrieves transcript content for a caption track you specify. Your LLM uses this tool to access the full transcript or captions for a video.

**Try asking**:

- `Get the English captions for this video.`
- `Download the transcript for this YouTube video.`
- `Show me the full caption text for this video.`
- `Retrieve the subtitles in Spanish for this video.`

### list\_playlists tool

The **list\_playlists** tool lists playlists for a YouTube channel. Your LLM uses this tool to view existing playlists on a channel.

**Try asking**:

- `Show me all my YouTube playlists.`
- `List the playlists on my channel.`
- `What playlists does this channel have?`
- `Get all playlists for the Workato channel.`

### get\_playlist\_items tool

The **get\_playlist\_items** tool retrieves videos contained within a playlist you specify. Your LLM uses this tool to view playlist videos.

**Try asking**:

- `Show me the videos in my Tutorials playlist.`
- `List all videos in this YouTube playlist.`
- `What's in the Product Demos playlist?`
- `Get the contents of playlist PLxxxxxxxxxxxxxx.`

### create\_playlist tool

The **create\_playlist** tool creates a new playlist in your channel and returns the playlist ID. Your LLM uses this tool to create a new playlist to organize your content.

**Try asking**:

- `Create a new playlist called 'Product Demos'.`
- `Make a playlist for my tutorial videos.`
- `Create a playlist titled 'Customer Success Stories'.`
- `Set up a new playlist for webinar recordings.`

### update\_playlist tool

The **update\_playlist** tool updates metadata for an existing playlist, including title, description, and privacy settings. Your LLM uses this tool to modify playlist details.

**Try asking**:

- `Update my Tutorials playlist title to 'Getting Started Guides'.`
- `Change the description of this playlist.`
- `Make this playlist public.`
- `Update the metadata for my Product Demos playlist.`

### add\_to\_playlist tool

The **add\_to\_playlist** tool adds a video to a playlist. Your LLM uses this tool to organize videos into playlists.

**Try asking**:

- `Add this video to my Tutorials playlist.`
- `Put video kjdalsfiao91 in the Product Demos playlist.`
- `Add my latest video to the Featured Content playlist.`
- `Include this video in the Getting Started playlist.`

### remove\_from\_playlist tool

The **remove\_from\_playlist** tool removes a video from a playlist. Your LLM uses this tool to reorganize playlists or remove outdated content.

**Try asking**:

- `Remove this video from the Tutorials playlist.`
- `Take video dskji232sd out of the Featured Content playlist.`
- `Delete the outdated video from my Getting Started playlist.`
- `Remove this from the Product Demos playlist.`

### update\_video\_metadata tool

The **update\_video\_metadata** tool updates metadata for a YouTube video you own, including title, description, and tags. Your LLM uses this tool to modify video details.

**Try asking**:

- `Update the title of my latest video to include 'Tutorial'.`
- `Change the description of video aksdfjskd913.`
- `Add tags to this video: python, tutorial, beginner.`
- `Update my video metadata to improve SEO.`

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
  https://docs.workato.com/en/mcp/prebuilt-mcps/zendesk-knowledge-base-mcp-server.md
description: >-
  Use the Zendesk Knowledge Base MCP server to connect your LLM to Zendesk Guide
  with tools to search, read, navigate, create, and update knowledge base
  articles through natural language.
---

# Zendesk Knowledge Base MCP server

The Zendesk Knowledge Base MCP server enables LLMs to interact with Zendesk Guide knowledge base content through natural conversation. It provides tools to search, retrieve, navigate, create, and update articles without requiring direct interaction with the Zendesk Guide interface.

## Uses

Use the Zendesk Knowledge Base MCP server to perform the following actions:

- Search knowledge base articles using keywords and filters
- Retrieve full content and metadata of articles
- List knowledge base categories to understand top-level organization
- Explore sections within categories
- List articles within sections
- Discover available article labels for metadata updates
- Create new draft knowledge base articles
- Update content and metadata of existing articles
- Navigate knowledge base hierarchy to understand structure
- Document newly resolved issues as draft articles
- Update outdated or incomplete articles

### Example prompts

Use the following example prompts to invoke Zendesk Knowledge Base MCP server tools:

- `Find knowledge base articles about password reset.`
- `Show me the full content of article 8983028.`
- `What categories are in the knowledge base?`
- `List sections in the Billing category.`
- `Show me articles in the Authentication section.`
- `What labels are available for articles?`
- `Create a draft article documenting how to fix the login timeout issue.`
- `Update this article to include the new troubleshooting steps.`
- `Find documentation about API rate limits.`
- `Explore what articles exist in the Technical Support category.`

## Zendesk Knowledge Base MCP server tools

The Zendesk Knowledge Base MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_articles](#search-articles-tool) | Searches knowledge base articles using keywords and optional filters. |
| [get\_article](#get-article-tool) | Retrieves the full content and metadata of a knowledge base article. |
| [list\_categories](#list-categories-tool) | Lists all knowledge base categories. |
| [list\_sections](#list-sections-tool) | Lists sections within a category you specify. |
| [list\_articles\_in\_section](#list-articles-in-section-tool) | Lists articles within a section you specify. |
| [list\_article\_labels](#list-article-labels-tool) | Lists available article labels for metadata updates. |
| [create\_article](#create-article-tool) | Creates a new draft knowledge base article. |
| [update\_article](#update-article-tool) | Updates content and metadata of an existing knowledge base article. |

## Install the Zendesk Knowledge Base MCP server

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
    

## Zendesk connection setup

View Zendesk connection setup steps

The Zendesk connector uses OAuth 2.0 authentication.

> **DEPRECATED AUTHENTICATION METHODS**
> 
> Effective March 31, 2026, you can no longer create new Zendesk connections using Basic authentication or Custom OAuth profiles. This change is required by [Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/).
> 
> Existing connections using these authentication methods will continue to work until **April 30, 2027**. On this date, Zendesk connections still using Basic authentication or a Custom OAuth profile will be terminated, and recipes relying on these connections will stop functioning.

Complete the following steps to connect to Zendesk in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Zendesk` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Zendesk with OAuth 2.0](/assets/oauth2.CJ5g3KV-.png)_Connect to Zendesk with OAuth 2.0_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your Zendesk subdomain in the **Subdomain** field. For example, your subdomain is `acme` if your Zendesk URL is `https://acme.zendesk.com`.
   
6. Click **Connect**.
   
7. Sign in to Zendesk using your credentials to authorize Workato.
   

### Project property configuration

The Zendesk Knowledge Base MCP server supports the following project-level properties to control behavior and defaults:

| Project-level property | Description |
| --- | --- |
| `section_id` | Restricts operations, such as search and retrieval, to a specific Zendesk section. |
| `category_id` | Restricts operations to a specific Zendesk category. |
| `max_article_content_size` | Limits the maximum size of article content returned. Defaults to `50,000`. |
| `default_result_limit` | Sets the default number of results returned by the search tool when no limit is specified by the user or tool. Defaults to `30`. |
| `default_user_segment_id` | Specifies the default user segment applied when creating new articles. |
| `default_permission_group_id` | Defines the default permission group assigned to newly created articles. |
| `default_article_locale` | Determines the default language or locale for newly created articles. Defaults to `en-us`. |

View project-level property configuration steps

Complete the following steps to configure your project-level properties:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Click the **Settings** tab.
   
   ![Click the Settings tab](/assets/project-settings.99X6TiYd.png)_Click the **Settings** tab._
   
4. Select **Project properties**.
   
5. Go to the project property you plan to update and click the **Edit** (pencil) icon.
   
   ![Click the Edit (pencil) icon](/assets/zendesk-knowledge-base-project-property.DGAT1hbT.png)_Click the **Edit** (pencil) icon._
   
6. Go to the **Value** field and make your changes. For example, set `max_article_content_size` to `70000` or `default_result_limit` to `15`.
   

## How to use Zendesk Knowledge Base MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_articles tool

The **search\_articles** tool searches knowledge base articles using keywords and optional filters. Your LLM uses this tool to find documentation, help articles, or information related to a topic.

**Try asking**:

- `Find knowledge base articles about password reset.`
- `Search for documentation on API authentication.`
- `Look for articles about billing errors.`
- `Find help articles containing 'SSO timeout'.`

### get\_article tool

The **get\_article** tool retrieves the full content and metadata of a knowledge base article. Your LLM uses this tool to read or review a specific article in detail.

**Try asking**:

- `Show me the full content of article 803812.`
- `Get the complete text of the password reset article.`
- `Read article 67890 in detail.`
- `What does the API rate limits article say?`

### list\_categories tool

The **list\_categories** tool lists all knowledge base categories. Your LLM uses this tool to understand the top-level organization of the knowledge base.

**Try asking**:

- `What categories are in the knowledge base?`
- `Show me all KB categories.`
- `List the top-level organization of documentation.`
- `What are the main knowledge base sections?`

### list\_sections tool

The **list\_sections** tool lists sections within a category you specify. Your LLM uses this tool after identifying a category to explore its sections.

**Try asking**:

- `List sections in the Billing category.`
- `Show me sections under Technical Support.`
- `What sections exist in the Authentication category?`
- `Explore sections within Getting Started.`

### list\_articles\_in\_section tool

The **list\_articles\_in\_section** tool lists articles within a section you specify. Your LLM uses this tool to explore articles within a known section.

**Try asking**:

- `Show me articles in the Authentication section.`
- `List all articles under Password Management.`
- `What articles are in the API Documentation section?`
- `Display articles in the Troubleshooting section.`

### list\_article\_labels tool

The **list\_article\_labels** tool lists available article labels for metadata updates. Your LLM uses this tool to discover valid label values before updating article labels.

**Try asking**:

- `What labels are available for articles?`
- `Show me the list of article tags.`
- `What metadata labels can I use?`
- `List valid labels for knowledge base articles.`

### create\_article tool

The **create\_article** tool creates a new draft knowledge base article. Your LLM uses this tool to document a new issue or create a new knowledge base article.

**Try asking**:

- `Create a draft article documenting how to fix the login timeout issue.`
- `Make a new KB article about the SSO configuration process.`
- `Document this resolution as a draft article.`
- `Create a knowledge base article for the API rate limit error.`

### update\_article tool

The **update\_article** tool updates content and metadata of an existing knowledge base article. Your LLM uses this tool to modify an existing article.

**Try asking**:

- `Update this article to include the new troubleshooting steps.`
- `Revise article 12345 with the corrected information.`
- `Add the latest workaround to the API timeout article.`
- `Update the password reset article with new screenshots.`

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
  https://docs.workato.com/en/mcp/prebuilt-mcps/zendesk-ticket-management-mcp-server.md
description: >-
  Use the Zendesk Ticket Management MCP server to let LLMs find, create, and
  update Support tickets, manage queues, and monitor SLAs.
---

# Zendesk Ticket Management MCP server

The Zendesk Ticket Management MCP server enables LLMs to manage and explore Zendesk Support tickets across their full lifecycle through natural conversation. It provides tools to find, create, and update support tickets, manage queues, and monitor SLAs without requiring direct interaction with the Zendesk interface.

## Uses

Use the Zendesk MCP server to perform the following actions:

- Search for tickets using keywords or structured filters
- Retrieve full details for specific tickets
- View conversation history and comments on tickets
- Retrieve information about ticket requesters and agents
- List tickets in your personal queue or team queues
- Find unassigned tickets for triage
- Monitor overdue tickets and SLA compliance
- Check when tickets entered specific statuses
- Create new support tickets
- Update ticket fields such as status, priority, and assignee
- Add public replies or internal notes to tickets

### Example prompts

Use the following example prompts to invoke Zendesk Ticket Management MCP server tools:

- `What's the status of ticket #12345?`
- `Show me the conversation on ticket #789.`
- `Find tickets about login failures.`
- `List my open tickets.`
- `What tickets are unassigned?`
- `Which tickets are overdue?`
- `When was ticket #4560 solved?`
- `Create a ticket for Acme Corp about their billing issue.`
- `Set ticket #7892 to high priority.`
- `Reply to the customer on ticket #1432 with the solution.`

## Zendesk MCP server tools

The Zendesk MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [get\_ticket](#get-ticket-tool) | Retrieves full details for a Zendesk ticket by ticket ID. |
| [get\_user](#get-user-tool) | Retrieves basic profile information for a Zendesk user by user ID. |
| [list\_ticket\_comments](#list-ticket-comments-tool) | Retrieves conversation comments for a Zendesk ticket. |
| [search\_tickets](#search-tickets-tool) | Searches Zendesk tickets using keyword queries. |
| [list\_tickets](#list-tickets-tool) | Lists Zendesk tickets using structured filters. |
| [list\_my\_tickets](#list-my-tickets-tool) | Lists tickets assigned to the authenticated user. |
| [list\_unassigned\_tickets](#list-unassigned-tickets-tool) | Lists Zendesk tickets without an assigned agent. |
| [list\_overdue\_tickets](#list-overdue-tickets-tool) | Lists tickets that are overdue or approaching SLA deadlines. |
| [get\_ticket\_status\_transition\_timestamp](#get-ticket-status-transition-timestamp-tool) | Retrieves the timestamp when a ticket most recently entered a status you specify. |
| [create\_ticket](#create-ticket-tool) | Creates a new Zendesk support ticket. |
| [update\_ticket](#update-ticket-tool) | Updates fields on an existing Zendesk ticket. |
| [add\_ticket\_comment](#add-ticket-comment-tool) | Adds a public reply or internal note to a Zendesk ticket. |

## Install the Zendesk MCP server

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
    

## Zendesk connection setup

View Zendesk connection setup steps

The Zendesk connector uses OAuth 2.0 authentication.

> **DEPRECATED AUTHENTICATION METHODS**
> 
> Effective March 31, 2026, you can no longer create new Zendesk connections using Basic authentication or Custom OAuth profiles. This change is required by [Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/).
> 
> Existing connections using these authentication methods will continue to work until **April 30, 2027**. On this date, Zendesk connections still using Basic authentication or a Custom OAuth profile will be terminated, and recipes relying on these connections will stop functioning.

Complete the following steps to connect to Zendesk in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Zendesk` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Zendesk with OAuth 2.0](/assets/oauth2.CJ5g3KV-.png)_Connect to Zendesk with OAuth 2.0_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your Zendesk subdomain in the **Subdomain** field. For example, your subdomain is `acme` if your Zendesk URL is `https://acme.zendesk.com`.
   
6. Click **Connect**.
   
7. Sign in to Zendesk using your credentials to authorize Workato.
   

### Project property configuration

You must configure the **ZENDESK\_SLA\_VIEW** for your Zendesk Ticket Management MCP server at the project level. **ZENDESK\_SLA\_VIEW** is used for the `list_overdue_tickets` tool. You can configure this setting to operate in deterministic or efficient mode. Deterministic mode scans for `SLA-breached` tickets while efficient mode scans for `SLA-nearing tickets`. Zendesk admins must configure Zendesk View IDs for SLA-breached or SLA-nearing tickets. The `list_overdue_tickets` tool queries the View IDs directly when you set the project property in Workato and View IDs are configured and accessible in Zendesk.

The `list_overdue_tickets` tool scans unsolved tickets using Search API with SLA sideloading and filters results by SLA metrics if you don't set the **ZENDESK\_SLA\_VIEW** project property. This fallback is bounded by page and record caps and may return partial results in large accounts.

Complete the following steps to configure your SLA view:

View Project property configuration steps

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Click the **Settings** tab.
   
   ![Click the Settings tab](/assets/project-settings.99X6TiYd.png)_Click the **Settings** tab._
   
4. Select **Project properties**.
   
5. Go to the **ZENDESK\_SLA\_VIEW** property and click the **Edit** (pencil) icon.
   
   ![Click the Edit (pencil) icon](/assets/zendesk-sla-view-project-property.CmKKHSw3.png)_Click the **Edit** (pencil) icon._
   
6. Go to the **Value** field and enter your Zendesk SLA view. For example, `SLA-Breached Tickets` or `SLA-nearing tickets`.
   

## How to use Zendesk MCP server tools

Refer to the following sections for detailed information on available tools:

### get\_ticket tool

The **get\_ticket** tool retrieves full details for a Zendesk ticket by ticket ID. Your LLM uses this tool to retrieve details for a ticket ID you provide.

**Try asking**:

- `What's the status of ticket #4234?`
- `Get the details for ticket 7890.`
- `Show me ticket #4561.`
- `Tell me about ticket 1432.`

### get\_user tool

The **get\_user** tool retrieves basic profile information for a Zendesk user by user ID. Your LLM uses this tool to provide information about a ticket requester or agent, or when additional user context is required after retrieving a ticket.

**Try asking**:

- `Who is the requester for this ticket?`
- `What organization is this customer part of?`
- `Get information about the agent assigned to this ticket.`
- `Tell me about user 9876.`

### list\_ticket\_comments tool

The **list\_ticket\_comments** tool retrieves conversation comments for a Zendesk ticket. Your LLM uses this tool to view replies, notes, or conversation history, or when deeper context is required after retrieving a ticket.

**Try asking**:

- `Show me the conversation on ticket #7890.`
- `What replies are on ticket #4562?`
- `Get the comment history for this ticket.`
- `What notes are on ticket #4325?`

### search\_tickets tool

The **search\_tickets** tool searches Zendesk tickets using keyword queries. Your LLM uses this tool to search with keywords, phrases, or error descriptions to find relevant tickets.

**Try asking**:

- `Find tickets about login failures.`
- `Search for tickets mentioning SSO timeout.`
- `Look for tickets about billing errors.`
- `Find tickets containing 'password reset'.`

### list\_tickets tool

The **list\_tickets** tool lists Zendesk tickets using structured filters. Your LLM uses this tool when you specify structured attributes such as status, assignee, group, or tags.

**Try asking**:

- `Show me open tickets for Acme Corp.`
- `List high-priority tickets assigned to Mei.`
- `Get all pending tickets from this week.`
- `Show me tickets tagged with 'billing'.`

### list\_my\_tickets tool

The **list\_my\_tickets** tool lists Zendesk tickets assigned to you. Your LLM uses this tool to view your work queue or check what tickets are assigned to you.

**Try asking**:

- `What's in my queue?`
- `Show me my open tickets.`
- `What tickets are assigned to me?`
- `What should I work on next?`

### list\_unassigned\_tickets tool

The **list\_unassigned\_tickets** tool lists Zendesk tickets without an assigned agent. Your LLM uses this tool to view unassigned tickets for triage or to identify work that needs to be picked up.

**Try asking**:

- `What tickets are unassigned?`
- `Show me tickets that need to be picked up.`
- `What's in the triage queue?`
- `What tickets haven't been assigned yet?`

### list\_overdue\_tickets tool

The **list\_overdue\_tickets** tool lists tickets that are overdue or approaching SLA deadlines. Your LLM uses this tool to monitor SLA compliance or identify at-risk tickets.

**Try asking**:

- `Which tickets are overdue?`
- `Show me tickets approaching SLA deadlines.`
- `What tickets are at risk?`
- `What needs immediate attention for SLA compliance?`

### get\_ticket\_status\_transition\_timestamp tool

The **get\_ticket\_status\_transition\_timestamp** tool retrieves the timestamp when a ticket most recently entered a status you specify. Your LLM uses this tool to find when a ticket entered a specific lifecycle state, such as when it was solved.

**Try asking**:

- `When was ticket #4561 solved?`
- `When did this ticket move to pending?`
- `What time was ticket #7890 closed?`
- `When did ticket #4324 enter the open status?`

### create\_ticket tool

The **create\_ticket** tool creates a new Zendesk support ticket. Your LLM uses this tool to create a new ticket from customer communications or reported issues.

**Try asking**:

- `Create a ticket for Acme Corp about their billing issue.`
- `File a bug report for the login timeout.`
- `Create a ticket for jade@acme.com about password reset.`
- `Log a new support ticket for the API error.`

### update\_ticket tool

The **update\_ticket** tool updates fields on an existing Zendesk ticket, including status, priority, assignee, and custom fields. Your LLM uses this tool to modify ticket attributes, reassign work, or update status as issues progress.

**Try asking**:

- `Set ticket #7890 to high priority.`
- `Assign ticket #4561 to Marco.`
- `Close ticket #4324.`
- `Change the status of ticket #7890 to pending.`

### add\_ticket\_comment tool

The **add\_ticket\_comment** tool adds a public reply or internal note to a Zendesk ticket. Your LLM uses this tool to reply to customers or add internal notes. Your LLM confirms whether the comment should be public or internal before invoking the tool.

**Try asking**:

- `Reply to the customer on ticket #4324 with the solution.`
- `Add an internal note to ticket #4561 about the troubleshooting steps.`
- `Post a public update to ticket #7890.`
- `Add a private note saying we're waiting on engineering.`

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
