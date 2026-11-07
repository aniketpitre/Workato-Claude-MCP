---
url: 'https://docs.workato.com/en/connectors/ai-by-workato/parse-text-action.md'
description: >-
  The Parse text action in the AI by Workato connector extracts structured data
  such as names, dates, and addresses from unstructured text.
---

# AI by Workato - Parse text action

The parse text action enables you to extract structured data from unstructured text without requiring any coding skills. It allows you to identify and extract specific information from text documents, emails, or other textual sources. This information can include names, addresses, dates, product details, and more.

You can use this action as part of your lead generation workflows to extract customer information from incoming text messages, chat conversations, or social media posts to capture and categorize leads.

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
| Source text | Provide the text you plan to parse. |
| Fields to identify | Determine the fields that you plan to identify from the text by providing the name and description of the field. Descriptions provide additional information to help Workato extract the fields. |

## Output

The output of this action is dynamic and depends on how you've configured the **Fields to identify** section of the input. For example, if you configure this action to identify **Customer emails**, **Phone numbers**, and **Names** Workato generates Customer emails, Phone numbers, and Names datapills as output.

Additionally, Workato provides the following output for this action.

| Output | Description |
| --- | --- |
| Remaining calls (deprecated) | The number of remaining calls Workato can execute out of the overall daily quota. This field has been deprecated. |
| Consumed calls (deprecated) | The number of actions completed out of the overall daily quota. This field has been deprecated. |
| Reset time (deprecated) | The time the daily quota resets. This field has been deprecated. |

> **RATE LIMIT DEPRECATION**
> 
> Workato has removed daily usage quotas from AI by Workato actions. Refer to the AI by Workato [Quotas](/en/connectors/ai-by-workato#limits) section to see the quotas that still apply.

---
