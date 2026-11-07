---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/genie-governance/pii-anonymization-patterns.md
description: >-
  Learn the three layers for anonymizing PII in Agent Studio genie workflows and
  when to apply each to meet compliance requirements.
---

# PII anonymization patterns

Personally identifiable information (PII) appears throughout enterprise data. Support tickets contain customer names and contact details. HR records contain employee personal information. Sales records contain prospect data. PII categories include names, email addresses, phone numbers, national ID numbers, health data, and financial account details. Genies retrieve, process, and store this data, passing it through the LLM, which means it's processed by an external model.

This raises a compliance question for many organizations. Should PII reach the LLM at all? The answer depends on the use case, the data sensitivity, and the organization's regulatory obligations. This page covers the three layers at which PII can be managed, when to apply each layer, and how to implement layers.

## PII three-layer model

PII anonymization in genie workflows has three potential intervention points. Each operates at a different layer and serves a different purpose. The right approach uses one, two, or all three layers depending on the sensitivity of the data and the specific use case requirements.

- **Layer 1**: PII is removed or replaced before content is written to the knowledge base. The knowledge base doesn't contain PII. The LLM retrieves anonymized content.
- **Layer 2**: Skills retrieve and anonymize data from external systems before the **Return response** step sends the result to the genie. The LLM receives anonymized data and reasons about it without seeing the original PII.
- **Layer 3**: The LLM is instructed through the genie's job description to remove PII from user input or retrieved data before passing it to a skill or storing it. This is the most flexible layer but also the least reliable. It depends on LLM instruction-following rather than deterministic processing.

