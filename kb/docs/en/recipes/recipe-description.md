---
url: 'https://docs.workato.com/en/recipes/recipe-description.md'
description: >-
  Use Docs Copilot in Workato to generate recipe descriptions automatically so
  administrators and teammates can understand each recipe.
---

# Docs Copilot

Deploying a recipe to production involves multiple contributors and various activities beyond the building and testing phases. One crucial activity is documenting your recipes using detailed descriptions. These descriptions enable administrators to comprehend each recipe's functionality and assist team members in extending your recipes in the future.

Docs Copilot generates initial recipe descriptions. This allows you to concentrate more on delivery and less on documentation.

> **FEATURE AVAILABILITY**
> 
> Copilot is available for all direct customers in the US, EU, AU, JP, SG, IL, KR, and UK data centers. All data is sent to OpenAI's servers in the US. Copilot isn't available to workspaces in the CN data center. This reflects local regulatory requirements and Workato's commitment to data sovereignty and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.
> 
> You can opt in to this feature by agreeing to our [AI feature addendum](https://www.workato.com/legal/ai-feature-addendum). Contact your Customer Success representative to learn more.

## Prerequisites

- Ensure that you have **Copilot** enabled for your workspace. Enabling Copilots requires the [Environment admin](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles#environment-admin) role or the legacy [Admin](/en/roles#role-admin) system role. If you aren't assigned one of these roles, contact your workspace administrator to enable this feature. For more information, refer to our [Copilots](/en/ai-features/copilot#set-up-copilots) documentation.

> **PERMISSIONS**
> 
> Copilots do not have granular permission settings. When you enable it in your workspace, all collaborators within your workspace can access it, regardless of their role.

## Generate your recipe descriptions

After you save, test, and debug your recipe, you can use Docs Copilot to help you generate your recipe in the following situations:

- [Docs Copilot](#docs-copilot)
  - [Prerequisites](#prerequisites)
  - [Generate your recipe descriptions](#generate-your-recipe-descriptions)
    - [No recipe description is present](#no-recipe-description-is-present)
    - [Recipe description is present](#recipe-description-is-present)
  - [How it works](#how-it-works)
  - [Data usage](#data-usage)

### No recipe description is present

Complete the following steps to generate a recipe description using Docs Copilot:

1. Click **Add description** to immediately trigger Docs Copilot to generate a recipe description.
   
   ![Trigger copilot with no description](/assets/copilot-generation-no-description.CrY2BXzm.png)_Trigger copilot with no description_
   
2. Edit the description as required in the popup.
   
3. Click **Save** to include the edited description in the recipe, or **Clear description** if you choose not to use it. This description serves as a draft that you can modify as needed.
   
   ![Generate recipe description](/assets/copilot-description.D3I9I7y5.png)_Generate recipe description_
   

### Recipe description is present

Complete the following steps to generate a new recipe description using Docs Copilot:

1. Click **Edit** to open the recipe description popup.
   
   ![Trigger copilot with existing description](/assets/copilot-generation-existing-description.CkbrADEq.png)_Trigger copilot with existing description_
   
2. Use Docs Copilot to generate a new description in the popup.
   
3. Review the generated description. If it meets your requirements, **Save** it. You can revert the generation if it does not meet your requirements.
   

## How it works

Docs Copilot generates a description by receiving information about your recipe, excluding job data. Specifically, Docs Copilot uses the recipe steps, which are the individual actions and triggers that make up your recipe, the input fields where data is entered or mapped, and the applications integrated within your recipe. If your recipe calls other recipes, Docs Copilot also gathers information about those linked recipes to provide a more accurate generation.

You can improve the recipe descriptions that Docs Copilot generates by providing relevant names for all custom actions or HTTP actions in your recipe.

## Data usage

Refer to our appendix to see the data that Docs Copilot uses. [Learn more](/en/recipes/copilot-data-usage).

---
