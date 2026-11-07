---
url: 'https://docs.workato.com/en/agentic/skills/design-skills-for-databases.md'
description: >-
  Design database skills by mapping how users naturally ask questions to the
  filters and parameters your data source uses to retrieve data.
---

# Design skills for databases

The key to effective database skills is mapping how users naturally ask questions to the parameters your data source can use for filtering data. Use the following guidelines to design your skills:

## List user questions

Create a list of questions users ask when designing skills. For example, users in a support ticket system might ask the following questions:

- `How many tickets are open for Acme Corp?`
- `Show me all P1 tickets from last week`
- `What tickets did Sarah close yesterday?`
- `Are there any tickets about login issues for Enterprise customers?`

## Identify filter patterns

Break down each user question into underlying filters to identify patterns. For example:

| Question | Filters needed |
| --- | --- |
| `How many tickets are open for Acme Corp?` | **Status**, **Customer** |
| `Show me all P1 tickets from last week` | **Priority**, **Date Range** |
| `What tickets did Sarah close yesterday?` | **Assigned To**, **Status**, **Date Range** |
| `Are there any tickets about login issues for Enterprise customers?` | **Keyword**, **Customer Tier** |

## Design your skill inputs

Configure filters based on how users will interact with your genie:

| Consideration | Recommendation |
| --- | --- |
| **Required vs Optional** | Make filters optional when users might not specify the data. For example, `Show me open tickets` doesn't include a customer. |
| **Data type** | Use enums or drop-down menus for fixed values, such as **Status** or **Priority**. Use free text for names or IDs. Use date fields for time ranges. |
| **Naming** | Use skill input names that your genie can naturally map to. For example, `customer_name` is clearer than `acct_id`. |
| **Default values** | Consider sensible defaults. For example, the date range defaults to `last 30 days` if not specified. |

## Handle combined filters

Users often combine multiple filters into a single question. We recommend designing your skill to accept multiple optional parameters that work together. For example:

```plaintext
Skill: Search Support Tickets
Inputs:
  - status (optional): Open, Closed, Pending
  - priority (optional): P1, P2, P3, P4
  - customer_id (optional): string
  - assigned_to (optional): string
  - created_after (optional): date
  - created_before (optional): date
  - keyword (optional): string for searching ticket subject/description
```

This single skill can handle dozens of question variations by combining parameters.

## Identify the output your skill returns

Review your filters and parameters carefully to identify the key data your skill returns. Consider the data your skill should return:

- **For counts:** Return only the number.
- **For lists:** Return key fields only, such as **ID**, **title**, **status**, and **date**. Ensure your output returns less than 250KB.
- **For details:** Create a separate `Get Ticket Details` skill that takes a ticket ID.

> **USE SUMMARY AND DETAIL SKILL PATTERNS**
> 
> Pair a summary skill with a detail skill. The genie can search broadly before narrowing the search to more specific information.

---
