---
url: 'https://docs.workato.com/en/workato-api/cross-workspace-sharing.md'
description: >-
  Reference for the Workato cross-workspace sharing API to create, list, update,
  and revoke cross-workspace grants, review incoming grants, and discover
  grantable environments.
---

# Developer API - Cross-workspace sharing

The following endpoints enable you to manage [cross-workspace grants](/en/cross-share-streams) programmatically.

Grants are two-sided. Outgoing grants are the grants your workspace shares out, and they support full management operations. Incoming grants are the grants other workspaces share with your workspace, and they are read-only. The source and target environment endpoints help a client discover valid environments before it creates a grant. Every call is scoped to the caller's own workspace.

> **REQUIRED PRIVILEGES**
> 
> Your API client's role must include the relevant privileges under **Admin > Cross-workspace sharing** in the API client role editor. The **Cross-workspace sharing grants** feature contains the outgoing grant and environment discovery privileges. The **Cross-workspace sharing incoming grants** feature contains the **List incoming grants** and **View incoming grant** privileges.

## Rate limits

Cross-workspace sharing developer API resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| Read | All read [Cross-workspace sharing](/en/workato-api/cross-workspace-sharing.html) endpoints | 600 requests per minute |
| Write | All write [Cross-workspace sharing](/en/workato-api/cross-workspace-sharing.html) endpoints | 60 requests per minute |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/cross\_workspace/grants](/en/workato-api/cross-workspace-sharing#list-outgoing-grants) | Retrieve a list of outgoing grants. |
| GET | [/api/cross\_workspace/grants/:handle](/en/workato-api/cross-workspace-sharing#get-an-outgoing-grant) | Get an outgoing grant by handle. |
| POST | [/api/cross\_workspace/grants](/en/workato-api/cross-workspace-sharing#create-a-grant) | Create a grant. |
| PUT | [/api/cross\_workspace/grants/:handle](/en/workato-api/cross-workspace-sharing#update-a-grant) | Update a grant. |
| DELETE | [/api/cross\_workspace/grants/:handle](/en/workato-api/cross-workspace-sharing#revoke-a-grant) | Revoke a grant. |
| GET | [/api/cross\_workspace/incoming\_grants](/en/workato-api/cross-workspace-sharing#list-incoming-grants) | Retrieve a list of incoming grants. |
| GET | [/api/cross\_workspace/incoming\_grants/:handle](/en/workato-api/cross-workspace-sharing#get-an-incoming-grant) | Get an incoming grant by handle. |
| GET | [/api/cross\_workspace/source\_environments](/en/workato-api/cross-workspace-sharing#list-source-environments) | Retrieve environments that can act as a grant source. |
| GET | [/api/cross\_workspace/target\_environments](/en/workato-api/cross-workspace-sharing#list-target-environments) | Retrieve environments grantable from a given source. |

## How the API references environments and assets

The cross-workspace sharing API uses the following identifiers and conventions:

- Grants
  
- Each grant is identified by a unique string `handle`, such as `cwsgr-2f8h1k-a3x9qz-1`. A single grant can share from multiple source environments at once. The `environments` array carries one entry for each source environment.
  
- Environments
  
- Environments are referenced by their internal `id`. A grant shares from a `source_environment_id` in your own workspace to one or more `target_environment_ids`. Targets must be same-type siblings of the source, so a `prod` source shares to `prod` targets, in the same Automation HQ organization and the same data center. Use the [List source environments](#list-source-environments) and [List target environments](#list-target-environments) endpoints to discover valid IDs before you create a grant.
  
- Assets
  
- Assets are referenced by `id` and `type`. Cross-workspace sharing supports Event streams topics, so `type` is `Topic`. The asset `id` is the topic's ID, the same identifier the [Event streams API](/en/workato-api/event-streams) uses. This API represents the asset `id` as a string even though the Event streams topic ID is an integer, because cross-workspace sharing is designed to accommodate future asset types whose IDs aren't numbers. Quote the ID when you use it here.
  
- Access levels
  
- The `access_levels` array grants one or both of `read` and `write` for an asset. These map to the **Subscribe** and **Publish** access levels shown in the cross-workspace sharing UI. Both outgoing and incoming grants represent access levels as an array.
  

## List outgoing grants

Retrieves a list of grants owned by the caller's workspace, with optional name filtering and sorting.

```shell
GET /api/cross_workspace/grants
```

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Filters grants by a partial, case-insensitive match on `name`. |
| sort | **string** _optional_ | Defines how to sort the results. Options include `name`, `-name`, `updated_at`, and `-updated_at`. A `-` prefix sorts descending. Set to `updated_at` descending by default. |
| page\[number\] | **integer** _optional_ | The page number to retrieve. The default value is `1`. |
| page\[size\] | **integer** _optional_ | The number of grants per page to retrieve. The default and maximum value is `100`. |

### Sample request

This request retrieves outgoing grants that match the name `Orders`, sorted by name.

```shell
curl  -g -X GET "https://app.workato.com/api/cross_workspace/grants?name=Orders&sort=name&page[number]=1&page[size]=100" \
      -H 'Authorization: Bearer <api_token>'
```

### Response

```json
{
    "data": [
        {
            "handle": "cwsgr-2f8h1k-a3x9qz-1",
            "name": "Orders topic to EU and APAC",
            "description": "Share prod orders stream",
            "created_by": { "name": "Sasha Patel" },
            "created_at": "2026-06-30T12:00:00.000Z",
            "updated_at": "2026-06-30T12:00:00.000Z",
            "environments": [
                {
                    "source_environment_id": 123,
                    "source_environment_type": "prod",
                    "target_environments": [
                        { "id": 456, "type": "prod", "workspace_id": 17293, "workspace_name": "Acme EU" }
                    ],
                    "assets": [
                        { "id": "48213", "name": "orders", "type": "Topic", "access_levels": ["read", "write"] }
                    ]
                }
            ]
        }
    ],
    "total": 42,
    "page": { "number": 1, "size": 100 }
}
```

## Get an outgoing grant

Retrieves a single grant owned by the caller's workspace, resolved by handle.

```shell
GET /api/cross_workspace/grants/:handle
```

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| handle | **string** _required_ | The grant's handle. |

### Sample request

This request retrieves the grant with the handle `cwsgr-2f8h1k-a3x9qz-1`.

```shell
curl  -X GET "https://app.workato.com/api/cross_workspace/grants/cwsgr-2f8h1k-a3x9qz-1" \
      -H 'Authorization: Bearer <api_token>'
```

### Response

```json
{
    "data": {
        "handle": "cwsgr-2f8h1k-a3x9qz-1",
        "name": "Orders topic to EU and APAC",
        "description": "Share prod orders stream",
        "created_by": { "name": "Sasha Patel" },
        "created_at": "2026-06-30T12:00:00.000Z",
        "updated_at": "2026-06-30T12:00:00.000Z",
        "environments": [
            {
                "source_environment_id": 123,
                "source_environment_type": "prod",
                "target_environments": [
                    { "id": 456, "type": "prod", "workspace_id": 17293, "workspace_name": "Acme EU" }
                ],
                "assets": [
                    { "id": "48213", "name": "orders", "type": "Topic", "access_levels": ["read", "write"] }
                ]
            }
        ]
    }
}
```

A grant that isn't owned by the caller's workspace returns `404`.

## Create a grant

Creates a grant in the caller's workspace.

```shell
POST /api/cross_workspace/grants
```

### Body parameters

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | The grant's name. |
| description | **string** _optional_ | The grant's description. |
| environments | **array** _optional_ | One entry for each source environment you share from. Omit `environments` to create an empty grant that you populate later with an update. |
| environments\[source\_environment\_id\] | **integer** _required_ | The source environment's ID. Must belong to the caller's workspace. |
| environments\[target\_environment\_ids\] | **array** _optional_ | The IDs of the target environments to share to. Must be same-type siblings of the source, in the same Automation HQ organization. |
| environments\[assets\] | **array** _optional_ | The assets shared from this source environment. |
| environments\[assets\]\[id\] | **string** _required_ | The asset's ID, provided as a string. For Event streams topics, use the topic's ID. |
| environments\[assets\]\[type\] | **string** _required_ | The asset's type. Accepts `Topic`. |
| environments\[assets\]\[access\_levels\] | **array** _required_ | The access levels granted for the asset. One or both of `read` and `write`. |

### Sample request

This request creates a grant that shares the `orders` topic from source environment `123` with two target environments.

```shell
curl  -X POST "https://app.workato.com/api/cross_workspace/grants" \
      -H 'Authorization: Bearer <api_token>' \
      -H "Content-Type: application/json" \
      -d '{
            "name": "Orders topic to EU and APAC",
            "description": "Share prod orders stream",
            "environments": [
                {
                    "source_environment_id": 123,
                    "target_environment_ids": [456, 789],
                    "assets": [
                        { "id": "48213", "type": "Topic", "access_levels": ["read", "write"] }
                    ]
                }
            ]
         }'
```

### Response

```json
{
    "data": {
        "handle": "cwsgr-2f8h1k-a3x9qz-1",
        "name": "Orders topic to EU and APAC",
        "description": "Share prod orders stream",
        "created_by": { "name": "Sasha Patel" },
        "created_at": "2026-06-30T12:00:00.000Z",
        "updated_at": "2026-06-30T12:00:00.000Z",
        "environments": [
            {
                "source_environment_id": 123,
                "source_environment_type": "prod",
                "target_environments": [
                    { "id": 456, "type": "prod", "workspace_id": 17293, "workspace_name": "Acme EU" },
                    { "id": 789, "type": "prod", "workspace_id": 40021, "workspace_name": "Acme APAC" }
                ],
                "assets": [
                    { "id": "48213", "name": "orders", "type": "Topic", "access_levels": ["read", "write"] }
                ]
            }
        ]
    }
}
```

This endpoint returns `201` on success. It returns `400` if the body fails validation, including a `target_environment_id` equal to its own source, a target of a different environment type or outside the source's Automation HQ organization, or an asset not owned by its source environment. Each rule reports its own message, so a request that fails more than one rule receives one message for each failing rule.

## Update a grant

Updates a grant owned by the caller's workspace. The request accepts the same body shape as [Create a grant](#create-a-grant), applied as a partial update for each source environment. Each `environments` entry is a partial slice keyed by `source_environment_id`. An omitted `target_environment_ids` or `assets` leaves that side unchanged, and an explicit empty array clears it.

```shell
PUT /api/cross_workspace/grants/:handle
```

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| handle | **string** _required_ | The grant's handle. |

### Body parameters

The request accepts the same fields as the [Create a grant](#create-a-grant) endpoint and applies them as a partial update to each source environment. The `name` field is optional on update. Omit it to leave the grant's name unchanged.

### Sample request

This request updates the grant with the handle `cwsgr-2f8h1k-a3x9qz-1` to share source environment `123` with a single target environment.

```shell
curl  -X PUT "https://app.workato.com/api/cross_workspace/grants/cwsgr-2f8h1k-a3x9qz-1" \
      -H 'Authorization: Bearer <api_token>' \
      -H "Content-Type: application/json" \
      -d '{
            "name": "Orders topic to EU only",
            "environments": [
                { "source_environment_id": 123, "target_environment_ids": [456] }
            ]
         }'
```

### Response

```json
{
    "data": {
        "handle": "cwsgr-2f8h1k-a3x9qz-1",
        "name": "Orders topic to EU only",
        "description": "Share prod orders stream",
        "created_by": { "name": "Sasha Patel" },
        "created_at": "2026-06-30T12:00:00.000Z",
        "updated_at": "2026-07-21T09:10:00.000Z",
        "environments": [
            {
                "source_environment_id": 123,
                "source_environment_type": "prod",
                "target_environments": [
                    { "id": 456, "type": "prod", "workspace_id": 17293, "workspace_name": "Acme EU" }
                ],
                "assets": [
                    { "id": "48213", "name": "orders", "type": "Topic", "access_levels": ["read", "write"] }
                ]
            }
        ]
    }
}
```

This endpoint returns `200` on success. It returns `404` if the handle isn't owned by the caller's workspace, and `400` on validation failure.

## Revoke a grant

Soft-deletes a grant owned by the caller's workspace.

```shell
DELETE /api/cross_workspace/grants/:handle
```

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| handle | **string** _required_ | The grant's handle. |

### Sample request

This request revokes the grant with the handle `cwsgr-2f8h1k-a3x9qz-1`.

```shell
curl  -X DELETE "https://app.workato.com/api/cross_workspace/grants/cwsgr-2f8h1k-a3x9qz-1" \
      -H 'Authorization: Bearer <api_token>'
```

### Response

This endpoint returns `204 No Content` with an empty body on success. It returns `404` if the handle isn't owned by the caller's workspace, and `400` if the deletion fails.

## List incoming grants

Retrieves a list of grants that target the caller's workspace. The list view is lightweight. Each `source_environments` entry carries a `has_assets` boolean instead of the full asset list. Use the [Get an incoming grant](#get-an-incoming-grant) endpoint to retrieve the full asset list for a grant.

```shell
GET /api/cross_workspace/incoming_grants
```

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page\[number\] | **integer** _optional_ | The page number to retrieve. The default value is `1`. |
| page\[size\] | **integer** _optional_ | The number of grants per page to retrieve. The default and maximum value is `100`. |

### Sample request

This request retrieves the grants that target your workspace.

```shell
curl  -g -X GET "https://app.workato.com/api/cross_workspace/incoming_grants?page[number]=1&page[size]=100" \
      -H 'Authorization: Bearer <api_token>'
```

### Response

```json
{
    "data": [
        {
            "handle": "cwsgr-2f8h1k-a3x9qz-1",
            "name": "Orders topic to EU and APAC",
            "description": "Share prod orders stream",
            "created_at": "2026-06-30T12:00:00.000Z",
            "updated_at": "2026-06-30T12:00:00.000Z",
            "source_workspace": { "id": 8842, "name": "Acme Global" },
            "source_environments": [
                { "id": 123, "type": "prod", "has_assets": true }
            ]
        }
    ],
    "total": 3,
    "page": { "number": 1, "size": 100 }
}
```

## Get an incoming grant

Retrieves a single grant that targets the caller's workspace. The single-grant view lists the shared `assets` for each source environment, including their `access_levels`.

```shell
GET /api/cross_workspace/incoming_grants/:handle
```

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| handle | **string** _required_ | The grant's handle. |

### Sample request

This request retrieves the incoming grant with the handle `cwsgr-2f8h1k-a3x9qz-1`.

```shell
curl  -X GET "https://app.workato.com/api/cross_workspace/incoming_grants/cwsgr-2f8h1k-a3x9qz-1" \
      -H 'Authorization: Bearer <api_token>'
```

### Response

```json
{
    "data": {
        "handle": "cwsgr-2f8h1k-a3x9qz-1",
        "name": "Orders topic to EU and APAC",
        "description": "Share prod orders stream",
        "created_at": "2026-06-30T12:00:00.000Z",
        "updated_at": "2026-06-30T12:00:00.000Z",
        "source_workspace": { "id": 8842, "name": "Acme Global" },
        "source_environments": [
            {
                "id": 123,
                "type": "prod",
                "assets": [
                    { "id": "48213", "name": "orders", "type": "Topic", "access_levels": ["read"] }
                ]
            }
        ]
    }
}
```

A handle that doesn't target the caller's workspace returns `404`.

## List source environments

Retrieves the caller workspace's environments that can act as a grant source.

```shell
GET /api/cross_workspace/source_environments
```

### Sample request

This request retrieves the environments that can act as a grant source.

```shell
curl  -X GET "https://app.workato.com/api/cross_workspace/source_environments" \
      -H 'Authorization: Bearer <api_token>'
```

### Response

```json
{
    "data": [
        { "id": 123, "type": "prod", "name": "Acme Global (prod)" },
        { "id": 124, "type": "test", "name": "Acme Global (test)" }
    ]
}
```

## List target environments

Retrieves the sibling environments a given source environment can grant to. Targets are in the same Automation HQ organization and the same data center, and share the same environment type as the source.

```shell
GET /api/cross_workspace/target_environments
```

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| source\_environment\_id | **integer** _required_ | The source environment's ID. Must belong to the caller's workspace. |

### Sample request

This request retrieves the environments grantable from source environment `123`.

```shell
curl  -X GET "https://app.workato.com/api/cross_workspace/target_environments?source_environment_id=123" \
      -H 'Authorization: Bearer <api_token>'
```

### Response

```json
{
    "data": [
        { "id": 456, "type": "prod", "workspace_id": 17293, "workspace_name": "Acme EU" },
        { "id": 789, "type": "prod", "workspace_id": 40021, "workspace_name": "Acme APAC" }
    ]
}
```

This endpoint returns `400` if `source_environment_id` is omitted, and `404` if it doesn't belong to the caller's workspace.

---
