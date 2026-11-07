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
