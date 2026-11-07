---
url: 'https://docs.workato.com/en/agentic/agent-studio/knowledge-bases-vs-skills.md'
description: >-
  Learn whether to access genie data through a knowledge base for semantic
  search or a skill for structured, deterministic queries.
---

# Knowledge bases versus skills

Genie architecture must determine whether to access data through a [knowledge base](/en/agentic/agent-studio/knowledge-bases/knowledge-bases) or a [skill](/en/agentic/skills). You must determine what kind of retrieval the data requires to correctly design your genie.

## Knowledge base and skill distinctions

A knowledge base is for semantic search over unstructured content. The vector store retrieves the most relevant fragments based on semantic similarity to the query. It doesn't retrieve all matching records, count, or aggregate. The search finds and returns the most relevant content for a question.

A skill is for structured, deterministic data access. A skill calls an API or queries a database and returns exactly the records that match the specified criteria. The results are filtered and aggregated if needed. The result is deterministic so the same query returns the same data every time.

## When to use a knowledge base

Use a knowledge base in the following scenarios:

- **The data is unstructured reference content**: This content benefits from semantic retrieval. This includes policies, FAQs, process documentation, closed support tickets, product guides, competitive intelligence, and internal wikis. A user asking `what is the process for requesting a software license?` receives the answer from a document. The right retrieval mechanism is semantic search.
- **The question is open-ended**: The user doesn't know exactly where the answer lives. `What are my options for parental leave?` is a question a user would ask a knowledgeable colleague. The colleague would search their knowledge of HR policy and find the relevant information. The knowledge base does the same thing.
- **The content changes infrequently**: This enables content to be ingested in advance. Policies, procedures, and reference documentation are typically stable enough to ingest periodically and rely on for retrieval. Stale reference content is a manageable problem. A delta ingestion process keeps it current.
- **The content is too large or too varied to query with a structured API call**: A library of closed support tickets spanning three years, a collection of meeting notes from dozens of customer calls, a set of product documentation across multiple versions. This kind of content isn't queryable through a structured API in a useful way. Semantic search is the right access mechanism.

**Common knowledge base use cases**

- **HR policy Q&A**: Leave types, eligibility, and accrual rules
- **IT troubleshooting**: Known issues, resolution steps, and workarounds
- **Sales knowledge**: Competitive battlecards, product positioning, and objection handling
- **Compliance reference**: Regulatory requirements, internal policies, and audit procedures
- **Customer-facing knowledge**: Product documentation, support articles, and FAQs

## When to use a skill

Use a skill in the following scenarios:

- **The data is transactional and changes frequently**: Open support tickets, current opportunity pipeline, live inventory levels, and active user accounts are updated constantly. A knowledge base ingested yesterday may not reflect today's state. A skill that calls the source system API returns current data every time.
- **The query requires structured filtering, counting, or aggregation**: `How many P1 tickets were opened last month?` requires a `COUNT` query with date and priority filters. `What is the total value of opportunities closing this quarter?` requires a `SUM` with date filters. Knowledge bases can't perform either of these functions reliably. Use a skill for any question that requires knowing all matching records.
- **The result must be complete**: A knowledge base is the wrong tool if missing even one matching record produces an incorrect answer. Knowledge base retrieval is probabilistic. It returns the most relevant fragments, not necessarily all relevant fragments. Use a skill with a filtered API query that returns every matching record when completeness matters.
- **The data requires authentication as the requesting user**: Use a skill with [verified user access](/en/agentic/agent-studio/verified-user-access) if the data returned should be scoped to the individual user, such as their own tickets, opportunities, or leave balance. Knowledge bases ingested through knowledge base recipes aren't permission-aware and return the same content to all users regardless of their permissions.
- **The data needs to be created, updated, or deleted** Write operations are skills. A knowledge base is read-only.

**Common skill use cases**

- **Fetching a specific record by identifier**: A ticket by key, an opportunity by ID, or an account by name
- **Retrieving a user's current state**: Leave balance, assigned tickets, or open opportunities
- **Creating or updating records**: Ticket creation, leave submission, or opportunity updates
- **Running aggregate queries**: Counts, totals, or averages over a dataset
- **Retrieving real-time data**: Live system status, current queue length, or active incidents

