---
url: 'https://docs.workato.com/en/privileges.md'
description: >-
  Reference for Workato collaborator privileges, detailing the permissions each
  role has across recipe development, platform tools, and admin features.
---

# Collaborator privileges

Collaborator privileges determine the exact permissions that each **role** has to access Workato features, functions, and folders of [Role-based access control](/en/user-accounts-and-teams/role-based-access/).

> **LEGACY MODEL**
> 
> This page describes the legacy permissions model. Workato is replacing legacy roles with the new permissions model, which uses environment roles and project roles. Refer to the [New permissions model](/en/user-accounts-and-teams/role-based-access/access-control-v2) documentation to plan and migrate.

This document provides information about each of the collaborator privileges in Workato.

Refer to [Collaborator roles](/en/roles) to find out about possible collaborator roles.

When you create or modify a role, you'll see the following tabs:

- [Recipe development](#recipe-development-privileges)
- [Platform tools](#platform-tools-privileges)
- [Admin privileges](#admin-privileges)
- [XChange](#xchange)
- [Manage customers (Embedded only)](#manage-customers)

## Recipe development privileges

The **Recipe development** tab controls access and privileges related to projects, recipes, folders, and connections:

- [Project access](#project-access)
- [Recipe creation](#recipe-creation)
- [Decision models](#decision-models)
- [Genie building](#genie-building)
- [Test Automation](#test-automation)
- [Workflow app](#workflow-app)
- [Data storage](#data-tables)
- [Debug jobs](#debug-jobs)
- [Deployment](#deployment)

### Project access

![Project access privileges](/assets/privileges-project-access.B19bsoPb.png)_Project access privileges_

- Manage access to projects.
  - All projects
    
  - Access to all [projects](/en/projects.html) in a workspace.
    
  - Selected projects
    
  - This role can only access the projects specified here.
    

* * *

### Recipe creation

_Recipe creation privileges_

#### Projects

- Manage access to projects when working with recipes.
  - Full access
    
  - All [project](/en/projects.html) permissions: view, edit, create, and delete.
    
  - View
    
  - View specific projects in a workspace.
    
  - Edit
    
  - Edit specific projects in a workspace.
    
  - Create
    
  - Create projects in a workspace.
    
  - Delete
    
  - Delete projects in a workspace.
    

#### Folders

- Manage access to folders when working with recipes.
  - Full access
    
  - All folder permissions: view, edit, create, and delete.
    
  - View
    
  - View folders and sub-folders in a workspace.
    
  - Edit
    
  - Edit folders and sub-folders in a workspace.
    
  - Create
    
  - Create folders and sub-folders in a workspace.
    
  - Delete
    
  - Delete folders and sub-folders in a workspace.
    

#### Connections

- Manage access to connections when working with recipes.
  - Full access
    
  - All [connection](/en/connections.html) permissions: view, edit, create, and delete.
    
  - View
    
  - View connections in a workspace.
    
  - Edit
    
  - Edit connections in a workspace.
    
  - Create
    
  - Create connections in a workspace.
    
  - Delete
    
  - Delete connections in a workspace.
    

#### Recipes

- Manage access to recipes.
  - Full access
    
  - All [recipe](/en/recipes/building-recipes.html) permissions: View, edit, create, delete, run, and view job history.
    
  - View
    
  - View recipes in a workspace.
    
  - Edit
    
  - Edit recipes in a workspace.
    
  - Create
    
  - Create recipes in a workspace.
    
  - Delete
    
  - Delete recipes in a workspace.
    
  - Test/start/stop
    
  - Run recipes and start and stop recipe tests in a workspace.
    
  - Job history
    
  - View a recipe's job history in the **Jobs** tab.
    

#### Event streams

- Manage project-level access to event streams. Collaborators must also be members of the project that contains the event streams.
  - Full access
    
  - All [Event streams](/en/connectors/pubsub.html) permissions: view, edit, create, and delete event streams, and view history.
    
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

#### Blueprints

- Manage access to [Blueprints](/en/airo/blueprints) when working with recipes.
  - Full access
    
  - All Blueprint permissions: view, edit, create, and delete.
    
  - View
    
  - View Blueprints in a workspace.
    
  - Edit
    
  - Edit Blueprints in a workspace.
    
  - Create
    
  - Create Blueprints in a workspace.
    
  - Delete
    
  - Delete Blueprints in a workspace.
    

* * *

### Decision models

- Manage access to decision models when working with recipes.
  - Full access
    
  - All Decision model permissions: view, edit, create, and delete.
    
  - View
    
  - View decision models and decision tables in a workspace.
    
  - Edit
    
  - Edit decision models and decision tables in a workspace.
    
  - Create
    
  - Create decision models and decision tables in a workspace.
    
  - Delete
    
  - Delete decision models and decision tables in a workspace.
    

* * *

### Genie building

Genie building controls access to the core assets used to build genies, including the knowledge bases that power genies, and custom chat interfaces where end users interact with genies.

> **POTENTIAL SENSITIVE DATA EXPOSURE**
> 
> Admins should consider disabling Job history for certain users to prevent access to raw inputs and outputs that may contain sensitive data when using genies. Genies ingest knowledge and context through knowledge bases and skills. The raw inputs and outputs for knowledge bases and skills can be accessed through recipe Job history.

#### Genies

- Manage access to genies.
  - Full access
    
  - Grants full access to all genie permissions.
    
  - View
    
  - View genies in a workspace.
    
  - Edit
    
  - Edit genies in a workspace.
    
  - Create
    
  - Create genies in a workspace.
    
  - Delete
    
  - Delete genies from the workspace.
    
  - Test
    
  - Grants access to Test mode.
    
  - Start/stop
    
  - Start and stop genies in a workspace.
    
  - Conversation history
    
  - Grants access to the Conversations tab with historical genie conversations.
    

> **SKILL ACCESS FOR GENIES AND MCP**
> 
> Users with either the **Workato Genies** privilege or the **MCP servers** privilege can view and manage [skills](/en/agentic/skills) built with the [Workato Skill connector](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector). This lets builders on Business MCP and Enterprise MCP plans create and manage skills without an Agent Studio license.

#### Knowledge bases

- Manage access to knowledge bases.
  - Full access
    
  - Grants full access to all knowledge base permissions.
    
  - View
    
  - View knowledge bases in a workspace.
    
  - Edit
    
  - Edit knowledge bases in a workspace.
    
  - Create
    
  - Create knowledge bases in a workspace.
    
  - Delete
    
  - Delete knowledge bases from the workspace.
    

#### Custom chat interface

- Manage access to a genie's [custom chat interface](/en/agentic/agent-studio/chat-interface/headless-api) and genie clients.
  - Full access
    
  - Grants full access to all custom chat interface permissions.
    
  - View
    
  - View a genie's custom chat interface configuration and genie clients.
    
  - Edit
    
  - Edit a genie's custom chat interface configuration, including regenerating, detaching, and deleting genie clients.
    
  - Create
    
  - Create and attach genie clients for a genie's custom chat interface.
    

### Test Automation

![Permissions](/assets/permissions.fA_6yKog.png)_Test Automation privileges_

> **RECIPE PERMISSIONS**
> 
> When you provide a collaborator with Test Automation privileges, you must also enable certain Recipe permissions. These include the Recipe **View**, **Test/Start/Stop**, and **View job history** permissions.
> 
> For example, if you create a role with the Test Automation **View** privilege, that role can only view test case details of recipes for which it has the Recipe **View** privilege.
> 
> Similarly, if you create a role with the Test Automation **Manage** privilege, this role can only manage Test cases of recipes for which it has the Recipe **View** and **Job history** privilege.

- Manage access to [Test Automation](/en/test-automation).
  - Full access
    
  - All Test Automation privileges: View and manage.
    
  - View
    
  - View [test case](/en/test-automation/test-case) details, including mock data and checks.
    
  - Manage (Create, Edit, Delete, Run)
    
  - View test case details
    
    Create new test cases
    
    Edit test cases
    
    Pick data for mocks from previous jobs
    
    Delete test cases
    
    Run test cases
    

* * *

### Workflow app

![Workflow app permissions](/assets/workflow-apps-permissions.Da-zL7qg.png)_Workflow app permissions_

Define access to Workflow apps, including the ability to create apps and manage settings for Workflow apps on an individual basis. These permissions only apply to the web interface and do not affect access to the Workflow apps connector. Access to the Workflow apps portal is determined by [Workflow apps portal](#apps-portal) permissions. Access to a Workflow app's corresponding data table is determined by [data tables](#data-tables) permissions.

#### App development

- The following granular permission is available for [Workflow app](/en/workflow-apps) development.
  - Full access
  - All Workflow app development permissions: view, edit, create, and delete pages, workflow stages, and tabs.

#### App access and role management

- Apply the following granular permissions to Workflow app access and role management privileges.
  - Full access
    
  - All Workflow app access and role management permissions: Manage app users and roles and the ability to publish or unpublish apps in the Workflow apps portal.
    
  - Manage access and role
    
  - Manage the users of your Workflow app.
    
  - Go live or Take offline
    
  - Allows users to publish a Workflow app in the Workflow apps portal or take an app offline.
    

* * *

### Data storage

![Permissions - data storage](/assets/privileges-project-properties.BIKZI3CS.png)_Data storage permissions_

#### Project properties

- Apply the following granular permissions to [Project properties](/en/features/project-properties)
  - Full access
    
  - All project property permissions: view, edit records, create, and delete.
    
  - View
    
  - Allows users to view project properties. Users cannot view masked properties.
    
  - Edit records
    
  - Allows users to edit property names and values.
    
  - Create
    
  - Allows users to create new project properties.
    
  - Delete
    
  - Allows users to delete project properties.
    

#### Data tables

- Apply the following granular permissions to [data tables](/en/data-tables).
  
  > **SCOPE OF GRANULAR PERMISSIONS**
  > 
  > These permissions only apply to data tables on the web interface. Access to Data tables and Workflow apps connectors is unaffected.
  
  - Full access
    
  - Enables all other permissions.
    
  - View
    
  - Allows users to view all data tables.
    
  - Edit records
    
  - Allows users to add, edit, or delete records in data tables.
    
  - Create
    
  - Allows users to create new data tables.
    
  - Delete
    
  - Allows users to delete data tables.
    
  - Modify structure
    
  - Allows users to add, delete, and update columns in data tables.
    

* * *

### Deployment

![Deployment privilege](/assets/new-deployment-permission.TcXp9bFR.png)_Deployment privilege_

> **DEPLOYMENT REQUIREMENTS**
> 
> To deploy a project to an environment, you must have the deployment privilege enabled in both the Development environment and the target environment (Test or Production).
> 
> Additionally, deployment permissions allow you to deploy all assets within a project, regardless of whether you have view or edit permissions for those assets.

- Manage access to project [deployments](/en/features/environments/deployment) across environments.
  - Full access
  - Manage deployments for an environment.

* * *

### Debug jobs

![debug jobs](/assets/privileges-debug-jobs.CI7ksmsB.png)_Debug jobs privileges_

#### Network trace

- Manage access to network tracing information in job histories.
  - Full access
  - View [network traces](/en/recipes/job-debug-tracing.html#viewing-job-debug-tracing) in job histories. Includes recipe input, output, and the network trace of HTTP calls. HTTP call information includes HTTP headers, requests, and communication (responses) between Workato and the end application.

* * *

## Platform tools privileges

- [Tools](#tools)
- [On-premise](#on-premise)
- [Workflow apps portal](#apps-portal)
- [Data storage](#data-storage-privileges)
- [API platform](#api-platform)
- [Connector SDK](#connector-sdk)
- [Insights](#insights)

### Tools

_Tools privileges_

#### Common data models

- Privileges for the common data model
  - Full access
    
  - All [Common data model](/en/features/common-data-model.html) permissions: View, edit, create, and delete.
    
  - View
    
  - View Common data models in the workspace.
    
  - Edit
    
  - Edit Common data models in the workspace.
    
  - Create
    
  - Create Common data models in the workspace.
    
  - Delete
    
  - Delete Common data models in the workspace.
    

#### Custom OAuth profiles

- Privileges for accessing custom OAuth profiles
  - Full access
    
  - All [Custom OAuth profile](/en/custom-oauth-profiles.html) permissions: view, edit, create, and delete.
    
  - View
    
  - View Custom OAuth Profiles and Enterprise Workbots.
    
  - Edit
    
  - Edit Custom OAuth Profiles and Enterprise Workbots.
    
  - Create
    
  - Create Custom OAuth Profiles and Enterprise Workbots.
    
  - Delete
    
  - Delete Custom OAuth Profiles and Enterprise Workbots.
    

#### FileStorage UI

- Privileges for the FileStorage UI
  - Full access
    
  - All [FileStorage UI](/en/features/filestorage/filestorage-console.html) permissions: View and create.
    
  - View
    
  - View files and directories in the FileStorage UI.
    
  - Create
    
  - Create directories in the FileStorage UI.
    

#### Message templates

- Privileges for message templates
  - Full access
    
  - All [Message template](/en/features/message-template.html) permissions: view, edit, create, and delete.
    
  - View
    
  - View Message templates in the workspace.
    
  - Edit
    
  - Edit Message templates in the workspace.
    
  - Create
    
  - Create Message templates in the workspace.
    
  - Delete
    
  - Delete Message templates in the workspace.
    

#### Event streams

- Privileges to the Event streams feature
  - Full access
    
  - All [Event streams](/en/connectors/pubsub.html) permissions: view, edit, create, and delete topics, as well as view history.
    
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
    

#### Recipe lifecycle management

- Privileges to recipe lifecycle management
  - Full access
  - Access to the [Recipe lifecycle management (RLCM)](/en/recipe-development-lifecycle.html) feature. This includes the ability to create manifests and view and interact with all assets included in manifests.

> **RLCM PRIVILEGES**
> 
> The Recipe lifecycle management privilege can indirectly provide collaborators with access to assets that are normally restricted by their assigned permission scope. This is because the RLCM privilege grants access to all manifests within a workspace. This means that a collaborator with this privilege can view assets in a manifest, even if they wouldn't normally have access to the project that contains these assets.
> 
> For example:
> 
> - `User A` creates `Project 1` and builds a manifest with RLCM and exports it
> - `User B` has the RLCM permission but no access to `Project 1`
> - `User B` can't access `Project 1` in the UI or use RLCM to build a manifest package with `Project 1` assets
> 
> `User B` can view, download, and use the export package that `User A` created, which contains the `Project 1` content.
> 
> Workato recommends regularly deleting manifests if you do not plan to provide access to the contents of these files to other users of Recipe lifecycle management (RLCM). This practice helps maintain the security and privacy of your data.
> 
> For enhanced security, you can use the [Deployment](/en/features/environments/deploying-projects-to-an-environment) feature. This feature leverages the export-import functionality to facilitate the transfer of assets, making it a more secure and efficient method to move assets across your environments.
> 
> Learn more about [RLCM](/en/recipe-development-lifecycle/rdlc-guide-planning).

#### Workbot

- Privileges to manage the Workbot
  - Full access
    
  - All [Workbot](/en/workbot/overview.html) permissions: view, edit, create, and delete.
    
  - View
    
  - View installed Workbots in the workspace.
    
  - Edit
    
  - Edit installed Workbots in the workspace.
    
  - Create
    
  - Create Workbots in the workspace.
    
  - Delete
    
  - Delete installed Workbots in the workspace.
    

#### Runtime user connections

- Privileges to manage runtime user connections
  - Full access
    
  - All [Runtime user connection](/en/features/runtime-user-connections.html) permissions: view, edit, and delete.
    
  - View
    
  - View the Runtime user connections setting.
    
  - Edit
    
  - Edit the Runtime user connections setting.
    
  - Delete
    
  - Delete the Runtime user connections setting.
    

#### Resources

- Privileges to resources
  - Full access
    
  - All Resource permissions: view, edit, create, and delete.
    
  - View
    
  - View resources.
    
  - Edit
    
  - Edit resources.
    
  - Create
    
  - Create resources.
    
  - Delete
    
  - Delete resources.
    

#### Logs

- Privileges to logs
  - Full access
    
  - Access to all logs.
    
    Typically, this privilege is reserved for **Environment admin** or legacy **Admin** roles. You can grant it to custom roles.
    

#### People task

- Privilege for managing the people task tool
  - Full access
  - Access to the [People task tool](/en/workflow.html).

#### Secrets management

- Privileges to manage security settings, including [secrets management](/en/security/data-protection/secrets-management/secrets-management.html).
  - Full access
    
  - All secrets management permissions: View and edit.
    
  - View
    
  - View secrets management details, including all secrets configured in your workspace.
    
  - Edit
    
  - Edit secrets for your workspace.
    

#### Manage locked projects

- Privileges to manage locked projects in the workspace
  - Full access
  - Unlock projects and manage project lock state within the workspace.

* * *

### On-premise

![On-premise privileges](/assets/privileges-on-prem.Ba691cV2.png)_On-premise privileges_

#### On-prem groups & agents

- Privileges for on-prem groups & agents
  - Full access
    
  - Access all [on-prem groups and agents](/en/on-prem.html) in the workspace; view, edit, create, and delete.
    
  - View
    
  - View on-prem groups and agents.
    
  - Edit
    
  - Edit on-prem groups and agents.
    
  - Create
    
  - Create on-prem groups and agents.
    
  - Delete
    
  - Delete on-prem groups and agents.
    

#### Connection - on-prem files

- Privilege for managing on-prem files connection. You can restrict who can create and manage connections for the file system of the machine where the on-prem agent is installed. Global [connection setting](#connection) takes precedence over this setting.
  - Full access
  - Access to create, edit, and delete on-prem files and on-prem files secondary connections.

#### Connection - command line scripts

- Privilege for managing on-prem command line scripts connection. You can restrict who can create and manage connections for the command line script execution on the machine where the on-prem agent is installed. Global [connection setting](#connection) takes precedence over this setting.
  - Full access
  - Access to create, edit, and delete on-prem command line scripts connections.

* * *

### Workflow apps portal

![Workflow apps portal permissions](/assets/apps-portal-permissions.BRtjyhQx.png)_Workflow apps portal permissions_

Define privileges to access the [Workflow apps portal](/en/workflow-apps/portal-settings). Access to create a Workflow app is determined by [Workflow app](#workflow-app) permissions. Access to a Workflow app's corresponding data table is determined by [data tables](#data-tables) permissions.

#### Settings

- Allows users to manage settings, including branding, authentication, and more, for the Workflow apps portal.
  - Full access
  - Full access to Workflow apps portal settings, including branding, authentication, and more.

#### Users and groups

- Enables users to manage users and groups in the Workflow apps portal.
  - Full access
  - Full access to users and groups: Create, delete, and edit users and groups, manage group membership, and more.

* * *

### Data storage

_Data storage privileges_

#### Lookup tables

- Apply the following granular permissions to the [lookup tables interface](/en/features/lookup-tables). The permissions you define here control access to all lookup tables that are accessible by this role: lookup tables that are scoped to **All projects**, and those [scoped to a project](/en/features/lookup-tables#assign-to-project) that this role can access.  
    
  - Full access
    
  - Enables all other permissions on Lookup tables.
    
  - View
    
  - Allows users to view all tables and their records.
    
  - Edit records
    
  - Allows users to add, edit, or delete records for all Lookup tables in the Lookup tables interface.  
      
    
    > **EDIT RECORDS WITH THE LOOKUP TABLES CONNECTOR**
    > 
    > Collaborators can still edit records (add, update, or delete) using the [lookup tables connector](/en/features/lookup-tables#actions), but only for the lookup tables they have access to.
    
  - Create
    
  - Allows users to create new tables in the Lookup tables interface.
    
  - Delete
    
  - Allows users to delete tables.
    
  - Modify structure
    
  - Allows users to edit the schema (to add, remove, or edit columns) for any table.
    

#### Environment properties

- Apply the following granular permissions to [Environment properties](/en/features/account-properties).
  - Full access
    
  - Enables all other permissions on Environment properties.
    
  - View
    
  - Allows users to view all Environment properties.
    
  - Edit records
    
  - Allows users to add, edit, or delete Environment properties.
    
  - Create
    
  - Allows users to create new Environment properties.
    
  - Delete
    
  - Allows users to delete Environment properties.
    

* * *

### API platform

_API Platform privileges_

#### Dashboard & logs

- Privileges for using the dashboard and logs
  - Full access
  - Full privileges for dashboard & logs: View metrics in dashboard and details in logs.

#### Collections & endpoints

- Privileges for collections and endpoints
  - Full access
    
  - All collections and endpoints access: view, edit, create, and delete.
    
  - View
    
  - View collections and endpoints.
    
  - Edit
    
  - Edit collections and endpoints.
    
  - Create
    
  - Create collections and endpoints.
    
  - Delete
    
  - Delete collections and endpoints.
    

#### Clients and access profiles

- Privileges for using client and access profiles
  - Full access
    
  - All clients and access profiles permissions: view, edit, create, and delete.
    
  - View
    
  - View clients and access profiles.
    
  - Edit
    
  - Edit clients and access profiles.
    
  - Create
    
  - Create clients and access profiles.
    
  - Delete
    
  - Delete clients and access profiles.
    

#### Policies

- Privileges for using policies
  - Full access
    
  - All policy permissions: view, edit, create, and delete.
    
  - View
    
  - View policy.
    
  - Edit
    
  - Edit policy.
    
  - Create
    
  - Create policy.
    
  - Delete
    
  - Delete policy.
    

#### Settings

- Privileges for API platform settings
  - Full access
  - Manage API prefix and custom domain.

* * *

### Connector SDK

_Connector SDK privileges_

#### Connector SDK

- Connector SDK privileges
  - Full access
  - Full [Connector SDK](/en/developing-connectors/sdk.html) permissions: view, edit, create, and delete.

#### Use in recipes

- Privileges for using the Connector SDK in recipes
  - Full access
  - Allow users to distribute custom connectors into this workspace.

### Insights

![Insights privileges](/assets/insights-privileges.CVUAmpEO.png)_Insights privileges_

- Choose the privileges that people with this role have for accessing Insights dashboards.
  - Full access
  - Complete access to the Insights feature, including the ability to **View**, **Edit**, **Create**, and **Delete** Insights dashboards.
  - View
  - View existing Insights dashboards.
  - Edit
  - Edit existing Insights dashboards.
  - Create
  - Create new Insights dashboards.
  - Delete
  - Delete Insights dashboards.

## Admin privileges

- [Workspace admin](#workspace-access)
- [Environment settings](#environment-settings)

### Workspace admin

_Workspace admin privileges_

#### Collaborators

- Manage collaborator privileges in the workspace
  - Full access
  - Manage [collaborators](/en/user-accounts-and-teams/team-collaboration.html) in the workspace, including adding, editing, and removing collaborators.

#### Collaborator roles (non-system)

- Manage non-system collaborator roles
  - Full access
  - View, edit, create, and delete [custom collaborator roles](/en/roles.html#custom-roles) in the workspace.

#### Collaborator SAML SSO auth

- Manage access to SAML SSO, such as Okta, OneLogin, or other identity authentication providers
  - Full access
  - View and edit [SAML SSO settings](/en/user-accounts-and-teams/single-sign-on.html) for the workspace.

#### Developer API

- Manage access for developer API
  - Full access
  - View and edit developer API settings for the workspace.

#### SCIM provisioning

- Manage SCIM provisioning settings
  - Full access
  - View and edit SCIM provisioning settings for the workspace.

#### Workspace settings

- Manage workspace settings
  - Full access
  - View and edit various workspace settings.

### Environment settings

_Environment settings privileges_

#### Activity audit

- Manage access to the activity audit logs
  - Full access
  - Access to view workspace activity in the [Dashboard's Activity audit log](/en/features/activity-audit-log). This permission grants the user the ability to view all activity logs, regardless of other access settings.

#### Debug, Log and Security

- Manage debug, logs, and security settings
  - Full access
  - Access to view and edit the workspace’s [environment-specific settings](/en/workspace#environment-related-settings), including error alerts, network trace, data retention, and AWS IAM information.

## XChange privileges

The **XChange** tab controls permissions to create, curate, and consume packages in [XChange](/en/xchange), Workato's package management and distribution platform.

- [Package creation](#xchange-package-creation)
- [Curation](#xchange-curation)
- [Consumption](#xchange-consumption)

### Package creation

#### Version

- Manage access to create and submit package versions to XChange.
  - Full access
    
  - All package version permissions: view, edit, and create.
    
  - View
    
  - View existing package versions.
    
  - Edit
    
  - Edit package versions.
    
  - Create
    
  - Create new package versions.
    

### Curation

#### Packages

- Manage access to review and distribute packages submitted to XChange.
  - Full access
    
  - All package curation permissions: delete, publish/distribute, review, and share.
    
  - Delete
    
  - Delete packages from XChange.
    
  - Publish/Distribute
    
  - Publish and distribute packages to XChange.
    
  - Review
    
  - Review submitted packages.
    
  - Share
    
  - Share packages with other workspaces.
    

#### Settings

- Manage access to configure XChange curation settings.
  - Full access
    
  - All XChange settings permissions: view and edit.
    
  - View
    
  - View XChange settings.
    
  - Edit
    
  - Edit XChange settings.
    

### Consumption

#### Verified Packages

- Manage access to browse and install verified packages from XChange in the private library.
  - Full access
    
  - All verified package permissions: view and install.
    
  - View
    
  - View verified packages in the private library.
    
  - Install
    
  - Install verified packages from XChange.
    

## Manage customers privileges (Embedded only)

The **Manage customers** interface only appears for [Embedded](/en/oem) collaborators with permission to create or modify collaborator roles.

### Manage customers

![Manage customers privileges](/assets/privileges-manage-customers.C7GcizcR.png) _Manage customers privileges_

#### Customers and customer managers

- Manage access to the **Customers** and **Customer managers** tabs of the Embedded Admin console
  - Full access
    
  - All [customers](/en/oem/admin-console/customers) and [customer managers](/en/oem/admin-console/customer-managers) permissions: View, manage, and delete customers and customer managers
    
  - View
    
  - View customers and customer managers
    
  - Manage
    
  - Add customers and assign customer managers
    
  - Delete
    
  - Delete customers and customer managers
    

#### Shared connectors

- Manage access to the **Shared connectors** tab of the Embedded admin console
  - Full access
    
  - All [shared connectors](/en/oem/admin-console/shared-connectors) permissions: View, manage, and delete shared connectors
    
  - View
    
  - View shared connectors
    
  - Manage
    
  - Manage shared connectors
    
  - Delete
    
  - Delete shared connectors
    

#### Usage metrics and settings

- Manage access to the **Usage metrics** and **Settings** tabs of the Embedded Admin console
  - Full access
    
  - All [usage metrics](/en/oem/admin-console/usage-metrics) and [settings](/en/oem/admin-console/settings) permissions: View and manage usage metrics and settings
    
  - View
    
  - View usage metrics and settings
    
  - Manage
    
  - Manage audit log streaming and branding settings. Note that only workspace owners and admins can manage audit log streaming.
    

## Automation HQ privileges

_Automation HQ privileges_

- Automation HQ
- Manage access to Automation HQ
  - Full access
  - Access to the Automation HQ functionality.

## Customer managers

![Customer managers permissions](/assets/customer-managers.BOl3tPQS.png)

- Define access to the customer manager API.
  - Customer manager API
  - Access all endpoints.
  - List all customer managers.
  - The ability to obtain a list of all customer managers.
  - Update role for customer manager
  - The ability to update a customer manager's role.
  - Create new customer manager
  - The ability to create a new customer manager.
  - Delete customer manager
  - The ability to delete a customer manager.

---

---
url: >-
  https://docs.workato.com/en/user-accounts-and-teams/role-based-access/managing-team-collaborators.md
description: >-
  Invite, manage, and remove collaborators in a Workato workspace, and assign
  roles and collaborator groups to control project access.
---

# Invite and manage workspace collaborators

You can invite, manage, and delete collaborators within a Workato workspace. Invitations add a collaborator to a workspace. It isn’t possible to invite a collaborator to only a specific project. However, you can invite a collaborator to your workspace with assigned collaborator groups that configure access to specific projects. Collaborators with project access can view the recipes, connections, and folders within those projects depending on the project role you assign and its associated privileges.

> **ACCESS REQUIREMENTS**
> 
> You must have one of the following privileges or roles to invite and manage workspace collaborators:
> 
> - An [Environment admin](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles#environment-admin) role or the legacy [Admin system role](/en/roles#system-roles)
> - A custom environment role with the [**Workspace access** privilege](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#workspace-access)
> 
> Workspaces that haven't migrated to the new access control model may still use the legacy **Admin** system role. After migration, equivalent permissions are granted through the **Environment admin** role or a custom environment role.

## Invite collaborators

Complete the following steps to invite a new collaborator to your workspace:

1. Sign in to your Workato account.
   
2. Go to **Workspace admin > Access control > Collaborators**.
   
3. Click **\+ Invite collaborator**.
   
4. Enter the **Name** and **Email address** of the collaborator.
   
5. Use the **Environment role** drop-down menu to select the [Environment role](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles) you plan to assign. If multiple environments are enabled, you must select an environment role for each environment individually.
   
6. Add the collaborator to one or more [Collaborator groups](/en/user-accounts-and-teams/role-based-access/new-model/collaborator-groups).
   
7. Click **Invite** to send the invitation.
   

> **INVITATION RATE LIMIT**
> 
> The collaborator may receive an error if you delete and resend an invitation too quickly. This occurs due to system rate limits that block repeated invitations in a short time window.
> 
> You must wait at least **20 minutes** before you resend the invitation to avoid this issue.

Users with an existing Workato account can sign in to accept the invitation. New users are prompted to create an account.

## Update a collaborator's role

You can update a collaborator’s environment role to manage their workspace-level permissions. Project-level access is managed separately within each project's settings.

> **USING ENVIRONMENTS**
> 
> If you plan to use the [Environments feature](/en/features/environments), ensure that you understand how to manage [workspace roles in environments](/en/user-accounts-and-teams/role-based-access/managing-environment-access) before changing a collaborator's role.

Complete the following steps to update an existing collaborator's role:

1. Sign in to your Workato account.
   
2. Go to **Workspace admin > Access control > Collaborators**.
   
3. Click the collaborator you plan to modify. This opens the **Edit collaborator** page.
   
4. Select a new **Environmental role** from the drop-down menu.
   
5. Click **Save changes**.
   

## Manage a collaborator's project access

Project-level roles are managed separately from environment roles and are configured within each project's settings:

> **PROJECT ROLE VISIBILITY**
> 
> Environment admins can assign project roles to themselves or other collaborators, even if they aren’t members of the project yet.
> 
> However, environment admins don't automatically gain access to project content. To view recipes, connections, and folders inside a project, you must first assign yourself a project role. Once assigned, you're automatically added as a project member and gain visibility based on the role’s permissions.

1. Open the project where you plan to manage access.
   
2. Go to **Settings > Project access**.
   
3. Update an existing collaborator's role using the **Project role** drop-down menu next to their name. Their access updates immediately.
   
4. Add a new collaborator by clicking **\+ Add collaborators**. Select the collaborators or groups, choose the appropriate **Project role**, and click **Add** to grant access.
   

## Delete collaborators

You can delete a collaborator from your workspace if someone has left your organization or no longer requires access to Workato.

Deleting a collaborator revokes their access but doesn’t delete any work the collaborator created, such as recipes, connections, or projects.

Complete the following steps to delete a collaborator:

1. Sign in to your Workato account.
   
2. Go to **Workspace admin > Access control > Collaborators**.
   
3. Select the collaborator you plan to remove to open their details page.
   
4. Click the **Delete** icon.
   
5. Review the warning that their work is retained, then click **Delete** to confirm.

---
