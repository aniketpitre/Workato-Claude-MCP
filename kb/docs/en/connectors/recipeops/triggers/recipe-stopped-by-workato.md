---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/recipe-stopped-by-workato.md
description: >-
  The Recipe stopped by Workato trigger in the RecipeOps connector fires when
  Workato stops a monitored recipe due to non-recoverable errors, in real time.
---

# RecipeOps - Recipe stopped by Workato trigger

The **Recipe stopped by Workato** trigger monitors selected recipes for stops due to non-recoverable errors in real-time. Workato typically stops a recipe when it encounters errors that cannot be resolved automatically. For example, Workato stops a recipe if 60 consecutive authentication errors occur in a recipe trigger. This trigger allows you to build logic to restart the recipe and set escalation policies to notify teammates when stops occur.

## Input

| Input field | Description |
| --- | --- |
| Recipes to monitor | Select the recipes to monitor. Choose **All** to monitor all recipes in the workspace, **Selected** to monitor selected recipes, or **Tags** to monitor recipes associated with one or more tags. |
| Recipe IDs | Provide a comma-separated list of recipe IDs if monitoring **Selected** recipes. You can find recipe IDs in the recipe’s URL. For example, in `https://app.workato.com/recipes/362905-timekeeper`, the recipe ID is `362905`. |
| Tags | Provide one or more tags if monitoring recipes by **Tags**. |

## Output

| Output field | Description |
| --- | --- |
| Recipe ID | The ID of the recipe where the error occurred. |
| Error | Details about the error. This object contains the `Error ID`, `Message`, `Error count`, `Error connector`, `Error source`, `Error source name`, `Is authorization error`, `Is rate limit error`, and `Is poll error (deprecated)` output datapills. |

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)
