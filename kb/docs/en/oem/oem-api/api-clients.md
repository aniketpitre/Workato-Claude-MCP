---
url: 'https://docs.workato.com/en/oem/oem-api/api-clients.md'
description: >-
  Reference for Workato Embedded API endpoints to create, list, update, delete,
  and rotate tokens for Developer API clients and roles.
---

# Embedded API - API clients

The following endpoints allow you to manage API clients and client roles within a customer workspace. Use these endpoints to programmatically create new API clients for your customers or rotate API tokens regularly.

## Rate limits

API client resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| GET | List Developer API Clients: [/api/v2/managed\_users/:managed\_user\_id /developer\_api\_clients](/en/oem/oem-api/api-clients.html#list-developer-api-clients) | 1,000 requests per minute |
| GET | List Developer API Client roles: [/api/v2/managed\_users/:managed\_user\_id /developer\_api\_client\_roles](/en/oem/oem-api/api-clients.html#list-developer-api-client-roles) | 1,000 requests per minute |
| All | All other [API Client](/en/oem/oem-api/api-clients.html) endpoints | 60 requests per minute |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/v2/managed\_users/:managed\_user\_id/developer\_api\_clients](#list-developer-api-clients) | List Developer API clients in a customer workspace. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/developer\_api\_clients](#create-developer-api-client) | Create a Developer API client in a customer workspace. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/developer\_api\_clients/:id](#get-developer-api-client-by-id) | Get a Developer API client by ID in a customer workspace. |
| PUT | [/api/v2/managed\_users/:managed\_user\_id/developer\_api\_clients/:id](#update-developer-api-client) | Update a Developer API client in a customer workspace. |
| DELETE | [/api/v2/managed\_users/:managed\_user\_id/developer\_api\_clients/:id](#delete-developer-api-client) | Delete a Developer API client in a customer workspace. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/developer\_api\_clients/:id/regenerate](#regenerate-developer-api-client-token) | Regenerate a Developer API client token in a customer workspace. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/developer\_api\_client\_roles](#list-developer-api-client-roles) | List Developer API client roles in a customer workspace. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/developer\_api\_client\_roles/:id/copy](#copy-developer-api-client-role) | Copy a Developer API client role in a customer workspace. |

## List Developer API clients

List all Developer API clients in a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/developer_api_clients
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page | **integer** _optional_ | Page number of the API clients to fetch. Defaults to `1`. |
| per\_page | **integer** _optional_ | Number of API clients to return in a single page. Defaults to `100`. Max is `100`. |

### Sample request

<api-code>

```shell
curl -X GET "https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/developer_api_clients" \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "result": {
        "count": 1,
        "items": [
            {
                "id": 40947,
                "name": "Test",
                "api_privilege_group_id": 26779,
                "created_at": "2023-02-22T01:55:35.739-08:00",
                "updated_at": "2023-02-28T01:23:18.046-08:00",
                "all_folders": false,
                "folder_ids": [
                    26138,
                    26136
                ],
                "environment_name": "Development",
                "environment_id": 3218,
                "ip_allow_list": "192.0.2.10,198.51.100.5",
                "token": {
                    "updated_at": "2023-02-22T09:55:36.427Z"
                }
            }
        ]
    }
}
```

## Create a Developer API client

Create a Developer API client in a customer workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/developer_api_clients
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Name of the API client |
| api\_privilege\_group\_id | **integer** _required_ | ID of the API client role. |
| all\_folders | **boolean** _required_ | Indicates if the client has access to all folders. Must be `true`, `false`, `1`, or `0`. |
| folder\_ids | **array** _conditional_ | List of folder IDs. Required if `all_folders` is `false`. |
| environment\_name | **string** _conditional_ | Name of the environment. Required if your workspace has environments enabled. |
| ip\_allow\_list | **string** _optional_ | Array of IP addresses allowed to access the API client. Defaults to all IPs if not specified. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/developer_api_clients \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "api_privilege_group_id": :api_privilege_group_id_value,
            "environment_name": ":environment_name",
            "all_folders": :all_folders_value,
            "ip_allow_list": ":ip_allow_list"
          }'
```

</api-code>

### Response

```json
{
    "result": {
        "id": 40948,
        "name": "Test Client",
        "api_privilege_group_id": 26779,
        "created_at": "2023-02-28T02:09:07.255-08:00",
        "updated_at": "2023-02-28T02:09:07.586-08:00",
        "all_folders": true,
        "environment_name": "Development",
        "environment_id": 3218,
        "ip_allow_list": "192.0.2.10,198.51.100.5",
        "token": {
            "updated_at": "2023-02-28T10:09:07.579Z",
            "value": "wrkaus-eyJhbGciOiJSUz..."
        }
    }
}
```

## Get a Developer API client by ID

Retrieve a Developer API client in a customer workspace by its ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/developer_api_clients/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| id | **integer** _required_ | ID of the API Client. |

### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/developer_api_clients/:id \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "result": {
        "id": 40948,
        "name": "Test Client",
        "api_privilege_group_id": 26779,
        "created_at": "2023-02-28T02:09:07.255-08:00",
        "updated_at": "2023-02-28T02:09:07.586-08:00",
        "all_folders": false,
        "folder_ids": [26138, 26136],
        "environment_name": "Development",
        "environment_id": 3218,
        "token": {
            "updated_at": "2023-02-28T10:09:07.579Z"
        }
    }
}
```

## Update a Developer API client

Update a Developer API client in a customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/developer_api_clients/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| id | **integer** _required_ | ID of the API Client. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Updated name of the API client |
| api\_privilege\_group\_id | **integer** _optional_ | Updated API client role ID |
| all\_folders | **boolean** _optional_ | Indicates whether the client has access to all folders. Must be `true`, `false`, `1`, or `0`. |
| folder\_ids | **array** _conditional_ | Array of folder IDs. Required if `all_folders` is false. |
| environment\_name | **string** _conditional_ | Name of the environment. Required if your workspace has environments enabled. |
| ip\_allow\_list | **string** _optional_ | Array of IP addresses allowed to access the API client. Defaults to all IPs if not specified. |

### Sample request

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/developer_api_clients/:id \
      -H 'Authorization: Bearer <api_token>'  \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "api_privilege_group_id": :api_privilege_group_id_value,
            "environment_name": ":environment_name",
            "all_folders": :all_folders_value,
            "ip_allow_list": ":ip_allow_list"
          }'
```

</api-code>

### Response

```json
{
    "result": {
        "id": 40948,
        "name": "Test Client",
        "api_privilege_group_id": 26779,
        "created_at": "2023-02-28T02:09:07.255-08:00",
        "updated_at": "2023-02-28T02:09:07.586-08:00",
        "all_folders": true,
        "environment_name": "Development",
        "environment_id": 3218,
        "ip_allow_list": "192.0.2.10,198.51.100.5",
        "token": {
            "updated_at": "2023-02-28T10:09:07.579Z"
        },
        "user": {
            "id": 3218,
            "name": "Workato Customer Success test"
        }
    }
}
```

## Delete a Developer API client

Delete a Developer API client in a customer workspace.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/developer_api_clients/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| id | **integer** _required_ | ID of the API Client. |

### Sample request

<api-code>

```shell
curl  -X DELETE https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/developer_api_clients/:id \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "result": "success"
}
```

## Regenerate a Developer API client token

Regenerates the API token for an API client in a customer workspace. This invalidates the previous API token.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/developer_api_clients/:id/regenerate
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| id | **integer** _required_ | ID of the API Client. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/developer_api_clients/:id/regenerate \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "result": {
        "id": 40948,
        "name": "Test new API client",
        "api_privilege_group_id": 26779,
        "created_at": "2023-01-29T22:30:12.930-08:00",
        "updated_at": "2023-02-28T02:19:16.542-08:00",
        "all_folders": true,
        "environment_name": "Development",
        "environment_id": 3218,
        "token": {
            "updated_at": "2023-02-28T10:19:16.530Z",
            "value": "wrkaus-eyJhbGc..."
        }
    }
}
```

## List Developer API client roles

Returns a list of Developer API client roles in a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/developer_api_client_roles
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page | **integer** _optional_ | Page number. Defaults to 1. |
| per\_page | **integer** _optional_ | Page size. Defaults to 100. The maximum is 100. |

### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/developer_api_client_roles \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "data": [
        {
            "id": 416281,
            "name": "Read-only API client",
            "created_at": "2025-09-10T09:17:48.292-07:00",
            "updated_at": "2025-09-10T09:17:48.292-07:00"
        },
        {
            "id": 416282,
            "name": "Full-access API client",
            "created_at": "2025-09-10T09:17:54.676-07:00",
            "updated_at": "2025-09-10T09:18:02.740-07:00"
        }
    ],
    "count": 2,
    "page": 1,
    "per_page": 100
}
```

## Copy a Developer API client role

Creates a copy of an Embedded customer's Developer API client role.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/developer_api_client_roles/:id/copy
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| id | **integer** _required_ | The ID of the Developer API client role to copy. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | The name assigned to the copied Developer API client role. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/developer_api_client_roles/:id/copy \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name"
          }'
```

</api-code>

### Response

```json
{
    "data": {
        "id": 416283,
        "name": "Read-only API client (copy)",
        "created_at": "2025-09-10T09:21:14.459-07:00",
        "updated_at": "2025-09-10T09:21:14.459-07:00"
    }
}
```

---
