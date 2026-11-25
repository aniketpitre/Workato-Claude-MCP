---
url: 'https://docs.workato.com/en/workato-api/insights-catalog.md'
description: >-
  Insights table descriptions, row grain, join keys, and filter values for the
  Workato Developer API and Embedded API.
---

# Insights data catalog

Use this reference to choose and join tables, and interpret query results. Refer to the [Developer API](/en/workato-api/insights) or [Embedded API](/en/oem/oem-api/insights) Insights pages for authentication, request formats, and query limits.

## Discover the schema for your token

Complete the following steps to discover the tables and columns your API client can query:

1. Call List Insights schema tables on the [Developer API](/en/workato-api/insights#list-insights-schema-tables) or [Embedded API](/en/oem/oem-api/insights#list-insights-schema-tables-in-a-customer-workspace) to discover available catalogs and tables. Use `?catalog=workato_db` or `?catalog=lcap` to discover those tables.
   
2. Call Get Insights table columns on the [Developer API](/en/workato-api/insights#get-insights-table-columns) or [Embedded API](/en/oem/oem-api/insights#get-insights-table-columns-in-a-customer-workspace) with fully qualified names, such as `workato_data.public.recipes`. Check that the columns used in your query are present. The endpoint accepts up to 20 names per request.
   
3. Use the names returned by discovery in Execute Insights SQL query on the [Developer API](/en/workato-api/insights#execute-insights-sql-query) or [Embedded API](/en/oem/oem-api/insights#execute-an-insights-sql-query-in-a-customer-workspace) and apply a time window before joining or aggregating event data. Use a left join when every source row must remain in the result.
   

Tables and columns depend on enabled features and API client access. Use the exact case shown for string filter values. Example values can vary by workspace. Your billing contract determines the available usage metrics and their columns, so usage schemas can differ between workspaces. A table listed here may be unavailable to your token.

## Workspace metadata

### workato\_data.public.environments

Environment metadata, including its type and workspace.

| Column | Type | Notes |
| --- | --- | --- |
| `id` | `BIGINT` |  |
| `name` | `VARCHAR` |  |
| `type` | `VARCHAR` | Case-sensitive codes: `dev` (Development), `test` (Test), `prod` (Production). |
| `workspace_id` | `BIGINT` |  |
| `workspace_name` | `VARCHAR` |  |
| `created_at` | `TIMESTAMP` |  |
| `deleted_at` | `TIMESTAMP` |  |

**Relationships**

`workspace_id` groups environments belonging to the same workspace. Joining another table on workspace ID alone can match several environments. Historical results can include deleted environments.

### workato\_data.public.projects

Project metadata used to label recipe and usage reports.

| Column | Type |
| --- | --- |
| `id` | `BIGINT` |
| `name` | `VARCHAR` |
| `created_at` | `TIMESTAMP` |
| `updated_at` | `TIMESTAMP` |
| `environment_id` | `BIGINT` |

**Relationships**

The following joins are many-to-one:

- `environment_id` → `workato_data.public.environments`.`id`

### workato\_data.public.folders

Folder metadata and project membership.

| Column | Type |
| --- | --- |
| `id` | `BIGINT` |
| `project_id` | `BIGINT` |
| `name` | `VARCHAR` |
| `path` | `VARCHAR` |

**Relationships**

The following joins are many-to-one:

- `project_id` → `workato_data.public.projects`.`id`

### workato\_data.public.recipes

Recipe inventory, including activity status, type, tags, and applications.

| Column | Type | Notes |
| --- | --- | --- |
| `id` | `BIGINT` |  |
| `name` | `VARCHAR` |  |
| `project_id` | `BIGINT` |  |
| `folder_id` | `BIGINT` |  |
| `environment_id` | `BIGINT` |  |
| `is_active` | `BOOLEAN` |  |
| `recipe_type` | `VARCHAR` | Case-sensitive examples: `API Endpoint`, `App`, `Function`, `Workato Agent`. |
| `created_at` | `TIMESTAMP` |  |
| `updated_at` | `TIMESTAMP` |  |
| `tags` | `ARRAY<VARCHAR>` |  |
| `applications` | `ARRAY<VARCHAR>` |  |
| `trigger_application` | `VARCHAR` |  |

**Relationships**

The following joins are many-to-one:

- `project_id` → `workato_data.public.projects`.`id`
- `folder_id` → `workato_data.public.folders`.`id`
- `environment_id` → `workato_data.public.environments`.`id`

### workato\_data.public.connections

Connection inventory and associated folders.

| Column | Type |
| --- | --- |
| `id` | `BIGINT` |
| `folder_id` | `BIGINT` |
| `name` | `VARCHAR` |
| `provider` | `VARCHAR` |
| `type` | `VARCHAR` |
| `status` | `VARCHAR` |

**Relationships**

The following joins are many-to-one:

- `folder_id` → `workato_data.public.folders`.`id`

### workato\_data.public.recipe\_connections\_mapping

Associations between recipes and the connections they reference.

| Column | Type |
| --- | --- |
| `recipe_id` | `BIGINT` |
| `connection_id` | `BIGINT` |

**Relationships**

The following joins are many-to-one:

- `recipe_id` → `workato_data.public.recipes`.`id`
- `connection_id` → `workato_data.public.connections`.`id`

Recipes and connections are many-to-many through this mapping.

## Users and groups

End-user and group data depends on what is available in the workspace.

### users.public.collaborators

Workato workspace collaborators.

| Column | Type |
| --- | --- |
| `id` | `BIGINT` |
| `name` | `VARCHAR` |
| `email` | `VARCHAR` |

**Relationships**

See the tables that reference this table for join keys and cardinality.

### users.public.end\_users

End-user identities used by embedded or authenticated experiences.

| Column | Type |
| --- | --- |
| `id` | `VARCHAR` |
| `email` | `VARCHAR` |
| `name` | `VARCHAR` |

**Relationships**

See the tables that reference this table for join keys and cardinality.

### users.public.end\_user\_groups

Named end-user groups and their environments.

| Column | Type |
| --- | --- |
| `id` | `VARCHAR` |
| `name` | `VARCHAR` |
| `environment_id` | `BIGINT` |

**Relationships**

The following joins are many-to-one:

- `environment_id` → `workato_data.public.environments`.`id`

### users.public.end\_user\_groups\_mapping

Membership of end users in end-user groups.

| Column | Type |
| --- | --- |
| `end_user_id` | `VARCHAR` |
| `end_user_group_id` | `VARCHAR` |
| `environment_id` | `BIGINT` |

**Relationships**

The following joins are many-to-one:

- `end_user_id` → `users.public.end_users`.`id`
- `end_user_group_id` → `users.public.end_user_groups`.`id`
- `environment_id` → `workato_data.public.environments`.`id`

End users and groups are many-to-many through this mapping. Keep joins within the same workspace scope. A membership may lack a visible matching group or user.

## Usage and billing

**Billing contract.** Your billing contract determines the available metrics and their columns. Check the schema endpoint on the [Developer API](/en/workato-api/insights#get-insights-table-columns) or [Embedded API](/en/oem/oem-api/insights#get-insights-table-columns-in-a-customer-workspace) before querying a meter. A missing column or source is distinct from recorded zero consumption.

**Multiple workspaces.** Whether usage and billing data aggregates across a parent workspace and its child workspaces depends on which workspace's API client token you query with. Refer to [Insights in Automation HQ and Embedded](/en/insights/multiple-workspaces) to learn which data aggregates and which stays scoped to the current workspace.

### usage.public.billing\_periods

Billing period boundaries, trial status, and the credit limit shared across a workspace's environments. Only current and future billing periods are returned, never past ones.

An Automation HQ admin workspace token includes the Automation HQ workspace and all its managed workspaces. An Embedded admin workspace token includes the admin workspace and all its customer workspaces. A standalone or child workspace token only returns its own workspace, with all of that workspace's billing periods.

| Column | Type | Notes |
| --- | --- | --- |
| `id` | `VARCHAR` |  |
| `starts_at` | `TIMESTAMP` |  |
| `ends_at` | `TIMESTAMP` |  |
| `created_at` | `TIMESTAMP` |  |
| `updated_at` | `TIMESTAMP` |  |
| `is_current` | `BOOLEAN` |  |
| `workspace_id` | `BIGINT` |  |
| `credit_limit` | `BIGINT` | For customers on task-based pricing, this column represents the task limit. |
| `is_trial` | `BOOLEAN` |  |

**Relationships**

`workspace_id` to `workato_data.public.environments.workspace_id` is a shared grouping value. A direct join can multiply periods by environments. Pair a workspace match with the relevant time window when attributing usage to a billing period.

### usage.public.usage\_by\_plan

Metered consumption aggregated by time interval, environment, and available asset and usage dimensions. There isn't a unique key.

An Embedded admin workspace token aggregates this across the admin workspace and its customer workspaces. An Automation HQ admin workspace token aggregates it across managed workspaces only when `insights.child_aggregation` is enabled for that workspace. Otherwise, it returns only the Automation HQ workspace's own data.

| Column | Type | Notes |
| --- | --- | --- |
| `environment_id` | `BIGINT` |  |
| `recipe_id` | `BIGINT` | May be empty or unmatched. |
| `api_collection_id` | `BIGINT` |  |
| `api_endpoint_id` | `BIGINT` |  |
| `interval_start` | `TIMESTAMP` | Start of the usage interval. All usage is aggregated to PST midnight. |
| `tasks` | `DOUBLE` | Plan-dependent. |
| `usage_type` | `VARCHAR` | Case-sensitive examples: `TASKS`, `MCP_TOOL_CALLS`, `API_CALLS`, `GENIE_RUNS`. Values depend on your plan and can differ from the corresponding metric column names. |
| `api_sub_feature` | `VARCHAR` |  |
| `api_calls` | `BIGINT` |  |
| `idp_pages_processed` | `BIGINT` |  |
| `rows_consumed` | `BIGINT` |  |
| `events_processed` | `BIGINT` |  |
| `agent_actions` | `BIGINT` |  |
| `credits` | `DOUBLE` | Plan-dependent. |
| `business_actions` | `BIGINT` | Plan-dependent. |
| `mcp_tool_calls` | `BIGINT` | Plan-dependent. |

**Relationships**

The following joins are many-to-one:

- `environment_id` → `workato_data.public.environments`.`id`
- `recipe_id` → `workato_data.public.recipes`.`id`
- `api_collection_id` → `api_platform.public.api_collections`.`id`
- `api_endpoint_id` → `api_platform.public.api_endpoints`.`id`

Asset IDs can be empty or unmatched. Keep unmatched rows in a separate bucket when totaling usage. Avoid joining usage to individual job rows when summing credits.

## Job history

### job\_history\_all.public.job\_history\_all

Recipe job executions, including timing, success indicators, and available error details.

| Column | Type | Notes |
| --- | --- | --- |
| `job_handle` | `VARCHAR` |  |
| `completed_at` | `TIMESTAMP` |  |
| `recipe_id` | `BIGINT` |  |
| `environment_id` | `BIGINT` |  |
| `started_at` | `TIMESTAMP` |  |
| `is_complete_success` | `BOOLEAN` |  |
| `is_test` | `BOOLEAN` |  |
| `error_type` | `VARCHAR` |  |
| `error_message` | `VARCHAR` |  |
| `error_application` | `VARCHAR` |  |
| `duration` | `BIGINT` | Milliseconds. |

**Relationships**

The following joins are many-to-one:

- `recipe_id` → `workato_data.public.recipes`.`id`
- `environment_id` → `workato_data.public.environments`.`id`

For jobs by project or folder, join through the recipe. Recipe metadata can reflect its current assignment.

### job\_history.public.<recipe\_id>

Job records for one recipe, with its available custom job report fields. The following table lists the standard fields. Use `/schema` to discover any recipe-specific fields.

| Column | Type |
| --- | --- |
| `job_handle` | `VARCHAR` |
| `started_at` | `TIMESTAMP` |
| `completed_at` | `TIMESTAMP` |
| `is_complete_success` | `BOOLEAN` |
| `test_job` | `BOOLEAN` |
| `error_type` | `VARCHAR` |
| `error_message` | `VARCHAR` |
| `error_application` | `VARCHAR` |

**Relationships**

The recipe ID is part of the table name. Discover the table by name with `/schema`, and quote the numeric identifier in SQL.

Project access applies. Column names and types can vary by recipe.

## API Platform

Availability depends on your workspace's API Platform configuration and the API client's access.

### api\_platform.public.api\_collections

API collections and their metadata.

| Column | Type |
| --- | --- |
| `id` | `BIGINT` |
| `name` | `VARCHAR` |
| `description` | `VARCHAR` |
| `type` | `VARCHAR` |
| `environment_id` | `BIGINT` |
| `created_at` | `TIMESTAMP` |

**Relationships**

The following joins are many-to-one:

- `environment_id` → `workato_data.public.environments`.`id`

### api\_platform.public.api\_endpoints

API endpoints, including method and path.

| Column | Type |
| --- | --- |
| `id` | `BIGINT` |
| `name` | `VARCHAR` |
| `method` | `VARCHAR` |
| `path` | `VARCHAR` |
| `active` | `BOOLEAN` |
| `environment_id` | `BIGINT` |
| `api_collection_id` | `BIGINT` |
| `created_at` | `TIMESTAMP` |

**Relationships**

The following joins are many-to-one:

- `api_collection_id` → `api_platform.public.api_collections`.`id`
- `environment_id` → `workato_data.public.environments`.`id`

### api\_platform.public.api\_clients

API Platform clients and their policy references.

| Column | Type |
| --- | --- |
| `id` | `BIGINT` |
| `name` | `VARCHAR` |
| `email` | `VARCHAR` |
| `description` | `VARCHAR` |
| `api_policy_id` | `BIGINT` |
| `environment_id` | `BIGINT` |
| `deleted_at` | `TIMESTAMP` |
| `created_at` | `TIMESTAMP` |

**Relationships**

The following joins are many-to-one:

- `api_policy_id` → `api_platform.public.api_policies`.`id`
- `environment_id` → `workato_data.public.environments`.`id`

### api\_platform.public.api\_keys

API key metadata and the collections associated with each key.

| Column | Type |
| --- | --- |
| `id` | `BIGINT` |
| `name` | `VARCHAR` |
| `auth_type` | `VARCHAR` |
| `active` | `BOOLEAN` |
| `api_client_id` | `BIGINT` |
| `api_policy_id` | `BIGINT` |
| `environment_id` | `BIGINT` |
| `api_collection_ids` | `ARRAY<BIGINT>` |
| `deleted_at` | `TIMESTAMP` |
| `created_at` | `TIMESTAMP` |

**Relationships**

The following joins are many-to-one:

- `api_client_id` → `api_platform.public.api_clients`.`id`
- `api_policy_id` → `api_platform.public.api_policies`.`id`
- `environment_id` → `workato_data.public.environments`.`id`

`api_collection_ids` is an array of `api_platform.public.api_collections.id` values. This is a many-to-many relationship. Expand the array with `CROSS JOIN UNNEST` in a CTE or subquery. Join the expanded IDs to collections in the outer query. Each expanded row represents one key-collection association.

### api\_platform.public.api\_policies

API policy metadata such as limits and CORS configuration.

| Column | Type |
| --- | --- |
| `id` | `BIGINT` |
| `name` | `VARCHAR` |
| `rate_limits` | `VARCHAR` |
| `quota` | `VARCHAR` |
| `cors_enabled` | `BOOLEAN` |
| `created_at` | `TIMESTAMP` |

**Relationships**

See the tables that reference this table for join keys and cardinality.

### api\_platform.public.api\_gateway\_events

Recorded API gateway activity and request outcomes. Check request ID repetition before using event row counts as request counts.

| Column | Type |
| --- | --- |
| `created_at_d` | `DATE` |
| `created_at_dt` | `TIMESTAMP` |
| `event_type` | `VARCHAR` |
| `method` | `VARCHAR` |
| `path` | `VARCHAR` |
| `response_code` | `BIGINT` |
| `environment_id` | `BIGINT` |
| `api_collection_id` | `BIGINT` |
| `api_endpoint_id` | `BIGINT` |
| `api_key_id` | `BIGINT` |
| `api_client_id` | `BIGINT` |
| `request_id` | `VARCHAR` |
| `request_time` | `BIGINT` |
| `job_handle` | `VARCHAR` |
| `initial_concurrency` | `BIGINT` |

**Relationships**

The following joins are many-to-one:

- `environment_id` → `workato_data.public.environments`.`id`
- `api_collection_id` → `api_platform.public.api_collections`.`id`
- `api_endpoint_id` → `api_platform.public.api_endpoints`.`id`
- `api_key_id` → `api_platform.public.api_keys`.`id`
- `api_client_id` → `api_platform.public.api_clients`.`id`

`job_handle` can match `job_history_all.public.job_history_all.job_handle` when available. This is a best-effort many-to-one link.

## Enterprise MCP

Available tables depend on the workspace's access to Enterprise MCP data.

### mcp.public.mcp\_servers

Inventory of MCP servers.

| Column | Type |
| --- | --- |
| `id` | `BIGINT` |
| `name` | `VARCHAR` |
| `handle` | `VARCHAR` |
| `asset_type` | `VARCHAR` |
| `is_enabled` | `BOOLEAN` |
| `environment_id` | `BIGINT` |

**Relationships**

The following joins are many-to-one:

- `environment_id` → `workato_data.public.environments`.`id`

### mcp.public.mcp\_tools

Tools exposed by MCP servers, identified by the combination of server ID, tool ID, and tool type.

| Column | Type | Notes |
| --- | --- | --- |
| `mcp_server_id` | `BIGINT` |  |
| `tool_id` | `BIGINT` |  |
| `tool_type` | `VARCHAR` | Case-sensitive examples: `api_endpoint`, `api_proxy`, `function`, `skill`. |
| `tool_name` | `VARCHAR` |  |
| `is_active` | `BOOLEAN` |  |
| `vua_required` | `BOOLEAN` |  |

**Relationships**

The following joins are many-to-one:

- `mcp_server_id` → `mcp.public.mcp_servers`.`id`

`tool_id` can refer to different resources by tool type. For `tool_type = 'api_endpoint'`, it can match `api_platform.public.api_endpoints.id` many-to-one.

### mcp.public.mcp\_gateway\_events

Recorded MCP gateway activity. Use it to investigate traffic and outcomes.

| Column | Type |
| --- | --- |
| `event_time` | `TIMESTAMP` |
| `mcp_server_id` | `VARCHAR` |
| `request_id` | `VARCHAR` |
| `environment_id` | `BIGINT` |
| `method` | `VARCHAR` |
| `event_type` | `VARCHAR` |
| `error_code` | `VARCHAR` |
| `latency_ms` | `BIGINT` |
| `request_size` | `BIGINT` |
| `response_size` | `BIGINT` |
| `end_user_id` | `VARCHAR` |
| `auth_type` | `VARCHAR` |
| `ai_client` | `VARCHAR` |
| `token_name` | `VARCHAR` |
| `tool_name` | `VARCHAR` |
| `job_handle` | `VARCHAR` |

**Relationships**

The following joins are many-to-one:

- `environment_id` → `workato_data.public.environments`.`id`
- `end_user_id` → `users.public.end_users`.`id`
- `mcp_server_id` → `mcp.public.mcp_servers`.`id`

`job_handle` can match `job_history_all.public.job_history_all.job_handle` many-to-one when present. A `tool_name` match is best effort. Include server ID and check for multiple matching tool records before aggregating.

## Data pipelines

Available where the workspace has access to Data Pipelines data.

### data\_orchestration.public.data\_pipelines

Pipeline inventory and its folder and environment metadata.

| Column | Type |
| --- | --- |
| `id` | `BIGINT` |
| `handle` | `VARCHAR` |
| `name` | `VARCHAR` |
| `folder_id` | `BIGINT` |
| `environment_id` | `BIGINT` |
| `is_active` | `BOOLEAN` |
| `created_at` | `TIMESTAMP` |
| `updated_at` | `TIMESTAMP` |
| `deleted_at` | `TIMESTAMP` |

**Relationships**

The following joins are many-to-one:

- `folder_id` → `workato_data.public.folders`.`id`
- `environment_id` → `workato_data.public.environments`.`id`

Pipeline IDs use a separate namespace from recipe IDs.

### data\_orchestration.public.data\_pipeline\_runs\_history\_all

Recorded pipeline object runs, including status, timing, and available row counts.

| Column | Type | Notes |
| --- | --- | --- |
| `run_id` | `VARCHAR` |  |
| `sync_id` | `VARCHAR` | Groups related run records. |
| `object_name` | `VARCHAR` |  |
| `state` | `VARCHAR` |  |
| `run_type` | `VARCHAR` |  |
| `sync_type` | `VARCHAR` |  |
| `sync_is_completed` | `BOOLEAN` |  |
| `pipeline_id` | `VARCHAR` | Data pipeline handle. |
| `started_at` | `TIMESTAMP` |  |
| `completed_at` | `TIMESTAMP` |  |
| `loaded_count` | `BIGINT` |  |
| `updated_count` | `BIGINT` |  |
| `inserted_count` | `BIGINT` |  |

**Relationships**

The following joins are many-to-one:

- `pipeline_id` → `data_orchestration.public.data_pipelines`.`handle`

`pipeline_id` contains the pipeline handle. `sync_id` identifies the sync and can group related run records.

## Audit activity

Each row is one recorded event, not a single current record per actor or asset. This means that the same actor or asset can appear in several rows.

### audit\_log.public.invite\_updates

Invitation-related activity.

| Column | Type |
| --- | --- |
| `event_time` | `TIMESTAMP` |
| `event_type` | `VARCHAR` |
| `environment_id` | `BIGINT` |
| `actor_id` | `BIGINT` |
| `email` | `VARCHAR` |
| `role` | `VARCHAR` |

**Relationships**

The following joins are many-to-one:

- `environment_id` → `workato_data.public.environments`.`id`
- `actor_id` → `users.public.collaborators`.`id`

### audit\_log.public.membership\_updates

Workspace membership activity.

| Column | Type |
| --- | --- |
| `event_time` | `TIMESTAMP` |
| `event_type` | `VARCHAR` |
| `environment_id` | `BIGINT` |
| `actor_id` | `BIGINT` |
| `member_id` | `BIGINT` |

**Relationships**

The following joins are many-to-one:

- `environment_id` → `workato_data.public.environments`.`id`
- `actor_id` → `users.public.collaborators`.`id`
- `member_id` → `users.public.collaborators`.`id`

### audit\_log.public.role\_updates

Role assignment changes.

| Column | Type |
| --- | --- |
| `event_time` | `TIMESTAMP` |
| `event_type` | `VARCHAR` |
| `environment_id` | `BIGINT` |
| `actor_id` | `BIGINT` |
| `member_id` | `BIGINT` |
| `new_role` | `VARCHAR` |
| `previous_role` | `VARCHAR` |

**Relationships**

The following joins are many-to-one:

- `environment_id` → `workato_data.public.environments`.`id`
- `actor_id` → `users.public.collaborators`.`id`
- `member_id` → `users.public.collaborators`.`id`

### audit\_log.public.logins

Recorded login activity.

| Column | Type |
| --- | --- |
| `event_time` | `TIMESTAMP` |
| `event_type` | `VARCHAR` |
| `environment_id` | `BIGINT` |
| `actor_id` | `BIGINT` |

**Relationships**

The following joins are many-to-one:

- `environment_id` → `workato_data.public.environments`.`id`
- `actor_id` → `users.public.collaborators`.`id`

### audit\_log.public.connection\_updates

Recorded connection activity.

| Column | Type |
| --- | --- |
| `event_time` | `TIMESTAMP` |
| `event_type` | `VARCHAR` |
| `environment_id` | `BIGINT` |
| `actor_id` | `BIGINT` |
| `connection_id` | `BIGINT` |

**Relationships**

The following joins are many-to-one:

- `environment_id` → `workato_data.public.environments`.`id`
- `actor_id` → `users.public.collaborators`.`id`
- `connection_id` → `workato_data.public.connections`.`id`

### audit\_log.public.recipe\_updates

Recorded recipe lifecycle and change activity.

| Column | Type |
| --- | --- |
| `event_time` | `TIMESTAMP` |
| `event_type` | `VARCHAR` |
| `environment_id` | `BIGINT` |
| `actor_id` | `BIGINT` |
| `recipe_id` | `BIGINT` |

**Relationships**

The following joins are many-to-one:

- `environment_id` → `workato_data.public.environments`.`id`
- `actor_id` → `users.public.collaborators`.`id`
- `recipe_id` → `workato_data.public.recipes`.`id`

## Data tables and Workflow apps

### workato\_db.public.<table\_uuid>

Rows from a workspace data table.

**Columns.** Use the schema endpoint on the [Developer API](/en/workato-api/insights#get-insights-table-columns) or [Embedded API](/en/oem/oem-api/insights#get-insights-table-columns-in-a-customer-workspace) to discover the columns and types for the selected table.

**Relationships**

Relationships are defined by your data. Use `?catalog=workato_db` to look up the UUID by label. Quote the UUID in SQL.

Project access applies.

### lcap.public.<app\_uuid>

Rows exposed by a Workflow app table. The data represented by each row depends on the app.

**Columns.** Use the schema endpoint on the [Developer API](/en/workato-api/insights#get-insights-table-columns) or [Embedded API](/en/oem/oem-api/insights#get-insights-table-columns-in-a-customer-workspace) to discover the columns and types for the selected table.

**Relationships**

Discover table names with `?catalog=lcap`. Relationships depend on the app.

---
