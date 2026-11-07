# Organization & workspaces

54 pages. Paths are relative to the repository root.


## Organization & workspaces

- **Automation HQ** - `kb/docs/en/automation-hq.md` - Automation HQ gives you central control over managed workspaces, so you can provision team hierarchies, share assets, and govern usage and quotas.
- **Organization and workspaces** - `kb/docs/en/organization-workspaces.md` - Learn how Workato organizations and workspaces structure automation projects, support collaboration, and scale with Automation HQ and workspace provisioning.
- **Workspace collaboration** - `kb/docs/en/user-accounts-and-teams/team-collaboration.md` - Manage who can build, edit, and run integrations in a Workato workspace by inviting collaborators and assigning roles and access controls.
- **Workspace quotas** - `kb/docs/en/user-accounts-and-teams/workspace-limits.md` - Reference for Workato workspace quotas, including general workspace, environment property, and project property quotas.
- **Workspace provisioning** - `kb/docs/en/user-accounts-and-teams/workspace-provisioning.md` - Learn how Workato provisions workspaces for direct customers, including activation link emails, notification emails, and audit log tracking.
- **Workspace** - `kb/docs/en/workspace.md` - Learn how a Workato workspace organizes projects, recipes, and tools so your team can collaborate, build automations, and deploy them across your organization.

## Automation HQ

- **Audit log streaming for Automation HQ** - `kb/docs/en/ahq-audit-log-streaming.md` - Set up audit log streaming in Automation HQ to send logs from all current and future managed workspaces to a single external log provider.
- **AHQ AWS IAM role sharing** - `kb/docs/en/ahq-aws-iam-role-sharing.md` - Enable AWS IAM role sharing in Automation HQ to propagate the admin environment external ID to child workspaces for easier IAM role management.
- **HQ Workspace** - `kb/docs/en/ahq-hq-workspace.md` - The Automation HQ Workspace lets you manage quotas, settings, moderators, and monitor automations across all managed workspaces in your Workato account.
- **Create a workspace in Automation HQ** - `kb/docs/en/ahq-managed-workspace-create.md` - Create a managed workspace in Workato Automation HQ, set its name, and allocate billable recipe and task quotas from your organization subscription.
- **Managed Workspace** - `kb/docs/en/ahq-managed-workspace.md` - Learn how managed workspaces in Workato Automation HQ organize recipes and assets by department, with independent environments, users, and roles.
- **Automation HQ settings** - `kb/docs/en/ahq-settings.md` - Configure Automation HQ settings in Workato, including organization-wide audit log streaming and cross-workspace grants for sharing Event streams topics.
- **Share a connector** - `kb/docs/en/ahq-shared-connector-share.md` - Share a custom connector across your organization in Workato Automation HQ, choosing open source or proprietary closed source code for distribution.
- **Stop sharing a connector** - `kb/docs/en/ahq-shared-connector-stop-sharing.md` - Stop sharing a custom connector with workspaces in your organization through the Shared connectors tab in Workato Automation HQ.
- **Version a connector** - `kb/docs/en/ahq-shared-connector-version.md` - Update a shared custom connector to a new version across your organization from the Shared connectors tab in Workato Automation HQ.
- **Shared connectors** - `kb/docs/en/ahq-shared-connector.md` - Learn how shared connectors in Workato Automation HQ let admins build, share, and maintain custom connectors so all workspaces use the latest versions.
- **Configure SSO for AHQ workspaces** - `kb/docs/en/ahq-sso.md` - Configure SAML-based Single Sign-On for Workato Automation HQ workspaces and their child workspaces, with separate setup for each child workspace.
- **Automation HQ usage** - `kb/docs/en/ahq-usage.md` - Learn how Automation HQ in Workato consolidates billing and pooled task quotas, with plan overview, task usage, and recipe usage charts across workspaces.
- **Assign a workspace moderator** - `kb/docs/en/ahq-workspace-moderator-assign.md` - Assign a new workspace moderator in Automation HQ and grant them environment and project roles to manage your organization's workspaces.
- **Edit or remove a workspace moderator** - `kb/docs/en/ahq-workspace-moderator-edit.md` - Edit a workspace moderator's environment role, project role, and workspace access in Automation HQ, or remove the moderator to revoke access.
- **Workspace moderators** - `kb/docs/en/ahq-workspace-moderator.md` - Learn how workspace moderators in Automation HQ administer managed workspaces, support collaborators, and use environment and project roles.

## Workspace collaborators

