---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/google-docs-mcp-server.md'
description: >-
  Use the Google Docs MCP server to connect your LLM to Google Docs with a
  curated set of tools to author content, apply edits, propose suggestions,
  manage comments, and surface mentions.
---

# Google Docs MCP server

The Google Docs MCP server enables LLMs to create, read, update, and collaborate on Google Docs in a reliable, permission-respecting manner through natural conversation. It provides tools to author content, apply edits, propose suggestions, manage comments, surface mentions, and understand recent changes without requiring direct interaction with the Google Docs interface.

## Uses

Use the Google Docs MCP server when you plan to perform the following actions:

- Create new Google Docs with specified titles and initial content
- Read and review document content for summarization or analysis
- Update and revise specific sections of existing documents
- Find specific blocks or sections within documents
- Add, list, and reply to comments for feedback and collaboration
- Manage suggested edits and track pending changes
- Identify and review mentions within documents
- Resolve comment threads when feedback is addressed

### Example prompts

Use the following example prompts to invoke Google Docs MCP server tools:

- `Create a new Google Doc called 'Q4 Product Roadmap' with an outline.`
- `Read the quarterly report document and summarize the key findings.`
- `Update the executive summary section in the proposal document.`
- `Find the paragraph that mentions revenue projections.`
- `Add a comment to the budget section asking about the timeline.`
- `Show me all the comments on the project plan document.`
- `Reply to Jade's comment about the deadline.`
- `Who is mentioned in the marketing strategy document?`

## Google Docs MCP server tools

