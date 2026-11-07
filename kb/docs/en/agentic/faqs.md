---
url: 'https://docs.workato.com/en/agentic/faqs.md'
description: >-
  Answers to common questions about Workato Agentic features, including Agent
  Studio, Workato GO, knowledge bases, security, and MCP.
---

# Agentic - FAQ

Get answers to frequently asked questions about Agentic features, including Agent Studio, Workato GO, and MCP.

## Getting started

How do Agent Studio, Workato GO, and MCP work together?

[Agent Studio](/en/agentic/agent-studio) is where you build genies (AI agents) that can take actions across your business systems.

[Workato GO](/en/agentic/workato-go) provides a chat interface where users interact with genies, plus enterprise search across connected data sources.

[MCP](/en/mcp) exposes your Workato integrations as tools that external AI applications, such as Claude, ChatGPT, and Cursor, can use.

Agent Studio, Workato GO, and MCP connect in several ways:

- Genies you build in Agent Studio can be deployed to Workato GO as their chat interface.
- Workato GO data sources (for example, Google Drive or Slack) can feed into genie knowledge bases.
- Skills can be used by genies directly or exposed as MCP tools for external AI clients.
- MCP servers let both genies and external AI clients use the same Workato integrations.

When should I use Workato genies vs. external AI clients with MCP?

Genies are AI agents hosted and managed by Workato. They handle conversation management, knowledge retrieval, and decision-making about which skills to use.

MCP servers expose your Workato capabilities as tools that external AI clients can use. The external AI client manages the conversation and decides when to call your Workato tools.

Use Workato genies when:

- You want Workato to host and manage the AI agent
- Your users interact through Slack, Microsoft Teams, or Workato GO
- You need built-in knowledge bases for company-specific context
- You need business approvals or app events that trigger proactive actions

Use external AI clients with MCP when:

- Your organization already uses Claude Desktop, ChatGPT, or Cursor
- You want these AI clients to access Workato capabilities as tools
- You're building custom AI applications that need Workato integrations
- You want AI coding assistants to use your business system integrations

You can use both approaches. Build skills once, then deploy them to genies or expose them through MCP to external AI clients. Genies can also consume MCP servers as additional tools. Learn more about [MCP server skills](/en/agentic/skills/mcp-server-skills).

## Agent Studio

### Overview

What is Agent Studio?

[Agent Studio](/en/agentic/agent-studio) is where you build and configure AI agents (genies). These genies perform actions, call workflows, understand context, and execute pre-defined skills to achieve your defined goals.

What are genies?

Genies are AI-powered agents built in Agent Studio that pursue goals you define, adapt to context, and act across apps and data systems.

