---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/app-events-vs-agent-orchestration.md
description: >-
  Determine when to use App Events or Agent orchestration based on specific use
  cases.
---

# App Events vs Agent orchestration

Use this documentation to determine whether App Events or the **Assign task to genie** action is the right tool for your use case.

Ask yourself: **Does a user need to receive a message and potentially take action?**

- **Yes**: Use App Events
- **No**: Use the **Assign task to genie** action

**App Events** require a user. The genie reaches out to a specific, identified user through the chat interface. The user receives the message, responds, and the conversation continues.

**Assign task to genie** doesn't require a user. The genie processes a task in the background by reasoning, calling skills, and returning a structured result to the recipe. No conversation thread is created.

## When to use App Events

Use App Events when:

- A user needs to be informed and may need to take action. For example, a ticket they created was updated, or a renewal opportunity is approaching.
- User judgment is required mid-process. The genie presents context and options and the user decides.
- The downstream skill requires [Verified User Access](/en/agentic/agent-studio/verified-user-access). Verified user access requires an active user session.
- The flow involves [Business Approvals](/en/agentic/agent-studio/business-approvals). Approval notifications surface in the user's chat interface and require user interaction.
- The genie needs to initiate a conversation proactively. For example, scheduled reminders or event-triggered alerts.

App Events can't return a structured value to a recipe. The recipe continues immediately after sending the event without waiting for the genie to finish.

## When to use Assign task to genie

Use the **Assign task to genie** action when:

- Processing is automated and the result feeds back into the recipe. For example, classifying a ticket, summarizing a document, or extracting invoice data.
- No user is present or needed. For example, background jobs or system-to-system integrations.
- The genie's output is structured data, not a message to a user.
- Multiple genies need to collaborate in a pipeline. An orchestrating recipe can assign tasks to specialist genies in sequence, collecting structured outputs from each.

The **Assign task to genie** action can't be used with:

- [Verified User Access](/en/agentic/agent-studio/verified-user-access) because there's no user context in a headless invocation.
- [Business Approvals](/en/agentic/agent-studio/business-approvals) because approval notifications are delivered through the user's chat interface.
- Permission-aware knowledge bases because knowledge bases ingested with user-scoped permissions don't enforce those permissions without a user context.

These are platform constraints, not configuration choices.

## App Events and Assign task to genie comparison

Use the following comparison to determine which feature to use:

|  | App Events | Assign task to genie |
| --- | --- | --- |
| User required | Yes ✅ | No ❌ |
| Recipe pauses and waits | No ❌ | Yes ✅ |
| Structured output to recipe | No ❌ | Yes ✅ |
| Verified user access supported | Yes ✅ | No ❌ |
| Business Approvals | Yes ✅ | No ❌ |
| Conversational follow-up | Yes ✅ | No ❌ |

## Combine both features

The most powerful architectures combine both features in sequence.

A recipe uses **Assign task to genie** for automated reasoning, such as classifying a ticket or evaluating escalation criteria. The structured result allows the recipe to use **App Events** to notify the relevant user and start a conversation. The reasoning is automated while the decision is determined by a user.

## Common mistakes

- **Using App Events where Assign task to genie should be used**: A builder needs to classify incoming support tickets automatically. The builder uses App Events to send each ticket to an agent and wait for a classification response. This creates a conversation thread for every ticket and fills agents' chat interfaces with genie messages. The **Assign task to genie** action, which doesn't require user involvement, should be used in this case.
  
- **Using Assign task to genie where App Events should be used**: A builder needs to notify sales reps when a renewal opportunity approaches. The builder uses the **Assign task to genie** action to process the renewal event and return a summary as a datapill. The sales rep doesn't receive the notification because the **Assign task to genie** action doesn't start a conversation in the chat interface the way App Events do.
  

## Use case recommendations

Refer to the following use case recommendations to help you choose the correct feature for your workflow:

| Use case | Feature | Reason |
| --- | --- | --- |
| Categorize tickets from an email webhook | Assign task to genie | Automated output with no user interaction required |
| Notify a sales rep of a renewal 30 days out | App Events | Rep needs to receive the message and may act |
| Summarize a contract and extract key clauses | Assign task to genie | Automated output feeds downstream recipe |
| Alert an IT engineer about a P1 incident | App Events | Engineer decides whether to escalate |
| Evaluate whether a ticket meets escalation criteria | Assign task to genie | Automated reasoning with output that feeds conditional logic |
| Notify a user their ticket was updated | App Events | Specific user needs to receive a message |
| Generate a weekly pipeline summary per rep | App Events | Each rep receives a personalized message in the chat interface |
| Extract structured data from an invoice PDF | Assign task to genie | Automated extraction with structured output to recipe |
