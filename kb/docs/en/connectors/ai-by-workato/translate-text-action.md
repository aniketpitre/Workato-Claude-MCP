---
url: 'https://docs.workato.com/en/connectors/ai-by-workato/translate-text-action.md'
description: >-
  The Translate text action in the AI by Workato connector lets you
  automatically translate source text from one language into another.
---

# AI by Workato - Translate text action

The translate text action empowers you to automatically translate text from one language to another, enabling efficient communication across language barriers. With this action, you can automate the translation process and easily incorporate multilingual capabilities into your workflows.

Users can easily translate support tickets or inquiries from different languages into a common language, and generate localized content for websites and documents. It can also help with changing marketing assets across languages with ease.

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
| Output language | Select or type in the language to which you plan to translate your text. |
| Source language | Select or type in the language of your source text. |
| Source text | Provide the text you plan to translate. Limit your source text to 2000 tokens. |

## Output

| Output | Description |
| --- | --- |
| Translated text | The translated text. This should be in the specified output language. |
| Remaining calls (deprecated) | The number of remaining calls Workato can execute out of the overall daily quota. This field has been deprecated. |
| Consumed calls (deprecated) | The number of actions completed out of the overall daily quota. This field has been deprecated. |
| Reset time (deprecated) | The time the daily quota resets. This field has been deprecated. |

> **RATE LIMIT DEPRECATION**
> 
> Workato has removed daily usage quotas from AI by Workato actions. Refer to the AI by Workato [Quotas](/en/connectors/ai-by-workato#limits) section to see the quotas that still apply.

---
