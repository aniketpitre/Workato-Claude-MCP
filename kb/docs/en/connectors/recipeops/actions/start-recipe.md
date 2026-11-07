---
url: 'https://docs.workato.com/en/connectors/recipeops/actions/start-recipe.md'
description: >-
  The Start recipe action in the RecipeOps connector lets you start a single
  recipe specified by its ID or name.
---

# RecipeOps - Start recipe action

The **Start recipe** action starts a single recipe you specify by its ID or name. If the recipe can't start, the job fails with an error.

## Input

| Field | Description |
| --- | --- |
| Recipe | Enter the unique identifier or name of the recipe you plan to start. The recipe ID is the number found after `www.workato.com/recipes/` in the recipe URL. For example, in `www.workato.com/recipes/362905-timekeeper`, the recipe ID is `362905`. |

## Output

| Field | Description |
| --- | --- |
| Recipe ID | The unique identifier of the recipe that started. |
| Recipe name | The name of the recipe that started. |
| Active | Indicates whether the recipe is active or inactive. |

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---
