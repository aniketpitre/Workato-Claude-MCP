---
url: 'https://docs.workato.com/en/connectors/recipeops/actions/list-recipes.md'
description: >-
  The List recipes action in the RecipeOps connector retrieves a list of recipes
  with details such as ID, name, job count, and lifetime task count.
---

# RecipeOps - List recipes action

This action retrieves a list of recipes and includes info such as recipe ID, name, job count, and lifetime task count.

* * *

## Limitations

- Results are limited to 1,000 recipes
- Lifetime task count data is available from March 19, 2021 onward

* * *

## Input

| Field | Description |
| --- | --- |
| **Recipe status** | Filter recipes by their status: **All**, **Active**, **Inactive**, **Stopped due to error** |
| **Recipe IDs** | The ID(s) of specific recipes to retrieve. To include multiple recipes, provide their IDs as a comma-separated list. For example: `362905, 362906` Recipe IDs can be found in the URL of your browser. Navigate to the recipe's page and look for a number after `https://app.workato.com/recipes/`. For example: If the URL is `https://app.workato.com/recipes/362905-timekeeper`, then the recipe ID is `362905`. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Recipe ID** | The ID of the recipe. |
| **User ID** | The workspace ID where this recipe is located. |
| **Folder ID** | The ID of the folder containing the recipe. |
| **Name** | The name of the recipe. |
| **Active** | If `true`, the recipe is currently active. |
| **Parent ID** | If the recipe was cloned, this will contain the ID of the recipe it was originally cloned from. |
| **Successful job count** | The total number of successful jobs the recipe has had. |
| **Failed job count** | The total number of failed jobs the recipe has had. |
| **Lifetime task count** | The total number of tasks the recipe has used over the course of its lifetime. |
| **Version no** | The current version of the recipe. |
| **Major version no** |  |
| **Stopped due to error** | If `true`, the recipe was last stopped due to an error. |
| **Stop reason** | If the recipe was stopped, this will be the reason for the stoppage. |
| **Last run at** | The time the recipe last ran. |
| **Created at** | The time the recipe was created. |
| **Updated at** | The time the recipe was last updated. |
| **List size** | The total number of recipes in the result set. |
| **List index** | The index (current position) of the recipe in the list of results. |

* * *

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---
