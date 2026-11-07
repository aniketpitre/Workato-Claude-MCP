---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/trello-mcp-server.md'
description: >-
  Use the Trello MCP server to connect your LLM to Trello with tools to
  discover, read, create, and update assets for task management and project
  tracking.
---

# Trello MCP server

The Trello MCP server enables LLMs to interact with Trello workspaces on behalf of users for task management and project tracking through natural conversation. It provides tools to discover boards and lists, retrieve and filter cards, read full card details, create and update cards, post comments, update checklist items, and create boards without requiring direct interaction with the Trello interface.

## Uses

Use the Trello MCP server when you plan to perform the following actions:

- Check which cards are assigned to you or your team, filtered by assignee, due date, or label.
- Review cards that are overdue or due soon across one or more boards.
- Read full card details including description, checklist progress, and attachment metadata.
- Create one or more cards from a task list or meeting notes.
- Move cards between lists to reflect workflow progression.
- Update card titles, descriptions, or due dates.
- Post comments on cards as status updates or progress notes.
- Mark checklist items complete or incomplete to track task progress.
- Create a new Trello board as a starting point for a project.

### Example prompts

Use the following example prompts to invoke Trello MCP server tools:

- `What cards are assigned to me on the Marketing board?`
- `Show me everything that's due this week across my boards.`
- `Create cards for these action items from today's meeting: update the roadmap, schedule the design review, and send the stakeholder update.`
- `Move the 'Update homepage copy' card to the 'Done' list.`
- `Give me the full details on the 'API integration' card, including the checklist.`
- `Add a comment to the 'Q3 planning' card saying 'Draft sent to stakeholders for review.'`
- `Mark the 'Write unit tests' checklist item on the 'Backend refactor' card as complete.`
- `What cards are overdue on the 'Sprint 12' board?`
- `Give me a workload summary for the Product board. How many cards are in each list and who's assigned?`
- `Create a new board called 'Q4 Initiatives'.`

## Trello MCP server tools

