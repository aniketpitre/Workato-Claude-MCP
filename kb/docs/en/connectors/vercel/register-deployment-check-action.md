---
url: >-
  https://docs.workato.com/en/connectors/vercel/register-deployment-check-action.md
description: >-
  The Register deployment check action creates a deployment check on a Vercel
  project.
---

# Vercel - Register deployment check action

The **Register deployment check** action creates a deployment check on a project in Vercel. Vercel can block only `deployment-alias`.

## Input

| Input field | Description |
| --- | --- |
| Project ID or name | Select a project or enter a project ID or name. |
| Name | Enter the name Vercel shows for this check. |
| Requires | Select when the check starts. Options include **Build ready**, **Deployment URL**, and **None**. |

## Output

| Output field | Description |
| --- | --- |
| ID | The check ID. |
| Name | The check name. |
| Project ID | The ID of the project. |
| Owner ID | The ID of the owner of the check. |
| Requires | When the check starts. |
| Blocks | What the check blocks. |
| Targets | The environments the check runs on. |
| Timeout | The timeout in milliseconds. |
| Is rerequestable | Whether users can re-run the check. |
| Source | The origin of the check. |
| Source kind | The kind of source that created the check. |
| Created at | When the check was created, in ISO 8601 format. |
| Updated at | When the check was last changed, in ISO 8601 format. |
| Deleted at | When the check was deleted, in ISO 8601 format. This field is empty if the check hasn't been deleted. |
