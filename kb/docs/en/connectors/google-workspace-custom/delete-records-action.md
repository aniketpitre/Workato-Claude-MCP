---
url: >-
  https://docs.workato.com/en/connectors/google-workspace-custom/delete-records-action.md
description: >-
  The Delete records action enables you to delete multiple records in Google
  Workspace.
---

# Google Workspace (Custom) - Delete records action

The **Delete records** action enables you to delete multiple records in Google Workspace.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to delete records from. Fields load dynamically based on the object you select. |

For example, the following input fields correspond to the **Membership** object.

| Input field | Description |
| --- | --- |
| Group email address | Enter the value for the group email address. |
| Group member email address | Provide the group members’ email addresses. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the datatree to subsequent steps.

For example, the following output fields correspond to the **Membership** object.

| Output field | Description |
| --- | --- |
| Status | Status of the membership after the delete operation. |
