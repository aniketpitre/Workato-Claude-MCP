---
url: 'https://docs.workato.com/en/oem/oem-api/mcp-servers.md'
description: >-
  Reference for the Embedded API endpoints to create, manage, and configure MCP
  servers, tools, and policies in customer workspaces.
---

# Embedded API - MCP servers

Use these resources to programmatically manage MCP (Model Context Protocol) servers in customer workspaces.

> **TOKEN AND HASHED TOKEN AUTHENTICATION**
> 
> `hashed_token` is the default authentication type for token-based MCP servers. The `token` authentication type is considered _legacy_. Existing servers using `token` continue to work, but new servers use `hashed_token`. Refer to [MCP hashed tokens](#mcp-hashed-tokens) to manage tokens on `hashed_token` servers.

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:managed\_user\_id/mcp\_servers](#list-mcp-servers-in-a-customer-workspace) | List MCP servers in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/mcp\_servers](#create-an-mcp-server-in-a-customer-workspace) | Create an MCP server in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:handle](#get-mcp-server-details-in-a-customer-workspace) | Retrieve MCP server details in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:handle](#update-an-mcp-server-in-a-customer-workspace) | Update an MCP server in a customer workspace. |
| DELETE | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:handle](#delete-an-mcp-server-in-a-customer-workspace) | Delete an MCP server in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:handle/token\_renew](#renew-mcp-server-authentication-token-in-a-customer-workspace) | Renew an MCP server authentication token in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/tokens](#create-a-hashed-token-in-a-customer-workspace) | Create a hashed token in a customer workspace. |
| DELETE | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/tokens/:id](#delete-a-hashed-token-in-a-customer-workspace) | Delete a hashed token in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/tokens/:id/refresh](#refresh-a-hashed-token-in-a-customer-workspace) | Refresh a hashed token in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:handle/assign\_tools](#assign-tools-to-an-mcp-server-in-a-customer-workspace) | Assign tools to an MCP server in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:handle/assign\_user\_groups](#assign-user-groups-to-an-mcp-server-in-a-customer-workspace) | Assign user groups to an MCP server in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:handle/remove\_user\_groups](#remove-user-groups-from-an-mcp-server-in-a-customer-workspace) | Remove user groups from an MCP server in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:handle/update\_folder](#move-mcp-server-to-a-different-folder-in-a-customer-workspace) | Move an MCP server to a different folder in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/server\_policies](#get-server-policy-configuration-in-a-customer-workspace) | Retrieve server policy configuration in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/server\_policies](#update-server-policy-configuration-in-a-customer-workspace) | Update server policy configuration in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/tools](#list-tools-for-an-mcp-server-in-a-customer-workspace) | List tools for an MCP server in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/tools/:id](#update-tool-description-in-a-customer-workspace) | Update tool description in a customer workspace. |
| DELETE | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/tools/:id](#delete-a-tool-in-a-customer-workspace) | Delete a tool in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/user\_groups](#list-identity-provider-user-groups-in-a-customer-workspace) | List identity provider user groups in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/access\_assignments](#list-mcp-access-assignments-in-a-customer-workspace) | List MCP access assignments in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/access\_assignments](#create-an-mcp-access-assignment-in-a-customer-workspace) | Create an MCP access assignment in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/access\_assignments/:id](#get-an-mcp-access-assignment-in-a-customer-workspace) | Retrieve an MCP access assignment in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/access\_assignments/:id](#update-an-mcp-access-assignment-in-a-customer-workspace) | Update an MCP access assignment in a customer workspace. |
| DELETE | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/access\_assignments/:id](#delete-an-mcp-access-assignment-in-a-customer-workspace) | Delete an MCP access assignment in a customer workspace. |

## List MCP servers in a customer workspace

Returns a list of MCP servers in a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| project\_id | **number** _optional_ | Filter by project ID. |
| folder\_id | **number** _optional_ | Filter by folder ID. |
| authentication\_method | **string** _optional_ | Filter by authentication method. Accepted values: `hashed_token`, `token` (legacy), `workato_idp`. |
| page | **number** _optional_ | Page number. Defaults to 1. |
| per\_page | **number** _optional_ | Number of items per page. Maximum is 50. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers?folder_id=:folder_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

```json
{
    "data": [
        {
            "id": 1001,
            "name": "Sales Tools MCP Server",
            "description": "Provides CRM and deal management tools for AI clients",
            "folder_id": 27180380,
            "project_id": 13595198,
            "authentication_method": "hashed_token",
            "tools_count": 5
        },
        {
            "id": 1002,
            "name": "HR Automation Server",
            "description": "HR onboarding and employee management tools",
            "folder_id": 27180380,
            "project_id": 13595198,
            "authentication_method": "workato_idp",
            "tools_count": 3
        }
    ],
    "count": 2,
    "page": 1,
    "per_page": 50
}
```

## Create an MCP server in a customer workspace

Creates a new MCP server in a customer workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Server name. |
| folder\_id | **number** _required_ | Folder ID for the MCP server. |
| description | **string** _optional_ | Server description. |
| asset\_id | **number** _optional_ | API collection ID. Omit to create a project asset server. |
| tools | **array of objects** _optional_ | Tools to assign to the server at creation. Each object requires `trigger_application` (string) and `id` (string). `id` is a number when using `workato_recipe_function` and `workato_api_platform` tools. `id` is a string handle when using `workato_genie` tools. |

> **HASHED TOKEN AS DEFAULT AUTH TYPE**
> 
> MCP servers use `hashed_token` as the default `auth_type` unless you specify a different authentication type. Use the [MCP hashed tokens](#mcp-hashed-tokens) endpoints to manage tokens on a `hashed_token` server.

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "description": ":description",
            "folder_id": :folder_id,
            "tools": [
              {
                "trigger_application": ":trigger_application",
                "id": ":id"
              }
            ]
          }'
```

</api-code>

#### Sample response

```json
{
    "data": {
        "id": 1001,
        "name": "Sales Tools MCP Server",
        "description": "Provides CRM and deal management tools for AI clients",
        "asset_type": "api_collection",
        "logo_url": "https://www.workato.com/images/mcp-server-logo.png",
        "tools_count": 1,
        "mcp_url": "https://www.workato.com/mcp/servers/sales-tools-mcp-server?token=abc123xyz",
        "auth_type": "hashed_token",
        "idp_user_group_ids": [],
        "api_collection": null,
        "created_at": "2025-10-15T13:41:05.207-07:00",
        "updated_at": "2025-10-15T13:41:05.207-07:00"
    }
}
```

## Get MCP server details in a customer workspace

Retrieves details for a specific MCP server in a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:handle
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| handle | **string** _required_ | MCP server handle. You can find the `mcp_server_handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:handle' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

```json
{
    "data": {
        "id": 1001,
        "name": "Sales Tools MCP Server",
        "description": "Provides CRM and deal management tools for AI clients",
        "asset_type": "api_collection",
        "logo_url": "https://www.workato.com/images/mcp-server-logo.png",
        "tools_count": 5,
        "mcp_url": "https://www.workato.com/mcp/servers/sales-tools-mcp-server?token=abc123xyz",
        "auth_type": "hashed_token",
        "idp_user_group_ids": [],
        "api_collection": null,
        "created_at": "2025-10-15T13:41:05.207-07:00",
        "updated_at": "2025-10-16T09:22:11.100-07:00"
    }
}
```

## Update an MCP server in a customer workspace

Updates an existing MCP server in a customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:handle
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| handle | **string** _required_ | MCP server handle. You can find the `mcp_server_handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Server name. |
| description | **string** _optional_ | Server description. |
| auth\_type | **string** _optional_ | Authentication type. Accepted values: `hashed_token`, `token` (legacy), `workato_idp`. |
| idp\_user\_group\_ids | **array of strings** _optional_ | Identity provider user group IDs that have access to the server. Only applicable when `auth_type` is `workato_idp`. |
| folder\_id | **number** _optional_ | Target folder ID to move the server. |

#### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:handle' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "description": ":description",
            "auth_type": ":auth_type"
          }'
```

</api-code>

#### Sample response

```json
{
    "data": {
        "id": 1001,
        "name": "Sales & CRM Tools MCP Server",
        "description": "Provides CRM, deal management, and pipeline tools for AI clients",
        "asset_type": "api_collection",
        "logo_url": "https://www.workato.com/images/mcp-server-logo.png",
        "tools_count": 5,
        "mcp_url": "https://www.workato.com/mcp/servers/sales-tools-mcp-server?token=abc123xyz",
        "auth_type": "hashed_token",
        "idp_user_group_ids": [],
        "api_collection": null,
        "created_at": "2025-10-15T13:41:05.207-07:00",
        "updated_at": "2025-10-17T11:05:33.812-07:00"
    }
}
```

## Delete an MCP server in a customer workspace

Deletes an MCP server in a customer workspace.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:handle
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| handle | **string** _required_ | MCP server handle. You can find the `mcp_server_handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |

#### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:handle' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

Returns `204 No Content` on success.

## Renew MCP server authentication token in a customer workspace

Generates a new authentication token for an MCP server in a customer workspace and invalidates the previous token. Use this endpoint to rotate credentials after a security event or as part of a regular credential rotation policy.

> **LEGACY ENDPOINT**
> 
> This endpoint applies to servers using the legacy `token` auth type, which carry a single server-level token. Use [Refresh a hashed token in a customer workspace](#refresh-a-hashed-token-in-a-customer-workspace) for `hashed_token` servers, which operates on an individual, named token profile.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:handle/token_renew
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| handle | **string** _required_ | MCP server handle. You can find the `handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:handle/token_renew' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

Returns the updated MCP server object with the new `mcp_url` containing the refreshed token.

```json
{
    "data": {
        "id": 1001,
        "name": "Sales & CRM Tools MCP Server",
        "description": "Provides CRM, deal management, and pipeline tools for AI clients",
        "asset_type": "api_collection",
        "logo_url": "https://www.workato.com/images/mcp-server-logo.png",
        "tools_count": 5,
        "mcp_url": "https://www.workato.com/mcp/servers/sales-tools-mcp-server?token=newtoken789",
        "auth_type": "token",
        "idp_user_group_ids": [],
        "api_collection": null,
        "created_at": "2025-10-15T13:41:05.207-07:00",
        "updated_at": "2025-10-18T08:00:00.000-07:00"
    }
}
```

## MCP hashed tokens

MCP hashed token endpoints manage individual, named token profiles for MCP servers with `hashed_token` as the `auth_type` in a customer workspace. This extends the legacy `token` authentication type, which supports a single server-level token through [token renewal](#renew-mcp-server-authentication-token-in-a-customer-workspace). `hashed_token` supports up to 50 named, independently revocable token profiles per server.

### Create a hashed token in a customer workspace

Creates a token profile for a server with `hashed_token` as the `auth_type` in a customer workspace.

> MCP servers support a maximum of 50 active hashed tokens.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/tokens
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| mcp\_server\_handle | **string** _required_ | MCP server handle. You can find the `mcp_server_handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Token profile name. Must be non-blank, no longer than 100 characters, and case-insensitively unique among the server's active tokens. |

#### Additional constraints

> This endpoint is only available for `hashed_token` servers. Calling this endpoint on a `token` or `workato_idp` server returns an error.

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/tokens' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name"
          }'
```

</api-code>

#### Sample response

Returns `201 Created` with the token profile at the response root rather than nested under `data`.

```json
{
    "id": 731,
    "name": "Production token",
    "auth_type": "hashed_token",
    "created_at": "2026-07-10T10:00:00.000Z",
    "created_by": {
        "id": 42,
        "full_name": "Example User"
    },
    "token_first_symbols": "abc",
    "token_last_symbols": "wxyz",
    "plain_token": "<plain_token>"
}
```

> **PLAIN TOKEN IS SHOWN ONCE**
> 
> `plain_token` is returned only at creation and can't be retrieved later. Store the token securely. You can use the [refresh the token](#refresh-a-hashed-token-in-a-customer-workspace) endpoint to generate a new token if needed.

### Delete a hashed token in a customer workspace

Deleting a hashed token doesn't remove it from the database. The hashed token profile is marked as inactive. The token immediately stops working and can no longer authenticate MCP requests.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/tokens/:id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| mcp\_server\_handle | **string** _required_ | MCP server handle. You can find the `mcp_server_handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |
| id | **number** _required_ | Token profile ID. |

#### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/tokens/:id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

Returns `200 OK` with an empty response body.

This endpoint is available only for `hashed_token` servers. Deleted profiles no longer appear in the server's `mcp_profiles` array.

### Refresh a hashed token in a customer workspace

Invalidates the current token value for a profile and returns a fresh plain token.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/tokens/:id/refresh
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| mcp\_server\_handle | **string** _required_ | MCP server handle. You can find the `mcp_server_handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |
| id | **number** _required_ | Active token profile ID. |

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/tokens/:id/refresh' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

Returns `200 OK`. The response has the same root-level shape as [token creation](#create-a-hashed-token-in-a-customer-workspace-sample-response) and contains the `plain_token`, `token_first_symbols`, and `token_last_symbols`.

```json
{
    "id": 731,
    "name": "Production token",
    "auth_type": "hashed_token",
    "created_at": "2026-07-10T10:00:00.000Z",
    "created_by": {
        "id": 42,
        "full_name": "Example User"
    },
    "token_first_symbols": "def",
    "token_last_symbols": "uvwx",
    "plain_token": "<new_plain_token>"
}
```

This endpoint is available only for `hashed_token` servers. The returned `plain_token` is exposed only in this response. Store the token securely. You can't retrieve it later.

## Assign tools to an MCP server in a customer workspace

Assigns one or more tools to an MCP server in a customer workspace. Tools already assigned to the server aren't duplicated.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:handle/assign_tools
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| handle | **string** _required_ | MCP server handle. You can find the `handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| tools | **array of objects** _required_ | Tools to assign. Each object requires `trigger_application` (string) and `id` (string). |

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:handle/assign_tools' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "tools": [
              {
                "trigger_application": ":trigger_application_1",
                "id": ":id_1"
              },
              {
                "trigger_application": ":trigger_application_2",
                "id": ":id_2"
              }
            ]
          }'
