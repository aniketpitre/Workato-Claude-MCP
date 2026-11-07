---
url: 'https://docs.workato.com/en/agentic/agent-studio/guardrails/guardrails.md'
description: >-
  Configure security and safety controls for your genies, including prompt
  attack detection, harmful content filtering, and PII handling.
---

# Guardrails

Guardrails are built-in security and safety controls that ensure your genies behave reliably and appropriately. Guardrails are configured on your genie's **Build** page. The panel is organized into the following sections:

- **Content safety**: Set the sensitivity of the read-only **Prompt Attack** and **Harmful Content** guardrails. This protects against spam, phishing, prompt attacks, and harmful content.
- **Data Protection**: Toggle PII detection on or off, configure handling modes per entity type, and define custom regex patterns.
- **Topic & word filters**: Toggle the profanity filter and custom word filter on or off, and manage your word and phrase list. You can use **Denied Topics** to add, edit, and remove denied topics.

You can configure content safety guardrails to low, medium, or high sensitivity. Sensitivity settings can't be applied to PII detection or topic and word filters.

![Block sensitivity levels](/assets/block-sensitivity.W4R3GDN0.png)_Block sensitivity levels_

> **BETA FEATURE**
> 
> This feature is in beta. Workato may update its functionality or change its availability without notice during beta. Reach out to your account manager for more information about this feature.

## Content safety

Content safety guardrails are automatically active for all genies and can't be disabled. Content safety consist of:

- **Prompt Attack** detection blocks attempts to manipulate genie behavior or extract system configuration.
  
- **Harmful Content** filtering prevents dangerous material from being processed or generated.
  

### Prompt Attack

**Prompt Attack** detection blocks attempts to manipulate genie behavior, bypass safety guidelines, or extract system configuration. This includes:

- **Prompt injection**: Crafted inputs designed to override genie instructions, such as messages beginning with `Ignore all previous instructions`.
- **Jailbreak attempts**: Role-play scenarios or multi-turn manipulation designed to bypass safety guidelines.
- **Prompt leakage**: Requests attempting to surface the genie's job description or system prompt.

The genie run stops immediately when a prompt attack is detected, and you receive the following message: `I'm not able to process this request. Please try rephrasing your question.`

### Harmful Content

**Harmful Content** filtering prevents dangerous material from being processed or generated. Detection applies to both user input and genie output across the following categories:

| Category | Description | Examples |
| --- | --- | --- |
| Hate speech | Content that demeans people based on race, religion, gender, nationality, or other protected attributes. | Slurs or discriminatory statements. |
| Insults | Demeaning or derogatory language directed at individuals or groups, including bullying, shaming, or verbal aggression. | Personal attacks or bullying. |
| Sexual content | Explicit or suggestive sexual material. Use Low for genies where professional health or safety topics are expected in normal use. | Adult content or sexual solicitation. |
| Violence | Descriptions of physical harm, threats, or graphic content. This setting doesn't affect factual safety information, such as first aid or workplace hazard reporting. | Weapon instructions or graphic violence. |
| Misconduct | Content promoting fraud, criminal activity, unauthorized system access, or other harmful behaviors targeting individuals or organizations. | Drug instructions or fraud schemes. |

- **Harmful content detected in user input**: Users receive the following message: `Your message contains content that I'm not able to respond to. Please rephrase your request.`
- **Harmful content detected in genie output**: Users receive the following message: `I'm not able to provide a response to this request.`

## Optional guardrails

You can configure optional guardrails per genie in the **Build** page **Guardrails** panel. Optional guardrails are turned off by default.

### PII detection

PII detection identifies personally identifiable information in conversations and handles it according to the mode you configure. Detection applies to the following checkpoints:

- User input
- Tool input and output
- Genie output

The following high-risk entity types are on by default:

- Social Security numbers
- Credit card numbers
- Bank account numbers
- Passwords
- API keys

Lower-risk entity types are set to off by default. You can toggle detection on or off for the following lower-risk entity types:

- Email addresses
- Phone numbers
- Names
- Addresses

#### Handling modes

You can configure how detected PII is handled for each entity type:

| Mode | Description |
| --- | --- |
| Block | Refuses to pass PII to the LLM. The genie receives error context to generate a user-friendly refusal. |
| Redact | Permanently replaces PII with masked placeholders before passing to the LLM, for example `[SSN:***-**-6789]`. The genie output is also scanned and redacted before it's returned to the user. |
| Tokenize | Replaces PII with reversible tokens before passing to the LLM, for example `[EMAIL_TOKEN_1]`. Tokens are converted back to original values in the genie output before returning to the user. Token mappings are stored securely and aren't sent to the LLM. |
| Log Only | Detects and flags PII in the debug trace only. Content passes through unchanged. Useful for monitoring before enforcing a stricter mode. |

#### Tokenization behavior

Tokenization allows the genie to reason about content containing PII without exposing raw values. The following rules apply:

- The same PII value maps to the same token within a conversation to ensure references remain consistent.
- Token mappings are scoped to the conversation and aren't exposed in debug traces, logs, or API responses.
- Tool responses containing PII are tokenized before being sent to the LLM.
- Genie output and skill inputs that contain tokens are de-tokenized.
- Each nested genie maintains independent token mappings.

#### Custom regex patterns

You can define up to 10 custom regex patterns to detect organization-specific sensitive data, such as employee IDs. Each pattern requires a name and a valid regex string and supports the same handling modes as built-in entity types. Patterns are validated before saving.

When a PII block is triggered, the user receives: `Your message contains sensitive personal information. Please remove personal details and try again.`

### Profanity filter

The **profanity filter** uses a managed word list maintained by AWS Bedrock to block profane content in both user input and genie output. The genie run stops and the user receives the following message if the profanity filter is triggered: `Your message contains content that is not allowed.`

### Custom word filter

The custom word filter allows you to block specific words or phrases from conversations. Matching is case-insensitive and exact, not substring-based. You can add up to 100 words or phrases and configure whether the filter applies to user input, genie output, or both.

The genie run stops and the user receives the following message if the custom word filter is triggered: `Your message contains content that is not allowed.`

### Denied topics

Denied topics allow you to define subjects the genie shouldn't discuss. Detection uses semantic understanding rather than keyword matching to catch rephrased or indirect references to a denied topic. You can define up to 30 denied topics per genie.

Each topic requires a name and a natural language definition. You can also add up to five example queries per topic to improve detection accuracy.

| Topic name | Definition | Example blocked query |
| --- | --- | --- |
| Competitor products | Discussion of competitor products, pricing, or features | `How does this compare to ServiceNow?` |
| Legal advice | Providing specific legal recommendations | `Should I dispute this contract?` |
| Medical diagnosis | Providing specific medical diagnoses or treatment plans | `What medication should I take?` |

The genie run stops and users receive the following message when a denied topic is detected: `I'm not able to discuss this topic.`

## Debug traces

Every guardrail evaluation appears in the conversation debug trace under the step name **Input Guardrails** or **Output Guardrails**. Each entry shows the guardrail type, pass or fail status, rejection reason, and evaluation time.

Detected PII values aren't stored in plain text. Masked values appear in debug traces and conversation history in the following formats:

| PII type | Masked display |
| --- | --- |
| SSN | `[SSN:***-**-6789]` |
| Credit card | `[CARD:****-****-****-1111]` |
| Bank account | `[BANK_ACCT:*****8901]` |
| API key | `[API_KEY:sk-***]` |
| Email | `[EMAIL:j***@***.com]` |
| Phone | `[PHONE:***-4639]` |
| Name | `[NAME:J*** S***]` |
| Custom regex | `[CUSTOM_PII:***]` |

