---
url: 'https://docs.workato.com/en/connectors/ai-by-workato.md'
description: >-
  The AI by Workato connector lets you summarize, translate, categorize, parse,
  and analyze text and draft emails using built-in AI models.
---

# AI by Workato

AI by Workato is a Workato utility connector built through our collaboration with leading AI model providers. It uses models and prompts from Anthropic and OpenAI. AI by Workato doesn't use user data for training purposes.

> **FEATURE AVAILABILITY**
> 
> AI by Workato is available for customers on specific pricing plans in the US, EU, AU, JP, SG, IL, KR, and UK data centers.
> 
> AI by Workato processes data using Anthropic's models in most regions. Workato enforces data residency in the US and EMEA by ensuring data is processed within the same region (US or EMEA) as the source data center. The SG, JP, and AU data centers process AI by Workato data within the APAC region. The Israel data center processes data in the US using OpenAI's models.
> 
> AI by Workato isn't available to workspaces in the CN data center. This reflects local regulatory requirements and Workato's commitment to data sovereignty and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.
> 
> You can opt in to this feature by agreeing to our [AI feature addendum](https://www.workato.com/legal/ai-feature-addendum). Contact your Customer Success representative to learn more.

## Enable AI by Workato in your workspace

To enable AI by Workato in your workspace, you must meet the following requirements:

- Your company has signed and agreed to Workato's AI feature addendum through DocuSign.
- You are assigned the [Environment admin](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles#environment-admin) role or the legacy [Admin](/en/roles#role-admin) system role.

> **PERMISSIONS**
> 
> AI by Workato does not have granular permission settings. When you enable it in your workspace, all collaborators within your workspace can access it, regardless of their role.

### Standard workspaces

1. Sign in to your Workato account.
   
2. Go to **Workspace admin > Settings > Workato AI**.
   
3. Ensure that AI by Workato's terms of service comply with your company's policies.
   
4. Click **Enable AI by Workato**.
   
   ![Enable AI by Workato in your workspace settings](/assets/enable-ai-by-workato.CF6kjFj2.png)_Enable AI by Workato_
   
   > **IMPACT ON WORKSPACE ENVIRONMENTS**
   > 
   > Enabling AI by Workato affects all environments within your workspace. Ensure you consider this impact before activation.
   

### AHQ workspaces

1. Sign in to your Workato account.
   
2. Go to **Workspace admin > Settings > Workato AI**.
   
3. Ensure that AI by Workato's terms of service comply with your company's policies.
   
4. Click **Enable AI by Workato**.
   
   ![Enable AI by Workato in your workspace settings](/assets/enable-ai-by-workato.CF6kjFj2.png)_Enable AI by Workato_
   
   > **IMPACT ON AHQ WORKSPACES**
   > 
   > Enabling AI by Workato in the parent AHQ workspace will automatically enable it across all associated child workspaces. AI by Workato usage can then be enabled or disabled independently in each workspace. It is enabled by default. You can restrict access of AI by Workato in child workspaces by configuring it under the [app access settings](/en/ahq-managed-workspace#settings).
   > 
   > Enabling AI by Workato affects all environments in that workspace (and associated workspaces if enabled in parent workspace) such as Development, Test, and Production. Ensure you consider this impact before activation.
   

## Supported actions

We have created common business actions that enable you to use AI in your recipes. These actions are pre-configured, allowing you to implement AI capabilities without creating or fine-tuning the prompts yourself.

Workato supports the following actions:

- [Analyze image](/en/connectors/ai-by-workato/analyze-image-action)
- [Analyze text](/en/connectors/ai-by-workato/analyze-text-action)
- [Categorize text](/en/connectors/ai-by-workato/categorize-text-action)
- [Draft email](/en/connectors/ai-by-workato/draft-email-action)
- [Parse text](/en/connectors/ai-by-workato/parse-text-action)
- [Summarize text](/en/connectors/ai-by-workato/summarize-text-action)
- [Translate text](/en/connectors/ai-by-workato/translate-text-action)

---
