---
url: 'https://docs.workato.com/en/connectors/vercel/new-deployment-trigger.md'
description: >-
  The New deployment trigger checks Vercel for new deployments and starts a
  recipe for each one.
---

# Vercel - New deployment trigger

The **New deployment** trigger checks Vercel for new deployments and starts a recipe for each one.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Optional. The date and time to start from when you first start the recipe. Leave this field blank to pick up deployments created within the past hour. You can't change this value after you run or test the recipe. |
| Project ID | Optional. Select a project to limit the trigger to that project. |
| State | Optional. Select a deployment state to filter by. Vercel checks the state when the trigger polls, so a deployment that is still building when the trigger polls isn't picked up later. Leave this field blank to catch every new deployment. |
| Target | Optional. Select the deployment target. Options are **Production** or **Preview**. |

## Output

This trigger has a large number of output fields. The following are a representative set of output fields.

| Output field | Description |
| --- | --- |
| UID | The deployment ID. |
| Name | The deployment name. |
| URL | The deployment URL. |
| State | The state of the deployment. |
| Ready state | The current state of the deployment. |
| Target | The deployment target. Options are **Production** or **Preview**. |
| Project ID | The ID of the project. |
| Created | When Vercel created the deployment record, in ISO 8601 format. This is the time the deployment was requested, for example by a Git push or a CLI deploy. |
| Created at | When Vercel created the deployment record, in ISO 8601 format. This is the start point for measuring how long the deployment waited before building. |
| Building at | When the deployment started building, in ISO 8601 format. The time between **Created at** and **Building at** is how long the deployment waited in the queue. This field is empty if the build hasn't started. |
| Ready | When the deployment became ready to serve traffic, in ISO 8601 format. The time between **Building at** and **Ready** is the build duration. This field is empty if the deployment is still building or ended in an error or cancellation. |
| Creator | The user who created the deployment. |
| Source | How the deployment was created. |
| Attribution | Git and Vercel user details. |
| Checks state | The current state of the deployment checks. |
| Checks conclusion | The final result of the deployment checks. |
| Alias assigned | Whether aliases are assigned to the deployment. |
| Alias error | The error returned when assigning an alias, if any. |
| Error code | The error code when the deployment failed. |
| Error message | The error message when the deployment failed. |

---
