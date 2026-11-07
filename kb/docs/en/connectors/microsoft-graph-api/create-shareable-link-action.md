---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/create-shareable-link-action.md
description: >-
  The Create shareable link action creates a shareable link in Microsoft Graph
  API. The existing link is returned if a shareable link already exists.
---

# Microsoft Graph API - Create shareable link action

The **Create shareable link** action creates a shareable link in Microsoft Graph API. The existing link is returned if a shareable link already exists.

## Input

| Input field | Description |
| --- | --- |
| Entity type | Select the entity to provide permissions to create a shareable link. |
| Site ID | Select the ID of the site to create a shareable link for. Default is to pick up sites from the communication site directory. |
| Link type | Select the type of link to create. For example, `view`, `edit`, or `embed`. |
| Folder ID | The ID of the folder to create a shareable link for. |
| Retain inherited permissions | Select if existing inherited permissions are retained when you share this item. All existing permissions are removed when sharing the item if set to false. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the shareable link. |
| Roles | Any roles that associated with the shareable link, such as `read`. |
| Link | The shareable link URL. |
| Has password | A boolean response indicating if the shareable link requires a password to access. |
| Share ID | The ID of the resource the shareable link corresponds with. |
| Expiration date time | The date and time that the shareable link expires. |
