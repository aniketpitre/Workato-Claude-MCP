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
