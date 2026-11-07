# Developer API

41 pages. Paths are relative to the repository root.


## Developer API

- **Developer API - Introduction** - `kb/docs/en/workato-api.md` - The Developer API lets you manage recipes, connections, jobs, and on-prem agents, and automate every aspect of your Workato workspace.
- **API clients and roles** - `kb/docs/en/workato-api/api-clients.md` - Learn how Developer API clients scope endpoint, environment, and project access at the workspace level and replace legacy full-access API keys.
- **GitHub secret scanning** - `kb/docs/en/workato-api/github-secret-scanning.md` - Learn how Workato integrates Developer API tokens with GitHub secret scanning to revoke leaked tokens and notify workspace admins.
- **Developer API quotas** - `kb/docs/en/workato-api/limits.md` - Reference for Workato Developer API timeout, rate, and payload quotas that govern requests to the platform's developer endpoints.
- **Developer API - Endpoints** - `kb/docs/en/workato-api/resources.md` - Reference index of all Workato Developer API endpoints, including Agent Studio, API clients, projects, recipes, roles, and more.

## Endpoints

- **Developer API - Environment properties** - `kb/docs/en/workato-api/account-properties.md` - Reference for the Workato environment properties API, with endpoints to list properties by prefix and upsert environment properties.
- **Developer API - Activity audit log reference** - `kb/docs/en/workato-api/activity-reference.md` - Reference for the resource types and event types you can use to filter responses from the Workato activity audit log API.
- **Developer API - Agent Studio** - `kb/docs/en/workato-api/agent-studio.md` - Reference for the Agent Studio API to create and manage genies, knowledge bases, skills, and guardrail policies programmatically.
- **Developer API - API clients** - `kb/docs/en/workato-api/api-client-apis.md` - Reference for the Workato developer API endpoints to list, create, update, delete, and regenerate tokens for API clients and client roles.
- **Developer API - Connectors** - `kb/docs/en/workato-api/api-connectors.md` - Reference for the Workato developer API endpoints that return standard and platform connector metadata, useful for building an app marketplace.
- **Developer API - API platform** - `kb/docs/en/workato-api/api-platform.md` - Reference for the API platform endpoints to create and manage API collections, endpoints, clients, and access profiles in Workato.
- **Developer API - Collaborator groups** - `kb/docs/en/workato-api/collaborator-groups.md` - Reference for the Workato developer API endpoints to list, create, update, delete collaborator groups and manage their members and project grants.
- **Developer API - Connection parameters reference** - `kb/docs/en/workato-api/connections-parameters-dev.md` - Reference for the connection parameters and provider values required to configure connectors using the Developer API.
- **Developer API - Connections** - `kb/docs/en/workato-api/connections.md` - Reference for the Workato developer API endpoints to list, create, update, disconnect, and delete connections, and get picklist values.
- **Developer API - Cross-workspace sharing** - `kb/docs/en/workato-api/cross-workspace-sharing.md` - Reference for the Workato cross-workspace sharing API to create, list, update, and revoke cross-workspace grants, review incoming grants, and discover grantable environments.
- **Developer API - Custom OAuth profiles** - `kb/docs/en/workato-api/custom-oauth-profiles.md` - Reference for the Workato developer API endpoints to list, create, update, and delete custom OAuth profiles.
- **Developer API - Custom connectors** - `kb/docs/en/workato-api/custom_connectors.md` - Reference for the Workato custom connectors API to create, search, update, validate, release, and share connectors and generate schema from JSON or CSV.
- **Developer API - Data pipelines** - `kb/docs/en/workato-api/data-pipelines.md` - Reference for the Workato data pipelines API to create, configure, start, stop, and clone pipelines, re-sync objects, and monitor object runs.
- **Developer API - Data tables** - `kb/docs/en/workato-api/data-tables.md` - Reference for the Workato data tables API to list, create, update, delete, and truncate tables and manipulate their records programmatically.
- **Developer API - Environment management** - `kb/docs/en/workato-api/environment-management.md` - Reference for the Workato environment management API to clear the secrets cache, retrieve activity audit logs, and manage tags.
- **Developer API - Environment roles** - `kb/docs/en/workato-api/environment-roles.md` - Reference for the Workato environment roles API to list, retrieve, create, update, and delete environment roles in your workspace.
- **Developer API - Event streams** - `kb/docs/en/workato-api/event-streams.md` - Reference for the Workato event streams API to publish and consume messages and create, list, update, purge, and delete event topics.
- **Developer API - Folders** - `kb/docs/en/workato-api/folders.md` - Reference for the Workato folders API to list, create, update, and manage folders and projects in your workspace.
- **Developer API - Jobs** - `kb/docs/en/workato-api/jobs.md` - Reference for the Workato jobs API to list recipe jobs, retrieve job metadata, resume a job, and repeat jobs programmatically.
- **Developer API - Lookup tables** - `kb/docs/en/workato-api/lookup-tables.md` - Reference for the Workato lookup tables API to list, create, and delete tables and add, get, update, and remove rows programmatically.
- **Developer API - MCP servers** - `kb/docs/en/workato-api/mcp-servers.md` - Reference for the Workato MCP servers API to create, update, and delete servers, assign tools and user groups, manage server policies, and manage hashed tokens.
- **Developer API - On-prem agents** - `kb/docs/en/workato-api/on-prem.md` - Reference for the Developer API on-premise endpoints to list, create, update, delete, and check the status of on-prem groups and agents.
- **Developer API - Project grants** - `kb/docs/en/workato-api/project-grants.md` - Reference for the Workato project grants API to get, list, add, update, and delete project role assignments for collaborators and groups.
- **Developer API - Project properties** - `kb/docs/en/workato-api/project-properties.md` - Reference for the Workato project properties API to list and upsert project-level properties by project ID and name prefix.
- **Developer API - Project roles** - `kb/docs/en/workato-api/project-roles.md` - Reference for the Workato project roles API to list, get, create, update, and delete project roles in a workspace.
- **Developer API - Projects** - `kb/docs/en/workato-api/projects.md` - Reference for the Workato projects API to build, deploy, and manage projects across the environments in your workspace.
- **Developer API - Recipe Lifecycle Management** - `kb/docs/en/workato-api/recipe-lifecycle-management.md` - Reference for the Workato Recipe Lifecycle Management API to create export manifests and export, import, and download asset packages.
- **Developer API - Recipes** - `kb/docs/en/workato-api/recipes.md` - Reference for the Workato recipes API to create, copy, update, start, stop, delete, and list recipes and manage recipe versions.
- **Developer API - Role migration** - `kb/docs/en/workato-api/role-migration.md` - Reference for the Workato role migration API to convert legacy system and custom roles into environment and project roles.
- **Developer API - Legacy roles** - `kb/docs/en/workato-api/roles.md` - Reference for the Workato legacy roles API to list, update, and copy custom roles in the legacy permissions model.
- **Developer API - Resources** - `kb/docs/en/workato-api/static-assets.md` - Reference for the Workato resources API to list, upload, download, and delete static asset files within a project.
- **Developer API - Tag assignments** - `kb/docs/en/workato-api/tag-assignments.md` - Reference for the Workato tag assignments API to apply or remove tags from recipes and connections in your workspace.
- **Developer API - Workspace collaborators** - `kb/docs/en/workato-api/team.md` - Reference for the Workato workspace collaborators API to invite, list, update, and delete collaborators and manage their roles.
- **Developer API - Test Automation** - `kb/docs/en/workato-api/test-automation.md` - Reference for the Workato Test Automation API to run recipe test cases and poll run requests by manifest, project, folder, or recipe.
- **Developer API - Workspace details** - `kb/docs/en/workato-api/users.md` - Reference for the Developer API workspace details resource, with the GET /api/users/me endpoint that returns details about your workspace.
- **Developer API - XChange** - `kb/docs/en/workato-api/xchange.md` - Reference for the Workato XChange API to browse and create packages, review and approve versions, publish to the private library, distribute packages, manage sharing links, and view installation analy