The Google Docs MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [create\_document](#create-document-tool) | Creates a new Google Doc under your identity with the title and optional initial content you specify. |
| [get\_document\_info](#get-document-info-tool) | Retrieves metadata about a Google Doc needed for tab selection and safe write operations. |
| [get\_document\_content](#get-document-content-tool) | Retrieves the content of a Google Doc. |
| [find\_blocks](#find-blocks-tool) | Identifies content blocks within a Google Doc that match the text or structural criteria you provide. |
| [update\_document\_content](#update-document-content-tool) | Updates an existing Google Doc. |
| [list\_suggestions](#list-suggestions-tool) | Retrieves suggested edits in a Google Doc with structured context. |
| [add\_comment](#add-comment-tool) | Adds a new comment to a Google Doc. |
| [list\_comments](#list-comments-tool) | Retrieves comment threads for a Google Doc. |
| [reply\_to\_comment](#reply-to-comment-tool) | Adds a reply to an existing comment thread in a Google Doc. |
| [resolve\_comment](#resolve-comment-tool) | Resolves an existing comment thread in a Google Doc. |
| [list\_mentions](#list-mentions-tool) | Retrieves mentions in a Google Doc with context about who or what is mentioned and where. |

## Install the Google Docs MCP server

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
    

## Google Docs connection setup

View Google Docs connection setup steps

Google Docs supports the following authentication types:

- [OAuth 2.0](#oauth2)
- [Service account](#service-account)

> **SERVICE ACCOUNT AUTHENTICATION**
> 
> You can use a service account to authenticate without a personal user account. For consistent use, Workato recommends service account authentication.

### Download the Google Docs connector from the Community library

View steps to download the Google Docs connector from the community library

Complete the following steps to install the connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

### OAuth 2.0

View OAuth 2.0 connection setup steps

Complete the following steps to connect to Google Docs in Workato with OAuth 2.0 authentication:

- [Configure the OAuth consent screen](#consent-screen)
- [Delegate domain-wide authority to the service account](#delegate-authority-to-the-service-account)
- [Generate a client ID and client secret](#generate-client-id-and-secret)
- [Connect to Google Docs with OAuth 2.0](#oauth2-connect)

#### Configure the OAuth consent screen

View configure the OAuth consent screen steps

Complete the following steps to configure the OAuth consent screen:

1. Open the [Google Cloud Console](https://console.cloud.google.com) and go to **APIs & Services > OAuth consent screen**.
   
2. Click **Get started**.
   
3. Enter `Workato` in the **App name** field.
   
4. Enter an email in the **User support email** field.
   
5. Click **Next**.
   
6. Select **External** as the **Audience**. Refer to [Manage App Audience](https://support.google.com/cloud/answer/15549945?sjid=3043175652946470283-NC&authuser=1) to learn more about user types.
   
7. Click **Next**.
   
8. Enter an email address in the **Contact information** section.
   
9. Select the checkbox to agree to Google API Services User Data Policy and click **Continue**. Refer to [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy) for more information.
   
10. Click **Create**.
    
11. Click the **Data access** tab and select **Add or Remove Scopes**.
    
12. Select the necessary scopes, such as:
    
    - `https://www.googleapis.com/auth/documents`
    - `https://www.googleapis.com/auth/documents.readonly`
13. Click **Save**.
    

#### Delegate domain-wide authority to the service account

View delegate domain-wide authority to the service account steps

Complete the following steps to delegate domain-wide authority to the service account:

1. Open the [Google Admin console](https://admin.google.com/) and go to the **Main menu**.
   
2. Go to **Security > Access and data control > API Controls**.
   
3. Go to **Security > Access and data control > API Controls > Domain-wide Delegation**.
   
4. Click **Manage Domain Wide Delegation**.
   
5. Click **Add new**.
   
6. Enter the **Client ID** from the service account JSON file.
   
7. Add the necessary scopes for your [OAuth consent screen configuration](#consent-screen) in the **OAuth scopes (comma-delimited)** field.
   
8. Click **Authorize**.
   

#### Generate a client ID and client secret

Refer to the Google [Manage OAuth Clients](https://support.google.com/cloud/answer/15549257?hl=en&ref_topic=15540269&sjid=11430921100578225870-NC) guide to create a client ID and secret using `https://www.workato.com/oauth/callback` as the redirect URI.

#### Connect to Google Docs with OAuth 2.0 authentication

View connect to Google Docs with OAuth 2.0 authentication steps

Complete the following steps to set up your connection with OAuth 2.0 authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Google Docs` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field. ![OAuth 2.0 connection](/assets/oauth2.BZplQRFm.png)_OAuth 2.0 connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Client ID** and **Client secret**. Refer to the Google [Manage OAuth Clients](https://support.google.com/cloud/answer/15549257?hl=en&ref_topic=15540269&sjid=11430921100578225870-NC) guide to generate these values using `https://www.workato.com/oauth/callback` as the redirect URI.
   
6. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
7. Click **Sign in with Google**.
   

### Service account authentication

A Google service account is a specialized Google account associated with a Google Cloud Project (GCP) that can run API requests on your behalf.

Service accounts provide the following benefits:

- **Continuous operation:** Service accounts ensure that operations continue even if individual user permissions change.
- **Dedicated permissions:** Service accounts can only access projects that you share with them.
- **Dedicated API quotas:** You can manage a service account's API quotas through GCP and request quota increases directly from Google.

Refer to the [Google service account documentation](https://cloud.google.com/iam/docs/understanding-service-accounts) to learn more about service accounts.

View service account connection setup steps

Complete the following steps to connect to Google Docs in Workato with service account authentication:

- [Create a service account and generate a private key](#set-up-a-google-service-account)
- [Share Google Docs with the service account](#share-docs)
- [Connect to Google Docs with service account authentication](#service-account-connect)

> **PREREQUISITES**
> 
> You must [Enable the Google Docs API](https://support.google.com/googleapi/answer/6158841) in the Google Cloud API console before you can connect to Google Docs with service account authentication.

#### Set up a Google service account

View set up a Google service account steps

Complete the following steps to set up a Google service account:

1. [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating) in your GCP project.
   
2. Go to **IAM & Admin > Service accounts**. Ensure your dashboard is scoped to the project that contains your service account.
   
   ![Check the scope of your dashboard.](/assets/service-project-scope.8Rf50DK2.png)_Check the scope of your dashboard._
   
3. Click the **Email** of the service account you intend to use.
   
   ![Click the email of the service account you intend to use.](/assets/service-email-button.C9qaZFkJ.png)_Click the **Email** of the service account you intend to use._
   
4. Copy the service account's **Email** and save it to configure your connection later.
   
   ![Copy the account's email](/assets/service-account-email.DM6BBBhN.png)_Copy the account's **Email**._
   
5. Go to the **KEYS** tab.
   
6. [Generate a private key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and download it in JSON format. You can only download the key once.
   
7. Open the JSON file, then copy the entire private key from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----\n` (inclusive) and save it to configure your connection later.
   

#### Share Google Docs with the service account

View share Google Docs with the service account steps

Complete the following steps to share a Google Doc with the service account:

1. Open Google Docs and select the document you plan to integrate.
   
2. Click **Share** and enter the service account email.
   
3. Assign the appropriate permissions.
   
4. Click **Send**.
   

#### Connect to Google Docs with service account authentication

View connect to Google Docs with service account authentication steps

Complete the following steps to set up your connection with a service account:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Google Docs` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field. ![Service account connection](/assets/service-account.BTGgHdjM.png)_Service account connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Auth type** drop-down menu to select **Service account**.
   
6. Enter your service account email address in the **Service account email** field.
   
7. Enter your private key from the downloaded JSON in the **Private key** field. Refer to [Create a service account and generate a private key](#set-up-a-google-service-account) for more information.
   
8. Click **Sign in with Google**.
   

## How to use Google Docs MCP server tools

Refer to the following sections for detailed information on available tools:

### create\_document tool

The **create\_document** tool creates a new Google Doc under your identity with the title and optional initial content you provide. Your LLM uses this tool to create a new Google Doc or turn a discussion, notes, or outline into a document. **Try asking**:

- `Create a new Google Doc called 'Q4 Product Roadmap' with section headers for Goals, Timeline, and Resources.`
- `Turn our meeting notes into a new document titled 'Project Kickoff Meeting'.`
- `Make a new Google Doc for the customer proposal with an executive summary section.`
- `Create a document called 'Team OKRs' with an outline structure.`

### get\_document\_info tool

The **get\_document\_info** tool retrieves metadata about a Google Doc needed for tab selection and safe write operations, without returning document content blocks. Your LLM uses this tool to refer to a specific tab, obtain the current revision ID before attempting a write operation, or understand document structure.

**Try asking**:

- `Get the metadata for the quarterly report document.`
- `What tabs exist in the project plan Google Doc?`
- `Show me the document info for the Appendix tab.`
- `Check the revision ID for the proposal before I update it.`

### get\_document\_content tool

The **get\_document\_content** tool retrieves the content of a Google Doc. Your LLM uses this tool to read, review, or use a document as input for downstream tasks such as rewriting, summarization, or quality checks.

**Try asking**:

- `Read the quarterly report and summarize the key findings.`
- `Show me the contents of the project requirements document.`
- `Review the customer proposal and identify any gaps.`
- `Extract the action items from the meeting notes document.`

### find\_blocks tool

The **find\_blocks** tool identifies content blocks within a Google Doc that match the text or structural criteria you provide. Your LLM uses this tool to locate specific sections before applying edits, refer to content by description, or find sections by matching text.

**Try asking**:

- `Find the paragraph that starts with 'Our revenue projections'.`
- `Locate the Executive Summary section in the proposal.`
- `Find all headings that mention 'Timeline' in the project plan.`
- `Identify the block containing the budget breakdown.`

### update\_document\_content tool

The **update\_document\_content** tool updates an existing Google Doc. Your LLM uses this tool to revise, polish, or update an existing document, including structural changes such as inserting sections or changing heading levels.

**Try asking**:

- `Update the executive summary to include the new revenue figures.`
- `Change the Timeline section heading to 'Project Timeline and Milestones'.`
- `Insert a new paragraph after the introduction explaining the methodology.`
- `Revise the conclusion to emphasize the next steps.`

### list\_suggestions tool

The **list\_suggestions** tool retrieves suggested edits in a Google Doc with sufficient context to understand what suggestions are pending. Your LLM uses this tool to identify suggested edits that are still pending, review suggested changes before applying direct edits, or understand who suggested what and where.

**Try asking**:

- `Show me the suggestions on the quarterly report.`
- `What edits have been suggested in the project plan?`
- `List all pending suggestions in this document.`
- `Who suggested changes to the executive summary?`

### add\_comment tool

The **add\_comment** tool adds a new comment to a Google Doc. Your LLM uses this tool to leave feedback, ask a question, or add commentary in a document without proposing a specific content change.

**Try asking**:

- `Add a comment to the budget section asking about the contingency allocation.`
- `Leave feedback on the timeline requesting clarification on Phase 2.`
- `Comment on the executive summary suggesting we add customer testimonials.`
- `Ask a question in the methodology section about the data sources.`

### list\_comments tool

The **list\_comments** tool retrieves comment threads for a Google Doc with sufficient context to allow follow-on actions such as replying or resolving. Your LLM uses this tool to identify open feedback to address, find a comment thread to reply to, or see what comments are still outstanding.

**Try asking**:

- `Show me all the comments on the project plan.`
- `What feedback is still open on the quarterly report?`
- `List the comment threads that need responses.`
- `What comments are outstanding on this document?`

### reply\_to\_comment tool

The **reply\_to\_comment** tool adds a reply to an existing comment thread in a Google Doc. Your LLM uses this tool to respond within an existing comment thread.

**Try asking**:

- `Reply to Josh's comment about the timeline with an updated deadline.`
- `Respond to the feedback on the budget section.`
- `Answer Erin's question about the methodology.`
- `Reply to the comment asking for more details on Phase 2.`

### resolve\_comment tool

The **resolve\_comment** tool resolves an existing comment thread in a Google Doc, marking it as addressed. Your LLM uses this tool to mark feedback as addressed or close completed comment threads.

**Try asking**:

- `Resolve the comment about the budget now that it's updated.`
- `Mark Sarah's feedback as addressed.`
- `Close the comment thread about the timeline.`
- `Resolve all comments related to the executive summary.`

### list\_mentions tool

The **list\_mentions** tool retrieves mentions in a Google Doc with context about who or what is mentioned and where. Your LLM uses this tool to find who is mentioned in the document, identify where someone is referenced, or understand who is tagged in specific sections.

**Try asking**:

- `Who is mentioned in the project plan document?`
- `Where is Sarah referenced in the quarterly report?`
- `Show me all mentions of the engineering team.`
- `Find where Jordan is tagged in this document.`

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
