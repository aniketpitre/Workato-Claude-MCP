---
url: 'https://docs.workato.com/en/agentic/workato-genies/it/edi-genie/usage.md'
description: >-
  Learn how to use EDI Genie for common EDI operations tasks, including example
  prompts for transaction retrieval, partner health, audit reports, and more.
---

# Using EDI Genie

After setting up EDI Genie, you can interact with EDI Genie using natural language through your configured chat interface.

## EDI operations

Use the following prompts to get results from EDI Genie for common EDI operations tasks.

### Example prompts

**Transactions and errors**

- "Show me a list of all invalid transactions in the last week."
- "Get me details for transaction XYZ123."
- "Why is transaction ABC456 failing?"

**Trading partner health**

- "What is the partner health for partner ABC in the last month?"
- "What is the number of failed transactions by partner XYZ in the past week?"

**Audit trail reports**

- "Generate an audit trail report for all processed transactions in the last quarter."

**Poller diagnostics**

- "List all transactions stuck in poller xyz123."

**Real-time dashboard**

- "What is the status of the EDI gateway?"

### Paginating results

Transaction retrieval returns up to 100 records per page. If more results exist, EDI Genie returns a `next_cursor` value at the end of the response. Use it in a follow-up message to retrieve the next page:

- "Continue to the next page using the cursor `{next cursor value}`."

## Proactive alerts

EDI Genie sends summaries to your notification channel (Slack by default) covering successful and failed transactions, emerging error patterns, and partner-specific issues.

Each summary identifies whether failures are concentrated around a specific trading partner and includes a generated report. This helps teams spot recurring issues and operational risks without manually checking dashboards or logs.

## Onboarding help

EDI Genie answers onboarding and setup questions using Orderful guides and customer-supplied FAQs stored in its knowledge base. If the knowledge base doesn't contain the answer, EDI Genie lets you know.

---
