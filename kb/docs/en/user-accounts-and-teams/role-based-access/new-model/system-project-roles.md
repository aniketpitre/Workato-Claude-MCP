---
url: >-
  https://docs.workato.com/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles.md
description: >-
  Reference for Workato project roles, including Project admin, Advanced
  builder, Builder, and Project operator, and the access each provides.
---

# Project roles

Project roles control what a user or group can access and manage inside a specific project. You can assign these roles per project to define responsibilities across build, deploy, and review tasks. The following table lists system project roles and the access they provide:

| Type | Description |
| --- | --- |
| Project admin | Grants full access to all project content and settings, including user management and deletion. |
| Advanced builder | Grants full access to build and deploy, without access to manage settings or user permissions. |
| Builder | Allows users to modify folders, recipes, Workato apps, and data tables. This role also allows test automation but not deployment. |
| Project operator | Grants read-only access to project content and the ability to run and stop recipes. |

Use the following guides to review the full set of privileges for each role:

- [Project admin](#project-admin)
- [Advanced builder](#advanced-builder)
- [Builder](#builder)
- [Project operator](#project-operator)

## Project admin

The **Project admin** role provides full control over all content and settings within a project. This includes recipe development, resource configuration, deployments, and access management. Assign this role to collaborators who manage project assets without requiring environment-level administrative access.

Project admins can perform the following actions in their assigned project:

- Build and manage recipes, folders, and connections.
- Approve and review deployments.
- Manage project access and assign roles to collaborators.
- View and manage data tables, test automation, and network trace.

Project admins can access every recipe, connection, and asset in a project. This role doesn't include access to environment or workspace-level settings.

### Privileges

The following tables list the full set of privileges included in the **Project admin** role. Each section outlines what actions the role can perform within a project.

#### Project assets

The following privileges control access to recipe-building features and shared project resources:

| Privilege | Full access | View | Edit | Edit records | Create | Delete | Test/ Start/Stop | Job history | Modify structure | View history |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Connections | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Recipes | ✔ | ✔ | ✔ |  | ✔ | ✔ | ✔ | ✔ |  |  |
| Decision models | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Data Pipelines | ✔ | ✔ | ✔ |  | ✔ | ✔ | ✔ |  |  |  |
| Event streams | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  | ✔ |
| Data tables | ✔ | ✔ |  | ✔ | ✔ | ✔ |  |  | ✔ |  |
| Folders | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Blueprints | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Resources | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |

#### MCP servers

The following privileges control access to create and manage MCP servers:

| Privilege | Full access | View | Edit | Create | Delete | Manage access | Publish/Unpublish |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MCP servers | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

#### Genie building

The following privileges control access to the core assets used to build genies, including the knowledge bases that power genies, and custom chat interfaces where end users interact with genies:

| Privilege | Full access | View | Edit | Create | Delete | Start/ Stop | Test | Conversation history |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Genies | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Knowledge bases | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |  |
| Custom chat interface | ✔ | ✔ | ✔ | ✔ |  |  |  |  |

#### Project settings

The following privileges control project-level administration, such as access control, project properties, and deployment approvals:

> **ENABLE DEPLOYMENT**
> 
> You must enable deployment in both the source and target environments.

| Privilege | Full access | View | Edit | Edit records | Create | Delete | Access control |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Project administration | ✔ |  | ✔ |  |  | ✔ | ✔ |
| Project properties | ✔ | ✔ |  | ✔ | ✔ | ✔ |  |
| Approve deployment | ✔ |  |  |  |  |  |  |
| Review deployment | ✔ |  |  |  |  |  |  |

#### Low-code apps

The following privileges control access to workflow apps, including app configuration and approval steps:

> **ACCESS DEPENDENCY**
> 
> Access to workflow apps also depends on data table privileges.

| Privilege | Full access | Manage access and role | Go live/Take offline |
| --- | --- | --- | --- |
| App development | ✔ |  |  |
| App access and role management | ✔ | ✔ | ✔ |

#### Test automation

The following privileges control access to recipe test cases. Full access includes **View**, **Create**, **Edit**, **Run**, and **Delete** actions. Test automation management also depends on [recipe privileges](#project-assets) such as **View**, **Test**, and **Job History**.

| Privilege | Full access | View | Manage (Create, Edit, Delete, Run) |
| --- | --- | --- | --- |
| Test automation | ✔ | ✔ | ✔ |

#### Debug jobs

The following privileges control access to job-level network traces:

| Privilege | Full access |
| --- | --- |
| Network trace | ✔ |

#### Secrets management

The following privileges control access to security-related secrets within the project:

| Privilege | Full access | View | Edit |
| --- | --- | --- | --- |
| Secrets management | ✔ | ✔ | ✔ |

## Advanced builder

The **Advanced builder** role provides full access to build, test, and deploy project assets. This role doesn't include access to project administration or user management.

Advanced builders can perform the following tasks:

- View, edit, and manage project assets.
- Perform deployments across environments.
- Manage test automation and workflow apps.

They can't rename or delete projects, or manage project access. Assign this role to users who handle project development and deployment without administrative control.

### Privileges

The following tables list the full set of privileges included in the **Advanced builder** role. Each section outlines what actions the role can perform within a project.

#### Project assets

The following privileges control access to recipe-building features and shared project resources:

| Privilege | Full access | View | Edit | Edit records | Create | Delete | Test/ Start/Stop | Job history | Modify structure | View history |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Connections | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Recipes | ✔ | ✔ | ✔ |  | ✔ | ✔ | ✔ | ✔ |  |  |
| Decision models | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Data Pipelines | ✔ | ✔ | ✔ |  | ✔ | ✔ | ✔ |  |  |  |
| Event streams | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  | ✔ |
| Data tables | ✔ | ✔ |  | ✔ | ✔ | ✔ |  |  | ✔ |  |
| Folders | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Blueprints | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Resources | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |

#### MCP servers

The following privileges control access to create and manage MCP servers:

| Privilege | Full access | View | Edit | Create | Delete | Manage access | Publish/Unpublish |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MCP servers | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

#### Genie building

The following privileges control access to the core assets used to build genies, including the knowledge bases that power genies, and custom chat interfaces where end users interact with genies:

| Privilege | Full access | View | Edit | Create | Delete | Start/ Stop | Test | Conversation history |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Genies | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Knowledge bases | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |  |
| Custom chat interface | ✔ | ✔ | ✔ | ✔ |  |  |  |  |

#### Project settings

The following privileges control project-level administration, such as access control, project properties, and deployment approvals:

> **ENABLE DEPLOYMENT**
> 
> You must enable deployment in both the source and target environments.

| Privilege | Full access | View | Edit | Edit records | Create | Delete | Access control |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Project administration | ❌ |  | ❌ |  |  | ❌ | ❌ |
| Project properties | ✔ | ✔ |  | ✔ | ✔ | ✔ |  |
| Approve deployment | ✔ |  |  |  |  |  |  |
| Review deployment | ✔ |  |  |  |  |  |  |

#### Low-code apps

The following privileges control access to workflow apps, including app configuration and approval steps:

> **ACCESS DEPENDENCY**
> 
> Access to workflow apps also depends on data table privileges.

| Privilege | Full access | Manage access and role | Go live/Take offline |
| --- | --- | --- | --- |
| App development | ✔ |  |  |
| App access and role management | ✔ | ✔ | ✔ |

#### Test automation

The following privileges control access to recipe test cases. Full access includes **View**, **Create**, **Edit**, **Run**, and **Delete** actions. Test automation management also depends on [recipe privileges](#project-assets) such as **View**, **Test**, and **Job History**.

| Privilege | Full access | View | Manage (Create, Edit, Delete, Run) |
| --- | --- | --- | --- |
| Test automation | ✔ | ✔ | ✔ |

#### Debug jobs

The following privileges control access to job-level network traces:

| Privilege | Full access |
| --- | --- |
| Network trace | ❌ |

#### Secrets management

The following privileges control access to security-related secrets within the project:

| Privilege | Full access | View | Edit |
| --- | --- | --- | --- |
| Secrets management | ❌ | ✔ | ❌ |

## Builder

The **Builder** role provides access to develop recipes and manage key assets within a project. Builders don't have access to deployments or project administration.

Builders can perform the following actions in their assigned project:

- Create and test recipes and folders, and view connections
- Manage project properties and review deployments
- Configure workflow apps, manage access, and publish them

Builders can't deploy project assets or manage project-level access. Assign this role to collaborators who build and test project components without administrative access.

### Privileges

The following tables list the full set of privileges included in the **Builder** role. Each section outlines what actions the role can perform within a project.

#### Project assets

The following privileges control access to recipe-building features and shared project resources:

| Privilege | Full access | View | Edit | Edit records | Create | Delete | Test/ Start/Stop | Job history | Modify structure | View history |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Connections | ❌ | ✔ | ❌ |  | ❌ | ❌ |  |  |  |  |
| Recipes | ✔ | ✔ | ✔ |  | ✔ | ✔ | ✔ | ✔ |  |  |
| Decision models | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Data Pipelines | ❌ | ❌ | ❌ |  | ❌ | ❌ | ❌ |  |  |  |
| Event streams | ❌ | ✔ | ✔ |  | ✔ | ❌ |  |  |  | ✔ |
| Data tables | ✔ | ✔ |  | ✔ | ✔ | ✔ |  |  | ✔ |  |
| Folders | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Blueprints | ❌ | ❌ | ❌ |  | ❌ | ❌ |  |  |  |  |
| Resources | ❌ | ❌ | ❌ |  | ❌ | ❌ |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |

#### MCP servers

The following privileges control access to create and manage MCP servers:

| Privilege | Full access | View | Edit | Create | Delete | Manage access | Publish/Unpublish |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MCP servers | ❌ | ✔ | ✔ | ✔ | ❌ | ✔ | ❌ |

#### Genie building

The following privileges control access to the core assets used to build genies, including the knowledge bases that power genies, and custom chat interfaces where end users interact with genies:

| Privilege | Full access | View | Edit | Create | Delete | Start/ Stop | Test | Conversation history |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Genies | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Knowledge bases | ❌ | ❌ | ❌ | ❌ | ❌ |  |  |  |
| Custom chat interface | ❌ | ❌ | ❌ | ❌ |  |  |  |  |

#### Project settings

The following privileges control project-level administration, such as access control, project properties, and deployment approvals:

> **ENABLE DEPLOYMENT**
> 
> You must enable deployment in both the source and target environments.

| Privilege | Full access | View | Edit | Edit records | Create | Delete | Access control |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Project administration | ❌ |  | ❌ |  |  | ❌ | ❌ |
| Project properties | ✔ | ✔ |  | ✔ | ✔ | ✔ |  |
| Approve deployment | ❌ |  |  |  |  |  |  |
| Review deployment | ✔ |  |  |  |  |  |  |

#### Low-code apps

The following privileges control access to workflow apps, including app configuration and approval steps:

> **ACCESS DEPENDENCY**
> 
> Access to workflow apps also depends on data table privileges.

| Privilege | Full access | Manage access and role | Go live/Take offline |
| --- | --- | --- | --- |
| App development | ✔ |  |  |
| App access and role management | ✔ | ✔ | ✔ |

#### Test automation

The following privileges control access to recipe test cases. Full access includes **View**, **Create**, **Edit**, **Run**, and **Delete** actions. Test automation management also depends on [recipe privileges](#project-assets) such as **View**, **Test**, and **Job History**.

| Privilege | Full access | View | Manage (Create, Edit, Delete, Run) |
| --- | --- | --- | --- |
| Test automation | ✔ | ✔ | ✔ |

#### Debug jobs

The following privileges control access to job-level network traces:

| Privilege | Full access |
| --- | --- |
| Network trace | ❌ |

#### Secrets management

The following privileges control access to security-related secrets within the project:

| Privilege | Full access | View | Edit |
| --- | --- | --- | --- |
| Secrets management | ❌ | ❌ | ❌ |

## Project operator

The **Project operator** role provides limited access to view and run content within a project. Assign this role to users who need visibility into project activity and permission to test recipes, but not edit or deploy content.

Project operators can perform the following actions in their assigned project:

- View recipes and folders
- Access job history
- Test, start, and stop recipes

They can't create, edit, or deploy content. They also can't view connections or manage project settings or user access.

### Privileges

The following tables list the full set of privileges included in the **Project operator** role. Each section outlines what actions the role can perform within a project.

#### Project assets

The following privileges control access to recipe-building features and shared project resources:

| Privilege | Full access | View | Edit | Edit records | Create | Delete | Test/ Start/Stop | Job history | Modify structure | View history |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Connections | ❌ | ❌ | ❌ |  | ❌ | ❌ |  |  |  |  |
| Recipes | ❌ | ✔ | ❌ |  | ❌ | ❌ | ✔ | ✔ |  |  |
| Decision models | ❌ | ✔ | ❌ |  | ❌ | ❌ |  |  |  |  |
| Data Pipelines | ❌ | ✔ | ❌ |  | ❌ | ❌ | ❌ |  |  |  |
| Event streams | ❌ | ✔ | ❌ |  | ❌ | ❌ |  |  |  | ✔ |
| Data tables | ❌ | ❌ |  | ❌ | ❌ | ❌ |  |  | ❌ |  |
| Folders | ❌ | ✔ | ❌ |  | ❌ | ❌ |  |  |  |  |
| Blueprints | ❌ | ❌ | ❌ |  | ❌ | ❌ |  |  |  |  |
| Resources | ❌ | ❌ | ❌ |  | ❌ | ❌ |  |  |  |  |

#### MCP servers

The following privileges control access to create and manage MCP servers:

| Privilege | Full access | View | Edit | Create | Delete | Manage access | Publish/Unpublish |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MCP servers | ❌ | ✔ | ❌ | ❌ | ❌ | ❌ | ❌ |

#### Genie building

The following privileges control access to the core assets used to build genies, including the knowledge bases that power genies, and custom chat interfaces where end users interact with genies:

| Privilege | Full access | View | Edit | Create | Delete | Start/ Stop | Test | Conversation history |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Genies | ❌ | ✔ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Knowledge bases | ❌ | ✔ | ❌ | ❌ | ❌ |  |  |  |
| Custom chat interface | ❌ | ✔ | ❌ | ❌ |  |  |  |  |

#### Project settings

The following privileges control project-level administration, such as access control, project properties, and deployment approvals:

> **ENABLE DEPLOYMENT**
> 
> You must enable deployment in both the source and target environments.

| Privilege | Full access | View | Edit | Edit records | Create | Delete | Access control |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Project administration | ❌ |  | ❌ |  |  | ❌ | ❌ |
| Project properties | ❌ | ❌ |  | ❌ | ❌ | ❌ |  |
| Approve deployment | ❌ |  |  |  |  |  |  |
| Review deployment | ❌ |  |  |  |  |  |  |

#### Low-code apps

The following privileges control access to workflow apps, including app configuration and approval steps:

> **ACCESS DEPENDENCY**
> 
> Access to workflow apps also depends on data table privileges.

| Privilege | Full access | Manage access and role | Go live/Take offline |
| --- | --- | --- | --- |
| App development | ❌ |  |  |
| App access and role management | ❌ | ❌ | ❌ |

#### Test automation

The following privileges control access to recipe test cases. Full access includes **View**, **Create**, **Edit**, **Run**, and **Delete** actions. Test automation management also depends on [recipe privileges](#project-assets) such as **View**, **Test**, and **Job History**.

| Privilege | Full access | View | Manage (Create, Edit, Delete, Run) |
| --- | --- | --- | --- |
| Test automation | ❌ | ✔ | ❌ |

#### Debug jobs

The following privileges control access to job-level network traces:

| Privilege | Full access |
| --- | --- |
| Network trace | ❌ |

#### Secrets management

The following privileges control access to security-related secrets within the project:

| Privilege | Full access | View | Edit |
| --- | --- | --- | --- |
| Secrets management | ❌ | ❌ | ❌ |
