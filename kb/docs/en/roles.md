---
url: 'https://docs.workato.com/en/roles.md'
description: >-
  Reference for Workato collaborator roles, including built-in system roles and
  custom roles that control access to features and folders.
---

# Collaborator roles

Collaborator roles control access to Workato features, functions, and folders of [Role-based access control](/en/user-accounts-and-teams/role-based-access/).

> **LEGACY MODEL**
> 
> This page describes the legacy permissions model. Workato is replacing legacy roles with the new permissions model, which uses environment roles and project roles. Refer to the [New permissions model](/en/user-accounts-and-teams/role-based-access/access-control-v2) documentation to plan and migrate.

This guide covers the following topics:

- [Workato's built-in system roles](#system-roles)
- [Add collaborator roles](#custom-roles)

To learn about the privileges collaborators can have, see [Collaborator privileges](/en/privileges).

> **ENVIRONMENTS AND WORKSPACE ROLES**
> 
> Find out how [Environments works with workspace roles](/en/user-accounts-and-teams/role-based-access/managing-environment-access).

* * *

## System roles

Workato pre-defines system roles so you can assign them to workspace collaborators, based on the access each user requires.

> **ROLE SCOPE**
> 
> Workato may change the specific set of privileges in system roles to support new platform features. These changes can expand or limit access but don't alter the role's core purpose.
> 
> In contrast, Workato doesn't update the scope of custom roles. Review custom roles regularly to ensure they meet your workspace's access requirements.

Workato has three system roles: [Admin](#role-admin), [Analyst](#role-analyst), and [Operator](#role-operator).

You cannot edit these roles directly. However, you can [clone](/en/user-accounts-and-teams/role-based-access/#cloning-roles) each role, and then modify it.

To view the privileges of a system role, an Admin can select a role in the **Roles** tab. This opens a read-only version of the role.

> **WORKSPACE OWNER**
> 
> The workspace owner has direct (root) access to the workspace, which is different from a designated role. Workato advises against using the root login for tasks requiring administrative privileges and recommends limiting its use to emergencies. For example, you can use the root log in to recover access to your admin workspace if you've lost access due to misconfiguring SAML.
> 
> The following privileges are associated with the root login of a workspace:
> 
> - All Admin role privileges
>   
> - All privileges included in the Admin role.
>   
> - Full Workspace admin settings access
>   
> - Access to all workspace admin settings.
>   

### Admin

The Admin role is typically granted to users managing the Workato workspace and is the most permissive system role. This role grants privileges to manage workspace settings and offers unique permissions for managing advanced settings such as key management, debugging, notifications, and secrets management. These permissions are exclusive to the Admin role and are not available to any other system or custom roles.

> **CLONING AN ADMIN ROLE**
> 
> Workato supports the cloning of all system and custom roles within your workspace. However, when you [clone](/en/user-accounts-and-teams/role-based-access/#cloning-roles) the Admin role, the unique permissions for managing advanced workspace settings do not transfer to the newly-created role. To grant collaborators the ability to manage workspace settings, they must be assigned to the Admin system role.

<dl class="horizontal-dl"><dt>Full project access</dt><dd>All <a href="/en/projects.html">project</a> permissions: View, edit, create, and delete.</dd><dt>Full folder access</dt><dd>All folder permissions: View, edit, create, and delete.</dd><dt>Full connection access</dt><dd>All <a href="/en/connections.html">connection</a> permissions: View, edit, create, and delete.</dd><dt>Full recipe access</dt><dd>All <a href="/en/recipes/building-recipes.html">recipe</a> permissions: View, edit, create, delete, run, and view job history.</dd><dt>Full access network trace</dt><dd>View <a href="/en/recipes/job-debug-tracing.html#viewing-job-debug-tracing">network traces</a> in job histories. Includes recipe input, output, and the network trace of HTTP calls. HTTP call information includes HTTP headers, requests, and communication (responses) between Workato and the end application.</dd><dt>All projects</dt><dd>Access to all <a href="/en/projects.html">projects</a> in a workspace.</dd><dt>Full access</dt><dd>Access to the <a href="/en/api-management.html">API Platform</a>, including dashboard and logs, collections and endpoints, clients and access profiles, policies, and settings.</dd><dt>Full Common data model access</dt><dd>All <a href="/en/features/common-data-model.html">Common data model</a> permissions: View, edit, create, and delete.</dd><dt>Full Custom OAuth Profile access</dt><dd>All <a href="/en/custom-oauth-profiles.html">Custom OAuth Profile</a> permissions: View, edit, create, and delete.</dd><dt>Full FileStorage UI access</dt><dd>All <a href="/en/features/filestorage/filestorage-console.html">FileStorage UI</a> permissions: View and create.</dd><dt>Full Lookup table access</dt><dd>Access to the <a href="/en/features/lookup-tables.html">Lookup tables</a> feature.</dd><dt>Full Message template access</dt><dd>All <a href="/en/features/message-template.html">Message template</a> permissions: View, edit, create, and delete.</dd><dt>Full On-prem groups access</dt><dd>Access all <a href="/en/on-prem.html">on-prem groups and agents</a> in the workspace.</dd><dt>Full People task access</dt><dd>Access to the <a href="/en/workflow.html">People task tool</a>.</dd><dt>Full Properties access</dt><dd>Access to all <a href="/en/features/account-properties.html">Environment Properties</a> in the workspace.</dd><dt>Full Event streams access</dt><dd>All <a href="/en/en/connectors/pubsub.html">Event streams</a> permissions: View, edit, create, and delete topics.</dd><dt>Full Recipe lifecycle management access</dt><dd>Access to the <a href="/en/recipe-development-lifecycle.html">Recipe lifecycle management</a> feature.</dd><dt>Full Workbot access</dt><dd>All <a href="/en/workbot/overview.html">Workbot</a> permissions: View, edit, create, and delete.</dd><dt>Full Runtime user connection access</dt><dd>All <a href="/en/features/runtime-user-connections.html">Runtime user connection</a> permissions: View and edit.</dd><dt>Full Logs access</dt><dd>Access to the <a href="/en/features/logging-service.html">Workato Log Service</a> feature.</dd><dt>Full Connector SDK access</dt><dd>All <a href="/en/developing-connectors/sdk.html">Connector SDK</a> permissions: View, edit, create, and delete.</dd><dt>Full Collaborator access</dt><dd>Manage the <a href="/en/user-accounts-and-teams/team-collaboration.html">team collaborators</a> in the workspace, including <a href="/en/user-accounts-and-teams/role-based-access/managing-team-collaborators.html">adding, editing, and removing collaborators</a>.</dd><dt>Full Custom collaborator roles access</dt><dd>View, edit, create, and delete <a href="/en/user-accounts-and-teams/role-based-access.html/#creating-custom-roles">custom team roles</a> in the workspace.</dd><dt>Full Collaborator SAML SSO access</dt><dd>View and edit <a href="/en/user-accounts-and-teams/single-sign-on.html">SAML SSO settings</a> for the workspace.</dd><dt>Full API client access</dt><dd>View and edit <a href="/en/workato-api.html">API Clients</a> for the workspace.</dd><dt>Full activity audit</dt><dd>Access to view team activity in the <a href="/en/features/activity-audit-log.html">Dashboard's Activity audit log</a>. This permission grants the user the ability to view all activity logs, regardless of other access settings.</dd><dt>Full key management</dt><dd>Access to the account's <a href="/en/security/data-protection/encryption-key-management.html">Key Management System (KMS)</a>. Users with this privilege can update key policies and encryption keys.</dd><dt>Full Test Automation</dt><dd>All <a href="/en/test-automation.html">Test Automation</a> permissions: view and manage test case details.</dd><dt>Full Workflow apps access</dt><dd>All <a href="/en/workflow-apps.html">Workflow apps</a> permissions: create, edit, and delete Workflow apps, and manage settings for Workflow apps.</dd><dt>Full Workflow apps portal access</dt><dd>All <a href="/en/workflow-apps/portal.html">Workflow apps portal</a> permissions: configure Workflow apps portal settings and manage users and groups.</dd><dt>Full Insights access</dt><dd>All <a href="/en/insights.html">Insights</a> permissions: View, create, edit, and delete Insights dashboards.</dd><dt>Full Blueprint access</dt><dd>All Blueprint permissions: View, edit, create, and delete.</dd><dt>Full XChange access</dt><dd>All <a href="/en/xchange.html">XChange</a> permissions: create, curate, and consume packages.</dd></dl>

### Analyst

Analysts are typically users who build and test recipes or custom connectors.

<dl class="horizontal-dl"><dt>Full project access</dt><dd>All <a href="/en/projects.html">project</a> permissions: View, edit, create, and delete.</dd><dt>Full folder access</dt><dd>All folder permissions: View, edit, create, and delete.</dd><dt>Full connection access</dt><dd>All <a href="/en/connections.html">connection</a> permissions: View, edit, create, and delete.</dd><dt>Full recipe access</dt><dd>All <a href="/en/recipes/building-recipes.html">recipe</a> permissions: View, edit, create, delete, run, and view job history.</dd><dt>All projects</dt><dd>Access to all <a href="/en/projects.html">projects</a> in a workspace.</dd><dt>Full access</dt><dd>Access to the <a href="/en/api-management.html">API Platform</a>, including dashboard and logs, collections and endpoints, clients and access profiles, policies, and settings.</dd><dt>Full Common data model access</dt><dd>All <a href="/en/features/common-data-model.html">Common data model</a> permissions: View, edit, create, and delete.</dd><dt>Full Custom OAuth Profile access</dt><dd>All <a href="/en/custom-oauth-profiles.html">Custom OAuth Profile</a> permissions: View, edit, create, and delete.</dd><dt>Full FileStorage UI access</dt><dd>All <a href="/en/features/filestorage/filestorage-console.html">FileStorage UI</a> permissions: View and create.</dd><dt>Full Lookup table access</dt><dd>Access to the <a href="/en/features/lookup-tables.html">Lookup tables</a> feature.</dd><dt>Full Message template access</dt><dd>All <a href="/en/features/message-template.html">Message template</a> permissions: View, edit, create, and delete.</dd><dt>Full On-prem groups access</dt><dd>Access all <a href="/en/on-prem.html">on-prem groups and agents</a> in the workspace.</dd><dt>Full People task access</dt><dd>Access to the <a href="/en/workflow.html">People task tool</a>.</dd><dt>Full Event streams access</dt><dd>All <a href="/en/en/connectors/pubsub.html">Event streams</a> permissions: View, edit, create, and delete topics.</dd><dt>Full Workbot access</dt><dd>All <a href="/en/workbot/overview.html">Workbot</a> permissions: View, edit, create, and delete.</dd><dt>Full Runtime user connection access</dt><dd>All <a href="/en/features/runtime-user-connections.html">Runtime user connection</a> permissions: View and edit.</dd><dt>Full Connector SDK access</dt><dd>All <a href="/en/developing-connectors/sdk.html">Connector SDK</a> permissions: View, edit, create, and delete.</dd><dt>Full Test Automation</dt><dd>All <a href="/en/test-automation.html">Test Automation</a> permissions: view and manage test case details.</dd><dt>Full Workflow apps access</dt><dd>All <a href="/en/workflow-apps.html">Workflow apps</a> permissions: create, edit, and delete Workflow apps, and manage settings for Workflow apps.</dd><dt>Full Workflow apps portal access</dt><dd>All <a href="/en/workflow-apps/portal.html">Workflow apps portal</a> permissions: configure Workflow apps portal settings and manage users and groups.</dd><dt>Full Insights access</dt><dd>All <a href="/en/insights.html">Insights</a> permissions: View, create, edit, and delete Insights dashboards.</dd><dt>Deploy and review</dt><dd>Deploy recipes and review deployment requests.</dd><dt>Genies</dt><dd>Full access to <a href="/en/agentic/agent-studio.html">Genies</a>.</dd><dt>Knowledge bases</dt><dd>Full access to <a href="/en/agentic/agent-studio/create-a-genie.html#create-a-knowledge-base">Knowledge bases</a>.</dd><dt>Data pipelines</dt><dd>Full access to <a href="/en/data-orchestration/data-pipeline-recipe/create-data-pipeline-recipe.html">data pipelines</a>.</dd></dl>

### Operator

Operators are users who focus on maintaining and validating existing recipes. This is the least permissive system role.

This role includes **read-only** access to **All folders** and **All projects**.

<dl class="horizontal-dl"><dt>View projects</dt><dd>View specific projects in a workspace.</dd><dt>View folders</dt><dd>View folders and sub-folders in a workspace.</dd><dt>View recipes</dt><dd>View recipes in a workspace.</dd><dt>Test (start/stop) recipes</dt><dd>Run recipes and start and stop recipe tests in a workspace.</dd><dt>View recipe job history</dt><dd>View a recipe's job history in the Jobs tab.</dd><dt>View recipe job history</dt><dd>View a recipe's job history in the Jobs tab.</dd><dt>View Genies</dt><dd>Read-only access to <a href="/en/agentic/agent-studio.html">Genies</a>.</dd><dt>View Knowledge Bases</dt><dd>Read-only access to <a href="/en/agentic/agent-studio/create-a-genie.html#create-a-knowledge-base">Knowledge Bases</a>.</dd><dt>View data pipelines</dt><dd>Read-only access to <a href="/en/data-orchestration/data-pipeline-recipe/create-data-pipeline-recipe.html">data pipelines</a>.</dd><dt>All projects</dt><dd>Access to all <a href="/en/projects.html">projects</a> in a workspace.</dd></dl>

Additionally, this role includes **read-only** access to the Test Automation feature.

<dl class="horizontal-dl"><dt>View Test Automation</dt><dd>View test cases, including mock data and checks in the <a href="/en/test-automation.html">Test Automation</a> feature.</dd></dl>

## Add collaborator roles

In addition to system roles, you can create additional custom collaborator roles to assign more granular privileges to workspace collaborators. System roles have preset permissions, but the roles you add can be customized, allowing you to control access levels for projects, recipes, tools, and more.

For example, you can assign distinct collaborator roles to development, QA, and production teams within the same workspace, each with specific privileges that align with the [recipe development lifecycle](/en/recipe-development-lifecycle).

[Inheritable roles](/en/automation-hq#inheritable-roles) are custom roles that AHQ admins create in the HQ workspace. These roles automatically appear in all managed workspaces as non-editable roles.

Refer to the [Role-based access guide](/en/user-accounts-and-teams/role-based-access/#creating-custom-roles) to learn how to add a collaborator role.

> **FEATURE AVAILABILITY**
> 
> The custom collaborator role feature is included in specific pricing plans. Refer to your pricing plan and contract to learn more.

---
