---
url: 'https://docs.workato.com/en/connectors/recipeops/actions/stop-recipe.md'
description: >-
  The Stop recipe action in the RecipeOps connector lets you stop a single
  recipe by its ID or name, and choose whether to force the stop.
---

# RecipeOps - Stop recipe action

The **Stop recipe** action stops a single recipe you specify by its ID or name.

## Input

| Field | Description |
| --- | --- |
| Recipe | Enter the unique identifier or name of the recipe you plan to stop. The recipe ID is the number found after `www.workato.com/recipes/` in the recipe URL. For example, in `www.workato.com/recipes/362905-timekeeper`, the recipe ID is `362905`. |
| Force stop | Select whether to stop the recipe even if it's connected to active API endpoints, has pending jobs, or is called by other active recipes. `Yes` or `true`: Stops the recipe regardless of these conditions. Jobs already running finish processing, but the recipe stops accepting new jobs.; `No` or `false`: Keeps the recipe running if any of these conditions apply. The stop action fails instead of stopping the recipe. Depending on the error handling configured for the recipe that includes this step, that recipe's job can also fail. |

## Output

| Field | Description |
| --- | --- |
| Recipe ID | The unique identifier of the recipe that stopped. |
| Recipe name | The name of the recipe that stopped. |
| Active | Indicates whether the recipe is active or inactive. |

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---