## Data type boundaries

Several data types are at the boundary between knowledge base and skill and produce the most common misclassification errors. Refer to the following sections for guidance on these data type boundaries:

### Closed tickets and resolved issues

**Common mistake**: Ingesting closed tickets into a knowledge base so the genie can answer questions about past issues.

**When it's correct**: For ticket deflection, answering `has anyone seen this issue before?`, a knowledge base of closed tickets is appropriate. The query is semantic. The answer doesn't need to be complete or precise.

**When it's wrong**: For questions like `how many tickets did we close last month in this category?`, the knowledge base produces an incorrect answer. It retrieves the top-N most similar tickets, not all tickets matching the date and category filter. Use a skill for questions that require counting or completeness over the closed ticket dataset.

**The right approach**: Use a knowledge base for semantic similarity searches over closed tickets. Use a skill for structured queries requiring counts, filters by date or category, or completeness.

### Configuration data and business rules

**Common mistake**: Putting configuration data, such as approval thresholds, routing rules, and valid values, in a knowledge base for the genie to reference.

**Why it's usually wrong**: Configuration data is structured, specific, and needs to be retrieved exactly, not approximately. `What is the approval threshold for discounts?` should return a precise number, not a semantically similar fragment that might be from a different version of the policy. Configuration data belongs in a [Data table](/en/data-tables) accessed through a skill, or in the job description directly if it's small and stable enough.

**The right approach**: Store configuration data in a Data table. Build a skill that retrieves data by key. Reference the data in the job description if it's small enough to hardcode. Don't put structured configuration data in a knowledge base.

### Product catalogs and pricing

**Common mistake**: Ingesting a product catalog into a knowledge base for a CPQ genie to use when building quotes.

**When it's correct**: Use this data in knowledge bases for general product information questions, such as `what does Product X do?` or `what are the differences between Plan A and Plan B?`. The queries are semantic and the answers are informational.

**When it's wrong**: Use this data in skills when the genie needs to retrieve exact product IDs, pricing tiers, and SKUs to provide quotes. These values must be exact, not approximate. A knowledge base retrieval of pricing data risks returning the wrong tier, the wrong price point, or an outdated price.

**The right approach**: Use a knowledge base for product information and positioning. Use a skill that queries the pricing system directly for exact pricing and SKU data when building quotes.

## File retrieval

For use cases where the genie needs to access a specific file, such as a particular contract, a specific policy document, or a named spreadsheet, the decision depends on the file's characteristics.

- Use a skill if the file is under 250KB, can be retrieved by a unique identifier, and the relevant content can be extracted and filtered before being returned to the genie. A skill that fetches a specific file and returns its text content is faster and more precise than a knowledge base retrieval for a known document.
  
- Use a knowledge base if the file isn't easily retrievable through a structured identifier, the content is unstructured and would benefit from semantic chunking, or the user's query is open-ended enough that semantic retrieval is more appropriate than full document retrieval.
  

## Knowledge base and skill decision guide

| Question type | Data characteristics | Knowledge base or skill |
| --- | --- | --- |
| What is the policy on X? | Unstructured document, infrequently updated | Knowledge base |
| How does X work? | Reference documentation, explanatory content | Knowledge base |
| Has anyone seen this issue before? | Historical tickets, semantic similarity | Knowledge base |
| What is my current leave balance? | Structured, user-scoped, real-time | Skill with verified user access |
| How many tickets are open this week? | Requires count, structured filter | Skill |
| What are my open opportunities? | Transactional, user-scoped, requires completeness | Skill with verified user access |
| Create a ticket for this issue | Write operation | Skill |
| What is the approval threshold for discounts? | Precise configuration value | Skill or job description |
| What does Product X include? | Reference documentation, informational | Knowledge base |
| What is the price of Product X at enterprise tier? | Exact pricing, structured data | Skill |
| Summarize the last three calls with Acme | Transactional, filtered by account and date | Skill |
| What is our competitive positioning against Y? | Unstructured reference content | Knowledge base |

---