- **Teams - Collaborator Privileges** - `kb/docs/en/privileges.md` - Reference for Workato collaborator privileges, detailing the permissions each role has across recipe development, platform tools, and admin features.
- **Teams - Collaborator roles** - `kb/docs/en/roles.md` - Reference for Workato collaborator roles, including built-in system roles and custom roles that control access to features and folders.
- **SAML role sync in Microsoft Entra ID** - `kb/docs/en/saml-role-sync-azure.md` - Configure Microsoft Entra ID to sync Workato environment roles and collaborator groups through SAML attribute mapping at user sign-in.
- **CyberArk Identity SAML role sync configuration** - `kb/docs/en/saml-role-sync-cyberark-idaptive.md` - Configure CyberArk Identity to sync Workato roles through SAML SSO so user roles update across DEV, PROD, and TEST environments at login.
- **SAML role sync in Okta** - `kb/docs/en/saml-role-sync-okta.md` - Configure Okta to sync Workato environment roles and collaborator groups through SAML attributes for DEV, PROD, and TEST environments.
- **SAML role sync in OneLogin** - `kb/docs/en/saml-role-sync-onelogin.md` - Configure OneLogin to sync Workato role assignments for users and groups through SAML across DEV, PROD, and TEST environments.
- **Configure and use SCIM in Microsoft Entra ID** - `kb/docs/en/scim-azure-ad.md` - Configure SCIM 2.0 in Microsoft Entra ID to automate user provisioning, deprovisioning, and attribute mapping with Workato.
- **SCIM FAQs** - `kb/docs/en/scim-faqs.md` - Answers to common questions about using SCIM 2.0 with Workato, including benefits, prerequisites, provisioning, and supported features.
- **Configure and use SCIM in Okta** - `kb/docs/en/scim-okta.md` - Configure SCIM 2.0 in Okta to automate Workato user lifecycle management while SAML handles roles and group assignments.
- **Configure and use SCIM in OneLogin** - `kb/docs/en/scim-onelogin.md` - Configure SCIM 2.0 in OneLogin to automate user provisioning and deprovisioning for your Workato workspace.
- **SCIM troubleshooting** - `kb/docs/en/scim-troubleshooting.md` - Use this guide to troubleshoot errors that occur when using System for Cross-domain Identity Management (SCIM) provisioning in Workato.
- **System for Cross-domain Identity Management (SCIM 2.0)** - `kb/docs/en/scim.md` - Workato supports SCIM 2.0 to securely automate user provisioning, deprovisioning, and profile updates from identity providers like Okta and OneLogin.
- **Team - Just in time provisioning** - `kb/docs/en/user-accounts-and-teams/just-in-time-provisioning.md` - Set up SAML just-in-time provisioning in Workato to automatically add team members to your workspace and assign roles and groups.
- **Manage your workspace collaborators with role-based access control** - `kb/docs/en/user-accounts-and-teams/role-based-access.md` - Manage who can access your Workato workspace, environments, and projects using role-based access control across both permissions models.
- **Manage workspace collaborators with role-based access control** - `kb/docs/en/user-accounts-and-teams/role-based-access/access-control-v2.md` - Learn how the Workato role-based access control model uses environment roles, project roles, custom roles, and collaborator groups.
- **Workspaces - Managing Workspace Collaborators** - `kb/docs/en/user-accounts-and-teams/role-based-access/managing-team-collaborators.md` - Invite, manage, and remove collaborators in a Workato workspace, and assign roles and collaborator groups to control project access.
- **Migrate to the new access control model** - `kb/docs/en/user-accounts-and-teams/role-based-access/migrate-roles.md` - Migrate legacy collaborator roles to the new Workato access control model using the bulk-migration tool to create environment and project roles.
- **Collaborator groups** - `kb/docs/en/user-accounts-and-teams/role-based-access/new-model/collaborator-groups.md` - Learn how collaborator groups in Workato assign project roles to sets of users at once and how stacked group permissions are applied.
- **Privileges reference** - `kb/docs/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference.md` - Reference for Workato environment-level and project-level privileges, covering what each controls and its dependencies for custom roles.
- **Environment roles** - `kb/docs/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles.md` - Reference for Workato environment roles, including Environment admin, Environment manager, and Member, and the privileges each role grants.
- **Project roles** - `kb/docs/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles.md` - Reference for Workato project roles, including Project admin, Advanced builder, Builder, and Project operator, and the access each provides.
- **Role-based access control FAQs** - `kb/docs/en/user-accounts-and-teams/role-based-access/permission-model-faqs.md` - Answers to common questions about the new Workato permission model, including environment roles, project roles, and default system roles.
- **SAML role sync** - `kb/docs/en/user-accounts-and-teams/saml-role-sync.md` - Learn how SAML role sync maps identity provider attributes to Workato environment roles, workspace roles, and collaborator groups automatically.
- **Enable Single Sign-On For A Workato Workspace** - `kb/docs/en/user-accounts-and-teams/single-sign-on.md` - Set up SAML-based Single Sign-On for a Workato workspace to provide authorized access for members and enable just-in-time provisioning.
- **Troubleshoot Single Sign-On For A Workato Workspace** - `kb/docs/en/user-accounts-and-teams/troubleshoot-sso.md` - Troubleshoot common SAML-based Single Sign-On errors in Workato, including workspace switching, login, and case-sensitive username issues.

## Workspaces

- **Data masking** - `kb/docs/en/features/data-masking.md` - Learn how data masking in Workato hides sensitive trigger and step data so collaborators cannot view it in job history or audit logs.
- **Profile settings** - `kb/docs/en/profile-settings.md` - Manage your Workato profile settings to customize account preferences, security options, language, time zone, and workspace memberships.
- **Two-factor authentication FAQs** - `kb/docs/en/security/two-factor-authentication-faqs.md` - Answers to common questions about two-factor authentication in Workato, including authenticator apps and recovery codes.
- **Two-factor authentication** - `kb/docs/en/security/two-factor-authentication.md` - Learn how two-factor authentication works in Workato and how to set it up using an authenticator app and recovery codes.
- **Single Sign-On (SSO)** - `kb/docs/en/signing-up/sso.md` - Learn how single sign-on works in Workato using SAML 2.0 with identity providers such as Google Workspace, Microsoft Entra ID, and Okta.
- **Managing teams - Email notifications** - `kb/docs/en/user-accounts-and-teams/admin-email.md` - Learn how to assign Workato email notification contacts for admin, technical, error, legal, and billing alerts across workspaces and environments.
- **Update account email** - `kb/docs/en/user-accounts-and-teams/update-account-email.md` - Update the email address tied to your personal Workato account profile, the address you use to authenticate, and verify the change.
- **Workspace admin settings** - `kb/docs/en/workspace-admin-settings.md` - Reference for Workato workspace admin settings, covering workspace configuration, authentication, notifications, security, and debug and logging options.