```

</api-code>

#### Sample response

Returns the updated MCP server object.

```json
{
    "data": {
        "id": 1001,
        "name": "Sales & CRM Tools MCP Server",
        "description": "Provides CRM, deal management, and pipeline tools for AI clients",
        "asset_type": "api_collection",
        "logo_url": "https://www.workato.com/images/mcp-server-logo.png",
        "tools_count": 7,
        "mcp_url": "https://www.workato.com/mcp/servers/sales-tools-mcp-server?token=newtoken789",
        "auth_type": "hashed_token",
        "idp_user_group_ids": [],
        "api_collection": null,
        "created_at": "2025-10-15T13:41:05.207-07:00",
        "updated_at": "2025-10-18T09:15:22.000-07:00"
    }
}
```

## Assign user groups to an MCP server in a customer workspace

Assigns identity provider user groups to an MCP server in a customer workspace. Only applicable when the server's `auth_type` is `workato_idp`.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:handle/assign_user_groups
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| handle | **string** _required_ | MCP server handle. You can find the `handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| idp\_user\_group\_ids | **array of strings** _required_ | IDs of the user groups to add. |

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:handle/assign_user_groups' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "idp_user_group_ids": [":idp_user_group_ids_1", ":idp_user_group_ids_2"]
          }'
