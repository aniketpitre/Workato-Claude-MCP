---
url: >-
  https://docs.workato.com/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles.md
description: >-
  Reference for Workato environment roles, including Environment admin,
  Environment manager, and Member, and the privileges each role grants.
---

# Environment roles

Environment roles define a collaborator's permissions within a specific environment. These roles control access to platform tools, environment settings, and administrative functions, but don't grant access to project content.

You can assign different environment roles to the same collaborator in different environments. For example, a DevOps engineer can have **Environment admin** in Development, **Member** in Testing, and **No access** in Production.

> **PROJECT ACCESS**
> 
> Environment roles don't include project access. Assign a project role to allow collaborators to view, edit, or manage project content.

Workato provides the following default environment roles:

| Type | Description |
| --- | --- |
| Environment admin | Full control over workspace-wide and environment settings. |
| Environment manager | Full control over environment settings, but no workspace-wide permissions. |
| Member | View-only access to environment settings. |

Use the following guides to review the full set of privileges for each role:

- [Environment admin](#environment-admin)
- [Environment manager](#environment-manager)
- [Member](#member)

## Environment admin

The **Environment admin** role grants full administrative access within a specific environment. Assign this role to collaborators who manage projects, configure platform features, and control access within the environment.

Environment admins can perform the following actions in their assigned environment:

- [Create and manage](#project-management) projects in the environment
- [Manage project membership](#project-management), including adding or removing collaborators and assigning project roles
- [Configure tools](#tools) like Workbot, Logs, and Message templates
- Manage shared features such as data storage, the API platform, Apps portal, and Insights
- [Assign environment roles](#workspace-access) to other users

Environment admins can't access or edit the contents of a project, such as recipes or assets, unless also assigned a [project role](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles) that explicitly grants those permissions.

The following tables list the full set of privileges included in the **Environment admin** role. Each section describes the tools or features the privileges control.

### Platform tools privileges

The following privileges control environment-level tools and features shared across multiple projects. They include configuration access for core tools, project management, and on-prem systems.

#### Project management

These privileges control whether a collaborator can create projects and manage access to all projects in the environment. When a user creates a project, Workato automatically assigns them the [Project admin](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles#project-admin) role for that project.

| Privilege | Full access | Create | Access control |
| --- | --- | --- | --- |
| Manage projects | ✔ | ✔ | ✔ |

#### Tools

These privileges control access to shared environment-level tools and resources used across recipes. They include configuration access for components such as OAuth profiles, lifecycle management, and event streams.

| Privilege | Full access | View | Edit | Create | Delete | View history | Manage access |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Common data models | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Custom OAuth profiles | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Message templates | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Event streams | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  |
| Recipe lifecycle management | ✔ |  |  |  |  |  |  |
| Workbot | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Enterprise Workbot | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Runtime user connections | ✔ | ✔ | ✔ |  | ✔ |  |  |
| Logs | ✔ |  |  |  |  |  |  |
| File Storage | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Workato GO | ✔ | ✔ | ✔ |  |  |  | ✔ |

#### On-premise

These privileges control access to on-premise features, including agent management, file-based connections, and command line scripts.

| Privilege | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| On-prem groups & agents | ✔ | ✔ | ✔ | ✔ | ✔ |
| Connection - on-prem files | ✔ |  |  |  |  |
| Connection - command line scripts | ✔ |  |  |  |  |

#### Apps portal

These privileges control group management and access to related workspace settings through the apps portal.

| Privilege | Full access |
| --- | --- |
| Settings | ✔ |
| Users and groups | ✔ |

#### Data storage

These privileges control access to environment-level data, including lookup tables and environment properties.

| Privilege | Full access | View | Edit records | Create | Delete | Modify structure |
| --- | --- | --- | --- | --- | --- | --- |
| Lookup tables | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Environment properties | ✔ | ✔ | ✔ | ✔ | ✔ |  |
| Configurable data retention | ✔ |  |  |  |  |  |

#### API platform

These privileges control access to API platform features such as endpoint management, API clients, logs, and the ability to build and manage APIs within the environment.

| Privilege | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| Dashboard & logs | ✔ |  |  |  |  |
| Collections & endpoints | ✔ | ✔ | ✔ | ✔ | ✔ |
| Client & access profiles | ✔ | ✔ | ✔ | ✔ | ✔ |
| Policies | ✔ | ✔ | ✔ | ✔ | ✔ |
| Settings | ✔ |  |  |  |  |

#### Connector SDK

These privileges control access to develop and manage custom SDK connectors and use them in recipes.

| Privilege | Full access |
| --- | --- |
| Connector SDK | ✔ |
| Use in recipes | ✔ |

#### Insights

These privileges control access to Insights dashboards to monitor recipe usage, errors, and performance.

| Privilege | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| Insights | ✔ | ✔ | ✔ | ✔ | ✔ |

### Admin privileges

These privileges control administration at the workspace and environment level, including access to user roles, APIs, and security configurations that extend beyond individual projects.

#### Workspace access

These privileges control access to manage collaborators, workspace-level settings, and API clients that can modify workspaces.

| Privilege | Full access |
| --- | --- |
| Collaborators | ✔ |
| Collaborator roles (non-system) | ✔ |
| Collaborator SAML SSO auth | ✔ |
| Developer API | ✔ |
| SCIM provisioning | ✔ |
| Workspace settings | ✔ |

#### Environment settings

These privileges control access to environment-level security settings and audit logs. They include visibility into all team activity in the environment, regardless of platform tools or project access.

| Privilege | Full access |
| --- | --- |
| Activity audit | ✔ |
| Audit log replication | ✔ |
| Debug, Log and Security | ✔ |
| Manage locked projects | ✔ |

#### Billing & usage

These privileges control access to the Billing & Usage dashboard.

| Privilege | Full access |
| --- | --- |
| Usage dashboard | ✔ |

### Automation HQ privileges

This privilege grants access to the Automation HQ console for managing enterprise automation programs and initiatives.

| Privilege | Full access |
| --- | --- |
| Automation HQ | ✔ |

### Solutions access

These privileges control authentication, end-user groups, and identity management for solutions such as Workato GO, Genies, and Low Code App. They include configuration of authentication methods, SSO, and user/group assignments.

| Privilege | Full access |
| --- | --- |
| Authentication settings and SSO | ✔ |
| End users and groups | ✔ |

### XChange

The **XChange** tab controls permissions to create, curate, and consume packages in [XChange](/en/xchange), Workato's package management and distribution platform.

#### Package creation

| Privilege | Full access | View | Edit | Create |
| --- | --- | --- | --- | --- |
| Version | ✔ | ✔ | ✔ | ✔ |

#### Curation

| Privilege | Full access | View | Edit | Delete | Publish/Distribute | Review | Share |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Packages | ✔ |  |  | ✔ | ✔ | ✔ | ✔ |
| Settings | ✔ | ✔ | ✔ |  |  |  |  |

#### Consumption

| Privilege | Full access | View | Install |
| --- | --- | --- | --- |
| Verified Packages | ✔ | ✔ | ✔ |

## Environment manager

The **Environment manager** role provides administrative control over environment-level settings and platform tools, but excludes workspace-wide privileges and project-level access. Assign this role to collaborators who maintain environment configurations and create new projects, without needing full administrative control.

Environment managers can perform the following actions in their assigned environment:

- [Create new projects](#project-management) in the environment
- [Configure platform tools](#tools) such as Workbot and OAuth profiles
- Manage shared features such as data storage, the API platform, Apps portal, and Insights

Environment managers can't configure workspace settings or manage users across environments. They also can't access or edit project content, such as recipes or assets, unless also assigned a [project role](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles) that explicitly grants those permissions.

The following tables list the full set of privileges included in the **Environment manager** role. Each section describes the tools or features the privileges control.

### Platform tools privileges

The following privileges control environment-level tools and features shared across multiple projects. They include configuration access for core tools, project management, and on-prem systems.

#### Project management

These privileges control whether a collaborator can create projects and manage access to all projects in the environment. When a user creates a project, Workato automatically assigns them the [Project admin](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles#project-admin) role for that project.

| Privilege | Full access | Create | Access control |
| --- | --- | --- | --- |
| Manage projects | ❌ | ✔ | ❌ |

#### Tools

These privileges control access to shared environment-level tools and resources used across recipes. They include configuration access for components such as OAuth profiles, lifecycle management, and event streams.

| Privilege | Full access | View | Edit | Create | Delete | View history | Manage access |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Common data models | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Custom OAuth profiles | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Message templates | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Event streams | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  |
| Recipe lifecycle management | ❌ |  |  |  |  |  |  |
| Workbot | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Enterprise Workbot | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Runtime user connections | ✔ | ✔ | ✔ |  | ✔ |  |  |
| Logs | ❌ |  |  |  |  |  |  |
| File Storage | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Workato GO | ❌ | ❌ | ❌ |  |  |  | ❌ |

#### On-premise

These privileges control access to on-premise features, including agent management, file-based connections, and command line scripts.

| Privilege | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| On-prem groups & agents | ✔ | ✔ | ✔ | ✔ | ✔ |
| Connection - on-prem files | ✔ |  |  |  |  |
| Connection - command line scripts | ✔ |  |  |  |  |

#### Apps portal

These privileges control group management and access to related workspace settings through the apps portal.

| Privilege | Full access |
| --- | --- |
| Settings | ✔ |
| Users and groups | ✔ |

#### Data storage

These privileges control access to environment-level data, including lookup tables and environment properties.

| Privilege | Full access | View | Edit records | Create | Delete | Modify structure |
| --- | --- | --- | --- | --- | --- | --- |
| Lookup tables | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Environment properties | ✔ | ✔ | ✔ | ✔ | ✔ |  |
| Configurable data retention | ❌ |  |  |  |  |  |

#### API platform

These privileges control access to API platform features such as endpoint management, API clients, logs, and the ability to build and manage APIs within the environment.

| Privilege | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| Dashboard & logs | ✔ |  |  |  |  |
| Collections & endpoints | ✔ | ✔ | ✔ | ✔ | ✔ |
| Client & access profiles | ✔ | ✔ | ✔ | ✔ | ✔ |
| Policies | ✔ | ✔ | ✔ | ✔ | ✔ |
| Settings | ✔ |  |  |  |  |

#### Connector SDK

These privileges control access to develop and manage custom SDK connectors and use them in recipes.

| Privilege | Full access |
| --- | --- |
| Connector SDK | ✔ |
| Use in recipes | ✔ |

#### Insights

These privileges control access to Insights dashboards to monitor recipe usage, errors, and performance.

| Privilege | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| Insights | ✔ | ✔ | ✔ | ✔ | ✔ |

### Admin privileges

These privileges control administration at the workspace and environment level, including access to user roles, APIs, and security configurations that extend beyond individual projects.

#### Workspace access

These privileges control access to manage collaborators, workspace-level settings, and API clients that can modify workspaces.

| Privilege | Full access |
| --- | --- |
| Collaborators | ❌ |
| Collaborator roles (non-system) | ❌ |
| Collaborator SAML SSO auth | ❌ |
| Developer API | ❌ |
| SCIM provisioning | ❌ |
| Workspace settings | ❌ |

#### Environment settings

These privileges control access to environment-level security settings and audit logs. They include visibility into all team activity in the environment, regardless of platform tools or project access.

| Privilege | Full access |
| --- | --- |
| Activity audit | ❌ |
| Audit log replication | ❌ |
| Debug, Log and Security | ❌ |
| Manage locked projects | ❌ |

#### Billing & usage

These privileges control access to the Billing & Usage dashboard.

| Privilege | Full access |
| --- | --- |
| Usage dashboard | ❌ |

### Automation HQ privileges

This privilege grants access to the Automation HQ console for managing enterprise automation programs and initiatives.

| Privilege | Full access |
| --- | --- |
| Automation HQ | ❌ |

### Solutions access

These privileges control authentication, end-user groups, and identity management for solutions such as Workato GO, Genies, and Low Code App. They include configuration of authentication methods, SSO, and user/group assignments.

| Privilege | Full access |
| --- | --- |
| Authentication settings and SSO | ❌ |
| End users and groups | ❌ |

### XChange

The **XChange** tab controls permissions to create, curate, and consume packages in [XChange](/en/xchange), Workato's package management and distribution platform.

#### Package creation

| Privilege | Full access | View | Edit | Create |
| --- | --- | --- | --- | --- |
| Version | ❌ | ❌ | ❌ | ❌ |

#### Curation

| Privilege | Full access | View | Edit | Delete | Publish/Distribute | Review | Share |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Packages | ❌ |  |  | ❌ | ❌ | ❌ | ❌ |
| Settings | ❌ | ❌ | ❌ |  |  |  |  |

#### Consumption

| Privilege | Full access | View | Install |
| --- | --- | --- | --- |
| Verified Packages | ❌ | ❌ | ❌ |

## Member

The **Member** role grants limited, view-only visibility in an environment. Assign this role to users who need visibility into an environment without permission to make changes.

Members can perform the following actions:

- View basic environment information.
- Reference shared assets for context.

Members can't edit, create, or delete tools or settings at the environment level. They also can't access project content unless assigned a [project role](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles).

The following tables list the full set of privileges included in the **Member** role. Each section describes the tools or features the privileges control.

### Platform tools privileges

The following privileges control environment-level tools and features shared across multiple projects. They include configuration access for core tools, project management, and on-prem systems.

#### Project management

These privileges control whether a collaborator can create projects and manage access to all projects in the environment. When a user creates a project, Workato automatically assigns them the [Project admin](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles#project-admin) role for that project.

| Privilege | Full access | Create | Access control |
| --- | --- | --- | --- |
| Manage projects | ❌ | ❌ | ❌ |

#### Tools

These privileges control access to shared environment-level tools and resources used across recipes. They include configuration access for components such as OAuth profiles, lifecycle management, and event streams.

| Privilege | Full access | View | Edit | Create | Delete | View history | Manage access |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Common data models | ❌ | ❌ | ❌ | ❌ | ❌ |  |  |
| Custom OAuth profiles | ❌ | ❌ | ❌ | ❌ | ❌ |  |  |
| Message templates | ❌ | ❌ | ❌ | ❌ | ❌ |  |  |
| Event streams | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |  |
| Recipe lifecycle management | ❌ |  |  |  |  |  |  |
| Workbot | ❌ | ❌ | ❌ | ❌ | ❌ |  |  |
| Enterprise Workbot | ❌ | ❌ | ❌ | ❌ | ❌ |  |  |
| Runtime user connections | ❌ | ❌ | ❌ |  | ❌ |  |  |
| Logs | ❌ |  |  |  |  |  |  |
| File Storage | ❌ | ❌ | ❌ | ❌ | ❌ |  |  |
| Workato GO | ❌ | ❌ | ❌ |  |  |  | ❌ |

### On-premise

These privileges control access to on-premise features, including agent management, file-based connections, and command line scripts.

| Privilege | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| On-prem groups & agents | ❌ | ❌ | ❌ | ❌ | ❌ |
| Connection - on-prem files | ❌ |  |  |  |  |
| Connection - command line scripts | ❌ |  |  |  |  |

#### Apps portal

These privileges control group management and access to related workspace settings through the apps portal.

| Privilege | Full access |
| --- | --- |
| Settings | ❌ |
| Users and groups | ❌ |

#### Data storage

These privileges control access to environment-level data, including lookup tables and environment properties.

| Privilege | Full access | View | Edit records | Create | Delete | Modify structure |
| --- | --- | --- | --- | --- | --- | --- |
| Lookup tables | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Environment properties | ❌ | ❌ | ❌ | ❌ | ❌ |  |
| Configurable data retention | ❌ |  |  |  |  |  |

#### API platform

These privileges control access to API platform features such as endpoint management, API clients, and logs. These privileges control who can build and manage APIs within the environment.

| Privilege | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| Dashboard & logs | ❌ |  |  |  |  |
| Collections & endpoints | ❌ | ❌ | ❌ | ❌ | ❌ |
| Client & access profiles | ❌ | ❌ | ❌ | ❌ | ❌ |
| Policies | ❌ | ❌ | ❌ | ❌ | ❌ |
| Settings | ❌ |  |  |  |  |

#### Connector SDK

These privileges control access to develop and manage custom SDK connectors and use them in recipes.

| Privilege | Full access |
| --- | --- |
| Connector SDK | ❌ |
| Use in recipes | ✔ |

#### Insights

These privileges control access to Insights dashboards to monitor recipe usage, errors, and performance.

| Privilege | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| Insights | ❌ | ❌ | ❌ | ❌ | ❌ |

### Admin privileges

These privileges control administration at the workspace and environment level, including access to user roles, APIs, and security configurations that extend beyond individual projects.

#### Workspace access

These privileges control access to manage collaborators, workspace-level settings, and API clients that can modify workspaces.

| Privilege | Full access |
| --- | --- |
| Collaborators | ❌ |
| Collaborator roles (non-system) | ❌ |
| Collaborator SAML SSO auth | ❌ |
| Developer API | ❌ |
| SCIM provisioning | ❌ |
| Workspace settings | ❌ |

#### Environment settings

These privileges control access to environment-level security settings and audit logs. They include visibility into all team activity in the environment, regardless of platform tools or project access.

| Privilege | Full access |
| --- | --- |
| Activity audit | ❌ |
| Audit log replication | ❌ |
| Debug, Log and Security | ❌ |
| Manage locked projects | ❌ |

#### Billing & usage

These privileges control access to the Billing & Usage dashboard.

| Privilege | Full access |
| --- | --- |
| Usage dashboard | ❌ |

### Automation HQ privileges

This privilege grants access to the Automation HQ console for managing enterprise automation programs and initiatives.

| Privilege | Full access |
| --- | --- |
| Automation HQ | ❌ |

### Solutions access

These privileges control authentication, end-user groups, and identity management for solutions such as Workato GO, Genies, and Low Code App. They include configuration of authentication methods, SSO, and user/group assignments.

| Privilege | Full access |
| --- | --- |
| Authentication settings and SSO | ❌ |
| End users and groups | ❌ |

### XChange

The **XChange** tab controls permissions to create, curate, and consume packages in [XChange](/en/xchange), Workato's package management and distribution platform.

#### Package creation

| Privilege | Full access | View | Edit | Create |
| --- | --- | --- | --- | --- |
| Version | ❌ | ❌ | ❌ | ❌ |

#### Curation

| Privilege | Full access | View | Edit | Delete | Publish/Distribute | Review | Share |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Packages | ❌ |  |  | ❌ | ❌ | ❌ | ❌ |
| Settings | ❌ | ❌ | ❌ |  |  |  |  |

#### Consumption

| Privilege | Full access | View | Install |
| --- | --- | --- | --- |
| Verified Packages | ❌ | ❌ | ❌ |