Genies operate through the following [key components](/en/agentic/agent-studio#genies-key-components):

- **AI model and job description** combine to form the brain and instructions of the genie. These components use LLMs to interpret requests, analyze context, make decisions, generate responses, and define your genie's behavior, persona, and constraints. Genies use Anthropic Claude by default. You can switch your LLM to OpenAI GPT or your own LLM connection.
- **Chat interface** provides the user interface where users can converse with the genie. You can use the Slack, Microsoft Teams, or Workato GO chat interface to trigger a conversation with your genie.
- **Knowledge base** stores company-specific information, conversation history, and metadata.
- **Skills** enable interaction with various applications and systems.

### Setup and access

Who can access Agent Studio and what are the prerequisites?

[Genies](/en/agentic/agent-studio) are an Agentic feature available to customers on specific pricing plans. **Genies are available in the US, EU, AU, SG, and JP data centers.** Genie models are hosted in the US, EU, and APAC regions and respect data residency requirements where possible.

You must ensure that genies are enabled in your account before using this feature. Contact your Customer Success representative to enable genies if you don't see the genies option in your workspace or require additional information. Refer to your pricing plan and contract to learn more.

Can I enable Agent Studio for child workspaces independently?

No. Agent Studio becomes available to all child workspaces when it's enabled on an [AHQ parent workspace](/en/ahq-hq-workspace). You can't enable Agent Studio for specific child workspaces without enabling the parent first.

You can use [collaborator permissions](/en/user-accounts-and-teams/role-based-access/) to control which users can access Agent Studio in each workspace.

Where do I access and manage genies?

You can view and configure genies by going to **AI Hub > Agent Studio**. Refer to [Getting started with genies](/en/agentic/agent-studio/genies-configuration#genies-configuration) for more information.

What LLM models does Agent Studio support?

Agent Studio supports [three LLM options for genies](/en/agentic/agent-studio/ai-model/ai-model):

- **Anthropic Claude** (default)
- **OpenAI GPT**
- **Use your own LLM connection** (BYOLLM)

Note that the AI model can only be changed after you stop your genie.

What chat interfaces can be used with genies?

The following options are available for the genie [chat interface](/en/agentic/agent-studio/chat-interface/chat-interface):

- Slack
- Microsoft Teams
- Workato GO
- Custom interface

Only custom interfaces can use [Headless API](/en/agentic/agent-studio/chat-interface/headless-api). You can't change the chat interface after a genie is created.

What file and image types can genies handle?

Genies support [file and image uploads](/en/agentic/agent-studio/upload-files-and-images) up to 25MB.

Common document file types are supported, including `.pdf`,`.doc` and `.csv`. Refer to [Files](/en/agentic/agent-studio/upload-files-and-images#files) for a complete list of supported file types.

Common image formats are supported, including `.jpg` and `.png`. Video files aren't supported. Refer to [Images](/en/agentic/agent-studio/upload-files-and-images#images) for a complete list of supported image formats.

How do I create a genie?

Refer to [Create your first genie](/en/agentic/agent-studio/create-a-genie) for detailed instructions.

What are the required components to run a genie?

Configure the following components to get your genie working:

- **[Job description](/en/agentic/agent-studio/ai-model/ai-model#job-description)**: Define your genie's role and goals.
- **[Chat interface](/en/agentic/agent-studio/chat-interface/chat-interface)**: Choose where users interact with the genie. Options are Slack, Microsoft Teams, or Workato GO.
- **[AI model](/en/agentic/agent-studio/ai-model/ai-model)**: Select the LLM that powers the genie. Options are Anthropic Claude, OpenAI GPT, or your own LLM connection.
- **[Knowledge base](/en/agentic/agent-studio/knowledge-bases/knowledge-bases)**: Configure knowledge sources for your genie.
- **[Skills](/en/agentic/skills)**: Enable your genie to take actions.

Refer to [Create your first genie](/en/agentic/agent-studio/create-a-genie) for a step-by-step walkthrough of creating all components together.

What metrics can I track for my genies?

The genie [Overview page](/en/agentic/agent-studio/genie-overview-page) tracks:

- **Total Conversations**: Distinct conversations initiated each day
- **Total End-User Messages**: Message volume to gauge engagement
- **Unique Users**: Distinct users for measuring adoption
- **Response Time**: Average, median, and 90th percentile response times
- **Conversation Volume**: Conversations over time
- **Skills Usage Heat Map**: Skill execution frequency and success rates

You can filter metrics by time range.

**Note**: Genies using Workato GO can also track custom business KPIs. Refer to the [Action Board](/en/agentic/faqs#action-board) section for more information.

### Knowledge bases

What is a knowledge base?

A [knowledge base](/en/agentic/agent-studio/knowledge-bases/knowledge-bases) serves as the genie's memory and provides the following capabilities:

- Stores any data and information that is crucial as a contextual reference for the genie to perform its role.
- Can be updated in real-time to ensure the genie has the most current information.
- Can access metadata to filter by attributes such as created date, source, or knowledge base ID.

How do I create a knowledge base?

Complete the following steps to [create a knowledge base](/en/agentic/agent-studio/knowledge-bases/knowledge-bases#getting-started-with-knowledge-bases):

1. Go to **AI Hub > Agent Studio** and create or edit a genie.
   
2. Add a knowledge base in the **Knowledge bases** section.
   
3. Choose your data source (Knowledge recipes or Workato GO data sources).
   

How do I add a knowledge base to a genie?

Complete the following steps to [add a knowledge base to a genie](/en/agentic/agent-studio/create-a-genie#add-knowledge-to-a-genie):

1. Go to **AI Hub > Agent Studio** and select your genie.
   
2. Locate the **Knowledge bases** section and click **\+ Add**.
   
3. Search for and select the knowledge base you plan to add.
   

Can a knowledge base be shared across multiple genies?

Yes. [Knowledge bases](/en/agentic/agent-studio/knowledge-bases/knowledge-bases) can be shared across multiple genies, even when genies are in different projects. This allows you to reuse the same knowledge base across different genies without duplication.

What file formats are supported when ingesting documents through knowledge recipes?

The following file formats are supported when using the **Store document in a knowledge base** action in [knowledge recipes](/en/agentic/agent-studio/knowledge-bases/knowledge-base-recipes):

- PDF (.pdf)
- Microsoft Word (.docx)
- Microsoft Excel (.xlsx)
- Microsoft PowerPoint (.pptx)

When should I use a knowledge base versus a database?

Use **knowledge bases** for semantic search over unstructured content, such as policies, guides, or descriptions. Use **databases** (accessed through skills) for exact lookups, counts, and filtered queries over structured data.

Refer to [Knowledge bases and databases](/en/agentic/agent-studio/knowledge-bases/knowledge-bases-and-databases) for more information.

Why isn't my genie finding information in structured data files?

Knowledge bases use semantic search, which struggles with structured formats like JSON or CSV. Raw structured data creates poor search results because semantic search can't effectively parse key-value pairs and repetitive field names.

**Solution**: Transform structured data into readable prose before adding it to knowledge bases. For example, convert:

- Raw: `{"ticket_id": "12345", "status": "open"}`
- Prose: "Support Ticket #12345 for Acme Corp - Login timeout issue (Status: Open)"

**When to use knowledge bases vs. databases**:

- Use knowledge bases for semantic search, such as finding similar issues or discovering patterns.
- Use databases accessed through skills for structured queries, such as counting, filtering, or exact lookups.

Refer to [Prepare JSON and API application data](/en/agentic/agent-studio/knowledge-bases/knowledge-base-configuration#prepare-json-and-api-application-data) for format examples.

Why does my genie return incomplete results for counting or listing questions?

Knowledge bases are designed for semantic search, not comprehensive queries. Each query returns only the 10 most relevant documents. This means that when you ask `how many invoices are overdue?`, your genie sees only 10 matches even if hundreds exist.

**Solution**: Use databases accessed through skills for counting, aggregations, or comprehensive lists. Databases query all matching records and return exact counts.

Refer to [Knowledge bases versus databases](/en/agentic/agent-studio/knowledge-bases/knowledge-bases-and-databases) for guidance on when to use each option.

Why isn't my genie finding information in my documents?

Knowledge bases split documents into 8,000-character chunks with no overlap. This means your genie may not find information if a chunk boundary splits mid-concept, or if key content is buried deep in a document.

**Quick fixes**:

- **Structure documents with headings** so chunks break at natural divisions rather than mid-paragraph.
- **Front-load important information** in the first 2,000 characters of documents.
- **Keep related concepts together** within 8,000-character sections.

Refer to [Knowledge base document preparation](/en/agentic/agent-studio/knowledge-bases/knowledge-base-configuration#knowledge-base-document-preparation) for more information.

### Security and authentication

What security features are available in Agent Studio?

Agent Studio provides several security controls:

**Access control**:

- Use [end-user groups](/en/workato-identity/user-groups) to control who can use specific genies.
- Configure [Verified User Access](/en/agentic/agent-studio/verified-user-access) (VUA) so skills execute with individual user permissions.

**Auditing**:

- Genie logs track skill executions and user interactions.
- VUA-enabled skills show which user performed each action in audit trails.

**Governance**:

- Genies can only execute skills you explicitly add to them.
- Skills respect connected app permissions and access controls.

What is Verified User Access and when should I use it?

[Verified User Access (VUA)](/en/agentic/agent-studio/verified-user-access) allows skills to execute with each end user's own credentials, rather than the recipe builder's credentials. End users authenticate once when first using a VUA-enabled skill and can manage their connections using the `!list_connections` keyword in chat.

**Connection types**:

Skills support two approaches:

**End user's connection (individual credentials with VUA)**:

- Actions run with each end user's identity and permissions
- Provides user-level audit trails
- Respects individual access rights in connected apps
- Requires OAuth 2.0 authorization code grant connections

**This recipe's connection (the builder's credentials)**:

- Actions run with the recipe builder's connection
- Works like standard Workato recipes

**When to use VUA**: Use individual credentials when you need user-level auditing, permission enforcement, or want to eliminate security risks of shared credentials. Use the builder's credentials when individual user permissions aren't required.

Refer to [Add verified user access to skills](/en/agentic/agent-studio/verified-user-access#add-verified-user-access-to-skill-recipes).

### Advanced features

What are app events and when should I use them?

[App events](/en/agentic/agent-studio/app-events) enable genies to act proactively by responding to triggers from external systems (like Salesforce or Zoom) instead of waiting for users to start conversations.

For example, when a NetSuite access request is approved, an IT Genie can automatically process next steps without user input.

App events automate complex tasks, surface relevant work at the right time, and give genies context earlier in the process.

What is agent orchestration?

[Agent orchestration](/en/agentic/agent-studio/agent-orchestration) enables genies to work autonomously within recipes. Recipes can assign tasks to genies without user input, and genies can delegate subtasks to other genies.

When a recipe uses the **Assign task to genie** action, the recipe job pauses while the genie processes the task autonomously, then resumes when the genie returns its response. This enables complex multi-agent workflows like compliance audits where one genie delegates evidence collection to another specialized genie.

What are the limitations of agent orchestration?

Agent orchestration has the following limitations:

- Genies using [verified user access](/en/agentic/agent-studio/verified-user-access) skills can't be used with the **Assign task to genie** action.
- Genies requiring [Business approvals](/en/agentic/agent-studio/business-approvals) can't process autonomous tasks.

Can skills, knowledge bases, and genies be used across multiple projects?

Yes. You can share and use skills, knowledge bases, and genies across multiple projects.

- **Skills**: You can add a skill from one project to genies in other projects. This lets teams reuse skills without duplicating recipes.
- **Knowledge bases**: You can assign a knowledge base from one project to genies in other projects. Recipes in any project can also store knowledge to a knowledge base and send app events to a genie regardless of which project they belong to.
- **Genies**: You can assign tasks to genies from recipes in other projects. Genies can also delegate subtasks to genies in other projects using [agent orchestration](/en/agentic/agent-studio/agent-orchestration).

Skills, knowledge bases, and genies can also be moved between projects freely without losing their configuration or connections.

### Troubleshooting

Why can't users access or interact with my genie?

Verify the following if users can't access your genie or the genie isn't responding:

- **The genie is started**: Check status in **AI Hub > Agent Studio**.
- **End user access is configured**: Add user groups. Go to **AI Hub > Agent Studio**, select the genie, and go to **End user access**.
- **Workato Identity accounts are activated**: Users should receive an email invitation.
- **The correct user group is assigned** to the genie.
- **Genie is properly connected to the chat interface**.

This applies to genies in Slack, Microsoft Teams, and Workato GO.

Refer to [Create a user group](/en/workato-identity/user-groups#create-a-user-group) for step-by-step instructions.

## Skills

### Overview

What are skills?

[Skills](/en/agentic/skills) are tools that let genies and MCP clients take actions in your business systems. A skill can query data, create records, send messages, update tickets, or perform any action your Workato recipes can do. Refer to the [Workato Skill connector](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector) for the connector that powers skills.

Can skills be shared across multiple genies?

Yes. You can share [skills](/en/agentic/skills) across multiple genies, even when genies are in different projects. Sharing lets you reuse skills across different genies without duplication.

Can I publish skills to the community library?

Yes. You can share [skills](/en/agentic/skills) in the [community library](/en/community-library#browse-assets).

### Workato Skill connector

Will my existing skills break?

No. Existing skills built on the [Workato Genie connector](/en/agentic/agent-studio/connectors/workato-genie-connector/workato-genie-connector) continue to function and remain available for assignment to genies.

The Workato Genie connector **Start workflow** trigger and **Return response** action are deprecated. They continue to work, but they don't receive new enhancements.

Do I have to migrate?

No. Migration is optional and at your own pace. New skills automatically use the [Workato Skill connector](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector) regardless of where you create them. Refer to [Migrate an existing skill](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector#migrate-an-existing-skill) for the steps.

What happens when I create a new skill?

New skills automatically use the [Workato Skill connector](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector) regardless of where you create them.

Will pre-built MCP servers I've already added change?

No. Existing pre-built MCP servers are unchanged. Newly added pre-built MCP servers will use the [Workato Skill connector](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector).

Can I use skills if I'm an MCP-only customer?

Yes. Customers on Business MCP and Enterprise MCP plans can create and use skills without an Agent Studio license.

Can I assign skills built on the Workato Skill connector to a genie?

Yes. Skills built on the [Workato Skill connector](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector) are assignable to genies, just like skills built on the [Workato Genie connector](/en/agentic/agent-studio/connectors/workato-genie-connector/workato-genie-connector). The genie builder lists both skill types.

Can I change the trigger of a skill after creation?

Yes. Workato sets the **Start workflow** trigger as the default when you create a skill. However, after you configure the trigger, you can replace it with a different trigger to run the recipe from an external event instead of an agent invocation. This differs from skills built on the [Workato Genie connector](/en/agentic/agent-studio/connectors/workato-genie-connector/workato-genie-connector), where the trigger was fixed.

Replacing the **Start workflow** trigger permanently removes the skill from any genies and MCP servers it was assigned to, and you can't undo this action. The recipe editor prompts you for confirmation before you make this change. The fields defined in the original trigger's result schema remain available in the **Return response** action.

What's the maximum response size from a skill?

The **Return response** action has a maximum response size of 250 KB. You can pass larger results as a streamable datapill to work around this limitation. Refer to [Stream large results](/en/agentic/agent-studio/connectors/workato-skill-connector/return-response#streaming) for more information.

Can a skill return binary file content?

No. Result fields don't support binary file content. To work around this limitation, upload the file earlier in the recipe to a file storage location your agent can access, such as Workato file storage, Amazon S3, or Google Drive. Then return the file URL or ID as a string field. The agent retrieves the file using that reference.

Does the Developer API for skills still work?

Yes. The Developer API supports skills built on either the [Workato Skill connector](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector) or the [Workato Genie connector](/en/agentic/agent-studio/connectors/workato-genie-connector/workato-genie-connector). Refer to [Skills](/en/workato-api/agent-studio#skills) in the Workato API reference for endpoint details.

### Troubleshooting

Why is my skill only returning one record instead of the full dataset?

The **Return response** action can return one record when you use **Text mode** instead of **Formula mode**, or when you select individual field datapills instead of the Records datapill. Text mode returns only the last record from a collection.

This applies to both the [Workato Skill connector](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector) **Return response** action and the legacy Workato Genie connector **Return response to Genie** action.

Complete the following steps to resolve this issue:

1. Open your skill and locate the **Return response** action.
   
2. Switch to **Formula mode**.
   
3. Select the Records list datapill, not individual field datapills.
   
4. Test to verify all records return.
   

Refer to [Text versus formula mode](/en/formulas/formula-mode#text-vs-formula-mode) for more information.

Why does my genie make mistakes with simple math calculations?

LLMs generate responses by predicting tokens instead of performing mathematical operations. This can cause errors in precise arithmetic, especially multi-step calculations and financial computations.

**Solution**: Give your genie access to a Python code execution skill that performs calculations accurately. The skill intercepts calculation requests and returns precise results.

**When this is critical**:

- Financial calculations (expense reports, budgets, invoices)
- Multi-step arithmetic (totals, aggregations, percentages)
- Any scenario requiring precise numerical results

Refer to [Troubleshoot arithmetic errors](/en/agentic/agent-studio/troubleshooting/troubleshooting#arithmetic-errors) for implementation steps and a pre-built skill template.

## Workato GO

### Overview

What is Workato GO?

[Workato GO](/en/agentic/workato-go) is an end-user interface that unifies AI-driven workflows, knowledge searches, and transactional interactions within a single, cohesive interface. It eliminates the need to switch between disconnected tools, search systems, and workflows.

**Key capabilities**:

- **Knowledge searches**: Combines public resources and multiple third-party applications to find answers across internal data sources like Google Drive, Slack, Confluence, Salesforce, and more.
- **Integrated chat**: Users can interact with agents and Enterprise data through a single prompt-driven interface.
- **Context-aware routing**: Determines whether a query is handled better by a genie, a search result, or both.
- **Simplified task flow**: Forms, approvals, and user confirmations are built into the interface to avoid switching between apps.

What types of knowledge can I search with Workato GO?

Workato GO provides two [knowledge sources](/en/agentic/workato-go/search):

- **World knowledge**: Search across publicly available information
- **Company knowledge**: Search across your company's third-party apps and internal documentation

What data sources does Workato GO support?

Workato GO supports a broad range of [data sources](/en/agentic/workato-go/data-sources) out-of-the-box, including Confluence, Salesforce, Slack, Google Drive, Jira, Gmail, Gong, and more. You can also add custom web crawler data sources to index internal documentation sites or public web pages.

### Setup and configuration

How do I configure a subdomain for Workato GO?

Complete the following steps to [configure your subdomain](/en/agentic/workato-go/configuration#configure-your-subdomain):

1. Go to **Manage > Workato GO admin > Subdomain**.
   
2. Enter your subdomain. For example, `acme-enhanced` creates `https://acme-enhanced.workato.ai`.
   
3. Click **Save**.
   

Your subdomain must be 3-65 characters. A unique, randomly generated subdomain is provided by default if you don't customize it.

Can I customize the branding in Workato GO?

Yes, you can [customize the company name and logo](/en/agentic/workato-go/configuration#configure-your-branding) using organization properties:

1. Go to **Admin > Advanced** in Workato GO.
   
2. Click **Add Organization Property**.
   
3. Set the property:
   
   - **Company name**: Use `ui.company_name` with your company name as the value
   - **Logo**: Use `ui.branding_logo` with your logo URL as the value

**Logo requirements**: Public URL, transparent .png or .svg, 210x40px dimensions, under 200 KB.

How do I add administrators to Workato GO?

Complete the following steps to [add administrators](/en/agentic/workato-go/admins-user-groups) to Workato GO:

1. Go to **Manage > Workato GO admin > End user access**.
   
2. Select users from the **End users** drop-down menu.
   
3. Click **Save**.
   

Administrators can manage data sources and view the activity log.

How do I change the theme in Workato GO?

Workato GO supports three themes: Light theme, Dark theme, and Sync with device, which matches your operating system settings.

You can change your theme by clicking your profile icon in the side navigation bar to open **Preferences**, then selecting your preferred theme.

Refer to [Choose a theme](/en/agentic/workato-go/preference-settings#choose-a-theme) for more information.

### Data sources

What are data sources?

[Data sources](/en/agentic/workato-go/data-sources) enable Workato GO to connect to your business systems, such as Jira, Confluence, Salesforce, and Google Drive, for enterprise search and AI workflows. This ensures search results reflect your actual business context and genies can retrieve current data to complete tasks.

How do I add a data source to Workato GO?

Each data source has specific configuration requirements. You must have administrator privileges in Workato GO to add data sources.

Refer to the connector-specific documentation for setup instructions:

- [Confluence](/en/agentic/workato-go/data-sources/confluence)
- [Gmail](/en/agentic/workato-go/data-sources/gmail)
- [Gong](/en/agentic/workato-go/data-sources/gong)
- [Google Calendar](/en/agentic/workato-go/data-sources/google-calendar)
- [Google Drive](/en/agentic/workato-go/data-sources/google-drive)
- [Highspot](/en/agentic/workato-go/data-sources/highspot)
- [Jira](/en/agentic/workato-go/data-sources/jira)
- [Okta](/en/agentic/workato-go/data-sources/okta)
- [Salesforce](/en/agentic/workato-go/data-sources/salesforce)
- [Slack](/en/agentic/workato-go/data-sources/slack)
- [Zendesk](/en/agentic/workato-go/data-sources/zendesk)

**Custom web pages**: You can also add custom web crawler data sources to index internal documentation sites or public web pages. Refer to [Add a web crawler data source](/en/agentic/workato-go/data-sources#add-a-custom-data-source).

Can I limit which Google Drive files are indexed by Workato GO?

Yes, you can [limit the Google Drive crawler scope](/en/agentic/workato-go/data-sources/google-drive#limit-google-drive-crawler-scope) to specific users' files:

1. Go to **Admin > Advanced** in Workato GO.
   
2. Click **Add Organization Property**.
   
3. Set `google_drive.user_allowlist` as the name and a comma-separated list of email addresses as the value.
   

This enables you to limit indexing to a pilot group, specific departments, or restrict access to sensitive content.

How does Workato GO handle permissions when ingesting data?

[Workato GO](/en/agentic/workato-go) respects native permissions from source systems:

- Documents private to specific users won't appear in searches for other users
- Folder-level security permissions are maintained (for example, Google Drive)
- You can restrict which users are crawled/indexed
- Permission-aware crawling ensures users only see content they have access to in the source system

### Action Board

What is Action Board?

[Action Board](/en/agentic/agent-studio/action-board) displays customizable dashboards in [Workato GO](/en/agentic/workato-go) that visualize KPI metrics configured in Agent Studio. Action Board displays:

- **Real-time KPI metrics** for each genie using customizable thumbnails for charts, tables, or stacked metrics.
- **Open action items** in the right-side panel, including business events directed to you and approvals assigned to you.
- **Genie widgets** with defined roles and job descriptions that you can engage with conversationally.

**Important**: Action Board and the KPI tab are only available for genies that use Workato GO as the chat interface. Action Board doesn't support genies using Slack or Microsoft Teams.

What are the prerequisites for using Action Board?

To use Action Board, you must:

- Have a genie configured with **Workato GO** as the chat interface.
- Create at least one KPI for your genie.
- Configure at least one Action Board thumbnail to display metrics.
- Have the appropriate user group permissions to view Action Board thumbnails.

Learn more about [Action Board](/en/agentic/agent-studio/action-board).

How do KPIs work with Action Board?

KPIs (Key Performance Indicators) are quantifiable measurements of progress toward company goals. KPIs use [data tables](/en/data-tables) to store frequently used data that KPI skills reference.

The workflow is:

1. End user triggers a KPI skill, for example, `New lead`.
2. The skill writes to the configured data table.
3. Workato loads this information and combines it with configured tasks.
4. KPI reports are generated and displayed in Action Board thumbnails.

Action Board supports four thumbnail types:

- Card format (default)
- Metric & chart
- Stacked metrics
- Detailed table

Each action board is limited to five thumbnails.

Learn more about [creating KPIs](/en/agentic/agent-studio/action-board).

### Troubleshooting

What should I do if real-time search or chat stops working?

This is typically caused by blocked or terminated Server-Sent Events (SSE) connections. SSE is a network-level issue, not a browser-specific problem.

**Symptoms**:

- Chat messages aren't updating in real-time
- Connection appears to close immediately
- No continuous event stream received

**Diagnosis**: You need to test the connection directly from the affected machine using browser Developer Tools and a curl command to determine whether the network blocks the SSE connection.

**Resolution**: If the connection closes immediately or doesn't stream events, contact your IT department. They should:

- Add your data center-specific domain to the allowlist (for example, `api-prod.matrix.workato.com`)
- Allow SSE/streaming connections to this endpoint
- Ensure proxy settings permit long-lived HTTP connections
- Verify firewall rules don't terminate persistent connections

Refer to [Troubleshoot search and real-time chat issues](/en/agentic/workato-go/search#troubleshoot-search-and-real-time-chat-issues) for more information.

Why aren't my genies appearing in Workato GO?

Verify the following if genies aren't appearing in Workato GO after configuration:

- **The genie is started** (not just configured).
- **Workato GO is selected as the chat interface** when creating the genie.
- **[End user access is configured](/en/agentic/agent-studio/manage-users-and-access#user-group-genie-access)** with the correct user groups. Go to **AI Hub > Agent Studio**, select the genie, and go to **End user access**.
- **You've activated your [Workato Identity account](/en/workato-identity/account-management#set-up-your-workato-id)**. Check your email for the invitation and activate your end user access.
- **The genie is assigned to your user group**.

If genies still don't appear after completing setup, verify you're accessing the correct Workato GO URL for your account, not a demo or dev environment.

## MCP

### Overview

What is MCP?

[Model Context Protocol (MCP)](/en/mcp) is an open protocol that standardizes how AI models connect to external systems and data sources. MCP enables you to expose your Workato capabilities (API collections, API recipes, recipe functions, and skills) as tools that AI clients can use.

Key benefits of MCP include:

- **Connects AI to external resources**: Enables AI models to access external data and tools to improve versatility and capabilities
- **Standardizes interactions**: Provides a consistent way for AI models to communicate with different systems like Slack, Jira, or Google Drive
- **Reduces development**: MCP's standardization reduces the need for custom integrations for each new data source

What MCP capabilities does Workato provide?

Workato provides the following MCP capabilities:

- **[MCP servers](/en/mcp/mcp-servers)**: Enable you to provide Workato capabilities (API collections, recipe functions, API recipes, and skills) as tools to AI agents through remote, cloud-based MCP servers with unique, authenticated URLs.
- **[Verified User Access](/en/mcp/verified-user-access)**: Enables your MCP servers to use authenticated end-user credentials for external API calls instead of static tokens.
- **[Workato Developer API and Embedded API MCP](/en/mcp/developer-api-mcp)**: Enables AI-powered developer environments like Claude Desktop and Cursor to programmatically access your Workato workspace.

Which AI clients/LLMs are compatible with Workato MCP?

[Workato MCP](/en/mcp#getting-started) is compatible with:

- Claude (Anthropic)
- Cursor
- Windsurf
- ChatGPT
- Any MCP client that supports the Model Context Protocol standard

### Setup and access

Is MCP available in my region?

**[MCP](/en/mcp) is available in the US, EU, AU, SG, and JP data centers.**

Contact your Customer Success representative if you're interested in using MCP or require additional information. Refer to your pricing plan and contract to learn more.

How do I create an MCP server in Workato?

You can create an MCP server in the AI Hub by [starting with a prebuilt template](/en/mcp/prebuilt-mcps#install-a-prebuilt-mcp-server-in-workato) or [building your own from scratch](/en/mcp/mcp-servers#create-an-mcp-server). The setup steps vary depending on which approach you choose.

What prebuilt MCP server templates are available?

Workato provides prebuilt MCP server templates for common collaboration and productivity apps, such as [Slack](/en/mcp/prebuilt-mcps/slack-mcp-server), [Google Calendar](/en/mcp/prebuilt-mcps/google-calendar-mcp-server), and [Google Sheets](/en/mcp/prebuilt-mcps/google-sheets-mcp-server), project and development apps, such as [Jira](/en/mcp/prebuilt-mcps/jira-mcp-server) and [GitHub](/en/mcp/prebuilt-mcps/github-mcp-server), identity management apps, such as [Google Directory End User](/en/mcp/prebuilt-mcps/google-directory-end-user-mcp-server) and [Okta End User](/en/mcp/prebuilt-mcps/okta-end-user-mcp-server), and sales operations apps, such as [Gong](/en/mcp/prebuilt-mcps/gong-mcp-server).

Refer to the [Prebuilt MCP servers](/en/mcp/prebuilt-mcps/mcp-servers) page for a complete list of available templates.

What types of assets can I add as tools to an MCP server?

You can select one of two tool source types when creating an MCP server from scratch:

**API collection**

Expose an entire API collection as MCP tools. This includes standard API recipe collections and AI gateway collections (API proxy collections). API collections don't support Verified User Access.

**Project assets**

Select individual assets from a project folder to expose as MCP tools:

- Recipe functions
- API recipes
- Skills

With project assets, you can mix multiple asset types in the same MCP server. All assets must be in the same project folder.

Learn more about [MCP servers](/en/mcp/mcp-servers) and [Verified User Access](/en/mcp/verified-user-access).

How do I configure an AI client to use my MCP server?

Configuration steps vary by AI client:

- [ChatGPT](/en/mcp/remote-mcp-servers#chatgpt-mcp-configuration)
- [Claude Desktop](/en/mcp/remote-mcp-servers#claude-mcp-configuration)
- [Cursor](/en/mcp/remote-mcp-servers#cursor-mcp-configuration)
- [Microsoft Copilot](/en/mcp/remote-mcp-servers#microsoft-copilot-mcp-configuration)

What are the best practices for designing MCP tools?

Follow these key principles when [designing MCP tools](/en/mcp/mcp-server-tool-design):

**Tool design principles**:

- **Simple**: Each tool performs exactly one specific action or retrieval
- **Composable**: Tools act as building blocks that work together seamlessly
- **Predictable**: Tools behave consistently and return standard errors

**Data strategy**:

- Return only necessary fields to preserve context windows
- Use AI preprocessing to summarize large datasets before returning to the agent

**Developer experience**:

- Write clear tool names and detailed descriptions
- Include sample requests and responses in tool documentation
- Use consistent naming conventions across all tools
- Implement standard HTTP status codes (200, 400, 404, 500)

**Monitoring and refinement**:

- Test tools with real AI workflows
- Monitor usage patterns and refine based on which tools are used most frequently

### Authentication and access control

What authentication methods does MCP support?

MCP supports [two authentication methods](/en/mcp/mcp-authentication):

**Token-based authentication** (default):

- Simple authentication with minimal configuration
- Tokens generated automatically and managed in MCP server settings
- Assigned by default to new MCP servers

**OAuth 2.0 integration with Workato Identity**:

- Required for Verified User Access (VUA)
- Provides centralized user access management
- Enables user-level audit trails and identity-aware authorization

**Important**: Switching from token-based authentication to Workato Identity revokes the MCP token, requiring all clients to be reconfigured for OAuth 2.0 authentication.

What is Verified User Access and when should I use it?

[Verified User Access (VUA)](/en/mcp/verified-user-access) enables end users to authenticate with their own credentials when interacting with MCP tools, bringing enterprise-grade governance and user-level security to AI workflows.

**How it works**:

- End users authenticate once when first accessing the MCP server
- Credentials are securely stored and reused across tools
- All tool calls respect individual user permissions
- Each action executes with the user's own identity and access rights

**When to use VUA**:

- You need user-level audit trails for compliance
- Tools access sensitive data requiring individual permissions
- You want to eliminate shared credentials for security
- Your organization requires identity-aware authorization

**Requirements**:

- MCP server must use [Workato Identity (OAuth 2.0) authentication](/en/mcp/mcp-authentication#oauth2-authentication-with-workato-identity)
- MCP server must use project assets as the tool source. API collections aren't supported.
- Selected tools must be recipe functions or skills
- Connected applications must support OAuth 2.0 authorization code grant. API keys, basic auth, and other OAuth 2.0 grant types don't work with VUA.

How do I enable Verified User Access for my MCP server?

Complete the following steps to use [Verified User Access (VUA)](/en/mcp/verified-user-access) with your MCP server:

1. Configure your MCP server to use [Workato Identity authentication](/en/mcp/mcp-authentication#oauth2-authentication-with-workato-identity).
   
2. Create recipe functions or skills as your MCP tools.
   
3. Configure connections to use **end-user connections**.
   

This allows each user to interact with your MCP tools using their own credentials, ensuring actions are performed as the authenticated user rather than the builder's credentials.

### Limitations

Can I limit MCP server usage?

Yes. You can [configure MCP server quotas](/en/mcp/mcp-server-access-and-configuration#configure-mcp-server-limits) by going to your MCP server's **Settings > Limits** page:

- **Rate limits** (throttling): Control request speed to prevent traffic bursts with customizable time intervals. No rate limits are enforced by default. Requests are unlimited if left blank.
- **Usage limits** (cumulative): Limit total consumption over time with aggregate request quotas. No usage limits are enforced by default. Consumption is unlimited if left blank.
- **IP restrictions**: Configure IP allowlists and blocklists to control which IP addresses can access your server. Blocked IPs take precedence over allowed IPs.

When rate limits or usage quotas are exceeded, all requests are blocked until the quota interval passes or the quota resets.

How many tokens can I have active on an MCP server at once?

Up to 50.

What's the maximum size of the Allowed IPs and Blocked IPs lists?

Each list holds up to 500 entries. The same quota applies to the **Allowed IPs** and **Blocked IPs** lists independently.

How long can an MCP tool call run before it times out?

A tool call returns inline within 30 seconds. After that, the call detaches and continues in the background up to a total of 300 seconds. Requests that exceed the asynchronous timeout don't return a response to the MCP client. Set the asynchronous timeout in your recipe settings.

### Troubleshooting

Why can't I access my MCP server with Workato Identity?

MCP servers using Workato Identity (OAuth 2.0) authentication don't grant automatic access to any users. All users must be added to an end-user group to access MCP servers, including administrators.

Complete the following steps to grant access:

1. Create or select an end-user group in Workato Identity.
   
2. Add users to the group.
   
3. Add the group to your MCP server's **Settings > End user access** page.
   

You must have admin privileges to manage user groups. If using token-based authentication instead, you only need the MCP URL and token.

Refer to [MCP access methods user groups](/en/mcp/mcp-authentication#user-groups) for step-by-step instructions.

How can I track who is accessing my MCP server?

[MCP server logs](/en/mcp/mcp-server-access-and-configuration#view-mcp-server-logs) provide a unified usage and access overview for governance and tracking. Logs include:

- **User ID**: Who accessed the server
- **Request IP address**: Where the request came from
- **Creation timestamp**: When the access occurred
- **Which tools/APIs were called**: What actions were performed

You can access logs in the [Workato Logging Service](/en/features/logging-service). Go to **Tools > Logs**, then click the **Log type** filter, select **MCP server**, and click **Apply** to view only MCP server logs.

---