```

</api-code>

#### Sample response

Returns the updated MCP server object with the assigned user group IDs reflected in `idp_user_group_ids`.

```json
{
    "data": {
        "id": 1002,
        "name": "HR Automation Server",
        "description": "HR onboarding and employee management tools",
        "asset_type": "project_asset",
        "logo_url": "https://www.workato.com/images/mcp-server-logo.png",
        "tools_count": 3,
        "mcp_url": "https://www.workato.com/mcp/servers/hr-automation-server?token=hrtoken456",
        "auth_type": "workato_idp",
        "idp_user_group_ids": ["group-abc123", "group-def456"],
        "api_collection": null,
        "created_at": "2025-10-15T10:00:00.000-07:00",
        "updated_at": "2025-10-18T10:30:00.000-07:00"
    }
}
```

## Remove user groups from an MCP server in a customer workspace

Removes identity provider user groups from an MCP server in a customer workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:handle/remove_user_groups
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| handle | **string** _required_ | MCP server handle. You can find the `handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| idp\_user\_group\_ids | **array of strings** _required_ | IDs of the user groups to remove. |

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:handle/remove_user_groups' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "idp_user_group_ids": [":idp_user_group_ids"]
          }'
```

</api-code>

#### Sample response

Returns the updated MCP server object with the specified groups removed from `idp_user_group_ids`.

```json
{
    "data": {
        "id": 1002,
        "name": "HR Automation Server",
        "description": "HR onboarding and employee management tools",
        "asset_type": "project_asset",
        "logo_url": "https://www.workato.com/images/mcp-server-logo.png",
        "tools_count": 3,
        "mcp_url": "https://www.workato.com/mcp/servers/hr-automation-server?token=hrtoken456",
        "auth_type": "workato_idp",
        "idp_user_group_ids": ["group-def456"],
        "api_collection": null,
        "created_at": "2025-10-15T10:00:00.000-07:00",
        "updated_at": "2025-10-18T11:00:00.000-07:00"
    }
}
```

## Move MCP server to a different folder in a customer workspace

Moves an MCP server to a specified folder in a customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:handle/update_folder
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| handle | **string** _required_ | MCP server handle. You can find the `handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| folder\_id | **number** _required_ | Target folder ID. |

#### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:handle/update_folder' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "folder_id": :folder_id
          }'
```

</api-code>

#### Sample response

Returns the updated MCP server object reflecting the new folder.

```json
{
    "data": {
        "id": 1002,
        "name": "HR Automation Server",
        "description": "HR onboarding and employee management tools",
        "asset_type": "project_asset",
        "logo_url": "https://www.workato.com/images/mcp-server-logo.png",
        "tools_count": 3,
        "mcp_url": "https://www.workato.com/mcp/servers/hr-automation-server?token=hrtoken456",
        "auth_type": "workato_idp",
        "idp_user_group_ids": ["group-def456"],
        "api_collection": null,
        "created_at": "2025-10-15T10:00:00.000-07:00",
        "updated_at": "2025-10-18T12:00:00.000-07:00"
    }
}
```

## Get server policy configuration in a customer workspace

Retrieves the security policy configuration for an MCP server, including rate limits, usage limits, Classless Inter-Domain Routing (CIDR), and IP addresses.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/server_policies
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| mcp\_server\_handle | **string** _required_ | MCP server handle. You can find the `mcp_server_handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/server_policies' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

```json
{
    "id": 501,
    "mcp_server_id": 1001,
    "rate_limits": {
        "per_minute": 60
    },
    "quota_limits": {
        "per_day": 10000
    },
    "ip_allow_list": ["203.0.113.0/24"],
    "ip_deny_list": [],
    "created_at": "2025-10-15T13:41:05.207-07:00",
    "updated_at": "2025-10-16T09:22:11.100-07:00"
}
```

