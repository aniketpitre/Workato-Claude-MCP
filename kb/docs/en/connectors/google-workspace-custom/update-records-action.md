---
url: >-
  https://docs.workato.com/en/connectors/google-workspace-custom/update-records-action.md
description: >-
  The Update records action enables you to update the details of multiple
  records in Google Workspace.
---

# Google Workspace (Custom) - Update records action

The **Update records** action enables you to update the details of multiple records in Google Workspace.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object type of the records you plan to update. Fields load dynamically based on the object you select. |

For example, the following input fields correspond to the **Membership** object.

| Input field | Description |
| --- | --- |
| Members | An array of Member objects. |
| Group email address | Provide the group’s email address. |
| Group member email address | Provide the group members’ email addresses. |
| Mail delivery preferences | Provide preference for mail delivery. |
| Group member role | Provide a role for the group member. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the datatree to subsequent steps.

For example, the following output fields correspond to the **Membership** object.

| Output field | Description |
| --- | --- |
| Group Member | An array of group member objects. |
| ID | Unique identifier for membership. |
| Kind | Kind of the resource. |
| Entity tag | Entity tag for the membership. |
| Member email | Email address of group member. |
| Member type | Details about the type of member. |
| Member status | Current status of the member. |
| Delivery preference | Preference for mail delivery. |
