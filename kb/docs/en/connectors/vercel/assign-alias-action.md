---
url: 'https://docs.workato.com/en/connectors/vercel/assign-alias-action.md'
description: The Assign alias action assigns an alias to a Vercel deployment.
---

# Vercel - Assign alias action

The **Assign alias** action assigns an alias to a deployment in Vercel.

## Input

| Input field | Description |
| --- | --- |
| Deployment ID | Select a deployment or enter a deployment UID. |
| Alias | Enter the hostname to point at this deployment. For example, `app.example.com`. |
| Redirect | Optional. Enter a hostname to redirect this alias to with an HTTP 307 response. For example, `example.com`. |

## Output

| Output field | Description |
| --- | --- |
| UID | The ID of the alias. |
| Alias | The assigned alias hostname. |
| Created | When the alias was created, in ISO 8601 format. |
| Old deployment ID | The ID of the deployment the alias previously pointed to, if any. |

---
