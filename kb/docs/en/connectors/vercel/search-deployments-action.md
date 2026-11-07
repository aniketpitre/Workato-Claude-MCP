---
url: 'https://docs.workato.com/en/connectors/vercel/search-deployments-action.md'
description: >-
  The Search deployments action searches deployments for the authenticated user
  or team using filters.
---

# Vercel - Search deployments action

The **Search deployments** action searches deployments for the authenticated user or team using filters.

## Input

| Input field | Description |
| --- | --- |
| Project ID | Optional. Select a project or enter a project ID. |
| State | Optional. Select the deployment state. Options include **Building**, **Error**, **Initializing**, **Queued**, **Ready**, and **Canceled**. |
| Target | Optional. Select the deployment target. Options are **Production** or **Preview**. |
| App | Optional. Enter the deployment name, which is normally the project name. |
| Limit | Optional. Enter the maximum number of deployments to return. |

## Output

| Output field | Description |
| --- | --- |
| Deployments | The list of deployments. Each item includes fields such as **UID**, **Name**, **URL**, **State**, **Ready state**, **Target**, **Source**, **Project ID**, **Created**, **Creator**, **Attribution**, **Checks state**, and **Checks conclusion**. |
| Pagination | Pagination details, including **Count**, **Next**, and **Prev**. |

---
