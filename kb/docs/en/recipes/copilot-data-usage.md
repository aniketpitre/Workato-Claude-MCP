---
url: 'https://docs.workato.com/en/recipes/copilot-data-usage.md'
description: >-
  Learn what recipe data Workato Copilot uses for each feature and how privacy
  and data security are handled across Copilots.
---

# Copilots - Data usage

We prioritize your privacy and data security, selectively retrieving contextual data to ensure optimal Copilot performance. Copilot only uses data directly related to the recipes you create within Workato. This does not include any third-party application data or job logs. Specifically, recipe data is defined as recipe steps, input fields, and apps used in your recipes.

## Data usage by feature

The following is a summary of the data used for its various features:

| Feature | Data used | Example |
| --- | --- | --- |
| Recipe Copilot: Recipe generation | User prompts and data about your field structure (metadata) used in your applications. | [See example recipe generation data usage](#examples-by-feature). |
| Recipe Copilot: Add next step | User prompts, data about your field structure (metadata) used in your applications, and data about your current recipe and output fields. | [See example add next step data usage](#examples-by-feature). |
| Docs Copilot | Data about your current recipe and input fields. | [See example recipe description data usage](#examples-by-feature). |
| Formula Copilot | User prompts for formulas, data about field structure (metadata) used in your applications, and data about your current recipe steps and their expected input and output formats. | [See example Formula Copilot data usage](#examples-by-feature). |
| Mapper Copilot | User prompts for text, data about your field structure (metadata), and data about your current recipe fields and their expected input and output formats. | [See example Mapper Copilot data usage](#examples-by-feature). |
| Connector Copilot | User prompts for connector actions, API documentation, and metadata about the connectors being developed. | [See example Connector Copilot data usage](#examples-by-feature). |
| AI by Workato | Data from the input fields to create the proper output for actions such as text analysis, categorization, email drafting, parsing, and translation. | [See example AI by Workato data usage](#examples-by-feature). |

## Examples by feature

The following examples demonstrate the data usage for each Copilots feature:

**Recipe generation**

### Recipe Copilot: Recipe generation

![Example data usage for recipe generation](/assets/recipe-generation-usage.-UmR7F9L.png)_Recipe Copilot uses your prompt and the connection you select to generate a new recipe_

**Add next step**

### Recipe Copilot: Add next step

![Example data usage for add next step](/assets/add-step-usage.BYKuaSOc.png)_Recipe Copilot uses your prompt, the current recipe data, and the selected connection to suggest adding a new step_

**Docs Copilot**

### Docs Copilot

![Example data usage for Docs Copilot](/assets/recipe-description-usage.DSL2pHDn.png)_Docs Copilot uses the recipe data and data from called functions to generate a recipe description_

**Formula Copilot**

### Formula Copilot

![Example data usage for Formula Copilot](/assets/formula-data.DFDvbg0c.png)_Formula Copilot uses your prompt, field structure metadata, and recipe data to generate a formula_

**Mapper Copilot**

### Mapper Copilot

![Example data usage for Mapper Copilot](/assets/text-data-usage.BcvEkSX7.png)_Mapper Copilot uses your prompt, field structure metadata, and recipe data to generate a text input suggestion_

**Connector Copilot**

### Connector Copilot

![Example data usage for Connector Copilot](/assets/connector-data-usage.Bmjo7nkc.png)_Connector Copilot uses your prompt, API documentation, and metadata to assist in creating and refining custom connectors_

**AI by Workato**

### AI by Workato

![Example data usage for AI by Workato](/assets/ai-data-usage.BjmHUL9f.png)_AI by Workato uses data from input fields to create output for actions such as text analysis, categorization, email drafting, parsing, and translation_

---