Guardrails PII detection works with these layers. Guardrails are a genie-level control that detect PII in user input, tool input and output, and genie output. Guardrails block, redact, or tokenize detected PII based on the handling mode you select. Refer to [Guardrails](/en/agentic/agent-studio/guardrails/guardrails) for more information, and to [Combine Guardrails and genie workflow anonymization](#combine-guardrails-and-genie-workflow-anonymization) for how Guardrails and the layers apply to a genie workflow.

## Layer 1: Anonymization before knowledge base ingestion

Review the following sections for Layer 1 anonymization before knowledge base ingestion guidelines.

### When to use Layer 1

Use Layer 1 anonymization when:

- The content to be ingested contains PII that isn't necessary for the genie's retrieval tasks
- The knowledge base is accessed by users who shouldn't see the original PII
- Regulatory requirements prohibit storing PII in an LLM-accessible vector store

**Examples**

- Ingesting closed support tickets that contain customer names and contact details. Anonymize before ingestion so the ticket content is searchable but customer PII isn't stored in the knowledge base.
- Ingesting HR records for an HR assistant knowledge base. Remove employee personal details that aren't needed for the policy retrieval use case.

### How to implement Layer 1

Layer 1 anonymization happens in the knowledge base ingestion recipe, before the content is written to the knowledge base.

Retrieve the content from the source system, add a transformation step that anonymizes it, and map the anonymized output to the knowledge base ingestion step. Use recipe formula steps or a custom code step to apply the transformation. You can route the content through an on-premises agent that runs your anonymization logic before ingestion if your source data resides in on-premises systems or you need to detect PII in unstructured text.

Common anonymization techniques at this layer include:

- **Named entity replacement**: Replace detected names, email addresses, phone numbers, and other identifiers with generic placeholders. `Jade Anderson at jade.anderson@example.com reported...` becomes `The employee at [EMAIL_REDACTED] reported...`
- **Consistent pseudonymization**: Replace PII with consistent pseudonyms rather than generic placeholders so the same person maps to the same pseudonym within a document or across related documents. This preserves the ability to reason about a specific person's history without exposing their real identity. `Customer_A` consistently refers to the same person across all ingested tickets.
- **Data minimization**: Remove fields or sections of documents that contain PII that aren't needed for the retrieval use case. A support ticket ingested for troubleshooting purposes doesn't need the customer's billing address. Remove that section entirely before ingestion.

Use an entity detection tool or service that identifies PII, such as an NLP library or a cloud PII detection API, for unstructured text. Call the service from the recipe, for example, with the HTTP connector.

### Limitations

Layer 1 anonymization is a pre-processing step. It doesn't affect PII that reaches the genie through other channels, such as skill outputs or the user's own messages in the conversation. Layer 1 only protects PII in ingested knowledge base content. Guardrails PII detection doesn't evaluate content during knowledge base ingestion.

## Layer 2: Anonymization in skill output before it reaches the LLM

Review the following sections for Layer 2 anonymization in skill output before it reaches the LLM guidelines.

### When to use Layer 2

Use Layer 2 anonymization when:

- Skills retrieve data from external systems that contains PII
- The genie doesn't need the actual PII values to complete its task, only the anonymized or aggregated information
- The organization's data governance policy prohibits passing certain PII categories to the LLM

**Examples**

- A support ticket retrieval skill fetches ticket details including customer name, email, and phone number. The genie only needs the ticket subject, description, and status for its analysis. Anonymize the customer contact fields before returning to the genie.
- An HR data skill fetches employee records that include salary, health plan enrollment, and personal address. The genie only needs the employee name and leave balance. Strip all other fields before returning.

### How to implement Layer 2

Layer 2 anonymization happens inside the skill, between the external system API call and the **Return response** step.

Retrieve data from the external system and add a data transformation step that applies anonymization before the output is mapped to the Return response step. The transformation can be implemented as:

- **Field exclusion**: Don't include PII fields in the skill's output mapping. If the genie doesn't need the customer's email address, don't include it in the return schema. This isn't anonymization in the strict sense, but it achieves the same result. The PII doesn't reach the LLM.
- **Replacement in a Workato recipe step**: Use formula steps or custom Ruby/Python functions in the recipe to replace specific field values with anonymized equivalents before mapping them to the output.
- **Custom anonymization logic**: Apply your own anonymization logic before returning the output to the genie for complex requirements, such as detecting PII in unstructured text fields like ticket descriptions or call notes. Route the output through an on-premises agent if the source data resides in an on-premises system or the logic must run inside your network. This handles cases where PII appears in free-text fields that can’t be excluded entirely.

### The output schema principle

The most reliable approach to Layer 2 anonymization is designing the skill output schema from the start to exclude PII the genie doesn't need. Returning only what the genie needs for the task is a core skill design principle. This principle has a security dimension for sensitive PII. A field excluded from the output schema is protected by design, not by anonymization.

Ask whether the genie actually needs the field before adding anonymization logic to a skill. Exclude it from the output schema if it isn't needed. Anonymization is the right approach only for fields where the genie needs the information but should receive it in anonymized form.

### Limitations

Layer 2 anonymization doesn't affect PII that users introduce into the conversation themselves. A user who types their own personal information, or a colleague's contact details, into the chat bypasses Layer 2 controls entirely. It also doesn't affect PII that the genie retrieves from the knowledge base. That is covered by Layer 1.

## Layer 3: LLM-level anonymization

Review the following sections for Layer 3 LLM-level anonymization guidelines.

### When to use Layer 3

Use Layer 3 anonymization when:

- The use case involves processing user-provided content that may contain PII before passing it to a skill or storing it
- The genie needs to strip PII from its own output before responding, for example in a summarization use case where the input contains customer data that shouldn't appear verbatim in the response
- The organization wants a defense-in-depth layer that catches PII not handled by Layers 1 and 2

Use Guardrails PII detection with or without Layer 3 if you need PII handling that doesn’t depend on the LLM following your instructions.

**Examples**

- A genie that processes customer feedback. The user pastes raw feedback text that contains customer names and contact details. The genie is instructed to anonymize the feedback before summarizing and storing it.
- A genie that summarizes call transcripts. The transcript contains customer names and contact details. The genie is instructed to replace identifiable information with generic references in the summary before passing it to a storage skill.

### How to implement Layer 3

Layer 3 anonymization is implemented through job description instructions that tell the genie to identify and replace PII before specific actions.

```plaintext

PII HANDLING

Before passing any data to a skill or
storing any content, apply the following
anonymization rules:

- Replace customer names with "the customer"
  or "Customer_[number]" if multiple customers
  are involved
- Replace email addresses with [EMAIL_REDACTED]
- Replace phone numbers with [PHONE_REDACTED]
- Replace national ID numbers, account numbers,
  and financial identifiers with [ID_REDACTED]
- Replace physical addresses with [ADDRESS_REDACTED]

Apply these replacements consistently within
a single processing task. If "Josh Hernandez"
is referred to later in the same content
as "Mr. Hernandez" or "Josh", apply the same
replacement to all references.

Do not apply anonymization to:
- The requesting user's own authenticated
  identity from the skill trigger context
- Names of employees within your organization
  when used in their professional capacity
```

### Layer 3 limitations

Layer 3 depends on the LLM following anonymization instructions consistently. LLMs are probabilistic. They occasionally miss a PII instance, apply replacements inconsistently, or fail to recognize an identifier as PII in an ambiguous context.

Layer 3 shouldn't be the only anonymization control for high-sensitivity PII. It's a defense-in-depth layer, valuable for catching cases that Layers 1 and 2 don't cover, but isn't reliable enough to stand alone. Use Guardrails PII detection and treat Layer 3 instructions as a supplement to handle PII in user input and genie output without relying on the LLM.

Apply Layer 1 or Layer 2 controls as the primary anonymization mechanism for regulated data categories, including health information, financial account data, national identity numbers, and data subject to GDPR, HIPAA, or CCPA. Use Layer 3 as a supplementary layer.

## Combine Guardrails and genie workflow anonymization

Guardrails and the three anonymization layers cover different parts of a genie workflow. Use the following table to understand where data controls apply in the Workato workflow and determine how to combine Guardrails and PII anonymization layers for your use case:

| Workflow component | Where PII appears | Layer | Guardrails |
| --- | --- | --- | --- |
| [Knowledge base ingestion](/en/agentic/agent-studio/knowledge-bases/data-ingestion) | Source documents, such as wikis, standard operating procedures, or corporate guidelines. | Layer 1 transformation step. This is the only control for this component. | Not evaluated. |
| [Skills](/en/agentic/skills#getting-started-with-skills) | Data returned from external systems. | Layer 2 field exclusion or transformation before **Return response**. This is the primary control. | Detects PII in tool output as an additional control. |
| [Conversation](/en/agentic/agent-studio/conversations) | User input and genie output. | Layer 3 job description instructions as a supplement. | Primary control. Detects PII in user input and genie output. |

### Choose a Guardrails handling mode

Each PII type you detect uses one of the following handling modes. Choose the mode based on what the genie needs to do with the value.

| Guardrails mode | Use case |
| --- | --- |
| [Block](/en/agentic/agent-studio/guardrails/guardrails#handling-modes) | The genie doesn't need the value. The genie refuses the request and the user must remove the PII. |
| [Redact](/en/agentic/agent-studio/guardrails/guardrails#handling-modes) | The genie requires the surrounding context but not the value. |
| [Tokenize](/en/agentic/agent-studio/guardrails/guardrails#tokenization-behavior) | The genie must reason about or return the value, such as referencing a customer's email in a reply. |
| [Log Only](/en/agentic/agent-studio/guardrails/guardrails#handling-modes) | Measure detection in the debug trace before you enforce a stricter mode. |

### Example support ticket genie use case

A support genie answers questions using closed tickets and looks up open tickets through a skill. Apply controls as follows:

- **Knowledge ingestion with Layer 1**: Add a formula step that masks email addresses in the ticket body before the knowledge base step. For example, `description.gsub(/[\w.+-]+@[\w-]+\.[\w.]+/, "[EMAIL_REDACTED]")`, where `description` is the ticket body datapill.
- **Ticket lookup skill with Layer 2**: Return only `subject`, `description`, and `status` in the **Return response** schema. Exclude `customer_name`, `email`, and `phone`.
- **Guardrails**: Keep the default high-risk PII types, such as Social Security numbers and credit card numbers, set to **Block**. Turn on **Email addresses** and set it to **Tokenize** to allow users to paste an email into the chat for the genie to use in a reply without the LLM seeing the address.
- **Job description with Layer 3**: Add the PII handling instructions from [How to implement Layer 3](#how-to-implement-layer-3) as a supplement for identifiers that Guardrails don’t cover, such as names if you haven’t enabled that PII type, or organization-specific data not matched by a [custom regex pattern](/en/agentic/agent-studio/guardrails/guardrails#custom-regex-patterns).

Review the **Input Guardrails** and **Output Guardrails** steps in the debug trace to confirm which PII was detected and how it was handled. Review the job details for the skill recipe to confirm the **Return response** output.

## Choose the right layers for your use case

The right combination of layers depends on the sensitivity of the data, the regulatory requirements, and where in the workflow PII appears.

Use the following table to help you choose the right layers for your use case:

| PII source | Recommended layer | Notes |
| --- | --- | --- |
| Knowledge base content ingested from documents | Layer 1 | Anonymize in the ingestion recipe before content is written to the knowledge base. |
| Structured data returned by skills | Layer 2 | Exclude unnecessary PII fields from output schema and apply replacements for required but sensitive fields. |
| Free-text fields in skill output, such as descriptions or notes | Layer 2 | Apply anonymization logic before returning to the genie. Use an on-premises agent if the data or processing must stay inside your network. |
| User-provided content in conversation | Guardrails with Layer 3 as supplemental layer | Use Guardrails PII detection to handle PII before it reaches the LLM. Add job description instructions as a supplement. Also apply Layer 2 if the content is passed to a skill. |
| PII in genie output, such as summaries or reports | Guardrails with Layer 3 as supplemental layer | LLM instruction to anonymize before responding. |
| Regulated health or financial data | Layers 1 and 2 with Guardrails | Don't rely on Layer 3 only for regulated data categories. Use a combination of layers and Guardrails. |

## Test anonymization in production

Test anonymization controls with realistic data containing actual PII patterns before deploying a genie that handles PII. A test that uses `[CUSTOMER_NAME]` as the test PII won't reveal whether the anonymization logic handles `Dr. Sarah Williams` correctly.

Test each layer independently:

- **Layer 1**: Ingest the data and search the knowledge base for known PII from the source content and verify it has been replaced or removed.
- **Layer 2**: Call the skill directly in a test recipe with realistic source data and inspect the output to confirm PII fields are excluded or replaced before the **Return response** step.
- **Layer 3**: Switch to **Test** mode and provide the genie with content containing realistic PII patterns and ask it to summarize or process the content. Inspect the response and the skill inputs to confirm PII was handled according to the instructions.