## Getting started with guardrails

You can add guardrails to any genie in Agent Studio. The steps in this section assume that you're signed in to Workato and have already created the genie where you plan to add guardrails.

Complete the following steps to add guardrails to your genie:

1. Go to the **Guardrails** field and click the cog (edit) icon to open the configuration page.
   
2. Go to **Guardrails** in the sidebar and click **Content safety**.
   
3. Configure your content safety guardrails.
   
   1. Review the **Prompt attack** setting and optionally set the sensitivity to low or medium. **Prompt attack** is set to high sensitivity by default.
      
   2. Go to the **Harmful content** section and optionally set the sensitivity to low or medium for the following categories:
      
      | Category | Description |
      | --- | --- |
      | Hate speech | Content that demeans people based on race, religion, gender, nationality, or other protected attributes. |
      | Insults | Demeaning or derogatory language directed at individuals or groups, including bullying, shaming, or verbal aggression. |
      | Sexual content | Explicit or suggestive sexual material. Use Low for genies where professional health or safety topics are expected in normal use. |
      | Violence | Descriptions of physical harm, threats, or graphic content. This setting doesn't affect factual safety information, such as first aid or workplace hazard reporting. |
      | Misconduct | Content promoting fraud, criminal activity, unauthorized system access, or other harmful behaviors targeting individuals or organizations. |
      
   3. Click **Save**.
      
   
4. Configure your data protection guardrails.
   
   1. Click **Data protection** in the sidebar.
      
   2. Click the **Detect PII** toggle to enable Personally Identifiable Information (PII) guardrails.
      
   3. Use the **PII types to detect** drop-down menu to select the PII types you plan to apply guardrails to.
      
   4. Optional. Expand the **Hide custom PII types** section and add custom regex patterns.
      
   5. Go to the **When PII is detected** section and select the method your genie should use to respond to PII data.
      
      **Refuse**
      
      The genie blocks messages containing PII and asks users to rephrase or use a secure channel instead. **Refuse** is selected by default.
      
      ![Refuse](/assets/refuse.CCmDK1J_.png)_Refuse_
      
      **Redact**
      
      The genie receives the message with the sensitive data redacted and asks users to rephrase or use a secure channel instead.
      
      ![Redact](/assets/redact.sM1aeoBj.png)_Redact_
      
      **Tokenize**
      
      PII is hidden from the LLM but passed to skills and restored in the genie's response. Nothing is stored.
      
      ![Tokenize](/assets/tokenize.C_NpBTQT.png)_Tokenize_
      
   6. Click **Save**.
      
   
5. Configure your topics and word filters guardrails.
   
   1. Click **Topics & word filters** in the sidebar.
      
   2. Click **\+ Add a topic** to define specific a topic the genie shouldn't discuss. Denied topics use semantic matching.
      
   3. Enter a name in the **Topic name** field.
      
   4. Optional. Enter a topic description in the **Description** field.
      
   5. Click **\+ Add a sample phrase** to provide example user inputs that help the genie recognize this topic. You can add a maximum of 5 sample phrases.
      
   6. Click **Save**.
      
   7. Go to the **Blocked words and phrases** section.
      
   8. Click the **Profanity filter** toggle to enable your genie to filter for profanity.
      
   9. Go to the **Custom blocked words** field and enter or phrases for your genie to block. Words or phrases must be comma separated and are case sensitive. For example: `Confidential, internal only, Private`
      
   10. Click **Save**.
       
   

## Test guardrails

You can test your guardrails in **Test** mode. Testing allows you to refine your guardrails to ensure that your genie responds appropriately before moving to production.

Complete the following steps to test your guardrails:

1. Click the mode toggle to switch from **Build** to **Test**.
   
2. Enter a phrase or question that aligns with a denied topic you configured.
   
   ![Denied topic guardrail](/assets/denied-topic-configuration.C96s8dFB.png)_Denied topic guardrail example_
   
3. Ensure that your genie declines to discuss the topic.
   
   ![Denied topic in Test mode](/assets/denied-topic-test.C9Sezwn6.png)_Denied topic in **Test** mode_
   
4. Optional. Return to **Guardrails > Topic & word filters > Denied topics** to refine your sample phrases or add additional sample phrases to improve your genie's responses.

---

---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/knowledge-bases/knowledge-bases.md
description: >-
  Learn how knowledge bases serve as a genie's memory, storing policies,
  documentation, and conversation history for grounded responses.
---

# Knowledge bases

Knowledge bases serve as the genie's memory. They support long-term memory, such as persistent reference content like policies, documentation, and product information, and short-term memory, such as conversation history that grounds responses within an active session.

Knowledge bases receive all data and associated metadata from returned documents. You can provide the knowledge base with relevant context on your company's policies or access to historical data that grounds the behavior of the genie. The genie's behavior is further tailored by information it gleans from the knowledge bases you provide it access to and your conversation history.

Knowledge bases provide the following capabilities:

- Stores and organizes company-specific information and conversation history
- Provides quick access to relevant data for informed decision-making
- Can be updated in real-time to ensure the genie has the most current information
- Helps maintain consistency in genie responses and actions across the organization
- Can access metadata to filter by attributes such as created date, source, or knowledge base ID

> **KNOWLEDGE BASE DESCRIPTION**
> 
> It's important to provide a detailed description of each knowledge base you create. Precise descriptions enable your genie to understand the scope and relevance of each knowledge base. This ensures that genie responses are as accurate and contextually grounded as possible.

## How knowledge bases work

Your genie searches a knowledge base using semantic similarity when a user asks the genie a question that requires reference knowledge. It finds the content fragments most relevant to the question and uses them to construct a response.

Watch a quick video guide: Reference a knowledge base