## Update server policy configuration in a customer workspace

Updates the security policy configuration for an MCP server in a customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/server_policies
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| mcp\_server\_handle | **string** _required_ | MCP server handle. You can find the `mcp_server_handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| mcp\_server\_policy | **object** _required_ | Policy configuration object. |
| mcp\_server\_policy\[rate\_limits\] | **object** _optional_ | Rate limit configurations. |
| mcp\_server\_policy\[quota\_limits\] | **object** _optional_ | Quota limits configurations. |
| mcp\_server\_policy\[ip\_allow\_list\] | **array of strings** _optional_ | IP addresses or CIDR ranges to allow. |
| mcp\_server\_policy\[ip\_deny\_list\] | **array of strings** _optional_ | IP addresses or CIDR ranges to deny. |

#### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/server_policies' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "mcp_server_policy": {
              "rate_limits": { "per_minute": :per_minute },
              "quota_limits": { "per_day": :per_day },
              "ip_allow_list": [":ip_allow_list_1", ":ip_allow_list_2"],
              "ip_deny_list": []
            }
          }'
```

</api-code>

### Sample response

```json
{
    "id": 501,
    "mcp_server_id": 1001,
    "rate_limits": {
        "per_minute": 30
    },
    "quota_limits": {
        "per_day": 5000
    },
    "ip_allow_list": ["203.0.113.0/24", "198.51.100.42"],
    "ip_deny_list": [],
    "created_at": "2025-10-15T13:41:05.207-07:00",
    "updated_at": "2025-10-18T14:00:00.000-07:00"
}
```

