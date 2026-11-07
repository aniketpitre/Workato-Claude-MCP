---
url: 'https://docs.workato.com/en/connectors/ai-by-workato/draft-email-action.md'
description: >-
  The Draft email action in the AI by Workato connector lets you generate
  personalized email subject lines and body content from a short description.
---

# AI by Workato - Draft email action

The draft email action allows you to create personalized emails using a visual interface without writing code. This action automates your communication workflows by simplifying the process of composing and sending customized emails to individuals or groups.

You can use this action in marketing and sales workflows to draft personalized emails. It can help with lead nurturing with different types of emails depending on the sales funnel stage, with the added user-specific context of past emails or other data. This action is also useful for marketing campaigns and event reminders that require minimal but necessary customization across various campaigns or events.

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
| Email description | Enter a description of the email you plan AI by Workato to draft. |

## Output

| Output | Description |
| --- | --- |
| Subject | The subject of the email. |
| Body | The body (main content) of the email. |
| Remaining calls (deprecated) | The number of remaining calls Workato can execute out of the overall daily quota. This field has been deprecated. |
| Consumed calls (deprecated) | The number of actions completed out of the overall daily quota. This field has been deprecated. |
| Reset time (deprecated) | The time the daily quota resets. This field has been deprecated. |

> **RATE LIMIT DEPRECATION**
> 
> Workato has removed daily usage quotas from AI by Workato actions. Refer to the AI by Workato [Quotas](/en/connectors/ai-by-workato#limits) section to see the quotas that still apply.

---