[Video](https://www.youtube.com/embed/HacDiWcie_0?rel=0&si=DGA_Ykr5G5MhwYgU)

This is different from a database query or a skill call. The genie isn't retrieving a specific record by ID. It's finding the most semantically similar content from everything that has been ingested.

The quality of retrieval depends on the quality of the ingested content. A knowledge base populated with well-prepared, logically chunked, context-rich documents retrieves accurately. Knowledge bases populated with raw exports, large unsplit files, or formatting-heavy PDFs retrieves fragments that are technically relevant but incomplete, or miss key information.

Getting a knowledge base right requires good decisions at every stage: what to include, how to prepare it, how to ingest it, and how to tell the genie when to search it.

Workato recommends performing thorough [document preparation](/en/agentic/agent-studio/knowledge-bases/knowledge-base-configuration#knowledge-base-document-preparation) before uploading content to your knowledge base. Refer to [document preparation best practices](/en/agentic/agent-studio/knowledge-bases/knowledge-base-configuration#document-preparation-best-practices) for more information.

## Knowledge base management

Knowledge base management gives you a centralized view to monitor and manage the content stored across your knowledge bases. You can search, view, organize, and remove documents, track storage footprints, and manage file uploads to ensure your genie has access to accurate, up-to-date information. Refer to [Knowledge base management](/en/agentic/agent-studio/knowledge-bases/knowledge-base-management) for more information.

## Getting started with knowledge bases

You should plan your knowledge base configuration before you start building. Use the following guidelines to help you plan your knowledge base:

- Identify the exact knowledge you plan to use.
- Determine which data source the knowledge is stored in.
- Select a knowledge ingestion option:
  - Knowledge recipes: Populate a knowledge base through Workato recipes to connect and extract data from Workato-supported apps.
  - [Workato GO](/en/agentic/workato-go) data sources: Add knowledge to your knowledge base from Workato GO. Use this option if you have plan to use the same data for both your genie and Workato GO.
- [Prepare your knowledge documents](/en/agentic/agent-studio/knowledge-bases/knowledge-base-configuration#knowledge-base-document-preparation) for ingestion.

Watch a quick video guide: Create a knowledge recipe in Agent Studio

[Video](https://www.youtube.com/embed/ajBzQFor_hc)

  

> **NEED AN EXAMPLE?**
> 
> Refer to the [Connect your knowledge base to Confluence](/en/getting-started/use-cases/agent-studio/knowledge-bases/knowledge-base-confluence-use-case) use case for a step-by-step guide on how to create and connect your knowledge base to Confluence with a knowledge recipe.

Refer to [Create your first genie](/en/agentic/agent-studio/create-a-genie) for complete steps on how to create a genie with a job description, AI model, chat interface, knowledge base, knowledge base recipe, and skills.

Complete the following steps to create a knowledge base:

1. Go to **Projects**.
   
2. Click **Create > Knowledge base** or press C+K.
   
3. Provide a name for your knowledge base in the **Knowledge base name** field.
   
   ![Create a knowledge base](/assets/add-knowledge-base.D7qlZXNz.png)_Create a knowledge base_
   
4. Use the **Location** drop-down menu to select a location for your knowledge base.
   
5. Optional. Enter a description for your knowledge base in the **Description** field. Genies use descriptions to understand the context and purpose of the knowledge base to determine when to use it.
   
6. Go to the **How will you add data?** section and select the data source you plan to use to sync the information in your knowledge base.
   
   **Uploads and recipes**
   
   **Uploads and recipes** is selected by default. Add knowledge by uploading files directly or syncing data from a [knowledge recipe](/en/agentic/agent-studio/create-a-genie#create-a-knowledge-recipe).
   
   ![Uploads and recipes](/assets/sync-knowledge-recipes.CSsrmDs3.png)_Uploads and recipes_
   
   **Choose from connected data sources**
   
   1. Click **Choose from connected data sources**.
      
      ![Click Choose from connected data sources](/assets/sync-workato-go-data-sources.DE5n9fkX.png)_Click **Choose from connected data sources**_
      
   2. Use the **Data sources** drop-down menu to select the data sources Workato GO uses with your genie.
      
   
7. Click **Start building**.
   

Your knowledge base is ready for a knowledge recipe. Refer to [Create a knowledge recipe](/en/agentic/agent-studio/create-a-genie#create-a-knowledge-recipe) to add a knowledge recipe that syncs and updates information from your applications to your knowledge base.

## More resources

- [Knowledge bases versus database](/en/agentic/agent-studio/knowledge-bases/knowledge-bases-and-databases)

---

---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/knowledge-bases/design-best-practices.md
description: >-
  Learn how to scope, describe, and structure a genie knowledge base for
  reliable retrieval across a single functional area.
---

# Knowledge base design best practices

We recommend scoping a knowledge base to a specific use or topic. Knowledge bases that contain too much data or mix IT policies with HR procedures and sales playbooks, produce poor retrieval results. A knowledge base with a vague description produces a genie that doesn't know when to search it.

This page provides guidance on what to include in your knowledge base, how to scope it, how to describe it, and how to structure the content for effective retrieval.

## Scope to a functional area

The most important scoping decision is how broadly to define the knowledge base's content boundary. Use one knowledge base per functional area per genie.

A knowledge base scoped to a functional area, such as IT helpdesk policies, HR leave procedures, or sales competitive intelligence, produces reliable retrieval because the semantic space of the content is coherent. The most semantically similar fragments are typically relevant to the question because all the content is about the same domain.

A knowledge base scoped to the whole company produces unreliable retrieval because the semantic space is too broad. An employee asking about parental leave eligibility may receive a fragment from the IT security policy because both documents use similar language about employee responsibilities and compliance requirements. The retrieval is semantically plausible but contextually wrong.

## Design decisions

Determine the answers to the following design questions before you build your knowledge base:

- **What content will this knowledge base contain?**: Name the specific source, such as the Confluence space, Google Drive folder, or policy document library. Be specific enough to enumerate it. The scope is too broad if you can't enumerate it.
  
- **Which ingestion path will you use?**: A small, stable content library, direct file upload is the recommended path to a working knowledge base for a first build. A knowledge recipe is more appropriate if you have larger or frequently changing content. Use Workato GO data sources for content with user-level access restrictions. Refer to [Two ingestion paths](/en/agentic/agent-studio/knowledge-bases/data-ingestion#two-ingestion-paths) for more information.
  
- **What description will you give the knowledge base?** Write the description before you open Agent Studio. The genie reads this description to decide when to search this knowledge base. Write it in the same format as a skill's **When to Use section**. The description should include what content is available, what questions it answers, when the genie should search it, and when it shouldn't.
  

## Examples of well-scoped knowledge bases

Each of the following examples has a coherent content domain, a clear intended use case, and a specific genie context.

| Name | Contents | Used by |
| --- | --- | --- |
| Confluence | IT policies, acceptable use policies, software request procedures, hardware support guides, and troubleshooting documentation | IT Genie for ticket deflection and policy Q&A |
| Confluence | HR leave policies, eligibility criteria, leave type definitions, accrual rules, and onboarding documentation | HR Assistant Genie for policy questions |
| Jira | Resolved Jira tickets with resolution notes and comments | IT Genie to find known issues and past resolutions for similar problems |
| Google Drive | Customer case studies and testimonials | Sales Genie for reference during account research and presentation preparation |
| Highspot - Sales Competitive Intelligence | Competitive battlecards, objection handling guides, and win/loss analysis | Sales Genie for competitive positioning questions |

## Anti-patterns to avoid

The most common knowledge base design mistake is creating a single knowledge base that contains IT policies, HR procedures, sales playbooks, finance guidelines, and legal documentation. This type of knowledge base design produces:

- **Retrieval noise across domains**: The genie retrieves fragments from the wrong domain.
- **Slower retrieval**: Searching a large, broad knowledge base takes longer than searching a small, focused knowledge base.
- **Harder maintenance**: Updates to any part of the content require careful attention to avoid contaminating other domains.
- **Ambiguous genie behavior**: The genie doesn't know which domain to search for which type of question when everything is in one place.

Build separate, focused knowledge bases. The incremental management overhead is worth the retrieval quality improvement.

## Write a meaningful knowledge base description

The knowledge base description is one of the most important fields you'll provide in your knowledge base.

The genie reads the knowledge base description when deciding which knowledge base to search to answer a question. A description that clearly communicates what the knowledge base contains and when to use it produces reliable knowledge base selection. A vague or missing description forces the genie to guess.

A well-written knowledge base description answers three questions:

- What content does this knowledge base contain?
- What types of questions can it answer?
- When should the genie search it?

**Recommended**

```plaintext
Contains HR leave policies, eligibility
criteria, leave type definitions, and
accrual rules for all employee categories.
Use this knowledge base when an employee
asks about leave policy, leave eligibility,
how a specific leave type works, or how
leave accrual is calculated.
```

**Not recommended**

```plaintext
HR documents
```

```plaintext
Knowledge Base 1
```

The good description tells the genie exactly what's here and when to use it. The bad descriptions give the genie no useful signal.

Write descriptions for every knowledge base you create. Treat the description as a skill prompt for the knowledge base. It's the **when to use me** instruction the genie reads when deciding whether this knowledge base is relevant to the current question.

## Split large knowledge bases

Consider splitting a knowledge base into smaller, more focused knowledge bases when it grows larger, either because the content domain is broad or because a large volume of documents has been ingested. There are two reasons to split a knowledge base:

- **Retrieval accuracy**: A smaller, more focused knowledge base produces more precise retrievals. The most semantically similar fragments may come from a different part of the domain than the question is about when the vector store searches a large knowledge base with thousands of document fragments. Smaller knowledge bases have fewer irrelevant fragments competing with the right fragments.
  
- **Token efficiency**: The fragments the genie retrieves from a knowledge base consume context window space. A large knowledge base may return several large fragments that together consume a significant portion of the context before the genie has composed a response. Smaller knowledge bases return more focused results that use context window space more efficiently.
  

Consider whether a knowledge base can be split into two or three more focused knowledge bases if the knowledge base contains more than a few hundred documents, or if retrieval quality is degrading for specific query types.

Update the job description to reference each knowledge base by name for the relevant use case categories when you split a knowledge base. The genie should know which of the split knowledge bases to search for which types of question.

## Reference knowledge bases by name in the job description

The job description tells the genie which knowledge base to search for each use case category when the genie is connected to multiple knowledge bases. This instruction prevents the genie from searching all knowledge bases for every query.

Reference each knowledge base by its exact name, the same name it has in your workspace. The exact name match helps the genie identify the correct knowledge base unambiguously. For example:

```plaintext
KNOWLEDGE BASE RETRIEVAL

For POLICY QUESTIONS: search
"HR Policies | HR Assistant" only

For IT TROUBLESHOOTING: search
"Confluence | IT Genie" only

For COMPETITIVE QUESTIONS: search
"Highspot | Sales Competitive Intelligence"
only

Do not search knowledge bases for use cases
where skills provide the data. Use skills
for all transactional data retrieval.
```

The `do not search knowledge bases for transactional data` instruction prevents the genie from answering structured data questions from a knowledge base when a skill should be used instead. The genie may search the knowledge base when it should call a skill without this instruction.

## Prevent knowledge base loops

A knowledge base loop occurs when the genie searches a knowledge base, doesn't find a satisfactory answer, searches again, still doesn't find a satisfactory answer, and continues searching. This consumes context window space, increases latency, and often produces no better answer on the second or third attempt than on the first attempt.

Prevent knowledge base loops with an explicit call limit instruction in the job description:

```plaintext
Call each knowledge base only once per user
question. If the first search doesn't produce
a relevant answer, don't search again.
Instead, tell the user you don't have that
information and suggest contacting
[relevant team] directly.
```

This instruction is also appropriate in App Event Business Data prompts for any event type where the genie needs to search a knowledge base as part of its processing. Include it as a **Critical Instruction** near the top of the Business Data prompt.

## Choose an ingestion path for your content

There are two mechanisms for ingesting content into a knowledge base: [Workato GO](/en/agentic/workato-go) data sources and knowledge base recipes. The choice between ingestion paths has a significant implication that's easy to miss.

- **Workato GO data sources are permission-aware**: Content ingested through a Workato GO data source, such as Google Drive, Confluence, or SharePoint, respects the source system's permission model. A user who doesn't have access to a specific Confluence page in the native system can't retrieve fragments from that page through the genie's knowledge base search.
  
- **Knowledge base recipes aren't permission-aware**: Content ingested through a custom recipe provides data to all users who interact with the genie, regardless of their permissions in the source system. A document restricted to HR managers in Confluence becomes accessible to all employees through the genie if it's ingested through a recipe.
  

Use Workato GO data sources for content that has access restrictions in the source system. Use knowledge base recipes only for content that's appropriate for all users who interact with the genie.

This distinction is particularly important for:

- HR documentation with different content for employees and managers
- Financial documentation with restricted access
- Legal documentation with limited distribution
- Any content marked confidential or restricted in the source system

Use Workato GO data sources if you're not sure whether content has access restrictions.

---

---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/knowledge-bases/knowledge-base-management.md
description: >-
  Manage content across Workato GO and custom genie knowledge bases to search,
  organize, remove documents, and track storage footprints.
---

# Knowledge base management

Knowledge base management gives you a centralized view to monitor and manage the content stored across your [Workato GO](/en/agentic/workato-go) and custom knowledge bases.

![Knowledge base management](/assets/knowledge-base-management.C9YXiwoi.png)_Knowledge base management_

You can search, view, organize, and remove documents, track storage footprints, and manage file uploads to ensure your genie has access to accurate and up-to-date information. Storage footprint isn't supported for Workato GO.

![Knowledge base management file uploads](/assets/knowledge-management-uploads.dPiihVhh.png)_Knowledge base management file uploads_

Workato GO enforces its own permission model. Agent Studio uses this permission model to scope file visibility to your Workato GO identity and access level. This means you can only view content that you have permission to access in the connected data source. File visibility for third-party apps, such as Confluence, is also scoped to your identity permissions.

![Workato GO permissions are applied to knowledge bases](/assets/knowledge-base-workato-go-permissions.DFJFL3V2.png)_Workato GO permissions are applied to knowledge bases_

## Manage knowledge bases

Complete the following steps to access and manage your knowledge base data sources, including Workato GO sources:

1. Go to **Projects > Assets**.
   
2. Click **Knowledge bases**.
   
3. Select the knowledge base you plan to view or update.
   
4. Review the details panel for total storage size (unsupported for Workato GO), description, dependencies (how many genies use this knowledge base) and recipe or data source details.
   
   ![Knowledge base details panel](/assets/knowledge-base-details-panel.M07Ekbie.png)_Knowledge base details panel_
   
5. Click a source to view the individual source details.
   
   ![Knowledge source details](/assets/knowledge-source-details.BkjIxx8I.png)_Knowledge source details_
   
6. Optional. Select one or more source checkboxes and click **Remove documents** to remove documents from your knowledge base.
   
   ![Remove documents](/assets/remove-knowledge.7atbwQ2_.png)_Remove documents_
   

## More resources

- [Knowledge base configuration](/en/agentic/agent-studio/knowledge-bases/knowledge-base-configuration)
- [Knowledge base document preparation](/en/agentic/agent-studio/knowledge-bases/knowledge-base-configuration#knowledge-base-document-preparation)
- [Knowledge base and database best practices](/en/agentic/agent-studio/knowledge-bases/knowledge-base-and-database-best-practices)
- [Design skills for databases](/en/agentic/skills/design-skills-for-databases)

---

---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/knowledge-bases/data-ingestion.md
description: >-
  Learn how to ingest content into a genie knowledge base using Workato GO data
  sources or recipes, and how to chunk it for retrieval.
---

# Knowledge base data ingestion

Ingesting data correctly determines whether the data can be retrieved reliably. A well-scoped knowledge base with poorly ingested content produces the same poor retrieval as a badly scoped knowledge base. This page covers the ingestion decisions that determine retrieval quality.

## Two ingestion paths

There are two methods to add content to a knowledge base:

- **Workato GO data sources**: Prebuilt connectors available in the [Workato GO](/en/agentic/workato-go) interface. Workato GO data sources connect to common content sources, including Google Drive, Confluence, SharePoint, and Notion, and ingest content with permission-awareness. A user who doesn't have access to a document in the source system can't retrieve fragments from that document through the genie.

Use Workato GO data sources when:

- The content has access restrictions in the source system
  
- A pre-built connector exists for your content source
  
- You need permission-aware retrieval without building custom ingestion logic
  
- **Knowledge base recipes**: Custom recipes you build in the Workato recipe editor. Knowledge base recipes fetch content from any source, including sources not supported by Workato GO data sources, and write it to the knowledge base using the [Knowledge base by Workato](/en/agentic/agent-studio/connectors/knowledge-base-connector/knowledge-base-connector) connector, which can upsert, delete, list, and search documents in a knowledge base. Knowledge base recipes aren't permission-aware. All ingested content is accessible to all users who interact with the genie.
  

Use knowledge base recipes when:

- No Workato GO data source exists for your content source
- The content is appropriate for all users and permission-awareness isn't required
- You need custom ingestion logic, such as transformation, filtering, or format conversion, that a pre-built connector doesn't support

Use Workato GO data sources When both options are available and the content has access restrictions. Content ingested through a recipe isn't retroactively permission-aware if you later switch to a Workato GO data source.

## Chunk content logically

[Content chunking](/en/agentic/agent-studio/knowledge-bases/knowledge-base-configuration#document-preparation-best-practices) before ingestion is the single biggest determinant of retrieval quality after scope. Chunking is the process of dividing content into the individual units that are stored in the knowledge base and retrieved as fragments.

The knowledge base retrieval mechanism returns the most semantically similar fragments rather than the most semantically similar documents. Retrieval quality depends on whether the fragments themselves contain the answer, not whether the document contains the answer.

**The problem with whole-document ingestion**

Retrieval for a question about annual leave accrual may return the entire document as the matching fragment if you ingest a 20-page HR policy document as a single knowledge base entry. The useful information is in the document, but the fragment is too large and too general for the retrieval mechanism to pinpoint it.

**The benefit of logical chunking**

Splitting the same document into individual sections enables section-specific retrieval for a question about annual leave accrual. Create entries for annual leave accrual, sick leave policy, and parental leave eligibility. These fragments are specific, relevant, and citable.

Logical chunking means splitting content at natural boundaries, such as sections, subsections, individual policy items, and individual FAQ entries, rather than at arbitrary size boundaries. A policy document with five sections becomes five knowledge base entries. A FAQ with thirty questions becomes thirty entries. A CSV file with one hundred products becomes one hundred entries.

### Chunking guidelines by content type

| Content type | Chunking approach |
| --- | --- |
| Policy documents | One entry per section or subsection. Split long sections further at logical paragraph breaks. |
| FAQ content | One entry per question-answer pair. Don't batch multiple FAQs into a single entry. |
| Closed tickets | One entry per ticket, including the title, description, and resolution notes. |
| CSV or tabular data | One entry per row, formatted as a structured document in JSON or YAML, not as a raw CSV row. |
| Meeting notes or call summaries | One entry per meeting or call, with key topics and outcomes clearly labeled. |
| Product documentation | One entry per feature or capability, not one entry per product. |

## Source URL

Every entry ingested into a knowledge base should include the URL of the original source document. Your genie uses this URL to cite its sources when presenting information to the user.

Source URLs serve two purposes:

- **Trust and verifiability**: A user who receives a policy answer from the genie can click the link to verify the answer in the original document. This builds trust in genie responses and reduces escalations to human experts.
- **Debugging**: When a retrieval produces incorrect results, the source URL in the knowledge base entry makes it easy to identify which document the incorrect fragment came from and update or remove it.

Include the source URL as a dedicated field in every knowledge base entry. Don't embed the source URL in the text content. Your genie can reference the URL in its response when it retrieves the fragment: `According to the Annual Leave Policy (link).`

## Data format and quality

The quality of content in the knowledge base directly affects retrieval quality. Poorly formatted, noisy, or outdated content produces poor results regardless of how well the knowledge base is scoped or chunked.

- **Use Markdown for structured content**: Plain text is acceptable, but Markdown improves the structure of retrieved fragments. Headers make section boundaries clear. Bold text highlights key terms. Lists present enumerable items cleanly. A knowledge base entry formatted in Markdown is easier for both the retrieval mechanism and the LLM to process than a wall of plain text.
  
- **Convert structured data to JSON or YAML before ingesting**: Raw CSV rows, raw SQL output, and raw tabular data aren't ideal for vector storage. Convert each row or record to a structured document format with labeled fields before ingesting. `annual_leave_days: 20, eligibility: all permanent employees, accrual_rate: 1.67 days per month` is more retrievable than a raw CSV row.
  
- **Clean content before ingesting**: Remove HTML tags, formatting artifacts, navigation elements, and boilerplate text that appears in every document but isn't useful for retrieval. Content that arrives from a web scrape or document export often contains significant noise that degrades retrieval quality if left in.
  
- **Remove outdated content**: A knowledge base that contains both the current version of a policy and an older version produces retrieval results that contradict each other. Check whether the content source already contains outdated versions before ingesting and exclude these versions. Implement logic to detect and remove deleted or superseded content for delta ingestion.
  

## Full load vs. delta load

Content ingestion isn't a one-time event. It requires an ongoing process to keep the knowledge base current. There are two ingestion modes, full load and delta load, and both are needed for a production knowledge base.

### Full load

A full load ingests all content from a source from scratch. Run it once when the knowledge base is first created to establish the baseline content.

Full load guidelines:

- **Apply specific filters, not blanket imports**: Don't ingest an entire Google Drive or an entire Confluence space. Define specific folders, labels, or tags that identify content relevant to this knowledge base. A Google Drive full load should specify the exact folder, such as `HR Policies`, not the entire drive.
- **Apply exclusion logic**: Exclude file types that aren't supported or useful, such as image-only PDFs, video files, and template files not intended for retrieval. Exclude documents with names or labels indicating they are drafts, archived, or internal-only if they shouldn't be retrieved.
- **Run the full load recipe once**: Mark it clearly. A recipe name like `FULL LOAD - Run Once - HR Policies KB` prevents future builders from accidentally re-running it and creating duplicate entries.
- **Verify the output**: Run the full load and check a sample of ingested entries to confirm the chunking, formatting, and source URLs are correct. Fix any issues before configuring the delta load.

### Delta load

A delta load ingests only content that has changed since the last run. Run it on a schedule to keep the knowledge base current as the source content evolves.

Delta load guidelines:

- **Set frequency based on content volatility**: Policies that change quarterly can be updated monthly. Product documentation that changes weekly should be updated daily. Match the ingestion frequency to how often the content changes and how quickly outdated content would cause user-facing problems.
- **Detect and handle deleted content**: When a document is deleted from the source system, remove the corresponding entries in the knowledge base. Delta loads that only add new content and don't remove deleted content accumulate stale entries over time. Implement deletion detection by comparing the current source document list against the knowledge base entries and removing entries for documents that no longer exist.
- **Handle updated content correctly**: When a document is updated, the old knowledge base entries should be replaced with entries reflecting the updated content. Avoid accumulating multiple versions of the same document as separate entries.

## Current data ingestion limitations

Understand the following platform limitations before designing your ingestion process:

| Limitation | Detail |
| --- | --- |
| Maximum file size | 100 MB per file for uploads to knowledge base. Knowledge base uploads follow a separate process and maintain separate limits from [file and image uploads](/en/agentic/agent-studio/upload-files-and-images) in the genie chat interface. |
| Supported file types | PDF, PPTX, XLSX, DOCX. Other file types, including images, videos, and audio files, aren't supported. |
| Text content only | Only the text content of documents is extracted during ingestion. Images within documents aren't extracted or indexed. If a policy document contains important information in an image or diagram rather than in text, that information isn't available for retrieval. |
| Images not supported | Image files such as JPG and PNG can't be ingested as knowledge base documents. Convert the visual to a text description before ingesting if the visual content is critical for a use case. |

These limitations affect how you approach ingestion for certain content types. A policy document that contains tables as images rather than formatted text requires a manual conversion step before ingestion. A product catalog that includes product images needs the image-based information captured as text.

## Track ingestion

Maintain a [Data table](/en/data-tables) that records what's been ingested into each knowledge base. Each row must contain:

- Source document identifier, such as the Confluence page ID or the Google Drive file ID
- Source document name
- Knowledge base it was ingested into
- Date of ingestion
- Number of entries created
- Status field: active, deleted, or superseded

This record serves two purposes. It makes it possible to audit what's in your knowledge base without reading every entry. It also provides the reference data needed for delta load deletion detection by comparing the current source document list against the ingestion record to identify documents that have been deleted from the source.

---

---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/knowledge-bases/retrieval-prompting.md
description: >-
  Learn how to write retrieval instructions that tell a genie which knowledge
  base to search and prevent loops and wasted context tokens.
---

# Retrieval prompting

A well-scoped, well-ingested knowledge base is necessary but not sufficient for reliable retrieval. The third element that determines whether retrieval works correctly in production is how the genie is instructed to use it. Poorly written retrieval instructions produce three specific failure modes:

- Searching the wrong knowledge base
- Searching the same knowledge base multiple times
- Retrieving irrelevant fragments from a knowledge base that's too broad for the question

This page covers how to prevent all these failure modes.

## Failure modes

The most common failure modes include:

- **Wrong knowledge base searched**: The genie has multiple knowledge bases connected and searches the wrong knowledge base for a question. An employee asking about leave policy triggers a search of the competitive intelligence knowledge base. A sales rep asking about competitive positioning triggers a search of the HR policies knowledge base. The retrieved fragments are irrelevant and the answer is wrong or missing.
  
- **Knowledge base loop**: The genie searches the knowledge base, doesn't find a satisfactory answer, and searches again. Each search consumes context window space and adds latency. The repeated searches rarely produce a better answer than the first, but the searches degrade the conversation experience and waste genie actions.
  
- **Retrieval token waste**: The genie searches a large, broad knowledge base and retrieves several large, loosely relevant fragments. These fragments consume a significant portion of the context window before the genie has composed a response, leaving less space for conversation history, skill outputs, and the response itself.
  

Each failure mode has a specific fix that can be addressed in the prompts.

### Specify knowledge bases by name per use case category

The most reliable way to prevent the wrong knowledge base from being searched is to tell the genie exactly which one to search for each use case category in the Job Description. Don't rely on the genie to infer which knowledge base is relevant from descriptions alone. Make it explicit.

The instruction should use the exact name of the knowledge base, not a description of it or a paraphrase of its name. The exact name match is what the genie uses to identify the correct knowledge base.

```plaintext

KNOWLEDGE BASE RETRIEVAL

For POLICY QUESTIONS: search
"HR Policies | HR Assistant" only.
Do not search any other knowledge base.

For COMPETITIVE QUESTIONS: search
"Highspot | Sales Competitive Intelligence"
only. Do not search any other knowledge base.

For LEAVE REQUESTS: do not search any
knowledge base. Use skills only.

For all other use case categories: do not
search any knowledge base unless explicitly
instructed to do so in the category
instructions above.
```

The `do not search any other knowledge base` clauses are important. The genie may search multiple knowledge bases in parallel when uncertain which one to use without this instruction, producing retrieval noise.

The `do not search any knowledge base` instruction for skill-appropriate use cases prevents the genie from attempting to answer structured data questions from a knowledge base when a skill should be used instead.

### Implement call limits to prevent loops

Knowledge base loops are prevented by an explicit call limit instruction. The most reliable form specifies a hard limit per question:

```plaintext

Call each knowledge base only once per
user question. If the first search doesn't
return a relevant answer, don't search again.
Instead, tell the user you don't have that
information and suggest contacting
[relevant team or resource] directly.
```

This instruction does two things:

- Sets the call limit at one
- Specifies what to do when the limit is reached

Without the second part of the instruction, the genie may comply with the call limit but produce an unhelpful response when the knowledge base doesn't have the answer.

App Event Business Data prompts, where the genie processes a specific event type and may need to search a knowledge base as part of that processing, the call limit instruction should appear as a Critical Instruction near the top of the prompt:

```plaintext

CRITICAL INSTRUCTION: You are only allowed
to call the knowledge base once in this
entire process. Track this as kb_called =
false at the start. Set kb_called = true
after the first call. Never make a second
knowledge base call regardless of what the
first call returns.
```

The explicit state-tracking instruction, `kb_called = false / true`, produces more reliable adherence to the call limit than a simple `call only once` instruction. It gives the LLM a concrete mental model of the constraint it's enforcing.

### Split large knowledge bases and reference by relevance

Retrieval quality degrades when a knowledge base has grown large, either because it was scoped too broadly to begin with or because content has been added over time. A large knowledge base has more irrelevant fragments competing with the relevant ones.

The fix is to split the large knowledge base into smaller, more focused knowledge bases and reference only the relevant knowledge base for each type of question.

**Before splitting:**

One large `HR | HR Assistant` knowledge base containing leave policies, benefits information, onboarding materials, performance management guidelines, and disciplinary procedures. The genie searches this knowledge base for any HR question and may retrieve fragments from any of these areas.

**After splitting:**

- `HR Leave Policies | HR Assistant`: leave policies, eligibility, and accrual rules only
- `HR Benefits | HR Assistant`: benefits information only
- `HR Onboarding | HR Assistant`: onboarding materials only

The job description references each one specifically:

```plaintext

For leave policy questions: search
"HR Leave Policies | HR Assistant"

For benefits questions: search
"HR Benefits | HR Assistant"

For onboarding questions: search
"HR Onboarding | HR Assistant"
```

The retrieval quality improvement from this split is significant. A leave policy question now searches a knowledge base that contains only leave policy content. Every fragment in that knowledge base is relevant to some aspect of leave policy. The semantic similarity scores are higher, the retrieved fragments are more focused, and the LLM produces a more accurate answer.

The token usage reduction is also meaningful. A smaller knowledge base with more relevant content produces fewer, shorter fragments per retrieval, leaving more room for conversation history, skill outputs, and the response.

## Knowledge base loop

A knowledge base loop often starts because the genie can't find a satisfactory answer and searches again hoping for a different result. The search returns different fragments on the second attempt because vector search has an element of randomness in which fragments are returned, but they're no more useful than the first set.

Preventing the loop requires telling the genie what to do when the knowledge base doesn't have the answer:

```plaintext

If the knowledge base doesn't contain
information relevant to the user's question:
- Don't search again
- Tell the user clearly: "I don't have
  information about that in my knowledge base"
- Suggest where the user can find the answer:
  "For questions about [topic], please contact
  [team] directly or visit [resource]"
- Don't guess or infer an answer from
  general knowledge
```

The `don't guess or infer from general knowledge` instruction is particularly important for policy and compliance use cases. An LLM that doesn't find an answer in the knowledge base may fall back to its training data and provide a plausible-sounding but incorrect answer. A wrong answer is worse than no answer for HR policies, legal requirements, and compliance procedures.

## Balance retrieval instructions with knowledge base descriptions

The job description's retrieval instructions and the knowledge base descriptions work together. The knowledge base description is what the genie reads when it needs to identify which knowledge base to search without explicit instruction. The job description's retrieval instructions are what the genie reads when you want to be explicit about which knowledge base to use for which question type.

- **Knowledge base descriptions**: provide a reliable fallback when the genie encounters a question type not explicitly covered in the job description retrieval instructions.
- **Job description retrieval instructions**: Override the genie's inference from knowledge base descriptions for use case categories where you need deterministic knowledge base selection.

Don't rely on knowledge base descriptions alone to produce correct knowledge base selection for your primary use case categories. Explicitly reference each knowledge base by name in the job description for every use case category that requires retrieval. Use knowledge base descriptions as a secondary signal that catches cases the job description instructions don't cover.

## Retrieval instructions in App Events vs. job description

Knowledge base retrieval instructions in the job description apply to all conversational interactions. Retrieval instructions in [App Event](/en/agentic/agent-studio/app-events) Business Data prompts apply only to that specific event type.

App Events where the genie needs to search a knowledge base need the retrieval instruction directly in the Business Event Data prompt rather than relying on the job description. The genie in an App Event context doesn't reliably read the job description with the same fidelity as in a direct conversation. The Business Event Data prompt must be self-contained.

Knowledge base retrieval behavior required for the event type must be specified in the Business Event Data prompt itself:

```plaintext

CRITICAL INSTRUCTION: Search the
"Freshservice IT Genie" knowledge base
exactly once to identify if there is an
existing solution for the reported ticket.
Do not make more than one knowledge base call.
If no solution is found, proceed to step 4
without searching again.
```

## Retrieval instructions checklist

Verify the following before deploying any genie that uses knowledge bases:

- Every knowledge base connected to the genie is referenced by exact name in the job description retrieval instructions.
- Every use case category that should search a knowledge base has an explicit instruction specifying which knowledge base to search.
- Every use case category that shouldn't search a knowledge base has an explicit instruction saying so.
- A call limit of once per question is specified for every knowledge base.
- A fallback behavior is specified for when the knowledge base doesn't have the answer.
- Large knowledge bases have been split into smaller functional ones where retrieval quality has been observed to degrade.
- App Event prompts that require knowledge base retrieval include self-contained retrieval instructions and don't rely on the job description.

---

---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/knowledge-bases/knowledge-bases-and-databases.md
description: >-
  Learn when to use a knowledge base for semantic search and when to use a
  structured database for accurate, complete genie results.
---

# Knowledge bases versus databases

Knowledge bases and structured databases have different purposes in Agent Studio. Understanding when to use each is critical for building genies that return accurate and complete results.

## When to use knowledge bases

Use knowledge bases when you need to find related information across documents based on semantic similarity rather than exact matches.

Knowledge bases use hybrid semantic search to retrieve information based on relevance, not completeness.

Knowledge bases provide the following capabilities:

- Return a maximum of 10 documents per query
- Optimized for semantic similarity and relevance
- Use natural language understanding to find related content

Knowledge bases excel at the following semantic search scenarios:

- Finding related documents across your knowledge repository
- Traditional Retrieval-Augmented Generation (RAG) patterns
- Situations where approximate answers are acceptable
- Queries that benefit from understanding intent rather than exact matching

**Knowledge Base example**

- **User asks**: `What's our policy on returning damaged items?`
  
- **Genie responds**: The genie sends the query to the Knowledge Base, which performs hybrid search across policy documents, SOPs, and support guides. The genie returns the most relevant sections about damaged item returns, even if the exact phrase `damaged items` isn't in the document title.
  
- **Why this works**: The user needs related information, not an exact match. The Knowledge Base understands intent and finds semantically similar content, such as a document titled `Refund and Exchange Guidelines` that covers damage scenarios in section 3.
  

### Avoid knowledge bases for aggregation use

**What happens:** Builders add hundreds of documents to Knowledge Bases and expect them to handle aggregation queries like "how many invoices are overdue?" or "show me all tickets from Customer X last week."

**The result:** The agent returns incomplete or inaccurate results because Knowledge Bases return a maximum of 10 documents per query. They're optimized for relevance, not completeness.

**The solution:** Use structured databases with skills that have defined filter parameters for queries requiring accuracy, aggregation, or comprehensive results.

## When to use databases

Use databases when you need exact numbers, precise filtering, or comprehensive results from structured data.

Databases contain structured data with skills that have defined filter parameters. Workato supports external database systems, Workato [Data tables](/en/data-tables), and synced databases. Databases enable you to query for accuracy, aggregation, or comprehensive results.

Databases provide the following capabilities:

- Query across all records in your dataset
- Support exact filtering with multiple parameters
- Enable aggregation operations, such as counts, sums, and averages
- Return precise and complete results

Databases excel in the following structured dataset scenarios:

- Queries requiring exact numbers or counts
- Aggregation across multiple records
- Filtering by specific criteria, such as status, date, customer, and so on
- Comprehensive lists where completeness matters
- Operations on structured data fields

**Database example**

- **User asks**: `How many open tickets for Customer X?`
  
- The agent maps the question to skill inputs, such as `Status = Open`, `Customer ID = X`. The skill queries the database with exact filters and returns a precise count, such as `Customer X has 14 open tickets`.
  
- **Why this works**: The query needs an exact number across all matching records. A database can filter and count comprehensively.
  

## Knowledge Base and database quick comparison

| Scenario | Use Knowledge Base | Use database |
| --- | --- | --- |
| **Aggregation queries** | ❌ Not designed for aggregation | ✅ Counts, sums, totals |
| **Exact filtering** | ❌ Limited to 10 results | ✅ Comprehensive filtering |
| **Finding related content** | ✅ Semantic understanding | ✅ Requires exact matches |
| **"How many...?" questions** | ❌ Incomplete results | ✅ Precise counts |
| **Policy or procedure lookup** | ✅ Finds relevant sections | ❌ Requires structured data |
| **Status-based queries** | ❌ May miss records | ✅ Filters all records |
| **Similar document search** | ✅ Understands similarity | ❌ Not applicable |
| **Date range filtering** | ❌ Limited results | ✅ Comprehensive filtering |
| **"Show me all..." queries** | ❌ Returns max 10 | ✅ Returns all matches |
| **Conceptual questions** | ✅ Intent understanding | ❌ Needs exact criteria |

## Use the same data in knowledge bases and databases

You can use the same data in both a knowledge base and a database when it supports both structured queries and semantic search. Refer to [Knowledge base and database best practices](/en/agentic/agent-studio/knowledge-bases/knowledge-base-and-database-best-practices) to ensure that your genie routes queries to the correct knowledge base or database.

**Support ticket example**

Use a database for structured queries, such as:

- Ticket ID
- Status
- Priority
- Customer ID
- Assigned agent
- Created or updated dates
- Resolution code

Use a knowledge base for semantic searches, such as:

- Ticket descriptions
- Customer communications
- Resolution notes
- Error messages reported

| User question | System to use | Why |
| --- | --- | --- |
| `How many items are low stock?` | Database | Aggregation on inventory field |
| `What laptops are good for video editing?` | Knowledge Base | Semantic understanding of intent |
| `What's the price of SKU-12345?` | Database | Exact lookup |
| `Find products similar to the UltraWidget Pro` | Knowledge Base | Semantic similarity |
| `How many invoices are overdue?` | Database | Aggregation on invoice due date field |

### Link knowledge base and database skills

You can chain knowledge bases and databases together for powerful workflows. Refer to the following examples for more information:

#### Semantic search and structured lookup

- **User asks**: `Have we seen this authentication error before?`
  
- **Knowledge base**: Finds relevant past tickets by searching descriptions and returns ticket IDs from the most relevant matches.
  
- **Database skill**: Fetches current status and resolution details for the ticket IDs returned by the knowledge base.
  

#### Structured filter and semantic search within results

- **User asks**: `What are the common issues for Enterprise customers this quarter?`
  
- **Database skill**: Filters tickets, such as `Customer Tier = Enterprise` and `Created After = Q1 Start` and returns ticket IDs matching the filter.
  
- **Knowledge base**: Searches ticket descriptions within that set for patterns and themes.
  
- **Implementation tip**: Create skills that accept IDs from previous steps. For example: `Search Past Ticket Resolutions` in the knowledge base returns ticket ID and `Get Ticket Details by ID` in the database accepts the ticket ID and returns the full record.
  

## More resources

- [Knowledge base and database best practices](/en/agentic/agent-studio/knowledge-bases/knowledge-base-and-database-best-practices)
- [Design skills for databases](/en/agentic/skills/design-skills-for-databases)
- [Knowledge base configuration](/en/agentic/agent-studio/knowledge-bases/knowledge-base-configuration)

---

---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/knowledge-bases/knowledge-base-and-database-best-practices.md
description: >-
  Learn best practices for writing skill and knowledge base descriptions and job
  descriptions that route genie queries to the right source.
---

# Knowledge base and database best practices

Knowledge bases and databases are a powerful resource for your genie. It's important to create these sources carefully to improve information routing and retrieval.

## Provide detailed skill descriptions

Your genie uses skill descriptions to decide which skill to invoke. You must be explicit about when you expect each skill to be used. For example:

| ❌ Not recommended | ✅ Recommended |
| --- | --- |
| `Search Tickets - Searches the ticket system for information.` | `Search Tickets by Filters - Use this skill when the user needs EXACT counts, filtered lists, or specific ticket lookups. Supports filtering by: status, priority, customer, assigned agent, and date range. Use for questions like how many tickets..., show me all tickets where..., list tickets from...` |

## Provide detailed knowledge base descriptions

Your genie uses knowledge base descriptions to determine the scope and relevance of the information, which improves response accuracy. For example:

| ❌ Not recommended | ✅ Recommended |
| --- | --- |
| `Search Tickets Knowledge Base - Searches the ticket system knowledge base for information.` | `Search Ticket Knowledge Base - Use this skill when the user needs to find RELATED information, past solutions, or similar issues. Use for questions like have we seen this before?, how did we fix this?, find similar issues to...Does NOT return exact counts or comprehensive lists.` |

## Add a detailed job description

You must provide a detailed job description to help your genie route queries to the correct information source. For example:

```plaintext
When the user asks about tickets, choose the appropriate skill:

USE "Search Tickets by Filters" when:
- User asks for counts ("how many", "what's the total")
- User asks for filtered lists ("show me all X where Y")
- User asks for specific lookups by ID, customer, status, date
- User needs exact, comprehensive results

USE "Search Ticket Knowledge Base" when:
- User asks about similar past issues ("have we seen this before")
- User asks how something was resolved ("how did we fix")
- User asks about patterns or common problems
- User is searching by symptoms or error messages
- Approximate or "most relevant" results are acceptable

If unsure, ask the user: "Are you looking for an exact count/list, or trying
to find related information from past tickets?"
```

Include examples in your job description to help your genie learn and provide extra context. For example:

```plaintext

Examples:

User: "How many open tickets does Acme Corp have?"
→ Use: Search Tickets by Filters (status=open, customer=Acme Corp)

User: "Have we seen this 'connection timeout' error before?"
→ Use: Search Ticket Knowledge Base (query="connection timeout error")

User: "What P1 tickets came in last week?"
→ Use: Search Tickets by Filters (priority=P1, created_after=last week)

User: "How did we resolve the SSO issues for enterprise clients?"
→ Use: Search Ticket Knowledge Base (query="SSO issues enterprise resolution")
```

## Test your genie

Workato recommends testing your genie to verify that routing between knowledge bases and databases is accurate. Refer to [Create a sample scenario and test messages](/en/agentic/agent-studio/test-genie#create-a-sample-scenario-and-test-messages) for more information.

---

---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/knowledge-bases/knowledge-base-recipes.md
description: >-
  Create a knowledge base recipe that syncs content from connected apps so your
  genie's knowledge base stays current with the latest data.
---

# Knowledge base recipes

Knowledge base recipes sync and update information from your connected applications to your knowledge base. The knowledge base recipe ensures that your genie's knowledge base has access to the latest data and stays aligned with your business requirements. Knowledge bases and knowledge base recipes can be assigned to multiple genies, including genies stored in different projects. Refer to [Create a genie manually](/en/agentic/agent-studio/create-a-genie) for complete steps on how to create a genie with a job description, AI model, chat interface, knowledge base, knowledge base recipe, and skills.

> **NEED AN EXAMPLE?**
> 
> Refer to the [Connect your knowledge base to Confluence](/en/getting-started/use-cases/agent-studio/knowledge-bases/knowledge-base-confluence-use-case) use case for a step-by-step example on how to create and connect your knowledge base to Confluence with a knowledge recipe.

## Getting started with Knowledge base recipes

Complete the following steps to create a knowledge recipe:

1. Sign in to Workato.
   
2. Go to **AI Hub > Agent Studio**.
   
3. Select the genie where you plan to create a knowledge base recipe.
   
4. Go to the **Knowledge bases** section and select the knowledge base where you plan to add your knowledge recipe.
   
   ![Go to the Knowledge bases section](/assets/genie-build-page.DQ8_sDC8.png)_Go to the **Knowledge bases** section_
   
5. Click **\+ Add knowledge**.
   
6. Select **New knowledge recipe**.
   
7. Enter a name for your knowledge recipe in the **Recipe name** field.
   
8. Use the **Location** drop-down menu to select a location for your knowledge recipe.
   
   ![Set up your knowledge recipe](/assets/set-up-knowledge-recipe.DSLepKGW.png)_Set up your knowledge recipe_
   
9. Click **Add knowledge base**. The recipe editor opens with the [Upsert documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/upsert-documents) action from [Knowledge base by Workato](/en/agentic/agent-studio/connectors/knowledge-base-connector/knowledge-base-connector) automatically selected.
   
   ![Knowledge recipe with the document upsert action automatically selected](/assets/knowledge-recipe.CqTvF1Cz.png)_Knowledge recipe with the document upsert action automatically selected_
   
   > **NEW RECIPES USE THE UPSERT DOCUMENTS ACTION**
   > 
   > New knowledge base recipes use the [Upsert documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/upsert-documents) action. Recipes created earlier use the deprecated [Store knowledge](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/store-knowledge) action, which continues to run unchanged.
   
10. Configure your recipe.
    
11. Test your recipe to ensure workflow compatibility with your genie.
    
12. Click **Save**.

---
