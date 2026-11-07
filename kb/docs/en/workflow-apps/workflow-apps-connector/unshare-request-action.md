---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/unshare-request-action.md
description: >-
  Use the Unshare request action to remove a user's or user group's access to a
  request in a Workflow app.
---

# Unshare request action

Use the **Unshare request** action to remove a user's or user group's access to a request in a Workflow app. This reverses access granted through the [Share request action](/en/workflow-apps/workflow-apps-connector/share-request-action).

This action succeeds even if the request wasn't shared with a user or user group. For example, if you share a request with a user who doesn't have access to the Workflow apps portal, the action succeeds, but the user isn't provisioned access to the request.

## Input

| Input field | Description |
| --- | --- |
| Workflow app | Select the Workflow app that contains the request. |
| Record ID | Select the request to unshare. You can map in a datapill or enter the request ID. |
| Unshare from | Specify the user group or individual user to remove access from. You can select a user group from the list, provide a user group ID, or enter a user's email address. |

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

| Output field | Description |
| --- | --- |
| Shared with (Record) | A nested object within the `Record` object containing information about users or user groups who still have access to the request. Returns an empty list if the request isn't shared with anyone. |
| ID (Shared with) | The ID of the user group who still has access to the request. |
| Name (Shared with) | The name of the user or user group who still has access to the request. |
| Email (Shared with) | The email address of the user who still has access to the request, if applicable. Emails don't display for user groups. |
| Type (Shared with) | Indicates whether the request is shared with a user or user group. |
| Record | This object represents a record in a Workflow app. |
| Record ID (Record) | Workato automatically generates a unique ID for each record in a Workflow app's corresponding data table. |
| Application (Record) | This object represents a Workflow app. It contains columns from a request and approval app's primary data table. The exact output varies based on the columns present in your app's data table. |
| Created by (Record) | A nested object within the `Record` object containing information about the user who created the request. |
| User ID (Created by) | The ID of the user who created the request. |
| User name (Created by) | The name of the user who created the request. |
| Email (Created by) | The email of the user who created the request. |
| Status (Created by) | The status of the user. |
| Groups (Created by) | A nested object within the `Created by` object containing information on group membership. |
| Group ID (Created by) (Groups) | The ID of the group this task is assigned to. |
| Group name (Created by) (Groups) | The name of the group this task is assigned to. |
| List size (Created by) (Groups) | The size of the list. |
| List index (Created by) (Groups) | The list index. |
| Guest user (Created by) | Indicates whether the request was submitted by an anonymous user. |
| Stage (Created by) | A nested object within the `Request` object containing stage details. |
| Stage ID (Created by) (Stage) | The ID of the group this task is assigned to. |
| Stage name (Created by) (Stage) | The name of the stage this task is assigned to. |
| Created at (Record) | The date the record was created. |
| Updated at (Record) | The date the record was most recently updated. |
