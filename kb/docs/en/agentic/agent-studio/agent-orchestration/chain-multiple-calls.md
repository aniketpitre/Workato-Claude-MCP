---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/agent-orchestration/chain-multiple-calls.md
description: Use multiple Assign task to genie calls in the same recipe.
---

# Chain multiple calls

You can use multiple **Assign task to genie** calls in the same recipe, for example, a validation genie, followed by a summarization genie, followed by a routing genie. Chaining these correctly requires attention to context continuity and error handling.

## Pass context between calls

Each **Assign task to genie** call is discrete. The second genie call doesn't automatically have access to the first genie's context unless you pass it explicitly.

There are two approaches to handle how context is passed between genies:

- **Pass the Conversation ID**: Use the Conversation ID from the first **Assign task to genie** output as the Conversation ID input for the second call. This gives the second genie access to the conversation history from the first call. Use this approach when the second task must reference what the first genie said.
  
- **Pass structured output as task context**: Use the custom output fields from the first **Assign task to genie** call as labeled context in the second call's task instructions. This provides clean and reliable conversation history for structured data and enables the second genie to receive specific field values rather than a full conversation thread to parse.
  

For example:

```plaintext
Task: Draft a customer notification based
on the following ticket resolution details.

Resolution details from previous step:
- Ticket key: [ticket_key datapill]
- Category: [category datapill from Step 3]
- Resolution summary: [resolution datapill
  from Step 3]
- Time to resolve: [duration datapill]
```

## Error handling for chained calls

A chain of **Assign task to genie** calls can fail if the genie times out, a skill returns an error, or the output doesn't match the expected format causing downstream calls to receive incorrect or missing inputs.

You must add error handling after each **Assign task to genie** step in a chain:

- **Check the output fields**: Output fields must be populated and in the expected format before passing the values to the next step.
- **Handle low-confidence outputs**: Route to a human review step rather than continuing the automated chain if the genie returns a low-confidence output.
- **Log failures with enough context to diagnose the issue**: Include the task instructions, the genie's raw response, and the recipe job ID.

## Delegate subtasks between genies

The **Assign task to genie** action supports multi-agent architectures where a primary genie delegates subtasks to specialist genies. This allows the user to interact with the primary genie, which calls specialist genies headlessly through the **Assign task to genie** action to complete tasks.

The skills available to the primary genie must include a skill that calls the **Assign task to genie** action. This effectively makes the **Assign task to genie** action a callable skill. The primary genie calls this skill when it needs to delegate work.
