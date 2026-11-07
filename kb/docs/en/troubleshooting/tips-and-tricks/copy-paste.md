---
url: 'https://docs.workato.com/en/troubleshooting/tips-and-tricks/copy-paste.md'
description: >-
  Learn how to copy and paste steps within a Workato recipe or across recipes
  while preserving step order, logic, and app connections.
---

# Copy paste steps

Get the most out of copy/paste with this video guide

[Video](https://www.youtube.com/embed/SdvPlXB0U9Q)

Copy and paste your recipe steps anywhere. Select any number of steps in a recipe to copy. Paste your copied steps anywhere within your recipe, or even into other recipes.

![Copy/paste with multi-select](/assets/copy-paste-step.DJZzALGb.png)_Copy/paste with multi-select_

> **Copy/paste within a workspace**
> 
> Copy/paste is limited to the same workspace. You may not log out / log in to a different account between copy and pasting.

## Preserve order and prevent errors

Move entire sections of your recipe with multi-select copy/paste while preserving the order of each step.

![Pasted steps preserve step order](/assets/pasted-steps-preserves-step-order.C6BfWwpw.png)_Pasted steps preserve the order of each step, including control statements_

This is critical in maintaining the logic of your recipes.

- The order for each step is preserved, ensuring that your are performing your workflow in the correct order.
- Recipe logic like [if-else conditionals](/en/features/if-conditions), [repeat loops](/en/recipes/steps#repeat-step), and [error monitoring blocks](/en/recipes/best-practices-error-handling) is maintained when pasting steps.
- [Formulas](/en/formulas/formula-mode) will also be pasted.

## Replicating app connection when pasting steps

When using copy/paste to duplicate steps in another recipe, the connection configuration is also copied to the target recipe. If the target recipe doesn't have an app connection, the app connection from the source recipe automatically connects.

![Pasting steps will replicate the app connection](/assets/pasted-steps-copies-app-connection.Dgljfkvp.png)_Pasting steps will replicate the app connection_

If there is an existing app connection configured in the target recipe, the app connection does not change.

## Remap datapills and auto-suggestion

A side effect of copy-pasting steps is that some datapill mappings might be broken if their source actions are not copied together, resulting in invalid datapill mappings.

Each invalid datapill mapping is highlighted in the recipe editor upon pasting. You may select **Remap** to replace this datapill with one from the current recipe. Workato ensures that the datapill mapping uses the same app and action to provide the most relevant suggestions.

![Remap datapills with auto-suggestions](/assets/remap-datapill-with-auto-suggestion.Y-GMBnkK.png)_Remap invalid datapills with auto-suggestions_

## Auto-remap datapills

If your action requires multiple remaps, Workato offers **auto-remap** to simplify the remapping process. Remap datapills in one go with intelligent matching suggestions.

1. Remap your first invalid datapill.
   
   ![Remap the first invalid datapill](/assets/auto-remap-first-datapill.-DbM8_Ot.png)_Remap the first invalid datapill_
   
2. After you remapped your first invalid datapill, Workato checks for matching datapills for all the other invalid mappings. This is useful for actions with many datapill mappings, including NetSuite, Workday, and Salesforce.
   
   ![Auto-remap](/assets/auto-remap.C-lfMOdX.png)_Auto-remap is available for steps with multiple invalid datapill mappings_
   
3. Review the datapill suggestion and select **Accept all**.
   
   ![Suggestions for auto-remap](/assets/auto-remap-review-and-accept.6kI9lWN_.png)_Workato provides suggestions for auto-remaps_

---
