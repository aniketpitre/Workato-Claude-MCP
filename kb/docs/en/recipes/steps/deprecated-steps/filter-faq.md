---
url: 'https://docs.workato.com/en/recipes/steps/deprecated-steps/filter-faq.md'
description: >-
  Answers to common questions about the deprecated Filter step type in Workato
  and how it affects recipes that still use it.
---

# Filter step deprecation notice

Workato has deprecated support of the **Filter** step type.

This notice covers the following frequently asked questions (FAQs):

- [What is a Filter step?](#filter-step)
- [What is the current user experience with Filter steps?](#ux-filter-steps)
- [What does this mean for users?](#ux)
- [Why is Workato making this change?](#why)
- [What happens to my recipes that use the Filter step type?](#recipes-filter-step)
- [How do I prepare?](#preparation)

## What is a Filter step?

A **Filter** step is a type of **IF condition** that begins with **If {X} then Finish**, demonstrated in the following screenshot.

![filter step](/assets/filter-step.Ju7c3IJ2.png)_Deprecated Filter step_

## What is the current user experience with Filter steps?

Currently, you cannot add **Filter** steps to your recipes using the recipe builder.

However, you can import recipes with this step type using the Recipe Lifecycle Management (RLCM) feature or APIs and run them in your workspace.

## What does this mean for users?

Moving forward, Workato will eliminate run time support for recipes containing the legacy **Filter** step type. This means that if any of your existing recipes contain **Filter** steps, Workato will display an error message when you attempt to save or start them and these types of recipes will not run.

Additionally, if you import a recipe with this step type into your workspace and run the imported recipe, an error will occur.

## Why is Workato making this change?

Workato is deprecating the **Filter** step type because it duplicates existing functionality.

## What happens to my recipes that currently use the Filter step type?

- For running recipes
  
- Workato plans to automatically update all recipes that use this step type. We plan to replace the **Filter** step with equivalent recipe logic - an **If condition** and **Stop** step type. This logic achieves the same functionality as the **Filter** step type.
  
- For stopped recipes
  
- Stopped recipes that use this step type must be updated manually.
  

The following screenshot demonstrates the resulting recipe logic after the **Filter** step type is replaced with an **If condition** and **Stop** step type.

![filter step](/assets/filter-step-replacement.BjC81tSv.png)_IF condition combined with a Stop step_

## How do I prepare?

No preparation is required, as Workato will automatically update all running recipes in your workspace with equivalent recipe logic.

However, if you prefer to handle the necessary updates yourself, you can stop your recipes and update them manually. Simply replace **Filter** steps in your recipes with an **If condition** and **Stop** steps (displayed above).

---