## List tools for an MCP server in a customer workspace

Returns a paginated list of tools assigned to an MCP server in a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/tools
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| mcp\_server\_handle | **string** _required_ | MCP server handle. You can find the `mcp_server_handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| vua\_required | **boolean** _optional_ | Filter by whether VUA (Verified User Authentication) is required. |
| search | **string** _optional_ | Search term to filter tools by name. |
| page | **number** _optional_ | Page number. Defaults to 1. |
| per\_page | **number** _optional_ | Number of items per page. Defaults to 100. Maximum is 100. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/tools' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

```json
{
    "data": [
        {
            "id": 3001,
            "name": "Create Salesforce Lead",
            "description": "Creates a new lead record in Salesforce CRM",
            "trigger_application": "workato_api_platform",
            "action_applications": ["salesforce"],
            "flow_id": 66870001,
            "vua_required": false
        },
        {
            "id": 3002,
            "name": "Send Deal Notification",
            "description": "Sends a Slack notification when a deal stage changes",
            "trigger_application": "workato_recipe_function",
            "action_applications": ["slack"],
            "flow_id": 66870002,
            "vua_required": true
        }
    ],
    "count": 2,
    "page": 1,
    "per_page": 100
}
```

## Update tool description in a customer workspace

Updates the description of a tool within an MCP server in a customer workspace. This modifies the description shown to AI clients without affecting the underlying recipe or API endpoint.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/tools/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| mcp\_server\_handle | **string** _required_ | MCP server handle. You can find the `mcp_server_handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |
| id | **number** _required_ | Tool ID. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| description | **string** _optional_ | New description for the tool. |

#### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/tools/:id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "description": ":description"
          }'
```

</api-code>

#### Sample response

```json
{
    "id": 3001,
    "name": "Create Salesforce Lead",
    "description": "Creates a new lead record in Salesforce CRM with name, email, and company details",
    "trigger_application": "workato_api_platform",
    "action_applications": ["salesforce"],
    "flow_id": 66870001,
    "vua_required": false
}
```

## Delete a tool in a customer workspace

Removes a tool from an MCP server in a customer workspace.

> **API ENDPOINTS CAN'T BE DELETED**
> 
> Only tools backed by recipe functions or Genie agents can be deleted. Attempting to delete an API endpoint tool returns a `400 Bad Request` error.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/tools/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| mcp\_server\_handle | **string** _required_ | MCP server handle. You can find the `mcp_server_handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |
| id | **number** _required_ | Tool ID. |

#### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/tools/:id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Sample response

Returns `204 No Content` on success.

## List identity provider user groups in a customer workspace

Returns a paginated list of identity provider user groups available in a customer workspace. Use the group IDs from this response when assigning access to MCP servers that use `workato_idp` authentication.

> **THIS ISN'T THE COLLABORATOR GROUPS RESOURCE**
> 
> The user groups on this endpoint aren't RBAC [collaborator groups](/en/oem/oem-api/collaborator-groups). Use the `/api/v2/managed_users/:managed_user_id/user_groups` endpoints to manage collaborator groups.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/user_groups
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page | **number** _optional_ | Page number. Defaults to 1. |
| per\_page | **number** _optional_ | Number of items per page. Defaults to 100. Maximum is 100. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/user_groups' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

```json
{
    "data": [
        {
            "id": "group-abc123",
            "name": "Sales Team",
            "users_count": 24,
            "created_at": "2025-01-10T08:00:00.000Z",
            "updated_at": "2025-09-15T12:30:00.000Z"
        },
        {
            "id": "group-def456",
            "name": "HR Admins",
            "users_count": 6,
            "created_at": "2025-01-10T08:00:00.000Z",
            "updated_at": "2025-08-20T10:00:00.000Z"
        }
    ],
    "count": 2,
    "page": 1,
    "per_page": 100
}
```

## MCP access assignments

MCP access assignments control tool-level role-based access control (RBAC) for an MCP server in a customer workspace. Each assignment grants one identity provider user or user group access to either all tools on the server or a specific set of tools.

