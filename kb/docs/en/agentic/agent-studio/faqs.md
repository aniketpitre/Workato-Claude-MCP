---
url: 'https://docs.workato.com/en/agentic/agent-studio/faqs.md'
description: >-
  Find answers to common questions about Agent Studio, including genies,
  knowledge bases, skills, security, authentication, and troubleshooting.
---

# Agent Studio - FAQ

Get answers to frequently asked questions (FAQs) about Agent Studio, including genies, knowledge bases, skills, and security features.

## Overview

### What is Agent Studio?

View answer

[Agent Studio](/en/agentic/agent-studio) is where you build and configure AI agents (genies). These genies perform actions, call workflows, understand context, and execute pre-defined skills to achieve your defined goals.

### What are genies?

View answer

Genies are AI-powered agents built in Agent Studio that pursue goals you define, adapt to context, and act across apps and data systems.

Genies operate through the following [key components](/en/agentic/agent-studio#genies-key-components):

- **AI model and job description** combine to form the brain and instructions of the genie. These components use LLMs to interpret requests, analyze context, make decisions, generate responses, and define your genie's behavior, persona, and constraints. Genies use Anthropic Claude by default. You can switch your LLM to OpenAI GPT or your own LLM connection.
- **Chat interface** provides the user interface where users can converse with the genie. You can use the Slack, Microsoft Teams, or Workato GO chat interface to trigger a conversation with your genie.
- **Knowledge base** stores company-specific information, conversation history, and metadata.
- **Skills** enable interaction with various applications and systems.

## Setup and access

### Who can access Agent Studio and what are the prerequisites?

View answer

[Genies](/en/agentic/agent-studio) are an Agentic feature available to customers on specific pricing plans. **Genies are available in the US, EU, AU, SG, and JP data centers.** Genie models are hosted in the US, EU, and APAC regions and respect data residency requirements where possible.

You must ensure that genies are enabled in your account before using this feature. Contact your Customer Success representative to enable genies if you don't see the genies option in your workspace or require additional information. Refer to your pricing plan and contract to learn more.

### Can I enable Agent Studio for child workspaces independently?

View answer

No. Agent Studio becomes available to all child workspaces when it's enabled on an [AHQ parent workspace](/en/ahq-hq-workspace). You can't enable Agent Studio for specific child workspaces without enabling the parent first.

You can use [collaborator permissions](/en/user-accounts-and-teams/role-based-access/) to control which users can access Agent Studio in each workspace.

### Where do I access and manage genies?

View answer

You can view and configure genies by going to **AI Hub > Agent Studio**. Refer to [Getting started with genies](/en/agentic/agent-studio/genies-configuration#genies-configuration) for more information.

### What LLM models does Agent Studio support?

View answer

Agent Studio supports [three LLM options for genies](/en/agentic/agent-studio/ai-model/ai-model):

- **Anthropic Claude** (default)
- **OpenAI GPT**
- **Use your own LLM connection** (BYOLLM)

Note that the AI model can only be changed after you stop your genie.

### What chat interfaces can be used with genies?

View answer

The following options are available for the genie [chat interface](/en/agentic/agent-studio/chat-interface/chat-interface):

- Slack
- Microsoft Teams
- Workato GO
- Custom interface

Only custom interfaces can use [Headless API](/en/agentic/agent-studio/chat-interface/headless-api). You can't change the chat interface after a genie is created.

### What file and image types can genies handle?

View answer

Genies support [file and image uploads](/en/agentic/agent-studio/upload-files-and-images) up to 25MB.

Common document file types are supported, including `.pdf`,`.doc` and `.csv`. Refer to [Files](/en/agentic/agent-studio/upload-files-and-images#files) for a complete list of supported file types.

Common image formats are supported, including `.jpg` and `.png`. Video files aren't supported. Refer to [Images](/en/agentic/agent-studio/upload-files-and-images#images) for a complete list of supported image formats.

### How do I create a genie?

View answer

Refer to [Create your first genie](/en/agentic/agent-studio/create-a-genie) for detailed instructions.

### What are the required components to run a genie?

View answer

Configure the following components to get your genie working:

- **[Job description](/en/agentic/agent-studio/ai-model/ai-model#job-description)**: Define your genie's role and goals.
- **[Chat interface](/en/agentic/agent-studio/chat-interface/chat-interface)**: Choose where users interact with the genie. Options are Slack, Microsoft Teams, or Workato GO.
- **[AI model](/en/agentic/agent-studio/ai-model/ai-model)**: Select the LLM that powers the genie. Options are Anthropic Claude, OpenAI GPT, or your own LLM connection.
- **[Knowledge base](/en/agentic/agent-studio/knowledge-bases/knowledge-bases)**: Configure knowledge sources for your genie.
- **[Skills](/en/agentic/skills)**: Enable your genie to take actions.

Refer to [Create your first genie](/en/agentic/agent-studio/create-a-genie) for a step-by-step walkthrough of creating all components together.

### What metrics can I track for my genies?

View answer

The genie [Overview page](/en/agentic/agent-studio/genie-overview-page) tracks:

- **Total Conversations**: Distinct conversations initiated each day
- **Total End-User Messages**: Message volume to gauge engagement
- **Unique Users**: Distinct users for measuring adoption
- **Response Time**: Average, median, and 90th percentile response times
- **Conversation Volume**: Conversations over time
- **Skills Usage Heat Map**: Skill execution frequency and success rates

You can filter metrics by time range.

**Note**: Genies using Workato GO can also track custom business KPIs. Refer to the [Action Board](/en/agentic/faqs#action-board) section for more information.

## Knowledge bases

### What is a knowledge base?

View answer

A [knowledge base](/en/agentic/agent-studio/knowledge-bases/knowledge-bases) serves as the genie's memory and provides the following capabilities:

- Stores any data and information that is crucial as a contextual reference for the genie to perform its role.
- Can be updated in real-time to ensure the genie has the most current information.
- Can access metadata to filter by attributes such as created date, source, or knowledge base ID.

### How do I create a knowledge base?

View answer

Complete the following steps to [create a knowledge base](/en/agentic/agent-studio/knowledge-bases/knowledge-bases#getting-started-with-knowledge-bases):

1. Go to **AI Hub > Agent Studio** and create or edit a genie.
   
2. Add a knowledge base in the **Knowledge bases** section.
   
3. Choose your data source (Knowledge recipes or Workato GO data sources).
   

### How do I add a knowledge base to a genie?

View answer

Complete the following steps to [add a knowledge base to a genie](/en/agentic/agent-studio/create-a-genie#add-knowledge-to-a-genie):

1. Go to **AI Hub > Agent Studio** and select your genie.
   
2. Locate the **Knowledge bases** section and click **\+ Add**.
   
3. Search for and select the knowledge base you plan to add.
   

### Can a knowledge base be shared across multiple genies?

View answer

Yes. [Knowledge bases](/en/agentic/agent-studio/knowledge-bases/knowledge-bases) can be shared across multiple genies, even when genies are in different projects. This allows you to reuse the same knowledge base across different genies without duplication.

### What file formats are supported when ingesting documents through knowledge recipes?

View answer

The following file formats are supported when using the **Store document in a knowledge base** action in [knowledge recipes](/en/agentic/agent-studio/knowledge-bases/knowledge-base-recipes):

- PDF (.pdf)
- Microsoft Word (.docx)
- Microsoft Excel (.xlsx)
- Microsoft PowerPoint (.pptx)

### When should I use a knowledge base versus a database?

View answer

Use **knowledge bases** for semantic search over unstructured content, such as policies, guides, or descriptions. Use **databases** (accessed through skills) for exact lookups, counts, and filtered queries over structured data.

Refer to [Knowledge bases and databases](/en/agentic/agent-studio/knowledge-bases/knowledge-bases-and-databases) for more information.

### Why isn't my genie finding information in structured data files?

View answer

Knowledge bases use semantic search, which struggles with structured formats like JSON or CSV. Raw structured data creates poor search results because semantic search can't effectively parse key-value pairs and repetitive field names.

**Solution**: Transform structured data into readable prose before adding it to knowledge bases. For example, convert:

- Raw: `{"ticket_id": "12345", "status": "open"}`
- Prose: "Support Ticket #12345 for Acme Corp - Login timeout issue (Status: Open)"

**When to use knowledge bases vs. databases**:

- Use knowledge bases for semantic search, such as finding similar issues or discovering patterns.
- Use databases accessed through skills for structured queries, such as counting, filtering, or exact lookups.

Refer to [Prepare JSON and API application data](/en/agentic/agent-studio/knowledge-bases/knowledge-base-configuration#prepare-json-and-api-application-data) for format examples.

### Why does my genie return incomplete results for counting or listing questions?

View answer

Knowledge bases are designed for semantic search, not comprehensive queries. Each query returns only the 10 most relevant documents. This means that when you ask `how many invoices are overdue?`, your genie sees only 10 matches even if hundreds exist.

**Solution**: Use databases accessed through skills for counting, aggregations, or comprehensive lists. Databases query all matching records and return exact counts.

Refer to [Knowledge bases versus databases](/en/agentic/agent-studio/knowledge-bases/knowledge-bases-and-databases) for guidance on when to use each option.

### Why isn't my genie finding information in my documents?

View answer

Knowledge bases split documents into 8,000-character chunks with no overlap. This means your genie may not find information if a chunk boundary splits mid-concept, or if key content is buried deep in a document.

**Quick fixes**:

- **Structure documents with headings** so chunks break at natural divisions rather than mid-paragraph.
- **Front-load important information** in the first 2,000 characters of documents.
- **Keep related concepts together** within 8,000-character sections.

Refer to [Knowledge base document preparation](/en/agentic/agent-studio/knowledge-bases/knowledge-base-configuration#knowledge-base-document-preparation) for more information.

## Security and authentication

### What security features are available in Agent Studio?

View answer

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

### What is Verified User Access and when should I use it?

View answer

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

## Advanced features

### What are app events and when should I use them?

View answer

[App events](/en/agentic/agent-studio/app-events) enable genies to act proactively by responding to triggers from external systems (like Salesforce or Zoom) instead of waiting for users to start conversations.

For example, when a NetSuite access request is approved, an IT Genie can automatically process next steps without user input.

App events automate complex tasks, surface relevant work at the right time, and give genies context earlier in the process.

### What is agent orchestration?

View answer

[Agent orchestration](/en/agentic/agent-studio/agent-orchestration) enables genies to work autonomously within recipes. Recipes can assign tasks to genies without user input, and genies can delegate subtasks to other genies.

When a recipe uses the **Assign task to genie** action, the recipe job pauses while the genie processes the task autonomously, then resumes when the genie returns its response. This enables complex multi-agent workflows like compliance audits where one genie delegates evidence collection to another specialized genie.

### What are the limitations of agent orchestration?

View answer

Agent orchestration has the following limitations:

- Genies using [verified user access](/en/agentic/agent-studio/verified-user-access) skills can't be used with the **Assign task to genie** action.
- Genies requiring [Business approvals](/en/agentic/agent-studio/business-approvals) can't process autonomous tasks.

### Can skills, knowledge bases, and genies be used across multiple projects?

View answer

Yes. You can share and use skills, knowledge bases, and genies across multiple projects.

- **Skills**: You can add a skill from one project to genies in other projects. This lets teams reuse skills without duplicating recipes.
- **Knowledge bases**: You can assign a knowledge base from one project to genies in other projects. Recipes in any project can also store knowledge to a knowledge base and send app events to a genie regardless of which project they belong to.
- **Genies**: You can assign tasks to genies from recipes in other projects. Genies can also delegate subtasks to genies in other projects using [agent orchestration](/en/agentic/agent-studio/agent-orchestration).

Skills, knowledge bases, and genies can also be moved between projects freely without losing their configuration or connections.

## Troubleshooting

### Why can't users access or interact with my genie?

View answer

Verify the following if users can't access your genie or the genie isn't responding:

- **The genie is started**: Check status in **AI Hub > Agent Studio**.
- **End user access is configured**: Add user groups. Go to **AI Hub > Agent Studio**, select the genie, and go to **End user access**.
- **Workato Identity accounts are activated**: Users should receive an email invitation.
- **The correct user group is assigned** to the genie.
- **Genie is properly connected to the chat interface**.

This applies to genies in Slack, Microsoft Teams, and Workato GO.

Refer to [Create a user group](/en/workato-identity/user-groups#create-a-user-group) for step-by-step instructions.

---