The Trello MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_boards](#list-boards-tool) | Retrieves all Trello boards accessible to the authenticated user. Supports pagination. |
| [list\_lists](#list-lists-tool) | Retrieves all lists on a specified Trello board, returning list IDs and names. |
| [list\_cards](#list-cards-tool) | Retrieves cards on a board or list with optional server-side filtering and pagination. |
| [get\_card\_details](#get-card-details-tool) | Retrieves full card details including description, checklists, and attachment metadata. |
| [create\_card](#create-card-tool) | Creates a new card in a specified list. Requires user approval. Not idempotent. |
| [update\_card](#update-card-tool) | Modifies card fields or moves a card to a different list. Requires user approval. Idempotent. |
| [create\_board](#create-board-tool) | Creates a new empty Trello board in the user's workspace. Requires user approval. Not idempotent. |
| [add\_comment](#add-comment-tool) | Posts a new comment on a specified card. Requires user approval. Not idempotent. |
| [update\_checklist\_item](#update-checklist-item-tool) | Marks a checklist item within a card as complete or incomplete. Requires user approval. Idempotent. |

## Install the Trello MCP server

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
    

## Trello connection setup

View Trello connection setup steps

Complete the following steps to connect to Trello in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Trello` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Trello](/assets/connect-to-trello.thFd_ZNH.png)_Connect to Trello_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
6. Click **Connect**.
   
7. Sign in to the Trello account you plan to connect to, then click **Allow** to grant Workato access and complete the connection.
   

## How to use Trello MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_boards tool

The **list\_boards** tool retrieves all Trello boards accessible to the authenticated user, with pagination support. Your LLM uses this tool as the root discovery step whenever a board ID is needed.

**Try asking**:

- `Show me all my Trello boards.`
- `Which board should I use for the Q3 launch project?`
- `What boards do I have access to in Trello?`
- `List my active boards — I want to pick one to review.`

### list\_lists tool

The **list\_lists** tool retrieves information about all lists on a specified Trello board. Your LLM uses this tool to obtain list IDs for write operations such as creating or moving a card.

**Try asking**:

- `What lists are on the Product Roadmap board?`
- `Show me the columns on the Sprint 12 board before I move a card.`
- `Which lists are available on the Marketing board?`
- `I want to create a card — what lists can I choose from on the Dev board?`

### list\_cards tool

The **list\_cards** tool retrieves cards on a specified board or list with optional server-side filtering and pagination. Your LLM uses this tool to find cards assigned to a person, cards due within a date range, cards with a specific label, or all cards on a board or list. This tool uses server-side filters to reduce token usage and improve reliability.

**Try asking**:

- `What cards are assigned to me on the Design board?`
- `Show me all cards due before Friday on the Sprint 12 board.`
- `List all cards labeled 'urgent' on the Marketing board.`
- `What's in the In Progress list on the Backend board?`

### get\_card\_details tool

The **get\_card\_details** tool retrieves full card details, including description, checklists, and attachment metadata. Your LLM uses this tool when a user wants to review a specific card in depth, check checklist completion, or look up attachment links. Retrieving checklist information from this tool is a prerequisite to using the **update\_checklist\_item** tool.

**Try asking**:

- `Give me the full details on the 'Homepage redesign' card.`
- `What's the checklist progress on the 'API migration' card?`
- `Are there any attachments on the 'Brand guidelines' card?`
- `Walk me through everything on the 'Q4 planning' card before our meeting.`

### create\_card tool

The **create\_card** tool creates a new card in a specified list. Your LLM uses this tool to capture action items, tasks, or notes as Trello cards, either one at a time or in batches. The tool shows a preview and requests user approval before creating a card.

**Try asking**:

- `Create a card called 'Follow up with legal' in the Backlog list on the Contracts board.`
- `Add these three action items from today's meeting as cards in the To Do list.`
- `Capture 'Write release notes' as a card on the Sprint 13 board.`
- `Create a card for the homepage bug with due date end of next week.`

### update\_card tool

The **update\_card** tool modifies card fields or moves a card to a different list. Your LLM uses this tool to update a card's title, description, or due date, or to move a card between lists to reflect progress.

**Try asking**:

- `Move the 'Write API docs' card to the Done list.`
- `Update the due date on the 'Homepage redesign' card to next Monday.`
- `Change the title of the 'Fix login bug' card to 'Fix OAuth login timeout bug'.`

### create\_board tool

The **create\_board** tool creates a new empty Trello board in the user's workspace. Your LLM uses this tool when a user wants to start a new project board. The board is created empty, and the user must add lists manually in the Trello UI afterward.

**Try asking**:

- `Create a new Trello board called 'Q4 Initiatives'.`
- `I need a new board for the rebrand project — can you set one up?`
- `Create a board called 'Customer Feedback Tracker'.`
- `Set up a new board called '2026 Roadmap Planning'.`

### add\_comment tool

The **add\_comment** tool posts a comment on a specified card as the authenticated user. Your LLM uses this tool to log status updates, notes, or decisions on a card. Your LLM asks for approval before posting a comment.

> **COMMENT LIMITATIONS**
> 
> The Trello MCP server can't read comments back. Open a card directly in Trello to review its comment history.

**Try asking**:

- `Add a comment to the 'Homepage redesign' card: 'Mockups approved by stakeholders, moving to dev.'`
- `Post a status update on the 'Q3 planning' card saying the draft is ready for review.`
- `Leave a note on the 'API migration' card: 'Blocked — waiting on security sign-off.'`
- `Comment on the 'Release prep' card that testing is complete.`

### update\_checklist\_item tool

The **update\_checklist\_item** tool marks a checklist item within a card as complete or incomplete. Your LLM uses this tool after calling **get\_card\_details** to retrieve the correct checklist item ID, then applies the state change with user approval. This tool cannot create or delete checklist items; it can only toggle their completion state.

**Try asking**:

- `Mark the 'Write unit tests' checklist item on the 'Backend refactor' card as done.`
- `Check off 'Send invites' on the 'Event planning' card checklist.`
- `Uncheck the 'Deploy to staging' item on the 'Release v2.1' card — we need to redo it.`

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
  https://docs.workato.com/en/mcp/prebuilt-mcps/wordpress-content-operations-mcp-server.md
description: >-
  Use the WordPress Content Operations MCP server to connect your LLM to
  WordPress with tools to create, update, and manage posts, pages, custom post
  types, categories, tags, media, and comments through natural language.
---

# WordPress Content Operations MCP server

The WordPress Content Operations MCP server enables LLMs to create, retrieve, update, and manage structured content on a WordPress site through natural conversation. It provides direct access to core content objects, including posts, pages, custom post types, taxonomy, media metadata, and comments without direct interaction with the WordPress interface.

## Uses

Use the WordPress Content Operations MCP server to perform the following actions:

- List, retrieve, create, update, and trash posts
- List, retrieve, create, update, and trash pages
- Discover available post types and retrieve schema definitions for custom post types
- List, retrieve, create, and update categories
- List, create, and update tags
- List and retrieve media items from the WordPress media library
- Update metadata for media items, including titles, alt text, descriptions, and captions
- List and retrieve comments filtered by post, status, and recency
- Moderate comments by approving, holding, or marking as spam
- Trash comments and reply to existing comments

### Example prompts

Use the following example prompts to invoke WordPress Content Operations MCP server tools:

- `Show me all draft posts.`
- `Get the full content of this post before I update it.`
- `Create a new blog post with this content.`
- `Update the title and status of this post.`
- `Move this post to trash.`
- `List all published pages on the site.`
- `Create a new page for the About section.`
- `What content types are available on this site?`
- `Show me the schema for this custom post type.`
- `List all categories and find the right one for this post.`
- `Create a new tag called "Product Update".`
- `Show me images in the media library I can attach to this post.`
- `Update the alt text on this image for accessibility.`
- `Show me pending comments on this post.`
- `Approve this comment and reply to it.`

## WordPress Content Operations MCP server tools

The WordPress Content Operations MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_posts](#list-posts-tool) | Lists posts filtered by status, post type, and recency. |
| [get\_post](#get-post-tool) | Retrieves full content and metadata for a post. |
| [create\_post](#create-post-tool) | Creates a new post with content and metadata you specify. |
| [update\_post](#update-post-tool) | Updates fields and state of an existing post. |
| [trash\_post](#trash-post-tool) | Moves a post to trash. |
| [list\_pages](#list-pages-tool) | Lists pages filtered by status, hierarchy, and recency. |
| [get\_page](#get-page-tool) | Retrieves full content and metadata for a page. |
| [create\_page](#create-page-tool) | Creates a new page with content and metadata you specify. |
| [update\_page](#update-page-tool) | Updates fields and structure of an existing page. |
| [trash\_page](#trash-page-tool) | Moves a page to trash. |
| [list\_post\_types](#list-post-types-tool) | Lists available post types exposed through the WordPress REST API. |
| [get\_post\_type\_schema](#get-post-type-schema-tool) | Retrieves the schema definition for a post type. |
| [list\_categories](#list-categories-tool) | Lists categories used to organize content. |
| [get\_category](#get-category-tool) | Retrieves details for a category you specify. |
| [create\_category](#create-category-tool) | Creates a new category. |
| [update\_category](#update-category-tool) | Updates an existing category. |
| [list\_tags](#list-tags-tool) | Lists tags used to label and group content. |
| [create\_tag](#create-tag-tool) | Creates a new tag. |
| [update\_tag](#update-tag-tool) | Updates an existing tag. |
| [list\_media](#list-media-tool) | Lists media items stored in the WordPress media library. |
| [get\_media](#get-media-tool) | Retrieves details and metadata for a media item. |
| [update\_media\_metadata](#update-media-metadata-tool) | Updates metadata for an existing media item, including title, alt text, description, and caption. |
| [list\_comments](#list-comments-tool) | Lists comments filtered by post, status, and recency. |
| [get\_comment](#get-comment-tool) | Retrieves full details for a comment. |
| [update\_comment](#update-comment-tool) | Updates the moderation status of an existing comment. |
| [trash\_comment](#trash-comment-tool) | Moves a comment to trash. |
| [reply\_to\_comment](#reply-to-comment-tool) | Creates a reply to an existing comment. |

## Install the WordPress Content Operations MCP server

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
    

### WordPress connection setup

View WordPress connection setup steps

Complete the following steps to connect to WordPress in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `WordPress` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![WordPress connection](/assets/connection-setup.XrOftDED.png)_Create your connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Deployment type** drop-down menu to select one of the following deployment types:
   
   - **WordPress.com**: Hosted sites authenticated with OAuth 2.0.
   - **Self-hosted WordPress**: Sites running WordPress 5.6+ with application passwords enabled.
   - **Legacy (deprecated)**: Only select this option to keep an existing recipe on the legacy v1 API. New integrations should use **WordPress.com** instead.
6. Optional. Use the **Timezone** drop-down menu to select the timezone of the WordPress site. Workato uses the timezone to interpret date-time values returned by the API and to format date-time inputs when sending requests. Defaults to **UTC**.
   
7. Complete the following steps if your **Deployment type** is **Self-hosted WordPress**:
   
   Self-hosted WordPress steps
   
   1. Enter the full URL of your WordPress site, including the scheme, in the **Site URL** field. For example, `https://example.com`. We strongly recommend https because application passwords transmit credentials with basic auth.
      
   2. Enter the username to authenticate with in the **Username** field. Ensure the authentication user has at least an Editor or Administrator role.
      
   3. Enter the password for the WordPress authentication user in the **Application password** field. Refer to the WordPress [Creating an Application Password in wp-admin](https://developer.wordpress.org/advanced-administration/security/application-passwords/#creating-an-application-password-in-wp-admin) guide to create this value.
      
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile to use for the connection.
   
9. Click **Connect**, then click **Approve** to grant Workato access if prompted.
   

## How to use WordPress Content Operations MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_posts tool

The **list\_posts** tool lists posts filtered by status, post type, and recency. Your LLM uses this tool to view recent posts, list drafts, scheduled posts, or unpublished content, or browse post types.

**Try asking**:

- `Show me all draft posts.`
- `List scheduled posts going out this week.`
- `Show me the most recent published posts.`
- `Browse posts of this custom post type.`

### get\_post tool

The **get\_post** tool retrieves full content and metadata for a post. Your LLM uses this tool to retrieve a post or provide full context before updating it.

**Try asking**:

- `Get the full content of this post before I update it.`
- `Show me the metadata for this post.`
- `Retrieve this post so I can review it before publishing.`
- `Pull up the full details for this draft.`

### create\_post tool

The **create\_post** tool creates a new post with content and metadata you specify. Your LLM uses this tool to create or publish content.

**Try asking**:

- `Create a new blog post with this content.`
- `Draft a new post with this title and body.`
- `Publish a new announcement post.`
- `Create a new post and schedule it for next Monday.`

### update\_post tool

The **update\_post** tool updates fields and the state of an existing post. Your LLM uses this tool to modify existing content, such as changing the title, body, status, or metadata of a post.

**Try asking**:

- `Update the title and status of this post.`
- `Change this draft to published.`
- `Update the featured image on this post.`
- `Edit the excerpt on this post.`

### trash\_post tool

The **trash\_post** tool moves a post to trash. Your LLM uses this tool to delete a post.

**Try asking**:

- `Move this post to trash.`
- `Delete this draft post.`
- `Trash this outdated announcement.`
- `Remove this post from the site.`

### list\_pages tool

The **list\_pages** tool lists pages filtered by status, hierarchy, and recency. Your LLM uses this tool to view pages, list drafts or scheduled pages, or browse the site's page structure.

**Try asking**:

- `List all published pages on the site.`
- `Show me draft pages that haven't been published yet.`
- `Browse the page hierarchy for the main navigation.`
- `List all child pages under the Services section.`

### get\_page tool

The **get\_page** tool retrieves full content and metadata for a page. Your LLM uses this to retrieve a page to provide full context before updating it.

**Try asking**:

- `Get the full content of the About page.`
- `Show me this page before I make changes.`
- `Retrieve the metadata for this page.`
- `Pull up the full details for this draft page.`

### create\_page tool

The **create\_page** tool creates a new page with content and metadata you specify. Your LLM uses this tool to create or publish a page.

**Try asking**:

- `Create a new page for the About section.`
- `Add a new Contact Us page to the site.`
- `Create a landing page with this content.`
- `Draft a new page under the Services section.`

### update\_page tool

The **update\_page** tool updates fields and the structure of an existing page. Your LLM uses this tool to modify an existing page.

**Try asking**:

- `Update the content on the About page.`
- `Change this page's parent to the Services section.`
- `Publish this draft page.`
- `Update the title and template for this page.`

### trash\_page tool

The **trash\_page** tool moves a page to trash. Your LLM uses this tool to delete a page.

**Try asking**:

- `Move this page to trash.`
- `Delete the old landing page.`
- `Trash this outdated campaign page.`
- `Remove this page from the site.`

### list\_post\_types tool

The **list\_post\_types** tool lists available post types exposed through the WordPress REST API, including name, label, and description. Your LLM uses this tool to retrieve types of content that exist on the site, including what content types can be created or updated, or to discover available custom post types before creating content.

**Try asking**:

- `What content types are available on this site?`
- `What custom post types can I create content for?`
- `Show me all available post types.`
- `What types of content does this WordPress site support?`

### get\_post\_type\_schema tool

The **get\_post\_type\_schema** tool retrieves the schema definition for a post type. Your LLM uses this tool to create or update content for a custom post type when the structure or required fields of a content type are unknown.

**Try asking**:

- `Show me the schema for this custom post type.`
- `What fields are required for this content type?`
- `Get the structure of the Events post type before I create one.`
- `What does the schema look like for this post type?`

### list\_categories tool

The **list\_categories** tool lists categories used to organize content. Your LLM uses this tool to view available categories, find a category by name, or select categories for content creation or updates.

**Try asking**:

- `List all categories and find the right one for this post.`
- `Show me all available categories on the site.`
- `Find the News category before I assign it to this post.`
- `What categories can I use for this content?`

### get\_category tool

The **get\_category** tool retrieves details for a category you specify. Your LLM uses this tool to provide full details about that category.

**Try asking**:

- `Get the details for the Product Updates category.`
- `Show me the description and slug for this category.`
- `Retrieve this category's full details.`
- `Pull up the metadata for this category.`

### create\_category tool

The **create\_category** tool creates a new category. Your LLM uses this tool to add a new category to the site.

**Try asking**:

- `Create a new category called Case Studies.`
- `Add a new category for product announcements.`
- `Set up a new category for the blog.`
- `Create a subcategory under the News section.`

### update\_category tool

The **update\_category** tool updates an existing category. Your LLM uses this tool to modify a category's name, description, slug, or parent.

**Try asking**:

- `Rename this category to Industry News.`
- `Update the description for the Product Updates category.`
- `Change the parent category for this subcategory.`
- `Update the slug for this category.`

### list\_tags tool

The **list\_tags** tool lists tags used to label and group content. Your LLM uses this tool to view available tags, find a tag by name, or select tags for content.

**Try asking**:

- `Show me all available tags on the site.`
- `Find the tag I need before assigning it to this post.`
- `List all tags used on recent posts.`
- `What tags are available for this content?`

### create\_tag tool

The **create\_tag** tool creates a new tag. Your LLM uses this tool to add a new tag to the site.

**Try asking**:

- `Create a new tag called "Product Update".`
- `Add a new tag for this content topic.`
- `Set up a new tag before I assign it to this post.`
- `Create a tag called "How-To" for tutorial content.`

### update\_tag tool

The **update\_tag** tool updates an existing tag. Your LLM uses this tool to modify a tag.

**Try asking**:

- `Rename this tag to "Release Notes".`
- `Update the description for this tag.`
- `Change the slug for this tag.`
- `Update this tag's details.`

### list\_media tool

The **list\_media** tool lists media items stored in the WordPress media library. Your LLM uses this tool to view available media assets or find an image or file to associate with content.

**Try asking**:

- `Show me images in the media library I can attach to this post.`
- `List recent uploads to the media library.`
- `Find a header image I can use for this page.`
- `Browse available media files.`

### get\_media tool

The **get\_media** tool retrieves details and metadata for a media item. Your LLM uses this tool to provide full details about a media item.

**Try asking**:

- `Get the details for this image in the media library.`
- `Show me the metadata for this media file.`
- `Retrieve the alt text and caption for this image.`
- `Pull up the full details for this media item.`

### update\_media\_metadata tool

The **update\_media\_metadata** tool updates metadata for an existing media item, including title, alt text, description, and caption. Your LLM uses this tool to update media metadata, particularly alt text for accessibility.

**Try asking**:

- `Update the alt text on this image for accessibility.`
- `Add a caption to this media item.`
- `Update the title and description for this image.`
- `Set the alt text for all images on this post.`

### list\_comments tool

The **list\_comments** tool lists comments filtered by post, status, and recency. Your LLM uses this tool to view comments on a post or page, review pending, approved, spam, or trashed comments, or browse recent comments.

**Try asking**:

- `Show me pending comments on this post.`
- `List all approved comments on the blog.`
- `Show me recent comments across the site.`
- `Are there any spam comments I need to review?`

### get\_comment tool

The **get\_comment** tool retrieves full details for a comment. Your LLM uses this tool to provide a specific comment for context before moderating or replying.

**Try asking**:

- `Get the full details for this comment.`
- `Show me the content and metadata for this comment before I moderate it.`
- `Retrieve this comment so I can review it before replying.`
- `Pull up the full details for this pending comment.`

### update\_comment tool

The **update\_comment** tool updates the moderation status of an existing comment. Your LLM uses this tool to approve, unapprove, hold, or mark a comment as spam.

**Try asking**:

- `Approve this comment.`
- `Mark this comment as spam.`
- `Hold this comment for further review.`
- `Unapprove this comment.`

### trash\_comment tool

The **trash\_comment** tool moves a comment to trash. Your LLM uses this tool to delete or remove a comment.

**Try asking**:

- `Move this comment to trash.`
- `Delete this spam comment.`
- `Trash this inappropriate comment.`
- `Remove this comment from the post.`

### reply\_to\_comment tool

The **reply\_to\_comment** tool creates a reply to an existing comment. Your LLM uses this tool to respond to a comment on a post or page.

**Try asking**:

- `Reply to this comment with this response.`
- `Post my reply to this customer comment.`
- `Respond to this comment on the blog post.`
- `Add a reply to this pending comment.`

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
