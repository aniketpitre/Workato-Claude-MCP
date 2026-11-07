---
url: >-
  https://docs.workato.com/en/connectors/mural/get-record-details-by-id-action.md
description: >-
  The Get record details by ID action enables you to retrieve details of a
  specific record in Mural.
---

# Mural - Get record details by ID action

The **Get record details by ID** action enables you to retrieve details of a specific record in Mural.

## Input

| Input fields | Description |
| --- | --- |
| Object | Specify the object to retrieve its details. Fields load dynamically based on the object you select. |
| Mural ID | Provide the ID of a Mural. |

## Output

| Output fields | Description |
| --- | --- |
| Canvas link | The mural’s link. |
| Title | The title of the mural. |
| Room ID | ID of a room. |
| ID | The unique ID of the mural. |
| Workspace ID | The unique ID of the workspace containing the mural. |
| Background color | The background color of the mural. |
| Height | The height of the mural in px. |
| Width | The width of the mural in px. |
| Timer sound theme | The timer sound theme for the mural. |
| Visitor avatar theme | The visitor avatar theme for the mural. |
| Created on | The mural's creation timestamp in milliseconds. |
| First name | Child parameter of the **Created by** object. This is the first name of the object collaborator. |
| Last name | Child parameter of the **Created by** object. This is the last name of the object collaborator. |
| ID | Child parameter of the **Created by** object. This is the of the object collaborator. |
| Visitors | Child parameter of the **Visitors Setting** object. The visitor's permission for a collaborator on a mural. |
| Workspace members | Child parameter of the **Visitors Setting** object. This is the visitor's workspace permission for a collaborator on a mural. |
| Link | Child parameter of the **Visitors Setting** object. This is the link that a visitor can use to access a mural. |
| Expires on | Child parameter of the **Visitors Setting** object. The unix timestamp is in milliseconds, after which the visitor link becomes invalid. |
| Confidential | Child parameter of the **Sharing Setting** object. When true, the mural is confidential. Confidential murals do not allow a shared link and cannot be duplicated or moved to other workspaces. |
| Link | Child parameter of **Sharing Setting** object. This is the link that a visitor can use to access a mural. |
| Folder ID | The UUID of the folder this mural belongs to. |
| Updated on | The last time the mural was updated in milliseconds. |
| First name | Child parameter of the **Updated by** object. This is the first name of the object collaborator. |
| Last name | Child parameter of the **Updated by** object. The last name of the object collaborator. |
| ID | Child parameter of the **Updated by** object. This is the ID of the object collaborator. |
| Thumbnail URL | A URL pointing to the latest thumbnail generated for this mural. |
| Embed link | A URL pointing to the mural that can be embedded in a blog or any public web page. |
| Favorite | When true, the mural is favorited by the currently authenticated user. |
| Infinite | When true, this indicates that the mural canvas is borderless and grows as you add widgets to it. |
| State | The value used to authorize anonymous visitors. |
| Status | The current status of the mural. |
