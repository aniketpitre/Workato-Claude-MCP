---
url: 'https://docs.workato.com/en/oem/workspace-structure.md'
description: >-
  Learn the Embedded workspace structure, including the admin workspace,
  customer workspaces, collaborators, and customer managers.
---

# Embedded workspace structure

The following defines the typical workspace structure for Embedded partners and their customers: ![Embedded workspace structure](/assets/jwt-account-heirarchy.DCikFa5O.png)_Workspace hierarchy for Embedded partners_

- Admin workspace
- The Embedded partner uses the admin workspace to manage internal development tasks, such as creating and testing customer-facing integrations, and to oversee workspaces through the **Admin console**.

> **BETA ACCESS**
> 
> Embedded partners must sign in with a workspace that has the [Environment admin](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles#environment-admin) or the legacy [Admin role](/en/roles#role-admin). Go to **Workspace admin > Settings > Workato AI** to enable features such as [Copilot](/en/ai-features/copilot).

- Customer workspaces
- Customer workspaces are created and managed by the Embedded partner for each individual customer. In these dedicated workspaces, customers can collaboratively build and manage integrations, or the Embedded partner's customer managers can do so on their behalf.

> **CUSTOMER WORKSPACE LIMIT**
> 
> Each Embedded partner has a default quota of 10,000 customer workspaces.

- Collaborators
  
- Collaborators are users who have accepted an invitation to an admin or customer workspace. A collaborator's [role](/en/user-accounts-and-teams/role-based-access/) determines their access to folders, features, and the [Admin console](/en/oem/admin-console).
  
- Customer managers
  
- [Customer managers](/en/oem/admin-console/customer-managers) are collaborators within the Embedded partner's admin workspace who have access to manage customer workspaces. The Embedded partner assigns customer managers through the **Admin console**, selecting the specific customer workspaces they can access and granting inheritable roles that apply when the customer manager accesses those workspaces.

---
