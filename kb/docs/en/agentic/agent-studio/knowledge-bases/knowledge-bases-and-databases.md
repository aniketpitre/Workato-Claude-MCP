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
