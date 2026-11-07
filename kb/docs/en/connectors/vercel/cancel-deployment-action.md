---
url: 'https://docs.workato.com/en/connectors/vercel/cancel-deployment-action.md'
description: The Cancel deployment action cancels an in-progress deployment in Vercel.
---

# Vercel - Cancel deployment action

The **Cancel deployment** action cancels an in-progress deployment in Vercel.

## Input

| Input field | Description |
| --- | --- |
| Deployment ID | Select a deployment or enter a deployment UID. |

## Output

This action has a large number of output fields. The following are a representative set of output fields.

| Output field | Description |
| --- | --- |
| ID | The deployment ID. |
| Name | The deployment name. |
| URL | The deployment URL. |
| Ready state | The current state of the deployment. |
| Target | The deployment target. Options are **Production** or **Preview**. |
| Project ID | The ID of the project. |
| Created at | When Vercel created the deployment record, in ISO 8601 format. This is the start point for measuring how long the deployment waited before building. |
| Building at | When the deployment started building, in ISO 8601 format. The time between **Created at** and **Building at** is how long the deployment waited in the queue. This field is empty if the build hasn't started. |
| Ready | When the deployment became ready to serve traffic, in ISO 8601 format. The time between **Building at** and **Ready** is the build duration. This field is empty if the deployment is still building or ended in an error or cancellation. |
| Canceled at | When the deployment was canceled, in ISO 8601 format. This field is empty if the deployment wasn't canceled. |
| Creator | The user who created the deployment. |
| Git source | The Git source the deployment was created from. |
| Git repo | The Git repository the deployment belongs to. |
| Alias | The aliases assigned to the deployment. |
| Alias assigned | Whether aliases are assigned to the deployment. |
| Alias error | The error returned when assigning an alias, if any. |
| Checks state | The current state of the deployment checks. |
| Checks conclusion | The final result of the deployment checks. |
| Error code | The error code when the deployment failed. |
| Error message | The error message when the deployment failed. |

---
