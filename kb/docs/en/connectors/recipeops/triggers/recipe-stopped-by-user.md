---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/recipe-stopped-by-user.md
description: >-
  The Recipe stopped by user trigger in the RecipeOps connector fires when a
  user manually stops a monitored recipe, in real time.
---

# RecipeOps - Recipe stopped by user trigger

The **Recipe stopped by user** trigger monitors recipes manually stopped by users in real-time.

## Input

| Input field | Description |
| --- | --- |
| Recipes to monitor | Select the recipes to monitor. Choose **All** to monitor all recipes in the workspace, **Selected** to monitor selected recipes, or **Tags** to monitor recipes associated with one or more tags. |
| Recipe IDs | Provide a comma-separated list of recipe IDs if monitoring **Selected** recipes. You can find recipe IDs in the recipe’s URL. For example, in `https://app.workato.com/recipes/362905-timekeeper`, the recipe ID is `362905`. |
| Tags | Provide one or more tags if monitoring recipes by **Tags**. |

## Output

| Output field | Description |
| --- | --- |
| Stopped at | The time the recipe was stopped. |
| Recipe ID | The ID of the recipe that was stopped. |
| Name | The name of the recipe that was stopped. |
| Last run at | The time the recipe last ran. |
| Created at | The time the recipe was created. |
| Updated at | The time the recipe was last updated. |
| Stopped by user | Details about the user who stopped the recipe, including the `User ID`, `User name`, and `User email`. |

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)
