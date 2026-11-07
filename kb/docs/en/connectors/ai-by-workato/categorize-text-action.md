---
url: 'https://docs.workato.com/en/connectors/ai-by-workato/categorize-text-action.md'
description: >-
  The Categorize text action in the AI by Workato connector lets you classify or
  sort text into predefined categories for routing, tagging, and filtering.
---

# AI by Workato - Categorize text action

The categorize text action enables you to classify or organize text data based on predefined categories automatically. For common categories, you can omit the rules, but in general, we recommend configuring a clear rule description to aid with classification.

This action allows you to efficiently sort, group, or route incoming text information to streamline your business processes. Some possible workflows it can augment are customer support ticket routing, content tagging, spam filtering, and product classification.

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
| Text | Provide the text you plan the connector to categorize. |
| List of categories | Create a list of categories to sort the text into. Create rules to provide additional details to help classify what each category represents. |

## Output

| Output | Description |
| --- | --- |
| Best match category | This action chooses one of the categories that fits the input text. The output datapill contains the value of the closest match category or error if none of the categories you define are found in the source text. If you plan to have an option for none, you must configure it explicitly. |
| Remaining calls (deprecated) | The number of remaining calls Workato can execute out of the overall daily quota. This field has been deprecated. |
| Consumed calls (deprecated) | The number of actions completed out of the overall daily quota. This field has been deprecated. |
| Reset time (deprecated) | The time the daily quota resets. This field has been deprecated. |

> **RATE LIMIT DEPRECATION**
> 
> Workato has removed daily usage quotas from AI by Workato actions. Refer to the AI by Workato [Quotas](/en/connectors/ai-by-workato#limits) section to see the quotas that still apply.

---
