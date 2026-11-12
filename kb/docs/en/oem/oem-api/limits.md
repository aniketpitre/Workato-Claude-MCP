---
url: 'https://docs.workato.com/en/oem/oem-api/limits.md'
description: >-
  Reference for Embedded API rate, timeout, and payload quotas applied to
  requests across Embedded API resources.
---

# Rate limits

Workato enforces rate limits on Embedded APIs to optimize performance and stability. These quotas apply at the Embed admin workspace level, not at the individual customer workspace level or per API key. This means all API requests from an Embed admin workspace share the same rate limit, regardless of which customer workspace is invoked or which admin API key makes the request. The Embedded API is only accessible from Embed admin workspaces.

> **DEFAULT QUOTAS**
> 
> The quotas on this page are defaults based on Workato best practices and are configured to enable optimal platform performance. Customers on Enterprise plans or above can contact their Customer Success Representative to request an extension of these quotas for their specific use cases.

Requests made to the Embedded API are subject to the following timeout limit:

| Description | Quota |
| --- | --- |
| Timeout limit | 40 seconds |

In addition, Embedded API resources have the following rate and payload quotas:

| Collection | Type | Resource | Quota |
| --- | --- | --- | --- |
| **API clients** | GET | List Developer API Clients: [/api/v2/managed\_users/:managed\_user\_id /developer\_api\_clients](/en/oem/oem-api/api-clients.html#list-developer-api-clients) | 1,000 requests per minute |
| **API clients** | GET | List Developer API Client roles: [/api/v2/managed\_users/:managed\_user\_id /developer\_api\_client\_roles](/en/oem/oem-api/api-clients.html#list-developer-api-client-roles) | 1,000 requests per minute |
| **API clients** | All | All other [API Client](/en/oem/oem-api/api-clients.html) endpoints | 60 requests per minute |
| **API platform** | All | All [API portals](/en/oem/oem-api/api-platform.html#list-api-portals) endpoints | 60 requests per minute |
| **API platform** | All | All [API collections](/en/oem/oem-api/api-platform.html#list-api-collections) endpoints | 1,000 requests per minute |
| **API platform** | All | All [API endpoint](/en/oem/oem-api/api-platform.html#list-api-endpoints) endpoints | 1,000 requests per minute |
| **API platform** | All | All [API clients](/en/oem/oem-api/api-platform.html#list-api-clients) endpoints | 1,000 requests per minute |
| **API platform** | All | All [API access profiles](/en/oem/oem-api/api-platform.html#list-access-profiles) endpoints | 1,000 requests per minute |
| **API platform** | All | All [API certificate bundles](/en/oem/oem-api/api-platform.html#list-certificate-bundles) endpoints | 60 requests per minute |
| **Collaborator groups** | GET | List group project grants: [/api/v2/managed\_users/:managed\_user\_id/ user\_groups/:id/project\_grants](/en/oem/oem-api/collaborator-groups.html#list-collaborator-grants) | 60 requests per minute |
| **Collaborator groups** | All | All other [Collaborator groups](/en/oem/oem-api/collaborator-groups.html) endpoints | 10 requests per second |
| **Connections** | GET | List connections: [/api/managed\_users/:managed\_user\_id /connections](/en/oem/oem-api/connections.html#list-connections) | 1,000 requests per minute |
| **Connections** | All | All other [Connections](/en/oem/oem-api/connections.html) endpoints | 60 requests per minute |
| **Connectors** | All | All [Connectors](/en/oem/oem-api/adapters.html) endpoints | 1,000 requests per minute |
| **Custom connectors** | All | All [Custom connectors](/en/oem/oem-api/custom_connectors.html) endpoints | 60 requests per minute |
| **Custom OAuth profiles** | All | All [Custom OAuth profiles](/en/oem/oem-api/custom-oauth-profiles.html) endpoints | 60 requests per minute |
| **Customer managers** | All | All [Customer managers](/en/oem/oem-api/customer-managers.html) endpoints | 60 requests per minute |
| **Customer workspace collaborators** | All | All [Customer workspace collaborators](/en/oem/oem-api/team.html) endpoints | 60 requests per minute. Additionally, you can send one request per user and workspace ID every 20 minutes to the **Invite collaborator to managed customer workspace** endpoint. |
| **Data retention** | All | All [Data retention](/en/oem/oem-api/data-retention.html) endpoints | 60 requests per minute |
| **Data tables** | GET, POST | Read endpoints: [Query records](/en/oem/oem-api/data-tables.html#query-records), [Download file from the record](/en/oem/oem-api/data-tables.html#download-file-from-the-record), [Describe uploaded file](/en/oem/oem-api/data-tables.html#describe-uploaded-file) | 200 requests per second |
| **Data tables** | POST, PUT, DELETE | Write endpoints: [Create record](/en/oem/oem-api/data-tables.html#create-record), [Update record](/en/oem/oem-api/data-tables.html#update-record), [Delete record](/en/oem/oem-api/data-tables.html#delete-record), [Generate link to upload file](/en/oem/oem-api/data-tables.html#generate-link-to-upload-file), All other [Record import](/en/oem/oem-api/data-tables.html#record-import-apis) endpoints | 40,000 values per second |
| **Data tables** | All | All other [Data tables](/en/oem/oem-api/data-tables.html) endpoints | 60 requests per minute |
| **Dynamic field mapping** | All | All [Dynamic field mapping](/en/oem/oem-api/dynamic-field-mapping.html) endpoints | 60 requests per minute |
| **Environment management** | All | All [Environment management](/en/oem/oem-api/environment-management.html) endpoints | 60 requests per minute |
| **Environment properties** | GET | List properties by prefix: [/api/managed\_users/:managed\_user\_id /properties](/en/oem/oem-api/account-properties.html#list-properties-by-prefix) | 1,000 requests per minute |
| **Environment properties** | All | All other [Environment properties](/en/oem/oem-api/account-properties.html) endpoints | 60 requests per minute |
| **Environment roles** | All[](/en/oem/oem-api/environment-roles.html) | All [Environment roles](/en/oem/oem-api/environment-roles.html) endpoints | 10 requests per second |
| **Event streams** | All | All [Event streams](/en/oem/oem-api/event-streams.html) endpoints | 60 requests per minute |
| **Folders** | All | All [Folders](/en/oem/oem-api/folders.html) endpoints | 60 requests per minute |
| **Jobs** | POST | Repeat jobs: [/api/managed\_users/:managed\_user\_id/recipes /:recipe\_id/repeat\_jobs](/en/oem/oem-api/jobs.html#repeat-jobs) | 25 jobs per request |
| **Jobs** | POST | Repeat jobs: [/api/managed\_users/:managed\_user\_id/recipes /:recipe\_id/repeat\_jobs](/en/oem/oem-api/jobs.html#repeat-jobs) | 1 request per second |
| **Jobs** | POST | Force an on-demand run of a recipe: [/api/managed\_users/:managed\_user\_id /recipes/:recipe\_id/force\_run](/en/oem/oem-api/recipes.html#force-run-a-recipe) | 1 request per second |
| **Jobs** | All | All other [Jobs](/en/oem/oem-api/jobs.html) endpoints | 1,000 requests per minute |
| **JWT Public Key** | All | All [JWT public key](/en/oem/oem-api/jwt-direct-link-configurations.html) endpoints | 60 requests per minute |
| **Legacy roles** | All | All [Legacy roles](/en/oem/oem-api/roles.html) endpoints | 60 requests per minute |
| **Lookup tables** | GET | List rows: [/api/managed\_users/:managed\_user\_id /lookup\_tables/:lookup\_table\_id/rows](/en/oem/oem-api/lookup-tables#list-rows) | 1,000 requests per minute |
| **Lookup tables** | All | All other [Lookup tables](/en/oem/oem-api/lookup-tables.html) endpoints | 60 requests per minute |
| **Manage customers** | POST | Create customer: [/api/managed\_users](/en/oem/oem-api/managed-users.html#create-customer-account) | 1,000 requests per minute |
| **Manage customers** | DELETE | Remove member from customer workspace: [/api/managed\_users/:id/members /:member\_id](/en/oem/oem-api/managed-users.html#remove-member-from-customer-account) | 1,000 requests per minute |
| **Manage customers** | POST | Provision environments: [/api/managed\_users/:id/environments](/en/oem/oem-api/managed-users.html#provision-environments) | 1,000 requests per minute |
| **Manage customers** | All | All [Usage](/en/oem/oem-api/managed-users.html#get-usage-v2) endpoints | 1,000 requests per minute |
| **Manage customers** | All | All other [Members](/en/oem/oem-api/managed-users.html#get-list-of-customer-account-members) endpoints | 60 requests per minute |
| **Manage customers** | All | All other [Manage customers](/en/oem/oem-api/managed-users.html) endpoints | 60 requests per minute |
| **On-prem** | All | All [On-prem](/en/oem/oem-api/on-prem.html) endpoints | 60 requests per minute |
| **Picklists** | All | All [Picklists](/en/oem/oem-api/picklists.html) endpoints | 60 requests per minute |
| **Project grants** | All[](/en/oem/oem-api/project-grants.html) | All [Project grants](/en/oem/oem-api/project-grants.html) endpoints | 60 requests per minute |
| **Project roles** | All[](/en/oem/oem-api/project-roles.html) | All [Project roles](/en/oem/oem-api/project-roles.html) endpoints | 10 requests per second |
| **Projects** | GET | List projects: [/api/managed\_users/:managed\_user\_id /projects](/en/oem/oem-api/project-properties.html#list-projects) | 1,000 requests per minute |
| **Projects** | All | All [Deployments](/en/oem/oem-api/project-properties.html#list-deployments) endpoints | 60 requests per minute |
| **Projects** | All | All other [Projects](/en/oem/oem-api/project-properties.html) endpoints | 60 requests per minute |
| **Recipes** | GET | List recipes in a customer workspace: [/api/managed\_users/:id/recipes](/en/oem/oem-api/recipes.html#list-recipes-in-a-customer-account) | 2,000 requests per minute |
| **Recipes** | GET | Get recipe in a customer workspace: [/api/managed\_users/:id/recipes /:recipe\_id](/en/oem/oem-api/recipes.html#get-recipe-in-a-customer-account) | 2,000 requests per minute |
| **Recipes** | All | All [Recipe versions](/en/oem/oem-api/recipes.html#get-recipe-versions-in-a-customer-workspace) endpoints | 60 requests per minute |
| **Recipes** | All | All other [Recipes](/en/oem/oem-api/recipes.html) endpoints | 1,000 requests per minute |
| **Recipe lifecycle management** | POST | Import package into a customer workspace: [/api/managed\_users/:managed\_user\_id /imports](/en/oem/oem-api/recipe-lifecycle-management.html#package-import) | 1,000 requests per minute |
| **Recipe lifecycle management** | GET | Get status of package import: [/api/managed\_users/:managed\_user\_id /imports/:package\_id](/en/oem/oem-api/recipe-lifecycle-management.html#get-package-status) | 1,000 requests per minute |
| **Recipe lifecycle management** | All | All other [Recipe lifecycle management](/en/oem/oem-api/recipe-lifecycle-management.html) endpoints | 60 requests per minute |
| **Role migration** | All[](/en/oem/oem-api/role-migration.html) | All [Role migration](/en/oem/oem-api/role-migration.html) endpoints | 60 requests per minute |
| **Tag assignments** | All | All [Tag assignments](/en/oem/oem-api/tag-assignments.html) endpoints | 1,000 requests per minute |
| **Test Automation** | All | All [Test Automation](/en/oem/oem-api/test-automation.html) endpoints | 60 requests per minute |

> **FURTHER READING**
> 
> Refer to the [Platform quotas](/en/limits) documentation for more information about Workato quotas.

---
