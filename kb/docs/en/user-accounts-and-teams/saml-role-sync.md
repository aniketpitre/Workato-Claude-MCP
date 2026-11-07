---
url: 'https://docs.workato.com/en/user-accounts-and-teams/saml-role-sync.md'
description: >-
  Learn how SAML role sync maps identity provider attributes to Workato
  environment roles, workspace roles, and collaborator groups automatically.
---

# SAML role sync: maintaining Workato roles in the identity provider

Managing access across multiple SaaS applications, such as Workato, can be complex and error-prone. For example, you may face challenges in the following areas:

- User lifecycle
  
- Provisioning, changing user roles, and deprovisioning become increasingly difficult as your organization scales, especially when many custom roles exist.
  
- Security
  
- Enforcing consistent organization-wide security policies for Workato can be challenging because of manual role configuration steps.
  
- Lack of automation
  
- Most applications require configuration to automate user provisioning and permissions.
  

To address these challenges, Workato supports SAML role sync for both workspaces using the legacy permissions model and workspaces using the new permission model. How roles and project-level access are assigned depends on your workspace configuration.

> **SAML ROLE SYNC CONFIGURATIONS**
> 
> Workato supports two different SAML role sync configurations depending on your workspace setup:
> 
> - **Legacy permissions model**: Use the `workato_role`, `workato_role_test`, and `workato_role_prod` attributes to assign workspace-level roles directly through SAML.
>   
> - **New permissions model**: Use the same `workato_role`, `workato_role_test`, and `workato_role_prod` attributes to assign environment roles in DEV, TEST, and PROD. Additionally, you can use the `workato_user_groups` attribute to assign users to collaborator groups for project-level access. Environment roles and project-level access are managed separately.
>   

## How SAML role sync works

Workato synchronizes user roles with the SAML attributes you configure in your identity provider (IdP):

- In workspaces using the legacy permissions model, the attributes `workato_role`, `workato_role_test`, and `workato_role_prod` map users to workspace-level system roles (for example, **Admin**, **Analyst**, **Operator**, or custom roles).
- In workspaces using the new permissions model, the same attributes map users to environment roles (for example, **Environment admin**, **Environment manager**, or **Member**). You can also use `workato_user_groups` to assign users to collaborator groups for project-level access.

Workato automatically synchronizes these assignments whenever you update the mapped SAML attributes in your identity provider.

For example, you can change a user's `workato_role` attribute from **Environment admin** to **Member** inside the IdP, and Workato automatically updates their environment permissions. Similarly, if you assign a user to the `Analytics_Team` collaborator group using `workato_user_groups`, Workato adds them to that group, and the user inherits the project-level permissions defined for it.

Workato supports SAML role sync for all customers who enable SSO on their identity provider. In this document, we describe how to use SAML role sync for the following identity providers:

- [Okta](/en/saml-role-sync-okta)
- [Microsoft Azure](/en/saml-role-sync-azure)
- [OneLogin](/en/saml-role-sync-onelogin)
- [CyberArk Identity](/en/saml-role-sync-cyberark-idaptive)

We support SAML role sync in all regions.

> **Recommendation**
> 
> Workato strongly recommends that you manage user role assignment through your identity provider after configuring the role sync, because the system overwrites manual role changes.

## Support for environment-specific roles

If you have [environments](/en/features/environments) enabled with Workato (through the Lifecycle Management feature), you can sync environment-specific user roles from your IdP. Workato defines the following custom attributes that map to specific environment roles:

- DEV `workato_role`
- TEST `workato_role_test`
- PROD `workato_role_prod`

In workspaces using the legacy permissions model, these attributes map directly to workspace-level roles (**Admin**, **Analyst**, **Operator**, or custom roles).

In workspaces using the new permissions model, these attributes map to environment roles such as **Environment admin**, **Environment manager**, or **Member**. These attributes are still required even if you also use `workato_user_groups` for project-level access.

## Project-level access through collaborator groups

In workspaces using the new permissions model, you can assign users to collaborator groups by syncing the `workato_user_groups` attribute through your identity provider.

For example, if you map a user to the `Analytics_Team` collaborator group in Okta, Workato automatically assigns the user to that group, and they inherit the project-level permissions configured for that group within Workato.

## Enable role sync

To use the role sync with your identity provider, you must enable the feature in the Workato interface.

> **Recommendation**
> 
> If not already turned on, we recommend enabling the **Enforce SAML authentication** and **Enable SAML JIT provisioning** options at the same time.

1. Go to **Workspace admin > Settings > Login methods**.
   
2. Enable the **Enable role sync** toggle.
   
   _Enable role sync in Workato_
   
3. Click **Validate settings**.
   
4. Click **Save**.
   

## Next steps

Complete role sync set-up on your identity provider. In this section, we describe how to connect to the following:

- [Okta](/en/saml-role-sync-okta)
- [Microsoft Azure](/en/saml-role-sync-azure)
- [OneLogin](/en/saml-role-sync-onelogin)
- [CyberArk Identity](/en/saml-role-sync-cyberark-idaptive)

---