> **REQUIREMENTS AND LIMITATIONS**
> 
> - Access assignments work only with MCP servers that use `workato_idp` as the `auth_type`.
> - Access assignments don't work with `api_collection`\-based MCP servers.
> - An identity can have only one access assignment per server.

### List MCP access assignments in a customer workspace

Returns a paginated list of MCP server access assignments for users or user groups in a customer workspace.

**Required privilege:** `oem_mcp_access_assignments.index`.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/access_assignments
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| mcp\_server\_handle | **string** _required_ | MCP server handle. You can find the `mcp_server_handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| identity\_type | **string** _required_ | Identity type. Accepted values: `user`, `user_group`. |
| search | **string** _optional_ | Search identity names. |
| order | **string** _optional_ | Sort by identity name. Accepted values: `asc`, `desc`. Defaults to `asc`. |
| page | **integer** _optional_ | Positive page number. Defaults to 1. |
| per\_page | **integer** _optional_ | Number of items per page, from 1 to 100. Defaults to 100. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/mcps-7Hk9pQ2r-aB3-1a/access_assignments?identity_type=user_group&page=1&per_page=100' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

Returns `200 OK`.

```json
{
    "data": [
        {
            "id": "mcpsaa-7Hk9pQ2s-aB3cD4-1a",
            "idp_user_id": null,
            "idp_user_group_id": "group-abc123",
            "all_tools": false,
            "tool_ids": [3001, 3002],
            "created_at": "2026-10-09T10:00:00.000Z",
            "updated_at": "2026-10-09T10:00:00.000Z"
        },
        {
            "id": "mcpsaa-7Hk9pQ2u-jK7mN8-1a",
            "idp_user_id": null,
            "idp_user_group_id": "group-def456",
            "all_tools": true,
            "tool_ids": [],
            "created_at": "2026-10-09T10:00:00.000Z",
            "updated_at": "2026-10-09T10:00:00.000Z"
        }
    ],
    "count": 2,
    "page": 1,
    "per_page": 100
}
```

The example lists group assignments. Each assignment has a string `idp_user_id` and a null `idp_user_group_id` when `identity_type` is `user`. Both identity fields are present by default.

### Create an MCP access assignment in a customer workspace

Creates one access assignment for a user or user group on an MCP server in a customer workspace.

**Required privilege:** `oem_mcp_access_assignments.create`.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/access_assignments
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| mcp\_server\_handle | **string** _required_ | MCP server handle. You can find the `mcp_server_handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| idp\_user\_id | **string** _conditional_ | Non-empty identity provider user ID. Supply exactly one of `idp_user_id` or `idp_user_group_id`. |
| idp\_user\_group\_id | **string** _conditional_ | Non-empty identity provider user group ID. Supply exactly one of `idp_user_id` or `idp_user_group_id`. |
| all\_tools | **boolean** _optional_ | Grant access to all tools on the server. Defaults to `false`. |
| tool\_ids | **array of integers** _conditional_ | Required and non-empty when `all_tools` is `false` or omitted. When `all_tools` is `true`, omit this field or send an empty array. Every ID must belong to this server. Use the [List tools](#list-tools-for-an-mcp-server-in-a-customer-workspace) endpoint to retrieve tool IDs. |

#### Additional constraints

- The identity must be available in the target environment.
- An identity can have only one assignment per server.
- Tool IDs refer to the server's MCP tool records, not recipe IDs or API endpoint IDs.

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/mcps-7Hk9pQ2r-aB3-1a/access_assignments' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "idp_user_group_id": "group-abc123",
            "all_tools": false,
            "tool_ids": [3001, 3002]
          }'
```

</api-code>

Use the following request body to grant a user access to all tools:

```json
{
    "idp_user_id": "user-abc123",
    "all_tools": true
}
```

#### Sample response

Returns `201 Created`.

```json
{
    "data": {
        "id": "mcpsaa-7Hk9pQ2s-aB3cD4-1a",
        "idp_user_id": null,
        "idp_user_group_id": "group-abc123",
        "all_tools": false,
        "tool_ids": [3001, 3002],
        "created_at": "2026-10-09T10:00:00.000Z",
        "updated_at": "2026-10-09T10:00:00.000Z"
    }
}
```

The server generates the assignment ID. Tool IDs are deduplicated and sorted.

### Get an MCP access assignment in a customer workspace

Retrieves an access assignment belonging to an MCP server in a customer workspace.

**Required privilege:** `oem_mcp_access_assignments.show`.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/access_assignments/:id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| mcp\_server\_handle | **string** _required_ | MCP server handle. You can find the `mcp_server_handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |
| id | **string** _required_ | Access assignment ID belonging to this server. |

