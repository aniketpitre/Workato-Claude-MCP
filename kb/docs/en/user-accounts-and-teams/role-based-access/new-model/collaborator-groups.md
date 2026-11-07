---
url: >-
  https://docs.workato.com/en/user-accounts-and-teams/role-based-access/new-model/collaborator-groups.md
description: >-
  Learn how collaborator groups in Workato assign project roles to sets of users
  at once and how stacked group permissions are applied.
---

# Collaborator groups

Collaborator groups simplify access management by letting you assign project roles to a set of collaborators at once. You can group collaborators based on team structure, such as QA testers, marketing, or engineering teams.

![Collaborator groups](/assets/collaborator-groups.id4PdREi.png)_Collaborator groups_

## How collaborator groups manage project permissions

Collaborator groups organize collaborators under shared project-level roles. After you create a group and add members, you can grant project access to entire groups instead of managing individual assignments.

Collaborators with the **Collaborators** admin privilege manage these groups and control their membership. Collaborators can belong to multiple groups, but each group can include only individual users. Group nesting isn't supported.

> **INDIVIDUAL ASSIGNMENT REQUIRED**
> 
> You can't grant environment roles through collaborator groups. You must assign environment access to each user individually, even if they belong to a group.

### How group-based permissions are applied

When you assign a collaborator group to a project, all members of the group inherit the assigned project role.

Collaborators who belong to multiple groups receive the highest level of access granted by any group. Permissions from multiple groups stack and don't conflict. For example, when one group grants the **Project admin** role in a project and another grants the **Builder** role in the same project, the collaborator inherits **Project admin** permissions.

Changes to collaborator groups take effect immediately after you refresh the page. The system immediately revokes any access granted through that group when you remove a collaborator from a group.

If your workspace uses SAML role sync / SCIM for passing in the workato\_user\_groups parameter, this serves as the source of truth and any manual updates will be overwritten.

## Create a collaborator group

Complete the following steps to create and manage a collaborator group:

1. Go to **Workspace admin > Access control > Collaborator groups**.
   
2. Click **\+ Create collaborator group**.
   
3. Enter a **Group name**.
   
   ![Create collaborator group](/assets/create-collaborator-group.C5qAEaer.png)_Create collaborator group_
   
4. Optional. Add a **Description**. The quota is 350 characters.
   
5. Select **Collaborators** to add to the group. Use the search bar to filter by name or email.
   
6. Click **Create**.
   

> **ADD COLLABORATORS TO GROUPS DURING INVITATION**
> 
> You can also add collaborators to groups when you invite them to the workspace. The **Invite collaborator** dialog in **Workspace admin > Access control > Collaborators** includes an optional **Collaborator groups** field. This allows you to assign group membership during the invitation process instead of adding the collaborator to a group separately.

## Manage group collaborators

After you create a collaborator group, you can manage its members directly:

**Add collaborators to an existing group**

1. Go to **Workspace admin > Access control > Collaborator groups**.
   
2. Select the group to manage.
   
3. Click **\+ Add collaborators**.
   
   ![Add collaborators](/assets/add-collaborators-group.BauZOWsY.png)_Add collaborators_
   
4. Search for collaborators by name or email, then select members to add.
   
5. Click **Add**.
   
   ![Click add](/assets/click-add.CUtY7JIU.png)_Click **Add**_
   

**Remove collaborators from a group**

1. Go to **Workspace admin > Access control > Collaborator groups**.
   
2. Select the group to manage.
   
3. Click the checkbox next to the group members you plan to remove.
   
4. Click **Remove member**.
   
   ![Remove member](/assets/remove-member.7B-4g-aE.png)_Remove member_
   

**View project access for a group**

1. Open the group page from **Workspace admin > Access control > Collaborator groups**.
   
2. Select the **Project access** tab.
   
3. View a list of all projects where the group has access.
   
   ![Project access](/assets/project-access.Cu45WI8s.png)_Project access_
   
   If the group has no access to any project, the page displays **No project access is given to this group**.
   
   ![No project access](/assets/no-project-access.CTzsH4N7.png)_No project access_
   

## Assign project access to collaborator groups

Collaborators with the Manage project access privilege can assign project roles to individual collaborators or entire collaborator groups.

1. Go to **Projects > \[Project name\] > Settings > Project access**.
   
2. Click **\+ Add collaborators**.
   
   ![Project access](/assets/add-collaborators-group-project.ChJlu_uA.png)_Add collaborators to project_
   
3. Select a **Project role** from the drop-down menu.
   
4. Search for collaborators or collaborator groups by name or email, then select the checkboxes next to the collaborators or groups you plan to add.
   
   ![Project access](/assets/select-collaborator-groups.DLL3kbVu.png)_Choose collaborators_
   
5. Click **Add** to apply the selected project roles.
