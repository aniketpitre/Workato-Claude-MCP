---
url: 'https://docs.workato.com/en/workato-api/limits.md'
description: >-
  Reference for Workato Developer API timeout, rate, and payload quotas that
  govern requests to the platform's developer endpoints.
---

# Developer API rate limits

Workato enforces specific quotas on its developer APIs to optimize performance and stability.

> **DEFAULT QUOTAS**
> 
> The quotas on this page are defaults based on Workato best practices and are configured to enable optimal platform performance. Customers on Enterprise plans or above can contact their Customer Success Representative to request an extension of these quotas for their specific use cases.

Requests made to the Developer API are subject to the following timeout limit:

| Description | Quota |
| --- | --- |
| Timeout limit | 40 seconds |

In addition, Developer API resources have the following rate and payload quotas:

| Collection | Type | Resource | Quota |
| --- | --- | --- | --- |
| **Agent studio** | GET | List genies: [/api/agentic/genies](https://docs.workato.com/workato-api/agent-studio.html#list-genies) | 1,000 requests per minute |
| **Agent studio** | GET | Get a genie by ID: [/api/agentic/genies/:id](https://docs.workato.com/workato-api/agent-studio.html#get-a-genie-by-id) | 1,000 requests per minute |
| **Agent studio** | GET | All [genie conversation](https://docs.workato.com/workato-api/agent-studio.html#conversations) endpoints | 10 requests per second |
| **Agent studio** | All | All other [genie](https://docs.workato.com/workato-api/agent-studio.html#genies) endpoints | 60 requests per minute |
| **Agent studio** | GET | List Knowledge bases: [/api/agentic/knowledge\_bases](https://docs.workato.com/workato-api/agent-studio.html#list-knowledge-bases) | 1,000 requests per minute |
| **Agent studio** | GET | Get a Knowledge base by ID: [/api/agentic/knowledge\_bases/:id](https://docs.workato.com/workato-api/agent-studio.html#get-a-knowledge-base-by-id) | 1,000 requests per minute |
| **Agent Studio** | All | All other [Knowledge bases](https://docs.workato.com/workato-api/agent-studio.html#knowledge-bases) endpoints | 60 requests per minute |
| **Agent Studio** | GET | List Skills: [/api/agentic/skills](https://docs.workato.com/workato-api/agent-studio.html#list-skills) | 1,000 requests per minute |
| **Agent Studio** | GET | Get a skill by ID: [api/agentic/skills/:id](https://docs.workato.com/workato-api/agent-studio.html#get-a-skill-by-id) | 1,000 requests per minute |
| **Agent studio** | All | All other [Skills](https://docs.workato.com/workato-api/agent-studio.html#skills) endpoints | 60 requests per minute |
| **API clients** | All | All [API client](https://docs.workato.com/workato-api/api-client-apis.html) endpoints | 60 requests per minute |
| **API platform** | All | All [API platform](/en/workato-api/api-platform.html) endpoints | 60 requests per minute |
| **Collaborator groups** | All | All [Collaborator groups](/en/workato-api/collaborator-groups.html) endpoints | 60 requests per minute |
| **XChange** | All | All [XChange](/en/workato-api/xchange.html) endpoints | 60 requests per second |
| **Connections** | GET | List connections: [/api/connections](/en/workato-api/connections.html#list-connections) | 60 requests per minute |
| **Connections** | All | All other [Connections](/en/workato-api/connections.html) endpoints | 1 request per second |
| **Connectors** | All | All [Connectors](/en/workato-api/api-connectors.html) endpoints | 60 requests per minute |
| **Custom connectors** | POST | Generate schema from JSON: [/api/sdk/generate\_schema /json](/en/workato-api/custom_connectors.html#generate-schema-from-json) | 60 requests per minute |
| **Custom connectors** | POST | Generate schema from CSV: [/api/sdk/generate\_schema /csv](/en/workato-api/custom_connectors.html) | 60 requests per minute |
| **Custom connectors** | All | All other [Custom connectors](/en/workato-api/custom_connectors.html) endpoints | 1 request per second |
| **Custom OAuth profiles** | All | All [Custom OAuth profiles](/en/workato-api/custom-oauth-profiles.html#create-custom-oauth-profile) endpoints | 60 requests per minute |
| **Data pipelines** | All | All [Data pipelines](/en/workato-api/data-pipelines.html) endpoints | 60 requests per minute |
| **Data tables** | All | All [Data tables](/en/workato-api/data-tables.html) endpoints | 60 requests per minute |
| **Environment management** | All | All [Environment management](/en/workato-api/environment-management.html) endpoints | 60 requests per minute |
| **Environment properties** | All | All [Environment properties](/en/workato-api/account-properties.html) endpoints | 60 requests per minute |
| **Environment roles** | All[](/en/workato-api/environment-roles.html) | All [Environment roles](/en/workato-api/environment-roles.html) endpoints | 60 requests per minute |
| **Event streams** | All | All [Event streams](/en/workato-api/event-streams.html) endpoints | 60 requests per minute |
| **Event streams** | All | All [Event streams](/en/workato-api/event-streams.html) endpoints | Maximum payload size:​ 1 MB |
| **Event streams public API** | All | All [Event streams public API](/en/workato-api/pubsub.html) endpoints | 60 requests per minute |
| **Event streams public API** | All | All [Event streams public API](/en/workato-api/pubsub.html) endpoints | Maximum payload size:​ 10 MB |
| **Folders** | All | All [Folders](/en/workato-api/folders.html) endpoints | 60 requests per minute |
| **Jobs** | POST | Repeat jobs: [/api/recipes/:recipe\_id/repeat\_jobs](/en/workato-api/jobs.html#repeat-jobs) | 25 jobs per request |
| **Jobs** | POST | Repeat jobs: [/api/recipes/:recipe\_id/repeat\_jobs](/en/workato-api/jobs.html#repeat-jobs) | 1 request per second |
| **Jobs** | POST | Cancel jobs: [/api/recipes/:recipe\_id/cancel\_jobs](/en/workato-api/jobs.html#cancel-jobs) | 25 jobs per request |
| **Jobs** | POST | Cancel jobs: [/api/recipes/:recipe\_id/cancel\_jobs](/en/workato-api/jobs.html#cancel-jobs) | 1 request per second |
| **Jobs** | POST | Force an on-demand run of a recipe: [/api/recipes/:recipe\_id/force\_run](/en/workato-api/recipes.html#force-run-a-recipe) | 1 request per second |
| **Jobs** | All | All other [Jobs](/en/workato-api/jobs.html) endpoints | 60 requests per minute |
| **Lookup tables** | POST | Delete lookup tables in batch: [/api/lookup\_tables/batch\_delete](/en/workato-api/lookup-tables.html#lut-delete) | 1 request per second |
| **Lookup tables** | All | All other [Lookup tables](workato-api/lookup-tables.html) endpoints | 60 requests per minute |
| **On-prem** | All | All [On-prem](/en/workato-api/on-prem.html) endpoints | 60 requests per minute |
| **Projects** | All | All [Projects](/en/workato-api/projects.html) endpoints | 60 requests per minute |
| **Project grants** | All[](/en/workato-api/project-grants.html) | All [Project grants](/en/workato-api/project-grants.html) endpoints | 60 requests per minute |
| **Project properties** | All | All [Project properties](/en/workato-api/project-properties.html) endpoints | 60 requests per minute |
| **Project roles** | All[](/en/workato-api/project-roles.html) | All [Project roles](/en/workato-api/project-roles.html) endpoints | 60 requests per minute |
| **Resources** | All | All [Resources](/en/workato-api/static-assets.html) endpoints | 60 requests per minute |
| **Recipes** | POST | Create a recipe: [/api/recipes](/en/workato-api/recipes.html#create-a-recipe) | 1 request per second |
| **Recipes** | POST | Start analyzing recipe health: [/api/recipes/:recipe\_id/health](/en/workato-api/recipes.html#start-analyzing-recipe-health) | 20 requests per minute |
| **Recipes** | All | All other [Recipes](/en/workato-api/recipes.html#get-recipe-details) endpoints | 60 requests per minute |
| **Recipe lifecycle management** | POST | Import a package into a folder: [/api/packages/import/:folder\_id](/en/workato-api/recipe-lifecycle-management.html#import-package-into-a-folder) | 500 requests per hour per user ID. If this quota is exceeded, the system denies additional requests until the following hour when the request allowance resets. |
| **Recipe lifecycle management** | All | All other [Recipe lifecycle management](/en/workato-api/recipe-lifecycle-management.html) endpoints | 60 requests per minute |
| **Legacy roles** | All | All [Legacy roles](/en/workato-api/roles.html) endpoints | 60 requests per minute |
| **Role migration** | All[](/en/workato-api/role-migration.html) | All [Role migration](/en/workato-api/role-migration.html) endpoints | 60 requests per minute |
| **Tag assignments** | All | All [Tag assignments](/en/workato-api/tag-assignments.html) endpoints | 60 requests per minute |
| **Test automation** | All | All [Test Automation](/en/workato-api/test-automation.html) endpoints | 60 requests per minute |
| **Workspace collaborators** | POST | Invite a collaborator: [/api/member\_invitations](/en/workato-api/team.html#invite-collaborator) | 60 requests per minute Additionally, you can send one request per user and workspace ID every 20 minutes to this endpoint. |
| **Workspace collaborators** | All | All other Workspace collaborators endpoints | 60 requests per minute |
| **Workspace details** | All | All [Workspace details](/en/workato-api/users.html) endpoints | 60 requests per minute |
| **Workato Identity IAM** | All | All [Workato Identity IAM](/en/workato-api/workato-identity-iam.html) endpoints | 60 requests per minute |
| **Cross-workspace sharing** | Read | All read [Cross-workspace sharing](/en/workato-api/cross-workspace-sharing.html) endpoints | 600 requests per minute |
| **Cross-workspace sharing** | Write | All write [Cross-workspace sharing](/en/workato-api/cross-workspace-sharing.html) endpoints | 60 requests per minute |

> **FURTHER READING**
> 
> Refer to the [Platform quotas](/en/limits) documentation for more information about Workato quotas.

---
