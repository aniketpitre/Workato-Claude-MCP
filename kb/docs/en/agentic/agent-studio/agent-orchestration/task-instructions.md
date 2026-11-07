---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/agent-orchestration/task-instructions.md
description: Learn best practices for Assign task to genie instructions.
---

# Task instructions

Task instructions for the **Assign task to genie** action have different requirements than conversational genie prompts. The genie is completing a defined task and returning a result rather than having a conversation.

## Be specific about the goal

State the goal of the task in the first sentence. The genie should know immediately what it's being asked to produce. A task instruction produces a conversational response rather than a structured classification.

| ❌ Not recommended | ✅ Recommended |
| --- | --- |
| `help with this ticket` | `Evaluate the following support ticket and return a classification including category, priority, and a one-sentence reasoning.` |

## Pass required context in the instructions or metadata

The genie can't ask a user for missing information. You must add required data, such as a ticket description, account name, or a document to summarize, to the task instructions or in the metadata fields. Pass structured values as metadata. Pass unstructured content, such as document text, transcript content, or description fields, directly in the task instructions as labeled fields.

For example:

```plaintext
Ticket details:
- Subject: [Subject datapill]
- Description: [Description datapill]
- Priority: [Priority datapill]
- Submitter: [Submitter Email datapill]
- Category (current): [Category datapill]
```

## Specify the output format

Provide an exact format for the genie to use in its response. The genie follows the schema automatically for tasks with configured custom output fields. You must specify the format in the instructions for tasks that don't have custom output field configuration. Explicit output format instructions are essential for tasks where the recipe must parse and use the genie's response. A genie that returns `I think this should be categorized as Hardware with P2 priority because...` requires regex parsing. A genie that returns a clean JSON object doesn't require parsing.

For example:

```plaintext
Return your response as a JSON object with
the following fields only:
{
  "category": "one of: Hardware, Software,
               Access, Network, Other",
  "priority": "one of: P1, P2, P3, P4",
  "reasoning": "one sentence explanation",
  "confidence": "one of: high, medium, low"
}

Do not include any text outside the JSON
object. Do not add fields not listed above.
```

## Provide evaluation criteria for judgment tasks

Provide explicit criteria for tasks that require the genie to make a judgment, such as classification, scoring, or evaluations. Vague criteria produce inconsistent results across runs, while anchored criteria produce consistent, reliable outputs.

For example:

```plaintext
Classification criteria:

Hardware: issues involving physical devices,
peripherals, or hardware failures

Software: issues involving application errors,
software installation, or software access

Access: issues involving login failures,
password resets, or permission requests

Network: issues involving connectivity, VPN,
or network performance

Priority criteria:
P1: business-critical system down, affecting
    multiple users, no workaround available
P2: significant impact, workaround available
    but inconvenient
P3: moderate impact, reasonable workaround
    available
P4: minor issue, minimal business impact
```

## Instruct the genie to use only the data you provide

The genie may supplement the data you provide with its own reasoning or general knowledge without this instruction. The genie should base its output only on what was provided for classification and evaluation tasks where accuracy and consistency matter.

For example:

```plaintext
Base your classification only on the ticket
details provided above. Do not use assumptions
or general knowledge about typical ticket
patterns. If the provided information is
insufficient to make a confident classification,
set confidence to "low" and explain why in
the reasoning field.
```

The following example provides a complete set of task instructions for a support ticket classification task:

```plaintext
Classify the following support ticket and
return a structured classification result.

Ticket details:
- Subject: [Subject datapill]
- Description: [Description datapill]
- Current priority: [Priority datapill]
- Submitter: [Submitter Email datapill]

Classification criteria:

Category:
- Hardware: physical devices, peripherals,
  hardware failures
- Software: application errors, installation,
  software access
- Access: login failures, password resets,
  permission requests
- Network: connectivity, VPN, network performance
- Other: does not fit the above categories
Priority:
- P1: business-critical system down,
  multiple users affected, no workaround
- P2: significant impact, workaround
  available but inconvenient
- P3: moderate impact, reasonable
  workaround available
- P4: minor issue, minimal business impact

Return your response as a JSON object:
{
  "category": "Hardware|Software|Access|
               Network|Other",
  "recommended_priority": "P1|P2|P3|P4",
  "priority_change_needed": true|false,
  "reasoning": "one sentence",
  "confidence": "high|medium|low"
}

Base your classification only on the ticket
details above. Set confidence to "low" if
the information is insufficient for a
confident classification.
```
