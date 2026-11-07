---
url: 'https://docs.workato.com/en/recipes/copilot-in-text-mode.md'
description: >-
  Use Mapper Copilot for AI-powered text help in Workato recipes, composing text
  with datapills and searching pills directly in the editor.
---

# Mapper Copilot

Workato's Mapper Copilot enhances text manipulation in your recipes by providing AI-powered assistance directly within the recipe editor. You can use this feature to compose text that incorporates datapills, such as drafting emails, Slack notifications, or descriptions for invoices. This page details how to use Mapper Copilot to handle regular inputs and manipulate English text effectively. Additionally, Mapper Copilot allows you to quickly search and select from thousands of datapills in a recipe for accurate data handling.

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

## Get started with Mapper Copilot

Mapper Copilot allows you to generate and manipulate input fields within your recipes. Complete the following steps to activate and use Mapper Copilot:

1. Navigate to any recipe action or trigger step where you require text manipulation.
   
2. Click the **Text** tab in the input field where you plan to insert or edit text. An icon displays indicating that you can activate input suggestions if Mapper Copilot is enabled.
   
   ![Formula tab](/assets/text-tab.C0gX4xXo.png)_Navigate to the **Text** tab_
   
3. Activate Mapper Copilot by clicking the suggested icon.
   
   ![Activate copilot](/assets/copilot-tab.C4MqOOFC.png)_Activate Mapper Copilot_
   

### Select input suggestions

Click an input field where you plan to insert data to display a suggested input menu with options based on the preceding actions in your recipe.

![Select input data](/assets/input-data.8lpJZY_h.png)_Select suggested input_

You can choose an option from the suggested input menu to map relevant datapills. Click **Fill field with AI instead** at the bottom of the input menu if the suggestions are not suitable. This option activates Mapper Copilot to generate new, customized input suggestions.

## Generate input suggestions

You can start generating specific text prompts after you activate Mapper Copilot in text mode.

> **HOW MAPPER COPILOT INTERPRETS DATA**
> 
> Mapper Copilot adjusts its approach when generating input suggestions based on the data present in the text field:
> 
> - No input or generation: Mapper Copilot only takes into account the prompt and the recipe.
> - Input present: Mapper Copilot takes into account the existing input, the prompt, and the recipe.
> - Generation present: Mapper Copilot takes into account the generation, the prompt, and the recipe.
> - Input and generation present: Mapper Copilot only takes into account the generation, the prompt, and the recipe.

1. Type your text requirements or a description of the transformation you require directly into the prompt. Select the **Back** option if you plan to revise your input or view previous suggestions.
   
   ![Generate prompt](/assets/generating-text-prompt.Ba0Yr_rN.png)_Generate a text prompt in Mapper Copilot_
   
2. Click the green arrow to begin the input generation process. The system begins to display **Generating input…**, indicating that it is processing your input for suggestions. You can also select **Stop** to cancel the process.
   
   ![Generate input](/assets/generating-text-input.DNVtCrUx.png)_Generate the input suggestion in Mapper Copilot_
   
3. Examine the input suggestion that Mapper Copilot generates to ensure that it meets your transformation requirements.
   
4. **Insert** the suggestion directly into your input field or click **Copy** to clipboard to use it in another part of your recipe.
   
   ![Insert the generated formula](/assets/insert-input.lcYB-Dza.png)_Insert the generated suggestion into the input field_
   
5. Use the provided suggestion or [refine](#refine-existing-input-or-mapper-copilot-generated-suggestions) it to ensure it aligns with your specific data needs and preferred output format.
   

### Refine existing input or Mapper Copilot-generated suggestions

You can tailor existing input in the text field or refine an input suggestion generated by Mapper Copilot. Complete the following steps to update Mapper Copilot suggestions to meet your requirements:

1. Click the Mapper Copilot icon again in the text box. This action allows you to update the prompt for a new suggestion.
   
   ![Activate Copilot](/assets/update-text.Dn4A3VJe.png)_Activate Mapper Copilot to update the input suggestion_
   
2. Type your updated prompt to refine the suggestion.
   
   ![Provide new prompt](/assets/type-new-text.BSraD9fW.png)_Type the new requirements for the text_
   
3. Examine the input suggestion to ensure it matches your intended output.
   
   ![Review the generated formula](/assets/review-updated-text.CB5l1MHh.png)_Review the updated formula suggestion_
   
4. Select **Replace** to replace the previous suggestion with the new suggestion.
   

### Map datapills in text mode

Mapper Copilot simplifies the process of locating and using datapills within your recipes, making it an essential tool for managing large datasets:

1. Switch to **Text** mode in the input field where you plan to insert datapills.
   
2. Type your datapill requirements in the prompt. Mapper Copilot dynamically suggests relevant datapills based on your input.
   
   ![Search Datapills](/assets/search-datapills.q8Z8nqcE.png)_Find datapills in Mapper Copilot_
   
3. Click **Insert** to map the datapills to your current step’s field or click **Copy to clipboard** to use the datapills in another part of your recipe.
   
   ![Select Datapills](/assets/select-datapills.BTK8RPZh.png)_Insert datapills_
   
4. Use Mapper Copilot's text manipulation features to modify or format the datapills within the input field.
   
   ![Refine Datapills](/assets/refine-datapills.CAWdrRUA.png)_Refine and use datapills_
   

### Remap unknown suggestions

You can remap unknown suggestions if Mapper Copilot cannot find similar datapills for your input. Complete one of the following options to remap unknown suggestions:

- **Delete** the unmatched datapill and manually select a replacement from the data tree.
- Select **Ask Copilot for help** to receive AI-assisted suggestions for remapping the datapills.

![Replace the formula](/assets/remap-datapills.CPXEy3Ym.png)_Remap unknown datapills in Mapper Copilot_

Following these steps ensures that your input accurately references the correct datapills within your recipes.

### Tips for effective use

- **Include relevant datapills**: Include the necessary datapills in the input field for accurate suggestions. The datapills you select provide Mapper Copilot with context, enabling you to generate precise text transformations.
  
- **Be specific in prompts**: Provide clear and specific instructions in your prompt for Mapper Copilot to generate more accurate suggestions. Specify the format or transformation you plan to use explicitly.
  
- **Leverage contextual data**: Use related data from preceding steps to give Mapper Copilot comprehensive context for generating accurate and relevant suggestions.
  

## Data usage

Refer to our appendix to see [how Mapper Copilot uses your data](/en/recipes/copilot-data-usage).

## Limitations

Mapper Copilot is designed to support a wide range of automation tasks, but complex scenarios may require manual setup. Refer to Workato's [datapills documentation](/en/recipes/data-pills-and-mapping) for these cases.

---
