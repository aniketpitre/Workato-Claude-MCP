---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/share-request-action.md
description: >-
  Use the Share request action to share a request from a Workflow app with a
  user or user group.
---

# Share request action

Use the **Share request** action to share a request from a Workflow app with a user or user group. You can use this action to:

- Share the request with approvers. This enablers approvers to see the request after approval. Requests disappear from an approver's view after approval by default if you don't share the request.
- Share the request with a group of observers who need to monitor certain requests without participating in the approval workflow.
- Add participants to the request for communication purposes. Participants can leave comments and stay informed about request progress.

Users with whom you share the request have the same view as the requester. Users can see the request, access the **View details** page, and leave comments when you share a request. Sharing a request doesn't allow users to make decisions to tasks that aren't assigned to them.

## Input

| Input field | Description |
| --- | --- |
| Workflow app | Choose the Workflow app to share the request from. |
| Record ID | Choose a request to share with one or more additional participants. You can map in a datapill or enter the exact ID of a request. |
| Share to | Specify the user group or individual user to share the request with. You can select a user group from the list, provide a user group ID, or enter a user's email address. You can share a request with a maximum of 20 users or user groups. |

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

| Output field | Description |
| --- | --- |
| Shared with (Record) | A nested object within the `Record` object containing information about the user group or user the request is shared with. |
| ID (Shared with) | The ID of the user group who the request is shared with. |
| Name (Shared with) | The name of the user or user group who the request is shared with. |
| Email (Shared with) | The email address of the user who the request is shared with, if applicable. Emails don't display for user groups. |
| Type (Shared with) | Indicates whether the request was shared with a user or user group. |
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
