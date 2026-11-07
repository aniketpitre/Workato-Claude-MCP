# CI/CD and operations

25 pages. Paths are relative to the repository root.


## CI/CD and operations

- **Operations hub dashboard** - `kb/docs/en/features/admin-dashboard.md` - The Workato Operations hub dashboard gives a real-time view of recipes and connections, with insights and analytics to help you resolve issues.
- **Recipe lifecycle management** - `kb/docs/en/recipe-development-lifecycle.md` - Learn how recipe lifecycle management (RLCM) lets teams export and import packages to move recipes and dependencies across Workato environments.
- **Lifecycle and operations** - `kb/docs/en/recipes/managing-recipes.md` - Manage Workato automation assets across their lifecycle with environments, the Operations hub dashboard, and the activity audit log.

## Environments

- **Environments** - `kb/docs/en/features/environments.md` - Environments let your team plan, test, and deploy automation projects across development, test, and production with built-in change management.
- **Environments - Best practices** - `kb/docs/en/features/environments/best-practices.md` - Learn best practices for using Workato Environments, including asset organization, connection management, and collaborator access.
- **Environments - Deploying A Project To An Environment** - `kb/docs/en/features/environments/deploying-projects-to-an-environment.md` - Deploy a project from Development to Test or Production in Workato, customize the deployment, review changes, and re-establish connections.
- **Environments - Understanding project deployment with environments** - `kb/docs/en/features/environments/deployment.md` - Learn how to deploy Workato projects across Development, Test, and Production environments, including dependencies and deployment details.
- **Environments - Review and approve deployments** - `kb/docs/en/features/environments/reviews-approvals.md` - Set up the Workato deployment review and approval workflow to govern recipe deployments across environments with audit trails and sign-off.
- **Manage environment access** - `kb/docs/en/user-accounts-and-teams/role-based-access/managing-environment-access.md` - Manage collaborator access to Workato DEV, TEST, and PROD environments by assigning environment and project roles with role-based access control.

## Operations hub dashboard

- **Activity audit log FAQs** - `kb/docs/en/features/activity-audit-log-faqs.md` - Answers to common questions about the Workato Activity audit log, including enabling it, customizing messages, and streaming retries.
- **Activity Audit Log - Reference** - `kb/docs/en/features/activity-audit-log-reference.md` - Reference for Workato Activity audit log events, listing account, recipe, and connection activities tracked in your workspace.
- **Audit log streaming - Custom log messages** - `kb/docs/en/features/activity-audit-log-streaming-customize-log.md` - Customize Workato audit log messages with JSON and placeholders before streaming them to destinations like Amazon S3, Splunk, or Datadog.
- **Audit log streaming destinations** - `kb/docs/en/features/activity-audit-log-streaming-destinations.md` - Configure audit log streaming destinations in Workato, including Amazon S3, Azure Monitor, Azure Blob Storage, and Google Cloud Storage.
- **Activity audit log streaming retry** - `kb/docs/en/features/activity-audit-log-streaming-retry.md` - Learn how Workato retries failed audit log streaming using a persistent cache and exponential backoff over a seven-day window.
- **Sample activity audit log** - `kb/docs/en/features/activity-audit-log-streaming-sample.md` - Reference for the Workato activity audit log JSON file, including the file path and name format plus sample job history data.
- **Activity audit log streaming** - `kb/docs/en/features/activity-audit-log-streaming.md` - Set up audit log streaming in Workato to replicate and store log data in an external destination beyond standard retention periods.
- **Activity Audit Log - view** - `kb/docs/en/features/activity-audit-log-view.md` - View and filter the Workato activity audit log by period, collaborators, clients, and asset type from the Operations hub.
- **Activity Audit Log - overview** - `kb/docs/en/features/activity-audit-log.md` - Learn how Workato activity audit logs let administrators track user logins, recipe changes, and other account activity over time.
- **Operations hub dashboard FAQs** - `kb/docs/en/features/admin-dashboard-faqs.md` - Answers to common questions about the Workato Operations hub dashboard, including recipe insights, jobs graph customization, and metrics.
- **Dependency graph** - `kb/docs/en/features/dependency-graph.md` - Use the Workato dependency graph to visualize relationships between workspace assets and analyze the impact of upstream and downstream changes.

## Recipe lifecycle management

- **Using a recipe diff to compare recipe changes** - `kb/docs/en/recipe-development-lifecycle/compare-versions-with-recipe-diff.md` - Learn how the Workato Recipe Diff feature visually compares two recipe or skill versions so you can review changes side by side.
- **Recipe lifecycle management - Exporting assets** - `kb/docs/en/recipe-development-lifecycle/export.md` - Export Workato recipes and their dependencies into package zip files to move assets between environments or store them in version control.
- **Recipe lifecycle management - Importing** - `kb/docs/en/recipe-development-lifecycle/import.md` - Import a package of exported recipes and dependencies to deploy them into a Workato workspace using the package import UI or deployment APIs.
- **Planning for lifecycle management** - `kb/docs/en/recipe-development-lifecycle/rdlc-guide-planning.md` - Plan recipe lifecycle management in Workato by defining environments, promotion criteria, and team roles before moving assets between stages.
- **Working with external source control systems** - `kb/docs/en/recipe-development-lifecycle/rdlc-guide-source-control.md` - Learn how to store exported Workato recipes in external source control like git, mapping projects to repositories and managing pull requests.
