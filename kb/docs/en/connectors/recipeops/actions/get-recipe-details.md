---
url: 'https://docs.workato.com/en/connectors/recipeops/actions/get-recipe-details.md'
description: >-
  The Get recipe details action in the RecipeOps connector retrieves key
  information about a recipe, such as status, version number, and lifetime task
  count.
---

# RecipeOps - Get recipe details action

This action retrieves key information about a recipe, such as status, version number, and lifetime task count.

* * *

## Limitations

Lifetime task count data is available from March 19, 2021 onward.

* * *

## Input

| Field | Description |
| --- | --- |
| **Recipe** | The recipe to retrieve. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Recipe ID** | The ID of the recipe. |
| **User ID** | The workspace ID where this recipe is located. |
| **Name** | The name of the recipe. |
| **Parent ID** | The ID of the parent recipe. |
| **Folder ID** | The ID of the folder. |
| **Version no.** | The current version of the recipe. |
| **Last run at** | The time the recipe last ran. |
| **Created at** | The time the recipe was created. |
| **Updated at** | The time the recipe was last updated. |
| **Successful job count** | The total number of successful jobs completed by the recipe. |
| **Failed job count** | The total number of failed jobs the recipe has had. |
| **Lifetime task count** | The total number of tasks the recipe has used over the course of its lifetime. |
| **Active** | If `true`, the recipe is currently active. |
| **Last version** | Details about the last version of the recipe. This field has the following sub-fields:
| Field | Description |
| --- | --- |
| **Version no** | The version number. |
| **User ID** | The workspace ID where this recipe is located. |
| **User name** | The name of the user who created the recipe. |
| **User email** | The email of the user who created the recipe. |
| **Updated at** | The time this version of the recipe was last updated. |

 |
| **Folder** | Details about the folder containing the recipe. This field has the following sub-fields:

| Field | Description |
| --- | --- |
| **ID** | The ID of the folder. |
| **Name** | The name of the folder. |
| **Path** | The location of the folder. |
| **Parents** | Details about the folders that contain the current folder. |

 |
| **Created by** | Details about the user who created the recipe. This field has the following sub-fields:

| Field | Description |
| --- | --- |
| **User ID** | The workspace ID where this recipe is located. |
| **User name** | The name of the user who created the recipe. |
| **User email** | The email of the user who created the recipe. |

 |

* * *

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---
