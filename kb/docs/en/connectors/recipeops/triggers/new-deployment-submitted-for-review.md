---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/new-deployment-submitted-for-review.md
description: >-
  The New deployment submitted for review trigger in the RecipeOps connector
  fires when a new project deployment is submitted for review in real time.
---

# RecipeOps - New deployment submitted for review trigger

The **New deployment submitted for review** trigger monitors new project deployments submitted for review in real-time.

> **PRIVATE BETA**
> 
> This trigger is in private beta. Private beta features are available in production but only to selected customers. Customers must opt in and be accepted into the beta.
> 
> During the private beta, Workato may update its functionality or change its availability without prior notice.

## Input

This trigger doesn't require any input.

## Output

| Field | Description |
| --- | --- |
| Deployment | An object containing details about the deployment. |
| ID (deployment) | The unique identifier for the deployment. |
| Name (deployment) | The name of the deployment. |
| Description (deployment) | A brief description of the deployment. |
| Author (deployment) | An object containing information about the user who created the deployment. |
| User ID (author) | The workspace ID of the user who created the deployment. |
| User name (author) | The name of the user who created the deployment. |
| User email (author) | The email address of the user who created the deployment. |
| Deployment state (deployment) | The current state of the deployment. For example, `pending_review`. |
| Reviews (deployment) | A list of reviews associated with the deployment. |
| Reviewer (reviews) | An object containing details about the user assigned to review the deployment. |
| User ID (reviewer) | The workspace ID of the user assigned to review the deployment. |
| User name (reviewer) | The name of the user assigned to review the deployment. |
| User email (reviewer) | The email address of the user assigned to review the deployment. |
| Status (reviews) | The status of the review. For example, `pending`, `approved`, or `rejected`. |
| Comment (reviews) | Any comment added to the review. |
| Project build ID (deployment) | The unique identifier for the project build associated with the deployment. |
| Target folder (deployment) | An object containing details about the target folder. |
| ID (target folder) | The unique identifier of the target folder. |
| Name (target folder) | The name of the target folder. |
| Path (target folder) | The workspace path that indicates the location of the target folder. |

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)
