---
url: 'https://docs.workato.com/en/connectors/ai-by-workato/summarize-text-action.md'
description: >-
  The Summarize text action in the AI by Workato connector lets you condense
  long text into concise summaries with a defined maximum word count.
---

# AI by Workato - Summarize text action

The summarize text action allows you to summarize long textual information easily. This action enables you to obtain summaries from any source and define the length of the output summary.

This action is versatile and can be used to augment multiple workflows across various departments within an organization. For example, you can use this action in sales workflows to summarize call transcripts and long email threads. Customer support teams can also use this action to quickly summarize long support tickets or product release notes into concise bullet points.

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
| Source text | Enter the text you plan to summarize. The quota is 2000 tokens. |
| Maximum words | Specify the maximum number of words to include in the summary. If left blank, it will default to 200 words. |

## Output

| Output | Description |
| --- | --- |
| Summary | Summarized text returned by OpenAI. |
| Remaining calls (deprecated) | The number of remaining calls Workato can execute out of the overall daily quota. This field has been deprecated. |
| Consumed calls (deprecated) | The number of actions completed out of the overall daily quota. This field has been deprecated. |
| Reset time (deprecated) | The time the daily quota resets. This field has been deprecated. |

> **RATE LIMIT DEPRECATION**
> 
> Workato has removed daily usage quotas from AI by Workato actions. Refer to the AI by Workato [Quotas](/en/connectors/ai-by-workato#limits) section to see the quotas that still apply.

---
