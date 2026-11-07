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
