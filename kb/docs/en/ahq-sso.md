---
url: 'https://docs.workato.com/en/ahq-sso.md'
description: >-
  Configure SAML-based Single Sign-On for Workato Automation HQ workspaces and
  their child workspaces, with separate setup for each child workspace.
---

# Configure Single Sign-On for Automation HQ workspaces

Workato supports SAML-based Single Sign-On (SSO) for Automation HQ (AHQ) workspaces, including child workspaces. Workato recommends enabling SSO for AHQ and child workspaces. You must enable SSO separately for each child workspace. Even if your AHQ workspace has SSO enabled, this doesn't automatically enable SSO for all child workspaces. Refer to [Create a workspace in Automation HQ](/en/ahq-managed-workspace-create) for more information about creating workspaces.

Complete the following steps to configure SSO for AHQ workspaces:

- Complete the [setup instructions](/en/user-accounts-and-teams/single-sign-on) for your identity provider (IdP).
- Complete the [configuration instructions](/en/user-accounts-and-teams/single-sign-on#workato-single-sign-on-setup) in Workato.

> **SSO FOR CHILD WORKSPACES**
> 
> You must configure each AHQ child workspace separately in your IdP. Refer to the [AHQ child workspaces](#ahq-child-workspaces) for more information.

## AHQ child workspaces

You must configure each child workspace as a separate app and assign it to a unique group in your IdP to enable SSO.

For each child workspace:

- Complete the [setup instructions](/en/user-accounts-and-teams/single-sign-on) for your identity provider (IdP).
- Complete the [configuration instructions](/en/user-accounts-and-teams/single-sign-on#workato-single-sign-on-setup) in Workato.
- [Create a separate group](/en/workflow-apps/app-user-groups#organize-users-groups) for each child workspace where you plan to enable SSO.

---
