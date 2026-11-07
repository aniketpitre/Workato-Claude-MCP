---
url: 'https://docs.workato.com/en/data-tables/data-table-permissions.md'
description: >-
  Set up data table permissions in Workato with RBAC and custom roles to control
  who can create, view, edit, and delete tables.
---

# Data table permissions

A collaborator's [project role](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles) controls what they can do with data tables in a project: view, create, edit records, delete, or modify structure.

The following table shows the default data tables access for each system project role:

| Role | Data tables permissions |
| --- | --- |
| Project admin | Full access |
| Advanced builder | Full access |
| Builder | Full access |
| Project operator | None |

If the system roles don't fit, create a [custom project role](/en/user-accounts-and-teams/role-based-access/access-control-v2#create-a-custom-project-role) and pick the data tables privileges yourself.

## Configure data tables privileges in a custom project role

Data tables privileges appear under the **Project assets** section of the project role editor.

![Data tables permissions](/assets/permissions.BGTmPsVO.png)_Assign data tables permissions_

Complete the following steps to configure data tables privileges in a custom project role:

1. Sign in to your Workato account.
   
2. Go to **Workspace admin > Project roles** and click **\+ Add project role**. Alternatively, you can modify an existing custom role.
   
3. Navigate to **Project assets > Data tables**.
   
4. Determine the privileges to assign to this role.
   
5. Click **Save changes**.
   

## Assign roles

Data tables access is controlled by **project roles**, which are assigned per project. A new collaborator must also be assigned an **environment role** when they're invited to the workspace, but environment roles don't grant data tables access on their own.

- To invite a new collaborator and assign their environment role, refer to [Invite collaborators](/en/user-accounts-and-teams/role-based-access/managing-team-collaborators#inviting-collaborators).
- To assign or change a collaborator's project role (which controls their data tables access), refer to [Manage a collaborator's project access](/en/user-accounts-and-teams/role-based-access/managing-team-collaborators#manage-a-collaborator-s-project-access).

---
