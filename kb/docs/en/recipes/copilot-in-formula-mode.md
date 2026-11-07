---
url: 'https://docs.workato.com/en/recipes/copilot-in-formula-mode.md'
description: >-
  Use Formula Copilot to get AI-powered formula suggestions in Workato recipes,
  building data transformations and formatting from prompts.
---

# Formula Copilot

Workato’s Formula Copilot leverages Large Language Models (LLMs) to enhance your experience in formula mode. This AI-powered feature provides assistance based on your formula requirements. You can create complex data transformations or fine-tune your formatting by directly prompting Copilot, which offers tailored suggestions and examples.

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

## Get started with Formula Copilot

Workato’s Formula Copilot offers various ways to assist you in formula mode, depending on your specific situation in the recipe.

### Direct assistance from Formula Copilot

When starting a new or empty formula field, complete the following steps to get direct help from Formula Copilot:

1. Navigate to any trigger or action step within your recipe that requires data transformation.
   
2. Click on the **Formula** tab in the input field to dynamically set values based on your recipe data.
   
   ![Formula tab](/assets/formula-mode-tab.Ctyg05s-.png)_Navigate to the **Formula** tab_
   
3. Select the **Ask Copilot to fill field** button within the formula box for empty fields to allow Formula Copilot to generate your formula.
   
   ![Ask Copilot tab](/assets/ask-copilot-tab.DiQ6K5AL.png)_Ask Formula Copilot to fill the input field_
   

### Overcome formula creation challenges

If you encounter difficulties while creating a formula, complete the following steps for additional assistance from Formula Copilot:

1. Click on the **Formula** tab and begin formulating your input.
   
2. Click **Ask Copilot for help** if your input results in no function matches, indicated by **No functions match your search**.
   
   ![Ask Copilot for help](/assets/ask-copilot-help.ByZbpP63.png)_Ask Formula Copilot for help when no function matches_
   

### Hide Formula Copilot

Click **Hide** at any point to minimize the Formula Copilot dialog. To restore the Formula Copilot interface, press **Shift + Space**.

![Restore the Copilot interface](/assets/shift-space.DGDYfNng.png)_Press **Shift + Space** to restore the Formula Copilot interface_

### Quick formula editing with Formula Copilot

When fine-tuning formulas, you can click the white box within any formula field to activate Formula Copilot. This feature ensures Formula Copilot is readily accessible to streamline your formula editing process.

![Activate Copilot for field editing](/assets/activate-copilot-box.BCokMyBS.png)_Click the white box to activate Formula Copilot for formula assistance_

## Generate formula suggestions

After you activate Formula Copilot in formula mode, you can start generating specific formula prompts.

> **HOW FORMULA COPILOT INTERPRETS DATA**
> 
> When generating formulas, Formula Copilot adjusts its approach based on the data present in the formula field:
> 
> - No input or generation: Formula Copilot only takes into account the prompt and the recipe.
> - Input present: Formula Copilot takes into account the existing input, the prompt, and the recipe.
> - Generation present: Formula Copilot takes into account the generation, the prompt, and the recipe.
> - Input and generation present: Formula Copilot only takes into account the generation, the prompt and the recipe.

1. Type your formula requirements or a description of the transformation you require directly into the prompt. Select the **Back** option if you plan to revise your input or view previous suggestions.
   
   ![Generate prompt](/assets/generating-prompt.t-hpJRrL.png)_Generate a formula prompt in Formula Copilot_
   
2. Click the green arrow to begin the formula generation process. The system will display **Generating input…**, indicating that it is processing your input for suggestions. You can also select **Stop** to cancel the process.
   
   ![Generate input](/assets/generating-input.CY0zjxb3.png)_Generate the formula in Formula Copilot_
   
3. Examine the formula suggestion that Formula Copilot generates to ensure that the formula meets your transformation requirements.
   
4. **Insert** the suggested formula directly into your formula field or click **Copy** to clipboard to use it in another part of your recipe.
   
   ![Insert the generated formula](/assets/insert-formula.D3xXH_rD.png)_Insert the generated formula into the input field_
   
5. Use the provided suggestion or [refine](#refine-existing-input-or-formula-copilot-generated-formulas) it to ensure it aligns with your specific data needs and preferred output format.
   

### Refine existing input or Formula Copilot-generated formulas

If you already have input in the formula field or need to refine a formula generated by Formula Copilot, complete the following steps to tailor the suggestions to your requirements:

1. Activate Formula Copilot by clicking **Fill field with AI** in the formula box. This step is crucial whether you're starting with a datapill, have existing input, or are refining a formula previously generated by Formula Copilot.
   
   ![Activate Copilot](/assets/update-formula.BLpWnMbZ.png)_Activate Formula Copilot for updating the formula prompt_
   
2. Enter your specific requirements in the prompt to customize the formula suggestion.
   
   ![Provide new prompt](/assets/type-new-prompt.DwsOhsHY.png)_Type the new requirements for the formula_
   
3. Examine the AI-generated formula suggestion to ensure it matches your intended output.
   
   ![Review the generated formula](/assets/review-updated-formula.DRgpwZ91.png)_Review the updated formula suggestion_
   
4. Select **Replace** to adjust the formula.
   
   ![Replace the formula](/assets/replaced-formula.DMyuCnKW.png)_Replace the formula_
   

### Map step outputs with formula mode

Workato's formula mode allows you to map outputs from one step to another within your recipes:

1. Switch to **Formula** mode in the input field where you plan to map the output from a previous step.
   
2. Type your mapping requirements in the prompt to automatically select the corresponding datapills from previous steps.
   
   ![Type your mapping requirements](/assets/type-mapping.eBb9dx_-.png)_Type your mapping requirements in Formula Copilot_
   
3. Click **Insert** to map them to your current step’s field or click **Copy** to clipboard for use in another part of your recipe.
   
   ![Insert mapping](/assets/insert-mapping.DbkUkvLU.png)_Insert mapped output into the formula field_
   
4. Edit the formula directly in the formula box or click **Ask Copilot for help** if you need assistance to refine the mapping.
   
   ![Edit formula mapping](/assets/mapped-formula.DYYfGMBs.png)_Edit the mapped formula in Formula Copilot_
   

### Remap unknown datapills

If Formula Copilot does not find similar datapills for your formula, complete one of the following options:

- **Delete** the unmatched datapill and manually select a replacement from the data tree.
- Select **Ask Copilot for help** to get AI-assisted suggestions for remapping the datapills.

![Handle unknown datapills](/assets/unmatched-datapills.CTyfZCBR.png)_Remap unknown datapills in Formula Copilot_

Following these steps ensures that your formula accurately references the correct datapills within your recipes.

## Use formula recommendations

When you insert a datapill in formula mode, Formula Copilot provides recommendations for functions in the input field. If you type a recognized function, such as `.where`, the footer displays a direct link to that function's detailed explanation in Workato's [formula documentation](/en/formulas). For additional support, you can click **Fill field with AI** in the footer to prompt Formula Copilot to generate a relevant formula for your needs.

![Link to formula documentation](/assets/formula-recommendations.wuqKVVZF.png)_Link to a function in Workato’s formula documentation_

## Data usage

For details on the data Formula Copilot uses, refer to our appendix. For more information, refer to our [data usage](/en/recipes/copilot-data-usage) documentation.

## Limitations

Copilot is designed to support a wide range of automation tasks, but there may be complex scenarios that require manual setup. For these cases, refer to Workato's [formula documentation](/en/formulas).

---
