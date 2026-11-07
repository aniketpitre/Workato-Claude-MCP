---
url: 'https://docs.workato.com/en/connectors/recipeops/triggers/new-failed-job.md'
description: >-
  The Job failed trigger in the RecipeOps connector fires when a monitored
  recipe has a failed job, so you can automate corrective actions in real time.
---

# RecipeOps - Job failed trigger

The **Job failed** trigger monitors all active or selected recipes for failed jobs in real-time. This allows you to build logic to automate corrective actions, such as sending notifications when an issue occurs. Each failed job triggers an event, even if additional jobs fail with the same error.

## Input

| Input field | Description |
| --- | --- |
| Recipes to monitor | Select the recipes to monitor. Choose **All** to monitor all recipes in the workspace, **Selected** to monitor selected recipes, or **Tags** to monitor recipes associated with one or more tags. |
| Recipe IDs | Provide a comma-separated list of recipe IDs if monitoring **Selected** recipes. You can find recipe IDs in the recipe’s URL. For example, in `https://app.workato.com/recipes/362905-timekeeper`, the recipe ID is `362905`. |
| Tags | Provide one or more tags if monitoring recipes by **Tags**. |

## Output

| Output field | Description |
| --- | --- |
| Job ID | The ID of the failed job. |
| Original Job ID | The ID of the original job if it was a repeated job. |
| Recipe ID | The ID of the recipe. |
| Calling job ID | The ID of the calling job if this job was called from [Recipe Functions](/en/connectors/recipe-functions). |
| Calling recipe ID | The ID of the calling recipe if this job was called from [Recipe Functions](/en/connectors/recipe-functions). |
| Root recipe ID | The ID of the original recipe that initiated the workflow. This remains the same for all jobs related to that workflow. |
| Root job ID | The ID of the first job in the workflow triggered by the root recipe. |
| Title | The title of the recipe. |
| Status | The status of the recipe. |
| Is repeat | Indicates whether the job was repeated. |
| Is test | Whether the job was a test job. |
| Started at | The time this job was started. |
| Completed at | The time the last step was completed. |
| Repeat count | The number of times this job was rerun. The count starts from 1. |
| Flow ID (deprecated) | **This field is deprecated.** The ID of the recipe. |
| Error | Details about the error that caused the job to fail. This object contains the Error ID, Error type, Error type ID, Error at, Errored app, Errored action, Errored step number, Error message, and Inner message output datapills. |

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---

---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/member-invitation-accepted.md
description: >-
  The Member invitation accepted trigger in the RecipeOps connector fires when a
  member invitation is accepted in the workspace.
---

# RecipeOps - Member invitation accepted trigger

This trigger monitors for accepted member invitations in the workspace.

* * *

## Input

| Field | Description |
| --- | --- |
| **Invitations to monitor** | Select invitations to monitor for acceptance. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Invitation ID** | The ID of the invitation. |
| **User ID** | The workspace ID where the invitation was accepted. |
| **Email** | The email of the user who accepted the invitation. |
| **Name** | The name of the user who accepted the invitation. |
| **Role** | The name of the collaborator role assigned to the user who accepted the invitation. |
| **Invitation sent at** | The time the invitation was sent. |
| **Joined at** | The time the user accepted the invitation. |
| **Team** | Details about the team the user joined. This field has some additional sub-fields:
| Field | Description |
| --- | --- |
| **Team ID** | The team's ID. |
| **Team name** | The team's name. |
| **Owner ID** | The ID of the user who owns the team. |

 |

* * *

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---

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

---
