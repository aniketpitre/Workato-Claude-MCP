---
url: 'https://docs.workato.com/en/connectors/ai-by-workato/analyze-text-action.md'
description: >-
  The Analyze text action in the AI by Workato connector extracts specific
  information from a piece of text based on the instructions you provide.
---

# AI by Workato - Analyze text action

Use the **Analyze text** action to understand specific information from a given piece of text. This action facilitates knowledge retrieval tasks and prioritizes the importance of the provided input. The action outputs an empty datapill if there is no answer found in the text.

Some common use cases include content summarization and sentiment analysis. A user can generate action items from a meeting transcript, title and hints for documents, and even descriptions for technical briefs.

The **Analyze text** action may return an `Unable to analyse the document provided` error when your input instructions contain certain words or phrases, even in legitimate business contexts. For example:

- `Outline the plan for cutting costs`
- `Summarize steps to kill a program running on a port`
- Other sensitive words or profanity

Rephrase your instructions to avoid sensitive words. For example:

- Use `stop process` or `terminate program` instead of `kill program`
- Use `reducing costs` or `optimizing costs` instead of `cutting costs`

> **FEATURE AVAILABILITY**
> 
> AI by Workato is available for customers on specific pricing plans in the US, EU, AU, JP, SG, IL, KR, and UK data centers.
> 
> AI by Workato processes data using Anthropic's models in most regions. Workato enforces data residency in the US and EMEA by ensuring data is processed within the same region (US or EMEA) as the source data center. The SG, JP, and AU data centers process AI by Workato data within the APAC region. The Israel data center processes data in the US using OpenAI's models.
> 
> AI by Workato isn't available to workspaces in the CN data center. This reflects local regulatory requirements and Workato's commitment to data sovereignty and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.
> 
> You can opt in to this feature by agreeing to our [AI feature addendum](https://www.workato.com/legal/ai-feature-addendum). Contact your Customer Success representative to learn more.

## Input

| Input field | Description |
| --- | --- |
| Source text | Provide the source text you plan to analyze. |
| Instruction | Provide instructions on how to analyze your source text. For example, this could be an analytic technique or question you want answered. |

## Output

| Output | Description |
| --- | --- |
| Analysis result | The result of the action. The output is determined by the instructions you provide. |
| Remaining calls (deprecated) | The number of remaining calls Workato can execute out of the overall daily quota. This field has been deprecated. |
| Consumed calls (deprecated) | The number of actions completed out of the overall daily quota. This field has been deprecated. |
| Reset time (deprecated) | The time the daily quota resets. This field has been deprecated. |

> **RATE LIMIT DEPRECATION**
> 
> Workato has removed daily usage quotas from AI by Workato actions. Refer to the AI by Workato [Quotas](/en/connectors/ai-by-workato#limits) section to see the quotas that still apply.

---
