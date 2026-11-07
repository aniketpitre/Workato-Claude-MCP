---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/connectors/workato-genie-connector/actions/assign-task-to-genie.md
description: >-
  Assign a task to a genie and wait for it to complete before the recipe
  continues.
---

# Workato Genie connector - Assign task to genie action

The **Assign task to genie** action assigns a task to a genie and waits for it to complete before proceeding to the next step. The recipe job suspends during processing and resumes with the genie's response available as a datapill. The output includes the genie's final response and a log of all actions performed.

Use this action for automated tasks that don't require a user. Use the [Send business event](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/send-business-event) action for use cases where a user needs to receive a message or take action. Refer to [App Events vs Agent orchestration](/en/agentic/agent-studio/app-events-vs-agent-orchestration) for a full comparison.

Refer to [Agent orchestration](/en/agentic/agent-studio/agent-orchestration) for setup steps, chaining patterns, and task instruction best practices.

> **LIMITATIONS**
> 
> This action doesn't support [Verified User Access](/en/agentic/agent-studio/verified-user-access), [Business Approvals](/en/agentic/agent-studio/business-approvals), or permission-aware knowledge bases, because no user is present when this action runs. Knowledge base retrieval is limited to public documents.

## Input

| Input field | Description |
| --- | --- |
| Genie | Select the genie to assign the task to. Supported only for genies whose skills don't require runtime user connections or confirmations. |
| Task description to genie | Enter a prompt describing what the genie should do. Include all context the genie needs to complete the task. Refer to [Write effective task instructions](/en/agentic/agent-studio/agent-orchestration#write-effective-task-instructions) for guidance. |
| Additional context for genie | Add up to ten files the genie can access when handling the task, in addition to public documents in its knowledge bases. |
| Additional context for genie source list | Specify a list datapill. |
| File name (Additional context for genie source list) | Map the name of the file. |
| File contents (Additional context for genie source list) | Map the contents of the file. |
| Conversation ID | Enter the ID of an existing conversation. When provided, the genie processes the task using context and history from that conversation. Leave blank for self-contained tasks like classification or summarization. Pass the Conversation ID output from a previous **Assign task to genie** step when chaining calls that must build on each other. |
| Task metadata | Specify custom key-value pairs to pass to the genie alongside task instructions. Use metadata for structured values a skill must access, such as `invoice_id` or `user_email`, rather than including these values directly in the task instructions. Any skill the genie calls can access these values as datapills, but you must define matching fields in the [Start workflow](/en/agentic/agent-studio/connectors/workato-skill-connector/start-workflow) trigger first. |
| Configure genie output for usage in this recipe | Select to allow the genie to output structured data rather than plain text. The defined fields become datapills available in downstream recipe steps. |

## Output

| Output field | Description |
| --- | --- |
| Response | The genie's final response. Returns as free-form text unless custom output fields are configured, in which case the response matches the defined schema. |
| Conversation ID | The ID of the conversation created for this task. Pass the Conversation ID datapill to subsequent **Assign task to genie** steps to maintain context across a chain of calls. |
| Tool calls | A list of all actions the genie performed to complete the task. |
| Index (Tool calls) | The position of the action in the sequence. |
| Type (Tool calls) | The type of action performed, such as a skill call or knowledge base lookup. |
| Name (Tool calls) | The name of the skill or tool that was called. |
| Timestamp (Tool calls) | The time the action was performed. |
| Status (Tool calls) | The outcome of the action. |
| Skill/RAG Tool Input (Tool calls) | The input passed to the skill or knowledge base tool. |
| Skill/RAG Tool Output (Tool calls) | The output returned by the skill or knowledge base tool. |
| List size (Tool calls) | The total number of actions in the list. |
| List index (Tool calls) | The index of the current item in the list. |
