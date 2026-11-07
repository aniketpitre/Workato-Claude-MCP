---
url: 'https://docs.workato.com/en/workato-identity/user-groups.md'
description: >-
  Create and manage end-user groups in Workato Identity, assign environment
  access, and scope user access more securely across your workspace.
---

# End-user group management

Workato Identity enables you to create and manage end-user groups. You can store end-users and end-user groups with customized environment access and assign access to specific groups. This lets you scope user access more securely.

You can also enable [user group syncing](/en/workato-identity/user-group-syncing) to automatically update user group memberships in Workato based on group information from your identity provider.

## End-user groups

End-user groups are created within specific environments. You must [add end-users to your external IdP](/en/workato-identity/identity-provider-user-access) or [add end-users manually](/en/workato-identity/add-end-user-manually) before you can assign them to a user group. Each end-user group must have at least one end user assigned to it.

### Create an end-user group

End-user groups are specific to each environment. You must select the environment before you can create a group.

> **ENVIRONMENT AVAILABILITY**
> 
> Workspaces without [Environments](/en/features/environments) provisioned only have one environment available.

Complete the following steps to create an end-user group in an environment:

1. Sign in to Workato.
   
2. Click **Workspace admin** in the sidebar. The **Access control** page displays by default.
   
3. Click **Authentication & Groups** in the sidebar.
   
4. Select the environment where you plan to create a group. The environment **End-user group** page displays by default.
   
   ![Select the environment](/assets/workato-identity-environments.CUpB5QYz.png)_Select the environment_
   
5. Click **\+ Create end-user group**.
   
   ![Click Create end-user group](/assets/create-end-user-group.BSRIRJMg.png)_Click **\+ Create end-user group**_
   
6. Provide a name for the group in the **Group name** field.
   
   ![Create end-user group](/assets/end-user-group-management.Dgp5IkSV.png)_Create the end-user group_
   
7. Select the end-users you plan to add to the end-user group. Each end-user group must include at least one end user.
   
8. Click **Create**.
   

### Grant access to users and groups

You can provide individual users and groups with feature access.

Complete the following steps grant access to users and groups:

1. Sign in to Workato.
   
2. Go to **End user access** page of the feature where you plan to add user or group access. For example:
   
   - Go to **AI Hub > Agent Studio**, select the genie, and go to **End user access**.
   - Go to **AI Hub > Enterprise MCP > Custom servers**, select the MCP server, and go to **Settings > End user access**.
3. Click **Add end users**.
   
4. Select the individual users or groups you plan to provide with feature access.
   
   ![Select individual users or groups](/assets/add-end-users.D4FvRGsM.png)_Select individual users or groups_
   
5. Click **Add**.
   

### Revoke user access to an environment

You can revoke user access to a specific environment if permissions are no longer needed.

Complete the following steps to revoke user access to an environment:

1. Sign in to Workato.
   
2. Click **End users** in the sidebar.
   
3. Search for and select the user profile where you plan to revoke environment access.
   
4. Deselect the environment checkbox to remove user access.
   
   ![Remove environment access](/assets/remove-environment-access.CtSF9NJz.png)_Remove environment access_
   
5. Select the checkbox in the revoke access confirmation screen when prompted.
   
   ![Select the checkbox in the revoke access confirmation screen when prompted](/assets/revoke-access.Dg-uXMpy.png)_Select the checkbox in the revoke access confirmation screen_
   
6. Click **Save**.
   

## End-user group quotas

| Description | Quota |
| --- | --- |
| Time for adding a user to an end-user group, removing a user from a group, or removing a user from a workspace to take effect | Up to 1 hour |

---
