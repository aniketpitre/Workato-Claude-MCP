---
url: 'https://docs.workato.com/en/connectors/recipeops/actions/search-recipes.md'
description: >-
  The Search recipes action in the RecipeOps connector retrieves recently
  updated recipes in the account, filtered by status and connection.
---

# RecipeOps - Search recipes action

This action retrieves recently updated recipes in the account. Recipes can be filtered by status and connection.

* * *

## Limitations

- Results are limited to 1,000 recipes
- Lifetime task count data is available from March 19, 2021 onward

* * *

## Input

| Field | Description |
| --- | --- |
| **Recipe status** | Filters jobs by status: **All**, **Active**, **Inactive**, **Stopped due to error** |
| **Connection** | Filters recipes by connection. If defined, only recipes that use the connection will be included in the results. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Recipe ID** | The ID of the recipe. |
| **User ID** | The workspace ID where this recipe is located. |
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