This endpoint doesn't accept query or body parameters.

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/mcps-7Hk9pQ2r-aB3-1a/access_assignments/mcpsaa-7Hk9pQ2s-aB3cD4-1a' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

Returns `200 OK`.

```json
{
    "data": {
        "id": "mcpsaa-7Hk9pQ2s-aB3cD4-1a",
        "idp_user_id": null,
        "idp_user_group_id": "group-abc123",
        "all_tools": false,
        "tool_ids": [3001, 3002],
        "created_at": "2026-10-09T10:00:00.000Z",
        "updated_at": "2026-10-09T10:00:00.000Z"
    }
}
```

`idp_user_id` contains the user ID and `idp_user_group_id` is `null` for user assignments. Both fields are present by default. Assignments that grant all tools have `all_tools: true` and `tool_ids: []`.

### Update an MCP access assignment in a customer workspace

Replaces the tool access scope of an existing MCP server access assignment in a customer workspace.

**Required privilege:** `oem_mcp_access_assignments.update`.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/access_assignments/:id
```

</api-code>

This path also accepts `PATCH` with the same replacement behavior.

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| mcp\_server\_handle | **string** _required_ | MCP server handle. You can find the `mcp_server_handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |
| id | **string** _required_ | Access assignment ID belonging to this server. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| all\_tools | **boolean** _optional_ | Grant access to all tools on the server. Defaults to `false` when omitted. |
| tool\_ids | **array of integers** _conditional_ | Required and non-empty when `all_tools` is `false` or omitted. When `all_tools` is `true`, omit this field or send an empty array. Every ID must belong to this server. |

> **UPDATES REPLACE THE ENTIRE TOOL SCOPE**
> 
> Provide at least one of `all_tools` or `tool_ids`. Omitted fields aren't retained. An omitted `all_tools` defaults to `false`, and an omitted `tool_ids` defaults to an empty array. You can't change the identity on an existing assignment.

#### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/mcps-7Hk9pQ2r-aB3-1a/access_assignments/mcpsaa-7Hk9pQ2s-aB3cD4-1a' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "all_tools": false,
            "tool_ids": [3001]
          }'
```

</api-code>

To grant all tools, send `{"all_tools": true}`. The response then contains `all_tools: true` and `tool_ids: []`.

#### Sample response

Returns `200 OK`.

```json
{
    "data": {
        "id": "mcpsaa-7Hk9pQ2s-aB3cD4-1a",
        "idp_user_id": null,
        "idp_user_group_id": "group-abc123",
        "all_tools": false,
        "tool_ids": [3001],
        "created_at": "2026-10-09T10:00:00.000Z",
        "updated_at": "2026-10-09T11:00:00.000Z"
    }
}
```

The assignment identity and creation timestamp don't change.

### Delete an MCP access assignment in a customer workspace

Deletes a user's or user group's access assignment from an MCP server in a customer workspace.

**Required privilege:** `oem_mcp_access_assignments.destroy`.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/:mcp_server_handle/access_assignments/:id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| mcp\_server\_handle | **string** _required_ | MCP server handle. You can find the `mcp_server_handle` in the URL when you go to **AI Hub > Enterprise MCP > Custom servers** and select the MCP server you plan to use. For example, your MCP server handle is `mcps-AxbxNxNz-wsB-SM` if the URL is `https://app.workato.com/mcp/mcps-AxbxNxNz-wsB-SM/overview`. |
| id | **string** _required_ | Access assignment ID belonging to this server. |

This endpoint doesn't accept query or body parameters.

#### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/mcp_servers/mcps-7Hk9pQ2r-aB3-1a/access_assignments/mcpsaa-7Hk9pQ2s-aB3cD4-1a' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

Returns `204 No Content` on success, with an empty response body.

---
