---
url: >-
  https://docs.workato.com/en/connectors/google-workspace-custom/get-records-action.md
description: >-
  The Update record action enables you to retrieve multiple records in Google
  Workspace.
---

# Google Workspace (Custom) - Get records action

The **Get records** action enables you to retrieve multiple records in Google Workspace.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to retrieve details for. Fields load dynamically based on the object you select. |

For example, the following input fields correspond to the **Groups** object.

| Input field | Description |
| --- | --- |
| User keys | Provide the array of keys for group members. |
| Group member email address | Provide the group members’ email addresses. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the datatree to subsequent steps.

For example, the following output fields correspond to the **Groups** object.

| Output field | Description |
| --- | --- |
| Groups | Array of group objects. |
| Kind | Kind of the resource. |
| ID | Unique identifier for the group. |
| Entity tag | Entity tag for the group. |
| Group email | Group’s email address. |
| Group name | Group’s name. |
| Direct members count | Number of direct members in the group. |
| Description | Description of the group. |
| Admin created | Indicates if the group was created by an admin. |
| Aliases | The object of email aliases associated with the group. |
| Non editable aliases | Object of email aliases that cannot be edited. |
