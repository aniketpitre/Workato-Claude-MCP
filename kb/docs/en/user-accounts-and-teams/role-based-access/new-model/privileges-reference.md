---
url: >-
  https://docs.workato.com/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference.md
description: >-
  Reference for Workato environment-level and project-level privileges, covering
  what each controls and its dependencies for custom roles.
---

# Privileges

This page lists all available privileges in Workato. Use this reference when creating or editing custom roles. Each entry describes what the privilege controls, where it applies, and any dependencies to consider.

Privileges fall into two scopes:

- [Environment-level privileges](#environment-privileges): Apply across the entire environment
- [Project-level privileges](#project-privileges): Apply within a specific project

## Environment privileges

Environment-level privileges control access across entire environments. They cover administrative tools, configuration options, and features shared across multiple projects, such as lifecycle settings, OAuth profiles, or project creation.

Workspaces may include multiple environments, and collaborators can have different environment roles across each one.

### Platform tools

The **Platform tools** privileges tab controls access to shared tools and features that operate across projects within the environment. This tab includes the following privilege access:

- [Project management](#project-management)
- [Tools](#tools)
- [On-premise](#on-premise)
- [Apps portal](#apps-portal)
- [Data storage](#data-storage)
- [API platform](#api-platform)
- [Connector SDK](#connector-sdk)
- [Insights](#insights)

#### Project management

The following privileges control whether a collaborator can create projects and manage access to all projects in the environment. When a user creates a project, Workato automatically assigns them the [Project admin](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles#project-admin) role for that project.

- Manage projects
  
- Controls access to create projects and manage collaborator access across all projects in the environment.
  
  - Full access
    
  - Includes project creation and the ability to manage collaborator access for all projects in the environment.
    
  - Create
    
  - Grants the ability to create new projects. The creator is automatically assigned the **Project admin** role for that project.
    
  - Access control
    
  - Grants permission to manage collaborator roles and access across all projects in the environment.
    

#### Tools

The following privileges control access to shared environment-level tools and resources used across recipes:

- Common data models
  
- Controls access to create and manage common data models that standardize schema across recipes.
  
  - Full access
    
  - Grants all permissions to common data models.
    
  - View
    
  - View common data models in the workspace.
    
  - Edit
    
  - Edit common data models in the workspace.
    
  - Create
    
  - Create common data models in the workspace.
    
  - Delete
    
  - Delete common data models in the workspace.
    

- Custom Oauth profiles
  
- Controls access to manage custom OAuth profiles used for authentication across recipes and connectors in the environment.
  
  - Full access
    
  - Grants all Custom OAuth profile permissions.
    
  - View
    
  - View Custom OAuth Profiles and Enterprise Workbots.
    
  - Edit
    
  - Edit Custom OAuth Profiles and Enterprise Workbots.
    
  - Create
    
  - Create Custom OAuth Profiles and Enterprise Workbots.
    
  - Delete
    
  - Delete Custom OAuth Profiles and Enterprise Workbots.
    

- Message templates
  
- Controls access to manage message templates used in recipes.
  
  - Full access
    
  - Grants all message templates permissions.
    
  - View
    
  - View message templates in the workspace.
    
  - Edit
    
  - Edit message templates in the workspace.
    
  - Create
    
  - Create message templates in the workspace.
    
  - Delete
    
  - Delete message templates in the workspace.
    

- Event streams
  
- Controls access to event streams.
  
  - Full access
    
  - Grants full access to all event streams permissions.
    
  - View
    
  - View Event topics in the workspace.
    
  - Edit
    
  - Edit Event topics in the workspace.
    
  - Create
    
  - Create Event topics in the workspace.
    
  - Delete
    
  - Delete Event topics in the workspace.
    
  - View history
    
  - View the message content in the Event topics messages list.
    

- Recipe lifecycle management
  
- Controls access to the Recipe lifecycle management feature.
  
  - Full access
  - Grants full access to the Recipe lifecycle management (RLCM) feature. This includes the ability to create manifests and view and interact with all assets included in manifests.

- Workbot
  
- Controls access to manage Workbot configurations.
  
  - Full access
    
  - Grants full access to all Workbot permissions.
    
  - View
    
  - View installed Workbots in the workspace.
    
  - Edit
    
  - Edit installed Workbots in the workspace.
    
  - Create
    
  - Create Workbots in the workspace.
    
  - Delete
    
  - Delete installed Workbots in the workspace.
    

- Enterprise Workbot
  
- Controls access to manage Enterprise Workbot configurations.
  
  - Full access
    
  - Grants full access to all Enterprise Workbot permissions.
    
  - View
    
  - View installed Enterprise Workbots in the workspace.
    
  - Edit
    
  - Edit installed Enterprise Workbots in the workspace.
    
  - Create
    
  - Create Enterprise Workbots in the workspace.
    
  - Delete
    
  - Delete installed Enterprise Workbots in the workspace.
    

- Runtime user connections
  
- Controls access to runtime user connections.
  
  - Full access
    
  - Grants all runtime connection permissions.
    
  - View
    
  - View runtime connections in the workspace.
    
  - Edit
    
  - Edit runtime connections in the workspace.
    
  - Delete
    
  - Delete runtime connections in the workspace.
    

- Logs
  
- Controls access to system logs that track platform activity at the environment level.
  
  - Full access
  - Grants full access to available logs.

- File Storage
  
- Controls access to the FileStorage feature.
  
  - Full access
    
  - Grants full access to FileStorage permissions.
    
  - View
    
  - View files and directories in the FileStorage interface.
    
  - Edit
    
  - Edit files and directories in the FileStorage interface.
    
  - Create
    
  - Create files and directories in the FileStorage interface.
    
  - Delete
    
  - Delete files and directories in the FileStorage interface.
    

- Workato GO
  
- Controls access to manage [Workato GO](/en/agentic/workato-go).
  
  - Full access
    
  - Grants full access to all Workato GO permissions.
    
  - View
    
  - View Workato GO configurations.
    
  - Edit
    
  - Edit Workato GO configurations.
    
  - Manage access
    
  - Manage user access to Workato GO.
    

#### On-premise

The following privileges control access to on-premise features, including agent management, file-based connections, and command line scripts:

- On-prem groups & agents
  
- Controls access to set up, configure, and manage on-premise agents and agent groups.
  
  - Full access
    
  - Grants full access to permissions for on-prem groups and agents.
    
  - View
    
  - View on-prem groups and agents.
    
  - Edit
    
  - Edit on-prem groups and agents.
    
  - Create
    
  - Create on-prem groups and agents.
    
  - Delete
    
  - Delete on-prem groups and agents.
    

- Connection - on-prem files
  
- Controls access to create and manage connections to local file systems through the on-prem agent. These connections enable recipes to interact with the file system of the machine where the agent is installed.
  
  - Full access
  - Grants full access to permissions for on-prem groups and agents. Grants permission to create, edit, and delete on-prem file connections, including secondary connections. Note that global connection settings may override this permission.

- Connection - command line scripts
  
- Controls access to create and manage on-premise connections that execute command-line scripts on machines where the on-prem agent is installed. These connections enable recipes to run local shell commands as part of automated workflows.
  
  - Full access
  - Grants permission to create, edit, and delete command-line script connections. Note that global connection settings may override this permission.

#### Apps portal

The following privileges control access to the Workflow Apps portal. These permissions control portal-level settings and identity group access. Creating or editing a Workflow app requires Workflow app privileges. Access to a Workflow app's data depends on data table permissions.

- Settings
  
- Controls access to manage settings for the Workflow Apps portal. This includes workspace-level branding, authentication methods, login experience, and other global configurations for end-user apps.
  
  - Full access
  - Grants full access to all Workflow Apps portal settings.

> **ACCESS CONTEXT**
> 
> Workflow app creation is controlled by Workflow app permissions. Access to a Workflow app's data is controlled by data table privileges.

- Users and groups
  
- Controls access to manage groups and user assignments in the Workflow Apps portal.
  
  - Full access
  - Grants permission to view, add, remove, and modify users and their group memberships in the Apps portal.

#### Data storage

The following privileges control access to environment-level data storage features such as lookup tables and environment properties:

- Lookup tables
  
- Controls access to the lookup tables interface. These permissions apply only to tables the user can already access. This includes tables scoped to All projects, and project-scoped tables if the user also has access to that project.
  
  - Full access
    
  - Grants full to lookup tables permissions.
    
  - View
    
  - View all tables and their records.
    
  - Edit records
    
  - Add, edit, or delete records for all lookup tables in the lookup tables interface.
    
  - Create
    
  - Create new tables in the Lookup tables interface.
    
  - Delete
    
  - Delete tables in the Lookup tables interface.
    
  - Modify structure
    
  - Edit the schema, such as adding, removing, or editing columns for any table.
    

> **CONNECTOR ACCESS**
> 
> Users can still add, update, or delete records using the Lookup Tables connector in recipes, as long as they have access to the table. This works independently of the “Edit records” UI permission.

- Environment properties
  
- Controls access to environment-level configuration values used across recipes.
  
  - Full access
    
  - Grants full to environment properties permissions.
    
  - View
    
  - View all Environment properties.
    
  - Edit records
    
  - Add, edit, or delete environment properties.
    
  - Create
    
  - Create new environment properties.
    
  - Delete
    
  - Delete environment properties.
    

- Configurable data retention
  
- Controls access to environment-level data retention settings.
  
  - Full access
  - Configure and manage data retention policies for the environment.

#### API platform

The following privileges control access to the API platform, including endpoints, policies, and related configurations:

- Dashboard & logs
  
- Controls access to API dashboards and logs.
  
  - Full access
  - Grants full access to view, configure, and manage API dashboards and logs.

- Collections & endpoints
  
- Controls access to API collections and endpoints.
  
  - Full access
    
  - Grants all permissions for managing API collections and endpoints.
    
  - View
    
  - View existing API collections and endpoints.
    
  - Edit
    
  - Edit API collections and endpoints.
    
  - Create
    
  - Create new API collections and endpoints.
    
  - Delete
    
  - Delete API collections and endpoints.
    

- Client & access profiles
  
- Controls access to client profiles and access credentials for API usage.
  
  - Full access
    
  - Grants full access to manage client profiles and access credentials.
    
  - View
    
  - View client profiles and access credentials.
    
  - Edit
    
  - Edit client profiles and access credentials.
    
  - Create
    
  - Create client profiles and access credentials.
    
  - Delete
    
  - Delete client profiles and access credentials.
    

- Policies
  
- Controls access to manage API policies that govern usage and security.
  
  - Full access
    
  - Grants all API policy permissions.
    
  - View
    
  - View API policies.
    
  - Edit
    
  - Edit API policies.
    
  - Create
    
  - Create new API policies.
    
  - Delete
    
  - Delete API policies.
    

- Settings
  
- Controls access to API platform settings.
  
  - Full access
  - Grants complete control of API platform settings.

#### Connector SDK

The following privileges control access to custom SDK connectors and their usage in recipes:

- Connector SDK
  
- Controls access to develop and manage SDK-based connectors within the environment.
  
  - Full access
  - Grants full access to create, edit, publish, and manage custom SDK connectors. Note that this doesn't include permissions for recipe-level use.

- Use in recipes
  
- Controls whether users can use SDK connectors in recipes.
  
  - Full access
  - Grants full access to using custom SDK connectors in recipes across any accessible project.

#### Insights

The following privileges control access to Insights dashboards:

- Insights
  
- Controls access to Insights dashboards and their underlying data.
  
  - Full access
    
  - Grants full access to the Insights feature and permissions.
    
  - View
    
  - View all accessible Insights dashboards and their metrics.
    
  - Edit
    
  - Edit existing Insights dashboards.
    
  - Create
    
  - Create new Insights dashboards.
    
  - Delete
    
  - Delete Insights dashboards.
    

### Admin privileges

The **Admin privileges** tab controls access to administrative features at the workspace and environment level. The following privileges affect collaborator roles, workspace configuration, API access, and security visibility.

This tab includes the following privilege categories:

- [Workspace access](#workspace-access)
- [Environment settings](#environment-settings)
- [Billing & usage](#billing-usage)

#### Workspace access

The following privileges control access to workspace-wide configuration and collaborator management. Use these privileges to assign roles, manage users, and configure workspace settings:

- Collaborators
  
- Controls access to manage collaborators in the workspace.
  
  - Full access
  - Grants full control over collaborator management, including viewing, adding, updating, and removing users.

- Collaborator roles (non-system)
  
- Controls access to create and manage custom roles within the workspace. This applies to both environment and project-level roles, but does not include system-defined roles like Environment admin or Project admin.
  
  - Full access
  - Grants permission to define, edit, and delete custom roles.

- Collaborator SAML SSO auth
  
- Controls access to configure SAML single sign-on authentication for collaborators.
  
  - Full access
  - Grants permission to configure and manage collaborator SAML SSO settings.

- Developer API
  
- Controls access to manage the Developer API settings in the workspace.
  
  - Full access
  - Grants permission to view and update Developer API settings.

- SCIM provisioning
  
- Controls access to configure SCIM-based user provisioning for the workspace.
  
  - Full access
  - Grants permission to configure and manage SCIM provisioning settings.

- Cross-workspace sharing
  
- Controls access to manage [cross-workspace grants](/en/cross-share-streams) that share Event streams topics with other workspaces in your Automation HQ organization.
  
  - Full access
  - Grants permission to create, view, edit, and delete cross-workspace grants.

- Workspace settings
  
- Controls access to update global workspace-level settings.
  
  - Full access
  - Grants permission to view and update all workspace settings.

#### Environment settings

The following privileges control access to environment-level logs, debug tools, and security configurations:

- Activity audit
  
- Controls access to view activity audit logs for the environment.
  
  - Full access
  - View all activity audit logs for the environment
- Audit log replication
  
- Controls access to configure and manage audit log replication for the environment.
  
  - Full access
  - Configure audit log replication settings and manage replication targets.
- Debug, Log and Security
  
- Controls access to view team activity and security settings for the environment.
  
  - Full access
  - Grants permission to view and edit the workspace's [environment-specific settings](/en/workspace#environment-related-settings), including error alerts, network trace, data retention, and AWS IAM information.
- Manage locked projects
  
- Controls access to manage locked projects in the environment
  
  - Full access
  - Unlock projects and manage project lock state within the environment.

#### Billing & usage

The following privileges control access to the Billing & Usage dashboard:

- Usage dashboard
  
- Controls access to view the workspace's billing and usage dashboard.
  
  - Full access
  - Grants full access to view the Billing & Usage dashboard.

### Manage customers privileges

- Customers & customer managers
  
- Controls access to the **Customers** and **Customer managers** tabs of the Embedded Admin console.
  
  - Full access
    
  - Grants all [customers](/en/oem/admin-console/customers) and [customer managers](/en/oem/admin-console/customer-managers) permissions to view, add, update, and delete customers and customer managers.
    
  - View
    
  - Grants permission to view customers and customer managers.
    
  - Manage
    
  - Grants permission to add customers and assign customer managers.
    
  - Delete
    
  - Grants permission to delete customers and customer managers.
    

- Shared connectors
  
- Controls access to **Shared connectors** tab of the Embedded Admin console.
  
  - Full access
    
  - Grants all [shared connectors](/en/oem/admin-console/shared-connectors) permissions to view, manage, and delete shared connectors.
    
  - View
    
  - Grants permission to view shared connectors.
    
  - Manage
    
  - Grants permission to manage shared connectors.
    
  - Delete
    
  - Grants permission to delete shared connectors.
    

- Usage metrics & settings
  
- Controls access to usage metrics and settings in the Embedded Admin console.
  
  - Full access
    
  - Grants all [usage metrics](/en/oem/admin-console/usage-metrics) and [settings](/en/oem/admin-console/settings) permissions, including viewing and managing usage metrics and settings.
    
  - View
    
  - Grants permission to view usage metrics and settings.
    
  - Manage
    
  - Grants permission to manage audit log streaming and branding settings.
    

> **WHO CAN USE THIS FEATURE?**
> 
> The **Manage customers** interface only appears for [Embedded](/en/oem) collaborators with permission to create or modify collaborator roles.

### Automation HQ privileges

The **Automation HQ privileges** tab controls access to Automation HQ.

- Automation HQ
  
- Controls access to the Automation HQ interface.
  
  - Full access
  - Allows users to access and use all features within Automation HQ.

### Solutions access

The **Solutions access** tab controls permissions to manage end users, user groups, and authentication for Workato solutions such as Workato ID, Workato GO, Genies, and the Low Code App.

- Authentication settings and SSO
  
- Controls access to configure authentication methods and single sign-on (SSO) for Workato solutions.
  
  - Full access
  - Grants permission to configure authentication settings, enable or disable SSO, and manage identity providers.

- End users and groups
  
- Controls access to manage end users and user groups for Workato solutions.
  
  - Full access
  - Grants permission to add, remove, and update end users and groups.

### XChange

The **XChange** tab controls permissions to create, curate, and consume packages in [XChange](/en/xchange), Workato's package management and distribution platform.

#### Package creation

The following privileges control access to create and submit packages to XChange:

- Version
  
- Controls access to manage package versions submitted to XChange.
  
  - Full access
    
  - Grants all package version permissions.
    
  - View
    
  - View existing package versions.
    
  - Edit
    
  - Edit package versions.
    
  - Create
    
  - Create new package versions.
    

#### Curation

The following privileges control access to approve, manage, and distribute packages in XChange:

- Packages
  
- Controls access to review and distribute submitted packages.
  
  - Full access
    
  - Grants all package curation permissions.
    
  - Delete
    
  - Delete packages from XChange.
    
  - Publish/Distribute
    
  - Publish and distribute packages to XChange.
    
  - Review
    
  - Review submitted packages.
    
  - Share
    
  - Share packages with other workspaces.
    

- Settings
  
- Controls access to configure XChange curation settings.
  
  - Full access
    
  - Grants all XChange settings permissions.
    
  - View
    
  - View XChange settings.
    
  - Edit
    
  - Edit XChange settings.
    

#### Consumption

The following privileges control access to browse and install packages from XChange in the private library:

- Verified Packages
  
- Controls access to browse and install verified packages from XChange.
  
  - Full access
    
  - Grants all verified package permissions.
    
  - View
    
  - View verified packages in the private library.
    
  - Install
    
  - Install verified packages from XChange.
    

## Project privileges

The following privileges control what users can access and manage within a specific project. Assign these permissions when creating custom project roles to define what collaborators can build, deploy, or view.

Project-level privileges are grouped into the following categories:

- [Project assets](#project-assets)
- [MCP servers](#mcp-servers)
- [Genie building](#genie-building)
- [Project settings](#project-settings)
- [Low-code apps](#low-code-apps)
- [Test automation](#test-automation)
- [Debug jobs](#debug-jobs)
- [Secrets management](#secrets-management)

### Project assets

The following privileges control access to build and manage core project components such as recipes, folders, and connections. Each asset type has its own set of granular permissions.

- Connections
  
- Controls access to manage connections that recipes use to integrate with external systems.
  
  - Full access
    
  - Grants all connection permissions.
    
  - View
    
  - View existing connections in the project.
    
  - Edit
    
  - Update connection configurations.
    
  - Create
    
  - Create new connections in the project.
    
  - Delete
    
  - Remove existing connections from the project.
    

- Recipes
  
- Controls access to create, manage, and operate recipes in the project.
  
  - Full access
    
  - Grants all recipe-related permissions.
    
  - View
    
  - View existing recipes.
    
  - Edit
    
  - Update recipe configurations.
    
  - Create
    
  - Build new recipes.
    
  - Delete
    
  - Remove existing recipes from the project.
    
  - Test/Start/Stop
    
  - Start, stop, and test recipes.
    
  - Job history
    
  - View a recipe's job history in the **Jobs** tab.
    

> **POTENTIAL SENSITIVE DATA EXPOSURE**
> 
> Admins should consider disabling Job history for certain users to prevent access to raw inputs and outputs that may contain sensitive data when using genies. Genies ingest knowledge and context through knowledge bases and skills. The raw inputs and outputs for knowledge bases and skills can be accessed through recipe Job history.

- Decision models
  
- Controls access to create and manage decision models.
  
  - Full access
    
  - Grants all decision model permissions.
    
  - View
    
  - View decision models and decision tables.
    
  - Edit
    
  - Edit decision models and decision tables.
    
  - Create
    
  - Create decision models and decision tables.
    
  - Delete
    
  - Delete decision models and decision tables.
    

- Data Pipelines
  
- Controls access to create, manage, and test Data Pipelines.
  
  - Full access
    
  - Grants all Data Pipeline permissions.
    
  - View
    
  - View Data Pipelines.
    
  - Edit
    
  - Update existing Data Pipeline configurations.
    
  - Create
    
  - Build new Data Pipelines.
    
  - Delete
    
  - Remove existing Data Pipelines.
    
  - Test/Start/Stop
    
  - Start, stop, and test Data Pipelines.
    

- Data tables
  
- Controls access to create and manage data tables.
  
  - Full access
    
  - Grants all Data Table permissions.
    
  - View
    
  - View Data Tables.
    
  - Edit records
    
  - Update existing records within a data table.
    
  - Create
    
  - Add new data tables.
    
  - Delete
    
  - Remove existing data tables.
    
  - Modify structure
    
  - Change the schema of a data table, including adding, updating, or removing columns.
    

- Folders
  
- Controls access to project folders used to organize recipes and assets.
  
  - Full access
    
  - Grants all folder permissions.
    
  - View
    
  - View folders and sub-folders in the project.
    
  - Edit
    
  - Update folder properties.
    
  - Create
    
  - Add new folders and sub-folders.
    
  - Delete
    
  - Remove existing folders and sub-folders.
    

- Blueprints
  
- Controls access to manage [Blueprints](/en/airo/blueprints), AIRO-generated implementation plans that scaffold the assets needed for a project.
  
  - Full access
    
  - Grants all Blueprint permissions.
    
  - View
    
  - View existing Blueprints in the project.
    
  - Edit
    
  - Update Blueprint configurations.
    
  - Create
    
  - Create new Blueprints in the project.
    
  - Delete
    
  - Remove existing Blueprints from the project.
    

### MCP servers

The following privileges control access to create and manage MCP servers:

- MCP servers
  
- Controls access to create and manage MCP servers.
  
  - Full access
    
  - Grants all MCP server-related permissions.
    
  - View
    
  - View existing MCP servers.
    
  - Edit
    
  - Update MCP server configurations.
    
  - Create
    
  - Build new MCP servers.
    
  - Delete
    
  - Remove existing MCP servers.
    
  - Manage access
    
  - Manage which users and roles can access an MCP server.
    
  - Publish/Unpublish
    
  - [Publish or unpublish](/en/mcp/manage-mcp-registry#publish-an-mcp-server) an MCP server to or from the MCP server registry.
    

> **SKILL ACCESS FOR GENIES AND MCP**
> 
> Users with either the **Workato Genies** privilege or the **MCP servers** privilege can view and manage [skills](/en/agentic/skills) built with the [Workato Skill connector](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector). This lets builders on Business MCP and Enterprise MCP plans create and manage skills without an Agent Studio license.

### Genie building

The following privileges control access to the core assets used to build genies, including the knowledge bases that power genies, and custom chat interfaces where end users interact with genies:

- Genies
  
- Controls access to create and manage genies.
  
  - Full access
    
  - Grants all genie-related permissions.
    
  - View
    
  - View existing genies.
    
  - Edit
    
  - Update genie configurations.
    
  - Create
    
  - Build new genies.
    
  - Delete
    
  - Remove existing genies.
    
  - Start/Stop
    
  - Start and stop genies in a project.
    
  - Test
    
  - Grants access to Test mode.
    
  - Conversation history
    
  - Grants access to the Conversations tab with historical genie conversations.
    

- Knowledge Bases
  
- Controls access to manage Knowledge Bases used for storing and retrieving structured content.
  
  - Full access
    
  - Grants all Knowledge Base permissions.
    
  - View
    
  - View Knowledge Bases in the project.
    
  - Edit
    
  - Update Knowledge Base configurations.
    
  - Create
    
  - Add new Knowledge Bases.
    
  - Delete
    
  - Remove existing Knowledge Bases.
    

- Custom chat interface
  
- Controls access to manage a genie's [custom chat interface](/en/agentic/agent-studio/chat-interface/headless-api) and genie clients.
  
  - Full access
    
  - Grants full access to all custom chat interface permissions.
    
  - View
    
  - View a genie's custom chat interface configuration and genie clients.
    
  - Edit
    
  - Edit a genie's custom chat interface configuration, including regenerating, detaching, and deleting genie clients.
    
  - Create
    
  - Create and attach genie clients for a genie's custom chat interface.
    

- Event streams
  
- Controls project-level access to event streams. Collaborators must also be members of the project that contains the event streams.
  
  - Full access
    
  - Grants all Event streams permissions.
    
  - View
    
  - View event streams in the project.
    
  - Edit
    
  - Edit event streams in the project.
    
  - Create
    
  - Create event streams in the project.
    
  - Delete
    
  - Delete event streams in the project.
    
  - View history
    
  - View the message content in the event stream messages list.
    

> **PERMISSION MIGRATION**
> 
> Access control for event streams is transitioning to the project level because event streams are now assets. Workato migrates existing access automatically by creating new user groups and project roles named **Topics manager**, **Topics editor**, and **Topics viewer**, which provide collaborators equivalent project-level permissions to their pre-migration access. Workato skips environment roles without any collaborators, and environment roles with the same access level share one project role.
> 
> You can access event stream access through either [project-level](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-assets) or [environment-level](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#tools) privileges during the [transition period](/en/event-streams#event-streams-as-project-assets). You must use the project-level privilege after the transition period.

### Project settings

The following privileges control access to manage project-level configurations, deployments, and collaborator permissions. These settings define who can administer the project, modify properties, and approve or review deployments.

> **ENABLE DEPLOYMENT**
> 
> You must enable deployment in both the source and target environments.

- Project administration
  
- Controls access to core administrative actions within a project.
  
  - Full access
    
  - Grants all project administrative permissions.
    
  - Edit
    
  - Update the project's name and description.
    
  - Delete
    
  - Delete the entire project.
    
  - Access control
    
  - Manage collaborator access and assign roles within the project.
    

- Project properties
  
- Controls access to manage project-level metadata and related configurations.
  
  - Full access
    
  - Grants all permissions to configure project properties.
    
  - View
    
  - View project properties such as the name, description, and metadata.
    
  - Edit records
    
  - Update existing project property records.
    
  - Create
    
  - Add new project property records.
    
  - Delete
    
  - Remove existing project property records.
    

- Approve deployment
  
- Controls the ability to approve deployments when deployment approval workflows are enabled.
  
  - Full access
  - Grants permission to approve deployment requests.

- Review deployment
  
- Controls the ability to review deployment details before approving or rejecting.
  
  - Full access
  - Grants permission to view and review deployment configurations.

### Low-code apps

The following privileges control access to Workflow apps, such as the ability to create apps and manage settings for Workflow apps on an individual basis. These permissions only apply to the web interface and don't affect access to the Workflow apps connector. Access to the Workflow apps portal is determined by Workflow apps portal permissions. Access to a Workflow app's corresponding data table is determined by data tables permissions.

- App development
  
- Controls access to build and edit the workflow app's structure and logic.
  
  - Full access
  - Grants full Workflow app development permissions.

- App access and role management
  
- Controls access to manage who can use and manage the workflow app.
  
  - Full access
    
  - Grants full access to Workflow apps and role management permissions.
    
  - Manage access and role
    
  - Manage the users of your Workflow app.
    
  - Go live / Take offline
    
  - Allows users to publish a Workflow app in the Workflow apps portal or take an app offline.
    

### Test automation

The following privileges control access to [Test Automation](/en/test-automation):

- Test automation
  
- Grants access to all test automation privileges.
  
  - Full access
    
  - Grants all test automation permissions.
    
  - View
    
  - View [test case](/en/test-automation/test-case) details, including mock data and checks.
    
  - Manage (Create, Edit, Delete, Run)
    
  - Manage (create, edit, run, delete) test cases for recipes.
    

### Debug jobs

The following privileges control access to the network trace within job history:

- Network trace
  
- Manage access to network tracing information in job histories.
  
  - Full access
  - View [network traces](/en/recipes/job-debug-tracing#viewing-job-debug-tracing) in job histories.

### Secrets management

The following privileges control access to manage security-related settings, including viewing, editing, and configuring secrets:

- Secrets management
  
- Controls access to create, view, and update secrets in the workspace.
  
  - Full access
    
  - Grants all permissions to manage secrets, including viewing and editing.
    
  - View
    
  - View existing secrets and their configurations.
    
  - Edit
    
  - Update or modify existing secrets.
