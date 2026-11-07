---
url: 'https://docs.workato.com/en/recipes/steps/skip-step.md'
description: >-
  Learn how to mark recipe steps as skipped in Workato to build and test
  automation logic incrementally at runtime.
---

# Skip step

Troubleshoot with skip steps in under 2 minutes

[Video](https://www.youtube.com/embed/MWqMBEJvhxw)

When you mark a step as skipped, the recipe ignores it at runtime. You can skip an individual [action](/en/recipes/actions#actions) or a block of actions, such as a [repeat](/en/recipes/steps#repeat-step) or [conditional](/en/recipes/steps#if-condition-step) step. Skipping steps is useful when you plan to:

- Outline the recipe’s high-level logic before configuring and testing details.
- Compare different logic approaches by skipping steps selectively.
- Continue testing without interruption by skipping steps with broken connections, incorrect formulas, or missing configurations.

Since triggers are required to start recipes, Workato doesn't support skipping triggers.

> **WARNING**
> 
> You can't use datapills from skipped steps in subsequent recipe steps.

![Skipped step](/assets/skipped-step.CV4gD5SP.png)_A skipped step won't be processed at runtime, and its datapills won't be available_

## How to use skip steps

Complete the following steps to mark a recipe step as skipped:

1. Open a recipe in the recipe editor.
   
2. Hover over the recipe step and click the **•••** (ellipsis).
   
3. Click **Skip**. This skips the step when the recipe is started.
   
   ![Skip step](/assets/skip-icon.BIbsmrSp.png)_Skip step_
   
   Select **Unskip** to return the step to the recipe logic.
   
   ![Unskip step](/assets/unskip-icon.B7JgE5FQ.png)_Unskip step_
   

> **KEYBOARD SHORTCUT**
> 
> Use the keyboard shortcut (Command+/ or Control+/) while a step is selected to toggle between skipping and unskipping it.

## Skip action block

You can mark an action block as skipped to skip multiple actions at once, rather than skipping each action individually.

The following action blocks can be skipped:

- Conditional blocks
- Repeat blocks
- Error monitor blocks

This follows the same logic as control flows. A conditional statement is tied to its actions, so skipping a conditional block also skips its nested steps.

![Skipped block](/assets/skipped-block.CoilV5eS.png)_A skipped repeat block. All nested actions won't be processed at runtime_

## How to use skip action blocks

You can skip an action block by selecting **Skip** on a parent step, such as a **Repeat** step. This process is identical to [skipping a single step](#how-to-use-skip-steps).

When a recipe skips the parent node of an action block, it also skips all nested steps.

To unskip an action block, you must select **Unskip** from the parent node. A nested step inside a skipped block can't be unskipped.

Instead, you can choose one of the following options:

- Skip or unskip an entire block.
- Keep the block active and directly skip or unskip its child steps.

![Skip block](/assets/skip-block.WoxV8J1M.png)_Skip block_

## What happens to datapills in skipped steps?

When you skip a step, all dependent steps break when you try to run the recipe. Subsequent actions that rely on datapills from a skipped step will return an error.

For example, this recipe returns an error during testing because the step references a datapill from an earlier skipped step.

![Skipped datapills](/assets/skipped-datapill.D7GuNt1p.png)_Datapills in a skipped step/block won't be available_

---
